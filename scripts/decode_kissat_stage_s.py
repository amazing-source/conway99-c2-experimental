"""Decode une solution kissat de data/cnf/stage_s_alone.cnf (variables P_op = 2k+1, M_op = 2k+2 pour la k-ieme paire o<p).
Verifie S C = 0 et S^2 + S = 12I - CC^T exactement, calcule rang_7(S - 3I) (49x49) et rang_7(S_out - 3I), ecrit un json
compatible avec extend_s_to_q.py.  Usage : python decode_kissat_stage_s.py logs/night_C_kissat.log out.json"""
import sys, json, os
import numpy as np
LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(LAB, "scripts"))
from padic import rank_mod_p
m = 7
orb = [(i, j, t) for i in range(m) for j in range(i + 1, m) for t in (1, -1)]
N = len(orb)
C = np.zeros((N, m), dtype=int)
for o, (i, j, t) in enumerate(orb): C[o, i] = 1; C[o, j] = t
G = C @ C.T
val = set()
sat = False
for line in open(sys.argv[1], encoding="utf-8", errors="ignore"):
    if line.startswith("s SATISFIABLE"): sat = True
    if line.startswith("v "):
        for x in line.split()[1:]:
            x = int(x)
            if x > 0: val.add(x)
if not sat:
    print("pas de solution dans ce journal"); sys.exit(0)
S = np.zeros((N, N), dtype=int); k = 0
for o in range(N):
    for p in range(o + 1, N):
        Pv, Mv = 2 * k + 1, 2 * k + 2
        s = (1 if Pv in val else 0) - (1 if Mv in val else 0)
        S[o, p] = S[p, o] = s; k += 1
ok1 = (S @ C == 0).all(); ok2 = (S @ S + S == 12 * np.eye(N, dtype=int) - G).all()
print("S C = 0 :", ok1, " S^2 + S = 12I - G :", ok2)
Sf = np.zeros((49, 49), dtype=int); Sf[:7, :7] = -np.eye(7, dtype=int); Sf[:7, 7:] = C.T; Sf[7:, :7] = C; Sf[7:, 7:] = S
print("rang_7(S - 3I) =", rank_mod_p((Sf - 3 * np.eye(49, dtype=int)) % 7, 7), "(theoreme : pair)",
      "  rang_7(S_out - 3I) =", rank_mod_p((S - 3 * np.eye(N, dtype=int)) % 7, 7), "(theoreme : pair)")
json.dump({"orb": orb, "S_out": S.tolist(), "m": 7}, open(sys.argv[2], "w"))
print("ecrit :", sys.argv[2], "-> lancer scripts/extend_s_to_q.py", sys.argv[2])
