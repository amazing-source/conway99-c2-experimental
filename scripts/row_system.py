"""Systeme des lignes RS(S) de l'etage Q (notes/19).

RS(S) := les contraintes de l'etage Q (vendor/stage_q.constraints, encodage valide du depot, INCHANGE) dont le support est contenu
dans les lignes de S, c.-a-d. qui ne font intervenir que des entrees Q[U,W] avec U dans S (ou W dans S) :
  - pour U dans S : somme de ligne = 12 ; exactement un Q = 2 (partenaire D) ; sommes par bloc (2 ou 4) ;
  - pour U != U' dans S : Gram  sum_W Q[U,W] Q[U',W] + Q[U,U'] = 4 - Sh[U,U'] ;
  - (automatiquement) les contraintes dont tout le support tombe dans les lignes de S pour une autre raison.
C'est un sous-ensemble des contraintes de l'etage Q, donc une relaxation : RS(S) + donnees UNSAT  =>  etage Q + donnees UNSAT
=> modele complet + donnees UNSAT.  RS(toutes les orbites) = etage Q.
Donnees optionnelles :
  sigma = ensemble E de paires {i,j} :  pour toute paire r dont une orbite est dans S, Y[U_r^+,U_r^-] = [r dans E]  (Sigma exact sur S) ;
  dpairs = paires d'orbites (U,V) imposees partenaires D (Y = 1).
Le systeme chi (notes/18) est RS(orbites soeurs) compresse par le lemme S1 (verifie ici numeriquement : notes/19 §1).
"""
import itertools, sys, os
from pysat.formula import CNF, IDPool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
import stage_q

_CACHE = {}
def base(m=7):
    if m not in _CACHE:
        outer, X, Y, top = stage_q.primaries(m)
        cons = list(stage_q.constraints(m))
        owner = {}                                   # id primaire -> paire (U,V), U<V
        for (U, V), x in X.items():
            if U < V:
                owner[x] = (U, V); owner[Y[U, V]] = (U, V)
        supp = []
        for c in cons:
            ids = set()
            if c[0] == "clause":
                ids = {abs(l) for l in c[1]}
            else:
                for t in c[1]:
                    ids.update(t if isinstance(t, tuple) else (abs(t),))
            supp.append(frozenset(owner[i] for i in ids))
        _CACHE[m] = (outer, X, Y, top, cons, supp)
    return _CACHE[m]

def frame(m=7):
    return stage_q.frame(m)

def orbit(i, j, e, m=7):
    outer = base(m)[0]
    return outer.index((min(i, j), max(i, j), e))

def select(S, m=7):
    """Indices des contraintes de RS(S)."""
    outer, X, Y, top, cons, supp = base(m)
    S = set(S)
    return [k for k, sp in enumerate(supp) if all(U in S or V in S for (U, V) in sp)]

def build(S, sigma=None, dpairs=(), m=7, extra_clauses=()):
    outer, X, Y, top, cons, supp = base(m)
    pool = IDPool(start_from=top + 1); cnf = CNF(); prodmap = {}
    for k in select(S, m):
        stage_q.encode(cons[k], pool, cnf, prodmap)
    if sigma is not None:
        E = set(tuple(sorted(p)) for p in sigma)
        pairs = sorted({outer[U][:2] for U in S})
        for (i, j) in pairs:
            y = Y[outer.index((i, j, 0)), outer.index((i, j, 1))]
            cnf.append([y] if (i, j) in E else [-y])
    for U, V in dpairs:
        cnf.append([Y[U, V]])
    for c in extra_clauses:
        cnf.append(list(c))
    return cnf, pool

def orbits_on(blocks, m=7):
    """Orbites portees par les paires contenues dans l'ensemble de blocs donne."""
    outer = base(m)[0]
    B = set(blocks)
    return [U for U, (i, j, e) in enumerate(outer) if i in B and j in B]
