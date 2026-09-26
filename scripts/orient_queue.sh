#!/bin/bash
# Orientation-first campaign (note 43) on the classes not filtered (15, 16, 18-46), ONE lane, classes with fewest orientations first.
# Each class: orient_campaign.py (resumable: done indices are skipped).  Env TL, LOWMEM passed through.
cd /c/home/researcher/Desktop/c2_experimental
for c in ${CLASSES:-22 46 42 44 45 41 17 37 39 43 34 40 27 23 15 28 38 30 32 33 36 24 35 19 21 18 31 29 16 26 25 20}; do
  [ "$c" = "17" ] && continue
  .venv/Scripts/python.exe scripts/orient_campaign.py $c ${K0:-0} ${KK:-1} >> logs/orient_queue.log 2>&1
  echo "CLASS $c DONE $(grep -c '"dead"' logs/orient_$c.jsonl) dead $(grep -c '"feasible"' logs/orient_$c.jsonl) feasible $(grep -c -E '"timeout"|"certfail"' logs/orient_$c.jsonl) other" >> logs/orient_queue.log
done
echo "ORIENT QUEUE DONE" >> logs/orient_queue.log
