#!/bin/bash
# note 40: v6 sound filter on the mixture classes not yet filtered (3..46), one process per class, P in parallel
cd /c/home/researcher/Desktop/c2_experimental
P=${P:-6}
seq 3 46 | xargs -P $P -I{} bash -c 'start=$(date +%s); timeout 7200 .venv/Scripts/python.exe scripts/mix_filter6.py {} 0 1 7000 "" > logs/mix6f_{}_0.out 2>&1; echo "class {} rc=$? $(( $(date +%s) - start ))s $(tail -c 200 logs/mix6f_{}_0.out | tr "\n" " " | grep -o "orientation classes [0-9]*.*" | cut -c1-160)"' >> logs/filter_all.log
echo "FILTER ALL DONE" >> logs/filter_all.log
