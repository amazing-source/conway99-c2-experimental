"""Independent coverage check (C2 code) for structures' triangle-free pure-twisted classes: enumerate ALL labelled decompositions
of E(K7) into cycles (length >= 3) with no triangle; compute for each of the 14 representatives |Aut| under S7 and check the
representatives are pairwise non-isomorphic; coverage <=> sum 5040/|Aut| = number of labelled triangle-free decompositions."""
import sys, gzip, json, itertools
N = 7
E = [frozenset(e) for e in itertools.combinations(range(N), 2)]
def cycles_through(edge, avail):
    """all cycles (as frozensets of edges) using `edge`, within available edge set, length >= 4 (triangle-free)"""
    a, b = sorted(edge); out = []
    adj = {v: [w for w in range(N) if frozenset((v, w)) in avail] for v in range(N)}
    def ext(path, used):
        u = path[-1]
        for w in adj[u]:
            if w == a and len(path) >= 4:
                out.append(frozenset(used | {frozenset((u, w))}))
            elif w not in path and w != a:
                ext(path + [w], used | {frozenset((u, w))})
    ext([a, b], {edge})
    return set(out)
count = 0
def rec(avail):
    global count
    if not avail: count += 1; return
    e = min(avail, key=lambda f: sorted(f))
    for cyc in cycles_through(e, avail):
        rec(avail - cyc)
rec(frozenset(E))
print("labelled triangle-free cycle decompositions of K7:", count)
def edgeset_of(dec): return frozenset(frozenset(frozenset((c[t], c[(t + 1) % len(c)])) for t in range(len(c))) for c in dec)
def img(D, g): return frozenset(frozenset(frozenset(g[v] for v in e) for e in C) for C in D)
path = sys.argv[1]; reps = []
for n in range(14):
    d = json.load(gzip.open("%s/logs/orbit_certs/zero_%02d.json.gz" % (path, n), "rt"))
    reps.append((d["labelled"], edgeset_of(d["decomposition"])))
perms = list(itertools.permutations(range(N)))
tot = 0; canon = []
for lab, D in reps:
    auts = sum(1 for g in perms if img(D, g) == D)
    orb = 5040 // auts; tot += orb
    canon.append(min(sorted(sorted(sorted(g[v] for v in e) for e in C) for C in img(D, g)) for g in perms[:0]) if False else None)
    print("rep orbit size", orb, "| stored 'labelled'", lab)
iso = 0
for a in range(14):
    for b in range(a + 1, 14):
        if any(img(reps[a][1], g) == reps[b][1] for g in perms): iso += 1
print("sum of orbit sizes:", tot, "| isomorphic rep pairs:", iso, "| COVERAGE", "OK" if tot == count and iso == 0 else "FAILED")
