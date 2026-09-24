"""Region admissible (n3, z11) pour srg(99,14,1,2) d'apres les frequences d'ordre 7 de Reimbayev (arXiv 2608.19410).
On reconstruit chaque formule z_i depuis le texte extrait (fractions eclatees sur deux lignes), on l'evalue en n=99, k=14
sous la forme a + b n3 + c z11, puis on resout les PL min/max n3 sous z_i >= 0. Controle : m = 2 (n=9,k=4) et m = 11 (n=243,k=22)."""
import re, sys
from fractions import Fraction as F
import sympy as sp

txt = open(sys.argv[1] if len(sys.argv) > 1 else "downloads/reimbayev_order7.txt", encoding="utf-8").read()
lines = [l.strip() for l in txt.splitlines()]
# regrouper les formules : une formule commence par 'z<num> =' ; on concatene les lignes suivantes jusqu'a la prochaine
forms = {}; cur = None; buf = []
for l in lines:
    mm = re.match(r"^z(\d+)\s*=\s*(.*)$", l)
    if mm:
        if cur is not None: forms[cur] = buf
        cur = int(mm.group(1)); buf = [mm.group(2)]
    elif cur is not None:
        if l.startswith("===") or l.startswith("Figure") or re.match(r"^\d+$", l) and len(buf) > 0 and buf[-1].rstrip().endswith(","):
            forms[cur] = buf; cur = None; buf = []
        else:
            buf.append(l)
if cur is not None: forms[cur] = buf

n, k, N3, Z11 = sp.symbols("n k N3 Z11")
def to_expr(parts):
    s = "|".join(parts)
    s = s.split(",")[0] if "," in s else s
    s = s.replace("−", "-").replace("–", "-")
    s = s.replace("z11", "Z").replace("n3", "M")
    # fractions eclatees : 'a|b' ou 'Z|b' ou 'M|b' en fin de segment -> a/b
    s = re.sub(r"(\d+)\s*\|\s*(\d+)\s*([A-Za-z(])", r"(\1/\2)*\3", s)     # 1|4nk -> (1/4)*nk
    s = re.sub(r"(\d+)\s*\|\s*(\d+)\s*\*?\s*$", r"(\1/\2)", s)
    s = re.sub(r"([ZM])\s*\|\s*(\d+)", r"\1/\2", s)                          # Z|4 -> Z/4
    s = s.replace("|", " ")
    s = re.sub(r"k(\d)", r"k**\1", s)          # exposants
    s = re.sub(r"\)(\d)", r")**\1", s)
    s = s.replace("nk", "n*k")
    s = re.sub(r"(\d)\s*([A-Za-z(])", r"\1*\2", s)
    s = re.sub(r"\)\s*\(", ")*(", s)
    s = re.sub(r"([nkMZ])\s*\(", r"\1*(", s)
    s = re.sub(r"\)\s*([nkMZ])", r")*\1", s)
    s = s.replace("M", "N3").replace("Z", "Z11")
    return sp.sympify(s, locals={"n": n, "k": k, "N3": N3, "Z11": Z11})

exprs = {}
bad = []
for i, parts in sorted(forms.items()):
    try:
        exprs[i] = sp.expand(to_expr(parts))
    except Exception as e:
        bad.append((i, parts))
print("formules lues : %d / %d  (echecs : %s)" % (len(exprs), len(forms), [b[0] for b in bad][:20]))

def region(nv, kv):
    rows = []
    for i, e in exprs.items():
        ee = sp.expand(e.subs({n: nv, k: kv}))
        a = ee.subs({N3: 0, Z11: 0}); b = ee.coeff(N3); c = ee.coeff(Z11)
        rows.append((i, F(str(a)), F(str(b)), F(str(c))))
    return rows

from scipy.optimize import linprog
def lp(rows, obj):
    A = [[-float(b), -float(c)] for (_, a, b, c) in rows]; bb = [float(a) for (_, a, b, c) in rows]
    r = linprog(obj, A_ub=A, b_ub=bb, bounds=[(0, None), (0, None)], method="highs")
    return r
for (nv, kv, lab) in ((9, 4, "Paley(9)"), (243, 22, "BvLS"), (99, 14, "Conway-99")):
    rows = region(nv, kv)
    lo = lp(rows, [1, 0]); hi = lp(rows, [-1, 0])
    print("%-10s n3 in [%s, %s]" % (lab, lo.x[0] if lo.success else lo.message, -hi.fun if hi.success else hi.message))
    if lab == "Conway-99":
        tight = [(i, a, b, c) for (i, a, b, c) in rows if a < 5000 and (b < 0 or c < 0)]
        print("  contraintes 'petites' (constante < 5000, coefficient negatif) :")
        for t in tight: print("   z%d = %s + %s n3 + %s z11" % t)
