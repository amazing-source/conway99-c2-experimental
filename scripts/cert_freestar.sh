#!/bin/bash
# « lignes soeurs + etoile d'un bloc libre », Sigma exact : kissat 900 s + DRAT si UNSAT ; deux voies en parallele (1 CPU chacune).
cd /c/home/researcher/Desktop/c2_experimental
lane() { for n in "$@"; do MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$n" 900; done; }
lane fs_C4 fs_P5 fs_P3K2 fs_K3 fs_P3 fs_vide > logs/cert_freestar_A.out 2>&1 &
lane fs_2P3 fs_3K2 fs_P4 fs_2K2 fs_K2 > logs/cert_freestar_B.out 2>&1 &
wait
echo FIN > logs/cert_freestar.done
