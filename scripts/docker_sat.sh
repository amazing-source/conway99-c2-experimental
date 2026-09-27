#!/bin/bash
# One SAT run in Docker (note 45): kissat or cadical (tools/linux, built in gcc:13) on sat/<cnf>, time cap, optional DRAT proof
# checked by drat-trim inside the container.  One CPU, 4 GB cap.  Verdict line -> logs/tier_probe.log ("DOCKERSAT name: ...").
# usage: bash scripts/docker_sat.sh <cnf path relative to sat/> <secs> [kissat|cadical] [proof]
cd "$(dirname "$0")/.."
cnf=$1; secs=$2; solver=${3:-kissat}; proof=$4
name=$(echo "${cnf%.cnf}" | tr '/' '_')_$solver$( [ "$proof" = proof ] && echo _proof )
out=sat/out/$name.out; t0=$(date +%s)
if [ "$proof" = proof ]; then
  inner="timeout $secs /t/$solver -q /sat/$cnf /tmp/p.drat > /sat/out/$name.out 2>&1; rc=\$?; echo rc=\$rc >> /sat/out/$name.out; if [ \$rc = 20 ]; then echo proof_bytes=\$(stat -c %s /tmp/p.drat) >> /sat/out/$name.out; /t/drat-trim /sat/$cnf /tmp/p.drat -t 400000 > /sat/out/$name.drattrim 2>&1; fi"
else
  inner="timeout $secs /t/$solver -q /sat/$cnf > /sat/out/$name.out 2>&1; echo rc=\$? >> /sat/out/$name.out"
fi
MSYS_NO_PATHCONV=1 docker run --rm --name "sat_$name" --cpus=1 --memory=4g -v "C:/home/researcher/Desktop/c2_experimental/sat:/sat" -v "C:/home/researcher/Desktop/c2_experimental/tools/linux:/t" gcc:13 bash -c "$inner" > /dev/null 2>&1
rc=$(grep -o 'rc=[0-9]*' "$out" 2>/dev/null | tail -n 1 | cut -d= -f2)
st=UNKNOWN; [ "$rc" = 20 ] && st=UNSAT; [ "$rc" = 10 ] && st=SAT
v=""; [ -f "sat/out/$name.drattrim" ] && v=" drat-trim: $(grep -o 's VERIFIED\|s NOT VERIFIED' sat/out/$name.drattrim | head -1), $(grep -o 'proof_bytes=[0-9]*' "$out")"
echo "DOCKERSAT $name: $st (rc $rc) $(( $(date +%s) - t0 ))s$v" >> logs/tier_probe.log
