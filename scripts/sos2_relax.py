"""Relaxation de moments de degre 2 (Shor / Sherali-Adams niveau 1 + PSD), symetrisee par W(B_m), du modele enracine C2 (notes/16).

Modele exact (orbit_sat.py) : graphe Q sur les racines de D_m, invariant par t = -1, avec
  (R) sum_w Q_uw = 2m-2 ;  (I) #{w contenant c, w ~ u} = 1 si c ou -c dans u, 2 sinon ;
  (P) sum_w Q_uw Q_wv + Q_uv = 2 - |u n v| (u != v, v != -u) ;  sum_w Q_uw Q_(w,-u) = 2  (dont la contrainte D).
Variables binaires : orbites sous t des paires de racines {u, w} (w != u, -u).
Relaxation : moments y_e = E[x_e], Y_ef = E[x_e x_f] ; x_e^2 = x_e ; (R),(I) et leurs produits par chaque x_f ; (P) (lineaire en Y) ;
Sherali-Adams : 0 <= Y_ef <= y_e, Y_ef >= y_e + y_f - 1 ; matrice des moments [[1, y],[y, Y]] PSD.
Symetrisation (legitime) : si une solution existe, la moyenne sur ses reetiquetages par W(B_m) est une pseudo-distribution invariante
satisfaisant tout ; les moments ne dependent donc que des orbites de paires ; la PSD se reduit par la representation reguliere
de l'algebre commutante (de Klerk-Pasechnik-Schrijver) : X >= 0  <=>  sum_k x_k L_k >= 0, L_k[i,j] = p_kj^i sqrt(n_i/n_j).
Usage : python sos2_relax.py <m> [objectif : feas | ysib]
"""
import itertools, sys, time
import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

def build(m, verbose=True):
    t0 = time.time()
    HALF = [(i, s) for i in range(1, m + 1) for s in (1, -1)]
    ROOTS = [frozenset([h1, h2]) for h1, h2 in itertools.combinations(HALF, 2) if h1[0] != h2[0]]
    RIDX = {r: i for i, r in enumerate(ROOTS)}
    neg = lambda r: frozenset((i, -s) for i, s in r)
    VAR = {}          # frozenset({u,w}) -> index de variable (1..n), 0 = constante
    VLIST = [None]
    for u, w in itertools.combinations(ROOTS, 2):
        if w == neg(u):
            continue
        k1, k2 = frozenset([u, w]), frozenset([neg(u), neg(w)])
        if k1 in VAR:
            continue
        VLIST.append((u, w)); VAR[k1] = VAR[k2] = len(VLIST) - 1
    N = len(VLIST)
    var = lambda u, w: VAR[frozenset([u, w])]
    # generateurs de W(B_m) agissant sur les demi-etiquettes
    def gen_flip(h): return (h[0], -h[1]) if h[0] == 1 else h
    def gen_swap(h): return ({1: 2, 2: 1}.get(h[0], h[0]), h[1])
    def gen_cyc(h):  return (h[0] % m + 1, h[1])
    gens = [gen_flip, gen_swap, gen_cyc]
    def vperm(g):
        P = np.zeros(N, dtype=np.int64)
        for k in range(1, N):
            u, w = VLIST[k]
            gu = frozenset(g(h) for h in u); gw = frozenset(g(h) for h in w)
            P[k] = var(gu, gw)
        return P
    Ps = [vperm(g) for g in gens]
    # orbites des paires ordonnees (a, b) de {0..N-1}
    idx = np.arange(N * N, dtype=np.int64)
    a, b = idx // N, idx % N
    rows, cols = [], []
    for P in Ps:
        rows.append(idx); cols.append(P[a] * N + P[b])
    G = sp.csr_matrix((np.ones(3 * N * N, dtype=np.int8), (np.concatenate(rows), np.concatenate(cols))), shape=(N * N, N * N))
    d, lab = connected_components(G, directed=True, connection="weak")
    orb = lab.reshape(N, N)
    del G, rows, cols, idx, a, b
    nsize = np.bincount(lab, minlength=d).astype(float)
    reps = np.zeros((d, 2), dtype=np.int64)
    flat = np.argsort(lab, kind="stable")
    first = np.searchsorted(lab[flat], np.arange(d))
    reps[:, 0] = flat[first] // N; reps[:, 1] = flat[first] % N
    transp = orb[reps[:, 1], reps[:, 0]]
    if verbose:
        print("m=%d : racines %d, variables %d, orbites de paires (avec la constante) %d  [%.1f s]" % (m, len(ROOTS), N - 1, d, time.time() - t0), flush=True)
    # constantes de structure p[k, j, i] = #{c : orb(a_i,c) = k, orb(c,b_i) = j}
    p = np.zeros((d, d, d), dtype=np.float64)
    for i in range(d):
        ks = orb[reps[i, 0], :]; js = orb[:, reps[i, 1]]
        np.add.at(p, (ks, js, np.full(N, i)), 1.0)
    L = np.zeros((d, d, d))
    ratio = np.sqrt(nsize[:, None] / nsize[None, :])          # [i, j]
    for k in range(d):
        L[k] = p[k].T * ratio                                    # L_k[i,j] = p[k, j, i] sqrt(n_i/n_j)
    # contraintes lineaires sur le vecteur x (moments par orbite)
    eqs = {}
    def add(row, rhs):
        key = (tuple(sorted((k, round(v, 12)) for k, v in row.items() if abs(v) > 1e-12)), round(rhs, 12))
        eqs[key] = (row, rhs)
    c0 = orb[0, 0]
    add({c0: 1.0}, 1.0)
    for k in range(1, N):                                         # x_e^2 = x_e
        add({orb[k, k]: 1.0, orb[0, k]: -1.0}, 0.0)
    for k in range(d):                                            # symetrie Y_ef = Y_fe
        if transp[k] != k:
            add({k: 1.0, transp[k]: -1.0}, 0.0)
    u0 = ROOTS[0]
    lin = []                                                      # (support, constante)
    others = [w for w in ROOTS if w != u0 and w != neg(u0)]
    lin.append(([var(u0, w) for w in others], 2 * m - 2.0))                     # (R)
    for c in HALF:                                                               # (I)
        sup = [var(u0, w) for w in others if c in w]
        rhs = 1.0 if (c in u0 or (c[0], -c[1]) in u0) else 2.0
        lin.append((sup, rhs))
    for sup, rhs in lin:                                          # L et x_f * L pour tout f
        for f in range(N):
            row = {}
            for e in sup:
                k = orb[f, e]; row[k] = row.get(k, 0.0) + 1.0
            k0 = orb[f, 0]; row[k0] = row.get(k0, 0.0) - rhs
            add(row, 0.0)
    for v in ROOTS:                                               # (P) et D
        if v == u0:
            continue
        row = {}
        if v == neg(u0):
            for w in ROOTS:
                if w in (u0, neg(u0)):
                    continue
                k = orb[var(u0, w), var(w, neg(u0))]; row[k] = row.get(k, 0.0) + 1.0
            add(row, 2.0)
        else:
            for w in ROOTS:
                if w in (u0, v, neg(u0), neg(v)):
                    continue
                k = orb[var(u0, w), var(w, v)]; row[k] = row.get(k, 0.0) + 1.0
            k0 = orb[0, var(u0, v)]; row[k0] = row.get(k0, 0.0) + 1.0
            add(row, 2.0 - len(u0 & v))
    info = dict(m=m, N=N, d=d, orb=orb, reps=reps, nsize=nsize, transp=transp, VLIST=VLIST, ROOTS=ROOTS, var=var, neg=neg)
    if verbose:
        print("   equations lineaires distinctes : %d  [%.1f s]" % (len(eqs), time.time() - t0), flush=True)
    return L, list(eqs.values()), info

