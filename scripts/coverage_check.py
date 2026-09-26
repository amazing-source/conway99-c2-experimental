"""Coverage bookkeeping (note 41): for a twisted class, is every surviving leaf of every orientation job covered by a STORED certificate?
Certificates (logs/orbit_certs):
  gen_<cls>_<job>.json.gz / fc_<cls>_<job>_<node> / fix_<cls>_<job>_b<c>_o<t> : model 'gen' (orientation fixed), spec.forbid = forbidden
     (orbit, partner) choices.  A leaf is covered iff SOME orbit-level lift of its D-structures (labels inside anchored pairs are
     interchangeable: WLOG) uses no forbidden choice; A-block orbits are free in these models.
  leaf_<cls>_<job>_<t> : model 'var' (the leaf with A variable): covers leaf t exactly (triples compared).
Symmetry: leaves in the same orbit of the orientation's stabilizer as a covered leaf are covered.
This script only checks coverage; the validity of each certificate is checked by orbit_verify_certs.py.
Usage: python coverage_check.py <class id>"""
import sys, json, glob, gzip, itertools
from collections import defaultdict
sys.path.insert(0, "scripts")
import orbit_colmodel_gen as OG
ci = sys.argv[1]; N = 7
jobs = []
for f in sorted(glob.glob("logs/mix6_cls_%s_S_*.json" % ci)):
    d = json.load(open(f))
    for po in d["per_orient"]:
        if po["leaves"]: jobs.append(po)

def lifts_ok(g0, leaf, forbid, A):
    """is there a labelling of the leaf's D-structure avoiding all forbidden (Z, Dz)?  (block by block: independent)"""
    for c in range(N):
        if c == A: continue
        trip = [z for z in leaf if z[0] == c]
        if not trip: continue
        thirds = defaultdict(list)
        for (i, x, y) in trip: thirds[x].append(y)
        xs = sorted(thirds)
        orbs = {x: [o for o in g0.orbs_of[frozenset((c, x))] if g0.pivot[o] == c] for x in xs}
        found = False
        for perm in itertools.product(*[list(itertools.permutations(orbs[x])) for x in xs]):
            has = defaultdict(list)
            for x, pos in zip(xs, perm):
                for o, y in zip(pos, sorted(thirds[x])): has[(x, y)].append(o)
            edges = sorted({(min(x, y), max(x, y)) for (x, y) in has})
            choices = [[list(zip(has[(x, y)], pb)) for pb in itertools.permutations(has[(y, x)])] for (x, y) in edges]
            for pick in itertools.product(*choices):
                ok = all((Z, W) not in forbid and (W, Z) not in forbid for lst in pick for (Z, W) in lst)
                if ok: found = True; break
            if found: break
        if not found: return False
    return True

total = 0; covered_all = 0; report = []
for job, po in enumerate(jobs):
    In = {int(x): v for x, v in po["In"].items()}; A = po["A"]
    leaves = [tuple(sorted(tuple(z) for z in L)) for L in po["leaves"]]
    g0 = OG.OrbitModelGen(In)
    certs = []
    for fn in glob.glob("logs/orbit_certs/gen_%s_%d.json.gz" % (ci, job)) + glob.glob("logs/orbit_certs/fc_%s_%d_*.json.gz" % (ci, job)) + \
              glob.glob("logs/orbit_certs/fix_%s_%d_*.json.gz" % (ci, job)) + glob.glob("logs/orbit_certs/comb_%s_%d_*.json.gz" % (ci, job)):
        d = json.load(gzip.open(fn, "rt"))
        if {int(k): v for k, v in d["spec"]["In"].items()} != In: continue
        certs.append(("gen", {tuple(z) for z in d["spec"].get("forbid", [])}, fn))
    leafcert = set()
    for fn in glob.glob("logs/orbit_certs/leaf_%s_%d_*.json.gz" % (ci, job)):
        d = json.load(gzip.open(fn, "rt")); leafcert.add(tuple(sorted(tuple(z) for z in d["spec"]["leaf"])))
    In_ = {c: set(v) for c, v in In.items()}; arcs = {(c, x) for c, xs in In_.items() for x in xs}
    stab = [g for g in itertools.permutations(range(N)) if {(g[c], g[x]) for (c, x) in arcs} == arcs and (A is None or g[A] == A)]
    img = lambda L, g: tuple(sorted((g[i], g[j], g[k]) for (i, j, k) in L))
    cov = [False] * len(leaves)
    for t, L in enumerate(leaves):
        if L in leafcert: cov[t] = True; continue
        for kind, fb, fn in certs:
            if not fb or lifts_ok(g0, L, fb, A): cov[t] = True; break
    idx = {L: t for t, L in enumerate(leaves)}
    changed = True
    while changed:
        changed = False
        for t, L in enumerate(leaves):
            if cov[t]: continue
            if any(cov[idx[img(L, g)]] for g in stab if img(L, g) in idx): cov[t] = True; changed = True
    n = sum(cov); total += len(leaves)
    if n == len(leaves): covered_all += 1
    report.append((job, len(leaves), n, len(certs), len(leafcert)))
for r in report: print("job %d: leaves %d covered %d  (gen/fc/fix certs %d, leaf certs %d)%s" % (r + ("" if r[1] == r[2] else "  <-- INCOMPLETE",)))
print("class %s: %d/%d jobs fully covered by stored certificates" % (ci, covered_all, len(jobs)))
