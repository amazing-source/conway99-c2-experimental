#!/bin/bash
# note 35: A-generic filter stage for M1 n=5,6 (single cycles) and the 47 mixture classes
PY=.venv/Scripts/python.exe
for spec in edges=01,12,23,34,04 edges=01,12,23,34,45,05 $(seq 0 46); do
  for k in 0 1 2 3; do timeout 3600 $PY scripts/mix_filter3.py $spec $k 4 3500 "" > logs/mix3f_${spec//[=,]/_}_$k.out 2>&1 & done; wait
  echo "filtered $spec: $(cat logs/mix3f_${spec//[=,]/_}_*.out | grep -o 'surviving skeleton classes [0-9]*' | awk '{s+=$4} END {print s}') non-A parts (sum over workers), $(grep -c 'TIME CAP' logs/mix3f_${spec//[=,]/_}_*.out | awk -F: '{s+=$2} END {print s}') capped"
done
echo MIX3 FILTER DONE
