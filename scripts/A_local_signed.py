"""SIGNED A-local system (note 40): can a degree-6 block A exist at all?  Only the 12 A-orbits and, for each of the 30 other
orbits Z, the SIGNED set of A-orbits it sees are modelled.  Everything else (orientation outside A, D-structures, free graphs)
is relaxed away, so infeasibility would be a universal 'no A-block' lemma.

A-orbits U = (A,x,e), x != A.  For an outside orbit Z (pair inside the 6 blocks != A) the column is
  pivot p of Z (either block of its pair; F1: Z sees no orbit of {A,p}),
  a support of 4 A-orbits among those of the pairs {A,x}, x != p   (mu = 2 at (A,+) and at (A,-)),
  t_Z(U) = sign at block A of the root of U seen by z,  with 2 plus and 2 minus  (mu = 2 at each of (A,+), (A,-)).
Rows (all proved; derivation in note 40 §9):
  G[U,W] = sum_Z t_Z(U) t_Z(W) = 10 [U = W] - [U, W in different pairs]      (anti-invariant identity S^2 + S = 12I - CC^T;
                                                                             A-orbits contribute 0: their only 2 is D, s = 0)
  H[U,W] = sum_Z |t_Z(U)| |t_Z(W)| = 1 (W = D(U)), 2 (sisters), 3 (other)     (invariant identity Q^2 + Q = 12I + 4J - Sh)
  free[U]: sum over Z whose pair contains x of |t_Z(U)| = 2      (U = (A,x,.) is free at x: exactly 2 free neighbours)
  sis5[x]: sum over Z containing x of |t_Z(U)| |t_Z(U')| <= 1 (Lemma 11.5)
Input: the orbit-level D-matching at A (one class per pair-level type, gauge-free).
Usage: python A_local_signed.py"""
import itertools, sys
import numpy as np
import highspy
from scipy.sparse import csc_matrix
A = 6; BL = [0, 1, 2, 3, 4, 5]
AORB = [(x, e) for x in BL for e in (0, 1)]             # 12 A-orbits
AI = {u: t for t, u in enumerate(AORB)}
OUT = [((i, j), s) for i, j in itertools.combinations(BL, 2) for s in (0, 1)]   # 30 outside orbits

def dmatch(cycles):
    """orbit-level D-matching for a pair-level 2-regular multigraph given as a list of cycles (digon = [x, y])"""
    D = {}
    for cyc in cycles:
        L = len(cyc)
        for t in range(L):
            x, y = cyc[t], cyc[(t + 1) % L]
            u, w = (x, 1), (y, 0)                           # orbit 1 of x goes forward, orbit 0 of y comes back
            D[u] = w; D[w] = u
    assert len(D) == 12
    return D

