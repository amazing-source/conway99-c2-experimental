"""Orbit-level UNION LPs per orientation (note 40): the orbit-level analogue of mix_union_lp.py.
For an orientation job (representative, own labelling) with surviving non-A leaves S (sound filter v6), the LP allows, for every
orbit, the thirds occurring in S (union), and every third for the orbits of the degree-6 block A (A variable).  Infeasible (exact
certificate, saved) => every leaf of S dies (each leaf's LP is more constrained).  Feasible => split S by the pivot block where the
leaves differ most and recurse.  A single leaf that stays feasible is reported (no A-branching here).
Usage: python orbit_union.py <class json glob> <tag> <job indices...>"""
import sys, json, glob, time, os
from collections import defaultdict, Counter
import numpy as np
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_gen as OG
N = 7

def solve(po, leaves, tl, certpath):
    In = {int(x): v for x, v in po["In"].items()}; A = po["A"]
    allowed = defaultdict(set)                       # (pivot i, free j) -> allowed thirds
    for L in leaves:
        for (i, j, k) in L: allowed[(i, j)].add(k)
    if A is not None:
        for x in range(N):
            if x != A: allowed[(A, x)] = {y for y in range(N) if y not in (A, x)}
    forbid = set()
    # labelling identical to OrbitModelGen: pairs lexicographic, s = 0, 1
    anch = {}
    for c, xs in In.items():
        for x in xs: anch[frozenset((c, x))] = c
    T = []; orbs_of = defaultdict(list)
    for a in range(N):
        for b in range(a + 1, N):
            R = frozenset((a, b)); piv = [anch[R], anch[R]] if R in anch else [a, b]
            for s in (0, 1):
                i = piv[s]; T.append((i, a + b - i)); orbs_of[R].append(len(T) - 1)
    for Z, (i, j) in enumerate(T):
        for k in range(N):
            if k in (i, j): continue
            if k not in allowed[(i, j)]:
                for Dz in orbs_of[frozenset((i, k))]: forbid.add((Z, Dz))
    g = OG.OrbitModelGen(In, forbid=forbid)
    obj, y = g.solve(tlimit=tl, verbose=False)
    if g.done and obj > 1e-6:
        ok, b = g.verify(y)
        if ok:
            OM.save_cert(g, y, certpath, "gen", {"In": po["In"], "allowed": {"%d,%d" % key: sorted(v) for key, v in allowed.items()}}, b)
        return ('dead' if ok else 'certfail'), obj
    return ('feasible' if g.done else 'timeout'), obj

def rec(po, leaves, depth, log, tl, tag, job):
    t0 = time.time(); certpath = "logs/orbit_certs/union_%s_%d_%d.json.gz" % (tag, job, len(log))
    st, obj = solve(po, leaves, tl, certpath)
    log.append({"depth": depth, "nleaves": len(leaves), "status": st, "slack": obj, "secs": round(time.time() - t0, 1),
                "cert": certpath if st == 'dead' else None, "leaves": [[list(z) for z in L] for L in leaves] if st == 'dead' else None})
    print("   depth %d leaves %d: %s %.3f %.0fs" % (depth, len(leaves), st, obj, time.time() - t0)); sys.stdout.flush()
    if st == 'dead': return []
    if len(leaves) == 1: return [(leaves[0], st)]
    best = None
    for c in range(N):
        sig = Counter(tuple(sorted(z for z in L if z[0] == c)) for L in leaves)
        if len(sig) > 1 and (best is None or len(sig) > best[1]): best = (c, len(sig))
    c = best[0]; groups = defaultdict(list)
    for L in leaves: groups[tuple(sorted(z for z in L if z[0] == c))].append(L)
    res = []
    for gl in groups.values(): res += rec(po, gl, depth + 1, log, tl, tag, job)
    return res

if __name__ == "__main__":
    pat, tag = sys.argv[1], sys.argv[2]
    jobs = []
    for f in sorted(glob.glob(pat)):
        d = json.load(open(f))
        for po in d["per_orient"]:
            if po["leaves"]: jobs.append((po, [tuple(map(tuple, L)) for L in po["leaves"]]))
    out = open("logs/orbit_union_%s.jsonl" % tag, "a")
    for job in [int(a) for a in sys.argv[3:]]:
        po, leaves = jobs[job]; t0 = time.time(); log = []
        print("job %d: %d leaves, In %s" % (job, len(leaves), po["In"])); sys.stdout.flush()
        bad = rec(po, leaves, 0, log, float(os.environ.get('TL', 1500)), tag, job)
        out.write(json.dumps({"job": job, "In": po["In"], "A": po["A"], "nleaves": len(leaves), "lps": len(log),
                              "unresolved": [[[list(z) for z in L], st] for L, st in bad], "log": log, "secs": round(time.time() - t0, 1)}) + "\n"); out.flush()
        print("job %d: LPs %d unresolved %d %.0fs" % (job, len(log), len(bad), time.time() - t0)); sys.stdout.flush()
