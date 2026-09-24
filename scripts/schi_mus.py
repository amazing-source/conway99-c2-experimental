"""Noyaux minimaux du systeme chi signe (notes/19) : quelles instances de contraintes (non signees et signees) suffisent a la contradiction.

Groupes : non signes (notes/18) bij(p,q), disjX(p,q), disjC(p,q), int(p,q), fibre(p), bloc(p,l) ;
          signes : sbij(p,q), sdisj(p,q), sint(p,q), sbloc(p,l).
Les definitions de variables auxiliaires (ET, XOR, multiplexeur) sont des extensions conservatives, toujours actives.
Minimisation par suppression (chaque retrait teste par SAT) -> ensemble minimal d'instances deja contradictoire.
Usage : python schi_mus.py "12 34 56 67" [...]
"""
import itertools, sys, time
from pysat.formula import IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver
sys.path.insert(0, "scripts")
from chi_system import ALLPAIRS, BLOCKS
from schi_system import s_at

def groups(S):
    S = [tuple(sorted(p)) for p in S]
    pool = IDPool(); G = {}; defs = []
    def eq(lits, k, sink):
        if k < 0 or k > len(lits):
            sink.append([]); return
        sink.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    def AND(*lits):
        z = pool.id(("and",) + tuple(sorted(lits)))
        defs.extend([[-z, l] for l in lits]); defs.append([z] + [-l for l in lits]); return z
    def XOR(a, b):
        z = pool.id(("xor",) + tuple(sorted((a, b))))
        defs.extend([[-z, a, b], [-z, -a, -b], [z, -a, b], [z, a, -b]]); return z
    disj = lambda a, b: not (set(a) & set(b))
    O = {p: [(r, e) for r in ALLPAIRS if disj(r, p) for e in (0, 1)] for p in S}
    X = {(p, W): pool.id(("chi", p, W)) for p in S for W in O[p]}
    Z = {(p, W): pool.id(("sgn", p, W)) for p in S for W in O[p]}
    lit = lambda v, val: v if val else -v
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
            cl = []; eq([X[p, W] for W in common], 3, cl); G["disjC(%s,%s)" % (nm(p), nm(q))] = cl
            cl = []
            for e in (0, 1):
                for f in (0, 1):
                    for z in (0, 1):
                        a = AND(lit(X[p, (q, f)], e), lit(Z[p, (q, f)], z))
                        b = AND(lit(X[q, (p, e)], f), lit(Z[q, (p, e)], z))
                        cl += [[-a, b], [a, -b]]
            G["sbij(%s,%s)" % (nm(p), nm(q))] = cl
            cl = []
            for e in (0, 1):
                lits = []
                for W in common:
                    m = pool.id(("mux", p, q, W))
                    x = X[p, W]; z0 = Z[q, (p, 0)]; z1 = Z[q, (p, 1)]
                    defs.extend([[x, -m, z0], [x, m, -z0], [-x, -m, z1], [-x, m, -z1]])
                    r = XOR(XOR(Z[q, W], Z[p, W]), m)
                    lits.append(AND(lit(x, e), -r))
                eq(lits, 1, cl)
            G["sdisj(%s,%s)" % (nm(p), nm(q))] = cl
        elif len(set(p) & set(q)) == 1:
            (i,) = set(p) & set(q)
            common = [W for W in O[p] if W in O[q]]
            cl = []
            for e in (0, 1):
                for f in (0, 1):
                    lits = []
                    for W in common:
                        lits.append(AND(lit(X[p, W], e), lit(X[q, W], f)))
                    eq(lits, 3, cl)
            G["int(%s,%s)" % (nm(p), nm(q))] = cl
            cl = []
            for e in (0, 1):
                for f in (0, 1):
                    kap = s_at((p, e), i) * s_at((q, f), i)
                    lits = []
                    for W in common:
                        d = XOR(Z[p, W], Z[q, W])
                        lits.append(AND(lit(X[p, W], e), lit(X[q, W], f), lit(d, kap == -1)))
                    eq(lits, 1, cl)
            G["sint(%s,%s)" % (nm(p), nm(q))] = cl
    for p in S:
        cl = []; eq([X[p, W] for W in O[p]], 10, cl); G["fibre(%s)" % nm(p)] = cl
        for l in BLOCKS:
            if l in p:
                continue
            cl = []; eq([X[p, W] for W in O[p] if l in W[0]], 4, cl); G["bloc(%s,%d)" % (nm(p), l)] = cl
            cl = []
            for e in (0, 1):
                lits = [AND(lit(X[p, W], e), lit(Z[p, W], s_at(W, l) == -1)) for W in O[p] if l in W[0]]
                eq(lits, 2, cl)
            G["sbloc(%s,%d)" % (nm(p), l)] = cl
    return G, defs, pool

def mus(S):
    G, defs, pool = groups(S)
    names = list(G)
    sel = {n: pool.id(("sel", n)) for n in names}
    s = Solver(name="cadical195", bootstrap_with=defs)
    for n in names:
        for c in G[n]:
            s.add_clause(c + [-sel[n]])
    if s.solve(assumptions=[sel[n] for n in names]):
        s.delete(); return None
    core = [n for n in names if sel[n] in set(s.get_core())]
    i = 0
    while i < len(core):
        trial = core[:i] + core[i + 1:]
        if not s.solve(assumptions=[sel[n] for n in trial]):
            core2 = set(s.get_core()); core = [n for n in trial if sel[n] in core2]
        else:
            i += 1
    s.delete()
    return core

if __name__ == "__main__":
    from rs_experiments import idle; idle()
    for arg in sys.argv[1:]:
        E = [tuple(sorted((int(x[0]), int(x[1])))) for x in arg.split()]
        t0 = time.time(); core = mus(E)
        if core is None:
            print("%s : SAT" % arg); continue
        print("%s : noyau minimal de %d instances (%.1f s)" % (arg, len(core), time.time() - t0))
        for n in sorted(core):
            print("    " + n)
