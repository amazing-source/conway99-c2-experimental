"""Mixtures / M1-A (note 35): one LP per 'non-A part' -- every orbit whose pivot is not the degree-6 block A has its triple fixed,
while A's D-structure is VARIABLE (lambda over all its D-graphs, gen_colmodel_lam).  An infeasible LP (exact certificate over all
columns) kills every skeleton with this non-A part, whatever A's structure.
Usage: python mix_Agroup.py <classes json> <k> <K> <seconds per LP>   -> logs/<name>_Agroup_<k>.jsonl"""
import sys, json, time, os
from collections import defaultdict
sys.path.insert(0, "scripts")
import gen_colmodel_lam as G
P = G.P
src, k, K, tl = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
d = json.load(open(src)); classes = d["classes"] if isinstance(d, dict) else [[c[0], c[2]] for c in d]
groups = {}
for key, In in classes:
    orbs = [tuple(z) for z in key]
    piv = defaultdict(int)
    for z in orbs: piv[z[0]] += 1
    A = [c for c in range(7) if piv[c] == 12]
    a = A[0] if A else None
    rest = tuple(sorted(z for z in orbs if z[0] != a))
    groups.setdefault((a, rest), orbs)
out = open("logs/%s_Agroup_%d.jsonl" % (os.path.basename(src).replace(".json", ""), k), "w")
for gi, ((a, rest), orbs) in enumerate(sorted(groups.items(), key=str)):
    if gi % K != k: continue
    t0 = time.time()
    trip = defaultdict(list)
    for (i, j, kk) in orbs: trip[P(i, j)].append((i, kk))
    orient = {}
    for R, lst in trip.items():
        pivs = {i for i, _ in lst}
        orient[R] = 'tw' if len(pivs) == 2 else pivs.pop()
    allowed = {}
    for R, lst in trip.items():
        for s_ in (0, 1):
            if a is not None and a in R and orient[R] == a:
                allowed[(R, s_)] = {(a, x) for x in range(7) if x not in R}
            else:
                allowed[(R, s_)] = set(lst)
    g = G.GenModel(orient, useP2=True, cut5=False, allowed_ik=allowed)
    obj, y = g.solve_cg(tlimit=tl, verbose=False)
    rec = {"group": gi, "A": a, "slack": obj, "done": g.done, "secs": None}
    if g.done and obj > 1e-6:
        ok, info = g.verify(y); rec["cert"] = ok; rec["bounds"] = info
    else: rec["cert"] = None
    rec["secs"] = round(time.time() - t0, 1); rec["orbits"] = orbs
    out.write(json.dumps(rec) + "\n"); out.flush()
    print(gi, "A", a, "slack %.3f" % obj, "cert", rec["cert"], rec["secs"], "s"); sys.stdout.flush()
