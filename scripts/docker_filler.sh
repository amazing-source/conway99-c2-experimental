#!/bin/bash
# Lab PC lane filler for Docker SAT runs (note 45): starts the next task line ("<cnf rel to sat/> <secs> [solver] [proof]")
# whenever fewer than MAX jobs compute (python base processes of orbit_fixcamp/root_job/iota_dfs + running sat_* containers).
# usage: bash scripts/docker_filler.sh <taskfile> [MAX=12]        started lines -> <taskfile>.started
cd "$(dirname "$0")/.."
TF=$1; MAX=${2:-12}; ST=$TF.started; touch "$ST"
while true; do
  next=$(grep -v '^$' "$TF" | grep -v -x -F -f "$ST" | head -n 1)
  [ -z "$next" ] && break
  np=$(powershell -NoProfile -Command "@(Get-CimInstance Win32_Process -Filter \"name='python.exe'\" | Where-Object { (\$_.CommandLine -match 'Python312' -and \$_.CommandLine -match 'orbit_fixcamp|root_job|iota_dfs') -or \$_.CommandLine -match 'multiprocessing.spawn' }).Count" | tr -d '\r')
  nd=$(docker ps -q --filter "name=sat_" 2>/dev/null | wc -l)
  if [ -n "$np" ] && [ $(( np + nd )) -lt "$MAX" ]; then
    echo "$next" >> "$ST"; nohup bash scripts/docker_sat.sh $next > /dev/null 2>&1 &
    echo "$(date +%H:%M) started: $next (python $np + docker $nd)" >> logs/docker_filler.log; sleep 20
  else sleep 60; fi
done
echo "DOCKER FILLER DONE $TF" >> logs/tier_probe.log
