"""Noyau minimal (par deletion) des contraintes (ii) « = 2 » qui rendent l'etage lambda infaisable pour un kappa donne."""
import sys, os, itertools, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types
from ortools.sat.python import cp_model

def feasible(mu, tau, kpairs, entries, zero=True, T=30):
    Cx, Ct = targets(mu, tau, 12)
    P = [(a, b) for a in range(12) for b in range(a + 1, 12) if mu[a] != b]
    Z = [(a, b) for a in range(12) for b in range(a + 1, 12) if a // 2 != b // 2]
    ZI = {z: i for i, z in enumerate(Z)}
    neg = lambda z: tuple(sorted((z[0] ^ 1, z[1] ^ 1)))
    m = cp_model.CpModel()
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
            v = int(Cx[a, b])
            if (v == 0 and zero) or (a, b) in entries:
                lits = [y[w, z] for w in range(60) if b in P[w] for z in range(60) if a in Z[z]]
                m.Add(sum(lits) == v)
    s = cp_model.CpSolver(); s.parameters.num_workers = 1; s.parameters.max_time_in_seconds = T
    r = s.Solve(m)
    return s.StatusName(r)

if __name__ == "__main__":
    ti = int(sys.argv[1])
    mu, reps, st = types((1,1,1,1,1,1)); tau = reps[ti]
    Cx, Ct = targets(mu, tau, 12)
    kp = [tuple(p) for p in np.load("logs/kappa_sol_A111111_t%d.npy" % ti)]
    ent = [(a, b) for a in range(12) for b in range(12) if Cx[a, b] == 2]
    assert feasible(mu, tau, kp, set(ent)) == "INFEASIBLE"
    core = list(ent)
    i = 0
    while i < len(core):
        trial = core[:i] + core[i + 1:]
        if feasible(mu, tau, kp, set(trial)) == "INFEASIBLE":
            core = trial
        else:
            i += 1
    nm = lambda x: ("+" if x % 2 == 0 else "-") + str(x // 2 + 1)
    print("tau#%d : noyau de %d cases (a,b) [C2=2] : %s" % (ti, len(core), " ".join("(%s,%s)" % (nm(a), nm(b)) for a, b in core)))
    print("  zero seul + noyau, sans les zeros :", feasible(mu, tau, kp, set(core), zero=False))
