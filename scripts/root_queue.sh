#!/bin/bash
# root-first queue (note 44): orientation-level root LP (root_job.py) for each "ci rep" line of a task file, one lane,
# skipping reps whose logs/root/root_<ci>_<rep>.json exists.   usage: bash scripts/root_queue.sh <taskfile>   log: logs/root_queue.log
cd "$(dirname "$0")/.."
while read -r ci r; do
  [ -z "$ci" ] || [ -f logs/root/root_${ci}_$r.json ] && continue
  SMOOTH=0.6 LOWMEM=1 TL=6000 .venv/Scripts/python.exe scripts/root_job.py $ci $r >> logs/root_queue.log 2>&1
done < "$1"
echo "ROOT QUEUE DONE $1" >> logs/root_queue.log
