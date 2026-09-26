#!/bin/bash
# Root-first test (note 44): orientation-level orbit LP (all D variable) for a sample of jobs of a filtered class.
cd /c/home/researcher/Desktop/c2_experimental
ci=$1; shift
for job in "$@"; do
  SMOOTH=0.6 TL=5000 .venv/Scripts/python.exe scripts/orbit_fixcamp.py $ci $job 1 > logs/root_test_${ci}_${job}.out 2>&1
  echo "$ci $job: $(grep '^FIXCAMP' logs/root_test_${ci}_${job}.out | cut -c1-100)" >> logs/root_test.log
done
echo "ROOT SAMPLE DONE $ci" >> logs/root_test.log
