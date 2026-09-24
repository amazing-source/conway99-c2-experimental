"""Invariants de Brown des formes tordues b_f(y,y') = b(y, f(A,P) y') — generalisation du mecanisme C3 a p = 2.

Pour f = f0(A) + f1(A) P  (f_e = c0 + c1 A + c2 A^2), admissible si f = I (type I) ou f = P (type P) modulo 2 hors diagonale :
  (comb)  beta(q_f) calcule a partir de la seule diagonale de f (type I : somme des beta(f_uu) ; type P : beta(f_xx) + 4 #{orbites f_vv = 2 mod 4})
  (eig)   beta(q_f) = beta(n f(k,+)) + somme_{theta,eps} f(theta,eps) * t^eps_theta   (mod 8)
          ou t^eps_theta = oddite du reseau (N_theta^eps, b/2)  [formule des blocs de rang 1 sur Z_2[C_2] : a t+ + a' t-].
Validation : controles reels (t calcules directement). Puis Conway-99 : t donnes par la formule de l'oddite en fonction de rho+ et rho- (mod 2).
"""
import sys, os, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "vendor"))
from milgram_check import integer_kernel, gram, paley49, rook7, triangular7  # noqa
from involution_frame import paley9  # noqa


def beta1(c):
    """invariant de Brown de <c>, c impair : +1 si c = 1 mod 4, -1 sinon."""
    return 1 if c % 4 == 1 else 7


def oddity2(G, K=20):
    """(oddite mod 8, impair?) d'une Gram entiere 2-unimodulaire (det impair), par diagonalisation 2-adique mod 2^K."""
    P = 2 ** K
    n = len(G)
    M = [[x % P for x in row] for row in G]
    alive = list(range(n)); odd = 0; is_odd = False
    def elim(rows_piv):
        # elimine les autres lignes/colonnes vivantes contre le bloc rows_piv (inversible mod 2)
        k = len(rows_piv)
        B = [[M[a][b] for b in rows_piv] for a in rows_piv]
        if k == 1:
            Binv = [[pow(B[0][0], -1, P)]]
        else:
            det = (B[0][0] * B[1][1] - B[0][1] * B[1][0]) % P
            di = pow(det, -1, P)
            Binv = [[B[1][1] * di % P, -B[0][1] * di % P], [-B[1][0] * di % P, B[0][0] * di % P]]
        for c in alive:
            if c in rows_piv: continue
            row = [M[c][a] for a in rows_piv]
            if all(v % P == 0 for v in row): continue
            coef = [sum(row[t] * Binv[t][s] for t in range(k)) % P for s in range(k)]
            for tcol in range(n):
                M[c][tcol] = (M[c][tcol] - sum(coef[s] * M[rows_piv[s]][tcol] for s in range(k))) % P
            for trow in range(n):
                M[trow][c] = (M[trow][c] - sum(coef[s] * M[trow][rows_piv[s]] for s in range(k))) % P
    while alive:
        i = next((a for a in alive if M[a][a] % 2 == 1), None)
        if i is not None:
            odd += M[i][i]; is_odd = True
            elim([i]); alive.remove(i)
            continue
        pair = next(((a, b) for a in alive for b in alive if a < b and M[a][b] % 2 == 1), None)
        if pair is None:
            raise ValueError("pas 2-unimodulaire")
        elim(list(pair)); alive.remove(pair[0]); alive.remove(pair[1])
    return (odd % 8 if is_odd else 0), is_odd


def admissible_fs():
    out = []
    for c0, c1, c2, d0, d1, d2 in itertools.product(range(8), repeat=6):
        if (c1 + c2) % 2 or (d1 + d2) % 2: continue
        if (c0 % 2, d0 % 2) == (1, 0): typ = "I"
        elif (c0 % 2, d0 % 2) == (0, 1): typ = "P"
        else: continue
        out.append((typ, c0, c1, c2, d0, d1, d2))
    return out


def fval(co, th, eps):
    typ, c0, c1, c2, d0, d1, d2 = co
    return (c0 + c1 * th + c2 * th * th) + eps * (d0 + d1 * th + d2 * th * th)


