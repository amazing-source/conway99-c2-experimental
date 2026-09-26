"""INDEPENDENT cross-check (C2 code only) of the orbit-level certificates of 'structures' for the triangle-free pure-twisted
classes (their repo amazing-source/conway99-structures-lab, logs/orbit_certs/zero_NN.json.gz).  Nothing of their code is used:
only the certificate files (row labels, stored bounds, integer multipliers y at scale 1e9) and the documented semantics.

Own reconstruction:
  D-structure from the decomposition (list of cycles of K7): orbit (j,i) = pair {i,j}, free at j, paired via i to {i,k}, k = the
  other neighbour of i on the cycle through the edge ij.  At block j the free orbits are (j,r), r != j (6-cycle, 19.1).
  Pair-level columns: orbit (j,i), free-neighbour pair p (2 blocks q, orbits (j,q)), far row = every {0,1,2} weighting of the 10
  pairs of the 5 blocks != i,j with block sums  4 - [t in p] - 2[t = k]  (mu = 2 at (t,+-); lambda at k; own enumerator).
  Orbit-level expansion (their documented convention, re-implemented): free nbr q -> (j,q):1 ; square -> (k,i):2 ; far value 2 ->
  (a,b) and (b,a):1 each ; far value 1 -> (a,b) OR (b,a):1 (all 2^m choices).
  Rows rebuilt from labels with OWN bounds (stored bounds only compared):
    Ysym[j,a,b]: [(j,a) has b] - [(j,b) has a] = 0 ; Ysub[j,S]: free edges inside S (once) in [0,|S|-1] ;
    PPE[a,b]: #columns with far value 2 on {a,b} = 2 ; C[U,W]: q_U(W) on U's columns - q_W(U) on W's = 0 ;
    P2o[U,W] (doubled): 2 sum_Z q_Z(U) q_Z(W) + q_U(W) + q_W(U) = 2(12[U=W] + 4 - |blocks(U) & blocks(W)|).
  Farkas: low = sum_{rows != O} min(y lo, y hi) ; high = sum_Z max_{all orbit-level columns c of Z} sum_{rows != O} y_r A_rc.
  low > high  =>  no solution with one unit per orbit.
Usage: python xcheck_structures_orbit_certs.py <path to structures_ro> [class numbers]"""
import sys, gzip, json, itertools, time
from collections import defaultdict
N = 7

def far_solutions(blocks, deg):
    prs = list(itertools.combinations(blocks, 2)); out = []
    def rec(t, cur, rem):
        if t == len(prs):
            if all(v == 0 for v in rem.values()): out.append(tuple(cur))
            return
        a, b = prs[t]
        for v in (0, 1, 2):
            if rem[a] < v or rem[b] < v: break
            rem[a] -= v; rem[b] -= v; cur.append(v); rec(t + 1, cur, rem); cur.pop(); rem[a] += v; rem[b] += v
    rec(0, [], dict(deg)); return prs, out

def third(dec, j, i):
    for cyc in dec:
        m = len(cyc)
        for t in range(m):
            if {cyc[t], cyc[(t + 1) % m]} == {i, j}:
                s = cyc.index(i); a, b = cyc[(s - 1) % m], cyc[(s + 1) % m]
                return b if a == j else a
    raise ValueError("edge not in decomposition")

