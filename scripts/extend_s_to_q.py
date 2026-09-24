"""Etant donne une solution S_out de l'etage S seul, peut-on la completer ?
Q_out = |S_out| + 2D avec D couplage parfait sur les 42 orbites, soumis a :
  (blocs)  sum_{o' contient i} Q_{o o'} = 2 si i dans blocs(o), 4 sinon  -> determine la PAIRE DE BLOCS de D(o) ;
  (Gram)   Q_out^2 + Q_out = 12 I + 4 J - B B^T ;
et supp S = {Q = 1} (automatique : D evite le support de S).
Si oui, on releve (a,b) = ((Q+S)/2, (Q-S)/2) et on verifie A^2 + A - 12I = 2J sur 99 sommets.
Usage : python extend_s_to_q.py data/stage_s_solution_seed0.json
"""
import sys, json, itertools
import numpy as np

d = json.load(open(sys.argv[1]))
orb = [tuple(x) for x in d["orb"]]; So = np.array(d["S_out"]); N = len(orb); m = d.get("m", 7)
E = np.abs(So)
B = np.zeros((N, m), dtype=int)
for o, (i, j, t) in enumerate(orb): B[o, i] = B[o, j] = 1
target_pair = []
ok = True
for o in range(N):
    need = []
    for i in range(m):
        s = sum(E[o, p] for p in range(N) if B[p, i] and p != o)
        t = 2 if B[o, i] else 4
        dd = t - s
        if dd not in (0, 2): ok = False; need = None; break
        if dd == 2: need.append(i)
    if need is None or len(need) != 2:
        ok = False
        print("orbite %d %s : sommes par bloc incompatibles (besoin %s)" % (o, orb[o], need)); break
    target_pair.append(tuple(need))
if not ok:
    print("=> aucune completion possible (contrainte de blocs)"); sys.exit(0)
cand = []
for o in range(N):
    i, j = target_pair[o]
    cand.append([p for p in range(N) if p != o and E[o, p] == 0 and B[p, i] and B[p, j]])
print("candidats par orbite :", [len(c) for c in cand])
rhs = (2 * m - 2) * np.eye(N, dtype=int) + 4 * np.ones((N, N), dtype=int) - B @ B.T
sols = []
def rec(D):
    free = [o for o in range(N) if o not in D]
    if not free:
        Q = E.copy()
        for o, p in D.items(): Q[o, p] = 2
        if (Q @ Q + Q == rhs).all(): sols.append(dict(D))
        return
    o = min(free, key=lambda o: len([p for p in cand[o] if p not in D]))
    for p in cand[o]:
        if p in D or o not in cand[p]: continue
        D[o] = p; D[p] = o
        rec(D)
        del D[o]; del D[p]
rec({})
print("completions D valides :", len(sols))
for D in sols[:3]:
    types = []
    for o, p in D.items():
        if o < p:
            s = len(set(orb[o][:2]) & set(orb[p][:2]))
            types.append({2: "sib", 1: "one", 0: "dis"}[s])
    print("  types D :", {t: types.count(t) for t in set(types)})
