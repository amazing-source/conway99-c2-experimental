"""Taille exacte d'une relaxation de moments de degre 2 symetrisee pour le modele C2 (notes/16).  Comptage de Burnside, sans SDP.

Variables : orbites sous t = -1 des paires non ordonnees {r, s} de racines de D7 (r != s, s != -r) = variables a/b du modele d'orbites
(orbit_sat.py) : 1722 au total.  Types : partage d'une demi-etiquette (couplages locaux M_h), partage d'un bloc sans etiquette,
supports disjoints.
Groupe : W(B7) = 2^7 x| S7 (reetiquetage de la carte en x), qui contient t = -1.  La moyenne d'une solution sur ses reetiquetages
est une pseudo-distribution W(B7)-invariante : on peut donc symetriser la relaxation sans rien supposer sur la solution.
On compte, par Burnside sur les 110 classes de conjugaison (bipartitions de 7) :
- orbites sur les variables (nombre de moments d'ordre 1) ;
- orbites sur les paires ordonnees de variables = dim de l'algebre commutante = somme des m_lambda^2 (blocs SDP) ;
- orbites sur les paires non ordonnees (nombre de moments d'ordre 2 distincts).
"""
import itertools
from math import factorial
from collections import Counter

M = 7

def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

def classes(n):
    for k in range(n + 1):
        for alpha in partitions(k):
            for beta in partitions(n - k):
                yield alpha, beta

def centralizer(alpha, beta):
    z = 1
    for part in (alpha, beta):
        for i, mi in Counter(part).items():
            z *= (2 * i) ** mi * factorial(mi)
    return z

def representative(alpha, beta):
    """perm (bloc -> bloc) et signes eps (bloc -> +-1) : g(i, s) = (perm[i], s * eps[i])."""
    perm, eps = {}, {}
    b = 1
    for cyc, sign in [(c, 1) for c in alpha] + [(c, -1) for c in beta]:
        blocks = list(range(b, b + cyc))
        for idx, i in enumerate(blocks):
            perm[i] = blocks[(idx + 1) % cyc]
            eps[i] = sign if idx == cyc - 1 else 1
        b += cyc
    return perm, eps

HALF = [(i, s) for i in range(1, M + 1) for s in (1, -1)]
ROOTS = [frozenset([h1, h2]) for h1, h2 in itertools.combinations(HALF, 2) if h1[0] != h2[0]]
neg = lambda r: frozenset((i, -s) for i, s in r)

def vtype(r, s):
    if r & s:
        return "etiquette"
    if {i for i, _ in r} & {i for i, _ in s}:
        return "bloc"
    return "disjoints"

VARS, VIDX = [], {}
for r, s in itertools.combinations(ROOTS, 2):
    if s == neg(r):
        continue
    key = frozenset([frozenset([r, s]), frozenset([neg(r), neg(s)])])
    if key not in VIDX:
        VIDX[key] = len(VARS); VARS.append((r, s))
TYPES = [vtype(r, s) for r, s in VARS]

def act(g, r):
    perm, eps = g
    return frozenset((perm[i], s * eps[i]) for i, s in r)

def perm_on_vars(g):
    out = []
    for r, s in VARS:
        r2, s2 = act(g, r), act(g, s)
        out.append(VIDX[frozenset([frozenset([r2, s2]), frozenset([neg(r2), neg(s2)])])])
    return out

if __name__ == "__main__":
    order = 2 ** M * factorial(M)
    print("variables : %d  %s" % (len(VARS), dict(Counter(TYPES))))
    tot = Counter(); tot_type = Counter(); tot_pairs_by = Counter()
    ncls = 0; check = 0
    for alpha, beta in classes(M):
        ncls += 1
        size = order // centralizer(alpha, beta)
        check += size
        p = perm_on_vars(representative(alpha, beta))
        fixed = [i for i in range(len(p)) if p[i] == i]
        a = len(fixed)
        b = sum(1 for i in range(len(p)) if p[i] != i and p[p[i]] == i) // 2
        tot["vars"] += size * a
        tot["ordered_pairs"] += size * a * a
        tot["unordered_pairs"] += size * (a * (a - 1) // 2 + b + a)
        for ty, c in Counter(TYPES[i] for i in fixed).items():
            tot_type[ty] += size * c
        ft = Counter(TYPES[i] for i in fixed)
        for t1 in ft:
            for t2 in ft:
                tot_pairs_by[(t1, t2)] += size * ft[t1] * ft[t2]
    assert check == order, (check, order)
    print("classes de conjugaison : %d ; |W(B7)| = %d" % (ncls, order))
    print("orbites sur les variables (moments d'ordre 1) : %d" % (tot["vars"] // order))
    for ty, v in tot_type.items():
        print("   type %-9s : %d orbites" % (ty, v // order))
    print("orbites sur les paires ordonnees (dim algebre commutante = somme m_lambda^2) : %d" % (tot["ordered_pairs"] // order))
    print("orbites sur les paires non ordonnees (moments d'ordre 2 distincts) : %d" % (tot["unordered_pairs"] // order))
    for (t1, t2), v in sorted(tot_pairs_by.items()):
        print("   paires ordonnees %-9s x %-9s : %d orbites" % (t1, t2, v // order))
