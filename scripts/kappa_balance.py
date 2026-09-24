"""Probleme kappa + lemme d'equilibre (note 23 §8), cubes a plusieurs composantes (orbites de <s, mu, tau> sur X).
Pour la paire kappa {w, w'} = {Phi(z), Phi(-z)} : |z inter S| + |w inter S| + |w' inter S| = |S|/2 pour chaque orbite S.
Donc |w inter S| + |w' inter S| <= |S|/2, et le profil de z est determine : |z inter S| = |S|/2 - |w inter S| - |w' inter S|.
Comptes : pour chaque profil p de racine (nb d'elements de z dans chaque orbite), le nb de paires kappa de profil complementaire
= (nb de racines z de profil p)/2.  CP-SAT 1 fil, reponses definitives seulement.
Usage : python kappa_balance.py <partition> <indices> <secondes>
"""
import sys, os, time, itertools, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types
from ortools.sat.python import cp_model

def orbits(mu, tau):
    seen = set(); orbs = []
    for a in range(12):
        if a in seen: continue
        S = {a}; fr = [a]
        while fr:
            y = fr.pop()
            for g in (y ^ 1, mu[y], tau[y]):
                if g not in S: S.add(g); fr.append(g)
        seen |= S; orbs.append(sorted(S))
    return orbs

def run(mu, tau, T):
    Cx, Ct = targets(mu, tau, 12)
    orbs = orbits(mu, tau); oid = {a: k for k, S in enumerate(orbs) for a in S}; half = [len(S) // 2 for S in orbs]
    P = [(a, b) for a in range(12) for b in range(a + 1, 12) if mu[a] != b]
    Zs = [(a, b) for a in range(12) for b in range(a + 1, 12) if a // 2 != b // 2]
    prof = lambda s: tuple(sum(1 for y in s if oid[y] == k) for k in range(len(orbs)))
    need = collections.Counter(prof(z) for z in Zs)
    m = cp_model.CpModel(); x = {}; byprof = collections.defaultdict(list)
    for i, j in itertools.combinations(range(60), 2):
        pw = prof(P[i]); pv = prof(P[j]); tot = tuple(pw[k] + pv[k] for k in range(len(orbs)))
        if any(tot[k] > half[k] for k in range(len(orbs))): continue
        zp = tuple(half[k] - tot[k] for k in range(len(orbs)))
        v = m.NewBoolVar(""); x[i, j] = v; byprof[zp].append(v)
    for i in range(60):
        m.AddExactlyOne(v for (a, b), v in x.items() if i in (a, b))
    cov = collections.defaultdict(list)
    for (i, j), v in x.items():
        for u in P[i]:
            for w in P[j]:
                cov[(min(u, w), max(u, w))].append(v)
    for b in range(12):
        for d in range(b, 12):
            tgt = Ct[b, d] // 2 if b == d else Ct[b, d]
            m.Add(sum(cov[(b, d)]) == int(tgt))
    for zp, c in need.items():
        m.Add(sum(byprof[zp]) == c // 2)
    for zp in byprof:
        if zp not in need: m.Add(sum(byprof[zp]) == 0)
    s = cp_model.CpSolver(); s.parameters.num_workers = 1; s.parameters.max_time_in_seconds = T
    r = s.Solve(m)
    return s.StatusName(r), orbs, len(x)

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); T = float(sys.argv[3])
    mu, reps, st = types(part)
    for ti in [int(v) for v in sys.argv[2].split(",")]:
        t0 = time.time(); r, orbs, nopt = run(mu, reps[ti], T)
        print("A%s tau#%d : orbites %s ; %d paires kappa permises ; kappa+equilibre : %s (%.1f s)" % (sys.argv[1], ti, [len(S) for S in orbs], nopt, r, time.time() - t0), flush=True)
