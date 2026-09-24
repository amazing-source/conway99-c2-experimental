#!/bin/bash
# Survivants a 2 et 1 aretes, Sigma EXACT, modele complet, kissat 600 s + DRAT si UNSAT (apres le lot exact precedent).
cd /c/home/researcher/Desktop/c2_experimental
until grep -q FIN logs/cert_survivors_exact.out 2>/dev/null; do sleep 20; done
while [ -n "$(docker ps -q --filter ancestor=satbox-proof)" ]; do sleep 15; done
for n in survx_P3 survx_2K2 survx_K2; do
  MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$n" 600
done
echo FIN
