#!/bin/bash
# Modele complet (au moins ces paires soeurs), kissat 600 s + DRAT si UNSAT, un conteneur a la fois, apres les autres lots.
cd /c/home/researcher/Desktop/c2_experimental
while [ -n "$(docker ps -q --filter ancestor=satbox-proof)" ]; do sleep 15; done
for n in surv_C4 surv_P5 surv_P4K2 surv_2P3; do
  MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$n" 600
done
echo FIN
