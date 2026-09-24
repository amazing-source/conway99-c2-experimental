"""Parite « orbites moins » (notes/19 §10) : pour toute orbite U, #{V : Q[U,V] = 1, V orbite « - » (e = 1)} est PAIR.
Derivation : somme sur tous les blocs l des parites de (I) pour la ligne U ; les signes Z s'annulent (chaque voisin a deux blocs),
il reste sum_{V in N1(U)} e_V = sum_l n(l) - |blocs(D(U))| = 0 (mod 2), valable pour tout m.
Controle sur un graphe REEL : Berlekamp-van Lint-Seidel (m = 11), table planted (a,b) construite comme vendor/control_bvls.py.
Et : cette contrainte n'est PAS une consequence de l'etage Q (l'etage Q est invariant par l'echange des deux orbites d'une paire,
symetrie (Z2)^21 absente du vrai probleme) -- test : on echange U_r^+ et U_r^- pour une paire r dans la table BvLS et on regarde.
"""
import sys, itertools
import numpy as np
sys.path.insert(0, "scripts/vendor")
import control_bvls as cb

A, V, ix, cols, neg = cb.bvls()
n, k, m = 243, 22, 11
x = ix[(0,) * 5]; inner = {}
for i, c in enumerate(cols): inner[ix[c]] = (i + 1, 0); inner[ix[neg(c)]] = (i + 1, 1)
label = {}
for v in range(n):
    if v == x or v in inner: continue
    nb = [inner[w] for w in np.flatnonzero(A[v]) if w in inner]
    label[frozenset(nb)] = v
outer = [(i, j, e) for i in range(1, m + 1) for j in range(i + 1, m + 1) for e in (0, 1)]
rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
N = len(outer)
Am = np.array([[A[label[rep[U]], label[rep[W]]] if U != W else 0 for W in range(N)] for U in range(N)])
Bm = np.array([[A[label[rep[U]], label[trep[W]]] if U != W else 0 for W in range(N)] for U in range(N)])
Q = Am + Bm
minus = np.array([e for (i, j, e) in outer])
cnt = ((Q == 1).astype(int) @ minus)
print("BvLS m=11 : lignes =", N, "; #voisins Q=1 « - » pairs pour toutes les lignes :", bool((cnt % 2 == 0).all()),
      "; valeurs rencontrees :", sorted(set(cnt.tolist())))
# echange des deux orbites d'une paire r (symetrie de l'etage Q seulement)
r = outer.index((1, 2, 0)); r2 = outer.index((1, 2, 1))
perm = list(range(N)); perm[r], perm[r2] = r2, r
Q2 = Q[np.ix_(perm, perm)]
cnt2 = ((Q2 == 1).astype(int) @ minus)
print("apres echange de U_12^+ et U_12^- (encore solution de l'etage Q) : lignes de parite impaire :", int((cnt2 % 2 == 1).sum()))
