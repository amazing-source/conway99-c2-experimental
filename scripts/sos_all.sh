cd /c/home/researcher/Desktop/c2_experimental
{
echo "== degre 2 (sos2_relax.py) =="
for m in 2 3 4 5 6 7; do .venv/Scripts/python.exe scripts/sos2_relax.py $m feas 2>&1 | grep -v "Warning\|prob.solve"; done
.venv/Scripts/python.exe scripts/sos2_relax.py 7 ysib_min 2>&1 | grep -v "Warning\|prob.solve" | tail -1
.venv/Scripts/python.exe scripts/sos2_relax.py 7 ysib_max 2>&1 | grep -v "Warning\|prob.solve" | tail -1
echo "== degre 2 + triangles de degre 3 (sos3_triangles.py) =="
for m in 2 3 4 5 6 7; do .venv/Scripts/python.exe scripts/sos3_triangles.py $m feas 2>&1 | grep -v "Warning\|prob.solve"; done
.venv/Scripts/python.exe scripts/sos3_triangles.py 7 ysib_min 2>&1 | grep -v "Warning\|prob.solve" | tail -1
.venv/Scripts/python.exe scripts/sos3_triangles.py 7 ysib_max 2>&1 | grep -v "Warning\|prob.solve" | tail -1
} > logs/sos_relax_summary.txt 2>&1
