#!/bin/bash
# Stage 1 of the mixture campaign (note 43): per-leaf pair-level LP (pair_fast.py, MAXBB=0) on every no-A job; P lanes.
cd /c/home/researcher/Desktop/c2_experimental
P=${P:-1}
grep -v '^$' ${TASKS:-logs/pairfast_tasks.txt} | while read -r ci job; do
  [ -f "logs/pair_certs/open_${ci}_${job}.json" ] && continue
  echo "$ci $job"
done | xargs -P "$P" -L 1 bash -c 'r=$(MAXBB=0 .venv/Scripts/python.exe scripts/pair_fast.py $0 $1 2>&1 | tail -n 1); echo "$0 $1: $r" >> logs/pairfast_queue.log'
echo "PAIRFAST QUEUE DONE" >> logs/pairfast_queue.log
