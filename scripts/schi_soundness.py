"""Test de correction (soundness) du systeme chi signe (notes/19 §4) par transfert de modeles.

Pour une configuration Sigma ou RSF(orbites soeurs) est SAT : on prend un modele de RSF (variables a,b du modele complet), on en
deduit chi_p(W) et sigma_p(W) (Q[U_p^eps,W] = 1 pour un unique eps ; sigma = +1 si a = 1, -1 si b = 1), puis on impose ces valeurs
dans schi_system.build(Sigma) : le resultat DOIT etre SAT (sinon une contrainte derivee est fausse).
On verifie aussi S1 au passage (exactement un eps).
Usage : python schi_soundness.py "17 56 67" "23 25 36 56" ...
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from pysat.solvers import Solver
import row_system_full, schi_system
from chi_system import ALLPAIRS
from rs_experiments import idle, parse, sister_orbits

def transfer(E):
    S = sister_orbits(E)
    clauses, nv, outer, A, B = row_system_full.build(S, sigma=E)
    with Solver(name="cadical195", bootstrap_with=clauses) as s:
        if not s.solve():
            return "RSF-UNSAT (pas de test)"
        val = set(l for l in s.get_model() if l > 0)
    idx = {o: k for k, o in enumerate(outer)}
    cnf, pool, X, Z = schi_system.build(E)
    units = []
    for p in [tuple(sorted(e)) for e in E]:
        Up = [idx[(p[0], p[1], 0)], idx[(p[0], p[1], 1)]]
        for r in ALLPAIRS:
            if set(r) & set(p):
                continue
            for e in (0, 1):
                W = idx[(r[0], r[1], e)]
                hits = [(eps, A[Up[eps], W] in val, B[Up[eps], W] in val) for eps in (0, 1)]
                q1 = [(eps, a, b) for (eps, a, b) in hits if a + b == 1]
                bad = [(eps, a, b) for (eps, a, b) in hits if a + b == 2]
                if len(q1) != 1 or bad:
                    return "ECHEC S1 sur p=%s W=%s : %s" % (p, (r, e), hits)
                eps, a, b = q1[0]
                units.append([X[p, (r, e)] if eps else -X[p, (r, e)]])
                units.append([Z[p, (r, e)] if b else -Z[p, (r, e)]])
    with Solver(name="cadical195", bootstrap_with=cnf.clauses + units) as s:
        ok = s.solve()
    return "schi SAT avec les valeurs transferees (%d unites) : OK" % len(units) if ok else "ECHEC : schi UNSAT avec les valeurs transferees"

if __name__ == "__main__":
    idle()
    for s in sys.argv[1:]:
        t0 = time.time()
        print("%-20s %s (%.1f s)" % (s, transfer(parse(s)), time.time() - t0), flush=True)
