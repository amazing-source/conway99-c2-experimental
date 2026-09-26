"""Experiment (note 43): structures' pair-level model + the GENERAL BALANCE IDENTITY (star) for arbitrary block sets S, as a MILP.
(star)  for a block k and a set S of blocks (k not in S), Lab = orbits of the pairs {k,m}, m in S, g_o = sum_{m in S} phi_o(km):
        sum_{W: k not in P_W} delta_W^2 + sum_{W through k, W not in Lab} eps_W^2 = sum_{o in Lab} (2 - g_o)(g_o + 5),
        delta_W = |P_W & S| + sum_{m in S} phi_W(km) - |S|,  eps_W = sum_{m in S} phi_W(km).
(proof: f = s e_x + s 1_{(k,+-)} + 1_{(m,+-), m in S} + 1_Lab, |E_{-4} f|^2 = (8s - 2E_L)/7 and A f = 3f + s 1 - 7 E_{-4} f.)
Squares linearised exactly by one-hot variables over the (small) integer range.  Test only (no certificate).
Usage: python star_test.py <ci> <job> <leaf indices...>   env SETS = comps | all (default comps: the D-components at k and
their unions of size <= 2)"""
import sys, os, time, itertools
import numpy as np, scipy.sparse as sp
from scipy.optimize import milp, LinearConstraint, Bounds
sys.path.insert(0, "scripts"); sys.path.insert(0, "external_structures/ad")
import pair_blockdfs as PB
from general_model import build, pr
N = 7


def dgraph_components(orbs, k):
    adj = {m: set() for m in range(N) if m != k}
    for i, o in enumerate(orbs):
        if o['pivot'] == k and o['partner'] is not None:
            m = sum(o['pair']) - k; m2 = sum(orbs[o['partner']]['pair']) - k
            adj[m].add(m2); adj[m2].add(m)
    seen, comps = set(), []
    for m in adj:
        if m in seen or not adj[m]: continue
        comp, st = set(), [m]
        while st:
            u = st.pop()
            if u in comp: continue
            comp.add(u); st += list(adj[u] - comp)
        seen |= comp; comps.append(frozenset(comp))
    return comps


def star_model(orbs, sets_mode='comps'):
    A, lo, hi, lb, ub, nvar, phi, ns = build(orbs)
    A = sp.csr_matrix(A); rows_extra = []; lb = list(lb); ub = list(ub); nv = [nvar]
    def newvar(l, u):
        lb.append(l); ub.append(u); nv[0] += 1; return nv[0] - 1
    def onehot(lin, vals):
        """variables z_v (v in vals) with sum z = 1 and sum v z = lin (lin = list of (var, coef), const handled by caller)"""
        z = [newvar(0, 1) for _ in vals]
        rows_extra.append(([(j, 1) for j in z], 1, 1))
        return z
    n = len(orbs); pairs_of = [o['pair'] for o in orbs]
    Ss = set()
    for k in range(N):
        comps = dgraph_components(orbs, k)
        if sets_mode == 'all':
            others = [m for m in range(N) if m != k]
            for r in range(1, 6):
                for S in itertools.combinations(others, r): Ss.add((k, frozenset(S)))
        else:
            for c in comps: Ss.add((k, c))
            for c1, c2 in itertools.combinations(comps, 2): Ss.add((k, c1 | c2))
    for k, S in sorted(Ss, key=lambda t: (t[0], sorted(t[1]))):
        s = len(S); lhs = []; rhs_terms = []
        for W in range(n):
            P = pairs_of[W]
            lin = [(phi[(W, pr(k, m))], 1) for m in S if pr(k, m) != P]
            if k not in P:
                c0 = len(set(P) & S) - s; vals = list(range(c0, c0 + 2 * s + 1))
                z = onehot(lin, vals)
                rows_extra.append(([(j, v) for j, v in zip(z, vals)] + [(a, -c) for a, c in lin], c0, c0))
                lhs += [(j, v * v) for j, v in zip(z, vals)]
            elif sum(P) - k in S:                     # W in Lab
                vals = [0, 1, 2]; z = onehot(lin, vals)
                rows_extra.append(([(j, v) for j, v in zip(z, vals)] + [(a, -c) for a, c in lin], 0, 0))
                rhs_terms += [(j, (2 - v) * (v + 5)) for j, v in zip(z, vals)]
            else:
                vals = [0, 1, 2]; z = onehot(lin, vals)
                rows_extra.append(([(j, v) for j, v in zip(z, vals)] + [(a, -c) for a, c in lin], 0, 0))
                lhs += [(j, v * v) for j, v in zip(z, vals)]
        rows_extra.append((lhs + [(j, -c) for j, c in rhs_terms], 0, 0))
    m0 = A.shape[0]; ntot = nv[0]
    r_, c_, v_ = [], [], []
    for t, (co, l, h) in enumerate(rows_extra):
        for j, c in co: r_.append(t); c_.append(j); v_.append(c)
    E = sp.csr_matrix((v_, (r_, c_)), shape=(len(rows_extra), ntot))
    A2 = sp.vstack([sp.hstack([A, sp.csr_matrix((m0, ntot - nvar))]), E]).tocsr()
    lo2 = np.concatenate([lo, [r[1] for r in rows_extra]]); hi2 = np.concatenate([hi, [r[2] for r in rows_extra]])
    return A2, lo2, hi2, np.array(lb, float), np.array(ub, float), len(Ss)


if __name__ == "__main__":
    ci, job = sys.argv[1], int(sys.argv[2]); po = PB.load_job(ci, job); In = {int(x): v for x, v in po["In"].items()}
    for t in map(int, sys.argv[3:]):
        L = [tuple(z) for z in po["leaves"][t]]
        orbs = PB.orbit_list(In, {c: tuple(z for z in L if z[0] == c) for c in range(N) if c != po["A"]})
        for mode in (os.environ.get('SETS', 'comps'),):
            t0 = time.time(); A2, lo2, hi2, lb2, ub2, nS = star_model(orbs, mode)
            res = milp(c=np.zeros(A2.shape[1]), constraints=[LinearConstraint(A2, lo2, hi2)], integrality=np.ones(A2.shape[1]),
                       bounds=Bounds(lb2, ub2), options={'time_limit': float(os.environ.get('TL', 120))})
            print("leaf %d sets=%s (%d (k,S)) vars %d rows %d: status %d %s  %.1fs" % (t, mode, nS, A2.shape[1], A2.shape[0], res.status,
                  {0: 'FEASIBLE', 2: 'INFEASIBLE', 1: 'time/iter limit'}.get(res.status, res.message), time.time() - t0)); sys.stdout.flush()
