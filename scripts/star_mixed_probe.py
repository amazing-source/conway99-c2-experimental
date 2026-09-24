"""Etoile « mixte » (notes/19 §7) : deux paires soeurs {c,a},{c,b} + une arete D de type one de pivot c, dans star(c).
Question : le lemme des etoiles s'etend-il (d_c = # aretes D internes a star(c), soeurs ou one, >= 3 impossible ?).
RSF(lignes des 6 orbites concernees) avec sigma (au moins) = les deux paires soeurs, dpairs = l'arete D one.
Variantes : l'arete one sur deux paires {c,r1},{c,r2} hors {a,b} (orbites de meme parite ou non).
Usage : python star_mixed_probe.py <T>
"""
import sys, time
sys.path.insert(0, "scripts")
from rs_experiments import solve_full, idle
import row_system_full as R
if __name__ == "__main__":
    idle()
    T = float(sys.argv[1])
    o = R.orbit
    cases = {
        "soeurs 12,13 + D(14+)=15+": ([(1, 2), (1, 3)], [(o(1, 4, 0), o(1, 5, 0))]),
        "soeurs 12,13 + D(14+)=15-": ([(1, 2), (1, 3)], [(o(1, 4, 0), o(1, 5, 1))]),
        "soeur 12 + D(13+)=14+ + D(15+)=16+": ([(1, 2)], [(o(1, 3, 0), o(1, 4, 0)), (o(1, 5, 0), o(1, 6, 0))]),
        "D(12+)=13+ + D(14+)=15+ + D(16+)=17+": ([], [(o(1, 2, 0), o(1, 3, 0)), (o(1, 4, 0), o(1, 5, 0)), (o(1, 6, 0), o(1, 7, 0))]),
    }
    for name, (sig, dp) in cases.items():
        S = sorted(set([o(i, j, e) for (i, j) in sig for e in (0, 1)] + [u for d in dp for u in d]))
        t0 = time.time()
        r = solve_full(S, sigma=sig, dpairs=dp, T=T)
        print("%-40s |S|=%d : %-7s %.1f s" % (name, len(S), r[0], r[2]), flush=True)
