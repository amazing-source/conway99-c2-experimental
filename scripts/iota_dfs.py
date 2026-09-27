"""DFS over PARTIAL iota (step 1' of structures, involution/s1p_*.npz; note 44): at each node some iota-pairs are fixed
(p[n] = 1), the phase-1 LP of the model (near-design + block-level (ii)) is solved with warm start (bb_certify.BB), and the
node dies when the LP is infeasible (Farkas certificate, exact check with structures' certify.leaf_ok).  Branching: the
lowest unpaired non-mu edge; children = its admissible partners, ONE per orbit of the stabiliser of the node under the
label group G = <permutations commuting with sigma (i^1) and mu and tau> (orbital branching; the model's invariance under G
is checked numerically first).
Usage: python iota_dfs.py <model.npz> <index.json> [max nodes]      output: logs/iota_dfs_<name>.jsonl (one line per node)
Certificates: every dead node's exact Farkas vector goes to logs/iota_certs_<name>.jsonl.gz (node, fixed pairs, cert), so the
whole tree can be re-checked with structures' certify.leaf_ok; progress line every 200 nodes; final line says ALL DEAD or not."""
import sys, os, json, time, itertools, gzip
from collections import Counter
import numpy as np, scipy.sparse as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb_certify import BB

npz, idxf = sys.argv[1], sys.argv[2]; maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
z = np.load(npz); A = sp.csr_matrix((z['A_data'], z['A_indices'], z['A_indptr']), shape=tuple(z['A_shape']))
lo, hi, lb0, ub0 = z['lo'], z['hi'], z['lb'].astype(float), z['ub'].astype(float)
I = json.load(open(idxf)); mu, tau = I['mu'], I['tau']; E = [tuple(e) for e in I['edges (non-mu pairs)']]
IP = [tuple(p) for p in I['iota_pairs']]; npair = len(IP); BP = [tuple(b) for b in I['block_pairs']]
eidx = {e: i for i, e in enumerate(E)}; ipidx = {p: n for n, p in enumerate(IP)}; bpidx = {b: k for k, b in enumerate(BP)}
nv = A.shape[1]; assert nv == npair + 15 * npair, (nv, npair)
sig = [i ^ 1 for i in range(12)]

# label group: permutations commuting with sigma, mu, tau
def extend(images):
    pi = [None] * 12; stack = list(images)
    while stack:
        x, y = stack.pop()
        if pi[x] is not None:
            if pi[x] != y: return None
            continue
        pi[x] = y; stack += [(sig[x], sig[y]), (mu[x], mu[y]), (tau[x], tau[y])]
    return tuple(pi) if None not in pi and sorted(pi) == list(range(12)) else None
G = set()
for img0 in itertools.permutations(range(12), 2):
    cand = extend([(0, img0[0])])
    if cand is not None: G.add(cand)
    else:
        for x in range(12):
            c2 = extend([(0, img0[0]), (x, img0[1])]) if x != 0 else None
            if c2: G.add(c2)
G = [g for g in G if all(g[sig[x]] == sig[g[x]] and g[mu[x]] == mu[g[x]] and g[tau[x]] == tau[g[x]] for x in range(12))]
def gedge(e, g): return tuple(sorted((g[e[0]], g[e[1]])))
def gip(p, g):
    a, b = eidx[gedge(E[p[0]], g)], eidx[gedge(E[p[1]], g)]; return ipidx.get(tuple(sorted((a, b))))
