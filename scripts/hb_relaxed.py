"""First-order pair-level model on an H-beta SKELETON with the free cycles left as VARIABLES (note 31) -- a relaxation, sound for
infeasibility.  At each block j: edge variables x[Z,Z'] between free orbits (no sister edge), every free orbit of degree 2,
no triangle, sisters with <= 1 common neighbour, typed rule n_k <= 1;  n_r(Z) = sum of x over the free orbits of {j,r}.
(The 'single 6-cycle' condition is relaxed to 'triangle-free 2-regular', i.e. 6-cycle or two ... impossible: on 6 vertices a
triangle-free 2-regular graph IS a 6-cycle, since 4+2 has a double edge.)  Far values phi_Z(R) as in hb_pairlevel.
Constraints: (L), PPE diagonal (sum phi^2 = 32 via indicators), coupling (C), column sums (S); optional P2 off-diagonal.
Optionally fix the cycles at some blocks to the rotation of a given block-0 cycle.
Usage: python hb_relaxed.py <orient> <order> <seconds> [fix=0,1,..:cycleindex] [P2]"""
import sys, itertools, time
from collections import defaultdict
from ortools.sat.python import cp_model
sys.path.insert(0, "scripts")
import hb_pairlevel as H
N = H.N; P = H.P; PAIRS = H.PAIRS

def build(orbits, fixed_nbs, useP2):
    m = cp_model.CpModel()
    pair = {z: P(z[0], z[1]) for z in orbits}
    nval = {}          # (z, R) -> int or linear expr, for R containing j_z but not i_z
    for j in range(N):
        fr = [z for z in orbits if z[1] == j]
        if j in fixed_nbs:
            for z in fr:
                for r in range(N):
                    if r in (z[0], j): continue
                    nval[z, P(j, r)] = sum(1 for w in fixed_nbs[j][z] if pair[w] == P(j, r))
            continue
        x = {}
        for a, b in itertools.combinations(fr, 2):
            if pair[a] == pair[b]: continue          # no sister edge
            x[a, b] = x[b, a] = m.NewBoolVar("")
        for a in fr: m.Add(sum(x[a, b] for b in fr if (a, b) in x) == 2)
        for a, b, c in itertools.combinations(fr, 3):
            if (a, b) in x and (b, c) in x and (a, c) in x: m.Add(x[a, b] + x[b, c] + x[a, c] <= 2)
        for a, b in itertools.combinations(fr, 2):
            if pair[a] != pair[b]: continue
            com = []
            for c in fr:
                if (a, c) in x and (b, c) in x:
                    y = m.NewBoolVar(""); m.AddMultiplicationEquality(y, [x[a, c], x[b, c]]); com.append(y)
            m.Add(sum(com) <= 1)
        for z in fr:
            for r in range(N):
                if r in (z[0], j): continue
                nval[z, P(j, r)] = sum(x[z, w] for w in fr if (z, w) in x and pair[w] == P(j, r))
            m.Add(nval[z, P(j, z[2])] <= 1)          # typed rule
    val = {}; ind = {}
    for z in orbits:
        i, j, k = z
        for R in PAIRS:
            if R == pair[z]: val[z, R] = 0
            elif i in R: val[z, R] = 2 if R == P(i, k) else 0
            elif j in R: val[z, R] = nval[z, R]
            else:
                v = m.NewIntVar(0, 2, ""); val[z, R] = v
    # square of each value, via indicators
    def sq(z, R):
        v = val[z, R]
        if isinstance(v, int): return v * v
        key = (z, R)
        if key not in ind:
            b2 = m.NewBoolVar(""); b1 = m.NewBoolVar("")
            vv = v if isinstance(v, cp_model.IntVar) else None
            if vv is None:
                vv = m.NewIntVar(0, 2, ""); m.Add(vv == v)
            m.Add(vv == 2).OnlyEnforceIf(b2); m.Add(vv != 2).OnlyEnforceIf(b2.Not())
            ind[key] = (vv, b2)
        vv, b2 = ind[key]
        return vv + 2 * b2          # v^2 = v + 2[v=2] for v in {0,1,2}
    for z in orbits:
        i, j, k = z
        for t in range(N):
            if t in (i, j): continue
            m.Add(sum(val[z, R] for R in PAIRS if t in R) == 4)
    pairs_of = defaultdict(list)
    for z in orbits: pairs_of[pair[z]].append(z)
    E = {(R, R2): sum(val[y, R2] for y in pairs_of[R]) for R in PAIRS for R2 in PAIRS if R != R2}
    for ia, R in enumerate(PAIRS):
        m.Add(sum(val[z, R] for z in orbits) == 24)
        m.Add(sum(sq(z, R) for z in orbits) == 32)
        for R2 in PAIRS[ia + 1:]:
            m.Add(E[R, R2] == E[R2, R])
    if useP2:
        for ia, R in enumerate(PAIRS):
            for R2 in PAIRS[ia + 1:]:
                terms = []
                for z in orbits:
                    a, b = val[z, R], val[z, R2]
                    if isinstance(a, int) or isinstance(b, int): terms.append(a * b); continue
                    aa = m.NewIntVar(0, 2, ""); bb = m.NewIntVar(0, 2, ""); m.Add(aa == a); m.Add(bb == b)
                    p = m.NewIntVar(0, 4, ""); m.AddMultiplicationEquality(p, [aa, bb]); terms.append(p)
                m.Add(sum(terms) == 16 - E[R, R2] - (4 if R & R2 else 0))
    return m

if __name__ == "__main__":
    orient, order, secs = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
    useP2 = "P2" in sys.argv[4:]
    In, orbits = H.skeleton(orient, order)
    fixed = {}
    for a in sys.argv[4:]:
        if a.startswith("fix="):
            blocks, ci = a[4:].split(":"); nb0 = H.free_cycles(orbits, 0, True)[int(ci)]
            for s in [int(b) for b in blocks.split(",")]:
                fixed[s] = {H.rot(z, s): [H.rot(w, s) for w in ws] for z, ws in nb0.items()}
    t0 = time.time()
    m = build(orbits, fixed, useP2)
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = secs; s.parameters.num_workers = 8
    st = s.Solve(m)
    print("skeleton", orient, order, "| fixed blocks", sorted(fixed), "| P2" if useP2 else "| first order", "->", s.StatusName(st), "%.0fs" % (time.time() - t0))
