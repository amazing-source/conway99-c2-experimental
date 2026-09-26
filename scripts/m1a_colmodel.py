"""[GENERALISED COPY for any fixed M1 skeleton: orbits are 4-tuples (i,j,k,s); cuts of size 3 and 5 always, size 4 only when
the block has exactly 6 free orbits.]  Column ("configuration") model for an H-beta skeleton -- note 32.  Idea of "structures" (their S15): a column is an orbit Z with
a choice p of its two free-cycle neighbours at its free block j and an exact local solution s of its far row.  Every value
val_Z(R) is then a CONSTANT of the column, so all pair-level identities, including the second-order (P2), are LINEAR in the column
weights x_c:
  one column per orbit                        sum_{c in Z} x_c = 1
  cycle edges symmetric                        edge(Z,Y) = edge(Y,Z),  edge(Z,Y) = sum_{c in Z, Y in p_c} x_c
  6-cycle: subtour cuts                         sum_{Z,Y in S} edge(Z,Y) <= 2(|S|-1) for S of size 3,4,5 ;  sisters <= 1 common nbr
  column sums (S)                              sum_c val_c(R) x_c = 24
  (P2) incl. diagonal (PPE)                     sum_c val_c(R) val_c(R') x_c + sum_{c: P_Zc = R} val_c(R') x_c = 16 - 4[R meets R']  (R != R')
                                                sum_c val_c(R)^2 x_c = 32
  coupling (C)                                 sum_{c: P_Zc = R} val_c(R') x_c = sum_{c: P_Zc = R'} val_c(R) x_c
Near values (proved): val(P_Z) = 0; val({i,r}) = 2[r = k] (F1); val({j,r}) = #{Y in p : P_Y = {j,r}}; typed rule: p not inside {j,k}.
Far rows: all integer solutions of (L) (block sums 4).  LP relaxation with slacks on equality rows; inequality rows are turned into
equalities with bounded slack columns, so an infeasibility certificate is a single vector y, checked EXACTLY (fractions):
for every point of the box, y^T A x lies in [LB, UB]; infeasible iff y^T b is outside.
"""
import sys, itertools, time
from fractions import Fraction
from collections import defaultdict
import numpy as np
import highspy
from scipy.sparse import csc_matrix
sys.path.insert(0, "scripts")
import hb_pairlevel as H
N = H.N; P = H.P; PAIRS = H.PAIRS

def far_solutions(blocks5, deg):
    """all {0,1,2}-weightings of the 10 pairs of blocks5 with vertex sums deg[t]"""
    prs = [P(a, b) for a, b in itertools.combinations(blocks5, 2)]
    out = []
    def rec(t, cur, rem):
        if t == len(prs):
            if all(v == 0 for v in rem.values()): out.append(dict(zip(prs, cur)))
            return
        a, b = tuple(prs[t])
        for v in (0, 1, 2):
            if rem[a] < v or rem[b] < v: break
            rem[a] -= v; rem[b] -= v; cur.append(v)
            # prune: a block whose remaining pairs cannot fill it
            rec(t + 1, cur, rem)
            cur.pop(); rem[a] += v; rem[b] += v
    rec(0, [], dict(deg))
    return out

