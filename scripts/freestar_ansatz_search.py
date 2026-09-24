"""Recherche EXHAUSTIVE des solutions H-equivariantes du probleme local de l'etoile libre (note 23), cube mu = sigma (A111111).
Phi : R -> R (R = 60 racines de D6 sur les blocs 2..7), Phi(h z) = h Phi(z) pour h dans H <= Stab(mu, tau), -id hors de H.
Contraintes : (ii) #{z ∋ a : b ∈ Phi(z)} = Cx[a,b] ; (iii) #{z : b ∈ Phi(z), d ∈ Phi(-z)} = Ct[b,d] ; Phi bijective.
Retour : liste des solutions (vide = aucune solution H-equivariante ; resultat DEFINITIF pour cet ansatz)."""
import sys, os, itertools, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types
from freestar_ansatz import stab, order

R = [frozenset((a, b)) for a in range(12) for b in range(a + 1, 12) if a // 2 != b // 2]
RI = {r: i for i, r in enumerate(R)}
NEG = [RI[frozenset(x ^ 1 for x in r)] for r in R]

def act(h, i):
    return RI[frozenset(h[x] for x in R[i])]

def closure(gens):
    idt = tuple(range(12)); G = {idt}; frontier = [idt]
    while frontier:
        new = []
        for g in frontier:
            for s in gens:
                h = tuple(s[g[x]] for x in range(12))
                if h not in G: G.add(h); new.append(h)
        frontier = new
    return sorted(G)

def search(mu, tau, H, node_cap=None):
    Cx, Ct = targets(mu, tau, 12)
    # orbites de H sur R, stabilisateurs
    seen = [False] * 60; orbs = []
    for i in range(60):
        if seen[i]: continue
        orb = sorted({act(h, i) for h in H})
        for j in orb: seen[j] = True
        st = frozenset(h for h in H if act(h, i) == i)
        orbs.append((i, orb, st))
    # candidats pour chaque representant : f avec Stab(f) = Stab(z) (meme taille d'orbite)
    cand = []
    for (i, orb, st) in orbs:
        cs = [f for f in range(60) if frozenset(h for h in H if act(h, f) == f) == st]
        cand.append(cs)
    # ordre : orbites les plus contraintes d'abord
    order_ix = sorted(range(len(orbs)), key=lambda k: len(cand[k]))
    phi = [-1] * 60; used = [False] * 60
    c2 = np.zeros((12, 12), dtype=int); c3 = np.zeros((12, 12), dtype=int)
    sols = []; nodes = [0]
    def assign(z, f, sgn):
        for a in R[z]:
            for b in R[f]: c2[a, b] += sgn
        nz = NEG[z]
        if phi[nz] >= 0:
            g = phi[nz]
            for b in R[f]:
                for d in R[g]: c3[b, d] += sgn
            for b in R[g]:
                for d in R[f]: c3[b, d] += sgn
    def ok_bounds():
        return (c2 <= Cx).all() and (c3 <= Ct).all()
    def rec(k):
        nodes[0] += 1
        if node_cap and nodes[0] > node_cap: raise RuntimeError("cap")
        if k == len(order_ix):
            if (c2 == Cx).all() and (c3 == Ct).all(): sols.append(list(phi))
            return
        (i, orb, st) = orbs[order_ix[k]]
        for f in cand[order_ix[k]]:
            if used[f]: continue
            # etendre par equivariance : Phi(h i) = h f
            pairs = {}
            okk = True
            for h in H:
                z, g = act(h, i), act(h, f)
                if z in pairs:
                    if pairs[z] != g: okk = False; break
                else:
                    pairs[z] = g
            if not okk: continue
            tg = list(pairs.values())
            if len(set(tg)) != len(tg) or any(used[g] for g in tg): continue
            done = []
            for z, g in pairs.items():
                phi[z] = g; used[g] = True; assign(z, g, 1); done.append((z, g))
            if ok_bounds(): rec(k + 1)
            for z, g in reversed(done):
                assign(z, g, -1); phi[z] = -1; used[g] = False
    rec(0)
    return sols, nodes[0], [len(c) for c in cand], len(orbs)

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); minord = int(sys.argv[2]); cap = int(sys.argv[3])
    which = [int(x) for x in sys.argv[4].split(",")]; two_gen = sys.argv[5] == "2" if len(sys.argv) > 5 else True
    mu, reps, st = types(part)
    neg = tuple(x ^ 1 for x in range(12))
    log = open(os.path.join(HERE, "..", "logs", "freestar_ansatz.log"), "a", encoding="utf-8")
    for ti in which:
        tau = reps[ti]; S = stab(mu, tau)
        subs = {}
        for g in S:
            G = closure([g])
            if neg not in G and len(G) >= minord: subs[tuple(G)] = G
        if two_gen:
            for g1, g2 in itertools.combinations(S, 2):
                G = closure([g1, g2])
                if neg not in G and len(G) >= minord: subs[tuple(G)] = G
        print("A%s tau#%d : |Stab| = %d, %d sous-groupes a examiner (ordre >= %d, sans -id)" % (sys.argv[1], ti, len(S), len(subs), minord), flush=True)
        for key, G in sorted(subs.items(), key=lambda kv: -len(kv[1])):
            t0 = time.time()
            try:
                sols, nodes, cands, norb = search(mu, tau, G, cap)
                line = "A%s tau#%d |H|=%d orbites=%d : %s (%d noeuds, %.1f s)" % (sys.argv[1], ti, len(G), norb,
                        ("SOLUTION " + str(sols[0])) if sols else "aucune solution H-equivariante", nodes, time.time() - t0)
            except RuntimeError:
                line = "A%s tau#%d |H|=%d : budget atteint (non compte)" % (sys.argv[1], ti, len(G))
            print(line, flush=True); log.write(line + chr(10)); log.flush()
