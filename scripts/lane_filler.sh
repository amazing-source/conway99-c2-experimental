#!/bin/bash
# Lab PC lane filler (note 45): starts the next line of a task file ("<types json> <index> <seconds> [flags]" -> local_tier_probe.py)
# whenever fewer than MAX jobs are computing (orbit_fixcamp / root_job / iota_dfs base processes + SAT probe children).
# Started lines are recorded in <taskfile>.started.   usage: bash scripts/lane_filler.sh <taskfile> [MAX=12]
cd "$(dirname "$0")/.."
TF=$1; MAX=${2:-12}; ST=$TF.started; touch "$ST"
T=/c/home/researcher/Desktop/c2_experimental/scripts/c1_tiers
while true; do
  next=$(grep -v '^$' "$TF" | grep -v -x -F -f "$ST" | head -n 1)
  [ -z "$next" ] && break
  n=$(powershell -NoProfile -Command "@(Get-CimInstance Win32_Process -Filter \"name='python.exe'\" | Where-Object { (\$_.CommandLine -match 'Python312' -and \$_.CommandLine -match 'orbit_fixcamp|root_job|iota_dfs') -or \$_.CommandLine -match 'multiprocessing.spawn' }).Count" | tr -d '\r')
  if [ -n "$n" ] && [ "$n" -lt "$MAX" ]; then
    echo "$next" >> "$ST"; set -- $next
    nohup .venv/Scripts/python.exe scripts/local_tier_probe.py $T $T/data/$1 $2 $3 ${@:4} >> logs/tier_probe.log 2>&1 &
    echo "$(date +%H:%M) started: $next (computing jobs before: $n)" >> logs/lane_filler.log
    sleep 30
  else sleep 60; fi
done
echo "LANE FILLER DONE $TF" >> logs/tier_probe.log
