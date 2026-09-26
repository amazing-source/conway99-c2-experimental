#!/bin/bash
# note 35: filter stage for the 47 multi-cycle twisted subgraph classes (sound block filter, symmetry-reduced)
PY=.venv/Scripts/python.exe
for ci in $(seq 0 46); do
  for k in 0 1 2 3 4 5; do timeout 2400 $PY scripts/mix_filter.py $ci $k 6 2300 > logs/mix_cls_${ci}_$k.out 2>&1 & done; wait
  $PY - << PYEOF
import json, glob, sys
sys.path.insert(0, "scripts")
import mix_filter as MF
keys = {}; done = True; twE = None
for f in glob.glob("logs/mix_cls_${ci}_*.json"):
    d = json.load(open(f)); done &= d["done"]; twE = d["twE"]
    auts = MF.automorphisms([tuple(e) for e in twE])
    for k, In in d["classes"]:
        keys.setdefault(MF.canon_skel([tuple(z) for z in k], auts), In)
json.dump({"twE": twE, "done": done, "classes": [[list(map(list, k)), v] for k, v in keys.items()]}, open("logs/mix_classes_${ci}.json", "w"))
print("class ${ci}", twE, "surviving skeleton classes", len(keys), "complete" if done else "INCOMPLETE (time cap)")
PYEOF
done
echo MIX FILTER DONE
