#!/bin/bash
# lab PC SAT lanes (note 45): each line of the task file = "<types json> <index> <seconds> [flags]" -> local_tier_probe.py
# usage: bash scripts/local_sat_queue.sh <taskfile> <parallel lanes>      results: PROBE lines in logs/tier_probe.log
cd "$(dirname "$0")/.."
T=/c/home/researcher/Desktop/c2_experimental/scripts/c1_tiers
grep -v '^$' "$1" | xargs -P "$2" -I{} bash -c "set -- {}; .venv/Scripts/python.exe scripts/local_tier_probe.py $T $T/data/\$1 \$2 \$3 \${@:4} >> logs/tier_probe.log 2>&1"
echo "SAT QUEUE DONE $1" >> logs/tier_probe.log
