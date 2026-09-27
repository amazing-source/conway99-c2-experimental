#!/bin/bash
# Build the Linux SAT toolchain (note 45) into tools/linux with Docker (image gcc:13): cadical, kissat, drat-trim, lrat-check.
# Built 27/09 06:05: cadical 3.0.1, kissat 4.0.4 (git HEADs of that day). Runs in the same image (scripts/docker_sat.sh).
cd "$(dirname "$0")/.." && mkdir -p tools/linux
MSYS_NO_PATHCONV=1 docker run --rm --cpus=4 -v "$(pwd -W)/tools/linux:/out" gcc:13 bash -c 'set -e; cd /tmp
  git clone -q https://github.com/arminbiere/cadical.git && cd cadical && ./configure > /dev/null && make -j4 > /dev/null 2>&1 && cp build/cadical /out/ && cd /tmp
  git clone -q https://github.com/arminbiere/kissat.git && cd kissat && ./configure > /dev/null && make -j4 > /dev/null 2>&1 && cp build/kissat /out/ && cd /tmp
  git clone -q https://github.com/marijnheule/drat-trim.git && cd drat-trim && make > /dev/null 2>&1 && cp drat-trim lrat-check /out/
  /out/cadical --version; /out/kissat --version'
