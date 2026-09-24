"""Probleme kappa (note 23 §5) : la contrainte (iii) de la formulation compacte ne depend de Phi qu'a travers l'involution
kappa = Phi o neg o Phi^-1 des 60 paires hors mu.  (iii) <=> pour tous b, d :
    #{w paire hors mu : b dans w, d dans kappa(w)} = Ct[b, d].
Ce script enumere EXHAUSTIVEMENT les couplages parfaits kappa des 60 paires qui verifient ces comptes (DFS numba, choix de la
paire la plus contrainte, verification avant). Reponse definitive : liste (ou nombre) de solutions, ou aucune.
Usage : python kappa_search.py <partition mu, ex. 111111> <indices tau, ex. 0,1,2,3> [cap_solutions]
"""
import sys, os, time
import numpy as np
from numba import njit
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types

def pairs_non_mu(mu):
    P = [(a, b) for a in range(12) for b in range(a + 1, 12) if mu[a] != b]
    assert len(P) == 60
    return np.array(P, dtype=np.int64)

@njit(cache=True)
def _try(cnt, T, P, w, v, sgn):
    """ajoute (sgn=1) / retire (sgn=-1) la paire kappa {w, v} ; renvoie True si cnt <= T apres ajout."""
    ok = True
    for i in range(2):
        u = P[w, i]
        for j in range(2):
            x = P[v, j]
            cnt[u, x] += sgn; cnt[x, u] += sgn
    if sgn > 0:
        for i in range(2):
            u = P[w, i]
            for j in range(2):
                x = P[v, j]
                if cnt[u, x] > T[u, x] or cnt[x, u] > T[x, u]:
                    ok = False
    return ok

@njit(cache=True)
def _feasible(cnt, T, P, w, v):
    # test sans modifier : compte les increments sur chaque case touchee
    for i in range(2):
        u = P[w, i]
        for j in range(2):
            x = P[v, j]
            inc = 0
            for i2 in range(2):
                u2 = P[w, i2]
                for j2 in range(2):
                    x2 = P[v, j2]
                    if (u2 == u and x2 == x) or (x2 == u and u2 == x):
                        inc += 1
            if cnt[u, x] + inc > T[u, x]:
                return False
    return True

@njit(cache=True)
def search(T, P, cap, node_cap):
    n = P.shape[0]
    part = -np.ones(n, dtype=np.int64)
    cnt = np.zeros((12, 12), dtype=np.int64)
    sols = np.zeros((cap, n), dtype=np.int64)
    nsol = 0
    nodes = 0
    # pile explicite : pour chaque niveau, la paire choisie w, la liste de candidats et l'indice courant
    stack_w = np.zeros(n, dtype=np.int64)
    stack_c = np.zeros((n, n), dtype=np.int64)
    stack_nc = np.zeros(n, dtype=np.int64)
    stack_i = np.zeros(n, dtype=np.int64)
    depth = 0
    need_choose = True
    while True:
        if need_choose:
            nodes += 1
            if nodes > node_cap:
                return sols[:nsol], nsol, nodes, False
            # tout apparie ?
            best = -1; bestn = 10 ** 9
            for w in range(n):
                if part[w] >= 0: continue
                c = 0
                for v in range(n):
                    if v == w or part[v] >= 0: continue
                    if _feasible(cnt, T, P, w, v): c += 1
                if c < bestn:
                    bestn = c; best = w
                    if c == 0: break
            if best < 0:
                # solution complete : verifier l'egalite
                good = True
                for a in range(12):
                    for b in range(12):
                        if cnt[a, b] != T[a, b]: good = False
                if good:
                    if nsol < cap:
                        sols[nsol, :] = part
                    nsol += 1
                # remonter
                need_choose = False
                depth -= 1
                if depth < 0: break
                continue
            if bestn == 0:
                need_choose = False
                depth -= 1
                if depth < 0: break
                continue
            stack_w[depth] = best
            k = 0
            for v in range(n):
                if v == best or part[v] >= 0: continue
                if _feasible(cnt, T, P, best, v):
                    stack_c[depth, k] = v; k += 1
            stack_nc[depth] = k
            stack_i[depth] = -1
            need_choose = False
            # descendre au premier candidat (traite ci-dessous)
            depth += 1
            depth -= 1
        # avancer au candidat suivant du niveau depth (en annulant le precedent)
        w = stack_w[depth]
        if stack_i[depth] >= 0:
            v = stack_c[depth, stack_i[depth]]
            _try(cnt, T, P, w, v, -1)
            part[w] = -1; part[v] = -1
        stack_i[depth] += 1
        if stack_i[depth] >= stack_nc[depth]:
            depth -= 1
            if depth < 0: break
            continue
        v = stack_c[depth, stack_i[depth]]
        _try(cnt, T, P, w, v, 1)
        part[w] = v; part[v] = w
        depth += 1
        need_choose = True
    return sols[:min(nsol, cap)], nsol, nodes, True

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); which = [int(x) for x in sys.argv[2].split(",")]
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
    node_cap = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 12
    mu, reps, st = types(part)
    P = pairs_non_mu(mu)
    for ti in which:
        tau = reps[ti]
        Cx, Ct = targets(mu, tau, 12)
        t0 = time.time()
        sols, nsol, nodes, done = search(np.array(Ct, dtype=np.int64), P, cap, node_cap)
        print("A%s tau#%d : tau = %s ; %s ; solutions kappa = %d ; noeuds = %d ; %.1f s"
              % (sys.argv[1], ti, list(tau), "TERMINE" if done else "PLAFOND", nsol, nodes, time.time() - t0), flush=True)
        if nsol:
            np.save(os.path.join(HERE, "..", "logs", "kappa_A%s_t%d.npy" % (sys.argv[1], ti)), sols)
