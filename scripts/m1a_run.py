"""Certified skeleton-level LP for the classes of an M1 family with A (note 34).  Usage: python m1a_run.py <n> <k> <K>"""
import sys, json, time
sys.path.insert(0, "scripts")
import m1a_colmodel as MC
n, k, K = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
cls = json.load(open("logs/m1a_classes_%d.json" % n))
f = open("logs/m1a_res_%d_%d.jsonl" % (n, k), "w")
for idx, (key, mult, In) in enumerate(cls):
    if idx % K != k: continue
    t0 = time.time(); r = MC.run_class(key); r.update({"idx": idx, "mult": mult, "In": In, "secs": round(time.time() - t0, 1)})
    f.write(json.dumps(r) + "\n"); f.flush()
    print(idx, "slack %.3f" % r["slack"], "cert", r["cert"], r["secs"], "s"); sys.stdout.flush()
