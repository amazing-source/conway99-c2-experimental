"""Microscope on the positive controls (m=2: srg(9,4,1,2); m=11: BvLS srg(243,22,1,2)).

Checks the Z^m / D_m-root / F_3 Hamming-ball picture and computes candidate invariants:
  - D-edge types (sib/one/dis), s=1 edge types (sister or not), grids at the root
  - p-ranks of S - rI for p | (r - s), Smith normal form of rI - S, lattice determinants
"""
import json, sys, os, itertools
import numpy as np
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
from involution_frame import Frame, paley9, table_from_graph  # noqa

def load_table(m):
    if m == 11:
        T = json.load(open(os.path.join(HERE, "..", "data", "bvls_table_m11.json")))["T"]
        return Frame(11), T
    if m == 2:
        A, pts = paley9()
        neg = {p: pts.index(((-p[0]) % 3, (-p[1]) % 3)) for p in pts}
        fixed = [i for i in range(9) if neg[pts[i]] == i]
        fr, T, blocks, lab = table_from_graph(A, fixed[0], 2)
        return fr, T
    raise ValueError

def full_S(fr, T):
    m, N = fr.m, fr.N
    S = np.zeros((m + N, m + N), dtype=np.int64)
    S[:m, :m] = -np.eye(m, dtype=np.int64)
    S[m:, :m] = fr.C; S[:m, m:] = fr.C.T
    S[m:, m:] = fr.S_out(T)
    return S

def rank_mod_p(M, p):
    M = (np.array(M, dtype=np.int64) % p).copy(); rows, cols = M.shape; rk = 0
    for c in range(cols):
        piv = next((i for i in range(rk, rows) if M[i, c]), None)
        if piv is None: continue
        M[[rk, piv]] = M[[piv, rk]]
        inv = pow(int(M[rk, c]), -1, p); M[rk] = (M[rk] * inv) % p
        for i in range(rows):
            if i != rk and M[i, c]: M[i] = (M[i] - M[i, c] * M[rk]) % p
        rk += 1
    return rk

def dtype_pair(U, V):
    (i, j, e), (k, l, f) = U, V
    sh = len({i, j} & {k, l})
    if sh == 2: return "sib"
    return "one" if sh == 1 else "dis"

def main(m):
    fr, T = load_table(m)
    k, r, s = fr.k, fr.r, fr.s
    Q = fr.Q_out(T); S = fr.S_out(T)
    N = fr.N; outer = fr.outer
    print("=== m=%d k=%d r=%d s=%d  d=r-s=%d  N=%d" % (m, k, r, s, r - s, N))
    # D edges
    Dt = {"sib": 0, "one": 0, "dis": 0}
    for U in range(N):
        for V in range(U + 1, N):
            if Q[U, V] == 2: Dt[dtype_pair(outer[U], outer[V])] += 1
    print("D-edge types:", Dt)
    # s=1 edges: rep labels; an edge between labels sharing exactly one inner vertex
    # label of rep U=(i,j,e): {(i,0),(j,e)}; sigma-rep {(i,1),(j,1-e)}; a=A[u,v], b=A[u,sigma v]
    def lab(U, side):
        i, j, e = outer[U]
        return frozenset([(i, side), (j, e ^ side)])
    s1 = {"sister": 0, "nonsister": 0}
    for U in range(N):
        for V in range(N):
            if U == V: continue
            a, b = T[U][V] & 1, T[U][V] >> 1
            u = lab(U, 0)
            for bit, v in ((a, lab(V, 0)), (b, lab(V, 1))):
                if bit and len(u & v) == 1:
                    key = "sister" if {outer[U][0], outer[U][1]} == {outer[V][0], outer[V][1]} else "nonsister"
                    s1[key] += 1
    print("s=1 edge ends from reps (each s=1 edge counted per endpoint rep):", s1)
    # full S, spectra, p-ranks
    Sf = full_S(fr, T)
    n = Sf.shape[0]
    assert np.array_equal(Sf @ Sf + Sf, (k - 2) * np.eye(n, dtype=np.int64))
    d = r - s
    primes = sorted(sp.factorint(d).keys())
    for p in primes:
        print("rank_F%d(S - rI) = %d   (rank over Q = g_S = %d)" % (p, rank_mod_p(Sf - r * np.eye(n, dtype=np.int64), p), fr.gS))
    # p-adic Smith normal form of rI - S (rank g_S) and S - sI (rank f_S), p | d
    from padic import padic_elementary_divisors
    from collections import Counter
    for p in primes:
        for name, M in (("rI-S", r * np.eye(n, dtype=np.int64) - Sf), ("S-sI", Sf - s * np.eye(n, dtype=np.int64))):
            ex = padic_elementary_divisors(M, p)
            print("  %d-adic SNF(%s): rank %d, exponents %s" % (p, name, len(ex), sorted(Counter(ex).items())))

if __name__ == "__main__":
    for m in (2, 11):
        main(m)
