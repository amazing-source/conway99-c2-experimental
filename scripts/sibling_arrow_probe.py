"""Fleches sœurs « a seules » (notes/19 §7) : pour c < x, a[U_{cx}^+, U_{cx}^-] = 1 (arete sœur dans le couplage de N(e_c)) mais
b = 0 (pas de grille).  Etoile de telles fleches en c : RSF(lignes des orbites concernees), sans paire soeur, verdict ?
Usage : python sibling_arrow_probe.py <T>
"""
import sys, time
sys.path.insert(0, "scripts")
from rs_experiments import idle, free_gb
import multiprocessing as mp

def _w(c, xs, extra_rows, q):
    idle()
    import row_system_full as R
    from pysat.solvers import Solver
    S = sorted(set([R.orbit(c, x, e) for x in xs for e in (0, 1)] + [R.orbit(i, j, e) for (i, j) in extra_rows for e in (0, 1)]))
    clauses, nv, outer, A, B = R.build(S, sigma=(), sigma_exact=True)
    extra = []
    for x in xs:
        U, V = R.orbit(c, x, 0), R.orbit(c, x, 1)
        extra += [[A[U, V]], [-B[U, V]]]
    t0 = time.time()
    with Solver(name="cadical195", bootstrap_with=clauses + extra) as s:
        r = s.solve()
    q.put(("SAT" if r else "UNSAT", time.time() - t0))

if __name__ == "__main__":
    idle(); T = float(sys.argv[1])
    for xs in ([2, 3], [2, 3, 4], [2, 3, 4, 5], [2, 3, 4, 5, 6, 7]):
        q = mp.Queue(); p = mp.Process(target=_w, args=(1, xs, [], q)); p.start(); p.join(T)
        if p.is_alive():
            p.terminate(); p.join(); r = ("TIMEOUT", T)
        else:
            r = q.get(timeout=10)
        print("fleches soeurs a-seules 1->%s (lignes de star(1) concernees) : %s %.1f s" % (xs, r[0], r[1]), flush=True)
