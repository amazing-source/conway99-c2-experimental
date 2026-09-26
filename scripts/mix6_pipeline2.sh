#!/bin/bash
# note 35: same as mix6_pipeline.sh but over a given list of specs (to run several instances in parallel); W = workers per stage
PY=.venv/Scripts/python.exe
W=${W:-4}
for spec in "$@"; do
  tag=${spec//[=,]/_}
  if [[ $spec == edges=* ]]; then ci="E${spec#edges=}"; ci=${ci//,/_}; else ci=$spec; fi
  if [ $(grep -l "done$" logs/mix6f_${tag}_*.out 2>/dev/null | wc -l) -lt $W ]; then
    for k in $(seq 0 $((W-1))); do timeout 5400 $PY scripts/mix_filter6.py $spec $k $W 5300 "" > logs/mix6f_${tag}_$k.out 2>&1 & done; wait
  fi
  echo "filtered $spec: $(grep -h -o 'surviving skeleton classes [0-9]*' logs/mix6f_${tag}_*.out | awk '{s+=$4} END {print s}') classes; capped workers: $(grep -l 'TIME CAP' logs/mix6f_${tag}_*.out | wc -l)"
  for k in $(seq 0 $((W-1))); do timeout 21600 $PY scripts/mix_union_lp.py "logs/mix6_cls_${ci}_S_*.json" $k $W 400 $tag >> logs/mix6_ulp_${tag}_$k.out 2>&1 & done; wait
  echo "union LPs done for $spec: $(cat logs/mix6_ulp_${tag}_*.out | grep -c leaves) jobs, unresolved leaves: $(cat logs/mix6_ulp_${tag}_*.out | grep -o 'unresolved [0-9]*' | awk '{s+=$2} END {print s}')"
done
echo "INSTANCE DONE: $*"
