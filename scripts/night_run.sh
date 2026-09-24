#!/bin/bash
# Programme de nuit (24/09/2026) — charge plafonnee a ~8 fils sur 16, priorite basse.
# A : etage S + couplage D + sommes par bloc (CP-SAT, 4 fils)      -> UNSAT tuerait C2
# B : etage S seul (CP-SAT, 2 fils)                                 -> UNSAT tuerait C2 ; SAT -> test de parite + completion S->D
# C : etage S seul (kissat, 1 fil, sans preuve)
# D : etage S seul apres BreakID (kissat, 1 fil, sans preuve)
LAB=/c/home/researcher/Desktop/c2_experimental
PY=$LAB/.venv/Scripts/python.exe
T=25200
cd $LAB
echo "lancement $(date)" > logs/night_status.txt
nohup $PY scripts/stage_s_alone.py $T 4 3 none blocks > logs/night_A_blocks_cpsat.log 2>&1 &
echo "A pid $!" >> logs/night_status.txt
nohup $PY scripts/stage_s_alone.py $T 2 7 none > logs/night_B_s_alone_cpsat.log 2>&1 &
echo "B pid $!" >> logs/night_status.txt
MSYS_NO_PATHCONV=1 docker run -d --name night_C --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-breakid \
  sh -c "kissat --seed=1 --time=$T /lab/data/cnf/stage_s_alone.cnf > /lab/logs/night_C_kissat.log 2>&1; echo exit=\$? >> /lab/logs/night_C_kissat.log" >> logs/night_status.txt
MSYS_NO_PATHCONV=1 docker run -d --name night_D --cpus=1 -v "C:/home/researcher/Desktop/c2_experimental:/lab" satbox-breakid \
  sh -c "breakid /lab/data/cnf/stage_s_alone.cnf /lab/data/cnf/stage_s_alone_breakid.cnf > /lab/logs/night_D_breakid.log 2>&1; kissat --seed=2 --time=$T /lab/data/cnf/stage_s_alone_breakid.cnf > /lab/logs/night_D_kissat.log 2>&1; echo exit=\$? >> /lab/logs/night_D_kissat.log" >> logs/night_status.txt
echo "lance" >> logs/night_status.txt