def beta_comb(co, k, lam, mu, nfix, nadj, nfar):
    """nfix points fixes (ici 1), nadj sommets u ~ sigma u, nfar sommets u !~ sigma u (u != sigma u)."""
    typ, c0, c1, c2, d0, d1, d2 = co
    base = c0 + c2 * k
    f_fix = base + d0 + d2 * k
    f_adj = base + d1 + d2 * lam
    f_far = base + d2 * mu
    if typ == "I":
        return (nfix * beta1(f_fix) + nadj * beta1(f_adj) + nfar * beta1(f_far)) % 8
    # type P : orbites de taille 2 ; bloc E si f_vv = 2 mod 4
    assert nfix == 1
    nE = (nadj // 2) * (1 if f_adj % 4 == 2 else 0) + (nfar // 2) * (1 if f_far % 4 == 2 else 0)
    return (beta1(f_fix) + 4 * nE) % 8


def beta_eig(co, n, k, r, s, t):
    tot = beta1(n * fval(co, k, 1))
    for th in (r, s):
        for eps in (1, -1):
            tot += fval(co, th, eps) * t[(th, eps)]
    return tot % 8


def control(name, A, sig):
    n = A.shape[0]; k = int(A[0].sum())
    ev = sorted({int(round(x)) for x in np.linalg.eigvalsh(A.astype(float))}, reverse=True)
    r, s = ev[1], ev[2]
    lam = int(A[0] @ A[:, [j for j in range(n) if A[0, j]][0]]) if True else None
    # lambda, mu depuis A^2
    A2 = A @ A
    lam = int(next(A2[i, j] for i in range(n) for j in range(n) if A[i, j]))
    mu = int(next(A2[i, j] for i in range(n) for j in range(n) if i != j and not A[i, j]))
    P = np.zeros((n, n), dtype=np.int64)
    for i, j in enumerate(sig): P[j, i] = 1
    nfix = sum(1 for i in range(n) if sig[i] == i)
    nadj = sum(1 for i in range(n) if sig[i] != i and A[i, sig[i]])
    nfar = n - nfix - nadj
    I = np.eye(n, dtype=np.int64)
    t = {}
    for th in (r, s):
        for eps in (1, -1):
            B = integer_kernel(np.vstack([A - th * I, P - eps * I]).tolist())
            G = gram(B)
            assert all(x % 2 == 0 for row in G for x in row), "b/2 non entier"
            Gh = [[x // 2 for x in row] for row in G]
            t[(th, eps)] = oddity2(Gh)[0] if Gh else 0
    fs = admissible_fs()
    bad = sum(1 for co in fs if beta_comb(co, k, lam, mu, nfix, nadj, nfar) != beta_eig(co, n, k, r, s, t))
    print("%-18s n=%d k=%d lam=%d mu=%d r=%d s=%d fix=%d adj=%d  t=%s  -> %d/%d f en desaccord" % (
        name, n, k, lam, mu, r, s, nfix, nadj, {kk: v for kk, v in t.items()}, bad, len(fs)))
    return bad


def conway():
    n, k, lam, mu, r, s = 99, 14, 1, 2, 3, -4
    fs = admissible_fs()
    print("\nConway-99, C2 (1 point fixe, 14 sommets u ~ sigma u, 84 autres) ; %d f admissibles (coeffs mod 8)" % len(fs))
    res = {}
    for rp, rm in itertools.product((0, 1), repeat=2):
        for kp, km in itertools.product((0, 1), repeat=2):
            t = {(3, 1): (29 + 6 * rp + 4 * kp) % 8, (3, -1): (27 + 6 * rm + 4 * km) % 8,
                 (-4, 1): (22 + 10 * rp + 4 * kp) % 8, (-4, -1): (22 + 10 * rm + 4 * km) % 8}
            bad = [co for co in fs if beta_comb(co, k, lam, mu, 1, 14, 84) != beta_eig(co, n, k, r, s, t)]
            res[(rp, rm, kp, km)] = len(bad)
            ex = bad[0] if bad else None
            print("  rho+=%d rho-=%d k+=%d k-=%d (mod 2) : %6d f en desaccord%s" % (
                rp, rm, kp, km, len(bad), ("   ex. " + str(ex)) if ex else ""))
    return res


if __name__ == "__main__":
    A, pts = paley9(); neg = [pts.index(((-p[0]) % 3, (-p[1]) % 3)) for p in pts]
    control("Paley(9)", A, neg)
    A, sig = rook7(); control("L2(7)", A, sig)
    A, sig = paley49(); control("Paley(49)", A, sig)
    conway()
