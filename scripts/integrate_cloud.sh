#!/bin/bash
# Integrate a cloud results branch (note 44 s.8): copy root records/certificates and stage-1 results into the lab, re-check every
# new orbit certificate independently (orbit_verify_certs.py), summarise root verdicts per class.
# usage: bash scripts/integrate_cloud.sh <branch>        log: logs/integrate_<branch-suffix>.log
cd "$(dirname "$0")/.."
B=$1; S=${B##*/}; P=/c/home/researcher/AppData/Local/Temp/claude/C--Users-RESEARCHER-Desktop/19a7c411-3446-4f59-9793-6c42892ed6cd/scratchpad/c2-compute
L=logs/integrate_$S.log; : > $L
git -C $P fetch -q origin "$B" || { echo "fetch failed" | tee -a $L; exit 1; }
mkdir -p logs/cloud_results/$S logs/root
git -C $P archive "origin/$B" logs | tar -x -C logs/cloud_results/$S
new=()
for f in logs/cloud_results/$S/logs/orbit_certs/*.json.gz; do
  [ -f "$f" ] || continue; b=$(basename $f)
  [ -f logs/orbit_certs/$b ] && cmp -s $f logs/orbit_certs/$b && continue
  cp $f logs/orbit_certs/$b; new+=(logs/orbit_certs/$b)
done
cp logs/cloud_results/$S/logs/root/*.json logs/root/ 2>/dev/null
echo "new certificates: ${#new[@]}" | tee -a $L
[ ${#new[@]} -gt 0 ] && .venv/Scripts/python.exe scripts/orbit_verify_certs.py "${new[@]}" >> $L 2>&1
echo "verify: $(grep -c ' VALID' $L) VALID, $(grep -c -i 'invalid\|error\|traceback' $L) problems" | tee -a $L
.venv/Scripts/python.exe - "$S" << 'PY' | tee -a $L
import json, glob, sys
from collections import Counter, defaultdict
S = sys.argv[1]; per = defaultdict(Counter)
for f in glob.glob("logs/cloud_results/%s/logs/root/*.json" % S):
    r = json.load(open(f)); per[r["ci"]][r["status"]] += 1
for ci in sorted(per): print("class %d roots: %s" % (ci, dict(per[ci])))
PY
