"""Test de LOCALITE de R2 (notes/15) : R2 est-il une consequence des conditions srg qui touchent S = {x} u N(x) u L u tL ?

Relaxation (pas le modele complet) : variables d'orbites de orbit_sat.py (a[U,V], b[U,V]) ; on garde (R), (D), (I) pour toutes les
orbites et (P) seulement pour les paires d'orbites dont l'une porte une racine de L (donc de tL). Les paires entre deux orbites
exterieures a S ne sont PAS contraintes.  Grille L imposee (droites, lignes, colonnes, non-adjacences induites), etiquettes des coins
fixees, et NON(al ~ t.be) : R2 echoue sur la droite {w, al, be}.
SAT  => aucune preuve de R2 n'utilisant que les conditions en S n'existe pour cette disposition (modele local exhibe, phi decode).
UNSAT => R2 sur cette droite est force localement pour cette disposition (non certifie).
Mono-fil, delai dur.  Usage : python r2_local_sat.py <cas> <secondes>
"""
import sys, time, itertools, multiprocessing as mp

M = 7
# demi-etiquettes (bloc, signe) ; w = e1
CASES = {
    # T3 : 4 blocs distincts, disposition compatible avec la reflexion complete (motif 1 du theoreme 15.3)
    "T3": dict(a=(2, 1), b=(3, 1), c=(4, 1), d=(5, 1),
               z_ac=((2, -1), (6, 1)), z_ad=((5, -1), (7, 1)), z_bc=((4, -1), (7, -1)), z_bd=((3, -1), (6, -1))),
    # T1 : deux droites soeurs ; disposition qui laisse survivre les « droites R2 » avec echange des coins par lignes
    "T1": dict(a=(2, 1), b=(2, -1), c=(3, 1), d=(3, -1),
               z_ac=((4, 1), (5, 1)), z_ad=((4, -1), (6, 1)), z_bc=((7, -1), (5, -1)), z_bd=((6, -1), (7, 1))),
}

def build(case):
    from pysat.formula import CNF, IDPool
    from pysat.card import CardEnc, EncType
    k = 2 * M
    outer = [(i, j, e) for i in range(1, M + 1) for j in range(i + 1, M + 1) for e in (0, 1)]
    N = len(outer)
    rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
    trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
    pool = IDPool(); cnf = CNF()
    A = {}; B = {}
    for U in range(N):
        for V in range(U + 1, N):
            A[U, V] = A[V, U] = pool.id(("a", U, V)); B[U, V] = B[V, U] = pool.id(("b", U, V))
    def prod(x, y):
        p = pool.id(("p", min(x, y), max(x, y)))
        cnf.extend([[-p, x], [-p, y], [p, -x, -y]]); return p
    def eq(lits, kk):
        if kk < 0 or kk > len(lits):
            cnf.append([]); return
        cnf.extend(CardEnc.equals(lits=lits, bound=kk, vpool=pool, encoding=EncType.seqcounter).clauses)
    # racines de la grille
    C = CASES[case]
    e1 = (1, 1)
    neg = lambda h: (h[0], -h[1])
    root = lambda h1, h2: {h1[0]: h1[1], h2[0]: h2[1]}
    G = {"al": root(e1, C["a"]), "be": root(e1, C["b"]), "ga": root(e1, C["c"]), "de": root(e1, C["d"])}
    for z in ("z_ac", "z_ad", "z_bc", "z_bd"):
        G[z] = root(*C[z])
    def bits(r):
        (i, x), (j, y) = sorted(r.items())
        sx, sy = (0 if x > 0 else 1), (0 if y > 0 else 1)
        return outer.index((i, j, sx ^ sy)), sx
    def adj(r1, r2):
        U, su = bits(r1); V, sv = bits(r2)
        assert U != V
        return A[U, V] if su == sv else B[U, V]
    tr = lambda r: {i: -s for i, s in r.items()}
    S_orb = {bits(r)[0] for r in G.values()}
    assert len(S_orb) == 8, "deux racines de L dans la meme orbite"
    inner = [(i, s) for i in range(1, M + 1) for s in (0, 1)]
    for U in range(N):
        others = [V for V in range(N) if V != U]
        eq([A[U, V] for V in others] + [B[U, V] for V in others], k - 2)                        # (R)
        eq([prod(A[U, V], B[U, V]) for V in others], 1)                                           # (D)
        for c in inner:                                                                           # (I)
            partner = (c[0], 1 - c[1]); lits = []
            for V in others:
                if c in rep[V]: lits.append(A[U, V])
                if c in trep[V]: lits.append(B[U, V])
            eq(lits, 1 if (c in rep[U] or partner in rep[U]) else 2)
    npairs = 0
    for U in range(N):                                                                            # (P) restreint
        for V in range(U + 1, N):
            if U not in S_orb and V not in S_orb:
                continue
            npairs += 1
            Ws = [W for W in range(N) if W != U and W != V]
            same = [prod(A[U, W], A[V, W]) for W in Ws] + [prod(B[U, W], B[V, W]) for W in Ws]
            cross = [prod(A[U, W], B[V, W]) for W in Ws] + [prod(B[U, W], A[V, W]) for W in Ws]
            eq(same + [A[U, V]], 2 - len(rep[U] & rep[V]))
            eq(cross + [B[U, V]], 2 - len(rep[U] & trep[V]))
    # grille induite
    pos = {"al": (1, 0), "be": (2, 0), "ga": (0, 1), "de": (0, 2), "z_ac": (1, 1), "z_ad": (1, 2), "z_bc": (2, 1), "z_bd": (2, 2)}
    for u, v in itertools.combinations(pos, 2):
        pu, pv = pos[u], pos[v]
        on_line = pu[0] == pv[0] or pu[1] == pv[1]
        cnf.append([adj(G[u], G[v])] if on_line else [-adj(G[u], G[v])])
    cnf.append([-adj(G["al"], tr(G["be"]))])                                                      # NON R2 sur {w, al, be}
    return cnf, pool, G, adj, tr, pos, npairs

