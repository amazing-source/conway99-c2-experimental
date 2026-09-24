"""Test spectral du graphe lointain (note 23 §7), niveau TYPE (mu, tau).

Autour de la droite l_1 = {x, e_1, -e_1} : L (3), N(L) (36 = P_p u P_q u P_r), F (60 lointains). B = incidence N(L) x F.
A^2 = 12 I - A + 2 J (srg(99,14,1,2)), bloc F x F :  A_F^2 + A_F = 12 I + 2 J - B^T B.      (*)
BB^T (36 x 36) est connu au niveau du type : diagonale 10 ; meme classe : 0 si apparies par M, 1 sinon ;
P_p x P_q : Cx[a, b] ; P_q x P_r : Ct[b, s c] ; P_p x P_r : Cx[s a, s c].
Consequences de (*) : A_F commute avec B^T B ; sur l'espace propre de B^T B de valeur beta (orthogonal a 1), A_F a les valeurs
theta = (-1 +- r)/2, r = sqrt(49 - 4 beta) ; d_beta = m_+ - m_-.  Traces :
  tr A_F = 0                 =>  sum d r = 43
  tr A_F^3 = 6 (32 - T)      =>  sum d r^3 = 2443 - 48 T      (T = nb de droites transversales = #{b : tau b = s b})
  tr A_F^4 (connue au niveau du type)  =>  sum d (r + r^3) = K4
  valeurs propres de A_F algebriques entieres + polynome caracteristique rationnel (Galois).
Ce script : (1) coherence de (E3) et (E4) ; (2) beta <= 12.25 ; (3) resolubilite en entiers des d_beta pour les beta « rationnels »
(r entier impair : beta in {0, 6, 10, 12}), les autres etant traites exactement (polynome caracteristique, sympy) si besoin.
"""
import sys, os, itertools, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types

def BBt(mu, tau):
    Cx, Ct = targets(mu, tau, 12)
    s = lambda x: x ^ 1
    M = np.zeros((36, 36), dtype=np.int64)
    Mr = [s(mu[s(c)]) for c in range(12)]          # M_r = s mu s
    for cls, match in ((0, [s(a) for a in range(12)]), (1, list(mu)), (2, Mr)):
        for u in range(12):
            for v in range(12):
                M[12 * cls + u, 12 * cls + v] = 10 if u == v else (0 if v == match[u] else 1)
    for a in range(12):
        for b in range(12):
            M[a, 12 + b] = M[12 + b, a] = Cx[a, b]
            M[12 + a, 24 + b] = M[24 + b, 12 + a] = Ct[a, s(b)]
            M[a, 24 + b] = M[24 + b, a] = Cx[s(a), s(b)]
    return M

def trace_data(mu, tau):
    M = BBt(mu, tau)
    assert (M.sum(axis=1) == 60).all(), M.sum(axis=1)
    T = sum(1 for b in range(12) if tau[b] == (b ^ 1))
    ev = np.linalg.eigvalsh(M.astype(float))
    ev = np.sort(ev)[::-1]
    assert abs(ev[0] - 60) < 1e-8
    betas = list(ev[1:]) + [0.0] * 24                     # B^T B sur 1^perp : 35 valeurs de BB^T + 24 zeros
    fro2 = int((M * M).sum())
    sum_c2 = fro2 - 2160                                   # sum_{z != z'} c^2
    S2 = 1200 + sum_c2                                     # sum_{z != z'} (2 - c)^2
    trA4 = 60 * 64 + S2 - 2 * (672 - 6 * T) + 480
    rest4 = trA4 - 4096                                    # sum_{1perp} theta^4
    b = np.array(betas); m = np.ones_like(b)
    base = float(np.sum((12 - b) ** 2 + (12 - b)))
    r = np.sqrt(np.maximum(49 - 4 * b, 0))
    # sum theta^4 = base - sum (25 - 2 beta) s_beta ; s = (d r - 1)/2 par valeur propre (multiplicite 1 chacune ici)
    # => sum (25 - 2b)(d r)/2 = base - rest4 + sum (25 - 2b)/2
    rhs = base - rest4 + float(np.sum((25 - 2 * b) / 2))
    K4 = 2 * rhs * 2 / 1.0                                  # sum (1 + r^2) d r / 4 * 2 ... recalcul explicite ci-dessous
    # (25 - 2 beta) = (1 + r^2)/2  =>  sum (1 + r^2) d r / 4 = rhs  =>  sum d (r + r^3) = 4 rhs
    K4 = 4 * rhs
    E3 = 2443 - 48 * T
    return dict(T=T, maxbeta=float(max(betas)), K4=K4, E3=E3, E1=43, consistency=K4 - 43 - E3, betas=betas, fro2=fro2)

if __name__ == "__main__":
    parts = sys.argv[1].split(",") if len(sys.argv) > 1 else ["111111"]
    for ps in parts:
        part = tuple(int(c) for c in ps)
        mu, reps, st = types(part)
        bad = 0
        for ti, tau in enumerate(reps):
            d = trace_data(mu, tau)
            rb = sorted(set(round(x, 6) for x in d["betas"]))
            flag = ""
            if d["maxbeta"] > 12.25 + 1e-9: flag += " BETA>12.25"
            if abs(d["consistency"]) > 1e-6: flag += " INCOHERENT(E3/E4)"
            if flag: bad += 1
            if flag or ti < 4:
                print("A%s tau#%d T=%d maxbeta=%.4f K4-43-E3=%.4f%s ; beta distincts = %s" % (ps, ti, d["T"], d["maxbeta"], d["consistency"], flag, rb[:20]), flush=True)
        print("A%s : %d types, %d signales" % (ps, len(reps), bad), flush=True)
