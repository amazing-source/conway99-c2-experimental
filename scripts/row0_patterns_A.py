"""Relaxation A (etage S + couplage D + sommes par bloc) : motifs possibles de la ligne de alpha = e0 + e1.
N(alpha) = 10 racines (antipodalement libres, evitant la droite D), somme vectorielle nulle, nombre de voisins touchant chaque bloc impose :
  2 - 2[i in p] pour i in {0,1}, 4 - 2[i in p] sinon, p = paire de blocs du partenaire D.
Types a symetrie pres : sib p={0,1} (D = +-(e0-e1)), one p={0,2} (D = +-(e0+e2)), dis p={2,3} (D = +-(e2+e3)).
Compte les motifs et les orbites sous le stabilisateur (permutations signees fixant +-alpha, la paire p et la droite D ; -I agit trivialement)."""
import itertools, sys
m = 7
roots = []
for i in range(m):
    for j in range(i + 1, m):
        for a in (1, -1):
            for b in (1, -1):
                v = [0] * m; v[i] = a; v[j] = b; roots.append(tuple(v))
alpha = tuple([1, 1] + [0] * 5)
def line(v): return max(v, tuple(-x for x in v))
types = {"sib": ((0, 1), (1, -1, 0, 0, 0, 0, 0)), "one": ((0, 2), (1, 0, 1, 0, 0, 0, 0)), "dis": ((2, 3), (0, 0, 1, 1, 0, 0, 0))}

def group(p, dline):
    """permutations signees g avec g(alpha) = +-alpha, g(p) = p, g(droite D) = droite D"""
    G = []
    for perm in itertools.permutations(range(m)):
        if {perm[0], perm[1]} != {0, 1} or {perm[p[0]], perm[p[1]]} != set(p): continue
        for sg in itertools.product((1, -1), repeat=m):
            if sg[0] != sg[1]: continue
            def act(v):
                w = [0] * m
                for k in range(m):
                    if v[k]: w[perm[k]] = sg[k] * v[k]
                return tuple(w)
            if line(act(dline)) != line(dline): continue
            eps = 1 if act(alpha) == alpha else -1
            G.append((act, eps))
    return G

for name, (p, dvec) in types.items():
    target = [(2 if i in (0, 1) else 4) - (2 if i in p else 0) for i in range(m)]
    dl = line(dvec)
    cand = [r for r in roots if line(r) not in (line(alpha), dl)]
    cand.sort()
    sols = []
    cnt = [0] * m
    def rec(start, chosen, used_lines):
        if len(chosen) == 10:
            if cnt == target and all(sum(r[k] for r in chosen) == 0 for k in range(m)):
                sols.append(tuple(sorted(chosen)))
            return
        for idx in range(start, len(cand)):
            r = cand[idx]
            if line(r) in used_lines: continue
            ks = [k for k in range(m) if r[k]]
            if any(cnt[k] + 1 > target[k] for k in ks): continue
            for k in ks: cnt[k] += 1
            rec(idx + 1, chosen + [r], used_lines | {line(r)})
            for k in ks: cnt[k] -= 1
    rec(0, [], frozenset())
    G = group(p, dvec)
    seen = set(); orbits = 0
    for s in sols:
        if s in seen: continue
        orbits += 1
        for act, eps in G:
            seen.add(tuple(sorted(tuple(eps * x for x in act(r)) for r in s)))
    print("%s : %d motifs de ligne, %d orbites (|G| = %d)" % (name, len(sols), orbits, len(G)), flush=True)
