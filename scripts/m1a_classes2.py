"""M1 families with an A block, faster enumeration (note 35): orientations are first reduced to classes under the family group
(dihedral group of T = (0..n-1) x permutations of the other blocks); for one representative orientation per class, every choice of
D-structures (A's structure included) is run through the sound block filter (m1_blocks4.check); surviving skeletons are reduced
to classes (m1a_classes.canon).  Coverage: every labelled skeleton lies over some orientation, which is the image g(O) of a
representative O; g maps its skeletons bijectively onto those of O, and the filter and the LP model are relabelling-invariant.
Usage: python m1a_classes2.py <n> <k> <K>   -> logs/m1a_cls2_<n>_<k>.json"""
import sys, time, itertools, json
sys.path.insert(0, "scripts")
import m1_blocks4 as M4, m1a_classes as MC
N = 7

def orient_key(In, maps):
    arcs = [(a, b) for b in range(N) for a in In[b]]
    return min(tuple(sorted((g[a], g[b]) for a, b in arcs)) for g in maps)

if __name__ == "__main__":
    n, k, K = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    maps = MC.group(n); t0 = time.time()
    reps = {}
    for In, Ab in M4.orientations(n):
        if Ab is None: continue
        key = orient_key(In, maps)
        if key not in reps: reps[key] = (In, Ab)
    reps = list(reps.values())
    if k == 0: print("n", n, "orientation classes:", len(reps)); sys.stdout.flush()
    cls = {}; nsk = 0; nch = 0
    for idx, (In, Ab) in enumerate(reps):
        if idx % K != k: continue
        for choice in itertools.product(*M4.options(n, In, Ab)):
            nch += 1
            if not M4.check(n, In, choice, True, Ab): continue
            orbs = MC.triples(n, In, choice); assert len(orbs) == 42
            key = MC.canon(orbs, maps); nsk += 1
            if key not in cls: cls[key] = {str(a): b for a, b in In.items()}
    print("n", n, "worker", k, "choices", nch, "surviving skeletons (rep orientations)", nsk, "classes", len(cls), "%.0fs" % (time.time() - t0))
    json.dump([[list(map(list, key)), 1, In] for key, In in cls.items()], open("logs/m1a_cls2_%d_%d.json" % (n, k), "w"))
