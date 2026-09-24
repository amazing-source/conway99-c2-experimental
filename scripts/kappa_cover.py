"""Probleme kappa (note 23 §5) en couverture exacte a multiplicites (a la Knuth, algorithme M).
Objets : les 60 paires hors mu (chacune couverte exactement une fois) ; les cases (b, d), b <= d, de Ct :
  hors diagonale : couverte exactement Ct[b, d] fois, par les paires kappa {w, w'} avec b dans w et d dans w' (ou l'inverse) ;
  diagonale      : couverte exactement Ct[b, b] / 2 fois, par les paires kappa avec b dans w et dans w'.
Options : les 1 770 paires {w, w'}.  Branchement : l'objet qui a le moins d'options vivantes ; pour une case, « on prend A_i et on
exclut A_1..A_{i-1} » (exhaustif, sans doublon).  Reponse DEFINITIVE : nombre exact de solutions (et les premieres).
Usage : python kappa_cover.py <partition mu> <indices tau> [cap_solutions] [node_cap]
"""
import sys, os, time
import numpy as np
from numba import njit
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types

def build(mu, Ct):
    P = [(a, b) for a in range(12) for b in range(a + 1, 12) if mu[a] != b]
    assert len(P) == 60
    ent = {}
    for b in range(12):
        for d in range(b, 12):
            ent[(b, d)] = len(ent)
    need = np.zeros(len(ent), dtype=np.int64)
    for (b, d), k in ent.items():
        need[k] = Ct[b, d] // 2 if b == d else Ct[b, d]
        if b == d: assert Ct[b, d] % 2 == 0
        else: assert Ct[b, d] == Ct[d, b]
    opts_w = []; opts_e = []
    for i in range(60):
        for j in range(i + 1, 60):
            w, v = P[i], P[j]
            cov = {}
            for u in w:
                for x in v:
                    if u == x:
                        k = ent[(u, u)]; cov[k] = cov.get(k, 0) + 1
                    else:
                        k = ent[(min(u, x), max(u, x))]; cov[k] = cov.get(k, 0) + 1
            if any(c > 1 for c in cov.values()):
                raise ValueError("couverture > 1 inattendue")
            opts_w.append((i, j)); opts_e.append(sorted(cov))
    OW = np.array(opts_w, dtype=np.int64)
    OE = -np.ones((len(opts_e), 4), dtype=np.int64)
    for o, l in enumerate(opts_e):
        OE[o, :len(l)] = l
    return P, need, OW, OE, len(ent)

@njit(cache=True)
def live(o, OW, OE, used, dead, rem):
    if dead[o] or used[OW[o, 0]] or used[OW[o, 1]]: return False
    for t in range(4):
        k = OE[o, t]
        if k >= 0 and rem[k] <= 0: return False
    return True

