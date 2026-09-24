"""Formulation compacte (i)-(iii) + contraintes DERIVEES (note 23 §6-8) :
 (iv)  lointains z != z' partageant a : [Phi(z) adj Phi(z')] + [Phi(-z) adj Phi(-z')] <= 1   (mu <= 2 entre lointains)
 (v)   z ~ a et a dans Phi(z) => -a pas dans Phi(-z) ; b dans z et b dans Phi(z) => tau(b) pas dans Phi(-z)   (lambda = 1 (N,F))
 (bal) pour tout w du noyau de BB^T (niveau type) : sum_u w_u B[u, z] = 0 pour chaque lointain z   (somme de carres nulle)
CP-SAT 1 fil. On ne consigne que les reponses definitives.
Usage : python freestar_sos.py <partition> <indices> <secondes> [flags: iv,v,bal]
"""
import sys, os, time, itertools
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortools.sat.python import cp_model
from freestar_compact import far_roots, targets, types
from far_spectrum_test import BBt

def model(mu, tau, flags, m=7):
    n2 = 12; Ws = far_roots(m); nW = len(Ws)
    Z = [Ws[w][h] for w in range(nW) for h in (0, 1)]; nz = len(Z)
    pairs = [p for p in itertools.combinations(range(n2), 2) if mu[p[0]] != p[1]]; nP = len(pairs)
    Cx, Ct = targets(mu, tau, n2)
    md = cp_model.CpModel()
    x = [[md.NewBoolVar("") for p in range(nP)] for z in range(nz)]
    for z in range(nz): md.AddExactlyOne(x[z])
    for p in range(nP): md.AddExactlyOne([x[z][p] for z in range(nz)])
    B = [[md.NewBoolVar("") for b in range(n2)] for z in range(nz)]
    for z in range(nz):
        for b in range(n2):
            md.Add(B[z][b] == sum(x[z][p] for p in range(nP) if b in pairs[p]))
    for a in range(n2):
        for b in range(n2):
            md.Add(sum(B[z][b] for z in range(nz) if a in Z[z]) == int(Cx[a, b]))
    u = {}
    for z in range(nz):
        for b in range(n2):
            for d in range(n2):
                v = md.NewBoolVar(""); md.AddMultiplicationEquality(v, [B[z][b], B[z ^ 1][d]]); u[z, b, d] = v
    for b in range(n2):
        for d in range(n2):
            md.Add(sum(u[z, b, d] for z in range(nz)) == int(Ct[b, d]))
    if "iv" in flags:
        adj = {}
        for z, z2 in itertools.combinations(range(nz), 2):
            if len(set(Z[z]) & set(Z[z2])) == 1:
                v = md.NewBoolVar("")
                for b in range(n2):
                    md.Add(v >= B[z][b] + B[z2][b] - 1)
                adj[z, z2] = v
        for (z, z2), v in adj.items():
            if z < (z ^ 1) or True:
                w = adj.get((min(z ^ 1, z2 ^ 1), max(z ^ 1, z2 ^ 1)))
                if w is not None and (z, z2) < (min(z ^ 1, z2 ^ 1), max(z ^ 1, z2 ^ 1)):
                    md.Add(v + w <= 1)
    if "v" in flags:
        for z in range(nz):
            for a in Z[z]:
                md.AddBoolOr([B[z][a].Not(), B[z ^ 1][a ^ 1].Not()])
                md.AddBoolOr([B[z][a].Not(), B[z ^ 1][tau[a]].Not()])
    if "bal" in flags:
        M = sp.Matrix(BBt(mu, tau).tolist())
        for vec in M.nullspace():
            vec = vec * sp.ilcm(*[sp.fraction(q)[1] for q in vec]); vec = [int(q) for q in vec]
            for z in range(nz):
                # B[u,z] : P_x (a) : a dans Z[z] ; P_q (b) : B[z][b] ; P_r (c) : -c dans Phi(-z) : B[z^1][c^1]
                const = sum(vec[a] for a in Z[z])
                md.Add(const + sum(vec[12 + b] * B[z][b] for b in range(12)) + sum(vec[24 + c] * B[z ^ 1][c ^ 1] for c in range(12)) == 0)
    return md

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); secs = float(sys.argv[3])
    flags = sys.argv[4].split(",") if len(sys.argv) > 4 else ["iv", "v", "bal"]
    mu, reps, st = types(part)
    for i in [int(v) for v in sys.argv[2].split(",")]:
        t0 = time.time(); md = model(mu, reps[i], flags); tb = time.time() - t0
        sv = cp_model.CpSolver(); sv.parameters.num_workers = 1; sv.parameters.max_time_in_seconds = secs
        stt = sv.Solve(md)
        print("A%s tau#%d flags=%s : %s (modele %.0f s, resolution %.1f s)" % (sys.argv[1], i, ",".join(flags), sv.StatusName(stt), tb, sv.WallTime()), flush=True)
