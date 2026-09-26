"""AD configurations with exactly two doubly-disjoint pairs {0,1}, {2,3} (their four orbits pair crosswise), all other pairs
anchored: orientation classes allowed by the proved degree lemmas (39.4 / 26.2), up to the stabilizer of the dd structure.
Writes logs/ad2_reps.json (list of heads dicts).  No LP."""
import itertools, json
N = 7
DD = [(0, 1), (2, 3)]
PAIRS = [(a, b) for a in range(N) for b in range(a + 1, N) if (a, b) not in DD]
dis = {k: sum(1 for p in DD if k in p) for k in range(N)}
def ok(heads):
    d = {k: 0 for k in range(N)}; out = {k: 0 for k in range(N)}
    for (a, b), h in zip(PAIRS, heads):
        d[h] += 1; out[a + b - h] += 1
    for k in range(N):
        if d[k] in (1, 4, 5): return False
        if out[k] >= 1 and d[k] > 3: return False
        if dis[k] == 0 and d[k] not in (0, 2, 3, 6): return False
    return True
stab = [g for g in itertools.permutations(range(N)) if {frozenset((g[a], g[b])) for a, b in DD} == {frozenset(p) for p in DD}]
reps = {}
for bits in itertools.product((0, 1), repeat=len(PAIRS)):
    heads = [p[b] for p, b in zip(PAIRS, bits)]
    if not ok(heads): continue
    arcs = frozenset((p[0] + p[1] - h, h) for p, h in zip(PAIRS, heads))
    key = min(tuple(sorted((g[a], g[b]) for a, b in arcs)) for g in stab)
    if key not in reps: reps[key] = {"%d,%d" % p: h for p, h in zip(PAIRS, heads)}
json.dump(list(reps.values()), open("logs/ad2_reps.json", "w"))
print("AD2 orientation classes:", len(reps))
