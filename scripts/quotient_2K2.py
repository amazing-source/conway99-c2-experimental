"""Two disjoint sib pairs p={1,2}, q={3,4} at m=7: averaged quotient matrix of the 10-cell partition
   x | I_p | I_q | I_r | P_p | P_q | M(16) | T_pr(24) | T_qr(24) | R_r(12)
All average counts derived by hand from Lemma S1 (see notes/04_*.md); one free global parameter eps = #edges inside R_r.
Haemers interlacing: all eigenvalues except the Perron one must lie in [-4, 3]. Equitable case: must be in {14, 3, -4}.
"""
import numpy as np
from fractions import Fraction as F
import sympy as sp

def Bbar(eps):
    rb = F(24 + 2 * eps, 16)          # avg # neighbours in M of a vertex of M (= avg in R_r)
    tb = 3 - F(eps, 12)               # avg # neighbours in M of a vertex of T_pr (and of T_qr)
    nb = F(eps, 6)                    # avg # neighbours in R_r of a vertex of R_r
    rows = [
        [0, 4, 4, 6, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 2, 0, 4, 6, 0, 0],
        [1, 0, 1, 0, 0, 2, 4, 0, 6, 0],
        [1, 0, 0, 1, 0, 0, 0, 4, 4, 4],
        [0, 2, 0, 0, 2, 1, 0, 0, 6, 3],
        [0, 0, 2, 0, 1, 2, 0, 6, 0, 3],
        [0, 1, 1, 0, 0, 0, rb, 6 - rb, 6 - rb, rb],
        [0, 1, 0, 1, 0, 1, tb, 6 - tb, 6 - tb, tb - 1],
        [0, 0, 1, 1, 1, 0, tb, 6 - tb, 6 - tb, tb - 1],
        [0, 0, 0, 2, 1, 1, 2 + nb, 4 - nb, 4 - nb, nb],
    ]
    return sp.Matrix(rows)

sizes = [1, 4, 4, 6, 4, 4, 16, 24, 24, 12]
for eps in range(0, 25):
    B = Bbar(eps)
    assert all(sum(B.row(i)) == 14 for i in range(10)), eps
    # symmetry check: |C| B(C,D) == |D| B(D,C)
    for i in range(10):
        for j in range(10):
            assert sizes[i] * B[i, j] == sizes[j] * B[j, i], (eps, i, j)
    ev = sorted([complex(v).real for v in B.evalf().eigenvals(multiple=True)], reverse=True) if False else \
         sorted(np.linalg.eigvals(np.array(B.tolist(), dtype=float)).real, reverse=True)
    ok = all(-4 - 1e-9 <= v <= 3 + 1e-9 for v in ev[1:])
    print("eps=%2d  eigenvalues %s  interlacing %s" % (eps, " ".join("%.4f" % v for v in ev), "OK" if ok else "VIOLATED"))
eps = sp.symbols('eps')
