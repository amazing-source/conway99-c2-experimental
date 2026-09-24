"""Le probleme local de l'etoile libre pour la famille srg(v, 2m, 1, 2) (notes/20, idee 10).
La formulation compacte (freestar_compact) ne depend que de lambda = 1, mu = 2 : elle a un sens pour tout m (|X| = 2(m-1)).
Pour m = 3..6 le probleme est petit : on enumere les couples (mu, tau) (a symetrie B_{m-1} pres), avec et sans la condition
« etoile libre », et on resout le modele compact (cadical, delai par processus fils).
Question : l'etoile libre locale existe-t-elle pour de petits m ? (si oui pour m < 7, l'obstruction eventuelle est propre a m = 7.)
Usage : python freestar_family.py <m> <T_par_couple> [libre|tout]
"""
import sys, os, json, time, itertools, multiprocessing as mp
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import far_roots, targets, all_matchings, as_perm, conj, build

def bn(n):
    G = []
    for p in itertools.permutations(range(n)):
        for eps in itertools.product((0, 1), repeat=n):
            G.append([2 * p[x // 2] + ((x % 2) ^ eps[p[x // 2]]) for x in range(2 * n)])
    return np.array(G, dtype=np.int16)

def pair_types(m, free=True):
    n = m - 1; n2 = 2 * n; G = bn(n)
    code = lambda arr: (arr.astype(np.int64) * (n2 ** np.arange(n2))).sum(axis=-1)
    Ms = [as_perm(M, n2) for M in all_matchings(list(range(n2)))]
    seen = set(); reps = []
    for mu in Ms:
        cm = int(code(conj(G, mu)).min())
        # representant canonique de mu : on ne garde que les mu minimaux dans leur orbite
        if int(code(np.array([mu]))[0]) != cm: continue
        stab = G[(conj(G, mu) == np.array(mu)).all(axis=1)]
        for tau in Ms:
            if free and any(mu[b] == (b ^ 1) and tau[b] == (b ^ 1) for b in range(n2)): continue
            if any(tau[mu[b]] == (b ^ 1) and mu[tau[b]] == (b ^ 1) for b in range(n2)): continue
            c = (cm, int(code(conj(stab, tau)).min()))
            if c not in seen:
                seen.add(c); reps.append((mu, tau))
    return reps

def child(mu, tau, m, q):
    try:
        import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    except Exception:
        pass
    from pysat.solvers import Solver
    cnf, pool, y, B, pairs, Ws = build(mu, tau, m)
    s = Solver(name="cadical195", bootstrap_with=cnf.clauses)
    r = s.solve()
    sol = None
    if r:
        val = set(l for l in s.get_model() if l > 0)
        sol = [[sorted(Ws[w][h]), list([p for p in pairs if y[w, h, p] in val][0])] for w in range(len(Ws)) for h in (0, 1)]
    q.put(("SAT" if r else "UNSAT", sol))

def run(mu, tau, m, T):
    q = mp.Queue(); p = mp.Process(target=child, args=(mu, tau, m, q)); t0 = time.time(); p.start(); p.join(T)
    if p.is_alive():
        p.terminate(); p.join(); return "UNKNOWN", round(time.time() - t0, 1), None
    try:
        v, sol = q.get(timeout=10)
    except Exception:
        return "ERREUR", round(time.time() - t0, 1), None
    return v, round(time.time() - t0, 1), sol

def mu_type(mu, n2):
    """type de cycles de mu/sigma (partition), pour l'affichage"""
    seen = set(); parts = []
    for b in range(n2):
        if b // 2 in seen: continue
        L = 0; blk = b // 2; x = b
        while True:
            seen.add(x // 2); L += 1
            y = mu[x] ^ 1 if False else mu[x]
            x = y ^ 1 if (y // 2) != (x // 2) or True else y
            x = mu[x] ^ 1 if False else x
            if x // 2 == blk: break
        parts.append(L)
    return tuple(sorted(parts, reverse=True))

if __name__ == "__main__":
    try:
        import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    except Exception:
        pass
    m = int(sys.argv[1]); T = float(sys.argv[2]); free = (len(sys.argv) < 4 or sys.argv[3] == "libre")
    reps = pair_types(m, free)
    print("m = %d : %d couples (mu, tau) %s" % (m, len(reps), "(etoile libre)" if free else "(tous)"), flush=True)
    stats = {}; out = open(os.path.join(HERE, "..", "logs", "freestar_family.jsonl"), "a")
    for i, (mu, tau) in enumerate(reps):
        v, dt, sol = run(mu, tau, m, T)
        stats[v] = stats.get(v, 0) + 1
        nsis = sum(1 for b in range(2 * (m - 1)) if mu[b] == (b ^ 1) and tau[b] == (b ^ 1)) // 2
        out.write(json.dumps({"m": m, "free": free, "i": i, "mu": mu, "tau": tau, "sisters": nsis, "verdict": v, "s": dt, "sol": sol}) + "\n"); out.flush()
        if v != "UNSAT" or len(reps) <= 40:
            print("  #%d mu=%s tau=%s soeurs=%d : %s (%.1f s)" % (i, mu, tau, nsis, v, dt), flush=True)
    print("bilan m=%d :" % m, stats, flush=True)
