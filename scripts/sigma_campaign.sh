#!/bin/bash
# v6 filter for the sister patterns (C1's request, note 43): one lane, tasks from logs/sigma_tasks.txt ('<T> <Sigma>').
# BUDGET (s, default 900) per task; a task is skipped if its output exists and is complete ("done": true); an output with
# "done": false (time cap) is re-run only when BUDGET exceeds the budget it had (recorded in logs/sigma_budget/<file>).
cd /c/home/researcher/Desktop/c2_experimental
B=${BUDGET:-900}; mkdir -p logs/sigma_budget
while read -r T S; do
  ci=$T; [ "$T" = "none" ] && ci="edges="
  tag=$( [ "$T" = "none" ] && echo E || echo "E${T#edges=}" | tr "," "_" )
  base="mix6_cls_${tag}_S$(echo $S | tr -d ',' | sed 's/\(..\)/\1_/g; s/_$//')_0.json"; out="logs/$base"
  if [ -f "$out" ]; then
    grep -q '"done": true' "$out" && continue
    prev=$(cat "logs/sigma_budget/$base" 2>/dev/null || echo 0); [ "$B" -le "$prev" ] && continue
  fi
  t0=$(date +%s)
  line=$(.venv/Scripts/python.exe scripts/mix_filter6.py "$ci" 0 1 "$B" "$S" 2>&1 | tail -n 1)
  echo "$B" > "logs/sigma_budget/$base"
  echo "$T $S budget=$B $(( $(date +%s) - t0 ))s | $line" >> logs/sigma_filter.log
done < logs/sigma_tasks.txt
echo "SIGMA CAMPAIGN PASS DONE budget=$B" >> logs/sigma_filter.log
