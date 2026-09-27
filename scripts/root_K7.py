"""T = K7 (all 21 pairs twisted, Sigma = empty, all one-block; note 45 s.8): orientation-level orbit LP (orbit_colmodel_gen with
In[c] = [] for every block), i.e. EVERY D-structure: at each block the 6 pivot orbits are matched arbitrarily (any transition
system, simple circuits or not).  Infeasible -> certificate logs/orbit_certs/root_K7.json.gz (model 'gen', spec {"In": ...}).
Usage: python root_K7.py      env TL, SMOOTH, LOWMEM"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import orbit_colmodel as OM, orbit_colmodel_gen as OG
In = {c: [] for c in range(7)}; t0 = time.time()
g = OG.OrbitModelGen(In); ncol = sum(len(M) for M in g.cols)
print("T = K7: columns %d rows built %.0fs" % (ncol, time.time() - t0), flush=True)
obj, y = g.solve(tlimit=float(os.environ.get('TL', 20000)), verbose=False)
rec = {"In": {str(c): [] for c in range(7)}, "columns": ncol}
if g.done and obj > 1e-6:
    ok, b = g.verify(y); rec["status"] = "dead" if ok else "certfail"; rec["slack"] = round(obj, 4)
    if ok: OM.save_cert(g, y, "logs/orbit_certs/root_K7.json.gz", "gen", {"In": rec["In"]}, b)
else: rec["status"] = "feasible" if g.done else "timeout"
rec["secs"] = round(time.time() - t0)
os.makedirs("logs/root", exist_ok=True); json.dump(rec, open("logs/root/root_K7.json", "w"))
print("ROOT K7: %s columns %d %ds" % (rec["status"], ncol, rec["secs"]), flush=True)