def build(D, use_G=True, use_H=True, cycles=None):
    """cycles: block sets of the D_A cycles -> balance at A (24.0 / 27.1): sum over x in B of a_Z(x) = |B| - |pair(Z) & B|"""
    cols = []            # (Z, t vector over 12)
    for Z, ((i, j), s) in enumerate(OUT):
        for p in (i, j):
            allowed = [AI[(x, e)] for x in BL if x != p for e in (0, 1)]
            for sup in itertools.combinations(allowed, 4):
                if cycles:
                    a = {x: 0 for x in BL}
                    for u in sup: a[AORB[u][0]] += 1
                    if any(sum(a[x] for x in B) != len(B) - len(set(B) & {i, j}) for B in cycles): continue
                for plus in itertools.combinations(range(4), 2):
                    t = np.zeros(12, dtype=np.int64)
                    for q, u in enumerate(sup): t[u] = 1 if q in plus else -1
                    cols.append((Z, t))
    rows = {}; rname = []; rkind = []; rhs = []
    def add(nm, kind, b): rows[nm] = len(rname); rname.append(nm); rkind.append(kind); rhs.append(b)
    for Z in range(30): add(('one', Z), 'eq', 1)
    for a in range(12):
        for b in range(a, 12):
            ua, ub = AORB[a], AORB[b]
            if use_G: add(('G', a, b), 'eq', 10 if a == b else (0 if ua[0] == ub[0] else -1))
            if use_H and a < b: add(('H', a, b), 'eq', 2 if ua[0] == ub[0] else (1 if D[ua] == ub else 3))
    for a in range(12): add(('free', a), 'eq', 2)
    for x in BL: add(('sis5', x), 'le', 1)
    M = []
    for Z, t in cols:
        (i, j), s = OUT[Z]; e = {rows[('one', Z)]: 1}
        nz = np.nonzero(t)[0]
        for a in nz:
            for b in nz:
                if b < a: continue
                if use_G: e[rows[('G', a, b)]] = e.get(rows[('G', a, b)], 0) + int(t[a] * t[b])
                if use_H and a < b: e[rows[('H', a, b)]] = e.get(rows[('H', a, b)], 0) + 1
            x = AORB[a][0]
            if x in (i, j): e[rows[('free', a)]] = e.get(rows[('free', a)], 0) + 1
        for x in BL:
            if x in (i, j):
                u0, u1 = AI[(x, 0)], AI[(x, 1)]
                if t[u0] and t[u1]: e[rows[('sis5', x)]] = e.get(rows[('sis5', x)], 0) + 1
        M.append(e)
    return cols, M, rname, rkind, rhs

def phase1(M, rname, rkind, rhs):
    m = len(rname); nx = len(M)
    le = [r for r in range(m) if rkind[r] == 'le']; eq = [r for r in range(m) if rkind[r] == 'eq']
    ri, ci, dv = [], [], []
    for c, e in enumerate(M):
        for r, v in e.items(): ri.append(r); ci.append(c); dv.append(float(v))
    for t, r in enumerate(le): ri.append(r); ci.append(nx + t); dv.append(1.0)
    for t, r in enumerate(eq):
        ri += [r, r]; ci += [nx + len(le) + 2 * t, nx + len(le) + 2 * t + 1]; dv += [1.0, -1.0]
    nc = nx + len(le) + 2 * len(eq)
    Am = csc_matrix((dv, (ri, ci)), shape=(m, nc))
    lp = highspy.HighsLp(); lp.num_col_ = nc; lp.num_row_ = m
    lp.col_cost_ = np.concatenate([np.zeros(nx + len(le)), np.ones(2 * len(eq))])
    lp.col_lower_ = np.zeros(nc); lp.col_upper_ = np.concatenate([np.full(nx, highspy.kHighsInf), np.array([rhs[r] for r in le], dtype=float), np.full(2 * len(eq), highspy.kHighsInf)])
    b = np.array(rhs, dtype=float); lp.row_lower_ = b; lp.row_upper_ = b
    lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_ = Am.indptr; lp.a_matrix_.index_ = Am.indices; lp.a_matrix_.value_ = Am.data
    h = highspy.Highs(); h.setOptionValue("output_flag", False); h.passModel(lp); h.run()
    return h.getInfo().objective_function_value, np.array(h.getSolution().row_dual), np.array(h.getSolution().col_value)[:nx]

if __name__ == "__main__":
    types = {"6-cycle": [[0, 1, 2, 3, 4, 5]], "4+2": [[0, 1, 2, 3], [4, 5]], "3+3": [[0, 1, 2], [3, 4, 5]], "2+2+2": [[0, 1], [2, 3], [4, 5]]}
    for nm, cyc in types.items():
        D = dmatch(cyc)
        for flags in ((True, True), (False, True), (True, False), (False, False)):
            cols, M, rname, rkind, rhs = build(D, *flags, cycles=[set(c) for c in cyc])
            obj, y, x = phase1(M, rname, rkind, rhs)
            print("%-6s G=%s H=%s: columns %d rows %d  phase-1 objective %.4f  %s" % (nm, flags[0], flags[1], len(cols), len(rname), obj, "INFEASIBLE" if obj > 1e-6 else "feasible"))
            sys.stdout.flush()
