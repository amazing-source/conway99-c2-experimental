#!/bin/bash
# note 40: run orbit-level tasks from a task file, P in parallel.  Task lines:
#   gen <class id> <job>         orientation-level LP (all D variable) on job <job> of logs/mix6_cls_<class id>_S_*.json
#   surv <survivors json> <idx>  fixed-skeleton orbit LP on one pair-level survivor
cd /c/home/researcher/Desktop/c2_experimental
P=${P:-8}; TASKS=$1
run() {
  set -- $1
  if [ "$1" = gen ]; then
    TAG=$2 TL=3000 timeout 3300 .venv/Scripts/python.exe scripts/orbit_colmodel_gen.py "logs/mix6_cls_$2_S_*.json" $3 > logs/orbit_gen_$2_$3.out 2>&1
    echo "gen $2 $3: $(tail -n 1 logs/orbit_gen_$2_$3.out | cut -c1-160)"
  else
    TL=1500 timeout 1700 .venv/Scripts/python.exe scripts/orbit_colmodel.py $2 $3 2>&1 | grep "^survivor [0-9]*:" | sed "s|^|surv $2 |"
  fi
}
export -f run
cat $TASKS | xargs -P $P -I{} bash -c 'run "{}"' >> logs/orbit_queue.log
echo "QUEUE DONE $TASKS" >> logs/orbit_queue.log
