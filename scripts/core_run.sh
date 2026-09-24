#!/bin/bash
# Dans satbox-proof : bash /lab/scripts/core_run.sh <nom> <secondes_kissat>
# kissat + preuve DRAT ; si UNSAT, drat-trim avec extraction du NOYAU (clauses originales utilisees) -> /lab/data/tmp/<nom>.core.cnf
set -u
name="$1"; tl="$2"
cnf="/lab/data/cnf/${name}.cnf"
work="/tmp/core_${name}"; mkdir -p "$work"
proof="$work/${name}.drat"
kissat --time="$tl" "$cnf" "$proof" > "/lab/logs/core_${name}.kissat.log" 2>&1
ex=$?
if [ $ex -eq 20 ]; then
  mkdir -p /lab/data/tmp
  drat-trim "$cnf" "$proof" -t 40000 -c "/lab/data/tmp/${name}.core.cnf" > "/lab/logs/core_${name}.drat.log" 2>&1
  v=$(tr '\r' '\n' < "/lab/logs/core_${name}.drat.log" | grep -m1 "^s ")
  echo "$name kissat=$ex drat: $v core_lines=$(wc -l < /lab/data/tmp/${name}.core.cnf)"
else
  echo "$name kissat=$ex (pas UNSAT)"
fi
rm -f "$proof"
