"""Etoiles : le systeme signe a chi (non signe) FIXE est-il facile ?  (notes/19 §6)
On tire des solutions non signees (blocage successif), on fixe X = chi et on resout la partie signee (cadical, limite par instance).
Usage : python schi_fixchi.py "<paires>" <nb_solutions> <T_par_instance>
"""
import sys, time, multiprocessing as mp
sys.path.insert(0, "scripts")
import schi_system
from rs_experiments import idle

AUG = "noaug" not in sys.argv
def _sub(E, fix, q):
    idle()
    from pysat.solvers import Solver
    cnf, pool, X, Z = schi_system.build(E, aug=AUG)
    t0 = time.time()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        r = s.solve(assumptions=[X[k] if v else -X[k] for k, v in fix.items()])
    q.put(("SAT" if r else "UNSAT", time.time() - t0))

if __name__ == "__main__":
    idle()
    from pysat.solvers import Solver
    E = [tuple(sorted((int(x[0]), int(x[1])))) for x in sys.argv[1].split()]
    n, T = int(sys.argv[2]), float(sys.argv[3])
    cnf_u, pool_u, Xu, Zu = schi_system.build(E, signed=False)
    keys = sorted(Xu)
    m = Solver(name="cadical195", bootstrap_with=cnf_u.clauses)
    stats = {}
    for it in range(n):
        if not m.solve():
            print("plus de solution non signee apres", it); break
        val = set(l for l in m.get_model() if l > 0)
        fix = {k: (Xu[k] in val) for k in keys}
        m.add_clause([-Xu[k] if fix[k] else Xu[k] for k in keys])
        q = mp.Queue(); p = mp.Process(target=_sub, args=(E, fix, q)); p.start(); p.join(T)
        if p.is_alive():
            p.terminate(); p.join(); r = ("TIMEOUT", T)
        else:
            r = q.get()
        stats[r[0]] = stats.get(r[0], 0) + 1
        print("chi #%d : signe %s en %.1f s" % (it, r[0], r[1]), flush=True)
    print("bilan", stats)
