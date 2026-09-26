#!/bin/bash
# note 35: capped certified pipeline for M1 families with an A block, n = 4, 5, 6 (user approval 26/09 morning)
PY=.venv/Scripts/python.exe
for n in 4 5 6; do
  for k in 0 1 2 3 4 5 6 7; do timeout 3000 $PY scripts/m1a_classes2.py $n $k 8 > logs/m1a_cls2_${n}_$k.out 2>&1 & done; wait
  $PY - << PYEOF
import json, glob
allc = {}
for f in glob.glob("logs/m1a_cls2_${n}_*.json"):
    for key, m, In in json.load(open(f)):
        allc.setdefault(tuple(map(tuple, key)), In)
json.dump([[list(map(list, k)), 1, v] for k, v in allc.items()], open("logs/m1a_classes_${n}.json", "w"))
print("n ${n}: merged classes", len(allc))
PYEOF
  for k in 0 1 2 3 4 5 6 7; do timeout 5400 $PY scripts/m1a_run.py $n $k 8 > logs/m1a_run_${n}_$k.out 2>&1 & done; wait
  echo "n $n LP stage done"
done
echo PIPELINE DONE
