"""Decomposition maitre/esclave (Benders logique) du systeme chi signe (notes/19 §6).

Maitre : systeme chi NON signe (variables X = chi) ; esclave : systeme signe complet sous hypotheses X = chi du maitre.
Si l'esclave est SAT : solution trouvee (et verifiee).  Sinon son noyau (sous-ensemble des hypotheses X) donne une clause
interdite ajoutee au maitre.  S'arrete sur SAT, sur maitre UNSAT (=> systeme signe UNSAT) ou a la limite de temps.
Usage : python schi_benders.py <T> "12 16 17" [aug]
"""
import sys, time
from pysat.solvers import Solver
sys.path.insert(0, "scripts")
import schi_system
from rs_experiments import idle

def benders(E, T, aug=False, log=print):
    cnf_u, pool_u, Xu, Zu = schi_system.build(E, signed=False)
    cnf_s, pool_s, Xs, Zs = schi_system.build(E, signed=True, aug=aug)
    keys = sorted(Xu)
    assert all(k in Xs for k in keys)
    m = Solver(name="cadical195", bootstrap_with=cnf_u.clauses)
    sl = Solver(name="cadical195", bootstrap_with=cnf_s.clauses)
    t0 = time.time(); it = 0; sizes = []
    while time.time() - t0 < T:
        if not m.solve():
            return "UNSAT", it, time.time() - t0, sizes
        val = set(l for l in m.get_model() if l > 0)
        ass = [Xs[k] if Xu[k] in val else -Xs[k] for k in keys]
        if sl.solve(assumptions=ass):
            return "SAT", it, time.time() - t0, sizes
        core = set(sl.get_core())
        nog = [k for k in keys if (Xs[k] in core or -Xs[k] in core)]
        clause = [-Xu[k] if Xu[k] in val else Xu[k] for k in nog]
        m.add_clause(clause); sizes.append(len(clause)); it += 1
        if it % 200 == 0:
            log("   it=%d  %.0f s  taille moyenne des clauses interdites (200 dernieres) %.1f" % (it, time.time() - t0, sum(sizes[-200:]) / 200.0))
    return "TIMEOUT", it, time.time() - t0, sizes

if __name__ == "__main__":
    idle()
    T = float(sys.argv[1]); aug = len(sys.argv) > 3 and sys.argv[3] == "aug"
    E = [tuple(sorted((int(x[0]), int(x[1])))) for x in sys.argv[2].split()]
    r, it, dt, sizes = benders(E, T, aug, log=lambda s: print(s, flush=True))
    print("%s : %s apres %d iterations, %.1f s ; clauses interdites : min %s max %s" % (sys.argv[2], r, it, dt, min(sizes) if sizes else "-", max(sizes) if sizes else "-"), flush=True)
