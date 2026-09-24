"""Grille hors de x en C2 et conjecture de renormalisation (phi = reflexion ponctuelle).
Lemme (prouve a la main, notes/11) : si Lambda est une grille avec x hors de Lambda, alors Lambda et t.Lambda sont disjointes,
les aretes entre elles forment un couplage parfait pi, et phi = t o pi est une involution de Lambda de point fixe unique w = +e_1.
Conjecture : phi est la reflexion ponctuelle de Lambda en w ; en particulier phi(alpha) = beta, i.e. alpha ~ -beta.
Test : modele C2 exact + grille en e_1 entre les droites R1 = {e1, e1+a, e1+b} et C1 = {e1, e1+c, e1+d} (coins existentiels,
candidats restreints par la partition des etiquettes, consequence du code parfait) + NON(alpha ~ -beta).
UNSAT => phi(alpha) = beta force (non certifie).  Mono-fil, delai dur.
Usage : python grid_offx_phi.py <cas: SS|NN> <mode: phi|exist> <secondes>
"""
import os, sys, time, itertools, multiprocessing as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor")); sys.path.insert(0, HERE)
from grid_propagation import adj_lit
M = 7
CASES = {  # (a, b, c, d) demi-etiquettes (bloc, signe) ; blocs 2..7
    "SS": ((2, 1), (2, -1), (3, 1), (3, -1)),     # deux droites soeurs
    "NN": ((2, 1), (3, 1), (4, 1), (5, 1)),       # deux droites non soeurs, blocs disjoints
}

def worker(case, mode, q):
    import orbit_sat
    from pysat.solvers import Solver
    cnf, pool, outer, rep, trep, A, B = orbit_sat.build(M, "none")
    a, b, c, d = CASES[case]
    root = lambda h: {1: 1, h[0]: h[1]}
    al, be, ga, de = root(a), root(b), root(c), root(d)
    cnf.append([adj_lit(al, be, outer, A, B)]); cnf.append([adj_lit(ga, de, outer, A, B)])   # R1, C1 droites de M_{e1}
    used = {a, b, c, d}
    halves = [(j, s) for j in range(2, M + 1) for s in (1, -1) if (j, s) not in used]
    cand = [dict([h1, h2]) for h1, h2 in itertools.combinations(halves, 2) if h1[0] != h2[0]]
    def AND(*xs):
        z = pool.id(("and",) + tuple(xs)); cnf.extend([[-z, x] for x in xs]); cnf.append([z] + [-x for x in xs]); return z
    K = {}
    for p in (a, b):
        for r in (c, d):
            u, v = root(p), root(r)
            K[p, r] = [AND(adj_lit(g, u, outer, A, B), adj_lit(g, v, outer, A, B)) for g in cand]
    def rowcol(k1, k2):
        terms = []
        for x, g in enumerate(cand):
            for y, h in enumerate(cand):
                if x == y: continue
                e = adj_lit(g, h, outer, A, B)
                if e is None: continue
                terms.append(AND(K[k1][x], K[k2][y], e))
        rr = pool.id(("rc", k1, k2)); cnf.append([-rr] + terms); cnf.extend([[rr, -t] for t in terms]); return rr
    for (k1, k2) in (((a, c), (b, c)), ((a, d), (b, d)), ((a, c), (a, d)), ((b, c), (b, d))):
        cnf.append([rowcol(k1, k2)])                                     # la grille se ferme
    if mode == "phi":
        mb = {1: -1, b[0]: -b[1]}                                       # -beta
        cnf.append([-adj_lit(al, mb, outer, A, B)])                      # NON(alpha ~ -beta)
    t0 = time.time()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as sv:
        r = sv.solve()
        q.put(("SAT" if r else "UNSAT", time.time() - t0, len(cnf.clauses)))

if __name__ == "__main__":
    case, mode, T = sys.argv[1], sys.argv[2], float(sys.argv[3])
    q = mp.Queue(); p = mp.Process(target=worker, args=(case, mode, q)); p.start(); p.join(T)
    if p.is_alive():
        p.terminate(); p.join(); print("%s %s : TIMEOUT %.0f s" % (case, mode, T), flush=True)
    else:
        print("%s %s :" % (case, mode), q.get(), flush=True)
