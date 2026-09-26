#!/bin/bash
# note 41: orbit-level block-fixing campaign over a task list "<class id> <job>", P lanes (all capped to 4 CPUs at idle priority)
cd /c/home/researcher/Desktop/c2_experimental
P=${P:-2}; TASKS=$1
run() { set -- $1; TL=5000 .venv/Scripts/python.exe scripts/orbit_fixcamp.py $1 $2 80 > logs/orbit_fixcamp_$1_$2.out 2>&1; echo "$1 $2: $(tail -n 1 logs/orbit_fixcamp_$1_$2.out | cut -c1-120)"; }
export -f run
cat $TASKS | xargs -P $P -I{} bash -c 'run "{}"' >> logs/fixcamp_queue.log
echo "QUEUE DONE $TASKS" >> logs/fixcamp_queue.log
