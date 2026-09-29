"""Mark a lattice EXCLUDED in the tracker when all n chunks of its stream run are chunk_done (every pair EXCLUDED or SWAP-COVERED)."""
import json, glob, os
p = "data/finishC/finishC_tracker.json"; T = json.load(open(p)); byid = {v["id"]: v for v in T["lattices"]}; new = []
for f in glob.glob("data/finishC/stream/*/chunks.jsonl"):
    recs = [json.loads(l) for l in open(f) if l.strip()]
    for n in {r["chunk"][1] for r in recs if r.get("chunk")}:
        done = {r["chunk"][0]: r for r in recs if r.get("chunk") and r["chunk"][1] == n and r.get("chunk_done")}
        lid = recs[0]["id"]
        if len(done) == n and byid[lid]["status"] != "excluded":
            np_ = sum(r["n_pairs"] for r in done.values())
            byid[lid]["status"] = "excluded"; byid[lid].setdefault("reviewed_by", []).append("C2")
            byid[lid]["by"] = "29/09 C2 stream sweep (a): %d/%d chunks done, %d ordered pairs, all EXCLUDED (char trap / stage 1 with EC + boundary points / star sums) or swap-covered; %s" % (n, n, np_, f)
            new.append(lid)
json.dump(T, open(p, "w"), indent=1)
print("newly excluded:", new, "| total", sum(v["status"] == "excluded" for v in T["lattices"]))
