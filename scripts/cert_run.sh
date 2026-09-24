#!/bin/bash
# Run inside satbox-proof:  bash /lab/scripts/cert_run.sh <name> <kissat_seconds>
# kissat (statistics on) with a binary DRAT proof; if UNSAT, check with drat-trim; keep only the proof's size and sha256.
# Result line appended to /lab/data/cert_results.txt :
#   name verdict kissat_exit seconds conflicts drat=<VERIFIED|FAILED|NA> proof_bytes proof_sha256 cnf_sha256
set -u
name="$1"; tl="$2"
cnf="/lab/data/cnf/${name}.cnf"
work="/tmp/cert_${name}"; mkdir -p "$work"
log="/lab/logs/cert_${name}.kissat.log"
proof="$work/${name}.drat"
cnfsha=$(sha256sum "$cnf" | cut -d' ' -f1)
start=$(date +%s)
kissat --time="$tl" "$cnf" "$proof" > "$log" 2>&1
ex=$?
end=$(date +%s)
conf=$(grep -m1 "^c conflicts:" "$log" | awk '{print $3}')
verdict=UNKNOWN; [ $ex -eq 20 ] && verdict=UNSAT; [ $ex -eq 10 ] && verdict=SAT
drat=NA; psize=0; psha=NA
if [ $ex -eq 20 ]; then
  psize=$(stat -c %s "$proof"); psha=$(sha256sum "$proof" | cut -d' ' -f1)
  drat-trim "$cnf" "$proof" -t 40000 > "/lab/logs/cert_${name}.drat.log" 2>&1
  if tr '\r' '\n' < "/lab/logs/cert_${name}.drat.log" | grep -q "^s VERIFIED"; then drat=VERIFIED; else drat=FAILED; fi
fi
rm -f "$proof"
echo "$name $verdict $ex $((end-start)) ${conf:-NA} drat=$drat $psize $psha $cnfsha" >> /lab/data/cert_results.txt
echo "$name $verdict $ex $((end-start)) ${conf:-NA} drat=$drat"
