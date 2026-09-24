"""Relaxation LP (puis MILP) de la formulation compacte de l'etoile libre, au niveau des orbites lointaines (notes/20, idee 8).
Variables y[W,(f,f')] : l'orbite lointaine W = {z_W, -z_W} recoit Phi(z_W) = f et Phi(-z_W) = f' (f != f' paires hors mu).
Contraintes lineaires : une paire ordonnee par W ; chaque paire hors mu utilisee exactement une fois ; (ii) ; (iii).
Si le LP est infaisable, le type (mu, tau) est impossible (certificat de Farkas, verifiable en arithmetique exacte).
Usage : python freestar_lp.py <partition> <indices|all> [milp_secondes]
"""
import sys, os, json, time, itertools
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import far_roots, targets, types

def model(mu, tau, m=7):
    n2 = 2 * (m - 1); Ws = far_roots(m); nW = len(Ws)
    pairs = [p for p in itertools.combinations(range(n2), 2) if mu[p[0]] != p[1]]; nP = len(pairs)
    Cx, Ct = targets(mu, tau, n2)
    ords = [(i, j) for i in range(nP) for j in range(nP) if i != j]; nO = len(ords)
    ncol = nW * nO
    rows, cols, vals = [], [], []; rhs = []; r = 0
    col = lambda w, o: w * nO + o
    # (a) une paire ordonnee par W
    for w in range(nW):
        for o in range(nO): rows.append(r); cols.append(col(w, o)); vals.append(1)
        rhs.append(1); r += 1
    # (b) chaque paire utilisee une fois
    use = {i: [] for i in range(nP)}
    for o, (i, j) in enumerate(ords): use[i].append(o); use[j].append(o)
    for i in range(nP):
        for w in range(nW):
            for o in use[i]: rows.append(r); cols.append(col(w, o)); vals.append(1)
        rhs.append(1); r += 1
    # (ii)
    rid = {}
    for a in range(n2):
        for b in range(n2): rid[a, b] = r; rhs.append(int(Cx[a, b])); r += 1
    acc = {}
    for w in range(nW):
        z, mz = Ws[w]
        for o, (i, j) in enumerate(ords):
            c = col(w, o)
            for a in z:
                for b in pairs[i]: acc[(rid[a, b], c)] = acc.get((rid[a, b], c), 0) + 1
            for a in mz:
                for b in pairs[j]: acc[(rid[a, b], c)] = acc.get((rid[a, b], c), 0) + 1
    # (iii)
    tid = {}
    for b in range(n2):
        for d in range(b, n2): tid[b, d] = r; rhs.append(int(Ct[b, d])); r += 1
    for w in range(nW):
        for o, (i, j) in enumerate(ords):
            c = col(w, o)
            for b in pairs[i]:
                for d in pairs[j]:
                    key = (tid[min(b, d), max(b, d)], c)
                    acc[key] = acc.get(key, 0) + (2 if b == d else 1)
    for (rr, c), v in acc.items(): rows.append(rr); cols.append(c); vals.append(v)
    Aeq = sp.csr_matrix((vals, (rows, cols)), shape=(r, ncol), dtype=float)
    return Aeq, np.array(rhs, dtype=float), (Ws, pairs, ords)

if __name__ == "__main__":
    try:
        import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    except Exception:
        pass
    part = tuple(int(c) for c in sys.argv[1]); T = float(sys.argv[3]) if len(sys.argv) > 3 else 0
    mu, reps, st = types(part)
    sel = range(len(reps)) if sys.argv[2] == "all" else [int(i) for i in sys.argv[2].split(",")]
    out = open(os.path.join(HERE, "..", "logs", "freestar_lp.jsonl"), "a")
    for i in sel:
        t0 = time.time()
        Aeq, beq, meta = model(mu, reps[i])
        tb = time.time() - t0
        res = linprog(np.zeros(Aeq.shape[1]), A_eq=Aeq, b_eq=beq, bounds=(0, 1), method="highs")
        lp = {0: "FAISABLE", 2: "INFAISABLE"}.get(res.status, "statut %d" % res.status)
        rec = {"part": sys.argv[1], "i": i, "tau": reps[i], "rows": Aeq.shape[0], "cols": Aeq.shape[1], "nnz": int(Aeq.nnz),
               "build_s": round(tb, 1), "lp": lp, "lp_s": round(time.time() - t0 - tb, 1)}
        if lp == "FAISABLE" and T > 0:
            t1 = time.time()
            r2 = milp(np.zeros(Aeq.shape[1]), constraints=LinearConstraint(Aeq, beq, beq), integrality=np.ones(Aeq.shape[1]),
                      bounds=Bounds(0, 1), options={"time_limit": T})
            rec["milp"] = {0: "SOLUTION", 1: "LIMITE", 2: "INFAISABLE"}.get(r2.status, "statut %d" % r2.status)
            rec["milp_s"] = round(time.time() - t1, 1)
            if r2.status == 0:
                Ws, pairs, ords = meta; x = np.round(r2.x).astype(int); nO = len(ords)
                rec["sol"] = [[pairs[ords[o][0]], pairs[ords[o][1]]] for w in range(len(Ws)) for o in [int(np.argmax(x[w * nO:(w + 1) * nO]))]]
        out.write(json.dumps(rec) + "\n"); out.flush()
        print({k: v for k, v in rec.items() if k != "sol"}, flush=True)
