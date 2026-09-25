"""Etoile libre + grilles soeurs ailleurs (note 23 §11).  Si {d, e} est une paire soeur (d, e != c), la grille G_de est un code
parfait (m = 7) : chaque sommet hors de G_de a exactement un voisin dans G_de.  Vu de l_c :
  (G1) les 4 images Phi(g), g = +-e_d +-e_e (racines lointaines de l_c), partitionnent les 8 elements de X hors des blocs d, e.
Modele : formulation compacte (i)-(iii) + (G1) pour une liste de paires soeurs + options (bal, iv, v) de freestar_sos.
CP-SAT 1 fil, reponses definitives seulement.
Usage : python freestar_grids.py <partition> <tau> <paires soeurs ex. 01,23,45 (blocs 0..5 de X)> <secondes>
"""
import sys, os, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortools.sat.python import cp_model
from freestar_compact import types, far_roots
import freestar_sos as FS

def add_grids(md, Zl, pairs_list, x, pairs_img, sis):
    for (d, e) in sis:
        g_idx = [z for z in range(len(Zl)) if {y // 2 for y in Zl[z]} == {d, e}]
        assert len(g_idx) == 4
        others = [y for y in range(12) if y // 2 not in (d, e)]
        # chaque element hors des blocs d, e est dans exactement une image ; aucun element des blocs d, e
        for y in range(12):
            lits = [x[z][p] for z in g_idx for p in range(len(pairs_img)) if y in pairs_img[p]]
            md.Add(sum(lits) == (1 if y in others else 0))

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); ti = int(sys.argv[2])
    sis = [(int(s[0]), int(s[1])) for s in sys.argv[3].split(",")] if sys.argv[3] != "-" else []
    T = float(sys.argv[4]); flags = sys.argv[5].split(",") if len(sys.argv) > 5 else ["bal", "iv", "v"]
    mu, reps, st = types(part); tau = reps[ti]
    md = FS.model(mu, tau, flags)
    # recuperer les variables x : reconstruire comme dans FS.model (meme ordre de creation)
    Ws = far_roots(7); Zl = [Ws[w][h] for w in range(len(Ws)) for h in (0, 1)]
    pairs_img = [p for p in itertools.combinations(range(12), 2) if mu[p[0]] != p[1]]
    nP = len(pairs_img)
    # les premieres variables creees par FS.model sont x[z][p], dans l'ordre z, p
    x = [[md.GetBoolVarFromProtoIndex(z * nP + p) for p in range(nP)] for z in range(len(Zl))]
    add_grids(md, Zl, None, x, pairs_img, sis)
    sv = cp_model.CpSolver(); sv.parameters.num_workers = 1; sv.parameters.max_time_in_seconds = T
    r = sv.Solve(md)
    print("A%s tau#%d tau=%s soeurs %s flags=%s : %s (%.1f s)" % (sys.argv[1], ti, list(tau), sis, ",".join(flags), sv.StatusName(r), sv.WallTime()), flush=True)
