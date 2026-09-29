"""Finish a gpairs lattice with the current frame_dfs: run every index not yet EXCLUDED in data/finishC/frame_dfs/<id>/*.jsonl, then mark it
excluded in the tracker if every index is covered. Usage: python finish_gpairs.py <id> [workers]"""
import sys, os, json, glob, numpy as np
from fractions import Fraction as F
from concurrent.futures import ProcessPoolExecutor
os.environ.update(FD_LEMMA_U="1", FD_SYM="1", FD_PREBUDGET="0")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
GP = r"C:\Users\RESEARCHER\AppData\Local\Temp\claude\C--Users-RESEARCHER-Desktop\19a7c411-3446-4f59-9793-6c42892ed6cd\scratchpad\ext\conway99-c1\data\finishC\ypairs\gpairs_%s.json"
def seen_of(lid):
    s = set()
    for f in glob.glob("data/finishC/frame_dfs/%s/*.jsonl" % lid):
        for l in open(f):
            try: r = json.loads(l)
            except Exception: continue
            if r.get("k") is not None and r.get("verdict", "").startswith("EXCLUDED"): s.add(r["k"])
    return s
def work(a):
    lid, ks = a; import bench as B, frame_dfs as FD
    P = json.load(open(GP % lid))["pairs"]; L = B.lat(lid); Binv = np.linalg.inv(np.array([[float(x) for x in r] for r in L["B"]]))
    cv = lambda v: np.rint(np.array([float(F(x)) for x in v]) @ Binv).astype(np.int64)
    out = open("data/finishC/frame_dfs/%s/c_new_%d.jsonl" % (lid, ks[0]), "a")
    for k in ks:
        r = FD.search(L, cv(P[k][0]), cv(P[k][1]), node_limit=200_000_000)
        out.write(json.dumps({"k": k, "verdict": r["verdict"], "code": "frame_dfs 29/09"}) + "\n"); out.flush()
if __name__ == "__main__":
    lid = "%03d" % int(sys.argv[1]); w = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    n = len(json.load(open(GP % lid))["pairs"]); todo = sorted(set(range(n)) - seen_of(lid)); print(lid, "todo", len(todo), flush=True)
    if todo:
        with ProcessPoolExecutor(w) as ex: list(ex.map(work, [(lid, todo[i::w]) for i in range(w)]))
    s = seen_of(lid); print(lid, len(s), "/", n)
    if len(s) == n:
        p = "data/finishC/finishC_tracker.json"; T = json.load(open(p))
        for v in T["lattices"]:
            if v["id"] == int(lid): v["status"] = "excluded"; v["by"] = "29/09 C2 h-stage sweep (a): all %d pairs of gpairs_%s EXCLUDED (finished with the 29/09 frame_dfs)" % (n, lid); v.setdefault("reviewed_by", []).append("C2")
        json.dump(T, open(p, "w"), indent=1); print("total", sum(v["status"] == "excluded" for v in T["lattices"]))
