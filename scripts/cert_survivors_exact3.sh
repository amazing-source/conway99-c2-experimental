#!/bin/bash
# P5 et 2P3 en Sigma EXACT (la semantique « au moins » a donne UNKNOWN a 600 s), apres le lot exact2.
cd /c/home/researcher/Desktop/c2_experimental
until grep -q FIN logs/cert_survivors_exact2.out 2>/dev/null; do sleep 20; done
while [ -n "$(docker ps -q --filter ancestor=satbox-proof)" ]; do sleep 15; done
for n in survx_P5 survx_2P3; do
  MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$n" 600
done
echo FIN
