"""Transfert du mecanisme C3 (comparaison des specialisations) a C2 : verification sur graphes reels.

Pour un srg d'ordre n impair, de valeurs propres k, r, s, et un automorphisme sigma (involution) :
  N_th      = Z^n ∩ V_th                      (reseau propre, forme standard b)
  N_th^+/-  = N_th ∩ V^+ / V^-                 (parties invariante / anti-invariante)
Predictions testees :
  P1  N_th (th != k) est PAIR (vecteurs orthogonaux a 1).
  P2  si E_th est 2-entier : det N_th impair et, si f = rang pair, det N_th = (-1)^(f/2) mod 4
      (reseau pair 2-unimodulaire de rang 2m : det = (-1)^m mod 4).
  P3  si E_th est 2-entier et E_th Z_2^n libre sur Z_2[C2] : (N_th^±, b/2) entier a det impair.
  P4  formule de l'oddite pour N_th (pair, 2-unimodulaire) : f + somme_p p-exces = 0 mod 8.
  P5  si p | r-s, p ne divise pas n, p ne divise pas (k-r) : rang_p(A - rI) = 1 + dim D_p(N_r).
"""
import sys, os, itertools
from fractions import Fraction
import numpy as np
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
sys.path.insert(0, HERE)
from involution_frame import paley9  # noqa
from padic import rank_mod_p  # noqa


# ---------- graphes ----------
def paley49():
    # F_49 = F_7(i), i^2 = -1 (7 = 3 mod 4)
    els = [(a, b) for a in range(7) for b in range(7)]
    mul = lambda x, y: ((x[0]*y[0] - x[1]*y[1]) % 7, (x[0]*y[1] + x[1]*y[0]) % 7)
    sq = {mul(x, x) for x in els if x != (0, 0)}
    idx = {e: i for i, e in enumerate(els)}
    A = np.zeros((49, 49), dtype=np.int64)
    for x in els:
        for y in els:
            d = ((x[0]-y[0]) % 7, (x[1]-y[1]) % 7)
            if d in sq: A[idx[x], idx[y]] = 1
    neg = [idx[((-e[0]) % 7, (-e[1]) % 7)] for e in els]
    return A, neg


def rook7():
    V = [(i, j) for i in range(7) for j in range(7)]
    idx = {v: t for t, v in enumerate(V)}
    A = np.zeros((49, 49), dtype=np.int64)
    for (i, j) in V:
        for (k, l) in V:
            if (i == k) != (j == l): A[idx[(i, j)], idx[(k, l)]] = 1
    pi = [1, 0, 3, 2, 5, 4, 6]
    sig = [idx[(pi[i], pi[j])] for (i, j) in V]
    return A, sig


def triangular7():
    V = list(itertools.combinations(range(7), 2))
    idx = {v: t for t, v in enumerate(V)}
    A = np.zeros((21, 21), dtype=np.int64)
    for a in V:
        for b in V:
            if a != b and set(a) & set(b): A[idx[a], idx[b]] = 1
    pi = [1, 0, 3, 2, 5, 4, 6]
    sig = [idx[tuple(sorted((pi[a[0]], pi[a[1]])))] for a in V]
    return A, sig


# ---------- algebre entiere ----------
def integer_kernel(M):
    """Z-base (colonnes) de {x in Z^n : M x = 0}, par operations de colonnes unimodulaires sur [M; I]."""
    M = [[int(v) for v in row] for row in M]
    m, n = len(M), len(M[0])
    cols = [[M[i][j] for i in range(m)] + [int(k == j) for k in range(n)] for j in range(n)]
    piv = 0
    for i in range(m):
        while True:
            nz = [j for j in range(piv, n) if cols[j][i] != 0]
            if not nz: break
            jm = min(nz, key=lambda j: abs(cols[j][i]))
            cols[piv], cols[jm] = cols[jm], cols[piv]
            clean = True
            for j in range(piv + 1, n):
                if cols[j][i]:
                    q = cols[j][i] // cols[piv][i]
                    cols[j] = [a - q * b for a, b in zip(cols[j], cols[piv])]
                    if cols[j][i]: clean = False
            if clean: break
        if piv < n and cols[piv][i] != 0:
            piv += 1
    return [c[m:] for c in cols[piv:]]          # liste de vecteurs


