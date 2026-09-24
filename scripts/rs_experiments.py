"""Experiences sur le systeme des lignes RS(S) (scripts/row_system.py, notes/19).

  python rs_experiments.py validate                 # m=2 SAT, m=3 UNSAT, RS(tout) = etage Q (memes contraintes)
  python rs_experiments.py chi <sec>                # RS(orbites soeurs) vs systeme chi : 11 atomes (UNSAT attendu), 12 chi-SAT maximaux
  python rs_experiments.py local <b> <sec> [i0 i1]  # B = {1..b}, S = orbites(B), Sigma exact = H pour chaque graphe H a b sommets
Chaque resolution tourne dans un processus fils (priorite Idle), coupe a <sec> secondes ; memoire libre surveillee (< 3 Go -> arret).
"""
import sys, os, time, itertools, multiprocessing as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "vendor"))

def idle():
    try:
        import ctypes; k = ctypes.windll.kernel32
        k.GetCurrentProcess.restype = ctypes.c_void_p; k.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        k.SetPriorityClass(k.GetCurrentProcess(), 0x40)
    except Exception:
        pass

def free_gb():
    try:
        import ctypes
        class MS(ctypes.Structure):
            _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong), ("ullTotalPhys", ctypes.c_ulonglong),
                        ("ullAvailPhys", ctypes.c_ulonglong), ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                        ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong), ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
        s = MS(); s.dwLength = ctypes.sizeof(MS); ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(s))
        return s.ullAvailPhys / 2 ** 30
    except Exception:
        return 99.0

def _worker(S, sigma, dpairs, m, extra, q):
    idle()
    import row_system
    from pysat.solvers import Solver
    t0 = time.time()
    cnf, pool = row_system.build(S, sigma=sigma, dpairs=dpairs, m=m, extra_clauses=extra)
    tb = time.time() - t0
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        r = s.solve()
        model = s.get_model() if r else None
    outer, X, Y = row_system.base(m)[:3]
    Q = None
    if model:
        val = set(l for l in model if l > 0)
        Q = {}
        for U in set(S):
            for V in range(len(outer)):
                if V != U:
                    Q[U, V] = (X[U, V] in val) + (Y[U, V] in val)
    q.put(("SAT" if r else "UNSAT", round(tb, 1), round(time.time() - t0 - tb, 1), len(cnf.clauses), Q))

def solve(S, sigma=None, dpairs=(), m=7, T=60.0, extra=()):
    if free_gb() < 3.0:
        raise SystemExit("memoire libre < 3 Go : arret")
    q = mp.Queue(); p = mp.Process(target=_worker, args=(list(S), sigma, list(dpairs), m, list(extra), q)); p.start()
    t0 = time.time()
    while p.is_alive() and time.time() - t0 < T:
        p.join(1.0)
        if free_gb() < 3.0:
            p.terminate(); p.join(); return ("MEMSTOP", 0, round(time.time() - t0, 1), 0, None)
    if p.is_alive():
        p.terminate(); p.join(); return ("TIMEOUT", 0, T, 0, None)
    try:
        return q.get(timeout=10)
    except Exception:
        return ("ERREUR", 0, 0, 0, None)

def _worker_full(S, sigma, sigma_exact, dpairs, q):
    idle()
    import row_system_full
    from pysat.solvers import Solver
    t0 = time.time()
    clauses, nv, outer, A, B = row_system_full.build(S, sigma=sigma, sigma_exact=sigma_exact, dpairs=dpairs)
    tb = time.time() - t0
    with Solver(name="cadical195", bootstrap_with=clauses) as s:
        r = s.solve()
    q.put(("SAT" if r else "UNSAT", round(tb, 1), round(time.time() - t0 - tb, 1), len(clauses), None))

