"""H-beta capped search (note 32; user-approved 26/09, cap ~3 h): depth-first over the free cycles block by block, pruning with the
LP relaxation of the first-order pair-level system F2 (hb_tree.Instance), solved incrementally with highspy (bounds on lambda
change per node).  Every pruned node carries an EXACT rational certificate check (verify below).  Leaves that survive the LP are
recorded (they must then face integer F2 / P2).
Usage: python hb_dfs.py <skeleton spec> <seconds>     spec = circ:23:0 | idx:<class index>:<order bits>
"""
import sys, time, json
from fractions import Fraction
from collections import defaultdict
import numpy as np
import highspy
from scipy.sparse import csc_matrix
sys.path.insert(0, "scripts")
import hb_pairlevel as H, hb_tree as T
N = H.N

class FastLP:
    def __init__(self, inst):
        self.inst = inst
        rows, col = inst.build({})          # all blocks relaxed: every lambda present
        self.rows, self.col = rows, col
        nv = len(col); m = len(rows); nf = len(inst.far)
        self.nv, self.m, self.nf = nv, m, nf
        data = []; ri = []; ci = []
        for r, (d, rhs, _) in enumerate(rows):
            for c, v in d.items(): ri.append(r); ci.append(c); data.append(v)
            ri.append(r); ci.append(nv + r); data.append(1.0)
            ri.append(r); ci.append(nv + m + r); data.append(-1.0)
        for t, f in enumerate(inst.far):
            ri.append(m + t); ci.append(col[f, 'a']); data.append(1.0)
            ri.append(m + t); ci.append(col[f, 'b']); data.append(1.0)
        A = csc_matrix((data, (ri, ci)), shape=(m + nf, nv + 2 * m))
        lp = highspy.HighsLp()
        lp.num_col_ = nv + 2 * m; lp.num_row_ = m + nf
        lp.col_cost_ = np.concatenate([np.zeros(nv), np.ones(2 * m)])
        lp.col_lower_ = np.zeros(nv + 2 * m); lp.col_upper_ = np.concatenate([np.ones(nv), np.full(2 * m, highspy.kHighsInf)])
        b = np.array([rhs for (_, rhs, _) in rows], dtype=float)
        lp.row_lower_ = np.concatenate([b, np.full(nf, -highspy.kHighsInf)]); lp.row_upper_ = np.concatenate([b, np.ones(nf)])
        lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
        lp.a_matrix_.start_ = A.indptr; lp.a_matrix_.index_ = A.indices; lp.a_matrix_.value_ = A.data
        self.h = highspy.Highs(); self.h.setOptionValue("output_flag", False); self.h.passModel(lp)
        self.lamcols = {(j, c): col['lam', j, c] for j in range(N) for c in range(len(inst.cycles[j]))}

    def solve(self, fixed):
        idx = []; lo = []; up = []
        for (j, c), k in self.lamcols.items():
            idx.append(k)
            if j in fixed: v = 1.0 if fixed[j] == c else 0.0; lo.append(v); up.append(v)
            else: lo.append(0.0); up.append(1.0)
        self.h.changeColsBounds(len(idx), np.array(idx, dtype=np.int32), np.array(lo), np.array(up))
        self.h.run()
        obj = self.h.getInfo().objective_function_value
        return obj

    def certificate_ok(self, fixed, den=10 ** 6):
        y = self.h.getSolution().row_dual[:self.m]
        yq = [Fraction(v).limit_denominator(den) if abs(v) > 1e-9 else Fraction(0) for v in y]
        c = defaultdict(Fraction); yb = Fraction(0)
        for r, (d, rhs, _) in enumerate(self.rows):
            if yq[r] == 0: continue
            yb += yq[r] * Fraction(rhs)
            for k2, v in d.items(): c[k2] += yq[r] * Fraction(v)
        UB = Fraction(0); LB = Fraction(0)
        for f in self.inst.far:
            ca = c.get(self.col[f, 'a'], Fraction(0)); cb = c.get(self.col[f, 'b'], Fraction(0))
            UB += max(Fraction(0), ca, cb); LB += min(Fraction(0), ca, cb)
        for (j, cc), k in self.lamcols.items():
            cv = c.get(k, Fraction(0))
            if j in fixed:
                if fixed[j] == cc: UB += cv; LB += cv
            else: UB += max(cv, 0); LB += min(cv, 0)
        return yb > UB or yb < LB

def dfs(fl, order, budget, t0, log):
    stats = defaultdict(int); leaves = []
    stack = [dict()]
    while stack:
        if time.time() - t0 > budget: return stats, leaves, False
        fixed = stack.pop()
        obj = fl.solve(fixed); stats['nodes'] += 1
        if obj > 1e-6:
            if fl.certificate_ok(fixed): stats['pruned_certified', len(fixed)] += 1; continue
            stats['cert_failed', len(fixed)] += 1        # treat as not pruned (conservative)
        if len(fixed) == N: leaves.append(dict(fixed)); stats['leaf'] += 1; continue
        j = order[len(fixed)]
        for c in range(len(fl.inst.cycles[j])):
            nf_ = dict(fixed); nf_[j] = c; stack.append(nf_)
    return stats, leaves, True

if __name__ == "__main__":
    spec, budget = sys.argv[1], float(sys.argv[2])
    kind, a1, a2 = spec.split(":")
    if kind == "circ": In, orbits = H.skeleton(a1, int(a2))
    t0 = time.time()
    inst = T.Instance(orbits); fl = FastLP(inst)
    print("built in %.1fs" % (time.time() - t0), "| cycles per block", [len(inst.cycles[j]) for j in range(N)]); sys.stdout.flush()
    stats, leaves, done = dfs(fl, list(range(N)), budget, t0, None)
    print("done" if done else "TIME CAP", dict(stats), "| leaves (LP survivors):", len(leaves), "| %.0fs" % (time.time() - t0))
    json.dump({"spec": spec, "done": done, "leaves": leaves}, open("logs/hb_dfs_%s.json" % spec.replace(":", "_"), "w"))
