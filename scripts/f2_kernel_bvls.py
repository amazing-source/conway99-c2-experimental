"""Noyau sur F2 de A1 + Sh (A1 = [Q = 1]) pour BvLS (m = 11) : dimension, et quels vecteurs « naturels » il contient (notes/19 §10).
Vecteurs testes : colonnes de Nb (blocs), e (orbites moins), indicatrices par paire, e restreint aux paires contenant un bloc, etc.
"""
import sys, itertools
import numpy as np
sys.path.insert(0, "scripts")
exec(open("scripts/minus_parity_check.py", encoding="utf-8").read().split("# echange des deux orbites")[0])
from parity_star import rank_f2
C = np.array([[1 if l == i else ((-1 if e else 1) if l == j else 0) for l in range(1, m + 1)] for (i, j, e) in outer])
Nb = np.abs(C); Sh = Nb @ Nb.T
M = (((Q == 1).astype(int) + Sh) % 2).astype(np.uint8)
r = rank_f2(M)
print("m=11 : N =", N, "rang_F2(A1 + Sh) =", r, "noyau de dimension", N - r)
def inker(v):
    return not ((M.astype(int) @ v) % 2).any()
tests = {}
for l in range(m):
    tests["Nb_%d" % (l + 1)] = Nb[:, l] % 2
e = np.array([ee for (i, j, ee) in outer])
tests["e (moins)"] = e
D = (Q == 2).astype(int)
tests["D e"] = (D @ e) % 2
for (a, b) in [(1, 2), (1, 3), (2, 5)]:
    v = np.array([1 if (i, j) == (a, b) else 0 for (i, j, ee) in outer]); tests["paire %d%d (2 orbites)" % (a, b)] = v
for l in (1, 2):
    tests["e sur paires contenant %d" % l] = np.array([ee if l in (i, j) else 0 for (i, j, ee) in outer])
for name, v in tests.items():
    print("%-28s dans le noyau : %s" % (name, inker(v)))
# dimension de l'espace engendre par Nb et e dans le noyau
B = np.array([tests["Nb_%d" % (l + 1)] for l in range(m)] + [e]).astype(np.uint8)
print("rang(Nb, e) =", rank_f2(B))
