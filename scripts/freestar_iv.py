"""Formulation compacte (i)-(iii) + la contrainte NOUVELLE (iv) (note 23 §6) :
deux sommets lointains z != z' ont au plus 2 voisins communs, donc au plus 2 dans N(l_1) :
  |z inter z'| + |Phi(z) inter Phi(z')| + |Phi(-z) inter Phi(-z')| <= 2.
Seul le cas « z et z' partagent un vecteur a » n'est pas automatique ; il devient
  [Phi(z), Phi(z') adjacentes] + [Phi(-z), Phi(-z') adjacentes] <= 1.
CP-SAT 1 fil ; on ne consigne que les reponses definitives.
Usage : python freestar_iv.py <partition> <indices|all> <secondes> [iv 0/1]
"""
import sys, os, json, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortools.sat.python import cp_model
from freestar_compact import far_roots, targets, types

def model(mu, tau, use_iv=True, m=7):
    n2 = 2 * (m - 1); Ws = far_roots(m); nW = len(Ws)
    Z = [Ws[w][h] for w in range(nW) for h in (0, 1)]; nz = len(Z)          # Z[z ^ 1] = -Z[z]
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
    if use_iv:
        adj = {}
        for z, z2 in itertools.combinations(range(nz), 2):
            if len(set(Z[z]) & set(Z[z2])) == 1:
                v = md.NewBoolVar("")
                for b in range(n2):
                    md.Add(v >= B[z][b] + B[z2][b] - 1)
                adj[z, z2] = v
        for (z, z2), v in adj.items():
            w = adj.get((min(z ^ 1, z2 ^ 1), max(z ^ 1, z2 ^ 1)))
            if w is not None and z < (z ^ 1):
                md.Add(v + w <= 1)
    return md, x, Z, pairs

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); secs = float(sys.argv[3])
    use_iv = (sys.argv[4] == "1") if len(sys.argv) > 4 else True
    mu, reps, st = types(part)
    sel = range(len(reps)) if sys.argv[2] == "all" else [int(i) for i in sys.argv[2].split(",")]
    for i in sel:
        md, x, Z, pairs = model(mu, reps[i], use_iv)
        sv = cp_model.CpSolver(); sv.parameters.num_workers = 1; sv.parameters.max_time_in_seconds = secs
        t0 = time.time(); stt = sv.Solve(md)
        print("A%s tau#%d (iv=%d) : %s (%.1f s)" % (sys.argv[1], i, use_iv, sv.StatusName(stt), time.time() - t0), flush=True)