def _worker_star_d(d, q):
    """RSF(star(1)) sans paire soeur dans star(1), avec exactement d aretes D internes a star(1) (notes/19 §7)."""
    idle()
    import row_system_full
    from pysat.solvers import Solver
    from pysat.formula import IDPool
    from pysat.card import CardEnc, EncType
    t0 = time.time()
    outer = [(i, j, e) for i in range(1, 8) for j in range(i + 1, 8) for e in (0, 1)]
    S = [U for U, (i, j, e) in enumerate(outer) if i == 1]
    clauses, nv, outer, A, B = row_system_full.build(S, sigma=(), sigma_exact=True)
    pool = IDPool(start_from=nv + 1); extra = []
    zs = []
    for U, V in itertools.combinations(S, 2):
        z = pool.id(("dz", U, V)); zs.append(z)
        extra += [[-z, A[U, V]], [-z, B[U, V]], [z, -A[U, V], -B[U, V]]]
    extra += CardEnc.equals(lits=zs, bound=d, vpool=pool, encoding=EncType.seqcounter).clauses
    with Solver(name="cadical195", bootstrap_with=clauses + extra) as s:
        r = s.solve()
    q.put(("SAT" if r else "UNSAT", 0, round(time.time() - t0, 1), len(clauses) + len(extra), None))

def solve_star_d(d, T):
    q = mp.Queue(); p = mp.Process(target=_worker_star_d, args=(d, q)); p.start(); t0 = time.time()
    while p.is_alive() and time.time() - t0 < T:
        p.join(1.0)
        if free_gb() < 3.0:
            p.terminate(); p.join(); return ("MEMSTOP", 0, round(time.time() - t0, 1), 0, None)
    if p.is_alive():
        p.terminate(); p.join(); return ("TIMEOUT", 0, T, 0, None)
    try:
        return q.get(timeout=10)
    except Exception:
        return ("ERREUR", 0, 0, 0, None)

def solve_full(S, sigma=(), sigma_exact=False, dpairs=(), T=60.0):
    if free_gb() < 3.0:
        raise SystemExit("memoire libre < 3 Go : arret")
    q = mp.Queue(); p = mp.Process(target=_worker_full, args=(list(S), list(sigma), sigma_exact, list(dpairs), q)); p.start()
    t0 = time.time()
    while p.is_alive() and time.time() - t0 < T:
        p.join(1.0)
        if free_gb() < 3.0:
            p.terminate(); p.join(); return ("MEMSTOP", 0, round(time.time() - t0, 1), 0, None)
    if p.is_alive():
        p.terminate(); p.join(); return ("TIMEOUT", 0, T, 0, None)
    try:
        return q.get(timeout=10)
    except Exception:
        return ("ERREUR", 0, 0, 0, None)

def edges_str(E):
    return " ".join("%d%d" % e for e in sorted(tuple(sorted(e)) for e in E)) or "-"

def parse(s):
    return [tuple(sorted((int(p[0]), int(p[1])))) for p in s.split()]

ATOMS = ["13 15 35 67", "12 23 24 25 67", "14 15 23 36 37", "13 16 23 26 35 56", "12 16 23 34 45 56", "12 15 23 34 45 67",
         "12 14 15 17 23 25 56", "14 15 23 24 25 47 56", "14 15 23 24 25 27 36", "12 23 26 34 37 45 67", "12 15 23 34 36 56 67"]
MAXSAT = ["13 14 15 34 35 36 37", "12 23 24 25 34 35 37", "23 26 34 35 47 56 67", "14 15 23 24 25 37 67", "12 17 23 34 45 56 67",
          "23 26 27 36 37 67", "12 26 27 47 56 67", "23 34 36 47 56 67", "17 27 37 47 57 67", "12 23 24 25 47 56", "15 23 24 25 36 37",
          "12 14 15 23 47 56"]

def sister_orbits(E, m=7):
    import row_system
    return [row_system.orbit(i, j, e, m) for (i, j) in E for e in (0, 1)]

