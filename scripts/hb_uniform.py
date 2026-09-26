"""Is there a UNIFORM certificate for H-beta (note 34)?  The (P2)/(PPE) multipliers are forced to depend only on a local feature of
the pair couple (hb_features.feature), with parameters theta shared by all skeletons of a sample; all other multipliers are free per
skeleton.  Dual (certificate) LP, for each skeleton s:
   p_c >= (A^T y_s)_c, p_c >= 0 (every column c),   u_r >= y_r rhs_r, u_r >= 0 ('<=' rows),   y_s^T b - sum p - sum u >= 1.
Feasible  <=>  one feature-based W works for every skeleton of the sample (then test it on all 552 classes).
Usage: python hb_uniform.py <sample size> <seed>"""
import sys, time, random, json
from collections import defaultdict
import numpy as np
import highspy
from scipy.sparse import coo_matrix
sys.path.insert(0, "scripts")
import hb_pairlevel as H, hb_colmodel as CM, hb_colmodel_all as A, hb_features as F
PAIRS = H.PAIRS; PI = {R: t for t, R in enumerate(PAIRS)}

def build(sample):
    feats = {}; blocks = []
    for key in sample:
        orbits = [tuple(z) for z in key]
        cm = CM.ColModel(orbits, True)
        blocks.append((orbits, cm))
        for r in cm.rows:
            nm = r[3]
            if nm[0] == 'D': f = F.feature(nm[1], nm[1], orbits)
            elif nm[0] == 'P2': f = F.feature(nm[1], nm[2], orbits)
            else: continue
            feats.setdefault(f, len(feats))
    nth = len(feats)
    # variable layout: theta (nth) | per skeleton: y_free (rows not P2/D), p (cols), u (le rows)
    var = nth; lay = []
    for orbits, cm in blocks:
        free = [r for r, row in enumerate(cm.rows) if row[3][0] not in ('D', 'P2')]
        le = [r for r, row in enumerate(cm.rows) if row[2] == 'le']
        d = {'yfree': {r: var + t for t, r in enumerate(free)}}; var += len(free)
        d['p'] = var; var += len(cm.cols)
        d['u'] = {r: var + t for t, r in enumerate(le)}; var += len(le)
        lay.append(d)
    ri, ci, vv = [], [], []; lo, hi = [], []; row = 0
    for (orbits, cm), d in zip(blocks, lay):
        def yvar(r):
            nm = cm.rows[r][3]
            if nm[0] == 'D': return feats[F.feature(nm[1], nm[1], orbits)]
            if nm[0] == 'P2': return feats[F.feature(nm[1], nm[2], orbits)]
            return d['yfree'][r]
        # column constraints: sum_r y_r A_rc - p_c <= 0
        colterms = defaultdict(lambda: defaultdict(float))
        for r, (terms, rhs, kind, name) in enumerate(cm.rows):
            yv = yvar(r)
            for c, v in terms: colterms[c][yv] += v
        for c in range(len(cm.cols)):
            for yv, v in colterms[c].items(): ri.append(row); ci.append(yv); vv.append(v)
            ri.append(row); ci.append(d['p'] + c); vv.append(-1.0); lo.append(-np.inf); hi.append(0.0); row += 1
        for r, uv in d['u'].items():       # y_r rhs_r - u_r <= 0
            ri.append(row); ci.append(yvar(r)); vv.append(float(cm.rows[r][1])); ri.append(row); ci.append(uv); vv.append(-1.0)
            lo.append(-np.inf); hi.append(0.0); row += 1
        # y^T b - sum p - sum u >= 1
        bterm = defaultdict(float)
        for r, (terms, rhs, kind, name) in enumerate(cm.rows): bterm[yvar(r)] += rhs
        for yv, v in bterm.items(): ri.append(row); ci.append(yv); vv.append(v)
        for c in range(len(cm.cols)): ri.append(row); ci.append(d['p'] + c); vv.append(-1.0)
        for uv in d['u'].values(): ri.append(row); ci.append(uv); vv.append(-1.0)
        lo.append(1.0); hi.append(np.inf); row += 1
    M = coo_matrix((vv, (ri, ci)), shape=(row, var)).tocsc()
    lp = highspy.HighsLp(); lp.num_col_ = var; lp.num_row_ = row
    lp.col_cost_ = np.zeros(var)
    clo = np.full(var, -50.0); chi = np.full(var, 50.0)
    for d in lay:
        for c in range(d['p'], d['p'] + len(blocks[0][1].cols) + 100000):
            pass
    # p, u >= 0
    for (orbits, cm), d in zip(blocks, lay):
        clo[d['p']:d['p'] + len(cm.cols)] = 0.0; chi[d['p']:d['p'] + len(cm.cols)] = np.inf
        for uv in d['u'].values(): clo[uv] = 0.0; chi[uv] = np.inf
    lp.col_lower_ = clo; lp.col_upper_ = chi
    lp.row_lower_ = np.array(lo); lp.row_upper_ = np.array(hi)
    lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_ = M.indptr; lp.a_matrix_.index_ = M.indices; lp.a_matrix_.value_ = M.data
    h = highspy.Highs(); h.setOptionValue("output_flag", False); h.passModel(lp); h.run()
    st = h.getModelStatus()
    theta = None
    if st == highspy.HighsModelStatus.kOptimal:
        x = np.array(h.getSolution().col_value); theta = {f: x[t] for f, t in feats.items()}
    return h.modelStatusToString(st), theta, feats

if __name__ == "__main__":
    size, seed = int(sys.argv[1]), int(sys.argv[2])
    cls, mult = A.classes()
    rng = random.Random(seed)
    sample = [cls[0]] + rng.sample(cls[1:], size - 1)
    t0 = time.time()
    st, theta, feats = build(sample)
    print("sample", size, "| features", len(feats), "| joint dual LP:", st, "%.0fs" % (time.time() - t0))
    if theta:
        for f, v in sorted(theta.items(), key=str): print("  ", f, round(v, 3))
        json.dump({str(f): v for f, v in theta.items()}, open("logs/hb_uniform_theta_%d_%d.json" % (size, seed), "w"))
