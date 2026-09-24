#!/bin/bash
# Attend la fin du lot rsf (3 lignes dans logs/cert_rsf_batch2.out), puis certifie les 18 CNF du lemme des etoiles, un conteneur a la fois.
cd /c/home/researcher/Desktop/c2_experimental
until [ "$(wc -l < logs/cert_rsf_batch2.out 2>/dev/null || echo 0)" -ge 3 ]; do sleep 20; done
for f in $(awk '{print $2}' data/cnf/MANIFEST_starfacts.txt | sed 's/\.cnf$//'); do
  MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$f" 600
done
echo FIN