if __name__ == "__main__":
    idle()
    cmd = sys.argv[1]
    if cmd == "validate":
        import row_system
        for m in (2, 3):
            outer = row_system.base(m)[0]
            allS = list(range(len(outer)))
            n_all = len(row_system.base(m)[4]); n_sel = len(row_system.select(allS, m))
            r = solve(allS, m=m, T=120)
            print("m=%d : RS(toutes les orbites) %d/%d contraintes, %s (%.1f s)" % (m, n_sel, n_all, r[0], r[2]), flush=True)
        outer = row_system.base(7)[0]
        print("m=7 : RS(toutes) selectionne %d/%d contraintes" % (len(row_system.select(range(len(outer)), 7)), len(row_system.base(7)[4])), flush=True)
    elif cmd == "chi":
        T = float(sys.argv[2])
        for tag, lst, expect in (("atome", ATOMS, "UNSAT"), ("chi-SAT max", MAXSAT, "SAT")):
            for s in lst:
                E = parse(s)
                r = solve(sister_orbits(E), sigma=E, T=T)
                print("%-12s %-24s |S|=%2d  RS: %-7s (attendu %s) construction %.1f s, resolution %.1f s, %d clauses"
                      % (tag, s, 2 * len(E), r[0], expect, r[1], r[2], r[3]), flush=True)
    elif cmd == "signed":
        # RSF(orbites soeurs) (modele complet signe restreint aux lignes soeurs) vs RS(orbites soeurs) (= systeme chi)
        T = float(sys.argv[2])
        from chi_system import CONFIGS
        for name in sys.argv[3:]:
            E = CONFIGS[name] if name in CONFIGS else parse(name.replace("_", " "))
            S = sister_orbits(E)
            r = solve_full(S, sigma=E, T=T)
            print("%-16s %-24s |S|=%2d  RSF (signe, lignes soeurs): %-7s construction %.1f s, resolution %.1f s, %d clauses"
                  % (name, edges_str(E), len(S), r[0], r[1], r[2], r[3]), flush=True)
    elif cmd == "gridfree":
        # coeur sans grille : RSF(S) signe, aucune paire soeur parmi les paires portant une orbite de S (sigma_exact, sigma vide)
        T = float(sys.argv[2])
        import row_system
        star = lambda i: [U for U, (a, b, e) in enumerate(row_system.base(7)[0]) if i in (a, b)]
        fams = {"star1": star(1), "orb1234": row_system.orbits_on(range(1, 5)), "star12": sorted(set(star(1)) | set(star(2))),
                "orb12345": row_system.orbits_on(range(1, 6)), "star123": sorted(set(star(1)) | set(star(2)) | set(star(3)))}
        for name in sys.argv[3:]:
            S = fams[name]
            r = solve_full(S, sigma=(), sigma_exact=True, T=T)
            print("%-10s |S|=%2d  RSF sans soeur : %-7s resolution %.1f s, %d clauses" % (name, len(S), r[0], r[2], r[3]), flush=True)
    elif cmd == "stard":
        T = float(sys.argv[2])
        for d in [int(x) for x in sys.argv[3:]]:
            r = solve_star_d(d, T)
            print("star1 sans soeur, d_1 = %d aretes D internes : %-7s %.1f s" % (d, r[0], r[2]), flush=True)
    elif cmd == "local":
        import networkx as nx, row_system
        b = int(sys.argv[2]); T = float(sys.argv[3])
        graphs = [g for g in nx.graph_atlas_g() if g.number_of_nodes() == b]
        lo, hi = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (0, len(graphs))
        S = row_system.orbits_on(range(1, b + 1))
        for gi in range(lo, hi):
            g = graphs[gi]
            E = [tuple(sorted((u + 1, v + 1))) for u, v in g.edges()]
            r = solve(S, sigma=E, T=T)
            print("b=%d g%03d %-30s aretes=%2d  RS: %-7s construction %.1f s, resolution %.1f s" % (b, gi, edges_str(E), len(E), r[0], r[1], r[2]), flush=True)