@njit(cache=True)
def solve(OW, OE, need, nent, cap, node_cap):
    no = OW.shape[0]
    used = np.zeros(60, dtype=np.bool_)
    dead = np.zeros(no, dtype=np.bool_)
    rem = need.copy()
    chosen = np.zeros(30, dtype=np.int64); nch = 0
    sols = np.zeros((cap, 30), dtype=np.int64); nsol = 0; nodes = 0
    # pile : pour chaque niveau, la liste d'options de branchement, l'indice courant, et la pile des "morts" ajoutes
    lvl_opts = np.zeros((31, no), dtype=np.int64); lvl_n = np.zeros(31, dtype=np.int64); lvl_i = np.zeros(31, dtype=np.int64)
    dead_stack = np.zeros(no * 31, dtype=np.int64); dead_top = 0
    lvl_dead_base = np.zeros(31, dtype=np.int64)
    cntw = np.zeros(60, dtype=np.int64); cnte = np.zeros(nent, dtype=np.int64)
    depth = 0; fresh = True
    while True:
        if fresh:
            nodes += 1
            if nodes > node_cap: return sols, nsol, nodes, False
            if nch == 30:
                ok = True
                for k in range(nent):
                    if rem[k] != 0: ok = False
                if ok:
                    if nsol < cap: sols[nsol, :] = chosen
                    nsol += 1
                depth -= 1
                if depth < 0: break
                fresh = False
                continue
            # compter les options vivantes par objet
            for i in range(60): cntw[i] = 0
            for k in range(nent): cnte[k] = 0
            for o in range(no):
                if live(o, OW, OE, used, dead, rem):
                    cntw[OW[o, 0]] += 1; cntw[OW[o, 1]] += 1
                    for t in range(4):
                        k = OE[o, t]
                        if k >= 0: cnte[k] += 1
            best = -1; bestv = 10 ** 9; bestkind = 0
            fail = False
            for i in range(60):
                if not used[i]:
                    if cntw[i] == 0: fail = True; break
                    if cntw[i] < bestv: bestv = cntw[i]; best = i; bestkind = 0
            if not fail:
                for k in range(nent):
                    if rem[k] > 0:
                        if cnte[k] < rem[k]: fail = True; break
                        v = cnte[k] - rem[k] + 1
                        if v < bestv: bestv = v; best = k; bestkind = 1
            if fail:
                depth -= 1
                if depth < 0: break
                fresh = False
                continue
            n = 0
            for o in range(no):
                if live(o, OW, OE, used, dead, rem):
                    if bestkind == 0:
                        if OW[o, 0] == best or OW[o, 1] == best:
                            lvl_opts[depth, n] = o; n += 1
                    else:
                        hit = False
                        for t in range(4):
                            if OE[o, t] == best: hit = True
                        if hit:
                            lvl_opts[depth, n] = o; n += 1
            if bestkind == 1:
                n = n - rem[best] + 1        # au-dela, pas assez d'options restantes pour la case
            lvl_n[depth] = n; lvl_i[depth] = -1; lvl_dead_base[depth] = dead_top
            fresh = False
        # retirer l'option courante du niveau, la marquer morte (exclusion pour les branches suivantes), passer a la suivante
        i = lvl_i[depth]
        if i >= 0:
            o = lvl_opts[depth, i]
            used[OW[o, 0]] = False; used[OW[o, 1]] = False
            for t in range(4):
                k = OE[o, t]
                if k >= 0: rem[k] += 1
            nch -= 1
            dead[o] = True; dead_stack[dead_top] = o; dead_top += 1
        i += 1
        lvl_i[depth] = i
        if i >= lvl_n[depth]:
            # niveau epuise : ressusciter les options tuees a ce niveau
            while dead_top > lvl_dead_base[depth]:
                dead_top -= 1; dead[dead_stack[dead_top]] = False
            depth -= 1
            if depth < 0: break
            continue
        o = lvl_opts[depth, i]
        used[OW[o, 0]] = True; used[OW[o, 1]] = True
        for t in range(4):
            k = OE[o, t]
            if k >= 0: rem[k] -= 1
        chosen[nch] = o; nch += 1
        depth += 1; fresh = True
    return sols, nsol, nodes, True

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); which = [int(x) for x in sys.argv[2].split(",")]
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    node_cap = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 13
    mu, reps, st = types(part)
    for ti in which:
        tau = reps[ti]
        Cx, Ct = targets(mu, tau, 12)
        P, need, OW, OE, nent = build(mu, Ct)
        t0 = time.time()
        sols, nsol, nodes, done = solve(OW, OE, need, nent, cap, node_cap)
        print("A%s tau#%d : tau = %s ; %s ; solutions kappa = %d ; noeuds = %d ; %.1f s"
              % (sys.argv[1], ti, list(tau), "TERMINE" if done else "PLAFOND", nsol, nodes, time.time() - t0), flush=True)
        if nsol:
            np.save(os.path.join(HERE, "..", "logs", "kappa_cover_A%s_t%d.npy" % (sys.argv[1], ti)), sols[:min(nsol, cap)])
