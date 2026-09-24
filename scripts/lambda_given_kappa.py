"""Etage lambda (note 23 §5) : kappa fixe (solution de (iii)), existe-t-il Phi bijective avec Phi o neg = kappa o Phi et (ii) ?
Formulation : lambda = Phi^-1 envoie chaque paire kappa {w, w'} sur une paire antipodale {z, -z}, lambda(w) = z, lambda(w') = -z.
(ii) : #{w : b dans w, a dans lambda(w)} = Cx[a, b].  CP-SAT 1 fil ; on ne consigne que les reponses definitives.
Usage : python lambda_given_kappa.py <partition> <tau> <fichier kappa .npy> <secondes>
"""
import sys, os, time, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types
from ortools.sat.python import cp_model

def solve_lambda(mu, tau, kpairs, T, verbose=False):
    Cx, Ct = targets(mu, tau, 12)
    P = [(a, b) for a in range(12) for b in range(a + 1, 12) if mu[a] != b]          # images (paires hors mu)
    Z = [(a, b) for a in range(12) for b in range(a + 1, 12) if a // 2 != b // 2]     # racines lointaines (domaine)
    ZI = {z: i for i, z in enumerate(Z)}
    neg = lambda z: tuple(sorted((z[0] ^ 1, z[1] ^ 1)))
    m = cp_model.CpModel()
    # y[w, z] : lambda(w) = z
    y = {(w, z): m.NewBoolVar("") for w in range(60) for z in range(60)}
    for w in range(60): m.AddExactlyOne(y[w, z] for z in range(60))
    for z in range(60): m.AddExactlyOne(y[w, z] for w in range(60))
    kap = {}
    for (i, j) in kpairs: kap[i] = j; kap[j] = i
    for w in range(60):
        for z in range(60):
            m.Add(y[kap[w], ZI[neg(Z[z])]] == 1).OnlyEnforceIf(y[w, z])
    for a in range(12):
        for b in range(12):
            lits = [y[w, z] for w in range(60) if b in P[w] for z in range(60) if a in Z[z]]
            m.Add(sum(lits) == int(Cx[a, b]))
    s = cp_model.CpSolver(); s.parameters.num_workers = 1; s.parameters.max_time_in_seconds = T
    r = s.Solve(m)
    return s.StatusName(r)

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); ti = int(sys.argv[2]); f = sys.argv[3]; T = float(sys.argv[4])
    mu, reps, st = types(part); tau = reps[ti]
    kp = np.load(f)
    t0 = time.time()
    print("A%s tau#%d kappa=%s : lambda %s (%.1f s)" % (sys.argv[1], ti, os.path.basename(f), solve_lambda(mu, tau, [tuple(p) for p in kp], T), time.time() - t0), flush=True)
