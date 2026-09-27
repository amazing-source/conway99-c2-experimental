"""Family (B) of the finish line (note 46): ALL-DIS configuration (every one of the 42 orbits has its D-partner on a DISJOINT
pair; 7 free stars; Sigma = empty).  Unified orbit model (orbit_colmodel_U) with every pair of type 'dd' (both orbits dis), no
one-block or sib column; root LP.  Infeasible -> exact certificate logs/orbit_certs/root_alldis.json.gz (model 'U', spec ptype),
re-checkable with orbit_verify_U.py.   Usage: python root_alldis.py      env TL, LOWMEM, SMOOTH"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import orbit_colmodel as OM, orbit_colmodel_U as OU
N = 7
pt = {(a, b): ('dd',) for a in range(N) for b in range(a + 1, N)}
spec = {"%d,%d" % k: list(v) for k, v in pt.items()}
t0 = time.time(); g = OU.OrbitModelU(pt)
if g.empty_orbits: print("ALL-DIS: dead-comb, empty orbits", g.empty_orbits); sys.exit()
ncol = sum(len(M) for M in g.cols); print("ALL-DIS: columns %d, built %.0fs" % (ncol, time.time() - t0), flush=True)
obj, y = g.solve(tlimit=float(os.environ.get('TL', 20000)), verbose=False)
rec = {"columns": ncol}
if g.done and obj > 1e-6:
    ok, b = g.verify(y); rec["status"] = "dead" if ok else "certfail"; rec["slack"] = round(obj, 4)
    if ok: OM.save_cert(g, y, "logs/orbit_certs/root_alldis.json.gz", "U", {"ptype": spec}, b)
else: rec["status"] = "feasible" if g.done else "timeout"
rec["secs"] = round(time.time() - t0); json.dump(rec, open("logs/root/root_alldis.json", "w"))
print("ROOT ALL-DIS: %s columns %d %ds" % (rec["status"], ncol, rec["secs"]), flush=True)
