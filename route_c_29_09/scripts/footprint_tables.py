"""Allowed full h-footprints (multisets of |(x,h_i)|) of a test vector x in U, from the star energy bound (Astra, proven):
||a||^2 + L(a) <= 7|x|^2 - Y(x), #odd entries even, Bessel ||a||^2 <= 4|x|^2."""
from itertools import combinations_with_replacement as cwr
from astra_root_star_filters import star_energy_lower_bound as SLB
def allowed(n):                      # n = |x|^2 ; returns {profile(sorted desc, nonzero): max Y}
    out = {}
    for a in cwr(range(0, 5), 7):
        if sum(v * v for v in a) > 4 * n or sum(v & 1 for v in a) % 2: continue
        ymax = 7 * n - SLB(a)
        if ymax >= 0: out[tuple(sorted((v for v in a if v), reverse=True))] = ymax
    return out
def forbid_table(n, Y):              # F[r1][r2] True if no allowed profile with budget Y contains entries r1,r2 (r=0: singleton r2)
    prof = [p for p, ym in allowed(n).items() if ym >= Y]
    F = [[True] * 5 for _ in range(5)]
    for p in prof:
        for i in range(len(p)):
            F[0][p[i]] = F[p[i]][0] = False
            for j in range(len(p)):
                if i != j: F[p[i]][p[j]] = False
    F[0][0] = False
    return F
if __name__ == "__main__":
    for n in (2, 3, 4):
        t = allowed(n); print("norm", n, sorted(t.items(), key=lambda kv: -kv[1]))
