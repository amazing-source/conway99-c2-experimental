"""Noyaux minimaux (MUS au niveau des familles de contraintes) du systeme chi pour les atomes (notes/18).

Chaque instance de contrainte recoit un selecteur :
  bij(p,q) ; disjX(p,q) (relations chi_q = chi_p + c sur les 6 orbites) ; disjC(p,q) (repartition 3/3) ;
  int(p,q) (les 4 comptes = 3) ; fibre(p) ; bloc(p,l).
On extrait un noyau UNSAT puis on le minimise par suppression (chaque retrait teste par SAT) : le resultat est un ensemble minimal
d'instances dont la conjonction est deja contradictoire.  C'est le squelette de la preuve humaine.
Usage : python chi_mus.py chi_atom01 [...]
"""
import itertools, sys, time
from pysat.formula import IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver
sys.path.insert(0, "scripts")
from chi_system import CONFIGS, ALLPAIRS, BLOCKS

def groups(S):
    S = [tuple(sorted(p)) for p in S]
    pool = IDPool(); G = {}          # nom -> liste de clauses
    def eq(lits, k, sink):
        sink.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    disj = lambda a, b: not (set(a) & set(b))
    O = {p: [(r, e) for r in ALLPAIRS if disj(r, p) for e in (0, 1)] for p in S}
    X = {(p, W): pool.id(("chi", p, W)) for p in S for W in O[p]}
    nm = lambda p: "%d%d" % p
    for p, q in itertools.combinations(S, 2):
        if disj(p, q):
            cl = [[X[p, (q, 0)], X[p, (q, 1)]], [-X[p, (q, 0)], -X[p, (q, 1)]],
                  [X[q, (p, 0)], X[q, (p, 1)]], [-X[q, (p, 0)], -X[q, (p, 1)]]]
            a, b = X[p, (q, 0)], X[q, (p, 0)]
            cl += [[-a, b], [a, -b]]
            G["bij(%s,%s)" % (nm(p), nm(q))] = cl
            c = X[p, (q, 0)]
            common = [W for W in O[p] if W in O[q]]
            cl = []
            for W in common:
                x, y = X[q, W], X[p, W]
                cl += [[-x, y, c], [-x, -y, -c], [x, -y, c], [x, y, -c]]
            G["disjX(%s,%s)" % (nm(p), nm(q))] = cl
            cl = []; eq([X[p, W] for W in common], 3, cl)
            G["disjC(%s,%s)" % (nm(p), nm(q))] = cl
        elif len(set(p) & set(q)) == 1:
            common = [W for W in O[p] if W in O[q]]
            cl = []
            for e in (0, 1):
                for f in (0, 1):
                    lits = []
                    for W in common:
                        z = pool.id(("and", p, q, W, e, f))
                        a = X[p, W] if e else -X[p, W]
                        b = X[q, W] if f else -X[q, W]
                        cl += [[-z, a], [-z, b], [z, -a, -b]]
                        lits.append(z)
                    eq(lits, 3, cl)
            G["int(%s,%s)" % (nm(p), nm(q))] = cl
    for p in S:
        cl = []; eq([X[p, W] for W in O[p]], 10, cl); G["fibre(%s)" % nm(p)] = cl
        for l in BLOCKS:
            if l in p:
                continue
            cl = []; eq([X[p, W] for W in O[p] if l in W[0]], 4, cl); G["bloc(%s,%d)" % (nm(p), l)] = cl
    return G, pool

def mus(S):
    G, pool = groups(S)
    names = list(G)
    sel = {n: pool.id(("sel", n)) for n in names}
    s = Solver(name="cadical195")
    for n in names:
        for c in G[n]:
            s.add_clause(c + [-sel[n]])
    assert not s.solve(assumptions=[sel[n] for n in names])
    core = [n for n in names if sel[n] in set(s.get_core())]
    i = 0
    while i < len(core):
        trial = core[:i] + core[i + 1:]
        if not s.solve(assumptions=[sel[n] for n in trial]):
            core2 = set(s.get_core())
            core = [n for n in trial if sel[n] in core2]
        else:
            i += 1
    s.delete()
    return core

if __name__ == "__main__":
    for name in sys.argv[1:]:
        t0 = time.time()
        core = mus(CONFIGS[name])
        print("%s [%s] : noyau minimal de %d instances (%.1f s)" % (name, " ".join("%d%d" % p for p in CONFIGS[name]), len(core), time.time() - t0))
        for n in sorted(core):
            print("    " + n)
