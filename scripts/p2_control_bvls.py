"""Control on a REAL graph for the pair-level identities used in hb_pairlevel.py (note 31):
BvLS srg(243,22,1,2) with the involution x -> -x (fixed point 0). For every root orbit Z and pair R of blocks:
phi_Z(R) = #neighbours of a representative of Z among the 4 roots of R. Checks (independent of m):
 (L) t not in P_Z: sum_{R containing t} phi_Z(R) = 4 ;  (S) sum_Z phi_Z(R) = 2(k-2) ; (C) E[R][R'] = E[R'][R] ;
 (P2) sum_Z phi_Z(R) phi_Z(R') = 16 - E[R][R'] - 4[R meets R'] (R != R'),  sum_Z phi_Z(R)^2 = 2k + 4 - e(R)  (= 32 at k = 14, e = 0)."""
import sys, itertools
import numpy as np
sys.path.insert(0, "scripts/vendor")
import control_bvls as cb
A, V, ix, cols, neg = cb.bvls()
n = A.shape[0]; k = int(A[0].sum())
x = [i for i in range(n) if ix[neg(V[i])] == i]; assert len(x) == 1; x = x[0]
inner = list(np.flatnonzero(A[x]))
lines = []; seen = set()
for a in inner:
    if a in seen: continue
    b = [c for c in inner if A[a, c]][0]; lines.append((a, b)); seen |= {a, b}
blk = {v: m for m, (a, b) in enumerate(lines) for v in (a, b)}
M = len(lines)
roots = [v for v in range(n) if v != x and v not in blk]
rpair = {}
for r in roots:
    inn = [a for a in inner if A[r, a]]; assert len(inn) == 2
    rpair[r] = frozenset(blk[a] for a in inn)
tneg = {v: ix[neg(V[v])] for v in range(n)}
orbits = []; done = set()
for r in roots:
    if r in done: continue
    orbits.append(r); done |= {r, tneg[r]}
PAIRS = [frozenset(p) for p in itertools.combinations(range(M), 2)]
rootsof = {R: [r for r in roots if rpair[r] == R] for R in PAIRS}
phi = {(z, R): int(sum(A[z, r] for r in rootsof[R])) for z in orbits for R in PAIRS}
bad = 0
for z in orbits:
    for t in range(M):
        if t in rpair[z]: continue
        if sum(phi[z, R] for R in PAIRS if t in R) != 4: bad += 1
print("BvLS: blocks", M, "orbits", len(orbits), "| (L) violations:", bad)
print("(S) column sums:", set(sum(phi[z, R] for z in orbits) for R in PAIRS), "expected", 2 * (k - 2))
E = {(R, R2): sum(phi[z, R2] for z in orbits if rpair[z] == R) for R in PAIRS for R2 in PAIRS if R != R2}
print("(C) coupling asymmetries:", sum(1 for (R, R2) in E if E[R, R2] != E[R2, R]))
viol = 0; diag = Counter = {}
for R in PAIRS:
    eR = sum(A[r, s] for r in rootsof[R] for s in rootsof[R]) // 2
    if sum(phi[z, R] ** 2 for z in orbits) != 2 * k + 4 - eR: viol += 1
    for R2 in PAIRS:
        if R == R2: continue
        lhs = sum(phi[z, R] * phi[z, R2] for z in orbits)
        if lhs != 16 - E[R, R2] - (4 if R & R2 else 0): viol += 1
print("(P2) violations (diagonal + off-diagonal, both orders):", viol, "of", len(PAIRS) ** 2)
