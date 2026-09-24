#!/bin/bash
# Sous-cubes (mu, tau) de l'etoile libre, une seule voie ; attend 4 Go libres avant chaque cube (notes/22).
cd /c/home/researcher/Desktop/c2_experimental
for n in "$@"; do
  if grep -q "^$n " data/cert_results.txt 2>/dev/null; then continue; fi
  while true; do
    free=$(powershell -NoProfile -Command "[int]((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)")
    [ "${free:-0}" -ge 4000 ] && break
    sleep 60
  done
  MSYS_NO_PATHCONV=1 docker run --rm --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-proof bash /lab/scripts/cert_run.sh "$n" 900
done
echo FIN
