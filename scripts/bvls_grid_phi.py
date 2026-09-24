"""Controle BvLS (m=11, t = -1, x = 0) du lemme R1 et de la conjecture R2 (phi = reflexion ponctuelle en w).
Pour chaque grille L ne contenant pas x mais contenant un voisin w de x : L et tL disjointes ? pi couplage parfait ?
phi = t o pi involution de point fixe unique w ? phi = reflexion ponctuelle de L en w ?"""
import sys, os, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "vendor"))
from involution_frame import bvls243
A, syn, w8 = bvls243()
n = A.shape[0]
neg = [syn.index(tuple((-v) % 3 for v in s)) for s in syn]
x = syn.index((0, 0, 0, 0, 0))
N = [set(np.nonzero(A[v])[0]) for v in range(n)]
def third(u, v):
    c = (N[u] & N[v]); assert len(c) == 1; return next(iter(c))
def lines_at(v):
    seen, out = set(), []
    for u in N[v]:
        if u in seen: continue
        w = third(v, u); seen |= {u, w}; out.append((u, w))
    return out
grids = set()
for w in N[x]:
    L = lines_at(w)
    for (a, b), (c, d) in itertools.combinations(L, 2):
        if x in (a, b, c, d): continue
        def corner(p, q):
            cm = (N[p] & N[q]) - {w}
            return next(iter(cm)) if len(cm) == 1 else None
        z = {(p, q): corner(p, q) for p in (a, b) for q in (c, d)}
        if None in z.values(): continue
        if z[a, c] in N[z[b, c]] and z[a, d] in N[z[b, d]] and z[a, c] in N[z[a, d]] and z[b, c] in N[z[b, d]]:
            grids.add((w, a, b, c, d, z[a, c], z[a, d], z[b, c], z[b, d]))
print("grilles hors de x touchant N(x) :", len(grids))
ok = {"disjoint": 0, "pi_parfait": 0, "phi_inv_1pt": 0, "phi_reflexion": 0}
for g in grids:
    w, a, b, c, d, zac, zad, zbc, zbd = g
    Lset = set(g); tL = {neg[v] for v in Lset}
    if Lset & tL: continue
    ok["disjoint"] += 1
    pi = {}
    good = True
    for u in Lset:
        m = N[u] & tL
        if len(m) != 1: good = False; break
        pi[u] = next(iter(m))
    if not good: continue
    ok["pi_parfait"] += 1
    phi = {u: neg[pi[u]] for u in Lset}
    if all(phi[phi[u]] == u for u in Lset) and [u for u in Lset if phi[u] == u] == [w]:
        ok["phi_inv_1pt"] += 1
    refl = {w: w, a: b, b: a, c: d, d: c, zac: zbd, zbd: zac, zad: zbc, zbc: zad}
    if phi == refl: ok["phi_reflexion"] += 1
print(ok)
