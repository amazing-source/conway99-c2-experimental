"""LP stage for mix_filter3 outputs (note 35): each record is a NON-A PART (orbits of pivots != A) plus the label of the
degree-6 block A (or None).  A's D-structure is variable (lambda, gen_colmodel_lam); exact certificate over all columns.
Usage: python mix_Agroup3.py <glob of mix3 json files> <k> <K> <seconds per LP> <out tag>"""
import sys, json, time, glob
from collections import defaultdict
sys.path.insert(0, "scripts")
import gen_colmodel_lam as G, mix_filter as MF
P = G.P
pat, k, K, tl, tag = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
recs = {}; twE = None
for f in sorted(glob.glob(pat)):
    d = json.load(open(f)); twE = [tuple(e) for e in d["twE"]]
    for key, info in d["classes"]:
        recs.setdefault(tuple(map(tuple, key)), info)
auts = MF.automorphisms(twE)
keys = sorted({MF.canon_skel(list(kk), auts): kk for kk in recs}.values(), key=str)   # dedupe across workers
out = open("logs/mix3_lp_%s_%d.jsonl" % (tag, k), "w")
for gi, key in enumerate(keys):
    if gi % K != k: continue
    info = recs[key]; a = info["A"]; orbs = [tuple(z) for z in key]
    t0 = time.time()
    trip = defaultdict(list)
    for (i, j, kk) in orbs: trip[P(i, j)].append((i, kk))
    orient = {}
    for R, lst in trip.items():
        pivs = {i for i, _ in lst}
        orient[R] = 'tw' if len(pivs) == 2 else pivs.pop()
    allowed = {}
    for R, lst in trip.items():
        for s_ in (0, 1): allowed[(R, s_)] = set(lst)
    if a is not None:
        for x in range(7):
            if x == a: continue
            R = P(a, x); orient[R] = a
            for s_ in (0, 1): allowed[(R, s_)] = {(a, y) for y in range(7) if y not in R}
    assert len(orient) == 21, (len(orient), orient)
    g = G.GenModel(orient, useP2=True, cut5=False, allowed_ik=allowed)
    obj, y = g.solve_cg(tlimit=tl, verbose=False)
    rec = {"idx": gi, "A": a, "slack": obj, "done": g.done}
    if g.done and obj > 1e-6:
        ok, bnd = g.verify(y); rec["cert"] = ok; rec["bounds"] = bnd
        rec["y"] = [[str(g.rname[r]), round(float(v), 9)] for r, v in enumerate(y) if abs(v) > 1e-10]
    else: rec["cert"] = None
    rec["secs"] = round(time.time() - t0, 1); rec["orbits"] = orbs; rec["twE"] = twE
    out.write(json.dumps(rec) + "\n"); out.flush()
    print(gi, "A", a, "slack %.3f" % obj, "cert", rec["cert"], rec["secs"], "s"); sys.stdout.flush()
print("worker", k, "done: groups", len([1 for gi in range(len(keys)) if gi % K == k]))
