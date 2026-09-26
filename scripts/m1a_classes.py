"""M1 families with an A block (note 34): surviving skeletons (block filter m1_blocks4.check, sound) -> orbit-triple lists ->
classes under the symmetry group of the family (dihedral group of T = (0..n-1) x permutations of the non-T blocks).
Usage: python m1a_classes.py <n> <k> <K> <seconds>  -> logs/m1a_cls_<n>_<k>.json : {canonical triples: [multiplicity, orientation]}"""
import sys, time, itertools, json
sys.path.insert(0, "scripts")
import m1_blocks4 as M4
N = 7

def triples(n, In, choice):
    T = list(range(n)); dedges = []
    for c in range(N):
        ch = choice[c]
        Tw = [T[(c - 1) % n], T[(c + 1) % n]] if c < n else []
        if ch[0] == 'A':
            for cyc in ch[1]:
                if len(cyc) == 2: a, b = cyc; dedges += [(c, a, b), (c, a, b)]
                else: dedges += [(c, x, y) for x, y in zip(cyc, cyc[1:] + cyc[:1])]
        elif ch[0] == 'C':
            I = list(ch[1])
            if len(I) == 2: dedges += [(c, I[0], I[1])] * 2
            elif len(I) == 3: dedges += [(c, I[0], I[1]), (c, I[1], I[2]), (c, I[2], I[0])]
        elif ch[0] == 'L':
            a, b = ch[1]; dedges += [(c, a, b), (c, a, b), (c, Tw[0], Tw[1])]
        else:
            seq = [Tw[0]] + list(ch[1]) + [Tw[1]] if Tw else list(ch[1])
            dedges += [(c, x, y) for x, y in zip(seq, seq[1:])]
    orbs = []
    for (c, x, y) in dedges: orbs += [(c, x, y), (c, y, x)]
    return orbs

def group(n):
    rest = list(range(n, N)); maps = []
    for s in (1, -1):
        for r in range(n):
            for perm in itertools.permutations(rest):
                g = {t: (s * t + r) % n for t in range(n)}
                g.update(dict(zip(rest, perm))); maps.append(g)
    return maps

def canon(orbs, maps):
    return min(tuple(sorted(tuple(g[v] for v in z) for z in orbs)) for g in maps)

if __name__ == "__main__":
    n, k, K, budget = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
    maps = group(n); t0 = time.time(); cls = {}; nsk = 0; done = True
    for idx, (In, Ab) in enumerate(M4.orientations(n)):
        if Ab is None or idx % K != k: continue
        for choice in itertools.product(*M4.options(n, In, Ab)):
            if time.time() - t0 > budget: done = False; break
            if not M4.check(n, In, choice, True, Ab): continue
            orbs = triples(n, In, choice); assert len(orbs) == 42, len(orbs)
            key = canon(orbs, maps); nsk += 1
            if key in cls: cls[key][0] += 1
            else: cls[key] = [1, {str(a): b for a, b in In.items()}]
        if not done: break
    print("n", n, "worker", k, "skeletons", nsk, "classes", len(cls), "done" if done else "TIME CAP", "%.0fs" % (time.time() - t0))
    json.dump([[list(map(list, key)), v[0], v[1]] for key, v in cls.items()], open("logs/m1a_cls_%d_%d.json" % (n, k), "w"))
