"""Recherche locale (recuit) sur la formulation compacte de l'etoile libre (scripts/freestar_compact.py, notes/20 idee 7).
But : savoir vite si le probleme LOCAL (RSF(star(1)), etoile libre) a des solutions pour un type (mu, tau). Une solution trouvee
(cout 0) est ensuite verifiee contre le CNF RSF certifie (propagation unitaire apres fixation de toutes les variables primaires).
Etat : Phi, bijection des 60 racines lointaines sur les 60 paires hors mu. Cout = sum |(ii) obs - cible| + sum |(iii) obs - cible|.
Usage : python freestar_anneal.py <partition> <indices des types, ex. 0,1,2 ou all> <secondes par type> [graine]
"""
import sys, os, json, math, random, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import far_roots, targets, types

def anneal(mu, tau, secs, seed, m=7):
    rng = random.Random(seed)
    n2 = 2 * (m - 1); Ws = far_roots(m)
    Z = [Ws[w][h] for w in range(len(Ws)) for h in (0, 1)]            # 60 racines : indice 2w+h ; antipode = indice ^ 1
    pairs = [p for p in ((a, b) for a in range(n2) for b in range(a + 1, n2)) if mu[p[0]] != p[1]]
    Cx, Ct = targets(mu, tau, n2)
    nz = len(Z)
    phi = list(range(nz)); rng.shuffle(phi)                            # phi[z] = indice de paire
    Ox = np.zeros((n2, n2), dtype=int); Ot = np.zeros((n2, n2), dtype=int)
    def apply(z, sgn):
        f = pairs[phi[z]]; g = pairs[phi[z ^ 1]]
        for a in Z[z]:
            for b in f: Ox[a, b] += sgn
        for b in f:
            for d in g: Ot[b, d] += sgn
    for z in range(nz): apply(z, 1)
    cost = int(np.abs(Ox - Cx).sum() + np.abs(Ot - Ct).sum())
    best = cost; t0 = time.time(); it = 0
    T = 1.5
    while time.time() - t0 < secs and cost > 0:
        it += 1
        z1 = rng.randrange(nz); z2 = rng.randrange(nz)
        if z1 == z2: continue
        # cout local avant/apres : on retire les contributions de z1, z2 et de leurs antipodes (termes (iii) couples)
        S = {z1, z2, z1 ^ 1, z2 ^ 1}
        rows_x = set(); pts = set()
        for z in S:
            rows_x.update(Z[z]); pts.update(pairs[phi[z]])
        # zone touchee : Ox[rows_x, :] et Ot[pts', :] ; on calcule le delta exact sur une copie restreinte
        before = 0; after = 0
        idx_b = sorted(set(pairs[phi[z1]]) | set(pairs[phi[z2]]) | set(pairs[phi[z1 ^ 1]]) | set(pairs[phi[z2 ^ 1]]))
        rx = sorted(rows_x)
        before = np.abs(Ox[rx] - Cx[rx]).sum() + np.abs(Ot[idx_b] - Ct[idx_b]).sum() + np.abs(Ot[:, idx_b] - Ct[:, idx_b]).sum() \
            - np.abs(Ot[np.ix_(idx_b, idx_b)] - Ct[np.ix_(idx_b, idx_b)]).sum()
        for z in S: apply(z, -1)
        phi[z1], phi[z2] = phi[z2], phi[z1]
        for z in S: apply(z, 1)
        idx_a = sorted(set(idx_b) | set(pairs[phi[z1]]) | set(pairs[phi[z2]]))
        after_full = np.abs(Ox[rx] - Cx[rx]).sum() + np.abs(Ot[idx_a] - Ct[idx_a]).sum() + np.abs(Ot[:, idx_a] - Ct[:, idx_a]).sum() \
            - np.abs(Ot[np.ix_(idx_a, idx_a)] - Ct[np.ix_(idx_a, idx_a)]).sum()
        before_full = before  # idx_a == idx_b (memes paires, permutees)
        delta = int(after_full - before_full)
        if delta <= 0 or rng.random() < math.exp(-delta / T):
            cost += delta
            if cost < best: best = cost
        else:
            for z in S: apply(z, -1)
            phi[z1], phi[z2] = phi[z2], phi[z1]
            for z in S: apply(z, 1)
        if it % 2000 == 0:
            T = max(0.08, T * 0.97)
            if it % 200000 == 0:
                true = int(np.abs(Ox - Cx).sum() + np.abs(Ot - Ct).sum())
                assert true == cost, (true, cost)
                T = 1.5 if best > 0 else T                                 # re-chauffe periodique
    true = int(np.abs(Ox - Cx).sum() + np.abs(Ot - Ct).sum())
    return true, best, it, {tuple(sorted(Z[z])): pairs[phi[z]] for z in range(nz)}

if __name__ == "__main__":
    try:
        import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    except Exception:
        pass
    part = tuple(int(c) for c in sys.argv[1]); secs = float(sys.argv[3]); seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    mu, reps, st = types(part)
    sel = range(len(reps)) if sys.argv[2] == "all" else [int(i) for i in sys.argv[2].split(",")]
    out = open(os.path.join(HERE, "..", "logs", "freestar_anneal.jsonl"), "a")
    for i in sel:
        cost, best, it, sol = anneal(mu, reps[i], secs, seed)
        rec = {"part": sys.argv[1], "i": i, "tau": reps[i], "cost": cost, "best": best, "iters": it, "secs": secs, "seed": seed,
               "sol": {str(k): v for k, v in sol.items()} if cost == 0 else None}
        out.write(json.dumps(rec) + "\n"); out.flush()
        print("A%s tau#%d %s : cout final %d, meilleur %d, %d iterations" % (sys.argv[1], i, reps[i], cost, best, it), flush=True)
