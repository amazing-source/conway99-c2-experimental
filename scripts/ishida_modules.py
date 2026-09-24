"""Identite d'Ishida (quotient de Brauer) tr(t.E) = rang_F2(E[F,F] mod 2) sur les modules de permutation derives de Gamma (C2).
E : idempotent 2-entier issu de l'algebre de Bose-Mesner, commutant avec t ; F : elements fixes par t.
Modules : sommets (F = {x}), droites (231, F = 7 droites de x), aretes (693, F = 7 aretes {e_i,-e_i}),
carres mu (2079, F = 21 carres D).  Calcul exact en fractions ; aucune donnee inconnue du graphe n'intervient
sauf e = #aretes entre deux carres D (toujours pair).  Resultat attendu : identite verifiee partout (mecanisme vide).
"""
from fractions import Fraction as Fr

E = {  # idempotents de srg(99,14,1,2) : valeur selon la distance (0, 1, 2)
    14: {0: Fr(1, 99), 1: Fr(1, 99), 2: Fr(1, 99)},
    3: {0: Fr(6, 11), 1: Fr(9, 77), 2: Fr(-2, 77)},
    -4: {0: Fr(4, 9), 1: Fr(-8, 63), 2: Fr(1, 63)},
}
TR = {14: 1, 3: 0, -4: 0}  # tr(t | V_theta) en C2 (force par les parametres)

def mod2(q):
    assert q.denominator % 2 == 1, q
    return q.numerator % 2

def rank2(rows):
    rows = [r[:] for r in rows]; r = 0
    for c in range(len(rows[0]) if rows else 0):
        piv = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c]: rows[i] = [(a ^ b) for a, b in zip(rows[i], rows[r])]
        r += 1
    return r

def d(p, q):  # distances dans la boule de x : ('x',) ou ('e', i, s)
    if p == q: return 0
    if p[0] == 'x' or q[0] == 'x': return 1
    return 1 if p[1] == q[1] else 2

out = []
# 1. sommets
for th in (14, 3, -4):
    out.append("sommets  theta=%3d : E[x,x]=%s  rang=%d  tr=%d" % (th, E[th][0], mod2(E[th][0]), TR[th]))
# 2. droites : N N^T = A + 7I (valeurs propres 21, 10, 3) ; E_odd = I - N^T (E14/21 + E-4/3) N projette sur N^T V3 + ker N
line = lambda i: [('x',), ('e', i, 1), ('e', i, -1)]
def Eodd(i, j):
    s = sum(E[14][d(p, q)] / 21 + E[-4][d(p, q)] / 3 for p in line(i) for q in line(j))
    return (1 if i == j else 0) - s
M = [[Eodd(i, j) for j in range(7)] for i in range(7)]
r = rank2([[mod2(M[i][j]) for j in range(7)] for i in range(7)])
out.append("droites  E_odd : diag=%s horsdiag=%s  rang_F2=%d  tr=tr(t|V3)+tr(t|ker N)=0+(7-1)=6" % (M[0][0], M[0][1], r))
# 3. aretes : B B^T = A + 14I (28, 17, 10) ; E' = B^T E3 B / 17 (seul idempotent 2-entier non trivial)
edge = lambda i: [('e', i, 1), ('e', i, -1)]
Ed = lambda i, j: sum(E[3][d(p, q)] for p in edge(i) for q in edge(j)) / 17
out.append("aretes   E'=B^T E3 B/17 : diag=%s horsdiag=%s  (mod 2 : %d, %d)  rang=0  tr=tr(t|V3)=0"
           % (Ed(0, 0), Ed(0, 1), mod2(Ed(0, 0)), mod2(Ed(0, 1))))
# 4. carres mu : Q Q^T = 83I + 11A + J (336, 116, 39) ; E = Q^T E-4 Q / 39
diag = (4 * E[-4][0] + 8 * E[-4][1] + 4 * E[-4][2]) / 39
out.append("carres   E=Q^T E-4 Q/39 : diag=%s (mod 2 : %d)" % (diag, mod2(diag)))
for e in range(0, 9, 2):
    off = (e * E[-4][1] + (16 - e) * E[-4][2]) / 39
    out.append("         e=%d aretes entre deux carres D : %s (mod 2 : %d)" % (e, off, mod2(off)))
out.append("         => E[F] = 0 mod 2 : rang 0 = tr(t|V-4) = 0")
print("\n".join(out))
