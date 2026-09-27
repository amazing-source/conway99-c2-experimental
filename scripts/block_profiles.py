"""Per-block pivot profile of every orientation class of the large-T mixture classes (for C1/structures' local system, note 44 §8).
For each class ci (orient_campaign order: orientation reps sorted by canonical key, idx = position) and each block c:
  anch = blocks x with {c,x} anchored AT c (both orbits pivot at c; In[c]), tw = T-neighbours of c (one orbit pivots at c),
  away = blocks x with {c,x} anchored at x (no orbit pivots at c).   #pivot orbits at c = 2|anch| + |tw|.
Output logs/large_T_block_profiles.json: {"classes": {ci: {"T": edges, "reps": [[[anch, tw] per block] per idx]}},
"census": {(|anch|, |tw|): count over all (orientation, block)}, "root": known root status per (ci, idx)}."""
import sys, os, json, glob
from collections import Counter
sys.path.insert(0, "scripts")
import orient_campaign as OC, mix_filter6 as F
N = 7
classes = [int(a) for a in sys.argv[1:]] or [15, 16] + list(range(18, 47))
out = {"classes": {}, "census": Counter(), "root": {}}
for ci in classes:
    twE, reps = OC.orientation_reps(ci)
    Tn = {c: sorted({b for a, b in twE if a == c} | {a for a, b in twE if b == c}) for c in range(N)}
    rows = []
    for idx, In in enumerate(reps):
        prof = [[sorted(In[c]), Tn[c]] for c in range(N)]
        rows.append(prof)
        for c in range(N): out["census"][(len(In[c]), len(Tn[c]))] += 1
    out["classes"][ci] = {"T": [list(e) for e in twE], "reps": rows}
    if os.path.exists("logs/orient_%d.jsonl" % ci):
        for line in open("logs/orient_%d.jsonl" % ci):
            r = json.loads(line); out["root"]["%d_%d" % (ci, r["idx"])] = r["status"]
    print("class %d: |T| %d, %d orientation classes" % (ci, len(twE), len(reps))); sys.stdout.flush()
out["census"] = {"%d,%d" % k: v for k, v in sorted(out["census"].items())}
json.dump(out, open("logs/large_T_block_profiles.json", "w"))
print("census (|anch at c|, |tw at c|): count", out["census"])
