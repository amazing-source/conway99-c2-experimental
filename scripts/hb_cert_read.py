"""Readable form of an H-beta certificate (note 33; suggestion of C1).  Circulant skeleton: solve, take the 21x21 matrix W of the
(P2)+(PPE) multipliers, symmetrise it over Z7 (as a matrix on pairs), and test LOW-RANK restrictions: replace all (P2)/(PPE) rows by
the contracted rows  sum_{a,b} c_a c_b (P2/PPE)[a,b]  for the top-|eigenvalue| eigenvectors c of W (all linear rows kept).
If such a restricted LP is still infeasible, the proof reads as a few Rayleigh-type identities plus a table of column types."""
import sys, time, itertools, copy
from collections import defaultdict
from fractions import Fraction
import numpy as np
sys.path.insert(0, "scripts")
import hb_pairlevel as H, hb_colmodel as CM
N = H.N; PAIRS = H.PAIRS; PI = {R: t for t, R in enumerate(PAIRS)}
orient, order = sys.argv[1], int(sys.argv[2])
In, orbits = H.skeleton(orient, order)
cm = CM.ColModel(orbits, True)
obj = cm.solve(); y = np.array(cm.h.getSolution().row_dual)[:len(cm.rows)]
print("full model slack %.3f" % obj)
W = np.zeros((21, 21)); p2rows = {}
for r, row in enumerate(cm.rows):
    nm = row[3]
    if nm[0] == 'D': W[PI[nm[1]], PI[nm[1]]] += y[r]; p2rows[PI[nm[1]], PI[nm[1]]] = r
    if nm[0] == 'P2': a, b = PI[nm[1]], PI[nm[2]]; W[a, b] += y[r] / 2; W[b, a] += y[r] / 2; p2rows[min(a, b), max(a, b)] = r
rotP = [PI[frozenset((v + 1) % N for v in R)] for R in PAIRS]
Ws = np.zeros_like(W); Pm = np.eye(21)
for s in range(N):
    Ws += Pm @ W @ Pm.T / N
    Pm = np.eye(21)[rotP] @ Pm
ev, V = np.linalg.eigh(Ws)
print("eigenvalues of Z7-symmetrised W:", np.round(ev, 3))
base_rows = [row for row in cm.rows if row[3][0] not in ('D', 'P2')]
def restricted(vecs):
    rows = list(base_rows)
    for t, c in enumerate(vecs):
        terms = defaultdict(float); rhs = 0.0
        for (a, b), r in p2rows.items():
            w = c[a] * c[b] * (1 if a == b else 2)
            if abs(w) < 1e-12: continue
            tr, rh, _, _ = cm.rows[r]
            for col, v in tr: terms[col] += w * v
            rhs += w * rh
        rows.append((list(terms.items()), rhs, 'eq', ('rank', t)))
    cm2 = copy.copy(cm); cm2.rows = rows
    return cm2.solve()
order_ev = np.argsort(-np.abs(ev))
for r_ in (1, 2, 3, 4, 6, 8, 12, 21):
    vecs = [V[:, i] for i in order_ev[:r_]]
    print("rank %2d restriction (top |eigenvalues|): LP slack %.4f" % (r_, restricted(vecs))); sys.stdout.flush()
# also: the Johnson-scheme idempotents of T(7) (pairs), i.e. W constant on |R cap R'| classes
A1 = np.array([[1.0 if (R != S and R & S) else 0 for S in PAIRS] for R in PAIRS])
ew, U = np.linalg.eigh(A1)
print("Johnson eigen-spaces (eigenvalues of T(7) adjacency):", sorted(set(np.round(ew, 3))))
for lam in sorted(set(np.round(ew, 6))):
    vecs = [U[:, i] for i in range(21) if abs(ew[i] - lam) < 1e-6]
    print("  restriction to T(7) eigenspace %.1f (dim %d): LP slack %.4f" % (lam, len(vecs), restricted(vecs)))
