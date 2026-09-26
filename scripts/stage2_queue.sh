#!/bin/bash
# Stage 2 of the mixture campaign (note 43): orbit block fixing (orbit_fixcamp.py, orbital branching) restricted to the leaves left
# open by stage 1 (OPEN=logs/pair_certs/open_<ci>_<job>.json); one lane by default; resumable (skips jobs with a FIXCAMP line).
cd /c/home/researcher/Desktop/c2_experimental
P=${P:-1}
grep -v '^$' logs/stage2_tasks.txt | while read -r ci job f; do
  o="logs/orbit_fixcamp_S2_${ci}_${job}.out"; [ -f "$o" ] && grep -q "^FIXCAMP" "$o" && continue
  echo "$ci $job $f"
done | xargs -P "$P" -L 1 bash -c 'OPEN=$2 SMOOTH=0.6 TL=5000 .venv/Scripts/python.exe scripts/orbit_fixcamp.py $0 $1 80 > logs/orbit_fixcamp_S2_$0_$1.out 2>&1; echo "$0 $1: $(tail -n 1 logs/orbit_fixcamp_S2_$0_$1.out | cut -c1-120)" >> logs/stage2_queue.log'
echo "STAGE2 QUEUE DONE" >> logs/stage2_queue.log
