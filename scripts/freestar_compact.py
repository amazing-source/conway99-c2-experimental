"""Formulation compacte du probleme local de l'etoile libre (notes/20, idee 7).

Cadre (DERIVE, notes/20 §3) : droite l_1 = {x, e_1, -e_1}. X = les 2(m-1) vecteurs signes des autres blocs (x = 2j+s pour s*e_{j+2}),
sigma(x) = x^1. Les 24 racines +-e_1 + b (b dans X) sont les lignes de star(1). Donnees :
  mu  : couplage parfait de X,  mu(b) = b'  <=>  e_1+b ~ e_1+b'            (le couplage A_1 = M_1)
  tau : couplage parfait de X,  tau(b) = d  <=>  e_1+b ~ -(e_1+d)           (les bits b internes a star(1))
  Phi : pour chaque racine lointaine z (sans le bloc 1), Phi(z) = {b dans X : e_1+b ~ z}   (|Phi(z)| = 2)
RSF(star(1)) equivaut a :
  (i)   Phi est une bijection des 4*C(m-1,2) racines lointaines sur les paires de X qui ne sont pas des paires de mu ;
  (ii)  #{z : a dans N_x(z), b dans Phi(z)} = 2 - [b=sa] - [b=mu a] - [b=tau s a]   (a != b),   1 - [tau a = s a]   (a = b) ;
  (iii) #{z : b dans Phi(z), d dans Phi(-z)} = 2 - [d=sb] - [d=tau mu b] - [d=mu tau b] - [d=tau b] ;
  (etoile libre) aucune b avec mu(b) = tau(b) = s(b).
Ce script : (1) valide (i)-(iii) sur BvLS (m = 11, table exacte) ; (2) enumere les couples (mu, tau) a symetrie B_6 pres (m = 7) ;
(3) resout la formulation compacte par couple, avec une limite de temps.
Usage : python freestar_compact.py validate
        python freestar_compact.py types
        python freestar_compact.py solve <partition> <T_par_couple> [max_couples]
"""
import sys, os, itertools, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)

# ---------------------------------------------------------------- structures sur X
def far_roots(m):
    """racines lointaines (sans le bloc 1) : liste de (N_x frozenset, signe) ; orbites W = (z_W, -z_W) avec z_W de 1er signe +."""
    n = m - 1
    W = []
    for j, k in itertools.combinations(range(n), 2):
        for s2 in (0, 1):
            z = frozenset((2 * j, 2 * k + s2)); mz = frozenset((2 * j + 1, 2 * k + 1 - s2))
            W.append((z, mz))
    return W

def targets(mu, tau, n2):
    s = lambda x: x ^ 1
    Cx = np.zeros((n2, n2), dtype=int); Ct = np.zeros((n2, n2), dtype=int)
    for a in range(n2):
        for b in range(n2):
            if a == b:
                Cx[a, b] = 1 - (tau[a] == s(a))
            else:
                Cx[a, b] = 2 - (b == s(a)) - (b == mu[a]) - (b == tau[s(a)])
    for b in range(n2):
        for d in range(n2):
            Ct[b, d] = 2 - (d == s(b)) - (d == tau[mu[b]]) - (d == mu[tau[b]]) - (d == tau[b])
    return Cx, Ct

