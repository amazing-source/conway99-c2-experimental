"""Pair-level (second-order) test on H-beta skeletons -- note 31.  SMALL TEST (<= 5 min, rule of 25/09), definitive answers only.

Unknowns: phi_Z(R) in {0,1,2} for every orbit Z and every pair R disjoint from P_Z (the far values).
Known (from the skeleton + the free 6-cycles): phi_Z(P_Z) = 0; phi_Z({i,r}) = 2[r = k] (F1); phi_Z({j,r}) = n_r(Z) (free cycle at j).
Constraints (all proved):
  (L)  per orbit Z = (i,j,k), per block t not in {i,j}:  sum_{R containing t} phi_Z(R) = 4          (mu = 2 at (t,+-), lambda at k)
  (C)  coupling: E[R][R'] = E[R'][R], with E[R][R'] = sum_{Y in R} phi_Y(R')                          (edges between root sets)
  (S)  column sums: sum_Z phi_Z(R) = 24
  (P2) sum_Z phi_Z(R) phi_Z(R') = 16 - E[R][R'] - 4[R meets R']  (R != R'),  sum_Z phi_Z(R)^2 = 32         (lambda/mu summed on R x R')
Free 6-cycles (19.1): no sister edge, sisters <= 1 common neighbour; typed rule (note 30 §4): Z=(i,j,k) never has both
cycle-neighbours in the pair {j,k}.
Modes: symmetric (Z7-invariant skeleton, cycles and phi imposed Z7-invariant) -- a test of the LEVER's strength only.
Usage: python hb_pairlevel.py <orient: 23|2m3> <order: 0|1> <seconds per cycle choice> [--noP2] [--untyped]
"""
import itertools, sys, time
from collections import Counter, defaultdict
from ortools.sat.python import cp_model
N = 7
P = lambda a, b: frozenset((a % N, b % N))
PAIRS = [P(a, b) for a in range(N) for b in range(a + 1, N)]

def skeleton(orient, order):
    In = {}
    for c in range(N):
        I = [(c - 2) % N, (c - 3) % N] if orient == "23" else [(c - 2) % N, (c + 3) % N]
        In[c] = I if order == 0 else I[::-1]          # In[c] = [A_c, B_c]
    orbits = []                                        # (i, j, k)
    for c in range(N):
        A, B = In[c]
        seq = [(c - 1) % N, A, B, (c + 1) % N]
        for x, y in zip(seq, seq[1:]): orbits += [(c, x, y), (c, y, x)]
    return In, orbits

def free_cycles(orbits, j, typed):
    fr = [z for z in orbits if z[1] == j]
    assert len(fr) == 6
    pair = {z: P(z[0], z[1]) for z in fr}
    sis = {(a, b) for a in fr for b in fr if a != b and pair[a] == pair[b]}
    res = []
    first = fr[0]
    for perm in itertools.permutations(fr[1:]):
        if perm[0] > perm[-1]: continue
        cyc = (first,) + perm
        nb = {z: [] for z in fr}
        for t in range(6):
            a, b = cyc[t], cyc[(t + 1) % 6]; nb[a].append(b); nb[b].append(a)
        if any((a, b) in sis for a in fr for b in nb[a]): continue
        if any(len(set(nb[a]) & set(nb[b])) > 1 for (a, b) in sis): continue
        if typed and any(all(pair[w] == P(z[1], z[2]) for w in nb[z]) for z in fr): continue
        res.append(nb)
    return res

def rot(z, s): return tuple((v + s) % N for v in z)

def build_and_solve(orbits, nbs, secs, useP2, sym):
    # nbs[j] = neighbour dict at block j
    known = {}
    for z in orbits:
        i, j, k = z
        for R in PAIRS:
            if R == P(i, j): known[z, R] = 0
            elif i in R: known[z, R] = 2 if R == P(i, k) else 0
            elif j in R:
                r = next(iter(R - {j})); known[z, R] = sum(1 for w in nbs[j][z] if P(w[0], w[1]) == R)
    m = cp_model.CpModel(); var = {}
    def cls(z, R):
        if not sym: return (z, R)
        s = (-z[0]) % N
        return (rot(z, s), frozenset((v + s) % N for v in R))
    for z in orbits:
        for R in PAIRS:
            if (z, R) in known: continue
            c = cls(z, R)
            if c not in var: var[c] = m.NewIntVar(0, 2, "p%d" % len(var))
    val = lambda z, R: known[z, R] if (z, R) in known else var[cls(z, R)]
    # (L)
    for z in orbits:
        i, j, k = z
        for t in range(N):
            if t in (i, j): continue
            terms = [val(z, R) for R in PAIRS if t in R]
            m.Add(sum(terms) == 4)
    pairs_of = defaultdict(list)
    for z in orbits: pairs_of[P(z[0], z[1])].append(z)
    E = {(R, R2): sum(val(y, R2) for y in pairs_of[R]) for R in PAIRS for R2 in PAIRS if R != R2}
    for R in PAIRS:
        m.Add(sum(val(z, R) for z in orbits) == 24)
        for R2 in PAIRS:
            if R != R2 and PAIRS.index(R) < PAIRS.index(R2):
                m.Add(E[R, R2] == E[R2, R])
    if useP2:
        prod = {}
        def pr(z, R, R2):
            a, b = val(z, R), val(z, R2)
            if isinstance(a, int) or isinstance(b, int):
                return a * b
            key = (cls(z, R), cls(z, R2)) if sym else (z, R, R2)
            key2 = (cls(z, R2), cls(z, R)) if sym else (z, R2, R)
            if key2 in prod: return prod[key2]
            if key not in prod:
                p = m.NewIntVar(0, 4, "q%d" % len(prod)); m.AddMultiplicationEquality(p, [a, b]); prod[key] = p
            return prod[key]
        for ia, R in enumerate(PAIRS):
            for R2 in PAIRS[ia:]:
                lhs = sum(pr(z, R, R2) for z in orbits)
                if R == R2: m.Add(lhs == 32)
                else: m.Add(lhs == 16 - E[R, R2] - (4 if R & R2 else 0))
    sol = cp_model.CpSolver(); sol.parameters.max_time_in_seconds = secs; sol.parameters.num_workers = 8
    st = sol.Solve(m)
    return sol.StatusName(st), len(var)

if __name__ == "__main__":
    orient, order, secs = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
    useP2 = "--noP2" not in sys.argv; typed = "--untyped" not in sys.argv
    In, orbits = skeleton(orient, order)
    cyc0 = free_cycles(orbits, 0, typed)
    t0 = time.time(); out = Counter()
    print("skeleton", orient, "order", order, "In:", In, "| free 6-cycles at block 0:", len(cyc0), "| P2" if useP2 else "| no P2", "| typed" if typed else "| untyped")
    for ci, nb0 in enumerate(cyc0):
        nbs = {}
        for s in range(N):
            nbs[s] = {rot(z, s): [rot(w, s) for w in ws] for z, ws in nb0.items()}
        stname, nv = build_and_solve(orbits, nbs, secs, useP2, "--asym" not in sys.argv)
        out[stname] += 1
        print("  cycle", ci, stname, "(%d far classes)" % nv, "%.0fs" % (time.time() - t0)); sys.stdout.flush()
    print("summary:", dict(out), "time %.0fs" % (time.time() - t0))
