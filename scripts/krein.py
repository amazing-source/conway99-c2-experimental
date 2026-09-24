"""Krein parameters and absolute bound for srg(n,k,1,2) with n = 2m^2+1, k = 2m (m = 2, 7, 11, 56, 497)."""
from fractions import Fraction as F
import math

def params(m):
    k = 2 * m; n = 2 * m * m + 1; lam, mu = 1, 2
    d = math.isqrt(4 * k - 7); r = (-1 + d) // 2; s = (-1 - d) // 2
    f = F((n - 1) * (-s) - k, r - s); g = F((n - 1) * r + k, r - s)
    return n, k, lam, mu, r, s, f, g

def krein(n, k, r, s, f, g):
    # standard formulas (Brouwer-Haemers, Spectra of Graphs, 9.1.5 / Seidel): q_11^1, q_22^2
    q111 = f * f / n * (F(1) + F(r ** 3, k ** 2) - F((r + 1) ** 3, (n - k - 1) ** 2))
    q222 = g * g / n * (F(1) + F(s ** 3, k ** 2) - F((s + 1) ** 3, (n - k - 1) ** 2))
    return q111, q222

for m in (2, 7, 11, 56, 497):
    n, k, lam, mu, r, s, f, g = params(m)
    q111, q222 = krein(n, k, r, s, F(f), F(g))
    print(f"m={m:4d} n={n:7d} k={k:4d} r={r} s={s} d={r-s} f={f} g={g}  q111={float(q111):.4f} q222={float(q222):.4f}  "
          f"abs bound f<= g(g+3)/2: {f <= g*(g+3)/2}, g<= f(f+3)/2: {g <= f*(f+3)/2}")