# ---------------------------------------------------------------- (1) validation sur BvLS
def validate():
    sys.path.insert(0, os.path.join(HERE, "vendor"))
    from sib_partition_check import load, outer_graph
    fr, T = load(11)
    roots, idx, Hm = outer_graph(fr, T)
    m = 11; n2 = 2 * (m - 1)
    def root(pairs):
        v = [0] * m
        for (blk, sg) in pairs: v[blk] = sg
        return idx[tuple(v)]
    xs = lambda x: (x // 2 + 1, 1 - 2 * (x % 2))          # x -> (bloc 0-indexe dans le tuple, signe)
    e1p = lambda b: root([(0, 1), xs(b)])
    e1m = lambda c: root([(0, -1), xs(c)])
    mu = [None] * n2; tau = [None] * n2
    for b in range(n2):
        nb = [b2 for b2 in range(n2) if b2 != b and Hm[e1p(b), e1p(b2)]]
        assert len(nb) == 1; mu[b] = nb[0]
        nc = [c for c in range(n2) if Hm[e1p(b), e1m(c)]]
        assert len(nc) == 1; tau[b] = nc[0] ^ 1                  # e_1+b ~ -e_1+c = -(e_1 + s c)  =>  tau(b) = s(c)
    Ws = far_roots(m)
    Phi = {}
    for (z, mz) in Ws:
        for Z in (z, mz):
            zi = root([xs(x) for x in Z])
            Phi[Z] = frozenset(b for b in range(n2) if Hm[e1p(b), zi])
    ok_i = all(len(p) == 2 for p in Phi.values()) and len(set(Phi.values())) == len(Phi) \
        and all(mu[min(p)] != max(p) for p in Phi.values())
    Cx, Ct = targets(mu, tau, n2)
    Cx_obs = np.zeros((n2, n2), dtype=int); Ct_obs = np.zeros((n2, n2), dtype=int)
    for (z, mz) in Ws:
        for Z, MZ in ((z, mz), (mz, z)):
            for a in Z:
                for b in Phi[Z]: Cx_obs[a, b] += 1
            for b in Phi[Z]:
                for d in Phi[MZ]: Ct_obs[b, d] += 1
    s = lambda x: x ^ 1
    print("BvLS m=11 : |X| = %d, racines lointaines = %d" % (n2, len(Phi)))
    print("  mu = sigma partout :", all(mu[b] == s(b) for b in range(n2)), "; tau = sigma partout :", all(tau[b] == s(b) for b in range(n2)))
    print("  (i) bijection sur les paires hors mu :", ok_i)
    print("  (ii) formule = observe :", bool((Cx == Cx_obs).all()))
    print("  (iii) formule = observe :", bool((Ct == Ct_obs).all()))

# ---------------------------------------------------------------- (2) types (mu, tau) a symetrie pres, m = 7
def b6(n=6):
    """elements de B_n agissant sur X = {2j+s} : x -> 2 p(j) + (s xor eps_{p(j)})."""
    G = []
    for p in itertools.permutations(range(n)):
        for eps in itertools.product((0, 1), repeat=n):
            G.append([2 * p[x // 2] + ((x % 2) ^ eps[p[x // 2]]) for x in range(2 * n)])
    return np.array(G, dtype=np.int8)

def all_matchings(pts):
    if not pts: yield []; return
    a = pts[0]
    for i in range(1, len(pts)):
        rest = pts[1:i] + pts[i + 1:]
        for M in all_matchings(rest):
            yield [(a, pts[i])] + M

def as_perm(M, n2):
    t = [None] * n2
    for a, b in M: t[a] = b; t[b] = a
    return t

def conj(G, t):
    """g t g^-1 pour tous les g de G (tableau |G| x n2)."""
    n2 = len(t); out = np.empty_like(G)
    rows = np.arange(G.shape[0])[:, None]
    out[rows, G] = G[:, np.array(t)]
    return out

def mu_rep(part):
    from make_freestar_cubes import matching
    M = matching(tuple(part))
    return as_perm([(2 * (a[0] - 2) + a[1], 2 * (b[0] - 2) + b[1]) for a, b in M], 12)

def local_ok(mu, tau):
    s = lambda x: x ^ 1
    for b in range(12):
        if mu[b] == s(b) and tau[b] == s(b): return False          # paire soeur
        if tau[mu[b]] == s(b) and mu[tau[b]] == s(b): return False  # C_{+-}(b,b) < 0
    return True

def types(part):
    G = b6(); mu = mu_rep(part)
    stab = G[(conj(G, mu) == np.array(mu)).all(axis=1)]
    code = lambda arr: (arr.astype(np.int64) * (12 ** np.arange(12))).sum(axis=-1)
    seen = {}; reps = []
    for M in all_matchings(list(range(12))):
        t = as_perm(M, 12)
        if not local_ok(mu, t): continue
        c = int(code(conj(stab, t)).min())
        if c not in seen:
            seen[c] = len(reps); reps.append(t)
    return mu, reps, len(stab)

# ---------------------------------------------------------------- (3) modele compact (pysat)
def build(mu, tau, m=7):
    from pysat.formula import IDPool, CNF
    from pysat.card import CardEnc, EncType
    n2 = 2 * (m - 1); Ws = far_roots(m); nW = len(Ws)
    pool = IDPool(); cnf = CNF()
    pairs = [p for p in itertools.combinations(range(n2), 2) if mu[p[0]] != p[1]]
    y = {(w, h, p): pool.id(("y", w, h, p)) for w in range(nW) for h in (0, 1) for p in pairs}
    B = {(w, h, b): pool.id(("B", w, h, b)) for w in range(nW) for h in (0, 1) for b in range(n2)}
    def card(lits, k):
        enc = CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter)
        cnf.extend(enc.clauses)
    for w in range(nW):
        for h in (0, 1):
            card([y[w, h, p] for p in pairs], 1)
            for b in range(n2):                                     # B = OR des y des paires contenant b
                ys = [y[w, h, p] for p in pairs if b in p]
                cnf.append([-B[w, h, b]] + ys)
                for v in ys: cnf.append([-v, B[w, h, b]])
    for p in pairs:                                                  # (i) bijection
        card([y[w, h, p] for w in range(nW) for h in (0, 1)], 1)
    Cx, Ct = targets(mu, tau, n2)
    for a in range(n2):                                              # (ii)
        for b in range(n2):
            lits = [B[w, h, b] for w in range(nW) for h in (0, 1) if a in Ws[w][h]]
            card(lits, int(Cx[a, b]))
    u = {}
    for w in range(nW):
        for b in range(n2):
            for d in range(n2):
                v = pool.id(("u", w, b, d)); u[w, b, d] = v             # u = B[w,0,b] et B[w,1,d]
                cnf.extend([[-v, B[w, 0, b]], [-v, B[w, 1, d]], [v, -B[w, 0, b], -B[w, 1, d]]])
    for b in range(n2):                                              # (iii)
        for d in range(b, n2):
            lits = [u[w, b, d] for w in range(nW)] + ([u[w, d, b] for w in range(nW)] if d != b else [])
            k = int(Ct[b, d]) if d != b else int(Ct[b, b]) // 2
            card(lits, k)
    return cnf, pool, y, B, pairs, Ws

def solve_one(args):
    mu, tau, T = args
    import threading
    from pysat.solvers import Solver
    cnf, pool, y, B, pairs, Ws = build(mu, tau)
    s = Solver(name="cadical195", bootstrap_with=cnf.clauses)
    timer = threading.Timer(T, s.interrupt); timer.start()
    t0 = time.time(); r = s.solve_limited(expect_interrupt=True); dt = time.time() - t0
    timer.cancel()
    sol = None
    if r:
        val = set(l for l in s.get_model() if l > 0)
        sol = {str((w, h)): [p for p in pairs if y[w, h, p] in val][0] for w in range(len(Ws)) for h in (0, 1)}
    s.delete()
    return ("SAT" if r else ("UNSAT" if r is False else "UNKNOWN")), round(dt, 2), sol

if __name__ == "__main__":
    try:
        import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    except Exception:
        pass
    cmd = sys.argv[1]
    if cmd == "validate":
        validate()
    elif cmd == "types":
        from make_freestar_cubes import PARTS
        tot = 0
        for part in PARTS:
            mu, reps, st = types(part); tot += len(reps)
            print("A%s : |Stab(mu)| = %d, types de tau (etoile libre + conditions locales) : %d" % ("".join(map(str, part)), st, len(reps)), flush=True)
        print("total :", tot)
    elif cmd == "solve":
        part = tuple(int(c) for c in sys.argv[2]); T = float(sys.argv[3]); cap = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 9
        mu, reps, st = types(part)
        print("A%s : %d types de tau" % (sys.argv[2], len(reps)), flush=True)
        stats = {}
        out = open(os.path.join(HERE, "..", "logs", "freestar_compact_A%s.jsonl" % sys.argv[2]), "a")
        for i, tau in enumerate(reps[:cap]):
            v, dt, sol = solve_one((mu, tau, T))
            stats[v] = stats.get(v, 0) + 1
            out.write(json.dumps({"part": sys.argv[2], "i": i, "tau": tau, "verdict": v, "s": dt, "sol": sol}) + "\n"); out.flush()
            print("  tau #%d %s : %s (%.1f s)" % (i, tau, v, dt), flush=True)
        print("bilan A%s :" % sys.argv[2], stats)