def gblock(k, g):
    bl = BP[k]; return bpidx[tuple(sorted((g[2 * bl[0]] // 2, g[2 * bl[1]] // 2)))]
# variable permutation for each g; check model invariance (rows as multisets of (var, coef) with bounds)
rows_sig = Counter()
Acsr = A.tocsr()
def rowkey(r, perm):
    s, e = Acsr.indptr[r], Acsr.indptr[r + 1]
    return (float(lo[r]), float(hi[r]), tuple(sorted((int(perm[j]), float(v)) for j, v in zip(Acsr.indices[s:e], Acsr.data[s:e]))))
ident = np.arange(nv)
base = Counter(rowkey(r, ident) for r in range(A.shape[0]))
GOOD = []
for g in G:
    perm = np.empty(nv, dtype=np.int64); ok = True
    for n, p in enumerate(IP):
        m = gip(p, g)
        if m is None: ok = False; break
        perm[n] = m
        for k in range(15): perm[npair + 15 * n + k] = npair + 15 * m + gblock(k, g)
    if not ok: continue
    if Counter(rowkey(r, perm) for r in range(A.shape[0])) == base: GOOD.append((g, perm))
print("label group |G| = %d, model-invariant: %d" % (len(G), len(GOOD))); sys.stdout.flush()

# SECFIRST=1 (structures/C1, 27/09): branch first, for each NON-pivot label v (mu[v] != tau[v]), on WHICH secant iota-pair is centred
# at v (both edges contain v); children = each admissible such pair, plus one child 'no secant at v' (all forbidden), so the
# branching is complete without any lemma; then the usual edge branching.
NP = [v for v in range(12) if mu[v] != tau[v]]
cent = {}
for n, (e1, e2) in enumerate(IP):
    c = set(E[e1]) & set(E[e2])
    if len(c) == 1: cent.setdefault(next(iter(c)), []).append(n)
SECFIRST = bool(os.environ.get('SECFIRST'))
if SECFIRST: print("secant-first branching on non-pivot labels", NP, "| candidates per label", {v: len(cent.get(v, [])) for v in NP}); sys.stdout.flush()
B = BB(A, lo, hi, lb0, ub0)
name = os.path.basename(npz).replace('.npz', ''); out = open("logs/iota_dfs_%s.jsonl" % name, "w")
certs = gzip.open("logs/iota_certs_%s.jsonl.gz" % name, "wt"); uncert = 0; leaf_feas = 0
stack = [((), frozenset())]; nodes = 0; depth_stat = Counter(); dead_stat = Counter(); t0 = time.time()
while stack and nodes < maxn:
    fixed, noc = stack.pop(); nodes += 1
    if nodes % 200 == 0:
        print("  nodes %d stack %d  depth hist %s  dead %s  uncertified %d  %.0fs" % (nodes, len(stack), dict(sorted(depth_stat.items())), dict(sorted(dead_stat.items())), uncert, time.time() - t0)); sys.stdout.flush()
    lb, ub = lb0.copy(), ub0.copy()
    used = set()
    for n in fixed: lb[n] = ub[n] = 1; used |= set(IP[n])
    for n, p in enumerate(IP):
        if n not in fixed and (p[0] in used or p[1] in used): ub[n] = 0
    for v in noc:
        for n in cent.get(v, []): ub[n] = 0
    obj, dual, x = B.lp(lb, ub); d = len(fixed); depth_stat[d] += 1
    if obj is None or obj > 1e-7:
        c = B.cert(dual, lb, ub) if obj is not None else None
        dead_stat[d] += 1
        if c: certs.write(json.dumps({"node": nodes, "fixed": list(fixed), "nocenter": sorted(noc), "cert": c["cert"]}) + chr(10))
        else: uncert += 1
        out.write(json.dumps({"node": nodes, "fixed": list(fixed), "nocenter": sorted(noc), "status": "dead" if c else "lp-dead-uncertified"}) + chr(10))
        continue
    if SECFIRST:
        done = {v for v in NP if v in noc or any(n in cent.get(v, []) for n in fixed)}
        todo = [v for v in NP if v not in done]
        if todo:
            v = todo[0]; fset = set(fixed)
            H = [(g, perm) for g, perm in GOOD if g[v] == v and all(perm[n] in fset for n in fixed) and all(g[w] in noc for w in noc)]
            cands = [n for n in cent.get(v, []) if ub[n] > 0]
            reps = [n for n in cands if n == min(int(perm[n]) for _, perm in H)] if H else cands
            stack.append((fixed, noc | {v}))
            for n in reps: stack.append((fixed + (n,), noc))
            continue
    free = [i for i in range(len(E)) if i not in used]
    if not free: out.write(json.dumps({"node": nodes, "fixed": list(fixed), "nocenter": sorted(noc), "status": "LEAF-FEASIBLE"}) + chr(10)); print("LEAF-FEASIBLE", fixed); leaf_feas += 1; continue
    i = free[0]
    cands = [n for n, p in enumerate(IP) if i in p and ub[n] > 0]
    # orbital branching: stabiliser of the fixed set and of edge i
    fset = set(fixed); H = [perm for g, perm in GOOD if all(perm[n] in fset for n in fixed) and gedge(E[i], g) == E[i] and all(g[w] in noc for w in noc)]
    reps = [n for n in cands if n == min(int(perm[n]) for perm in H)] if H else cands
    for n in reps: stack.append((fixed + (n,), noc))
certs.close()
print("IOTA-DFS %s: nodes %d, stack left %d, uncertified dead %d, depth hist %s, dead %s, %.0fs  %s" % (name, nodes, len(stack), uncert, dict(sorted(depth_stat.items())), dict(sorted(dead_stat.items())), time.time() - t0,
      "ALL DEAD" if not stack and uncert == 0 and leaf_feas == 0 else "INCOMPLETE (%d feasible leaves)" % leaf_feas))
