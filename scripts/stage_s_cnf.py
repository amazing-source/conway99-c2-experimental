"""CNF de l'etage S seul (m = 7) pour kissat / cadical (+ DRAT si UNSAT).
Variables : P_op (S=+1), M_op (S=-1) pour o<p ; produits pp_{opk} (S_ok S_kp = +1), pn_{opk} (= -1).
Contraintes : poids de ligne 10 ; S C = 0 ; pour o != p : #pp - #pn = -G_op - S_op (compteurs unaires bornes a 10).
Usage : python stage_s_cnf.py out.cnf
"""
import sys, itertools, hashlib, os
import numpy as np
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType

m = 7
orb = [(i, j, t) for i in range(m) for j in range(i + 1, m) for t in (1, -1)]
N = len(orb)
C = np.zeros((N, m), dtype=int)
for o, (i, j, t) in enumerate(orb): C[o, i] = 1; C[o, j] = t
G = C @ C.T
pool = IDPool(); cnf = CNF()
Pv = {}; Mv = {}
for o in range(N):
    for p in range(o + 1, N):
        Pv[o, p] = pool.id(("P", o, p)); Mv[o, p] = pool.id(("M", o, p))
        cnf.append([-Pv[o, p], -Mv[o, p]])
P = lambda o, p: Pv[min(o, p), max(o, p)]
M = lambda o, p: Mv[min(o, p), max(o, p)]

def card_eq(lits, k):
    enc = CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.kmtotalizer)
    cnf.extend(enc.clauses)

# poids de ligne
for o in range(N):
    card_eq([P(o, p) for p in range(N) if p != o] + [M(o, p) for p in range(N) if p != o], 10)
# S C = 0 : #contributions + = #contributions -
for o in range(N):
    for i in range(m):
        plus, minus = [], []
        for p in range(N):
            if p == o or C[p, i] == 0: continue
            if C[p, i] == 1: plus.append(P(o, p)); minus.append(M(o, p))
            else: plus.append(M(o, p)); minus.append(P(o, p))
        # sum(plus) - sum(minus) = 0  <=>  sum(plus) + sum(not minus) = len(minus)
        card_eq(plus + [-x for x in minus], len(minus))

def AND(a, b):
    z = pool.id(("and", a, b))
    cnf.extend([[-z, a], [-z, b], [z, -a, -b]])
    return z
def OR2(a, b):
    z = pool.id(("or", a, b))
    cnf.extend([[z, -a], [z, -b], [-z, a, b]])
    return z

CAP = 11
for o in range(N):
    for p in range(o + 1, N):
        pp, pn = [], []
        for k in range(N):
            if k in (o, p): continue
            pp.append(OR2(AND(P(o, k), P(k, p)), AND(M(o, k), M(k, p))))
            pn.append(OR2(AND(P(o, k), M(k, p)), AND(M(o, k), P(k, p))))
        # a + b <= 10 (voisins communs) ; a - b + S = -G  <=>  sum(pp) + sum(not pn) + P + not M = 41 - G
        cnf.extend(CardEnc.atmost(lits=pp + pn, bound=10, vpool=pool, encoding=EncType.kmtotalizer).clauses)
        card_eq(pp + [-x for x in pn] + [P(o, p), -M(o, p)], 41 - int(G[o, p]))
cnf.to_file(sys.argv[1])
h = hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest()
print("CNF : %d variables, %d clauses, sha256 %s" % (pool.top, len(cnf.clauses), h))
