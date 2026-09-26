#!/bin/bash
# note 41: v6 sound filter on the mixture classes not yet filtered, ONE lane (low priority, capped CPUs)
cd /c/home/researcher/Desktop/c2_experimental
for c in 15 16 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46; do
  [ -f logs/mix6_cls_${c}_S_0.json ] && grep -q "done" logs/mix6f_${c}_0.out 2>/dev/null && continue
  start=$(date +%s); timeout 14000 .venv/Scripts/python.exe scripts/mix_filter6.py $c 0 1 13800 "" > logs/mix6f_${c}_0.out 2>&1
  echo "class $c rc=$? $(( $(date +%s) - start ))s $(tail -c 200 logs/mix6f_${c}_0.out | tr '\n' ' ' | grep -o 'orientation classes [0-9]*.*' | cut -c1-160)" >> logs/filter_all.log
done
echo "FILTER REST DONE" >> logs/filter_all.log
