#!/bin/bash
# note 35: v6 filter (A generic, per-orientation leaves) + union LPs, for M1 n=6 and the mixture classes 1..46 (bowtie = class 0 separately)
PY=.venv/Scripts/python.exe
W=${W:-6}
for spec in edges=01,12,23,34,04 edges=01,12,23,34,45,05 $(seq 1 46); do
  tag=${spec//[=,]/_}
  if [[ $spec == edges=* ]]; then ci="E${spec#edges=}"; ci=${ci//,/_}; else ci=$spec; fi
  for k in $(seq 0 $((W-1))); do timeout 3600 $PY scripts/mix_filter6.py $spec $k $W 3500 "" > logs/mix6f_${tag}_$k.out 2>&1 & done; wait
  echo "filtered $spec: $(grep -h -o 'surviving skeleton classes [0-9]*' logs/mix6f_${tag}_*.out | awk '{s+=$4} END {print s}') classes; capped workers: $(grep -l 'TIME CAP' logs/mix6f_${tag}_*.out | wc -l)"
  for k in $(seq 0 $((W-1))); do timeout 14400 $PY scripts/mix_union_lp.py "logs/mix6_cls_${ci}_S_*.json" $k $W 400 $tag > logs/mix6_ulp_${tag}_$k.out 2>&1 & done; wait
  echo "union LPs done for $spec: $(cat logs/mix6_ulp_${tag}_*.out | grep -c leaves) jobs, unresolved leaves: $(cat logs/mix6_ulp_${tag}_*.out | grep -o 'unresolved [0-9]*' | awk '{s+=$2} END {print s}')"
done
echo MIX6 PIPELINE DONE
