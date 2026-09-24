#!/bin/bash
# 11 cubes du lemme de l'etoile libre : kissat 900 s + DRAT si UNSAT, deux voies (1 CPU chacune).
cd /c/home/researcher/Desktop/c2_experimental
lane() { for n in "$@"; do MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$n" 900; done; }
lane freestar_A111111 freestar_A21111 freestar_A2211 freestar_A222 freestar_A3111 freestar_A321 > logs/cert_freestar_cubes_A.out 2>&1 &
lane freestar_A33 freestar_A411 freestar_A42 freestar_A51 freestar_A6 > logs/cert_freestar_cubes_B.out 2>&1 &
wait
echo FIN > logs/cert_freestar_cubes.done
