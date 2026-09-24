"""Systeme chi des paires soeurs (notes/18) : relaxation EXACTE (niveau orbites, etage Q) d'une configuration Sigma de paires soeurs.

Pour une paire soeur p (grille par x), le lemme S1 (notes/03) donne c_p : racines evitant p -> P_p, t-equivariante, fibres de taille 10.
chi_p(W) in Z2 (W orbite sous t d'une paire disjointe de p) = orbite (produit +/-) de P_p atteinte.  Q[U_p^e, W] = [chi_p(W) = e].
Contraintes, toutes derivees de l'identite de l'etage Q  sum_W Q[U,W]Q[V,W] + Q[U,V] = 4 - Sh[U,V]  et des sommes par bloc (notes/18) :
  (bij)    p, r soeurs disjointes : chi_p(U_r^-) = 1 + chi_p(U_r^+) ;  c(p,r) := chi_p(U_r^+) = chi_r(U_p^+)   (symetrie de Q) ;
  (disj)   p, q soeurs disjointes : chi_q(W) = chi_p(W) + c(p,q) sur les 6 orbites evitant p u q, et #{chi_p(W) = 1} = 3 ;
  (int)    p = ij, p' = ik soeurs : sur les 12 orbites evitant {i,j,k}, #{(chi_p, chi_p') = (e, e')} = 3 pour chaque (e, e') ;
  (fibre)  #{W in O_p : chi_p(W) = 1} = 10 ;
  (bloc)   pour chaque bloc l hors de p : parmi les 8 orbites des paires {l,m} disjointes de p, exactement 4 ont chi_p = 1.
Semantique « au moins ces paires soeurs » : les paires non listees sont libres (relaxation).  UNSAT => la configuration est impossible.
Usage : python chi_system.py [config ...]   (sans argument : toutes les configurations certifiees)
"""
import itertools, sys, time
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver

CONFIGS = {}
for line in list(open("data/cnf/MANIFEST.txt", encoding="utf-8")) + list(open("data/cnf/MANIFEST_chi.txt", encoding="utf-8")):
    name = line.split()[1].replace(".cnf", "")
    pairs = line.split("pairs=[")[1].split("]")[0].split()
    CONFIGS[name] = [tuple(sorted((int(p[0]), int(p[1])))) for p in pairs]

BLOCKS = range(1, 8)
ALLPAIRS = [p for p in itertools.combinations(BLOCKS, 2)]

def build(S, families=("bij", "disj", "int", "fibre", "bloc")):
    S = [tuple(sorted(p)) for p in S]
    pool = IDPool(); cnf = CNF()
    def eq(lits, k):
        if k < 0 or k > len(lits):
            cnf.append([]); return
        cnf.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    disj = lambda a, b: not (set(a) & set(b))
    O = {p: [(r, e) for r in ALLPAIRS if disj(r, p) for e in (0, 1)] for p in S}
    X = {(p, W): pool.id(("chi", p, W)) for p in S for W in O[p]}
    def xor_eq(a, b, c):          # a = b xor c  (c booleen litteral)
        cnf.extend([[-a, b, c], [-a, -b, -c], [a, -b, c], [a, b, -c]])
    for p, q in itertools.combinations(S, 2):
        if not disj(p, q):
            continue
        if "bij" in families:
            cnf.extend([[X[p, (q, 0)], X[p, (q, 1)]], [-X[p, (q, 0)], -X[p, (q, 1)]]])
            cnf.extend([[X[q, (p, 0)], X[q, (p, 1)]], [-X[q, (p, 0)], -X[q, (p, 1)]]])
            a, b = X[p, (q, 0)], X[q, (p, 0)]
            cnf.extend([[-a, b], [a, -b]])                      # c(p,q) = c(q,p)
        if "disj" in families:
            c = X[p, (q, 0)]
            common = [W for W in O[p] if W in O[q]]
            for W in common:
                xor_eq(X[q, W], X[p, W], c)
            eq([X[p, W] for W in common], 3)
    if "int" in families:
        for p, q in itertools.combinations(S, 2):
            if len(set(p) & set(q)) != 1:
                continue
            common = [W for W in O[p] if W in O[q]]
            for e in (0, 1):
                for f in (0, 1):
                    lits = []
                    for W in common:
                        z = pool.id(("and", p, q, W, e, f))
                        a = X[p, W] if e else -X[p, W]
                        b = X[q, W] if f else -X[q, W]
                        cnf.extend([[-z, a], [-z, b], [z, -a, -b]])
                        lits.append(z)
                    eq(lits, 3)
    for p in S:
        if "fibre" in families:
            eq([X[p, W] for W in O[p]], 10)
        if "bloc" in families:
            for l in BLOCKS:
                if l in p:
                    continue
                eq([X[p, W] for W in O[p] if l in W[0]], 4)
    return cnf, pool

def run(name, S, families=("bij", "disj", "int", "fibre", "bloc"), T=60.0):
    t0 = time.time()
    cnf, pool = build(S, families)
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        r = s.solve()
    return ("SAT" if r else "UNSAT"), time.time() - t0, pool.top

if __name__ == "__main__":
    names = sys.argv[1:] or list(CONFIGS)
    for n in names:
        res, dt, nv = run(n, CONFIGS[n])
        print("%-16s %-40s %-5s (%d vars, %.2f s)" % (n, " ".join("%d%d" % p for p in CONFIGS[n]), res, nv, dt), flush=True)