def idle():
    """Priorite minimale (machine partagee)."""
    try:
        import ctypes
        k = ctypes.windll.kernel32
        k.GetCurrentProcess.restype = ctypes.c_void_p
        k.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        k.SetPriorityClass(k.GetCurrentProcess(), 0x40)      # IDLE_PRIORITY_CLASS
    except Exception:
        pass

def free_gb():
    try:
        import ctypes
        class MS(ctypes.Structure):
            _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong), ("ullTotalPhys", ctypes.c_ulonglong),
                        ("ullAvailPhys", ctypes.c_ulonglong), ("ullTotalPageFile", ctypes.c_ulonglong),
                        ("ullAvailPageFile", ctypes.c_ulonglong), ("ullTotalVirtual", ctypes.c_ulonglong),
                        ("ullAvailVirtual", ctypes.c_ulonglong), ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
        m = MS(); m.dwLength = ctypes.sizeof(MS)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
        return m.ullAvailPhys / 2**30
    except Exception:
        return 99.0

def worker(case, q):
    idle()
    from pysat.solvers import Solver
    t0 = time.time()
    cnf, pool, G, adj, tr, pos, npairs = build(case)
    tb = time.time() - t0
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        r = s.solve()
        res = {"result": "SAT" if r else "UNSAT", "build_s": round(tb, 1), "solve_s": round(time.time() - t0 - tb, 1),
               "vars": pool.top, "clauses": len(cnf.clauses), "pairs_P": npairs}
        if r:
            val = set(l for l in s.get_model() if l > 0)
            phi = {}
            for u in pos:
                hits = [v for v in pos if v != u and adj(G[u], tr(G[v])) in val]
                phi[u] = hits
            res["phi"] = phi
        q.put(res)

if __name__ == "__main__":
    case, T = sys.argv[1], float(sys.argv[2])
    idle()
    q = mp.Queue(); p = mp.Process(target=worker, args=(case, q)); p.start()
    t0 = time.time(); low = False
    while p.is_alive() and time.time() - t0 < T:
        p.join(5)
        if p.is_alive() and free_gb() < 3.0:
            low = True; break
    if p.is_alive():
        p.terminate(); p.join()
        print("%s : %s %.0f s" % (case, "ARRET (RAM libre < 3 Go)" if low else "TIMEOUT", time.time() - t0), flush=True)
    else:
        print("%s :" % case, q.get(), flush=True)
