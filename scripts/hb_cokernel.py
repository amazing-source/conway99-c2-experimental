"""Pure linear obstruction (note 31): for disjoint pairs R, R' let e(R,R') = E[R][R'] = E[R'][R] (coupling).  For a pair R and a block
t not in R, the local system of the two orbits Z of R gives the bundle sum
    delta_R(t) = sum_{s} e(R, {t,s}) = 8 - sum_{Z in R} ( n_t(Z) + 2[k_Z = t] )        (known from skeleton + free cycles).
The map M : e (105 values) -> delta (105 values) has rank 84, so delta must lie in im M: 21 linear conditions on the NEAR data alone.
This script builds M, a basis of its left kernel, and tests delta for given configurations."""
import itertools, sys
import numpy as np
sys.path.insert(0, "scripts")
N = 7
PAIRS = [frozenset(p) for p in itertools.combinations(range(N), 2)]
EDGES = [frozenset((R, R2)) for R in PAIRS for R2 in PAIRS if not (R & R2) and PAIRS.index(R) < PAIRS.index(R2)]
ei = {e: t for t, e in enumerate(EDGES)}
ROWS = [(R, t) for R in PAIRS for t in range(N) if t not in R]
ri = {r: t for t, r in enumerate(ROWS)}
M = np.zeros((len(ROWS), len(EDGES)))
for r, (R, t) in enumerate(ROWS):
    for s in range(N):
        if s in R or s == t: continue
        M[r, ei[frozenset((R, frozenset((t, s))))]] = 1
U, sv, Vt = np.linalg.svd(M)
LK = U[:, 84:]            # left kernel basis (orthonormal), 105 x 21

def delta(orbits, nbs):
    P = lambda a, b: frozenset((a, b))
    d = np.zeros(len(ROWS))
    for (R, t), r in ri.items():
        v = 8
        for z in orbits:
            if P(z[0], z[1]) != R: continue
            i, j, k = z
            v -= sum(1 for w in nbs[j][z] if P(w[0], w[1]) == P(j, t)) + (2 if k == t else 0)
        d[r] = v
    return d

def defect(orbits, nbs):
    d = delta(orbits, nbs)
    return float(np.linalg.norm(LK.T @ d)), d

if __name__ == "__main__":
    import hb_pairlevel as H
    orient, order = sys.argv[1], int(sys.argv[2])
    In, orbits = H.skeleton(orient, order)
    cycs = H.free_cycles(orbits, 0, True)
    for q, nb0 in enumerate(cycs):
        nbs = {s: {H.rot(z, s): [H.rot(w, s) for w in ws] for z, ws in nb0.items()} for s in range(N)}
        df, d = defect(orbits, nbs)
        print("cycle", q, "cokernel defect %.3f" % df, "| delta range", d.min(), d.max())