def lll_reduce(B):
    """Petite reduction de taille (pas LLL complet) pour garder des entrees moderees."""
    return B


def gram(B):
    return [[sum(a * b for a, b in zip(u, v)) for v in B] for u in B]


def det_bareiss(G):
    M = [row[:] for row in G]; n = len(M); sign = 1; prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for r in range(k + 1, n):
                if M[r][k] != 0:
                    M[k], M[r] = M[r], M[k]; sign = -sign; break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def vp(x, p):
    if x == 0: return 10**9
    v = 0
    while x % p == 0: x //= p; v += 1
    return v


def jordan_odd(G, p, K):
    """Decomposition de Jordan p-adique (p impair) d'une Gram entiere non degeneree, calculs mod p^K.
    Renvoie liste (j, u mod p) : constituants 1x1 p^j * u."""
    P = p ** K
    M = [[x % P for x in row] for row in G]
    n = len(M); alive = list(range(n)); out = []
    def val(x):
        return vp(x % P, p) if x % P else 10**9
    while alive:
        best = None
        for a in alive:
            v = val(M[a][a])
            if best is None or v < best[0]: best = (v, a, a)
        for a in alive:
            for b in alive:
                if a < b:
                    v = val(M[a][b])
                    if v < best[0]: best = (v, a, b)
        v, a, b = best
        if v >= K: raise ValueError("precision insuffisante")
        if a != b:          # e_a <- e_a + e_b
            for t in range(n):
                M[a][t] = (M[a][t] + M[b][t]) % P
            for t in range(n):
                M[t][a] = (M[t][a] + M[t][b]) % P
        piv = M[a][a]
        vv = val(piv); unit = (piv // p ** vv) % P
        inv = pow(unit, -1, P)
        alive.remove(a)
        for c in alive:
            if M[c][a] % P:
                f = (M[c][a] // p ** vv) * inv % P      # M[c][a] a une valuation >= vv
                for t in range(n):
                    M[c][t] = (M[c][t] - f * M[a][t]) % P
                for t in range(n):
                    M[t][c] = (M[t][c] - f * M[t][a]) % P
        out.append((vv, unit % p))
    return out


def legendre(u, p):
    u %= p
    return 1 if pow(u, (p - 1) // 2, p) == 1 else -1


def p_excess(jd, p):
    """p-exces (Conway-Sloane) : somme sur constituants p^j de dim n_j : n_j(p^j - 1) + 4 k_j."""
    by = {}
    for j, u in jd:
        by.setdefault(j, []).append(u)
    tot = 0
    for j, us in by.items():
        nj = len(us); eps = 1
        for u in us: eps *= legendre(u, p)
        k = 1 if (j % 2 == 1 and eps == -1) else 0
        tot += nj * (p ** j - 1) + 4 * k
    return tot % 8, {j: (len(us), int(np.prod([legendre(u, p) for u in us]))) for j, us in by.items()}


def study(name, A, sig):
    n = A.shape[0]
    k = int(A[0].sum())
    ev = sorted({int(round(x)) for x in np.linalg.eigvalsh(A.astype(float))}, reverse=True)
    r, s = ev[1], ev[2]
    P = np.zeros((n, n), dtype=np.int64)
    for i, j in enumerate(sig): P[j, i] = 1
    fixed = sum(1 for i, j in enumerate(sig) if i == j)
    assert (P @ A == A @ P).all(), "sigma n'est pas un automorphisme"
    print("\n=== %s : n=%d k=%d r=%d s=%d ; sigma a %d point(s) fixe(s)" % (name, n, k, r, s, fixed))
    I = np.eye(n, dtype=np.int64)
    for th, other in ((r, s), (s, r)):
        den = (th - k) * (th - other)
        two_int = (den % 2 != 0) or all(((A - k * I) @ (A - other * I) % den == 0).ravel()) and False
        # E_th = (A-kI)(A-other I)/den ; 2-entier ssi (A-kI)(A-oI) divisible par la 2-partie de den
        num = (A - k * I) @ (A - other * I)
        d2 = 2 ** vp(abs(den), 2)
        two_int = bool((num % d2 == 0).all())
        B = integer_kernel((A - th * I).tolist())
        G = gram(B); f = len(G)
        dt = det_bareiss(G)
        even = all(G[i][i] % 2 == 0 for i in range(f))
        line = "  th=%3d f=%3d  E_th 2-entier=%s  pair=%s  det=%s" % (th, f, two_int, even, sp.factorint(dt))
        if two_int and f % 2 == 0:
            line += "  P2: det mod 4 = %d, attendu %d" % (dt % 4, (-1) ** (f // 2) % 4)
        print(line)
        # P4 : formule de l'oddite (si pair et det impair)
        if even and dt % 2 == 1:
            tot = f
            detail = []
            for p in sorted(sp.factorint(dt)):
                jd = jordan_odd(G, p, vp(dt, p) + 3)
                ex, info = p_excess(jd, p)
                tot += ex
                detail.append("p=%d exces=%d %s" % (p, ex, {j: v for j, v in info.items() if j > 0}))
            print("     P4: f + sum exces = %d mod 8 (attendu 0)   %s" % (tot % 8, "; ".join(detail)))
        # P5 : rang_p(A - th I) = 1 + dim D_p(N_th) pour p | (r-s), p ne divisant ni n ni (k-th)
        for p in sp.factorint(abs(r - s)):
            if n % p and (k - th) % p:
                rk = rank_mod_p((A - th * I) % p, p) if True else None
                dimD = vp(dt, p) if False else sum(1 for j, u in jordan_odd(G, p, vp(dt, p) + 3) if j > 0)
                print("     P5 (p=%d): rang_p(A-%dI) = %d ; 1 + dim D_p = %d" % (p, th, rk, 1 + dimD))
        # P3 : parties +/- (b/2)
        for eps, lab in ((1, "+"), (-1, "-")):
            Mst = np.vstack([A - th * I, P - eps * I])
            Bs = integer_kernel(Mst.tolist())
            Gs = gram(Bs); fs = len(Gs)
            if fs == 0:
                print("     N^%s : rang 0" % lab); continue
            evs = all(Gs[i][i] % 2 == 0 for i in range(fs)) and all(Gs[i][j] % 2 == 0 for i in range(fs) for j in range(fs))
            Gh = [[x // 2 for x in row] for row in Gs] if evs else None
            dts = det_bareiss(Gs)
            dth = det_bareiss(Gh) if Gh else None
            typ = None
            if Gh:
                typ = "pair" if all(Gh[i][i] % 2 == 0 for i in range(fs)) else "impair"
            print("     N^%s : rang %2d, b pair=%s, Gram divisible par 2=%s, det(b/2)=%s (type %s)" % (
                lab, fs, all(Gs[i][i] % 2 == 0 for i in range(fs)), evs,
                sp.factorint(dth) if dth else None, typ))


if __name__ == "__main__":
    A, pts = paley9()
    neg = [pts.index(((-p[0]) % 3, (-p[1]) % 3)) for p in pts]
    study("Paley(9) = H(2,3)", A, neg)
    A, sig = triangular7(); study("T(7)", A, sig)
    A, sig = rook7(); study("L2(7) = K7 x K7", A, sig)
    A, sig = paley49(); study("Paley(49)", A, sig)
