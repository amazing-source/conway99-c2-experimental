"""Systeme chi signe, encodage « un parmi quatre » (notes/19 §6) : c_p(rep W) in G_p code par Y[p,W,(e,s)], e = orbite, s = signe.

Memes contraintes que schi_system (meme derivation), sans aucune variable XOR : chaque contrainte signee devient une cardinalite
sur des ET/OU de litteraux Y.  Sert (a) de controle croise d'encodage, (b) a tester si le CDCL s'en sort mieux sur les etoiles.
(aug) optionnelle : ligne (I) d'une orbite quelconque W au bloc l hors W (au plus 2 voisins de grille de chaque signe en l).
Usage : python schi_onehot.py <T> "12 16 17" [...]     (T : limite en secondes par instance, processus fils Idle)
"""
import itertools, sys, time
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType
sys.path.insert(0, "scripts")
from chi_system import ALLPAIRS, BLOCKS
from schi_system import s_at

G4 = [(e, s) for e in (0, 1) for s in (1, -1)]

def build(S, aug=False):
    S = [tuple(sorted(p)) for p in S]
    pool = IDPool(); cnf = CNF()
    def eq(lits, k):
        if k < 0 or k > len(lits):
            cnf.append([]); return
        cnf.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    def atmost(lits, k):
        cnf.extend(CardEnc.atmost(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    def AND(*lits):
        z = pool.id(("and",) + tuple(sorted(lits)))
        cnf.extend([[-z, l] for l in lits]); cnf.append([z] + [-l for l in lits]); return z
    def OR(*lits):
        z = pool.id(("or",) + tuple(sorted(lits)))
        cnf.append([-z] + list(lits)); cnf.extend([[z, -l] for l in lits]); return z
    disj = lambda a, b: not (set(a) & set(b))
    O = {p: [(r, e) for r in ALLPAIRS if disj(r, p) for e in (0, 1)] for p in S}
    Y = {(p, W, g): pool.id(("y", p, W, g)) for p in S for W in O[p] for g in G4}
    for p in S:
        for W in O[p]:
            eq([Y[p, W, g] for g in G4], 1)
    chi = {(p, W, e): OR(Y[p, W, (e, 1)], Y[p, W, (e, -1)]) for p in S for W in O[p] for e in (0, 1)}
    for p in S:                                                       # fibre, bloc, sbloc
        eq([chi[p, W, 1] for W in O[p]], 10)
        for l in BLOCKS:
            if l in p:
                continue
            Wl = [W for W in O[p] if l in W[0]]
            eq([chi[p, W, 1] for W in Wl], 4)
            for e in (0, 1):
                eq([Y[p, W, (e, s_at(W, l))] for W in Wl], 2)
    for p, q in itertools.combinations(S, 2):
        common = [W for W in O[p] if W in O[q]]
        if disj(p, q):
            for e in (0, 1):                                          # sbij (contient bij)
                for f in (0, 1):
                    for s in (1, -1):
                        a, b = Y[p, (q, f), (e, s)], Y[q, (p, e), (f, s)]
                        cnf.extend([[-a, b], [a, -b]])
            for e in (0, 1):                                          # disj : chi_q = chi_p + c(p,q), 3/3
                eq([chi[p, W, e] for W in common], 3)
                for f in (0, 1):
                    link = chi[q, (p, e), f]                          # chi_q(U_p^e) = f
                    for W in common:
                        cnf.append([-link, -chi[p, W, e], chi[q, W, f]])
            for e in (0, 1):                                          # sdisj
                lits = []
                for W in common:
                    terms = []
                    for s in (1, -1):
                        for f in (0, 1):
                            for t in (1, -1):
                                terms.append(AND(Y[p, W, (e, s)], Y[q, (p, e), (f, t)], Y[q, W, (f, s * t)]))
                    lits.append(OR(*terms))
                eq(lits, 1)
        elif len(set(p) & set(q)) == 1:
            (i,) = set(p) & set(q)
            for e in (0, 1):
                for f in (0, 1):
                    eq([AND(chi[p, W, e], chi[q, W, f]) for W in common], 3)                 # int
                    kap = s_at((p, e), i) * s_at((q, f), i)
                    lits = [OR(AND(Y[p, W, (e, 1)], Y[q, W, (f, kap)]), AND(Y[p, W, (e, -1)], Y[q, W, (f, -kap)])) for W in common]
                    eq(lits, 1)                                                                # sint
    if aug:
        for W in [(r, e) for r in ALLPAIRS for e in (0, 1)]:
            for l in BLOCKS:
                if l in W[0]:
                    continue
                P = [p for p in S if l in p and disj(p, W[0])]
                if len(P) < 3:
                    continue
                plus = [OR(*[Y[p, W, (e, s)] for (e, s) in G4 if s * s_at((p, e), l) == 1]) for p in P]
                atmost(plus, 2); atmost([-x for x in plus], 2)
    return cnf, pool, Y

def _w(E, aug, q):
    sys.path.insert(0, "scripts")
    from rs_experiments import idle
    idle()
    from pysat.solvers import Solver
    t0 = time.time(); cnf, pool, Y = build(E, aug)
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        r = s.solve()
    q.put(("SAT" if r else "UNSAT", time.time() - t0, pool.top, len(cnf.clauses)))

if __name__ == "__main__":
    import multiprocessing as mp
    T = float(sys.argv[1]); aug = "aug" in sys.argv[2:]
    for arg in [a for a in sys.argv[2:] if a != "aug"]:
        E = [tuple(sorted((int(x[0]), int(x[1])))) for x in arg.split()]
        q = mp.Queue(); pr = mp.Process(target=_w, args=(E, aug, q)); pr.start(); pr.join(T)
        if pr.is_alive():
            pr.terminate(); pr.join(); print("%-24s onehot%s : TIMEOUT %.0f s" % (arg, "+aug" if aug else "", T), flush=True)
        else:
            r = q.get(); print("%-24s onehot%s : %-5s %.1f s (%d vars, %d clauses)" % (arg, "+aug" if aug else "", r[0], r[1], r[2], r[3]), flush=True)
