"""Count block-filter-surviving skeletons (orientation, full choice incl. A's structure) of an M1 family with an A block (note 33).
Usage: python m1a_count.py <n> <k> <K> <seconds>  -> prints counts; writes logs/m1a_surv_<n>_<k>.json"""
import sys, time, itertools, json
sys.path.insert(0, "scripts")
import m1_blocks4 as M4
n, k, K, budget = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
t0 = time.time(); surv = []; norient = 0; done = True
for idx, (In, Ab) in enumerate(M4.orientations(n)):
    if Ab is None or idx % K != k: continue
    norient += 1
    for choice in itertools.product(*M4.options(n, In, Ab)):
        if time.time() - t0 > budget: done = False; break
        if M4.check(n, In, choice, True, Ab): surv.append({"In": {str(a): b for a, b in In.items()}, "A": Ab, "choice": [list(map(str, c)) for c in choice]})
    if not done: break
print("n", n, "worker", k, "orientations scanned", norient, "surviving skeletons", len(surv), "done" if done else "TIME CAP", "%.0fs" % (time.time() - t0))
json.dump(surv, open("logs/m1a_surv_%d_%d.json" % (n, k), "w"))
