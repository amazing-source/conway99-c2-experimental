"""Bold bet T1: the s=1 structure as a transition system on the cross-polytope CP(m) (edges = roots of D_m).

For each outer root u = {a,b} (a,b inner), its two s=1 neighbours share a resp. b.  The s=1 edges form a 2-factor on the 2m(m-1) roots,
i.e. closed trails of CP(m).  We compute on the controls (m=2, m=11 BvLS):
  - cycle lengths of the s=1 2-factor, sigma-invariant vs paired cycles, holonomy on the orbit quotient;
  - F2 ranks: A1 (s=1 adjacency), A0 (s=0), H, H+I, A1+I, and relations with the rank-20-type invariants.
Goal: find a parity/rank identity that holds at m=2, 11 and could be violated at m=7.
"""
import json, os, sys, itertools
from collections import Counter
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
sys.path.insert(0, HERE)
from involution_frame import Frame, paley9, table_from_graph  # noqa
from sib_partition_check import load, outer_graph  # noqa
from padic import rank_mod_p  # noqa


def analyse(m):
    fr, T = load(m)
    roots, idx, Hm = outer_graph(fr, T)
    n = len(roots)
    supp = lambda r: [(i, x) for i, x in enumerate(r) if x]
    A1 = np.zeros_like(Hm); A0 = np.zeros_like(Hm)
    for u in range(n):
        for v in range(n):
            if Hm[u, v]:
                shared = set(supp(roots[u])) & set(supp(roots[v]))
                if shared: A1[u, v] = 1
                else: A0[u, v] = 1
    deg1 = set(A1.sum(1)); deg0 = set(A0.sum(1))
    # cycles of the 2-factor
    seen = [False] * n; cycles = []
    neg = {i: idx[tuple(-x for x in roots[i])] for i in range(n)}
    for s in range(n):
        if seen[s]: continue
        cyc = [s]; seen[s] = True; prev = None; cur = s
        while True:
            nb = [w for w in np.nonzero(A1[cur])[0] if w != prev]
            nxt = nb[0] if prev is not None else nb[0]
            if nxt == s: break
            if seen[nxt]:
                break
            cyc.append(nxt); seen[nxt] = True; prev, cur = cur, nxt
        cycles.append(cyc)
    lens = Counter(len(c) for c in cycles)
    inv = sum(1 for c in cycles if neg[c[0]] in set(c))
    print("=== m=%d : %d roots ; s=1 degrees %s, s=0 degrees %s" % (m, n, deg1, deg0))
    print("   s=1 cycles: %d  lengths %s ; sigma-invariant cycles %d, sigma-paired %d" % (len(cycles), dict(lens), inv, (len(cycles) - inv)))
    for name, M in (("A1", A1), ("A1+I", A1 + np.eye(n, dtype=int)), ("A0", A0), ("A0+I", A0 + np.eye(n, dtype=int)),
                    ("H", Hm), ("H+I", Hm + np.eye(n, dtype=int))):
        print("   rank_F2(%s) = %d   rank_F3 = %d" % (name, rank_mod_p(M, 2), rank_mod_p(M, 3)))
    return cycles


if __name__ == "__main__":
    for m in (2, 11):
        analyse(m)
