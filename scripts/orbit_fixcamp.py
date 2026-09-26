"""Orientation campaign by FIXING BLOCKS (note 40): orbit-level LP (orientation fixed, all D-structures variable) where the D-structure
is fixed at a growing set of blocks; the options at each block are those occurring in the filtered leaves consistent with the blocks
already fixed.  Node = partial assignment {block: option}.  Infeasible node (exact certificate, model 'gen' + forbid) => every leaf
extending it dies.  Feasible node => fix one more block (the one with the most options among the node's leaves), children = all its
options (complete cover of the node's leaves).  A node whose leaves are all fixed and still feasible is reported (never seen so far).
Usage: python orbit_fixcamp.py <class id> <job> [max nodes]"""
import sys, json, glob, time, os
from collections import Counter, defaultdict
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_gen as OG
ci, job = sys.argv[1], int(sys.argv[2]); maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 400
jobs = []
for f in sorted(glob.glob("logs/mix6_cls_%s_S_*.json" % ci)):
    d = json.load(open(f))
    for po in d["per_orient"]:
        if po["leaves"]: jobs.append(po)
po = jobs[job]; In = {int(x): v for x, v in po["In"].items()}; A = po["A"]
leaves = [tuple(sorted(tuple(z) for z in L)) for L in po["leaves"]]
g0 = OG.OrbitModelGen(In)
blockof = lambda L, c: tuple(z for z in L if z[0] == c)

def forbid_for(assign):
    forbid = set()
    for c, trip in assign.items():
        thirds = defaultdict(list)
        for (i, x, y) in trip: thirds[x].append(y)
        lab = {}
        for x, ys in thirds.items():
            os_ = [o for o in g0.orbs_of[frozenset((c, x))] if g0.pivot[o] == c]
            for o, y in zip(os_, sorted(ys)): lab.setdefault((x, y), []).append(o)
        partner = {}
        for (x, y), Zs in lab.items():
            for t_, Z in enumerate(Zs): partner[Z] = lab[(y, x)][t_]
        for Z, W in partner.items():
            i_, j_, _ = g0.T[Z]
            for k in range(7):
                if k in (i_, j_): continue
                for Dz in g0.orbs_of[frozenset((c, k))]:
                    if g0.pivot[Dz] == c and Dz != W: forbid.add((Z, Dz))
    return forbid

out = open("logs/orbit_fixcamp_%s_%d.jsonl" % (ci, job), "a")
stack = [({}, list(range(len(leaves))), None)]; nodes = 0; t0 = time.time(); open_nodes = 0
while stack:
    assign, idx, init = stack.pop()
    if nodes >= maxn: open_nodes += 1 + len(stack); break
    nodes += 1; t1 = time.time()
    fb = forbid_for(assign)
    if not assign and os.environ.get('SKIPROOT'):          # orientation-level LP already known feasible
        obj, st0 = 0.0, 'feasible'
        rec = {"node": nodes, "assign": {}, "fixed_blocks": [], "nleaves": len(idx), "status": "feasible(known)", "slack": 0, "secs": 0}
        out.write(json.dumps(rec) + chr(10)); out.flush(); print(rec)
        free_blocks = [c for c in range(7) if c != A]
        opts = {c: Counter(blockof(leaves[t], c) for t in idx) for c in free_blocks}
        c = max(free_blocks, key=lambda b: len(opts[b]))
        for trip in opts[c]:
            sub = [t for t in idx if blockof(leaves[t], c) == trip]
            stack.append(({c: trip}, sub, None))
        continue
    g = OG.OrbitModelGen(In, forbid=fb)
    obj, y = g.solve(tlimit=float(os.environ.get('TL', 4000)), verbose=False, init=init)   # warm start from the parent's columns
    if g.done and obj > 1e-6:
        ok, b = g.verify(y)
        st = 'dead' if ok else 'certfail'
        if ok: OM.save_cert(g, y, "logs/orbit_certs/fc_%s_%d_%d.json.gz" % (ci, job, nodes), "gen",
                            {"In": po["In"], "forbid": sorted(map(list, fb)), "assign": {str(c): [list(z) for z in v] for c, v in assign.items()}}, b)
    else: st = 'feasible' if g.done else 'timeout'
    rec = {"node": nodes, "assign": {str(c): len(v) for c, v in assign.items()}, "fixed_blocks": sorted(assign), "nleaves": len(idx),
           "status": st, "slack": round(obj, 4), "secs": round(time.time() - t1)}
    out.write(json.dumps(rec) + "\n"); out.flush(); print(rec); sys.stdout.flush()
    if st == 'dead': continue
    if st != 'feasible': open_nodes += 1; continue
    free_blocks = [c for c in range(7) if c != A and c not in assign]
    opts = {c: Counter(blockof(leaves[t], c) for t in idx) for c in free_blocks}
    cands = [c for c in free_blocks if len(opts[c]) > 1] or [c for c in free_blocks if len(opts[c]) == 1 and opts[c]]
    if not cands: print("UNRESOLVED fully fixed node", assign); open_nodes += 1; continue
    c = max(cands, key=lambda b: len(opts[b]))
    for trip in opts[c]:
        sub = [t for t in idx if blockof(leaves[t], c) == trip]
        a2 = dict(assign); a2[c] = trip; stack.append((a2, sub, getattr(g, 'final_keys', None)))
print("FIXCAMP %s job %d: nodes %d open %d %s %.0fs" % (ci, job, nodes, open_nodes, "ALL DEAD" if open_nodes == 0 else "INCOMPLETE", time.time() - t0))
