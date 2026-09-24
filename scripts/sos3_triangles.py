"""Cran suivant (notes/16) : relaxation de degre 2 (sos2_relax.py) + moments de TRIANGLES de degre 3.

Au degre 2, l'equation srg entre racines  sum_w Q_uw Q_wv + Q_uv = 2 - |u n v|  melange lambda et mu.  Le scinder demande le degre 3 :
  (P_adj)  E[ x_uv * sum_w x_uw x_wv ] = (1 - |u n v|) E[x_uv]      (une arete a exactement 1 - |u n v| triangles de racines)
(la partie mu s'en deduit).  Variables ajoutees : z_T = E[x_uv x_uw x_vw] pour chaque triangle de racines {u,v,w} (a t pres),
symetrisees par W(B_m) (moyenne des reetiquetages d'une solution).  Contraintes : (P_adj) ; Sherali-Adams niveau 2 sur chaque triplet
(les 8 probabilites d'atomes >= 0).  Tout le reste (degre 2, PSD) est repris de sos2_relax.py.
Usage : python sos3_triangles.py <m> [feas | ysib_min | ysib_max | all]
"""
import sys, time, itertools
import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components
sys.path.insert(0, __file__.rsplit("\\", 1)[0] if "\\" in __file__ else ".")
import sos2_relax as S2

def triangles(info, m):
    ROOTS, var, neg = info["ROOTS"], info["var"], info["neg"]
    R = len(ROOTS)
    RI = {r: i for i, r in enumerate(ROOTS)}
    ok = lambda a, b: a != b and a != neg(b)
    keys, KI = [], {}
    for a, b, c in itertools.combinations(range(R), 3):
        u, v, w = ROOTS[a], ROOTS[b], ROOTS[c]
        if not (ok(u, v) and ok(u, w) and ok(v, w)):
            continue
        k1 = frozenset([u, v, w]); k2 = frozenset([neg(u), neg(v), neg(w)])
        key = frozenset([k1, k2])
        if key not in KI:
            KI[key] = len(keys); keys.append((u, v, w))
    # orbites sous W(B_m)
    gens = [lambda h: (h[0], -h[1]) if h[0] == 1 else h,
            lambda h: ({1: 2, 2: 1}.get(h[0], h[0]), h[1]),
            lambda h: (h[0] % m + 1, h[1])]
    n = len(keys)
    rows, cols = [], []
    for g in gens:
        for i, (u, v, w) in enumerate(keys):
            gu, gv, gw = (frozenset(g(h) for h in r) for r in (u, v, w))
            j = KI[frozenset([frozenset([gu, gv, gw]), frozenset([neg(gu), neg(gv), neg(gw)])])]
            rows.append(i); cols.append(j)
    G = sp.csr_matrix((np.ones(len(rows), dtype=np.int8), (rows, cols)), shape=(n, n))
    nt, tlab = connected_components(G, directed=True, connection="weak")
    return keys, KI, nt, tlab

def solve(m, objective="feas"):
    import cvxpy as cp
    L, eqs, info = S2.build(m)
    d, orb, var, neg, ROOTS = info["d"], info["orb"], info["var"], info["neg"], info["ROOTS"]
    keys, KI, nt, tlab = triangles(info, m)
    print("   triangles de racines (a t pres) : %d ; orbites : %d" % (len(keys), nt), flush=True)
    x = cp.Variable(d); z = cp.Variable(nt)
    cons = []
    A = np.zeros((len(eqs), d)); rhs = np.zeros(len(eqs))
    for r, (row, c) in enumerate(eqs):
        for k, v in row.items():
            A[r, k] += v
        rhs[r] = c
    cons.append(A @ x == rhs)
    reps = info["reps"]
    for k in range(d):
        e, f = reps[k]
        if e >= 1 and f >= 1 and e != f:
            ke, kf = orb[0, e], orb[0, f]
            cons += [x[k] >= 0, x[k] <= x[ke], x[k] <= x[kf], x[k] >= x[ke] + x[kf] - 1]
    Lx = sum(x[k] * L[k] for k in range(d))
    cons.append((Lx + Lx.T) / 2 >> 0)
    # Sherali-Adams niveau 2 sur un representant de chaque orbite de triangles
    seen = set()
    for i, (u, v, w) in enumerate(keys):
        t = tlab[i]
        if t in seen:
            continue
        seen.add(t)
        a, b, c = var(u, v), var(u, w), var(v, w)
        ya, yb, yc = x[orb[0, a]], x[orb[0, b]], x[orb[0, c]]
        yab, yac, ybc = x[orb[a, b]], x[orb[a, c]], x[orb[b, c]]
        zt = z[t]
        cons += [zt >= 0, yab - zt >= 0, yac - zt >= 0, ybc - zt >= 0,
                 ya - yab - yac + zt >= 0, yb - yab - ybc + zt >= 0, yc - yac - ybc + zt >= 0,
                 1 - ya - yb - yc + yab + yac + ybc - zt >= 0]
    # (P_adj) : pour u0 et chaque v
    u0 = ROOTS[0]
    rows = {}
    for v in ROOTS:
        if v == u0 or v == neg(u0):
            continue
        cnt = np.zeros(nt)
        for w in ROOTS:
            if w in (u0, v, neg(u0), neg(v)):
                continue
            cnt[tlab[KI[frozenset([frozenset([u0, v, w]), frozenset([neg(u0), neg(v), neg(w)])])]]] += 1
        key = (tuple(np.round(cnt, 9)), orb[0, var(u0, v)], len(u0 & v))
        rows[key] = (cnt, orb[0, var(u0, v)], 1 - len(u0 & v))
    for cnt, k0, c in rows.values():
        cons.append(cnt @ z == c * x[k0])
    print("   equations (P_adj) distinctes : %d" % len(rows), flush=True)
    u0s = [w for w in ROOTS if w != u0 and w != neg(u0) and {i for i, _ in w} == {i for i, _ in u0}]
    ksis = orb[0, var(u0, u0s[0])]
    obj = {"feas": cp.Minimize(0), "ysib_min": cp.Minimize(x[ksis]), "ysib_max": cp.Maximize(x[ksis])}[objective]
    prob = cp.Problem(obj, cons)
    t0 = time.time()
    prob.solve(solver="CLARABEL")
    print("   %s : statut %s, y_soeur = %s  [%.1f s]" % (objective, prob.status,
          None if x.value is None else round(float(x.value[ksis]), 6), time.time() - t0), flush=True)
    return prob, x, z, info

if __name__ == "__main__":
    try:
        import ctypes; kk = ctypes.windll.kernel32
        kk.GetCurrentProcess.restype = ctypes.c_void_p; kk.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        kk.SetPriorityClass(kk.GetCurrentProcess(), 0x40)
    except Exception:
        pass
    m = int(sys.argv[1]); o = sys.argv[2] if len(sys.argv) > 2 else "feas"
    for obj in (["feas", "ysib_min", "ysib_max"] if o == "all" else [o]):
        solve(m, obj)
