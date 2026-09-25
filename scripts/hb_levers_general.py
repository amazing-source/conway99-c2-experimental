"""F2 (first-order pair level: L + PPE + S + C) on GENERAL H-beta skeletons with random valid free cycles (note 31).
One orientation per D7-class (6 classes), random beta orders, random cycles at each block.  SMALL TEST; definitive answers only."""
import sys, time, random, itertools
from collections import Counter
sys.path.insert(0, "scripts")
import hb_pairlevel as H, hb_p2_core as HC, m1_blocks4 as M4
N = H.N

def skeleton_from(In, order_bits):
    orbits = []
    for c in range(N):
        A, B = In[c] if not (order_bits >> c) & 1 else In[c][::-1]
        seq = [(c - 1) % N, A, B, (c + 1) % N]
        for x, y in zip(seq, seq[1:]): orbits += [(c, x, y), (c, y, x)]
    return orbits

if __name__ == "__main__":
    per_class, seed, secs = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    rng = random.Random(seed); seen = set(); reps = []
    for In, Ab in M4.orientations(7):
        ar = M4.arcs_of(In)
        if ar in seen: continue
        orb = set()
        for s in (1, -1):
            for r in range(7): orb.add(frozenset((((s * a + r) % 7), ((s * b + r) % 7)) for (a, b) in ar))
        seen |= orb; reps.append(In)
    t0 = time.time(); tally = Counter()
    for ci, In in enumerate(reps):
        for _ in range(per_class):
            if time.time() - t0 > 270: break
            ob = rng.randrange(128); orbits = skeleton_from(In, ob)
            per = {j: H.free_cycles(orbits, j, True) for j in range(N)}
            if any(len(v) == 0 for v in per.values()): tally[(ci, "no valid cycle")] += 1; continue
            nbs = {j: rng.choice(per[j]) for j in range(N)}
            m, groups = HC.model(orbits, nbs, None)
            F2 = {x for x in groups if not (x[0] == 'P2' and x[1] != x[2])}
            st = HC.solve(orbits, nbs, F2, secs)[0]
            tally[(ci, st)] += 1
    for k, v in sorted(tally.items(), key=str): print(k, v)
    print("time %.0fs" % (time.time() - t0))