class ColModel:
    def __init__(self, orbits, useP2=True, fixed_p=None):
        self.orbits = orbits
        pair = {z: P(z[0], z[1]) for z in orbits}; self.pair = pair
        cols = []          # (z, p, val dict over all 21 pairs)
        for z in orbits:
            i, j, k = z[:3]
            fr = [y for y in orbits if y[1] == j and y != z and pair[y] != pair[z]]
            cand = [frozenset(pp) for pp in itertools.combinations(fr, 2)]
            if fixed_p is not None: cand = [fixed_p[z]]
            outside = [t for t in range(N) if t not in (i, j)]
            for p in cand:
                if all(pair[y] == P(j, k) for y in p): continue          # typed rule
                near = {}
                for R in PAIRS:
                    if R == pair[z]: near[R] = 0
                    elif i in R: near[R] = 2 if R == P(i, k) else 0
                    elif j in R: near[R] = sum(1 for y in p if pair[y] == R)
                deg = {t: 4 - sum(v for R, v in near.items() if t in R) for t in outside}
                if any(v < 0 for v in deg.values()): continue
                for s in far_solutions(outside, deg):
                    val = dict(near); val.update(s); cols.append((z, p, val))
        self.cols = cols
        n = len(cols)
        rows = []          # (list of (col, coef), rhs, kind)  kind 'eq' or ('le', ub_for_slack)
        byz = defaultdict(list)
        for ci, (z, p, v) in enumerate(cols): byz[z].append(ci)
        for z in orbits: rows.append(([(c, 1) for c in byz[z]], 1, 'eq', ('one', z)))
        edge = defaultdict(list)
        for ci, (z, p, v) in enumerate(cols):
            for y in p: edge[z, y].append(ci)
        for j in range(N):
            fr = [y for y in orbits if y[1] == j]
            for a, b in itertools.combinations(fr, 2):
                if pair[a] == pair[b]: continue
                rows.append(([(c, 1) for c in edge[a, b]] + [(c, -1) for c in edge[b, a]], 0, 'eq', ('sym', a, b)))
            for size in ((3, 4, 5) if len(fr) == 6 else (3, 5)):
                for S in itertools.combinations(fr, size):
                    terms = [(c, 1) for a in S for b in S if a != b for c in edge[a, b]]
                    rows.append((terms, 2 * (size - 1), 'le', ('sub', S)))
            for a, b in itertools.combinations(fr, 2):
                if pair[a] != pair[b]: continue
                terms = [(ci, 1) for ci, (z, p, v) in enumerate(cols) if z[1] == j and p == frozenset((a, b))]
                rows.append((terms, 1, 'le', ('sis', a, b)))
        for R in PAIRS:
            rows.append(([(ci, v[R]) for ci, (z, p, v) in enumerate(cols) if v[R]], 24, 'eq', ('S', R)))
        for ia, R in enumerate(PAIRS):
            for R2 in PAIRS[ia:]:
                if R == R2:
                    rows.append(([(ci, v[R] ** 2) for ci, (z, p, v) in enumerate(cols) if v[R]], 32, 'eq', ('D', R))); continue
                cp = [(ci, v[R2]) for ci, (z, p, v) in enumerate(cols) if pair[z] == R and v[R2]]
                cm = [(ci, -v[R]) for ci, (z, p, v) in enumerate(cols) if pair[z] == R2 and v[R]]
                rows.append((cp + cm, 0, 'eq', ('C', R, R2)))
                if useP2:
                    d = defaultdict(int)
                    for ci, (z, p, v) in enumerate(cols):
                        if v[R] and v[R2]: d[ci] += v[R] * v[R2]
                        if pair[z] == R and v[R2]: d[ci] += v[R2]
                    rows.append((list(d.items()), 16 - (4 if R & R2 else 0), 'eq', ('P2', R, R2)))
        self.rows = rows

    def solve(self):
        cols, rows = self.cols, self.rows
        n = len(cols); m = len(rows)
        le = [r for r in range(m) if rows[r][2] == 'le']
        # columns: x (n) | slack_le (len(le)) | s+ (m) | s- (m)
        nl = len(le); lei = {r: t for t, r in enumerate(le)}
        data = []; ri = []; ci_ = []
        for r, (terms, rhs, kind, name) in enumerate(rows):
            for c, v in terms: ri.append(r); ci_.append(c); data.append(float(v))
            if kind == 'le': ri.append(r); ci_.append(n + lei[r]); data.append(1.0)
            ri.append(r); ci_.append(n + nl + r); data.append(1.0)
            ri.append(r); ci_.append(n + nl + m + r); data.append(-1.0)
        nc = n + nl + 2 * m
        A = csc_matrix((data, (ri, ci_)), shape=(m, nc))
        lp = highspy.HighsLp(); lp.num_col_ = nc; lp.num_row_ = m
        lp.col_cost_ = np.concatenate([np.zeros(n + nl), np.ones(2 * m)])
        lp.col_lower_ = np.zeros(nc)
        self.slack_ub = [float(rows[r][1]) for r in le]
        lp.col_upper_ = np.concatenate([np.ones(n), np.array(self.slack_ub), np.full(2 * m, highspy.kHighsInf)])
        b = np.array([float(rows[r][1]) for r in range(m)])
        lp.row_lower_ = b; lp.row_upper_ = b
        lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
        lp.a_matrix_.start_ = A.indptr; lp.a_matrix_.index_ = A.indices; lp.a_matrix_.value_ = A.data
        h = highspy.Highs(); h.setOptionValue("output_flag", False); h.setOptionValue("solver", "ipm"); h.setOptionValue("run_crossover", "off"); h.passModel(lp); h.run()
        self.h = h; self.le = le; self.n = n
        return h.getInfo().objective_function_value

    def certificate_ok(self, den=10 ** 7):
        y = self.h.getSolution().row_dual
        rows = self.rows; m = len(rows)
        yq = [Fraction(v).limit_denominator(den) if abs(v) > 1e-10 else Fraction(0) for v in y[:m]]
        c = defaultdict(Fraction); yb = Fraction(0)
        for r, (terms, rhs, kind, name) in enumerate(rows):
            if yq[r] == 0: continue
            yb += yq[r] * rhs
            for col, v in terms: c[col] += yq[r] * v
        UB = Fraction(0); LB = Fraction(0)
        for col in range(self.n):
            cv = c.get(col, Fraction(0)); UB += max(cv, 0); LB += min(cv, 0)
        for t, r in enumerate(self.le):      # slack column of row r: coefficient y_r, box [0, rhs_r]
            cv = yq[r]; u = rows[r][1]; UB += max(cv * u, 0); LB += min(cv * u, 0)
        return (yb > UB or yb < LB), (float(yb), float(LB), float(UB))

