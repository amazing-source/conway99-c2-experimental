"""Positivite des produits de Schur gradues par l'involution (Krein « a deux points » de la paire (Gamma, t)).
Pour les projecteurs E_th^a = E_th (I + aP)/2 : T(alpha,beta,gamma) = sum_{u,v} E_alpha[u,v] E_beta[u,v] E_gamma[u,v] >= 0
(produit de Schur de PSD = PSD). Chaque entree E^a[u,v] = (e(d(u,v)) + a e(d(u,tv)))/2 ne depend que de (d,d') = (d(u,v), d(u,tv)),
et N_{d,d'} = #{(u,v)} = sum_h n_h p^h_{d d'}, avec n_h = #{u : d(u,tu) = h}. Donc T est determine par les parametres et (n_0,n_1,n_2)."""
import itertools
from fractions import Fraction as F

def srg_data(n, k, lam, mu):
    import math
    D = (lam - mu) ** 2 + 4 * (k - mu); sq = int(round(math.isqrt(D)))
    assert sq * sq == D
    r = F(lam - mu + sq, 2); s = F(lam - mu - sq, 2)
    f = F(-k * (s + 1) * (k - s), (k + r * s) * (r - s)); g = n - 1 - f
    # intersection numbers p^h_{ij}, i,j,h in {0,1,2}
    l = n - k - 1
    p = {0: {(0, 0): 1, (1, 1): k, (2, 2): l},
         1: {(0, 1): 1, (1, 0): 1, (1, 1): lam, (1, 2): k - lam - 1, (2, 1): k - lam - 1, (2, 2): l - k + lam + 1},
         2: {(0, 2): 1, (2, 0): 1, (1, 1): mu, (1, 2): k - mu, (2, 1): k - mu, (2, 2): l - k + mu - 1}}
    # entries of primitive idempotents: E_th[u,v] as function of distance, via E = (m/n) * sum_d (P_d(th)/k_d) A_d
    def ent(th, m):
        kd = {0: 1, 1: k, 2: l}
        Pd = {0: F(1), 1: F(th), 2: F(-1 - th)}      # eigenvalue of A_2 = J - I - A on eigenvector th != k
        if th == k: Pd = {0: F(1), 1: F(k), 2: F(l)}
        return {d: F(m, n) * Pd[d] / kd[d] for d in (0, 1, 2)}
    return r, s, f, g, p, ent

def run(name, n, k, lam, mu, nh):
    r, s, f, g, p, ent = srg_data(n, k, lam, mu)
    N = {}
    for d in (0, 1, 2):
        for d2 in (0, 1, 2):
            N[d, d2] = sum(nh[h] * p[h].get((d, d2), 0) for h in (0, 1, 2))
    assert sum(N.values()) == n * n
    E = {"E0": (ent(k, 1), None), "E%s" % r: (ent(r, f), None), "E%s" % s: (ent(s, g), None)}
    idem = {"K": (ent(k, 1), 1)}
    for (lab, th, m) in (("r", r, f), ("s", s, g)):
        for a in (1, -1):
            idem["%s%s" % (lab, "+" if a == 1 else "-")] = (ent(th, m), a)
    def entry(key, d, d2):
        e, a = idem[key]
        if key == "K": return e[d]            # E_k P = E_k
        return (e[d] + a * e[d2]) / 2
    neg = []
    res = {}
    for trip in itertools.combinations_with_replacement(sorted(idem), 3):
        T = sum(N[d, d2] * entry(trip[0], d, d2) * entry(trip[1], d, d2) * entry(trip[2], d, d2) for (d, d2) in N)
        res[trip] = T
        if T < 0: neg.append((trip, T))
    print("%-22s n_h=%s : %d triplets, %d negatifs %s" % (name, nh, len(res), len(neg), [(t, float(v)) for t, v in neg][:6]))
    return res

run("Paley(9), t=-1", 9, 4, 1, 2, {0: 1, 1: 4, 2: 4})
run("BvLS, t=-1", 243, 22, 1, 2, {0: 1, 1: 22, 2: 220})
run("Conway-99, C2", 99, 14, 1, 2, {0: 1, 1: 14, 2: 84})
# autres types d'involution hypothetiques (tests de pouvoir discriminant)
for a1 in (0, 28, 42):
    run("Conway-99, a1=%d" % a1, 99, 14, 1, 2, {0: 1, 1: a1, 2: 98 - a1})
