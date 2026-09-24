#!/bin/bash
# Reprise du lot « etoile libre » sur UNE seule voie (la memoire libre est passee sous 3 Go avec deux conteneurs a 17:37-17:58).
cd /c/home/researcher/Desktop/c2_experimental
for n in fs_P5 fs_3K2 fs_vide; do
  free=$(powershell -NoProfile -Command "[int]((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)")
  if [ "${free:-0}" -lt 3800 ]; then echo "$n SAUTE (memoire libre ${free} Mo)"; continue; fi
  MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$n" 900
done
echo FIN
