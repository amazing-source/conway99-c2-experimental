#!/bin/bash
# Noyaux DRAT de surv_C4 puis surv_P4K2 (apres les lots de survivants en cours, un conteneur a la fois).
cd /c/home/researcher/Desktop/c2_experimental
until grep -q FIN logs/cert_survivors_exact3.out 2>/dev/null; do sleep 30; done
while [ -n "$(docker ps -q --filter ancestor=satbox-proof)" ]; do sleep 15; done
for n in surv_P4K2 surv_C4; do
  MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/core_run.sh "$n" 900
done
echo FIN
