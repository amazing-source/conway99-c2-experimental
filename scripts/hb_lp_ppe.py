"""First-order LINEAR test on H-beta (note 31): local system (L) + exact per-pair doubles (PPE, the diagonal of P2) [+ column sums S,
+ coupling C], in 0/1 indicator variables a (phi = 1) and b (phi = 2) for every FAR value phi_Z(R); near values are known from the
skeleton and the free cycles.  phi = a + 2b, phi^2 = a + 4b, a + b <= 1.  LP relaxation: if the minimum total slack is > 0, the LP is
infeasible and the dual gives a weighted-sum (Farkas) certificate, i.e. a counting proof.
Usage: python hb_lp_ppe.py <orient 23|2m3> <order 0|1> <cycle index | all> [S] [C]
"""
import sys, itertools
from collections import defaultdict
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
sys.path.insert(0, "scripts")
import hb_pairlevel as H
N = H.N; P = H.P; PAIRS = H.PAIRS

def known_values(orbits, nbs):
    known = {}
    for z in orbits:
        i, j, k = z
        for R in PAIRS:
            if R == P(i, j): known[z, R] = 0
            elif i in R: known[z, R] = 2 if R == P(i, k) else 0
            elif j in R: known[z, R] = sum(1 for w in nbs[j][z] if P(w[0], w[1]) == R)
    return known

def lp(orbits, nbs, useS, useC):
    known = known_values(orbits, nbs)
    far = [(z, R) for z in orbits for R in PAIRS if (z, R) not in known]
    col = {}
    for f in far: col[f, 'a'] = len(col); col[f, 'b'] = len(col)
    nv = len(col)
    rows = []   # (dict col->coef, rhs, name)   equality rows
    for z in orbits:
        i, j, k = z
        for t in range(N):
            if t in (i, j): continue
            d = defaultdict(float); rhs = 4
            for R in PAIRS:
                if t not in R: continue
                if (z, R) in known: rhs -= known[z, R]
                else: d[col[(z, R), 'a']] += 1; d[col[(z, R), 'b']] += 2
            rows.append((d, rhs, ('L', z, t)))
    pairs_of = defaultdict(list)
    for z in orbits: pairs_of[P(z[0], z[1])].append(z)
    for R in PAIRS:
        d = defaultdict(float); rhs = 32
        for z in orbits:
            if (z, R) in known: rhs -= known[z, R] ** 2
            else: d[col[(z, R), 'a']] += 1; d[col[(z, R), 'b']] += 4
        rows.append((d, rhs, ('D', R)))
        if useS:
            d = defaultdict(float); rhs = 24
            for z in orbits:
                if (z, R) in known: rhs -= known[z, R]
                else: d[col[(z, R), 'a']] += 1; d[col[(z, R), 'b']] += 2
            rows.append((d, rhs, ('S', R)))
    if useC:
        for ia, R in enumerate(PAIRS):
            for R2 in PAIRS[ia + 1:]:
                d = defaultdict(float); rhs = 0
                for y in pairs_of[R]:
                    if (y, R2) in known: rhs -= known[y, R2]
                    else: d[col[(y, R2), 'a']] += 1; d[col[(y, R2), 'b']] += 2
                for y in pairs_of[R2]:
                    if (y, R) in known: rhs += known[y, R]
                    else: d[col[(y, R), 'a']] -= 1; d[col[(y, R), 'b']] -= 2
                rows.append((d, rhs, ('C', R, R2)))
    # variables: x (nv), s+ (m), s- (m); minimise sum s
    m = len(rows)
    Aeq = lil_matrix((m, nv + 2 * m)); beq = np.zeros(m)
    for r, (d, rhs, _) in enumerate(rows):
        for c, v in d.items(): Aeq[r, c] = v
        Aeq[r, nv + r] = 1; Aeq[r, nv + m + r] = -1; beq[r] = rhs
    Aub = lil_matrix((len(far), nv + 2 * m)); bub = np.ones(len(far))
    for t, f in enumerate(far): Aub[t, col[f, 'a']] = 1; Aub[t, col[f, 'b']] = 1
    c = np.concatenate([np.zeros(nv), np.ones(2 * m)])
    res = linprog(c, A_ub=Aub.tocsr(), b_ub=bub, A_eq=Aeq.tocsr(), b_eq=beq, bounds=[(0, 1)] * nv + [(0, None)] * (2 * m), method="highs")
    return res, rows, far, col

if __name__ == "__main__":
    orient, order, ci = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    useS = "S" in sys.argv[4:]; useC = "C" in sys.argv[4:]
    In, orbits = H.skeleton(orient, order)
    cycs = H.free_cycles(orbits, 0, True)
    idxs = range(len(cycs)) if ci == "all" else [int(ci)]
    for q in idxs:
        nb0 = cycs[q]
        nbs = {s: {H.rot(z, s): [H.rot(w, s) for w in ws] for z, ws in nb0.items()} for s in range(N)}
        res, rows, far, col = lp(orbits, nbs, useS, useC)
        print("skeleton", orient, order, "cycle", q, "| rows", len(rows), "| LP min slack = %.4f" % res.fun, "(INFEASIBLE LP)" if res.fun > 1e-6 else "(LP feasible)")