def run_class(key):
    orbits = []; seen = {}
    for z in key:
        z = tuple(z); s_ = seen.get(z, 0); seen[z] = s_ + 1; orbits.append(z + (s_,))
    cm = ColModel(orbits, True)
    obj = cm.solve()
    out = {"ncols": len(cm.cols), "slack": obj}
    if obj > 1e-6:
        ok, info = cm.certificate_ok(); out["cert"] = ok; out["bounds"] = info
        y = cm.h.getSolution().row_dual
        out["y"] = [[str(cm.rows[r][3]), str(Fraction(y[r]).limit_denominator(10 ** 7))] for r in range(len(cm.rows)) if abs(y[r]) > 1e-10]
    else: out["cert"] = None
    out["orbits"] = orbits
    return out

if __name__ == "__main__" and False:
    orient, order = sys.argv[1], int(sys.argv[2]); useP2 = "noP2" not in sys.argv
    t0 = time.time()
    In, orbits = H.skeleton(orient, order)
    fixed_p = None
    for a in sys.argv[3:]:
        if a.startswith("fix="):
            nb0 = H.free_cycles(orbits, 0, True)[int(a[4:])]
            fixed_p = {}
            for s_ in range(N):
                for z, ws in nb0.items(): fixed_p[H.rot(z, s_)] = frozenset(H.rot(w, s_) for w in ws)
    cm = ColModel(orbits, useP2, fixed_p)
    print("columns", len(cm.cols), "rows", len(cm.rows), "built %.0fs" % (time.time() - t0)); sys.stdout.flush()
    obj = cm.solve()
    print("LP min slack %.4f" % obj, "%.0fs" % (time.time() - t0))
    if obj > 1e-6: print("certificate:", cm.certificate_ok())
