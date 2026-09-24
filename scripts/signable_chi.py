"""Une seule paire soeur p : quelles fonctions chi_p (fibre 10/10, bloc 4/4) sont « signables » (existe sigma avec (sbloc)) ? (notes/19 §6)
Enumeration exhaustive (2^20 au plus) ; pour chaque chi_p, test de (sbloc) par recherche sur les 20 signes.
Classes du multigraphe M_eps (paires {l,m} portant 0, 1 ou 2 orbites de chi = eps) et du type des orbites (+/-).
"""
import itertools, collections, sys
sys.path.insert(0, "scripts")
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
p = (6, 7)
B = [1, 2, 3, 4, 5]
pairs = list(itertools.combinations(B, 2))
orbs = [(r, e) for r in pairs for e in (0, 1)]          # e=0 : U+ (rep = e_a + e_b), e=1 : U- (rep = e_a - e_b)
def s_at(W, l):
    (a, b), e = W
    return 1 if l == a else (-1 if e else 1)
def ok_bloc(chi):
    if sum(chi.values()) != 10: return False
    for l in B:
        if sum(chi[W] for W in orbs if l in W[0]) != 4: return False
    return True
def signable(chi):
    pool = IDPool(); Z = {W: pool.id(W) for W in orbs}; cl = []
    for l in B:
        for e in (0, 1):
            lits = [(-Z[W] if s_at(W, l) == 1 else Z[W]) for W in orbs if l in W[0] and chi[W] == e]   # pi = +1
            cl += CardEnc.equals(lits=lits, bound=2, vpool=pool, encoding=EncType.seqcounter).clauses
    with Solver(name="cadical195", bootstrap_with=cl) as s:
        return s.solve()
tot = 0; sg = 0; shapes = collections.Counter(); shapes_ok = collections.Counter()
# enumeration par paire : pour chaque paire, (chi(U+), chi(U-)) in {00, 01, 10, 11}
for combo in itertools.product(range(4), repeat=10):
    chi = {}
    for (r, c) in zip(pairs, combo):
        chi[(r, 0)] = c & 1; chi[(r, 1)] = c >> 1
    if not ok_bloc(chi): continue
    tot += 1
    # forme : multigraphe des paires « doubles » (les deux orbites de meme chi) et « mixtes »
    dbl0 = tuple(sorted(r for r in pairs if chi[(r, 0)] == 0 and chi[(r, 1)] == 0))
    dbl1 = tuple(sorted(r for r in pairs if chi[(r, 0)] == 1 and chi[(r, 1)] == 1))
    key = (len(dbl0), len(dbl1))
    shapes[key] += 1
    if signable(chi):
        sg += 1; shapes_ok[key] += 1
print("chi_p (fibre+bloc) :", tot, " signables :", sg)
print("par (#paires doubles a 0, #paires doubles a 1) : total", dict(shapes))
print("                                          signables", dict(shapes_ok))
