"""[+ automatic A-branching: a single leaf that stays feasible with A variable is resolved by recursive splitting of A's D-graphs
(by the partner multiset of one A-pair at a time), exactly as mix_resolve.py.]
Union LPs per orientation (note 35).  For a representative orientation with surviving non-A leaves S (own labelling):
LP with allowed triples = UNION over S (A's structure variable).  Infeasible (exact certificate) => every leaf of S dies (the union
LP relaxes each leaf's LP: more allowed columns).  Feasible => split S by the D-structure of the block where the leaves differ most,
recurse; a single leaf that stays feasible is reported.
Usage: python mix_union_lp.py <glob of mix6 json> <k> <K> <seconds per LP> <tag>"""
import sys, json, time, glob
from collections import defaultdict, Counter
sys.path.insert(0, "scripts")
import gen_colmodel_lam as G, mix_enum as ME
P = G.P
pat, k, K, tl, tag = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
jobs = []
for f in sorted(glob.glob(pat)):
    d = json.load(open(f))
    for po in d["per_orient"]:
        if po["leaves"]: jobs.append((po, [tuple(map(tuple, L)) for L in po["leaves"]], d["twE"]))
import os
outfn = "logs/mix6_ulp_%s_%d.jsonl" % (tag, k)
done_jobs = set()
if os.path.exists(outfn):
    for l in open(outfn):
        try: done_jobs.add(json.loads(l)["job"])
        except Exception: pass
out = open(outfn, "a")

def solve(po, leaves, Adgs=None):
    a = po["A"]; In = {int(x): v for x, v in po["In"].items()}
    orient = {}
    for c in range(7):
        for x in In[c]: orient[P(c, x)] = c
    for L in leaves:
        for (i, j, kk) in L:
            R = P(i, j)
            if R not in orient: orient[R] = 'tw'
    for R in G.PAIRS:
        if R not in orient: orient[R] = 'tw'
    allowed = defaultdict(set)
    for L in leaves:
        for (i, j, kk) in L:
            for s_ in (0, 1): allowed[(P(i, j), s_)].add((i, kk))
    if a is not None:
        trip = defaultdict(set)
        if Adgs is None:
            for x in range(7):
                if x != a: trip[x] = {y for y in range(7) if y not in (a, x)}
        else:
            for g in Adgs:
                for (x, y) in g: trip[x].add(y); trip[y].add(x)
        for x in range(7):
            if x == a: continue
            for s_ in (0, 1): allowed[(P(a, x), s_)] = {(a, y) for y in trip[x]}
    g = G.GenModel(orient, useP2=True, cut5=False, allowed_ik=dict(allowed))
    obj, y = g.solve_cg(tlimit=tl, verbose=False)
    if g.done and obj > 1e-6:
        ok, bnd = g.verify(y)
        return ('dead' if ok else 'certfail'), obj, bnd
    return ('feasible' if g.done else 'timeout'), obj, None

def recA(po, leaf, dgs, depth, log):
    t0 = time.time(); st, obj, bnd = solve(po, [leaf], dgs)
    log.append({"depth": depth, "nleaves": 1, "nA": len(dgs), "status": st, "slack": obj, "bounds": bnd, "secs": round(time.time() - t0, 1)})
    if st == 'dead': return []
    if len(dgs) == 1: return [(leaf, st + ' (A fixed)')]
    a = po["A"]
    for x in range(7):
        if x == a: continue
        sig = defaultdict(list)
        for g in dgs: sig[tuple(sorted(y for (u, y) in g if u == x) + sorted(u for (u, y) in g if y == x))].append(g)
        if len(sig) > 1: break
    res = []
    for part in sig.values(): res += recA(po, leaf, part, depth + 1, log)
    return res

def rec(po, leaves, depth, log):
    t0 = time.time(); st, obj, bnd = solve(po, leaves)
    log.append({"depth": depth, "nleaves": len(leaves), "status": st, "slack": obj, "bounds": bnd, "secs": round(time.time() - t0, 1)})
    if st == 'dead': return []
    if len(leaves) == 1:
        a = po["A"]
        if st == 'feasible' and a is not None:
            Adg = ME.dgraphs([x for x in range(7) if x != a], [])
            # first split level directly (the full-A LP was just solved)
            for x in range(7):
                if x == a: continue
                sig = defaultdict(list)
                for g in Adg: sig[tuple(sorted(y for (u, y) in g if u == x) + sorted(u for (u, y) in g if y == x))].append(g)
                if len(sig) > 1: break
            res = []
            for part in sig.values(): res += recA(po, leaves[0], part, depth + 1, log)
            return res
        return [(leaves[0], st)]
    # split by the pivot block whose triple sets vary most among the leaves
    best = None
    for c in range(7):
        sig = Counter(tuple(sorted(z for z in L if z[0] == c)) for L in leaves)
        if len(sig) > 1 and (best is None or len(sig) > best[1]): best = (c, len(sig))
    c = best[0]; groups = defaultdict(list)
    for L in leaves: groups[tuple(sorted(z for z in L if z[0] == c))].append(L)
    res = []
    for gl in groups.values(): res += rec(po, gl, depth + 1, log)
    return res

for ji, (po, leaves, twE) in enumerate(jobs):
    if ji % K != k or ji in done_jobs: continue
    t0 = time.time(); log = []
    bad = rec(po, leaves, 0, log)
    out.write(json.dumps({"job": ji, "twE": twE, "In": po["In"], "A": po["A"], "nleaves": len(leaves), "lps": len(log),
                          "unresolved": [[list(map(list, L)), st] for L, st in bad], "log": log, "secs": round(time.time() - t0, 1)}) + "\n"); out.flush()
    print(ji, "leaves", len(leaves), "LPs", len(log), "unresolved", len(bad), "%.0fs" % (time.time() - t0)); sys.stdout.flush()
print("worker", k, "done")
