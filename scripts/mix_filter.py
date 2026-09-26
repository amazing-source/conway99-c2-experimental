"""General SOUND block filter for Sigma = empty, one-block-square configurations with ANY twisted subgraph (note 35).
Skeleton = orientation (twisted set + heads of anchored pairs) + D-graph at every pivot block.
Checks (all proved): at every block j, the free orbits admit a 2-regular graph with even cycles >= 4, no sister edge, sisters with
<= 1 common neighbour (19.1), typed rule (n_k <= 1, note 30), and every orbit's n-vector keeps its single-orbit profile feasible
(27.1: F1 + balance on the components of G_c that are CERTAIN: the closed D-cycles at c, i.e. components of the D-graph at c
without twisted pair, and their complement; unassigned blocks: a single component).  Partial skeletons are checked with the
information available (sound pruning).  Symmetry: Aut(twisted graph) on orientations and on surviving skeletons.
Usage: python mix_filter.py <twisted class index> <k> <K> <seconds>"""
import sys, time, itertools, json
from collections import Counter, defaultdict
sys.path.insert(0, "scripts")
import mix_enum as ME, m1_blocks as MB
from m1_blocks3 import two_factor_exists
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
N = 7; P = ME.P

def twisted_classes():
    basis = [{(0, a), (0, b), (a, b)} for a, b in itertools.combinations(range(1, N), 2)]
    seen = []
    for mask in range(1 << 15):
        s = set()
        for t in range(15):
            if mask >> t & 1: s ^= basis[t]
        G = nx.Graph(); G.add_nodes_from(range(N)); G.add_edges_from(s)
        key = (G.number_of_edges(), tuple(sorted(d for _, d in G.degree())))
        if any(k2 == key and nx.is_isomorphic(G, H) for k2, H in seen): continue
        seen.append((key, G))
    out = []
    for key, G in sorted(seen, key=lambda kg: (kg[0][0], kg[0][1])):
        H = G.copy(); H.remove_nodes_from([v for v in list(H) if H.degree(v) == 0])
        single = H.number_of_nodes() > 0 and all(d == 2 for _, d in H.degree()) and nx.is_connected(H)
        if G.number_of_edges() in (0, 21) or single: continue
        out.append(sorted(tuple(sorted(e)) for e in G.edges()))
    return out

def automorphisms(twE):
    G = nx.Graph(); G.add_nodes_from(range(N)); G.add_edges_from(twE)
    return [dict(m) for m in GraphMatcher(G, G).isomorphisms_iter()]

def comps_of(c, dg, assigned):
    rest = set(range(N)) - {c}
    if c not in assigned: return [rest]
    edges, twl = dg
    Gd = nx.MultiGraph(); Gd.add_nodes_from({x for e in edges for x in e}); Gd.add_edges_from(edges)
    out = []; used = set()
    for comp in nx.connected_components(Gd):
        if not (comp & twl): out.append(set(comp)); used |= comp
    if not out: return [rest]
    return out + [rest - used] if rest - used else out

def block_ok(j, orbit_list, comps, memo):
    free = [o for o in orbit_list if o[1] == j]
    if not free: return True
    ids = list(range(len(free))); typ = {t: free[t][0] for t in ids}
    sis_of = {}
    for a, b in itertools.combinations(ids, 2):
        if typ[a] == typ[b]: sis_of[a] = b; sis_of[b] = a
    present = sorted(set(typ.values())); allowed = {}
    for t in ids:
        i, jj, k = free[t][:3]; al = set()
        for r1, r2 in itertools.combinations_with_replacement(present, 2):
            nv = Counter([r1, r2])
            if any(nv[r] > sum(1 for u in ids if typ[u] == r) - (1 if r == typ[t] else 0) for r in nv): continue
            if r1 == r2 == typ[t]: continue
            if r1 == r2 == k: continue                                  # typed rule
            key = (i, jj, k, r1, r2, tuple(tuple(sorted(C)) for c in range(N) if c not in (i, jj) for C in comps[c]))
            if key not in memo:
                fixed = {r: nv.get(r, 0) for r in range(N) if r not in (i, jj)}
                memo[key] = MB.feasible_exact(i, jj, k, comps, fixed)
            if memo[key]: al.add((r1, r2))
        if not al: return False
        allowed[t] = al
    return two_factor_exists(ids, typ, allowed, sis_of)

def orbits_from(dgs):
    out = []
    for c, (edges, twl) in dgs.items():
        for (x, y) in edges: out += [(c, x, y), (c, y, x)]
    return out

def canon_skel(orbs, auts):
    return min(tuple(sorted(tuple(g[v] for v in z) for z in orbs)) for g in auts)

def run(twE, k, K, budget):
    auts = automorphisms(twE); t0 = time.time()
    reps = {}
    for In, tw in ME.orientations(twE):
        arcs = [(a, b) for b in range(N) for a in In[b]]
        key = min(tuple(sorted((g[a], g[b]) for a, b in arcs)) for g in auts)
        if key not in reps: reps[key] = In
    reps = list(reps.values())
    tw = {P(a, b) for a, b in twE}
    surv = {}; stats = Counter(); done = True
    for idx, In in enumerate(reps):
        if idx % K != k: continue
        stats['orient'] += 1
        opts = {}
        for c in range(N):
            twl = {x for x in range(N) if P(c, x) in tw}
            opts[c] = [(g, twl) for g in ME.dgraphs(In[c], sorted(twl))]
        # pivots of the orbits free at j: blocks c with {c,j} anchored at c, or twisted
        need = {j: {c for c in range(N) if c != j and (j in In[c] or P(c, j) in tw)} for j in range(N)}
        order = sorted(range(N), key=lambda c: len(opts[c]))
        memo = {}
        def dfs(pos, dgs):
            nonlocal done
            if time.time() - t0 > budget: done = False; return
            assigned = set(dgs)
            comps = {c: comps_of(c, dgs.get(c), assigned) for c in range(N)}
            orbs = orbits_from(dgs)
            for j in range(N):
                if need[j] <= assigned and need[j] and not block_ok(j, orbs, comps, memo):
                    stats['pruned', pos] += 1; return
            if pos == N:
                key = canon_skel(orbs, auts); stats['leaf'] += 1
                if key not in surv: surv[key] = {str(a): b for a, b in In.items()}
                return
            c = order[pos]
            for o in opts[c]:
                dgs[c] = (o[0], o[1]); dfs(pos + 1, dgs); del dgs[c]
                if not done: return
        dfs(0, {})
        if not done: break
    return reps, surv, stats, done

if __name__ == "__main__":
    ci, k, K, budget = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
    if ci.startswith("edges="): twE = [tuple(map(int, e)) for e in ci[6:].split(",")]; ci = "E" + ci[6:].replace(",", "_")
    else: ci = int(ci); twE = twisted_classes()[ci]
    reps, surv, stats, done = run(twE, k, K, budget)
    print("twisted class", ci, twE, "| orientation classes", len(reps), "| worker", k, dict(stats), "| surviving skeleton classes", len(surv), "done" if done else "TIME CAP")
    json.dump({"twE": twE, "done": done, "classes": [[list(map(list, key)), In] for key, In in surv.items()]}, open("logs/mix_cls_%s_%d.json" % (ci, k), "w"))