def solve(m, objective="feas", solver="CLARABEL"):
    import cvxpy as cp
    L, eqs, info = build(m)
    d, orb, N = info["d"], info["orb"], info["N"]
    x = cp.Variable(d)
    cons = []
    A = np.zeros((len(eqs), d)); rhs = np.zeros(len(eqs))
    for r, (row, c) in enumerate(eqs):
        for k, v in row.items():
            A[r, k] += v
        rhs[r] = c
    cons.append(A @ x == rhs)
    # Sherali-Adams niveau 1 : pour chaque orbite (e,f), e,f >= 1
    reps = info["reps"]
    for k in range(d):
        e, f = reps[k]
        if e >= 1 and f >= 1 and e != f:
            ke, kf = orb[0, e], orb[0, f]
            cons += [x[k] >= 0, x[k] <= x[ke], x[k] <= x[kf], x[k] >= x[ke] + x[kf] - 1]
    cons += [x >= -1e-9]
    Lx = sum(x[k] * L[k] for k in range(d))
    cons.append((Lx + Lx.T) / 2 >> 0)
    # moment d'ordre 1 des paires soeurs (meme support, une etiquette commune)
    ROOTS, var, neg = info["ROOTS"], info["var"], info["neg"]
    u0 = ROOTS[0]
    sis = [w for w in ROOTS if w != u0 and w != neg(u0) and {i for i, _ in w} == {i for i, _ in u0}]
    ksis = orb[0, var(u0, sis[0])]
    if objective == "feas":
        prob = cp.Problem(cp.Minimize(0), cons)
    elif objective == "ysib_min":
        prob = cp.Problem(cp.Minimize(x[ksis]), cons)
    else:
        prob = cp.Problem(cp.Maximize(x[ksis]), cons)
    t0 = time.time()
    prob.solve(solver=solver, verbose=False)
    print("   %s : statut %s, valeur %s, y_soeur = %s  [%.1f s]" % (objective, prob.status, prob.value,
          None if x.value is None else round(float(x.value[ksis]), 6), time.time() - t0), flush=True)
    return prob, x, info

if __name__ == "__main__":
    try:
        import ctypes; kk = ctypes.windll.kernel32
        kk.GetCurrentProcess.restype = ctypes.c_void_p; kk.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        kk.SetPriorityClass(kk.GetCurrentProcess(), 0x40)
    except Exception:
        pass
    m = int(sys.argv[1]); obj = sys.argv[2] if len(sys.argv) > 2 else "feas"
    for o in (["feas", "ysib_min", "ysib_max"] if obj == "all" else [obj]):
        solve(m, o)