def check(path, n):
    d = json.load(gzip.open("%s/logs/orbit_certs/zero_%02d.json.gz" % (path, n), "rt", encoding="utf-8"))
    dec = [tuple(c) for c in d["decomposition"]]
    assert d["p2o_rows_doubled"]
    # sanity: decomposition covers K7 exactly once
    E = [frozenset((c[t], c[(t + 1) % len(c)])) for c in dec for t in range(len(c))]
    assert len(E) == 21 and len(set(E)) == 21
    orbits = [(j, i) for j in range(N) for i in range(N) if i != j]
    K = {(j, i): third(dec, j, i) for (j, i) in orbits}
    ysym, ysub, yppe, yC, yP = {}, [], {}, defaultdict(int), defaultdict(int)
    low = 0; mism = 0
    for label, (lo_f, hi_f), y in d["rows"]:
        kind, key = label
        if kind == 'O': continue
        if kind == 'Ysym': j, a, b = key; ysym[(j, a, b)] = ysym.get((j, a, b), 0) + y; lo = hi = 0
        elif kind == 'Ysub': j, S = key; ysub.append((j, frozenset(S), y)); lo, hi = 0, len(S) - 1
        elif kind == 'PPE': yppe[frozenset(key)] = yppe.get(frozenset(key), 0) + y; lo = hi = 2
        elif kind == 'C': U, W = tuple(key[0]), tuple(key[1]); yC[(U, W)] += y; lo = hi = 0
        elif kind == 'P2o':
            U, W = tuple(key[0]), tuple(key[1]); yP[frozenset((U, W))] += y
            lo = hi = 2 * (12 * (U == W) + 4 - len(set(U) & set(W)))
        else: raise ValueError(kind)
        mism += (lo, hi) != (lo_f, hi_f)
        low += min(y * lo, y * hi)
    OI = {o: t for t, o in enumerate(orbits)}
    # quadratic form on orbit vectors: sum over unordered {U,W} (incl. U=W) of yP * 2 v_U v_W  -> matrix M with v^T M v
    M = [[0] * 42 for _ in range(42)]
    for key, y in yP.items():
        ks = list(key)
        if len(ks) == 1: u = OI[ks[0]]; M[u][u] += 2 * y
        else: u, w = OI[ks[0]], OI[ks[1]]; M[u][w] += y; M[w][u] += y
    high = 0; ncols = 0
    for Z in orbits:
        j, i = Z; k = K[Z]
        # linear terms on this orbit's own vector: P2o[U,W] has + q_U(W) + q_W(U): if Z = U -> + v[W]; C[U,W]: + v[W] if Z = U, - v[U] if Z = W
        lin = [0] * 42
        for key, y in yP.items():
            ks = list(key)
            if len(ks) == 1:
                if ks[0] == Z: pass                       # q_Z(Z) = 0 always
            else:
                U, W = ks
                if U == Z: lin[OI[W]] += y
                if W == Z: lin[OI[U]] += y
        for (U, W), y in yC.items():
            if U == Z: lin[OI[W]] += y
            if W == Z: lin[OI[U]] -= y
        best = None
        others = [r for r in range(N) if r not in (i, j)]
        blocks = [t for t in range(N) if t not in (i, j)]
        for p in itertools.combinations(others, 2):
            # static (non-quadratic) row terms of this pair-level column
            st = 0
            for q in p:                                   # Ysym[j,a,b] with {a,b} = {i,q}
                a, b = min(i, q), max(i, q)
                st += ysym.get((j, a, b), 0) * (1 if a == i else -1)
            for (jj, S, y) in ysub:
                if jj == j and i in S: st += y * sum(1 for q in p if q in S and q > i)
            deg = {t: 4 - (1 if t in p else 0) - (2 if t == k else 0) for t in blocks}
            prs, sols = far_solutions(blocks, deg)
            for s in sols:
                fixed = defaultdict(int); opts = []
                for q in p: fixed[(j, q)] += 1
                fixed[(k, i)] += 2
                stp = st
                for (a, b), v in zip(prs, s):
                    if v == 2:
                        fixed[(a, b)] += 1; fixed[(b, a)] += 1
                        stp += yppe.get(frozenset((a, b)), 0)
                    elif v == 1: opts.append(((a, b), (b, a)))
                for choice in itertools.product((0, 1), repeat=len(opts)):
                    v = dict(fixed)
                    for (o1, o2), c in zip(opts, choice):
                        o = o2 if c else o1; v[o] = v.get(o, 0) + 1
                    assert sum(v.values()) == 12
                    idx = [(OI[o], x) for o, x in v.items()]
                    val = stp + sum(lin[u] * x for u, x in idx)
                    val += sum(M[u][w] * x * xw for u, x in idx for w, xw in idx)
                    ncols += 1
                    if best is None or val > best: best = val
        high += best
    return d["class"], low, high, d["low"], d["high"], mism, ncols

if __name__ == "__main__":
    path = sys.argv[1]
    classes = [int(a) for a in sys.argv[2:]] or list(range(14))
    allok = True
    for n in classes:
        t0 = time.time()
        c, low, high, lo_s, hi_s, mism, ncols = check(path, n)
        ok = low > high; allok &= ok
        print("zero_%02d: low %d high %d margin %.4f (x1e9) | stored low %d high %d | bound mismatches %d | orbit columns %d | %s | %.0fs"
              % (n, low, high, (low - high) / 1e9, lo_s, hi_s, mism, ncols, "VALID" if ok else "INVALID", time.time() - t0)); sys.stdout.flush()
    print("ALL VALID" if allok else "SOME INVALID")
