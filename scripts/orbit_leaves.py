"""Per-leaf orbit-level LPs with the degree-6 block A variable (note 40), with column reuse between consecutive leaves and the
Lagrangian early stop.  Each dead leaf gets an exact certificate (model 'var'), re-checkable by orbit_verify_certs.py.
Usage: python orbit_leaves.py <class id> <job> [first leaf] [last leaf]"""
import sys, json, glob, time, os
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_var as OV
ci, job = sys.argv[1], int(sys.argv[2])
jobs = []
for f in sorted(glob.glob("logs/mix6_cls_%s_S_*.json" % ci)):
    d = json.load(open(f))
    for po in d["per_orient"]:
        if po["leaves"]: jobs.append((po, [tuple(map(tuple, L)) for L in po["leaves"]]))
po, leaves = jobs[job]
lo = int(sys.argv[3]) if len(sys.argv) > 3 else 0; hi = int(sys.argv[4]) if len(sys.argv) > 4 else len(leaves) - 1
out = open("logs/orbit_leaves_%s_%d.jsonl" % (ci, job), "a")
done = set()
if os.path.exists("logs/orbit_leaves_%s_%d.jsonl" % (ci, job)):
    for l in open("logs/orbit_leaves_%s_%d.jsonl" % (ci, job)):
        try:
            r = json.loads(l)
            if r["status"] == "dead": done.add(r["leaf"])
        except Exception: pass
# symmetry: permutations of the 7 blocks preserving the twisted graph, the anchoring (In) and A map leaves to leaves; the orbit LP is
# invariant under renaming, so only the lexicographically minimal image of each leaf needs an LP (the others are covered by it).
import itertools
In_ = {int(x): set(v) for x, v in po["In"].items()}
arcs = {(c, x) for c, xs in In_.items() for x in xs}
stab = [g for g in itertools.permutations(range(7))
        if {(g[c], g[x]) for (c, x) in arcs} == arcs and (po["A"] is None or g[po["A"]] == po["A"])]
canon = lambda L: min(tuple(sorted((g[i], g[j], g[k]) for (i, j, k) in L)) for g in stab)
keyof = {tuple(sorted(L)): t for t, L in enumerate(leaves)}
repof = {}
for t, L in enumerate(leaves):
    repof[t] = keyof.get(canon(L), t)
print("stabilizer order %d, leaf classes %d of %d" % (len(stab), len(set(repof.values())), len(leaves))); sys.stdout.flush()
prev = None
for t in range(lo, hi + 1):
    if t in done: continue
    if os.environ.get('REPS') and repof[t] != t:
        out.write(json.dumps({"leaf": t, "status": "sym", "rep": repof[t]}) + "
"); out.flush(); continue
    t0 = time.time()
    g = OV.OrbitModelVar(leaves[t], po["A"])
    obj, y = g.solve(tlimit=float(os.environ.get('TL', 2400)), verbose=False, init=prev)
    st = 'feasible' if (g.done and obj <= 1e-6) else ('timeout' if not g.done else None)
    if st is None:
        ok, b = g.verify(y)
        st = 'dead' if ok else 'certfail'
        if ok: OM.save_cert(g, y, "logs/orbit_certs/leaf_%s_%d_%d.json.gz" % (ci, job, t), "var", {"leaf": [list(z) for z in leaves[t]], "A": po["A"]}, b)
    prev = getattr(g, 'final_keys', None)
    rec = {"leaf": t, "status": st, "slack": round(obj, 4), "secs": round(time.time() - t0, 1)}
    out.write(json.dumps(rec) + "\n"); out.flush(); print(rec); sys.stdout.flush()
print("DONE %s job %d leaves %d-%d" % (ci, job, lo, hi))
