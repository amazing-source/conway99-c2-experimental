"""Leaf A-check (note 40): for a non-A part (orbit triples of all pivots != A) and the degree-6 block A, enumerate A's D-graphs g
and run the SOUND block filter (19.1 2-factor, profiles 27.1 with the certain components: closed D-cycles at every block, A's
cycles included, typed rule) on the full skeleton.  Returns the list of A-structures that pass.  No LP."""
import sys, json, glob, time, itertools
from collections import defaultdict
sys.path.insert(0, "scripts")
import mix_enum as ME, mix_filter as MF
import networkx as nx
N = 7; P = ME.P

def passing_A(orbs, In, A, tw):
    # orbs: non-A orbit triples (i,j,k); In: dict block -> anchored-at list; tw: set of twisted pairs
    base_dg = defaultdict(list)
    for (i, j, k) in orbs:
        if j < k or True: pass
    # D-graph at each non-A pivot c: edges (x,y) from triples (c,x,y) (each D-edge gives two triples)
    dgs = {}
    seen = defaultdict(int)
    for (c, x, y) in orbs: seen[(c, x, y)] += 1
    for c in range(N):
        if c == A: continue
        edges = []
        cnt = defaultdict(int)
        for (cc, x, y), m in seen.items():
            if cc == c: cnt[(x, y)] += m
        done = defaultdict(int)
        for (x, y), m in cnt.items():
            if x < y: edges += [(x, y)] * m
        twl = {x for x in range(N) if P(c, x) in tw}
        dgs[c] = (edges, twl)
    okA = []
    for g in ME.dgraphs([x for x in range(N) if x != A], []):
        full = dict(dgs); full[A] = (list(g), set())
        allorbs = MF.orbits_from(full)
        assigned = set(range(N))
        comps = {c: MF.comps_of(c, full[c], assigned) for c in range(N)}
        memo = {}
        if all(MF.block_ok(j, allorbs, comps, memo) for j in range(N)):
            okA.append(g)
    return okA

if __name__ == "__main__":
    pat = sys.argv[1]; t0 = time.time(); stats = []
    for f in sorted(glob.glob(pat)):
        d = json.load(open(f))
        for po in d["per_orient"]:
            if not po["leaves"]: continue
            In = {int(x): v for x, v in po["In"].items()}; A = po["A"]
            if A is None: continue
            tw = set()
            for c in range(N):
                for x in range(N):
                    if x != c and x not in In[c] and c not in In[x]: tw.add(P(c, x))
            for L in po["leaves"]:
                orbs = [tuple(z) for z in L]
                ok = passing_A(orbs, In, A, tw)
                stats.append(len(ok))
    import collections
    c = collections.Counter(stats)
    print("leaves", len(stats), "| killed by leaf A-check (no A-structure passes):", c[0], "| distribution of passing A-structures:", sorted(c.items())[:15], "| %.0fs" % (time.time() - t0))
