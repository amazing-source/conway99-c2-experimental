"""Survivants de degre <= 2 : RSF(lignes soeurs + quelques lignes NON soeurs), Sigma EXACT sur les paires portant une orbite de S.
(notes/19 §9) Question : quelles lignes non soeurs faut-il ajouter pour tuer un survivant ?
Usage : python rsf_extend_probe.py <T> "<Sigma>" "<paires supplementaires dont on ajoute les 2 orbites>" [...]
"""
import sys, time
sys.path.insert(0, "scripts")
from rs_experiments import solve_full, idle, parse, sister_orbits
import row_system_full as R
if __name__ == "__main__":
    idle()
    T = float(sys.argv[1]); E = parse(sys.argv[2])
    for extra in sys.argv[3:]:
        X = parse(extra)
        S = sorted(set(sister_orbits(E) + [R.orbit(i, j, e) for (i, j) in X for e in (0, 1)]))
        r = solve_full(S, sigma=E, sigma_exact=True, T=T)
        print("Sigma=%s + lignes {%s} (|S|=%d, Sigma exact) : %-7s %.1f s" % (sys.argv[2], extra, len(S), r[0], r[2]), flush=True)
