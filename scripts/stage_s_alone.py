"""Etage S SEUL (jamais teste dans le depot C2 avec C^T S_out = 0) : existe-t-il S_out dans {0,±1}^{42x42} symetrique,
diagonale nulle, avec S_out C = 0 et S_out^2 + S_out = 12 I - C C^T ?  (C fixe par le choix des representants.)
Si UNSAT : C2 est mort. Si SAT : on teste sur la solution le theoreme de parite (rang_7(S - 3I) pair, S 49x49).
CP-SAT (booleens pos/neg par paire, produits par ET logiques).
Usage : python stage_s_alone.py [temps_s] [workers] [graine]
"""
import sys, os, json, time, itertools
import numpy as np
from ortools.sat.python import cp_model

m = 7
T = float(sys.argv[1]) if len(sys.argv) > 1 else 1800
W = int(sys.argv[2]) if len(sys.argv) > 2 else 12
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 0
SYM = sys.argv[4] if len(sys.argv) > 4 else 'none'
BLOCKS = (len(sys.argv) > 5 and sys.argv[5] == 'blocks')
LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

orb = [(i, j, t) for i in range(m) for j in range(i + 1, m) for t in (1, -1)]   # representant e_i + t e_j
N = len(orb)
C = np.zeros((N, m), dtype=int)
for o, (i, j, t) in enumerate(orb):
    C[o, i] = 1; C[o, j] = t
G = C @ C.T
assert (C.T @ C == 12 * np.eye(m, dtype=int)).all()

md = cp_model.CpModel()
pos, neg = {}, {}
for o in range(N):
    for p in range(o + 1, N):
        pos[o, p] = md.NewBoolVar(""); neg[o, p] = md.NewBoolVar("")
        md.AddBoolOr([pos[o, p].Not(), neg[o, p].Not()])
def P(o, p): return pos[min(o, p), max(o, p)]
def Ng(o, p): return neg[min(o, p), max(o, p)]
def S(o, p): return P(o, p) - Ng(o, p)

# symetrie imposee (permutation signee des coordonnees) : S_{g(o),g(p)} s_o s_p = S_{o,p}
def act(perm, sg):
    res = []
    for (i, j, t) in orb:
        v = {perm[i]: sg[i], perm[j]: sg[j] * t}
        a, b = sorted(v)
        s = v[a]                      # on ramene au representant (+1 sur le plus petit indice)
        res.append((orb.index((a, b, v[b] * s)), s))
    return res
if SYM != 'none':
    gens = {'cyc7': [[1, 2, 3, 4, 5, 6, 0]], 'cyc3': [[1, 2, 0, 4, 5, 3, 6]],
            'f21': [[1, 2, 3, 4, 5, 6, 0], [0, 2, 4, 6, 1, 3, 5]], 'mul2': [[0, 2, 4, 6, 1, 3, 5]]}[SYM]
    for perm in gens:
        g = act(perm, [1] * m)
        for (o, p) in list(pos):
            (go, so), (gp, sp) = g[o], g[p]
            if so * sp == 1:
                md.Add(P(go, gp) == pos[o, p]); md.Add(Ng(go, gp) == neg[o, p])
            else:
                md.Add(P(go, gp) == neg[o, p]); md.Add(Ng(go, gp) == pos[o, p])
    print("symetrie imposee :", SYM, flush=True)
# option 'blocks' : couplage D (hors support de S) + sommes par bloc de Q = |S| + 2D (etage Q sans son equation quadratique)
if BLOCKS:
    dlt = {}
    for (o, p) in pos:
        dlt[o, p] = md.NewBoolVar("")
        md.AddImplication(dlt[o, p], pos[o, p].Not()); md.AddImplication(dlt[o, p], neg[o, p].Not())
    DD = lambda o, p: dlt[min(o, p), max(o, p)]
    for o in range(N):
        md.AddExactlyOne([DD(o, p) for p in range(N) if p != o])
        for i in range(m):
            t = 2 if C[o, i] != 0 else 4
            md.Add(sum(P(o, p) + Ng(o, p) + 2 * DD(o, p) for p in range(N) if p != o and C[p, i] != 0) == t)
    print("option blocks : couplage D + sommes par bloc", flush=True)
# diagonale de S^2 : 10 non-nuls par ligne
for o in range(N):
    md.Add(sum(P(o, p) + Ng(o, p) for p in range(N) if p != o) == 10)
# S_out C = 0
for o in range(N):
    for i in range(m):
        md.Add(sum(int(C[p, i]) * S(o, p) for p in range(N) if p != o and C[p, i] != 0) == 0)
# hors diagonale : sum_k S_ok S_kp + S_op = -G_op
def AND(a, b):
    z = md.NewBoolVar(""); md.AddBoolAnd([a, b]).OnlyEnforceIf(z); md.AddBoolOr([a.Not(), b.Not()]).OnlyEnforceIf(z.Not())
    return z
cnt = 0
for o in range(N):
    for p in range(o + 1, N):
        terms = []
        for k in range(N):
            if k == o or k == p: continue
            a1 = AND(P(o, k), P(k, p)); a2 = AND(Ng(o, k), Ng(k, p))
            a3 = AND(P(o, k), Ng(k, p)); a4 = AND(Ng(o, k), P(k, p))
            terms += [a1, a2, -1 * a3, -1 * a4]
            cnt += 4
        md.Add(sum(terms) + S(o, p) == int(-G[o, p]))
# redondant : somme des signes des triangles (tr S_out^3 = -420)
print("modele : %d booleens de base, %d produits" % (2 * len(pos), cnt), flush=True)

sv = cp_model.CpSolver()
sv.parameters.max_time_in_seconds = T
sv.parameters.num_search_workers = W
sv.parameters.random_seed = SEED
sv.parameters.log_search_progress = False
t0 = time.time()
st = sv.Solve(md)
print("statut :", sv.StatusName(st), "en %.0f s" % (time.time() - t0), flush=True)
if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    So = np.zeros((N, N), dtype=int)
    for (o, p) in pos:
        v = sv.Value(pos[o, p]) - sv.Value(neg[o, p]); So[o, p] = So[p, o] = v
    assert (So @ C == 0).all() and (So @ So + So == 12 * np.eye(N, dtype=int) - G).all()
    Sfull = np.zeros((49, 49), dtype=int)
    Sfull[:7, :7] = -np.eye(7, dtype=int); Sfull[:7, 7:] = C.T; Sfull[7:, :7] = C; Sfull[7:, 7:] = So
    assert (Sfull @ Sfull + Sfull == 12 * np.eye(49, dtype=int)).all()
    sys.path.insert(0, os.path.join(LAB, "scripts"))
    from padic import rank_mod_p
    r49 = rank_mod_p((Sfull - 3 * np.eye(49, dtype=int)) % 7, 7)
    r42 = rank_mod_p((So - 3 * np.eye(N, dtype=int)) % 7, 7)
    print("rang_7(S - 3I) [49x49] = %d  (theoreme : pair)   rang_7(S_out - 3I) = %d (theoreme : pair)" % (r49, r42), flush=True)
    out = os.path.join(LAB, "data", "stage_s_solution_%s%s_seed%d.json" % (SYM, "_blocks" if BLOCKS else "", SEED))
    Dsol = [[o, p] for (o, p) in dlt if sv.Value(dlt[o, p])] if BLOCKS else None
    json.dump({"orb": orb, "D": Dsol, "S_out": So.tolist(), "rank7_S49": int(r49), "rank7_Sout": int(r42)}, open(out, "w"))
    print("solution ecrite :", out, flush=True)
