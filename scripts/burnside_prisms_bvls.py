"""Controle sur BvLS (m = 11, graphe reel avec l'involution x -> -x) des comptes « Burnside mod 2 » (notes/20) :
  - prismes induits K3 x K2 (n1 de Reimbayev) et prismes t-invariants ;
  - configurations N3 (quadrilatere + triangles sur deux cotes opposes, troisiemes points NON adjacents) ;
  - 2K3 induits (n14) et 2K3 t-invariants.
Predictions (notes/20) : #prismes t-invariants = somme sur les etoiles des aretes D internes = 2 n_sib + n_one ;
#2K3 t-invariants = #triangles d'orbites (Q = 1 partout) d'holonomie + ; et n1 = n k(k-2)/12 - n3/3, n14 = ... + n3/3.
"""
import sys, itertools
import numpy as np
sys.path.insert(0, "scripts/vendor")
import control_bvls as cb

A, V, ix, cols, neg = cb.bvls()
n = A.shape[0]; k = 22
t = np.array([ix[neg(v)] for v in V])
nbrs = [set(np.flatnonzero(A[i])) for i in range(n)]
# triangles (droites)
tri = set()
for a in range(n):
    for b in nbrs[a]:
        if b > a:
            c = (nbrs[a] & nbrs[b]).pop()
            tri.add(tuple(sorted((a, b, c))))
tri = sorted(tri)
print("triangles :", len(tri), "(attendu n k / 6 =", n * k // 6, ")")
third = {}
for (a, b, c) in tri:
    third[(a, b)] = third[(b, a)] = c; third[(a, c)] = third[(c, a)] = b; third[(b, c)] = third[(c, b)] = a
# quadrilateres induits : pour chaque non-arete {u,v}, ses 2 voisins communs p,q (non adjacents entre eux) forment u-p-v-q
quads = set()
for u in range(n):
    for v in range(u + 1, n):
        if A[u, v]:
            continue
        cm = nbrs[u] & nbrs[v]
        if len(cm) == 2:
            p, q = sorted(cm)
            quads.add(tuple(sorted(((u, v), (p, q)))))
print("quadrilateres induits :", len(quads), "(attendu n k (k-2) / 8 =", n * k * (k - 2) // 8, ")")
# prismes et N3 : quadrilatere a-b-c-d (a~b~c~d~a), triangles sur les cotes opposes ab et cd : troisiemes points e (ab), f (cd)
prisms = set(); n3 = 0
for ((u, v), (p, q)) in quads:
    cyc = [u, p, v, q]                    # u~p~v~q~u
    for s in (0, 1):                      # paires de cotes opposes : (cyc[s],cyc[s+1]) et (cyc[s+2],cyc[s+3])
        a, b, c, d = cyc[s], cyc[(s + 1) % 4], cyc[(s + 2) % 4], cyc[(s + 3) % 4]
        e = third[(a, b)]; f = third[(c, d)]
        S = frozenset((a, b, c, d, e, f))
        if len(S) < 6:
            continue
        if A[e, f]:
            prisms.add(S)
        else:
            n3 += 1
print("prismes (n1) :", len(prisms), " N3 :", n3, " controle 2p4 = 3n1 + n3 :", 2 * len(quads) == 3 * len(prisms) + n3)
tinv = [S for S in prisms if frozenset(t[list(S)]) == S]
print("prismes t-invariants :", len(tinv))
# 2K3 induits t-invariants : paires {T, tT} de triangles disjoints sans arete entre eux
cnt = 0
for T in tri:
    tT = tuple(sorted(t[list(T)]))
    if tT <= T or set(T) & set(tT):
        continue
    if not any(A[a, b] for a in T for b in tT):
        cnt += 1
print("2K3 induits t-invariants :", cnt)
print("n3/3 =", n3 / 3, " ; parite de n1 =", len(prisms) % 2, " ; parite des prismes t-invariants =", len(tinv) % 2)
