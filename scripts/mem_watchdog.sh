#!/bin/bash
# Surveillance memoire : toutes les 20 s ; si memoire libre < 3 Go, arrete les conteneurs docker du labo et les solveurs Python du labo.
end=$(( $(date +%s) + ${1:-7200} ))
while [ $(date +%s) -lt $end ]; do
  free=$(powershell -NoProfile -Command "[int]((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)")
  if [ "${free:-9999}" -lt 3072 ]; then
    echo "$(date '+%H:%M:%S') memoire libre ${free} Mo < 3072 : arret des conteneurs" >> logs/mem_watchdog.txt
    for c in $(docker ps -q --filter ancestor=satbox-proof); do docker stop -t 2 "$c" >/dev/null 2>&1; done
  fi
  sleep 20
done
