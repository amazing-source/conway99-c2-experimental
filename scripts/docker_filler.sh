#!/bin/bash
# Lab PC lane filler for Docker SAT runs (note 45), ACTIVITY-AWARE (user rule 27/09: busy PC -> low mode): starts the next task line
# ("<cnf rel to sat/> <secs> [solver] [proof]") only when logs/pc_mode.txt says 'high' (cap_auto.ps1) and fewer than MAX jobs compute
# (python base processes of orbit_fixcamp/root_job/iota_dfs + sat_* containers). Starts Docker Desktop if needed (high mode only).
# usage: bash scripts/docker_filler.sh <taskfile> [MAX=10]        started lines -> <taskfile>.started
cd "$(dirname "$0")/.."
TF=$1; MAX=${2:-10}; ST=$TF.started; touch "$ST"
requeue() {   # runs cut short (Docker stopped by the activity watcher: verdict 'UNKNOWN (rc )', no container left) go back to the queue
  running=$(docker ps -a --filter "name=sat_" --format '{{.Names}}' 2>/dev/null)
  : > "$ST.keep"
  while read -r l; do
    [ -z "$l" ] && continue; set -- $l
    nm=$(echo "${1%.cnf}" | tr '/' '_')_${3:-kissat}$( [ "$4" = proof ] && echo _proof )
    last=$(grep "^DOCKERSAT $nm:" logs/tier_probe.log 2>/dev/null | tail -n 1)
    if echo "$last" | grep -q "UNKNOWN (rc )" && ! echo "$running" | grep -q "sat_$nm"; then echo "$(date +%H:%M) requeued (interrupted): $l" >> logs/docker_filler.log
    else echo "$l" >> "$ST.keep"; fi
  done < "$ST"
  mv "$ST.keep" "$ST"
}
while true; do
  requeue
  next=$(grep -v '^$' "$TF" | grep -v -x -F -f "$ST" | head -n 1)
  [ -z "$next" ] && break
  if [ "$(tr -d '\r\n ' < logs/pc_mode.txt 2>/dev/null)" != "high" ]; then sleep 60; continue; fi
  if ! docker info > /dev/null 2>&1; then
    powershell -NoProfile -Command "Start-Process 'C:\Program Files\Docker\Docker\Docker Desktop.exe'" > /dev/null 2>&1
    echo "$(date +%H:%M) high mode: starting Docker Desktop" >> logs/docker_filler.log; sleep 90; continue
  fi
  np=$(powershell -NoProfile -Command "@(Get-CimInstance Win32_Process -Filter \"name='python.exe'\" | Where-Object { (\$_.CommandLine -match 'Python312' -and \$_.CommandLine -match 'orbit_fixcamp|root_job|iota_dfs') -or \$_.CommandLine -match 'multiprocessing.spawn' }).Count" | tr -d '\r')
  nd=$(docker ps -q --filter "name=sat_" 2>/dev/null | wc -l)
  if [ -n "$np" ] && [ $(( np + nd )) -lt "$MAX" ]; then
    echo "$next" >> "$ST"; nohup bash scripts/docker_sat.sh $next > /dev/null 2>&1 &
    echo "$(date +%H:%M) started: $next (python $np + docker $nd)" >> logs/docker_filler.log; sleep 20
  else sleep 60; fi
done
echo "DOCKER FILLER DONE $TF" >> logs/tier_probe.log
