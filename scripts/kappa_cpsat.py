"""Sonde rapide du probleme kappa (note 23 §5) : existe-t-il un couplage parfait kappa des 60 paires hors mu tel que
#{w : b dans w, d dans kappa(w)} = Ct[b, d] ?  CP-SAT 1 fil, limite courte.  On ne consigne que les reponses DEFINITIVES
(solution trouvee et reverifiee, ou INFAISABLE) ; un UNKNOWN n'est pas un resultat.
Usage : python kappa_cpsat.py <partition mu> <indices tau> <secondes> [H : generateurs de symetrie imposee, optionnel]
"""
import sys, os, time, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types
from ortools.sat.python import cp_model

def model(mu, Ct):
    P = [(a, b) for a in range(12) for b in range(a + 1, 12) if mu[a] != b]
    m = cp_model.CpModel()
    x = {}
    for i, j in itertools.combinations(range(60), 2):
        x[i, j] = m.NewBoolVar("x%d_%d" % (i, j))
    X = lambda i, j: x[min(i, j), max(i, j)]
    for i in range(60):
        m.AddExactlyOne(X(i, j) for j in range(60) if j != i)
    cov = {}
    for (i, j), v in x.items():
        for u in P[i]:
            for w in P[j]:
                key = (min(u, w), max(u, w))
                cov.setdefault(key, []).append(v)
    for b in range(12):
        for d in range(b, 12):
            lits = cov.get((b, d), [])
            tgt = Ct[b, d] // 2 if b == d else Ct[b, d]
            m.Add(sum(lits) == tgt)
    return m, x, P

def check(sol, P, Ct):
    C = np.zeros((12, 12), dtype=int)
    for (i, j) in sol:
        for u in P[i]:
            for w in P[j]:
                C[u, w] += 1; C[w, u] += 1
    return bool((C == Ct).all())

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); which = [int(x) for x in sys.argv[2].split(",")]; T = float(sys.argv[3])
    mu, reps, st = types(part)
    for ti in which:
        tau = reps[ti]; Cx, Ct = targets(mu, tau, 12)
        m, x, P = model(mu, Ct)
        s = cp_model.CpSolver(); s.parameters.num_workers = 1; s.parameters.max_time_in_seconds = T
        t0 = time.time(); r = s.Solve(m)
        name = s.StatusName(r)
        extra = ""
        if r in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            sol = [k for k, v in x.items() if s.Value(v)]
            extra = " ; reverifie : %s" % check(sol, P, Ct)
            np.save(os.path.join(HERE, "..", "logs", "kappa_sol_A%s_t%d.npy" % (sys.argv[1], ti)), np.array(sol))
        print("A%s tau#%d : %s (%.1f s)%s" % (sys.argv[1], ti, name, time.time() - t0, extra), flush=True)
