"""Quelles familles de contraintes de la formulation compacte (note 20 §3) portent l'obstruction ? (note 22, cocycle a defauts)
Pour un type (mu, tau), on resout le modele compact en retirant une famille : (i) bijection, (ii) incidences x/+, (iii) incidences +/-.
Usage : python freestar_core_families.py <partition> <indice tau> <famille retiree : i|ii|iii|aucune> <T>"""
import sys, os, time, itertools, multiprocessing as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)

def build_partial(mu, tau, drop, m=7):
    from pysat.formula import IDPool, CNF
    from pysat.card import CardEnc, EncType
    from freestar_compact import far_roots, targets
    n2 = 2 * (m - 1); Ws = far_roots(m); nW = len(Ws)
    pool = IDPool(); cnf = CNF()
    pairs = [p for p in itertools.combinations(range(n2), 2) if mu[p[0]] != p[1]]
    y = {(w, h, p): pool.id(("y", w, h, p)) for w in range(nW) for h in (0, 1) for p in pairs}
    B = {(w, h, b): pool.id(("B", w, h, b)) for w in range(nW) for h in (0, 1) for b in range(n2)}
    def card(lits, k, mode="eq"):
        f = CardEnc.equals if mode == "eq" else CardEnc.atmost
        cnf.extend(f(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    for w in range(nW):
        for h in (0, 1):
            card([y[w, h, p] for p in pairs], 1)
            for b in range(n2):
                ys = [y[w, h, p] for p in pairs if b in p]
                cnf.append([-B[w, h, b]] + ys)
                for v in ys: cnf.append([-v, B[w, h, b]])
    if drop != "i":
        for p in pairs: card([y[w, h, p] for w in range(nW) for h in (0, 1)], 1)
    Cx, Ct = targets(mu, tau, n2)
    if drop != "ii":
        for a in range(n2):
            for b in range(n2):
                card([B[w, h, b] for w in range(nW) for h in (0, 1) if a in Ws[w][h]], int(Cx[a, b]))
    if drop != "iii":
        u = {}
        for w in range(nW):
            for b in range(n2):
                for d in range(n2):
                    v = pool.id(("u", w, b, d)); u[w, b, d] = v
                    cnf.extend([[-v, B[w, 0, b]], [-v, B[w, 1, d]], [v, -B[w, 0, b], -B[w, 1, d]]])
        for b in range(n2):
            for d in range(b, n2):
                lits = [u[w, b, d] for w in range(nW)] + ([u[w, d, b] for w in range(nW)] if d != b else [])
                card(lits, int(Ct[b, d]) if d != b else int(Ct[b, b]) // 2)
    return cnf

def child(part, i, drop, q):
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    from freestar_compact import types
    from pysat.solvers import Solver
    mu, reps, st = types(part)
    cnf = build_partial(mu, reps[i], drop)
    s = Solver(name="cadical195", bootstrap_with=cnf.clauses)
    t0 = time.time(); r = s.solve(); q.put(("SAT" if r else "UNSAT", round(time.time() - t0, 1)))

if __name__ == "__main__":
    part = tuple(int(c) for c in sys.argv[1]); i = int(sys.argv[2]); drop = sys.argv[3]; T = float(sys.argv[4])
    q = mp.Queue(); p = mp.Process(target=child, args=(part, i, drop, q)); p.start(); p.join(T)
    if p.is_alive():
        p.terminate(); p.join(); print("A%s tau#%d, sans (%s) : TIMEOUT %.0f s" % (sys.argv[1], i, drop, T), flush=True)
    else:
        print("A%s tau#%d, sans (%s) :" % (sys.argv[1], i, drop), q.get(timeout=10), flush=True)
