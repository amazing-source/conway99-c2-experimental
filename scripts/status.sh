#!/bin/bash
cd /c/home/researcher/Desktop/c2_experimental
echo "M1 n=4 (old): $(cat logs/m1a_run_4_*.out 2>/dev/null | grep -c slack)/214 done, $(cat logs/m1a_run_4_*.out 2>/dev/null | grep slack | grep -vc 'cert True') not certified"
for t in M1n5 M1n6; do echo "$t: $(cat logs/mix3_lp_${t}_*.out 2>/dev/null | grep -c slack) LPs done, $(cat logs/mix3_lp_${t}_*.out 2>/dev/null | grep slack | grep -vc 'cert True') not certified"; done
echo "--- mixture filter:"; cat logs/mix3_filter_all.log
cat logs/stop_m1a.log 2>/dev/null
