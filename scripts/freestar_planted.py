"""Calibration (notes/20) : le modele compact de l'etoile libre avec des cibles (ii),(iii) PLANTEES (tirees d'une bijection Phi
aleatoire, donc une solution existe). Si cadical trouve vite ces solutions, un UNKNOWN sur les vraies cibles suggere (sans le
prouver) l'absence de solution ; sinon le solveur est simplement faible sur cette structure.
Usage : python freestar_planted.py <graine> <T>
"""
import sys, os, random, time, multiprocessing as mp
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import freestar_compact as FC

def child(seed, q):
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    from pysat.solvers import Solver
    rng = random.Random(seed); n2 = 12
    mu = FC.mu_rep((1, 1, 1, 1, 1, 1))
    Ws = FC.far_roots(7); Z = [Ws[w][h] for w in range(len(Ws)) for h in (0, 1)]
    pairs = [p for p in ((a, b) for a in range(n2) for b in range(a + 1, n2)) if mu[p[0]] != p[1]]
    ph = list(range(len(Z))); rng.shuffle(ph)
    Cx = np.zeros((n2, n2), int); Ct = np.zeros((n2, n2), int)
    for z in range(len(Z)):
        f = pairs[ph[z]]; g = pairs[ph[z ^ 1]]
        for a in Z[z]:
            for b in f: Cx[a, b] += 1
        for b in f:
            for d in g: Ct[b, d] += 1
    FC.targets = lambda mu_, tau_, n2_: (Cx, Ct)          # cibles plantees
    cnf, pool, y, B, pr, W2 = FC.build(mu, mu, 7)
    s = Solver(name="cadical195", bootstrap_with=cnf.clauses)
    t0 = time.time(); r = s.solve(); q.put((r, round(time.time() - t0, 1)))

if __name__ == "__main__":
    seed, T = int(sys.argv[1]), float(sys.argv[2])
    q = mp.Queue(); p = mp.Process(target=child, args=(seed, q)); p.start(); p.join(T)
    if p.is_alive():
        p.terminate(); p.join(); print("plante graine %d : UNKNOWN (> %.0f s)" % (seed, T))
    else:
        print("plante graine %d :" % seed, q.get(timeout=10))
