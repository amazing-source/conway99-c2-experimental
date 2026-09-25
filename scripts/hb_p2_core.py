"""Infeasibility core of the pair-level system (hb_pairlevel.py) on one H-beta skeleton + one free-cycle choice (note 31).
Groups of constraints get enforcement literals; CP-SAT assumptions give a sufficient subset, then deletion-minimisation.
Only DEFINITIVE answers are used (INFEASIBLE for the subset); an UNKNOWN keeps the group (conservative)."""
import sys, time, itertools
from collections import defaultdict
from ortools.sat.python import cp_model
sys.path.insert(0, "scripts")
import hb_pairlevel as H
N = H.N; P = H.P; PAIRS = H.PAIRS

def model(orbits, nbs, active=None):
    known = {}
    for z in orbits:
        i, j, k = z
        for R in PAIRS:
            if R == P(i, j): known[z, R] = 0
            elif i in R: known[z, R] = 2 if R == P(i, k) else 0
            elif j in R: known[z, R] = sum(1 for w in nbs[j][z] if P(w[0], w[1]) == R)
    m = cp_model.CpModel(); var = {}
    for z in orbits:
        for R in PAIRS:
            if (z, R) not in known: var[z, R] = m.NewIntVar(0, 2, "")
    val = lambda z, R: known[z, R] if (z, R) in known else var[z, R]
    groups = {}
    def grp(name, cons_fn):
        if active is not None and name not in active: return
        lit = m.NewBoolVar(str(name)); groups[name] = lit
        for c in cons_fn(): c.OnlyEnforceIf(lit)
    for z in orbits:
        i, j, k = z
        for t in range(N):
            if t in (i, j): continue
            grp(('L', z, t), lambda z=z, t=t: [m.Add(sum(val(z, R) for R in PAIRS if t in R) == 4)])
    pairs_of = defaultdict(list)
    for z in orbits: pairs_of[P(z[0], z[1])].append(z)
    E = {(R, R2): sum(val(y, R2) for y in pairs_of[R]) for R in PAIRS for R2 in PAIRS if R != R2}
    for ia, R in enumerate(PAIRS):
        grp(('S', R), lambda R=R: [m.Add(sum(val(z, R) for z in orbits) == 24)])
        for R2 in PAIRS[ia + 1:]:
            grp(('C', R, R2), lambda R=R, R2=R2: [m.Add(E[R, R2] == E[R2, R])])
    prod = {}
    def pr(z, R, R2):
        a, b = val(z, R), val(z, R2)
        if isinstance(a, int) or isinstance(b, int): return a * b
        key = (z, frozenset((R, R2)))
        if key not in prod:
            p = m.NewIntVar(0, 4, ""); m.AddMultiplicationEquality(p, [a, b]); prod[key] = p
        return prod[key]
    for ia, R in enumerate(PAIRS):
        for R2 in PAIRS[ia:]:
            rhs = 32 if R == R2 else 16 - E[R, R2] - (4 if R & R2 else 0)
            grp(('P2', R, R2), lambda R=R, R2=R2, rhs=rhs: [m.Add(sum(pr(z, R, R2) for z in orbits) == rhs)])
    return m, groups

def solve(orbits, nbs, active, secs, assume=False):
    m, groups = model(orbits, nbs, active)
    if assume: m.AddAssumptions(list(groups.values()))
    else:
        for l in groups.values(): m.Add(l == 1)
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = secs
    s.parameters.num_workers = 1 if assume else 8
    st = s.Solve(m)
    core = None
    if assume and st == cp_model.INFEASIBLE:
        idx = set(s.SufficientAssumptionsForInfeasibility())
        core = [g for g, l in groups.items() if l.Index() in idx]
    return s.StatusName(st), core

if __name__ == "__main__":
    orient, order, ci = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    In, orbits = H.skeleton(orient, order)
    cyc0 = H.free_cycles(orbits, 0, True)
    nb0 = cyc0[ci]
    nbs = {s: {H.rot(z, s): [H.rot(w, s) for w in ws] for z, ws in nb0.items()} for s in range(N)}
    t0 = time.time()
    st, core = solve(orbits, nbs, None, 120, assume=True)
    print("full:", st, "| assumption core size:", None if core is None else len(core), "%.0fs" % (time.time() - t0)); sys.stdout.flush()
    if core is None: sys.exit()
    act = set(core)
    for g in sorted(core, key=lambda g: {'P2': 0, 'C': 1, 'S': 2, 'L': 3}[g[0]]):
        if time.time() - t0 > 250: break
        trial = act - {g}
        st2, _ = solve(orbits, nbs, trial, 10)
        if st2 == "INFEASIBLE": act = trial
    print("minimised core size:", len(act), "%.0fs" % (time.time() - t0))
    from collections import Counter
    print("by type:", Counter(g[0] for g in act))
    for g in sorted(act, key=str): print("  ", g[0], [sorted(x) if isinstance(x, frozenset) else x for x in g[1:]])
