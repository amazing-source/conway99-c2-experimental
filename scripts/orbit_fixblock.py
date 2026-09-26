"""Orientation-level orbit LP with the D-structure FIXED at one block c (all other blocks variable) -- note 40.
Tests whether fixing a single high-option block suffices to kill (instead of one LP per leaf).
Labels: for an anchored pair at c, orbit 0 takes the smaller third, orbit 1 the larger (WLOG: the two orbits of an anchored pair
are interchangeable in the model).  Usage: python orbit_fixblock.py <class id> <job> <block c> [option indices]"""
import sys, json, glob, time, os
from collections import Counter, defaultdict
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_gen as OG
ci, job, c = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
jobs = []
for f in sorted(glob.glob("logs/mix6_cls_%s_S_*.json" % ci)):
    d = json.load(open(f))
    for po in d["per_orient"]:
        if po["leaves"]: jobs.append(po)
po = jobs[job]; In = {int(x): v for x, v in po["In"].items()}
opts = sorted(Counter(tuple(sorted(tuple(z) for z in L if z[0] == c)) for L in po["leaves"]).items(), key=lambda t: -t[1])
print("class %s job %d block %d: %d leaves, %d D-options at block %d" % (ci, job, c, len(po["leaves"]), len(opts), c)); sys.stdout.flush()
g0 = OG.OrbitModelGen(In)                       # labelling only
sel = [int(a) for a in sys.argv[4:]] or list(range(len(opts)))
for t in sel:
    trip, mult = opts[t]
    thirds = defaultdict(list)
    for (i, x, y) in trip: thirds[x].append(y)
    lab = {}                                     # (x, third) -> orbit label
    for x, ys in thirds.items():
        R = frozenset((c, x)); os_ = [o for o in g0.orbs_of[R] if g0.pivot[o] == c]
        for o, y in zip(os_, sorted(ys)): lab[(x, y)] = o
    forbid = set()
    for (x, y), Z in lab.items():
        W = lab[(y, x)]
        i_, j_, _ = g0.T[Z]
        for k in range(7):
            if k in (i_, j_): continue
            for Dz in g0.orbs_of[frozenset((c, k))]:
                if g0.pivot[Dz] == c and Dz != W: forbid.add((Z, Dz))
    t0 = time.time(); g = OG.OrbitModelGen(In, forbid=forbid)
    obj, y = g.solve(tlimit=float(os.environ.get('TL', 3000)), verbose=False)
    if g.done and obj > 1e-6:
        ok, b = g.verify(y); st = "INFEASIBLE" if ok else "CERTFAIL"
        if ok: OM.save_cert(g, y, "logs/orbit_certs/fix_%s_%d_b%d_o%d.json.gz" % (ci, job, c, t), "gen", {"In": po["In"], "forbid": sorted(map(list, forbid))}, b)
    else: st = "FEASIBLE" if g.done else "TIMECAP"
    print("option %d (%d leaves): %s slack %.4f %.0fs" % (t, mult, st, obj, time.time() - t0)); sys.stdout.flush()
