"""Systeme des lignes SIGNE RSF(S) : le modele complet (vendor/orbit_sat.build, variables a,b) restreint aux lignes de S (notes/19).

Construction : copie ligne a ligne de orbit_sat.build (meme ordre d'appels, memes identifiants), avec un filtre de support :
une contrainte est gardee ssi toutes ses variables a[U,V], b[U,V] ont U dans S ou V dans S.
  (R),(D),(I) de la ligne U : gardees ssi U dans S (ou S contient toutes les autres orbites) ;
  (P) du couple (U,V) : gardees ssi toutes les entrees (U,W),(V,W),(U,V) tombent dans les lignes de S.
RSF(toutes les orbites) = orbit_sat.build(7,"none") a l'identique (verifie par sha256 contre data/cnf/MANIFEST.txt, notes/19 §1).
Relaxation du modele complet : RSF(S) + donnees UNSAT  =>  modele complet + donnees UNSAT.
sigma (paires soeurs, semantique « au moins ») : clauses [a[U0,U1]], [b[U0,U1]] comme scripts/make_cnf.py ;
sigma_exact : en plus, pour les paires r (dont une orbite est dans S) hors sigma : [-a, -b].
"""
import itertools, sys, os
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType

def build(S, m=7, sigma=(), sigma_exact=False, dpairs=()):
    k = 2 * m
    outer = [(i, j, e) for i in range(1, m + 1) for j in range(i + 1, m + 1) for e in (0, 1)]
    N = len(outer)
    rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
    trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
    S = set(S)
    inrow = lambda U, V: U in S or V in S
    pool = IDPool(); cnf = CNF()
    A = {}; B = {}
    for U in range(N):
        for V in range(U + 1, N):
            A[U, V] = A[V, U] = pool.id(("a", U, V)); B[U, V] = B[V, U] = pool.id(("b", U, V))
    def prod(x, y):
        p = pool.id(("p", min(x, y), max(x, y)))
        cnf.extend([[-p, x], [-p, y], [p, -x, -y]]); return p
    def eq(lits, kk):
        if not lits:
            assert kk == 0, "unsatisfiable constant constraint"; return
        if kk < 0 or kk > len(lits):
            cnf.append([]); return
        cnf.extend(CardEnc.equals(lits=lits, bound=kk, vpool=pool, encoding=EncType.seqcounter).clauses)
    inner = [(i, s) for i in range(1, m + 1) for s in (0, 1)]
    for U in range(N):
        others = [V for V in range(N) if V != U]
        if not all(inrow(U, V) for V in others):
            continue
        eq([A[U, V] for V in others] + [B[U, V] for V in others], k - 2)                      # (R)
        eq([prod(A[U, V], B[U, V]) for V in others], 1)                                         # (D)
        for c in inner:                                                                         # (I)
            partner = (c[0], 1 - c[1]); lits = []
            for V in others:
                if c in rep[V]: lits.append(A[U, V])
                if c in trep[V]: lits.append(B[U, V])
            eq(lits, 1 if (c in rep[U] or partner in rep[U]) else 2)
    for U in range(N):                                                                          # (P)
        for V in range(U + 1, N):
            Ws = [W for W in range(N) if W != U and W != V]
            if not (inrow(U, V) and all(inrow(U, W) and inrow(V, W) for W in Ws)):
                continue
            same = [prod(A[U, W], A[V, W]) for W in Ws] + [prod(B[U, W], B[V, W]) for W in Ws]
            cross = [prod(A[U, W], B[V, W]) for W in Ws] + [prod(B[U, W], A[V, W]) for W in Ws]
            eq(same + [A[U, V]], 2 - len(rep[U] & rep[V]))
            eq(cross + [B[U, V]], 2 - len(rep[U] & trep[V]))
    extra = []
    for (i, j) in sigma:
        U = outer.index((i, j, 0)); V = outer.index((i, j, 1))
        extra += [[A[U, V]], [B[U, V]]]
    if sigma_exact:
        E = set(tuple(sorted(p)) for p in sigma)
        for (i, j) in sorted({outer[U][:2] for U in S}):
            if (i, j) in E: continue
            U = outer.index((i, j, 0)); V = outer.index((i, j, 1))
            extra.append([-A[U, V], -B[U, V]])
    for U, V in dpairs:
        extra += [[A[U, V]], [B[U, V]]]
    return cnf.clauses + extra, pool.top, outer, A, B

def orbit(i, j, e, m=7):
    return [(a, b, c) for a in range(1, m + 1) for b in range(a + 1, m + 1) for c in (0, 1)].index((min(i, j), max(i, j), e))

if __name__ == "__main__":
    # validation : RSF(toutes) + paires de K2K2P3 doit reproduire data/cnf/K2K2P3.cnf octet pour octet (sha256 du MANIFEST)
    import hashlib
    pairs_s = "12 34 56 67"
    pairs = [(int(x[0]), int(x[1])) for x in pairs_s.split()]
    clauses, nv, outer, A, B = build(range(42), sigma=pairs)
    h = hashlib.sha256()
    head = "c C2 orbit model m=7, sib pairs %s%s\np cnf %d %d\n" % (pairs_s, "", nv, len(clauses))
    h.update(head.encode())
    for c in clauses:
        h.update((" ".join(map(str, c)) + " 0\n").encode())
    ref = [l.split()[0] for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "cnf", "MANIFEST.txt")) if " K2K2P3.cnf " in l][0]
    print("RSF(toutes)+K2K2P3 : vars=%d clauses=%d sha256=%s  reference=%s  %s" % (nv, len(clauses), h.hexdigest(), ref, "IDENTIQUE" if h.hexdigest() == ref else "DIFFERENT"))
