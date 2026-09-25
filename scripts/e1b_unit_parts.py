# E1b (D5 test): are the separate unit parts u+ = odd(det Lambda^+), u- = odd(det Lambda^-) mod 8 functions of the parameters?
import sys; sys.path.insert(0, "scripts"); sys.path.insert(0, "data")
import numpy as np
from e1_arf_local import half_lattice_det, odd_part, paley_sq, net_graph
from fractions import Fraction
def run(name, A, sig, x):
    n = len(A); k = int(A[0].sum())
    ev = np.round(np.linalg.eigvalsh(A.astype(float))).astype(int)
    r, s = sorted(set(ev.tolist()) - {k}, reverse=True)
    if (r - s) % 2 == 0: return
    row = []
    for th in (r, s):
        f = int(sum(ev == th))
        _, Dp, _ = half_lattice_det(A, sig, x, th, +1); _, Dm, _ = half_lattice_det(A, sig, x, th, -1)
        up, um = odd_part(Dp.numerator) % 8, odd_part(Dm.numerator) % 8
        Exx = Fraction(f, n)
        row.append(f"th={th:>3} f={f:>4} E_xx={str(Exx):>7} u+={up} u-={um} ratio={up*pow(um,-1,8)%8}")
    print(f"{name:14s} v={n:>3} " + " | ".join(row)); sys.stdout.flush()
for q, ns in ((3, 2), (5, 2), (7, 3), (11, 2), (13, 2)):
    A, sg, x = paley_sq(q, ns); run(f"Paley({q}^2)", A, sg, x)
for n in (5, 7, 11, 13):
    dirs_all = [(1, 0), (0, 1), (1, 1), (1, n - 1), (1, 2), (2, 1)]
    for m in range(2, min(n, 6) + 1):
        A, sg, x = net_graph(n, dirs_all[:m]); run(f"L_{m}({n})", A, sg, x)
from control_bvls_copy import bvls
A, V, ix, cols, neg = bvls(); A = A.astype(np.int64)
run("BvLS", A, [ix[neg(v)] for v in V], ix[(0,) * 5])
