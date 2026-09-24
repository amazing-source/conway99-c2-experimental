#!/bin/bash
# Deuxieme passe des cubes de l'etoile libre (notes/20) : attend la fin de la premiere passe (cert_freestar_cubes1.sh),
# puis relance, sur une seule voie, les cubes absents de data/cert_results.txt (cubes arretes par le garde-memoire).
cd /c/home/researcher/Desktop/c2_experimental
while ps -ef | grep -v grep | grep -q "cert_freestar_cubes1.sh"; do sleep 30; done
while [ -n "$(docker ps -q --filter ancestor=satbox-proof)" ]; do sleep 20; done
for n in freestar_A111111 freestar_A33 freestar_A21111 freestar_A411 freestar_A2211 freestar_A42 freestar_A222 freestar_A51 freestar_A3111 freestar_A6 freestar_A321; do
  if grep -q "^$n " data/cert_results.txt 2>/dev/null; then continue; fi
  while true; do
    free=$(powershell -NoProfile -Command "[int]((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)")
    [ "${free:-0}" -ge 4000 ] && break
    sleep 60
  done
  MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$n" 900
done
echo FIN
