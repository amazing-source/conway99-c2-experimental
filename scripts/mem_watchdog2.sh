#!/bin/bash
# Surveillance memoire, version 2 : lecture toutes les 20 s ; on arrete les conteneurs du labo seulement si la memoire libre
# reste sous 3 Go sur DEUX lectures consecutives (baisse soutenue, >= 20 s). Une baisse passagere due aux autres applications
# ne tue plus un calcul de 65 Mo qui n'en est pas la cause. Journal : logs/mem_watchdog.txt.
end=$(( $(date +%s) + ${1:-7200} ))
low=0
while [ $(date +%s) -lt $end ]; do
  free=$(powershell -NoProfile -Command "[int]((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)")
  if [ "${free:-9999}" -lt 3072 ]; then low=$((low+1)); else low=0; fi
  if [ $low -eq 1 ]; then echo "$(date '+%H:%M:%S') memoire libre ${free} Mo < 3072 (1re lecture, on attend la suivante)" >> logs/mem_watchdog.txt; fi
  if [ $low -ge 2 ]; then
    echo "$(date '+%H:%M:%S') memoire libre ${free} Mo < 3072 (soutenue) : arret des conteneurs" >> logs/mem_watchdog.txt
    for c in $(docker ps -q --filter ancestor=satbox-proof); do docker stop -t 2 "$c" >/dev/null 2>&1; done
    low=0
  fi
  sleep 20
done
