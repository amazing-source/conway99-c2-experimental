"""Orientation campaign by FIXING BLOCKS (note 40): orbit-level LP (orientation fixed, all D-structures variable) where the D-structure
is fixed at a growing set of blocks; the options at each block are those occurring in the filtered leaves consistent with the blocks
already fixed.  Node = partial assignment {block: option}.  Infeasible node (exact certificate, model 'gen' + forbid) => every leaf
extending it dies.  Feasible node => fix one more block (the one with the most options among the node's leaves), children = all its
options (complete cover of the node's leaves).  A node whose leaves are all fixed and still feasible is reported (never seen so far).
Usage: python orbit_fixcamp.py <class id> <job> [max nodes]"""
import sys, json, glob, time, os
from collections import Counter, defaultdict
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_gen as OG
ci, job = sys.argv[1], int(sys.argv[2]); maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 400
jobs = []
for f in sorted(glob.glob("logs/mix6_cls_%s_S_*.json" % ci)):
    d = json.load(open(f))
    for po in d["per_orient"]:
        if po["leaves"]: jobs.append(po)
po = jobs[job]; In = {int(x): v for x, v in po["In"].items()}; A = po["A"]
leaves = [tuple(sorted(tuple(z) for z in L)) for L in po["leaves"]]
if os.environ.get('OPEN'):                   # stage 2 (note 43): only the leaves left open by the pair-level stage (pair_fast.py)
    keep = json.load(open(os.environ['OPEN']))["open"]
    leaves = [leaves[t] for t in keep]
    print("OPEN: %d leaves kept of %d" % (len(leaves), len(po["leaves"]))); sys.stdout.flush()
g0 = OG.OrbitModelGen(In)
blockof = lambda L, c: tuple(z for z in L if z[0] == c)
import itertools as _it
_arcs = {(c, x) for c, xs in In.items() for x in xs}
STAB = [g for g in _it.permutations(range(7)) if {(g[c], g[x]) for (c, x) in _arcs} == _arcs and (A is None or g[A] == A)]


def orbit_reps(opts, assign, c):
    """orbital branching (note 44): one option per orbit of the stabiliser of the node's assignment and of block c; the leaves
    of the other options are images of covered leaves (coverage_check.py propagates coverage along STAB)"""
    if os.environ.get('NOSYM'): return list(opts)
    imt = lambda o, g: tuple(sorted((g[i], g[j], g[k]) for (i, j, k) in o))
    canon = {cc: tuple(sorted(v)) for cc, v in assign.items()}
    H = [g for g in STAB if g[c] == c and all(imt(v, g) == canon.get(g[cc]) for cc, v in canon.items())]
    return [o for o in opts if tuple(sorted(o)) == min(imt(o, g) for g in H)]

def forbid_for(assign):
    forbid = set()
    for c, trip in assign.items():
        thirds = defaultdict(list)
        for (i, x, y) in trip: thirds[x].append(y)
        lab = {}
        for x, ys in thirds.items():
            os_ = [o for o in g0.orbs_of[frozenset((c, x))] if g0.pivot[o] == c]
            for o, y in zip(os_, sorted(ys)): lab.setdefault((x, y), []).append(o)
        partner = {}
        for (x, y), Zs in lab.items():
            for t_, Z in enumerate(Zs): partner[Z] = lab[(y, x)][t_]
        for Z, W in partner.items():
            i_, j_, _ = g0.T[Z]
            for k in range(7):
                if k in (i_, j_): continue
                for Dz in g0.orbs_of[frozenset((c, k))]:
                    if g0.pivot[Dz] == c and Dz != W: forbid.add((Z, Dz))
    return forbid


def closed_components(assign):
    """closed D-classes at each fixed block c: components of the D-graph at c containing no twisted pair (balance 24.0)"""
    out = []
    for c, trip in assign.items():
        adj = defaultdict(set); nodes = set()
        for (i, x, y) in trip: adj[x].add(y); adj[y].add(x); nodes |= {x, y}
        tw = {x for x in nodes if not (c in In and x in In[c])}            # pair {c,x} not anchored at c: twisted at c
        seen = set()
        for v in nodes:
            if v in seen: continue
            comp = set(); st = [v]
            while st:
                u = st.pop()
                if u in comp: continue
                comp.add(u); st += list(adj[u] - comp)
            seen |= comp
            if not (comp & tw): out.append((c, frozenset(comp)))
    return out

def balance_filter(g, comps):
    """24.0 on each closed class S at c: every orbit Z whose pair avoids c has sum_{m in S} q_Z(orbits of {c,m}) = |S| - |P_Z & S|"""
    for c, S in comps:
        orbs = [o for m in S for o in g.orbs_of[frozenset((c, m))]]
        for Z in range(g.n):
            P = g.pair[Z]
            if c in P: continue
            need = len(S) - len(P & S)
            M = g.cols[Z]; g.cols[Z] = M[M[:, orbs].sum(axis=1) == need]

