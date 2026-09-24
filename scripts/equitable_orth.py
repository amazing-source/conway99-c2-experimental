"""Orthogonality test between lifted eigenvectors of the equitable partitions pi_p of different sib pairs (m=7).

For a sib pair p, pi_p = {x | I_p | I_rest | P_p | T_p | R_p^c} is equitable (Lemma S1, notes/03), quotient B with spectrum {14, 3^3, (-4)^2}.
Its cells are defined by blocks only, so the lifted eigenvectors P_p u are KNOWN vectors in R^99.  For two sib pairs p, q, lifted eigenvectors
for different eigenvalues must be orthogonal (A symmetric).  Also: all lifted eigenvectors for eigenvalue theta span an A-invariant space
inside the theta-eigenspace, so the Gram structure must be consistent.  Any violation => the configuration of sib pairs is impossible.
"""
import itertools
import numpy as np
import sympy as sp

M = 7
INNER = [(i, s) for i in range(1, M + 1) for s in (1, -1)]
ROOTS = []
for i, j in itertools.combinations(range(1, M + 1), 2):
    for a in (1, -1):
        for b in (1, -1):
            ROOTS.append(((i, a), (j, b)))
VERTS = ["x"] + INNER + ROOTS
assert len(VERTS) == 99


def cells(p):
    p = set(p)
    lab = []
    for v in VERTS:
        if v == "x": lab.append(0)
        elif isinstance(v[0], int):   # inner (i, s)
            lab.append(1 if v[0] in p else 2)
        else:
            blk = {v[0][0], v[1][0]}
            k = len(blk & p)
            lab.append({2: 3, 1: 4, 0: 5}[k])
    return np.array(lab)


B = sp.Matrix([[0, 4, 10, 0, 0, 0], [1, 1, 0, 2, 10, 0], [1, 0, 1, 0, 4, 8], [0, 2, 0, 2, 0, 10], [0, 1, 1, 0, 6, 6], [0, 0, 2, 1, 6, 5]])
EIG = {}
for val, mult, vecs in B.eigenvects():
    EIG[int(val)] = [np.array([float(c) for c in v], dtype=float) for v in vecs]


def lifted(p, theta):
    lab = cells(p)
    return [np.array([u[l] for l in lab]) for u in EIG[theta]]


def test(pairs, verbose=True):
    worst = 0.0
    for p, q in itertools.combinations(pairs, 2):
        for t1 in (14, 3, -4):
            for t2 in (14, 3, -4):
                if t1 == t2: continue
                for u in lifted(p, t1):
                    for w in lifted(q, t2):
                        ip = abs(u @ w) / (np.linalg.norm(u) * np.linalg.norm(w))
                        worst = max(worst, ip)
    if verbose:
        print("pairs %s : max |cos| between lifted eigenvectors of different eigenvalues = %.3e" % (pairs, worst))
    return worst


if __name__ == "__main__":
    # sanity: a single pair's own lifted eigenvectors are orthogonal across eigenvalues
    test([(1, 2)])
    for conf in ([(1, 2), (3, 4)], [(1, 2), (1, 3)], [(1, 2), (3, 4), (5, 6)], [(1, 2), (1, 3), (2, 3)]):
        test(conf)
    # also: dimension check of the span of all lifted theta-eigenvectors (must be <= multiplicity and A-invariant)
    for conf in ([(1, 2), (3, 4)], [(1, 2), (1, 3)], list(itertools.combinations(range(1, 8), 2))):
        for t in (3, -4):
            V = np.array([v for p in conf for v in lifted(p, t)])
            print("conf with %d pairs, theta=%d: span dim %d" % (len(conf), t, np.linalg.matrix_rank(V, tol=1e-8)))
