"""Allsib = connexion D4 sur le graphe de Kneser KG(7,2) (notes/17).  Modele reduit EXACT, petit SAT.

Allsib : les 21 paires de blocs sont soeurs (toutes les grilles par x existent).  Par le lemme S1 (notes/03, DERIVE) :
- chaque racine a ses 10 voisines de type II sur les 10 paires disjointes de la sienne, exactement une par paire ;
- deux racines de paires qui se coupent en un bloc ne sont jamais adjacentes ;
- pour p, q disjointes, l'adjacence P_p -> P_q est une bijection f_pq equivariante (t = -1) et qui preserve les soeurs :
  un element du groupe diedral D4 (permutations signees des 2 coordonnees).
Racine de P_p (p = {i<j}) : (a, b) = signes sur i et j.  Soeurs : differer d'une coordonnee.
Contraintes (toutes les autres conditions srg sont automatiques) :
  (LM) paires disjointes p, q, alpha in P_p, beta in P_q :
       sum_r [f_pr(alpha) = f_qr(beta)] + #{s soeur de alpha : s ~ beta} + #{s' soeur de beta : alpha ~ s'} = 2 - [alpha ~ beta]
       (r parcourt les 3 paires disjointes de p u q ; pas de voisin commun interieur) ;
  (H3) paires se coupant en un bloc i : alpha in P_ij, beta in P_ik :
       sum_{r dans [7]\\{i,j,k}} [f_{ij,r}(alpha) = f_{ik,r}(beta)] = 2 - [alpha, beta ont le meme signe sur i] ;
  (H4) alpha in P_p, bloc k hors de p, signe e : #{l : la voisine de alpha sur {k,l} a le signe e sur k} = 2.
Usage : python allsib_connection.py [familles : LM,H3,H4]
"""
import itertools, sys, time
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver

B = range(1, 8)
PAIRS = [tuple(p) for p in itertools.combinations(B, 2)]
SQ = [(a, b) for a in (1, -1) for b in (1, -1)]
D4 = [(w, s1, s2) for w in (0, 1) for s1 in (1, -1) for s2 in (1, -1)]   # (a,b) -> (s1*x, s2*y), (x,y) = (a,b) ou (b,a)

def apply(g, ab):
    w, s1, s2 = g
    x, y = (ab if w == 0 else (ab[1], ab[0]))
    return (s1 * x, s2 * y)

def build(families):
    pool = IDPool(); cnf = CNF()
    def eq(lits, k):
        if k < 0 or k > len(lits):
            cnf.append([]); return
        cnf.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    F = {}
    for p, q in itertools.combinations(PAIRS, 2):
        if set(p) & set(q):
            continue
        lits = [pool.id(("f", p, q, g)) for g in D4]
        eq(lits, 1)
        F[p, q] = lits
    # adj(p, alpha, q, beta)
    ADJ = {}
    for (p, q), lits in F.items():
        for al in SQ:
            for be in SQ:
                v = pool.id(("adj", p, al, q, be))
                src = [lits[i] for i, g in enumerate(D4) if apply(g, al) == be]
                cnf.append([-v] + src); cnf.extend([[v, -l] for l in src])
                ADJ[p, al, q, be] = v; ADJ[q, be, p, al] = v
    def adj(p, al, q, be):
        return ADJ[p, al, q, be]
    def common(p, al, q, be, r):
        terms = []
        for ga in SQ:
            z = pool.id(("and", p, al, q, be, r, ga))
            x1, x2 = adj(p, al, r, ga), adj(q, be, r, ga)
            cnf.extend([[-z, x1], [-z, x2], [z, -x1, -x2]])
            terms.append(z)
        return terms
    sisters = lambda ab: [(-ab[0], ab[1]), (ab[0], -ab[1])]
    if "LM" in families:
        for (p, q) in F:
            rest = [r for r in PAIRS if not (set(r) & (set(p) | set(q)))]
            for al in SQ:
                for be in SQ:
                    lits = []
                    for r in rest:
                        lits += common(p, al, q, be, r)
                    lits += [adj(p, s, q, be) for s in sisters(al)] + [adj(p, al, q, s) for s in sisters(be)]
                    a = adj(p, al, q, be)
                    # sum(lits) + a = 2
                    eq(lits + [a], 2)
    if "H3" in families:
        for i in B:
            others = [x for x in B if x != i]
            for j, k in itertools.permutations(others, 2):
                if j > k:
                    continue
                p, q = tuple(sorted((i, j))), tuple(sorted((i, k)))
                rest = [r for r in PAIRS if not (set(r) & {i, j, k})]
                for al in SQ:
                    for be in SQ:
                        si = al[p.index(i)]; sj = be[q.index(i)]
                        lits = []
                        for r in rest:
                            lits += common(p, al, q, be, r)
                        eq(lits, 2 - (1 if si == sj else 0))
    if "H4" in families:
        for p in PAIRS:
            for al in SQ:
                for k in B:
                    if k in p:
                        continue
                    for e in (1, -1):
                        lits = []
                        for l in B:
                            if l in p or l == k:
                                continue
                            q = tuple(sorted((k, l)))
                            for be in SQ:
                                if be[q.index(k)] == e:
                                    lits.append(adj(p, al, q, be))
                        eq(lits, 2)
    return cnf, pool

if __name__ == "__main__":
    fams = sys.argv[1].split(",") if len(sys.argv) > 1 else ["LM", "H3", "H4"]
    t0 = time.time()
    cnf, pool = build(fams)
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        r = s.solve()
        print("familles %-10s : %s  (vars %d, clauses %d, %.1f s)" % (",".join(fams), "SAT" if r else "UNSAT", pool.top, len(cnf.clauses), time.time() - t0))
