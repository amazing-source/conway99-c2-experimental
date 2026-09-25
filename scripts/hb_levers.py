"""Which lever kills H-beta at pair level? (note 31)  For a skeleton and a free-cycle assignment, CP-SAT (8 workers, short limit) on:
  F1 = (L) + PPE diagonal ;  F2 = F1 + S + C (first order complete) ;  P2 = F2 + off-diagonal P2 (second order).
Also the hand budget B: #{Z : n_k(Z) = 1} + 2 N_near <= 42 (note 31 §2).  Only INFEASIBLE / FEASIBLE are counted as answers.
Usage: python hb_levers.py sym <orient> <order>          (symmetric cycles, circulant skeleton)
       python hb_levers.py rand <orient> <order> <count> <seed>   (independent random valid cycles at each block)"""
import sys, time, random
from collections import Counter
sys.path.insert(0, "scripts")
import hb_pairlevel as H, hb_p2_core as HC
N = H.N; P = H.P

def budget(orbits, nbs):
    nk1 = nd = 0
    for z in orbits:
        i, j, k = z
        prs = [P(w[0], w[1]) for w in nbs[j][z]]
        nk1 += prs.count(P(j, k)) == 1
        nd += prs[0] == prs[1]
    return nk1, nd, nk1 + 2 * nd

def levers(orbits, nbs, secs):
    m, groups = HC.model(orbits, nbs, None)
    g = set(groups)
    F1 = {x for x in g if x[0] == 'L' or (x[0] == 'P2' and x[1] == x[2])}
    F2 = {x for x in g if not (x[0] == 'P2' and x[1] != x[2])}
    out = {}
    for name, act in (("F1", F1), ("F2", F2), ("P2", g)):
        out[name] = HC.solve(orbits, nbs, act, secs)[0]
        if out[name] == "INFEASIBLE":
            for rest in ("F2", "P2"):
                if rest not in out: out[rest] = "INFEASIBLE"
            break
    return out

if __name__ == "__main__":
    mode, orient, order = sys.argv[1], sys.argv[2], int(sys.argv[3])
    In, orbits = H.skeleton(orient, order)
    t0 = time.time(); tally = Counter()
    if mode == "sym":
        cycs = H.free_cycles(orbits, 0, True)
        cases = [{s: {H.rot(z, s): [H.rot(w, s) for w in ws] for z, ws in nb0.items()} for s in range(N)} for nb0 in cycs]
    else:
        cnt, seed = int(sys.argv[4]), int(sys.argv[5]); rng = random.Random(seed)
        per = {j: H.free_cycles(orbits, j, True) for j in range(N)}
        cases = [{j: rng.choice(per[j]) for j in range(N)} for _ in range(cnt)]
        print("valid cycles per block:", {j: len(per[j]) for j in range(N)})
    for q, nbs in enumerate(cases):
        if time.time() - t0 > 270: print("TIME CAP"); break
        b = budget(orbits, nbs)
        r = levers(orbits, nbs, 8)
        tally[("B>42" if b[2] > 42 else "B ok", r["F1"], r["F2"], r["P2"])] += 1
        print(q, "nk1=%d near=%d B=%d" % b, r); sys.stdout.flush()
    print("tally (budget, F1, F2, P2):"); [print("  ", k, v) for k, v in sorted(tally.items())]
    print("time %.0fs" % (time.time() - t0))
