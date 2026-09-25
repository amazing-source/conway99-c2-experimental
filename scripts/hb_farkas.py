"""Sparse Farkas certificate for the LP relaxation of the first-order system (hb_lp_ppe.lp) -- note 31.
System: A x = b (rows L, D, S, C), 0 <= x <= 1, a+b <= 1 per far value.  Certificate: y (free), z >= 0 (a+b<=1), w >= 0 (x<=1) with
  y^T A - z^T B - w^T <= 0  (columnwise)   and   y^T b - sum z - sum w >= 1.
Then for any feasible x: y^T b = y^T A x <= (z^T B + w^T) x <= sum z + sum w < y^T b.  Minimise |y|_1 + sum z + sum w (sparsity)."""
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, hstack, vstack, csr_matrix, identity
sys.path.insert(0, "scripts")
import hb_pairlevel as H, hb_lp_ppe as L
from collections import Counter, defaultdict
N = H.N

def certificate(orbits, nbs, useS=True, useC=True):
    res, rows, far, col = L.lp(orbits, nbs, useS, useC)
    nv = len(col); m = len(rows); nf = len(far)
    A = lil_matrix((m, nv)); b = np.zeros(m)
    for r, (d, rhs, _) in enumerate(rows):
        for c, v in d.items(): A[r, c] = v
        b[r] = rhs
    B = lil_matrix((nf, nv))
    for t, f in enumerate(far): B[t, col[f, 'a']] = 1; B[t, col[f, 'b']] = 1
    A = A.tocsr(); B = B.tocsr()
    # variables: y+ (m), y- (m), z (nf), w (nv)
    # column constraints: (y+ - y-)^T A - z^T B - w^T <= 0  ->  A^T y+ - A^T y- - B^T z - w <= 0
    G = hstack([A.T, -A.T, -B.T, -identity(nv)]).tocsr()
    h = np.zeros(nv)
    # normalisation: b^T y+ - b^T y- - sum z - sum w >= 1  ->  -b y+ + b y- + z + w <= -1
    g = np.concatenate([-b, b, np.ones(nf), np.ones(nv)])
    Aub = vstack([G, csr_matrix(g)]).tocsr(); bub = np.concatenate([h, [-1]])
    cost = np.concatenate([np.ones(2 * m), np.ones(nf), np.ones(nv)])
    r = linprog(cost, A_ub=Aub, b_ub=bub, bounds=[(0, None)] * (2 * m + nf + nv), method="highs")
    if r.status != 0: return None, rows
    y = r.x[:m] - r.x[m:2 * m]; z = r.x[2 * m:2 * m + nf]; w = r.x[2 * m + nf:]
    return (y, z, w, far, col), rows

if __name__ == "__main__":
    orient, order, q = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    In, orbits = H.skeleton(orient, order)
    nb0 = H.free_cycles(orbits, 0, True)[q]
    nbs = {s: {H.rot(z, s): [H.rot(w, s) for w in ws] for z, ws in nb0.items()} for s in range(N)}
    cert, rows = certificate(orbits, nbs)
    if cert is None: print("no certificate (LP feasible)"); sys.exit()
    y, z, w, far, col = cert
    sup = [(rows[r][2], y[r]) for r in range(len(rows)) if abs(y[r]) > 1e-7]
    print("support of y:", len(sup), Counter(s[0][0] for s in sup), "| z:", int((z > 1e-7).sum()), "| w:", int((w > 1e-7).sum()))
    for n_, v in sorted(sup, key=lambda s: (s[0][0], str(s[0][1:]))):
        if n_[0] != 'L' or rot0(n_) if False else True:
            pass
    byrot = defaultdict(list)
    for n_, v in sup:
        if n_[0] == 'L' and n_[1][0] == 0: print("  L", n_[1], "t=%d" % n_[2], round(v, 4))
        elif n_[0] in 'DSC' and 0 in set().union(*[x for x in n_[1:]]): print("  ", n_[0], [sorted(x) for x in n_[1:]], round(v, 4))