out = open("logs/orbit_fixcamp_%s_%d.jsonl" % (ci, job), "a")
stack = [({}, list(range(len(leaves))), None)]; nodes = 0; t0 = time.time(); open_nodes = 0
while stack:
    assign, idx, init = stack.pop()
    if nodes >= maxn: open_nodes += 1 + len(stack); break
    nodes += 1; t1 = time.time()
    fb = forbid_for(assign)
    if not assign and os.environ.get('SKIPROOT'):          # orientation-level LP already known feasible
        obj, st0 = 0.0, 'feasible'
        rec = {"node": nodes, "assign": {}, "fixed_blocks": [], "nleaves": len(idx), "status": "feasible(known)", "slack": 0, "secs": 0}
        out.write(json.dumps(rec) + chr(10)); out.flush(); print(rec)
        free_blocks = [c for c in range(7) if c != A]
        opts = {c: Counter(blockof(leaves[t], c) for t in idx) for c in free_blocks}
        multi = [b for b in free_blocks if len(opts[b]) > 1] or free_blocks
        c = (max if os.environ.get('RICHEST') else min)(multi, key=lambda b: len(opts[b]))   # default: fewest options > 1
        for trip in orbit_reps(opts[c], {}, c):
            sub = [t for t in idx if blockof(leaves[t], c) == trip]
            stack.append(({c: trip}, sub, None))
        continue
    g = OG.OrbitModelGen(In, forbid=fb)
    if not os.environ.get('NOBALF'):
        comps = closed_components(assign)
        if comps:
            balance_filter(g, comps)
            if any(len(M) == 0 for M in g.cols):          # combinatorial kill: some orbit has no admissible column
                rec = {"node": nodes, "assign": {str(c): len(v) for c, v in assign.items()}, "fixed_blocks": sorted(assign), "nleaves": len(idx),
                       "status": "dead-comb", "comps": [[c, sorted(S)] for c, S in comps], "secs": round(time.time() - t1)}
                import gzip as _gz
                _gz.open("logs/orbit_certs/comb_%s_%d_%d.json.gz" % (ci, job, nodes), "wt").write(json.dumps({"model": "comb", "spec": {"In": po["In"],
                    "forbid": sorted(map(list, fb)), "assign": {str(c): [list(z) for z in v] for c, v in assign.items()}, "comps": [[c, sorted(S)] for c, S in comps],
                    "empty_orbits": [Z for Z in range(42) if len(g.cols[Z]) == 0]}}))
                out.write(json.dumps(rec) + chr(10)); out.flush(); print(rec); continue
            g.build_rows()
    solver = g.solve_lazy if os.environ.get('LAZYCUTS') else g.solve
    obj, y = solver(tlimit=float(os.environ.get('TL', 4000)), verbose=False, init=init)   # warm start from the parent's columns
    if g.done and obj > 1e-6:
        ok, b = g.verify(y)
        st = 'dead' if ok else 'certfail'
        if ok: OM.save_cert(g, y, "logs/orbit_certs/fc_%s_%d_%d.json.gz" % (ci, job, nodes), "gen",
                            {"In": po["In"], "forbid": sorted(map(list, fb)), "assign": {str(c): [list(z) for z in v] for c, v in assign.items()}}, b)
    else: st = 'feasible' if g.done else 'timeout'
    rec = {"node": nodes, "assign": {str(c): len(v) for c, v in assign.items()}, "fixed_blocks": sorted(assign), "nleaves": len(idx),
           "status": st, "slack": round(obj, 4), "secs": round(time.time() - t1)}
    out.write(json.dumps(rec) + "\n"); out.flush(); print(rec); sys.stdout.flush()
    if st in ('dead', 'dead-comb'): continue
    if st != 'feasible': open_nodes += 1; continue
    free_blocks = [c for c in range(7) if c != A and c not in assign]
    opts = {c: Counter(blockof(leaves[t], c) for t in idx) for c in free_blocks}
    cands = [c for c in free_blocks if len(opts[c]) > 1] or [c for c in free_blocks if len(opts[c]) == 1 and opts[c]]
    if not cands: print("UNRESOLVED fully fixed node", assign); open_nodes += 1; continue
    c = (max if os.environ.get('RICHEST') else min)(cands, key=lambda b: len(opts[b]))
    for trip in orbit_reps(opts[c], assign, c):
        sub = [t for t in idx if blockof(leaves[t], c) == trip]
        a2 = dict(assign); a2[c] = trip; stack.append((a2, sub, getattr(g, 'final_keys', None)))
print("FIXCAMP %s job %d: nodes %d open %d %s %.0fs" % (ci, job, nodes, open_nodes, "ALL DEAD" if open_nodes == 0 else "INCOMPLETE", time.time() - t0))
