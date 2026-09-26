#!/bin/bash
# note 40: when an M1 n=6 lane finishes, reuse it for a quarter of M1 n=5 job 10 (228 leaves)
cd /c/home/researcher/Desktop/c2_experimental
lane() {  # $1 = n=6 job whose lane we inherit, $2 $3 = leaf range of M1 n=5 job 10
  until grep -q "^DONE" logs/orbit_leaves_m1n6_$1.out 2>/dev/null; do sleep 60; done
  REPS=1 .venv/Scripts/python.exe scripts/orbit_leaves.py E01_12_23_34_04 10 $2 $3 > logs/orbit_leaves_m1n5_10_$2.out 2>&1
}
lane 15 0 56 & lane 7 57 113 & lane 11 114 170 & lane 12 171 227 &
wait; echo "M1 CLOSE SCHED DONE" >> logs/m1_close.log
