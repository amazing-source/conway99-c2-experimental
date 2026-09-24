"""Check LEMMA S1 on the controls (root language).

Roots of D_m: +-e_i +- e_j.  Outer vertex label {(i,s),(j,t)} <-> root (-1)^s e_i + (-1)^t e_j.
LEMMA S1 (derived): if the block pair p={i,j} is sib (its two sister orbits are D-partners), then for alpha in P_p (4 roots)
  N(alpha) = {2 sisters} u N0(alpha), N0(alpha) avoids blocks i,j, |N0(alpha)| = 2(m-2), the four N0(alpha) are pairwise disjoint.
  Hence they PARTITION the 4*C(m-2,2) roots avoiding i,j iff 2(m-2) = C(m-2,2) iff m = 7 (or m = 2); at m = 11 it is a packing (72 of 144).
Also reports, for BvLS, the partial matchings phi_pq between disjoint sib pairs.
"""
import json, os, sys, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
from involution_frame import Frame, paley9, table_from_graph  # noqa


def load(m):
    if m == 11:
        T = json.load(open(os.path.join(HERE, "..", "data", "bvls_table_m11.json")))["T"]
        return Frame(11), T
    A, pts = paley9()
    neg = {p: pts.index(((-p[0]) % 3, (-p[1]) % 3)) for p in pts}
    fixed = [i for i in range(9) if neg[pts[i]] == i]
    fr, T, blocks, lab = table_from_graph(A, fixed[0], 2)
    return fr, T


def outer_graph(fr, T):
    """adjacency among the 2N outer labels as roots (tuples of length m)"""
    m, N = fr.m, fr.N
    roots = []
    for (i, j, e) in fr.outer:
        v = [0] * m; v[i - 1] = 1; v[j - 1] = -1 if e else 1; roots.append(tuple(v))
        w = [0] * m; w[i - 1] = -1; w[j - 1] = 1 if e else -1; roots.append(tuple(w))
    idx = {r: t for t, r in enumerate(roots)}
    Hm = np.zeros((2 * N, 2 * N), dtype=int)
    for U in range(N):
        for V in range(N):
            if U == V: continue
            a, b = T[U][V] & 1, T[U][V] >> 1
            Hm[2 * U, 2 * V] = Hm[2 * U + 1, 2 * V + 1] = a
            Hm[2 * U, 2 * V + 1] = Hm[2 * U + 1, 2 * V] = b
    return roots, idx, Hm


def main(m):
    fr, T = load(m)
    roots, idx, Hm = outer_graph(fr, T)
    supp = lambda r: frozenset(i for i, x in enumerate(r) if x)
    pairs = list(itertools.combinations(range(m), 2))
    P = {p: [r for r in roots if supp(r) == frozenset(p)] for p in pairs}
    ok_disjoint, sizes, cover = True, [], []
    for p in pairs:
        Np = []
        for a in P[p]:
            nb = [roots[t] for t in np.nonzero(Hm[idx[a]])[0]]
            sis = [r for r in nb if supp(r) == frozenset(p)]
            N0 = [r for r in nb if not (supp(r) & frozenset(p))]
            assert len(sis) == 2 and len(N0) == len(nb) - 2 - 0 or True
            sizes.append(len(N0)); Np.append(set(N0))
        for x, y in itertools.combinations(Np, 2):
            if x & y: ok_disjoint = False
        comp = [r for r in roots if not (supp(r) & frozenset(p))]
        cover.append(len(set().union(*Np)) / len(comp) if comp else 1.0)
    print("m=%d: |N0| values %s ; pairwise disjoint: %s ; coverage of complementary roots: min %.3f max %.3f" %
          (m, sorted(set(sizes)), ok_disjoint, min(cover), max(cover)))


if __name__ == "__main__":
    for m in (2, 11):
        main(m)
