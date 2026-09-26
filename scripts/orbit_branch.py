"""Branching on ONE orbit's D-partner (note 40; advice of 'structures'): orientation fixed, orbit-level LP (orbit_colmodel_gen).
A node is a set of forbidden (orbit, partner) choices.  Infeasible node: exact certificate saved (spec: In, forbid) and re-checkable
by orbit_verify_certs.py.  Feasible node: branch on the orbit whose LP mass is most spread over its partner choices; children = ALL
its remaining partner choices (complete cover).
Usage: python orbit_branch.py <class id> <job> [max nodes]"""
import sys, json, glob, time, os
from collections import defaultdict
import numpy as np
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_gen as OG

def options(g, Z, forbid):
    i, j, _ = g.T[Z]
    return [Dz for k in range(7) if k not in (i, j) for Dz in g.orbs_of[frozenset((i, k))] if g.pivot[Dz] == i and (Z, Dz) not in forbid]

if __name__ == "__main__":
    ci, job = sys.argv[1], int(sys.argv[2]); maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 60
    jobs = []
    for f in sorted(glob.glob("logs/mix6_cls_%s_S_*.json" % ci)):
        d = json.load(open(f))
        for po in d["per_orient"]:
            if po["leaves"]: jobs.append(po)
    po = jobs[job]; In = {int(x): v for x, v in po["In"].items()}
    stack = [frozenset()]; nodes = 0; t0 = time.time(); log = []
    out = open("logs/orbit_branch_%s_%d.jsonl" % (ci, job), "a")
    while stack:
        if nodes >= maxn: print("NODE CAP"); break
        fb = stack.pop(); nodes += 1; t1 = time.time()
        g = OG.OrbitModelGen(In, forbid=set(fb))
        obj, y = g.solve(tlimit=float(os.environ.get('TL', 2400)), verbose=False)
        if g.done and obj > 1e-6:
            ok, b = g.verify(y)
            if ok:
                OM.save_cert(g, y, "logs/orbit_certs/br_%s_%d_%d.json.gz" % (ci, job, nodes), "gen", {"In": po["In"], "forbid": sorted(map(list, fb))}, b)
                rec = {"node": nodes, "depth": len(fb), "status": "dead", "slack": obj}
            else: rec = {"node": nodes, "status": "certfail", "slack": obj}; print(rec); break
        elif not g.done: rec = {"node": nodes, "status": "timeout"}; print(rec); break
        else:
            w = defaultdict(float)
            for (Z, Dz), x in zip(g.colinfo, g.last_x): w[(Z, Dz)] += x
            best = None
            for Z in range(42):
                opts = options(g, Z, fb)
                if len(opts) < 2: continue
                share = max(w.get((Z, D), 0.0) for D in opts)
                if best is None or share < best[0]: best = (share, Z, opts)
            share, Z, opts = best
            for D in opts: stack.append(fb | {(Z, D2) for D2 in opts if D2 != D})
            rec = {"node": nodes, "status": "branch", "orbit": Z, "nopts": len(opts), "maxshare": round(share, 3)}
        rec["secs"] = round(time.time() - t1); log.append(rec); out.write(json.dumps(rec) + "\n"); out.flush()
        print(rec); sys.stdout.flush()
    print("BRANCH %s job %d: nodes %d open %d %s %.0fs" % (ci, job, nodes, len(stack), "ALL DEAD" if not stack and all(r["status"] in ("dead", "branch") for r in log) else "INCOMPLETE", time.time() - t0))
