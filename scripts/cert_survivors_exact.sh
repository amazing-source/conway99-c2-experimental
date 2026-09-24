#!/bin/bash
# Survivants a 3 aretes, Sigma EXACT (paires hors Sigma interdites soeurs), modele complet, kissat 600 s + DRAT si UNSAT.
cd /c/home/researcher/Desktop/c2_experimental
until grep -q FIN logs/cert_survivors.out 2>/dev/null; do sleep 20; done
while [ -n "$(docker ps -q --filter ancestor=satbox-proof)" ]; do sleep 15; done
for n in survx_K3 survx_P4 survx_P3K2 survx_3K2; do
  MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$n" 600
done
echo FIN
