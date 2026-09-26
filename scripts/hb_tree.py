"""Capped computer-assisted search on H-beta (note 32; approved by the user 26/09, cap ~3 h).
LP relaxation of the first-order pair-level system F2 (L + PPE + S + C, note 31) with the free cycles of the UNFIXED blocks relaxed
to the convex hull of their valid 6-cycles (19.1 + typed rule): variables lambda_c >= 0, sum = 1, and every near quantity
(n_r(Z), n_r(Z)^2) is the lambda-combination of its exact values.  Far values: indicators a (phi=1), b (phi=2), a+b <= 1.
Depth-first over blocks; a node is pruned when its LP is infeasible (min total slack > tol); the dual y is kept as a certificate
and re-checked in exact rational arithmetic by verify_certificate() (bound argument: for every feasible point y^T b = y^T A x
lies in [LB, UB] computed exactly over the box/simplex structure).
"""
import sys, itertools, time, json
from fractions import Fraction
from collections import defaultdict
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix
sys.path.insert(0, "scripts")
import hb_pairlevel as H
N = H.N; P = H.P; PAIRS = H.PAIRS

class Instance:
    def __init__(self, orbits):
        self.orbits = orbits
        self.pair = {z: P(z[0], z[1]) for z in orbits}
        self.cycles = {j: H.free_cycles(orbits, j, True) for j in range(N)}
        self.pairs_of = defaultdict(list)
        for z in orbits: self.pairs_of[self.pair[z]].append(z)
        self.far = [(z, R) for z in orbits for R in PAIRS if not (R & self.pair[z])]
        # exact near data per block and cycle: nv[j][c][(z,R)] = n value (R contains j, z free at j, i_z not in R)
        self.nv = {}
        for j in range(N):
            self.nv[j] = []
            for nb in self.cycles[j]:
                d = {}
                for z, ws in nb.items():
                    for r in range(N):
                        if r in (z[0], j): continue
                        d[z, P(j, r)] = sum(1 for w in ws if self.pair[w] == P(j, r))
                self.nv[j].append(d)

    def build(self, fixed):
        """fixed: dict block -> cycle index.  Returns (A (m x n) as dict rows, b, bounds info, var index)."""
        col = {}
        for f in self.far: col[f, 'a'] = len(col); col[f, 'b'] = len(col)
        for j in range(N):
            if j in fixed: continue
            for c in range(len(self.cycles[j])): col['lam', j, c] = len(col)
        rows = []
        def near_terms(z, R, power):
            """(constant, {col: coef}) for phi_z(R)^power when R meets P_z."""
            i, j, k = z
            if R == self.pair[z]: return 0, {}
            if i in R: v = 2 if R == P(i, k) else 0; return v ** power, {}
            if j in fixed: v = self.nv[j][fixed[j]][z, R]; return v ** power, {}
            d = {}
            for c in range(len(self.cycles[j])):
                v = self.nv[j][c][z, R]
                if v: d[col['lam', j, c]] = v ** power
            return 0, d
        def val_terms(z, R, power=1):
            if (z, R) in col or (z, R, 'a') in col: pass
            if not (R & self.pair[z]):
                return 0, {col[(z, R), 'a']: 1, col[(z, R), 'b']: (2 if power == 1 else 4)}
            return near_terms(z, R, power)
        def add(terms_list, rhs, name):
            d = defaultdict(float); const = 0
            for (cst, dd, sgn) in terms_list:
                const += sgn * cst
                for k2, v in dd.items(): d[k2] += sgn * v
            rows.append((dict(d), rhs - const, name))
        for z in self.orbits:
            i, j, k = z
            for t in range(N):
                if t in (i, j): continue
                add([(*val_terms(z, R), 1) for R in PAIRS if t in R], 4, ('L', z, t))
        for R in PAIRS:
            add([(*val_terms(z, R, 2), 1) for z in self.orbits], 32, ('D', R))
            add([(*val_terms(z, R), 1) for z in self.orbits], 24, ('S', R))
        for ia, R in enumerate(PAIRS):
            for R2 in PAIRS[ia + 1:]:
                if R & R2: continue
                add([(*val_terms(y, R2), 1) for y in self.pairs_of[R]] + [(*val_terms(y, R), -1) for y in self.pairs_of[R2]], 0, ('C', R, R2))
        for j in range(N):
            if j in fixed: continue
            rows.append(({col['lam', j, c]: 1 for c in range(len(self.cycles[j]))}, 1, ('lam', j)))
        return rows, col

    def lp(self, fixed):
        rows, col = self.build(fixed)
        nv = len(col); m = len(rows); nf = len(self.far)
        A = lil_matrix((m, nv + 2 * m)); b = np.zeros(m)
        for r, (d, rhs, _) in enumerate(rows):
            for c, v in d.items(): A[r, c] = v
            A[r, nv + r] = 1; A[r, nv + m + r] = -1; b[r] = rhs
        G = lil_matrix((nf, nv + 2 * m))
        for t, f in enumerate(self.far): G[t, col[f, 'a']] = 1; G[t, col[f, 'b']] = 1
        cost = np.concatenate([np.zeros(nv), np.ones(2 * m)])
        res = linprog(cost, A_ub=G.tocsr(), b_ub=np.ones(nf), A_eq=A.tocsr(), b_eq=b,
                      bounds=[(0, 1)] * nv + [(0, None)] * (2 * m), method="highs")
        return res, rows, col

def verify_certificate(inst, fixed, y, rows=None, col=None):
    """Exact check: with y rational (one weight per equality row), c = A^T y.  Over the feasible region of the non-row constraints
    (far pairs: a,b >= 0, a+b <= 1 ; lambda >= 0 with sum = 1 per block is a ROW, so lambda only has lambda >= 0, lambda <= 1),
    y^T A x ranges in [LB, UB] with LB/UB computed exactly per far value (max/min over {0, c_a, c_b}) and per lambda (box [0,1]).
    Infeasible iff y^T b > UB or y^T b < LB."""
    if rows is None: rows, col = inst.build(fixed)
    c = defaultdict(Fraction); yb = Fraction(0)
    for r, (d, rhs, _) in enumerate(rows):
        if y[r] == 0: continue
        yb += y[r] * Fraction(rhs).limit_denominator(10 ** 9) if not isinstance(rhs, int) else y[r] * rhs
        for k2, v in d.items(): c[k2] += y[r] * Fraction(v).limit_denominator(10 ** 9)
    UB = Fraction(0); LB = Fraction(0)
    inv = {v: k for k, v in col.items()}
    seen = set()
    for key, idx in col.items():
        if key[0] == 'lam':
            cv = c.get(idx, Fraction(0)); UB += max(cv, 0); LB += min(cv, 0)
        else:
            f = key[0]
            if f in seen: continue
            seen.add(f)
            ca = c.get(col[f, 'a'], Fraction(0)); cb = c.get(col[f, 'b'], Fraction(0))
            UB += max(Fraction(0), ca, cb); LB += min(Fraction(0), ca, cb)
    return yb > UB or yb < LB, (yb, LB, UB)

def rational_dual(res, rows, den=10 ** 6):
    y = res.eqlin.marginals[:len(rows)]
    return [Fraction(v).limit_denominator(den) if abs(v) > 1e-9 else Fraction(0) for v in y]
