"""Resolve a non-A part whose A-variable LP is feasible (note 35): branch on A's D-structure (recursive union over the set of
A's D-graphs, split by the partner of one A-pair at a time).  Every dead branch is certified exactly.
Usage: python mix_resolve.py <json file with {"In":..., "A":..., "orbits":[...]}> <seconds per LP>"""
import sys, json, time
from collections import defaultdict
sys.path.insert(0, "scripts")
import gen_colmodel_lam as G, mix_enum as ME
P = G.P
spec = json.load(open(sys.argv[1])); tl = float(sys.argv[2])
In = {int(x): v for x, v in spec["In"].items()}; a = spec["A"]; orbs = [tuple(z) for z in spec["orbits"]]
orient = {}
for c in range(7):
    for x in In[c]: orient[P(c, x)] = c
for (i, j, kk) in orbs:
    if P(i, j) not in orient: orient[P(i, j)] = 'tw'
for R in G.PAIRS:
    if R not in orient: orient[R] = 'tw'
base = defaultdict(set)
for (i, j, kk) in orbs:
    for s_ in (0, 1): base[(P(i, j), s_)].add((i, kk))
Adg = ME.dgraphs([x for x in range(7) if x != a], [])
log = []
def lp(dgs):
    allowed = dict(base)
    trip = defaultdict(set)
    for g in dgs:
        for (x, y) in g: trip[x].add(y); trip[y].add(x)
    for x in range(7):
        if x == a: continue
        for s_ in (0, 1): allowed[(P(a, x), s_)] = {(a, y) for y in trip[x]}
    gm = G.GenModel(orient, useP2=True, cut5=False, allowed_ik=allowed)
    obj, y = gm.solve_cg(tlimit=tl, verbose=False)
    if gm.done and obj > 1e-6:
        ok, bnd = gm.verify(y); return ('dead' if ok else 'certfail'), obj
    return ('feasible' if gm.done else 'timeout'), obj
def rec(dgs, depth):
    t0 = time.time(); st, obj = lp(dgs)
    log.append((depth, len(dgs), st, round(obj, 3), round(time.time() - t0, 1))); print(log[-1]); sys.stdout.flush()
    if st == 'dead': return []
    if len(dgs) == 1: return [(dgs[0], st)]
    # split by the partner multiset of the first A-pair whose partners vary
    for x in range(7):
        if x == a: continue
        sig = defaultdict(list)
        for g in dgs: sig[tuple(sorted(y for (u, y) in g if u == x) + sorted(u for (u, y) in g if y == x))].append(g)
        if len(sig) > 1: break
    res = []
    for part in sig.values(): res += rec(part, depth + 1)
    return res
t0 = time.time()
bad = rec(Adg, 0)
print("A structures:", len(Adg), "| LPs", len(log), "| unresolved A-structures:", len(bad), [b[1] for b in bad], "| %.0fs" % (time.time() - t0))
json.dump({"spec": spec, "log": log, "unresolved": [[list(map(list, g)), st] for g, st in bad]}, open(sys.argv[1].replace(".json", "_resolved.json"), "w"))
