"""Control (note 37): does the ORBIT-LEVEL second-order identity (Q^2 + Q = 12 I + 4 J - Sh, structures) see Theorem D (all 21 pairs
sister)?  Orbits (P,s).  A sister orbit U of P has q_U(U') = 2 (sib square), no other near neighbour, and exactly ONE neighbour in
every disjoint pair R (grid perfection, 8.1): one of R's two orbits -> 2^10 orbit-level columns per orbit.
Rows: one column per orbit; coupling q_U(W) = q_W(U); P2o (doubled).  LP feasibility (slack minimisation) + exact check."""
import itertools, sys, time
import numpy as np, highspy
from scipy.sparse import csc_matrix
from fractions import Fraction
N = 7
PAIRS = [frozenset(p) for p in itertools.combinations(range(N), 2)]
ORB = [(R, s) for R in PAIRS for s in (0, 1)]; OI = {o: t for t, o in enumerate(ORB)}
cols = []   # (orbit index, vector dict orbit-index -> value)
for (R, s) in ORB:
    far = [Q for Q in PAIRS if not (Q & R)]
    for ch in itertools.product((0, 1), repeat=len(far)):
        v = {OI[(R, 1 - s)]: 2}
        for Q, c in zip(far, ch): v[OI[(Q, c)]] = 1
        cols.append((OI[(R, s)], v))
print("columns", len(cols))
rows = []; rhs = []
def sh(U, W): return len(ORB[U][0] & ORB[W][0])
rid = {}
for u in range(42): rid['O', u] = len(rid); rhs.append(1)
for u in range(42):
    for w in range(u + 1, 42): rid['C', u, w] = len(rid); rhs.append(0)
for u in range(42):
    for w in range(u, 42): rid['P', u, w] = len(rid); rhs.append(2 * (12 * (u == w) + 4 - sh(u, w)))
m = len(rid); data, ri, ci = [], [], []
for c, (z, v) in enumerate(cols):
    ent = {rid['O', z]: 1}
    for w, x in v.items():
        if z < w: ent[rid['C', z, w]] = ent.get(rid['C', z, w], 0) + x
        elif w < z: ent[rid['C', w, z]] = ent.get(rid['C', w, z], 0) - x
    items = list(v.items())
    for (u, x), (w, y) in itertools.product(items, items):
        if u <= w: ent[rid['P', u, w]] = ent.get(rid['P', u, w], 0) + (2 * x * y if u != w else 2 * x * x) * (1 if u == w else 1)
    # fix double counting: for u<w both (u,w) and (w,u) appear in the product -> 2*x*y counted once per ordered pair u<w only
    for w, x in v.items():
        key = ('P', min(z, w), max(z, w))
        if z != w: ent[rid[key]] = ent.get(rid[key], 0) + x          # + q_Z(W) term (Z = U or W side)
    for r, val in ent.items(): ri.append(r); ci.append(c); data.append(val)
nx = len(cols)
for r in range(m):
    ri.append(r); ci.append(nx + 2 * r); data.append(1.0); ri.append(r); ci.append(nx + 2 * r + 1); data.append(-1.0)
A = csc_matrix((data, (ri, ci)), shape=(m, nx + 2 * m))
lp = highspy.HighsLp(); lp.num_col_ = nx + 2 * m; lp.num_row_ = m
lp.col_cost_ = np.concatenate([np.zeros(nx), np.ones(2 * m)]); lp.col_lower_ = np.zeros(nx + 2 * m)
lp.col_upper_ = np.concatenate([np.ones(nx), np.full(2 * m, highspy.kHighsInf)])
b = np.array(rhs, dtype=float); lp.row_lower_ = b; lp.row_upper_ = b
lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
lp.a_matrix_.start_ = A.indptr; lp.a_matrix_.index_ = A.indices; lp.a_matrix_.value_ = A.data
h = highspy.Highs(); h.setOptionValue("output_flag", False); h.setOptionValue("solver", "ipm"); h.setOptionValue("run_crossover", "off")
t0 = time.time(); h.passModel(lp); h.run(); obj = h.getInfo().objective_function_value
print("orbit-level all-sister LP: min slack %.4f (%.0fs)" % (obj, time.time() - t0))
if obj > 1e-6:
    y = h.getSolution().row_dual[:m]
    yq = [Fraction(v).limit_denominator(10 ** 7) for v in y]
    # exact per-orbit Farkas: low = sum_{rows != O} y*rhs ; high = sum_z max_c sum_{rows != O} y A_rc ; O rows through the max
    Acsr = A[:, :nx].tocsc()
    isO = [False] * m
    for key, r in rid.items(): isO[r] = key[0] == 'O'
    low = sum(yq[r] * rhs[r] for r in range(m) if not isO[r])
    best = {}
    for c in range(nx):
        z = cols[c][0]; st, en = Acsr.indptr[c], Acsr.indptr[c + 1]
        s_ = sum(yq[Acsr.indices[t]] * int(Acsr.data[t]) for t in range(st, en) if not isO[Acsr.indices[t]])
        if z not in best or s_ > best[z]: best[z] = s_
    high = sum(best.values())
    print("exact per-orbit Farkas: low %.4f high %.4f ->" % (float(low), float(high)), "INFEASIBLE (certified)" if low > high else "not certified with these duals")
