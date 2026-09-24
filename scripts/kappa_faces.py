"""Relaxation « (iii) + faces » du probleme local (note 23 §5).
Faces : pour a dans X, G_a = Phi(star a) = {Phi(z) : a dans z} (10 paires) ; (ii) <=> deg_{G_a}(b) = Cx[a, b] ; et G_{-a} = kappa(G_a).
Modele : kappa (couplage parfait des 60 paires, comptes (iii) exacts) + pour chaque a d'une liste A, un ensemble G_a de 10 paires,
disjoint de kappa(G_a), avec deg_{G_a} = Cx[a, .] et deg_{kappa(G_a)} = Cx[-a, .].  Option « inter » : |G_a inter G_a'| = 1
pour a' != +-a (a, a' dans A), comme l'impose la bijectivite de Phi.
Usage : python kappa_faces.py <partition> <tau> <liste des a (ex. 10,11 ou all)> <inter 0/1> <secondes>
"""
import sys, os, itertools, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types
from ortools.sat.python import cp_model

def build(mu, tau, A, inter):
    Cx, Ct = targets(mu, tau, 12)
    P = [(a, b) for a in range(12) for b in range(a + 1, 12) if mu[a] != b]
    m = cp_model.CpModel()
    x = {}
    for i, j in itertools.combinations(range(60), 2):
        x[i, j] = m.NewBoolVar("")
    X = lambda i, j: x[min(i, j), max(i, j)]
    for i in range(60):
        m.AddExactlyOne(X(i, j) for j in range(60) if j != i)
    cov = {}
    for (i, j), v in x.items():
        for u in P[i]:
            for w in P[j]:
                cov.setdefault((min(u, w), max(u, w)), []).append(v)
    for b in range(12):
        for d in range(b, 12):
            tgt = Ct[b, d] // 2 if b == d else Ct[b, d]
            m.Add(sum(cov.get((b, d), [])) == tgt)
    g = {}
    for a in A:
        ga = [m.NewBoolVar("") for _ in range(60)]; ha = [m.NewBoolVar("") for _ in range(60)]   # ha = kappa(G_a) = G_{-a}
        for (i, j), v in x.items():
            m.Add(ha[j] == ga[i]).OnlyEnforceIf(v); m.Add(ha[i] == ga[j]).OnlyEnforceIf(v)
        for w in range(60):
            m.AddBoolOr([ga[w].Not(), ha[w].Not()])
        for b in range(12):
            m.Add(sum(ga[w] for w in range(60) if b in P[w]) == int(Cx[a, b]))
            m.Add(sum(ha[w] for w in range(60) if b in P[w]) == int(Cx[a ^ 1, b]))
        m.Add(sum(ga) == 10)
        g[a] = ga; g[a ^ 1] = ha
    if inter:
        keys = sorted(g)
        for a, a2 in itertools.combinations(keys, 2):
            if a2 == a ^ 1: continue
            pr = []
            for w in range(60):
                t = m.NewBoolVar(""); m.AddBoolAnd([g[a][w], g[a2][w]]).OnlyEnforceIf(t)
                m.AddBoolOr([g[a][w].Not(), g[a2][w].Not()]).OnlyEnforceIf(t.Not()); pr.append(t)
            m.Add(sum(pr) == 1)
    return m, x, g, P

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); ti = int(sys.argv[2])
    A = list(range(0, 12, 2)) if sys.argv[3] == "all" else [int(v) for v in sys.argv[3].split(",")]
    inter = sys.argv[4] == "1"; T = float(sys.argv[5])
    mu, reps, st = types(part); tau = reps[ti]
    m, x, g, P = build(mu, tau, A, inter)
    s = cp_model.CpSolver(); s.parameters.num_workers = 1; s.parameters.max_time_in_seconds = T
    t0 = time.time(); r = s.Solve(m)
    print("A%s tau#%d faces a=%s inter=%d : %s (%.1f s)" % (sys.argv[1], ti, sys.argv[3], inter, s.StatusName(r), time.time() - t0), flush=True)
