"""CP-SAT (1 fil) sur la formulation compacte de l'etoile libre (notes/20, idee 9). Meme modele que freestar_compact.build :
x[z,p] = [Phi(z) = p] (affectation 60 x 60), (ii) lineaire, (iii) via produits booleens au niveau des orbites.
Une solution trouvee est ensuite verifiee contre le CNF RSF certifie (scripts/freestar_verify_rsf.py).
Usage : python freestar_cpsat.py <partition> <indices|all> <secondes>
"""
import sys, os, json, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortools.sat.python import cp_model
from freestar_compact import far_roots, targets, types

def solve(mu, tau, secs, m=7):
    n2 = 2 * (m - 1); Ws = far_roots(m); nW = len(Ws)
    Z = [Ws[w][h] for w in range(nW) for h in (0, 1)]; nz = len(Z)
    pairs = [p for p in itertools.combinations(range(n2), 2) if mu[p[0]] != p[1]]; nP = len(pairs)
    Cx, Ct = targets(mu, tau, n2)
    md = cp_model.CpModel()
    x = [[md.NewBoolVar("x%d_%d" % (z, p)) for p in range(nP)] for z in range(nz)]
    for z in range(nz): md.AddExactlyOne(x[z])
    for p in range(nP): md.AddExactlyOne([x[z][p] for z in range(nz)])
    B = [[md.NewBoolVar("B%d_%d" % (z, b)) for b in range(n2)] for z in range(nz)]
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
    sv = cp_model.CpSolver(); sv.parameters.num_workers = 1; sv.parameters.max_time_in_seconds = secs
    t0 = time.time(); st = sv.Solve(md); dt = time.time() - t0
    verdict = {cp_model.OPTIMAL: "SAT", cp_model.FEASIBLE: "SAT", cp_model.INFEASIBLE: "UNSAT"}.get(st, "UNKNOWN")
    sol = None
    if verdict == "SAT":
        sol = {str(sorted(Z[z])): list(pairs[[p for p in range(nP) if sv.Value(x[z][p])][0]]) for z in range(nz)}
    return verdict, round(dt, 1), sol

if __name__ == "__main__":
    try:
        import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    except Exception:
        pass
    part = tuple(int(c) for c in sys.argv[1]); secs = float(sys.argv[3])
    mu, reps, st = types(part)
    sel = range(len(reps)) if sys.argv[2] == "all" else [int(i) for i in sys.argv[2].split(",")]
    out = open(os.path.join(HERE, "..", "logs", "freestar_cpsat.jsonl"), "a")
    for i in sel:
        v, dt, sol = solve(mu, reps[i], secs)
        out.write(json.dumps({"part": sys.argv[1], "i": i, "mu": mu, "tau": reps[i], "verdict": v, "s": dt, "sol": sol}) + "\n"); out.flush()
        print("A%s tau#%d %s : %s (%.1f s)" % (sys.argv[1], i, reps[i], v, dt), flush=True)
