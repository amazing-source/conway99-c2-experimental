"""Validation du propagateur de Gauss (notes/22) : K13 (lignes soeurs de {1,2},{1,3},{1,4}) + les 18 faits A/B du lemme des etoiles
ajoutes comme contraintes de cardinalite (ce sont des consequences certifiees DRAT). Compare cadical seul et cadical + Gauss."""
import sys, os, time, multiprocessing as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)

def build():
    import row_system_full as R
    from rs_experiments import sister_orbits
    from star_lemma_check import outer, idx, rep, trep
    from pysat.formula import IDPool
    from pysat.card import CardEnc, EncType
    c, L = 1, (2, 3, 4); E = [(1, x) for x in L]
    cl, nv, outer_, A, B = R.build(sister_orbits(E), sigma=E)
    pool = IDPool(start_from=nv + 1); extra = []
    for x in L:                                   # faits A : compte = 4
        for l in L:
            if l == x: continue
            lits = []
            for W, (i, j, e) in enumerate(outer):
                if l not in (i, j) or {i, j} & {c, x}: continue
                for U in (idx[(c, x, 0)], idx[(c, x, 1)]):
                    if (l, 0) in rep[W]: lits.append(A[U, W])
                    if (l, 0) in trep[W]: lits.append(B[U, W])
            extra += CardEnc.equals(lits=lits, bound=4, vpool=pool, encoding=EncType.seqcounter).clauses
    for (x, y) in ((2, 3), (2, 4), (3, 4)):         # faits B : somme (P)-same = 1
        for e in (0, 1):
            for f in (0, 1):
                U = idx[(c, x, e)]; V = idx[(c, y, f)]; terms = []
                for W, (i, j, ee) in enumerate(outer):
                    if {i, j} & {c, x, y}: continue
                    for (p, q) in ((A[U, W], A[V, W]), (B[U, W], B[V, W])):
                        z = pool.id(("t", p, q)); extra += [[-z, p], [-z, q], [z, -p, -q]]; terms.append(z)
                extra += CardEnc.equals(lits=terms, bound=1, vpool=pool, encoding=EncType.seqcounter).clauses
    return cl + extra, sister_orbits(E), A, B, outer_

def child(mode, q):
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    from pysat.solvers import Solver
    from gauss_propagator import parity_constraints, GaussBilinear
    cl, S, A, B, outer = build()
    s = Solver(name="cadical195", bootstrap_with=cl); prop = None
    if mode == "gauss":
        prop = GaussBilinear(parity_constraints(S, A, B, outer)); s.connect_propagator(prop)
        for v in prop.vars: s.observe(v)
    t0 = time.time(); r = s.solve()
    q.put((r, round(time.time() - t0, 1), prop.stats if prop else None))

if __name__ == "__main__":
    mode, T = sys.argv[1], float(sys.argv[2])
    q = mp.Queue(); p = mp.Process(target=child, args=(mode, q)); p.start(); p.join(T)
    if p.is_alive():
        p.terminate(); p.join(); print("K13 + faits A/B, %s : TIMEOUT %.0f s" % (mode, T))
    else:
        print("K13 + faits A/B, %s :" % mode, q.get(timeout=10))
