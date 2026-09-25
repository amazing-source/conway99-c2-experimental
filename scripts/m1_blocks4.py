# Block-level SOUND filter v4 = v2/v3 + the TYPED rule of note 30 (from "structures" 26/09, re-derived by hand):
#   for an orbit x = (i, j, k), its two R_j-neighbours are never both in the pair {j, k}  (n_k <= 1).
#   Proof: m_j(x) = (j,b)(k,g), pi_j(x) = (j,-b)(k,d); d = -g would make x the D-partner of {j,k} (D(x) lies in {i,k}), so d = g,
#   and with v, sigma v (one on each sign of k) the inner vertex (k,g) would see 3 neighbours of x, against mu = 2.
# Mode "H": T = 0..6 hamiltonian, all degrees 2; counts surviving skeletons (orientation x choice) by number of alpha blocks.
# Mode "fam n": the M1 families with T = 0..n-1 (A enumerated as in v3); counts labelled orientations with a surviving choice.
# Flag --untyped reproduces v3 (control).
import itertools, sys, time
from collections import Counter
sys.path.insert(0, "scripts")
import m1_blocks as MB
from m1_blocks3 import two_factor_exists
from lib_cycles import cycle_structures
N = 7

def check(n, In, choice, typed, Ab, stats=None):
    T = list(range(n))
    tw = {frozenset((T[m], T[(m + 1) % n])) for m in range(n)}
    d = {c: len(In[c]) for c in range(N)}
    Tw = {c: ([T[(c - 1) % n], T[(c + 1) % n]] if c < n else []) for c in range(N)}
    outdeg = {c: 6 - d[c] - len(Tw[c]) for c in range(N)}
    f = {c: 2 * outdeg[c] + len(Tw[c]) for c in range(N)}
    def tail(a, b):
        if frozenset((a, b)) in tw: return None
        return a if a in In[b] else b
    dedges = []; linked = {}; cert42 = {}; cert33 = {}
    for c in range(N):
        ch = choice[c]
        if ch[0] == 'A':
            for cyc in ch[1]:
                if len(cyc) == 2:
                    a, b = cyc; dedges += [(c, a, b), (c, a, b)]; linked[('A', a, b)] = {a, b}
                else:
                    for x, y in zip(cyc, cyc[1:] + cyc[:1]): dedges.append((c, x, y))
            continue
        if ch[0] == 'C':
            I = list(ch[1])
            if len(I) == 2:
                a, b = I; dedges += [(c, a, b), (c, a, b)]; linked[c] = set(I); cert42[c] = set(I)
            elif len(I) == 3:
                a, b, e = I; dedges += [(c, a, b), (c, b, e), (c, e, a)]; cert33[c] = set(I)
            continue
        P1, P2 = Tw[c]
        if ch[0] == 'L':
            a, b = ch[1]; dedges += [(c, a, b), (c, a, b), (c, P1, P2)]; linked[c] = {a, b}; cert42[c] = {a, b}
        else:
            seq = [P1] + list(ch[1]) + [P2]
            for x, y in zip(seq, seq[1:]): dedges.append((c, x, y))
    orbits = []
    for (c, x, y) in dedges: orbits += [(c, x, y), (c, y, x)]
    if any(k in cert33 and j not in cert33[k] for (i, j, k) in orbits): return False
    for L in linked.values():
        a, b = sorted(L); t_ = tail(a, b)
        if t_ is not None and f[t_] < 8: return False
    for L in linked.values():
        for (i, j, k) in orbits:
            if {i, k} == L and j not in L and k in cert42 and j not in cert42[k]: return False
    comps = {c: MB.components_for(c, choice, In, Tw, n, d) for c in range(N)}
    if Ab is not None:
        comps[Ab] = [set(cyc) for cyc in choice[Ab][1]]
    memo = {}
    for j in range(N):
        if f[j] == 0: continue
        free = []
        for idx, (c, x, y) in enumerate(dedges):
            if x == j: free.append((('e', idx, 0), c, (c, j, y)))
            if y == j: free.append((('e', idx, 1), c, (c, j, x)))
        if len(free) != f[j]: continue
        ids = [fr[0] for fr in free]; typ = {fr[0]: fr[1] for fr in free}
        sis_of = {}
        for a_, b_ in itertools.combinations(free, 2):
            if a_[1] == b_[1] and frozenset((j, a_[1])) not in tw: sis_of[a_[0]] = b_[0]; sis_of[b_[0]] = a_[0]
        types_present = sorted(set(typ.values()))
        allowed = {}
        for fr in free:
            i, jj, k = fr[2]
            al = set()
            for r1, r2 in itertools.combinations_with_replacement(types_present, 2):
                nvec = Counter([r1, r2])
                if any(nvec[r] > sum(1 for t in typ.values() if t == r) - (1 if r == fr[1] else 0) for r in nvec): continue
                if r1 == r2 == fr[1]: continue
                if typed and r1 == r2 == k: continue          # typed rule n_k <= 1
                key = (fr[2], r1, r2)
                if key not in memo:
                    fixed = {r: nvec.get(r, 0) for r in range(N) if r not in (i, jj)}
                    memo[key] = MB.feasible_exact(i, jj, k, comps, fixed)
                if memo[key]: al.add((r1, r2))
            allowed[fr[0]] = al
            if not al:
                if stats is not None: stats['orbit', j] += 1
                return False
        if not two_factor_exists(ids, typ, allowed, sis_of):
            if stats is not None: stats['block', j] += 1
            return False
    return True

def orientations(n):
    T = list(range(n))
    tw = {frozenset((T[m], T[(m + 1) % n])) for m in range(n)}
    pairs = [(u, v) for u in range(N) for v in range(u + 1, N) if frozenset((u, v)) not in tw]
    for bits in range(1 << len(pairs)):
        In = {c: [] for c in range(N)}
        for t, (u, v) in enumerate(pairs):
            a, b = (u, v) if (bits >> t) & 1 else (v, u)
            In[b].append(a)
        d = {c: len(In[c]) for c in range(N)}
        A = [c for c in range(N) if d[c] == 6]
        if len(A) > 1: continue
        if any((c < n and d[c] > 2) or (c >= n and d[c] not in (0, 2, 3, 6)) for c in range(N)): continue
        yield In, (A[0] if A else None)

def options(n, In, Ab):
    opts = []
    for c in range(N):
        d = len(In[c])
        if c == Ab: opts.append([('A', cs) for cs in cycle_structures(In[c])]); continue
        if c >= n: opts.append([('C', tuple(sorted(In[c])))]); continue
        I = In[c]
        if d == 0: opts.append([('P', ())])
        elif d == 1: opts.append([('P', (I[0],))])
        else: opts.append([('L', tuple(sorted(I))), ('P', (I[0], I[1])), ('P', (I[1], I[0]))])
    return opts

def run_H(typed, budget):
    t0 = time.time(); surv = Counter(); tot = Counter(); stats = Counter(); orients = 0; beta_surv_orient = set()
    for oi, (In, Ab) in enumerate(orientations(7)):
        orients += 1
        for choice in itertools.product(*options(7, In, Ab)):
            if time.time() - t0 > budget: return surv, tot, stats, orients, beta_surv_orient, False
            na = sum(1 for ch in choice if ch[0] == 'L'); tot[na] += 1
            if check(7, In, choice, typed, Ab, stats if na == 0 else None):
                surv[na] += 1
                if na == 0: beta_surv_orient.add(oi)
    return surv, tot, stats, orients, beta_surv_orient, True

def run_fam(n, typed, budget):
    t0 = time.time(); out = Counter()
    for In, Ab in orientations(n):
        if time.time() - t0 > budget: return out, False
        d = {c: len(In[c]) for c in range(N)}
        cc = sum(1 for c in range(n, N) if d[c] == 3)
        for choice in itertools.product(*options(n, In, Ab)):
            if check(n, In, choice, typed, Ab):
                out[(0 if Ab is None else 1, cc, n)] += 1; break
    return out, True

if __name__ == "__main__":
    typed = "--untyped" not in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    t0 = time.time()
    if args and args[0] == "H":
        surv, tot, stats, orients, bso, done = run_H(typed, 280)
        print("typed" if typed else "UNTYPED (control)", "| H: orientations", orients, "| skeletons by #alpha: total", dict(sorted(tot.items())))
        print("  survivors by #alpha:", dict(sorted(surv.items())), "" if done else "(TIME CAP: partial)")
        print("  all-beta survivors spread over", len(bso), "orientations; all-beta kills by (reason, block):", dict(sorted(stats.items())))
    else:
        for n in [int(a) for a in args]:
            r, done = run_fam(n, typed, 280)
            print("typed" if typed else "UNTYPED (control)", "n =", n, dict(sorted(r.items())), "" if done else "(TIME CAP: partial)")
    print("time %.0fs" % (time.time() - t0))

def arcs_of(In):
    return frozenset((a, b) for b in range(N) for a in In[b])

def run_H_sym(typed, budget, only_alpha=False):
    # one orientation per D7-orbit (rotations/reflections of T = Z7); counts weighted by orbit size
    t0 = time.time(); seen = set(); reps = []
    for In, Ab in orientations(7):
        ar = arcs_of(In)
        if ar in seen: continue
        orb = set()
        for s in (1, -1):
            for r in range(7):
                orb.add(frozenset((((s * a + r) % 7), ((s * b + r) % 7)) for (a, b) in ar))
        seen |= orb; reps.append((In, Ab, len(orb)))
    surv = Counter(); tot = Counter()
    for In, Ab, w in reps:
        for choice in itertools.product(*options(7, In, Ab)):
            if time.time() - t0 > budget: return surv, tot, len(reps), False
            na = sum(1 for ch in choice if ch[0] == 'L')
            if only_alpha and na == 0: continue
            tot[na] += w
            if check(7, In, choice, typed, Ab): surv[na] += w
    return surv, tot, len(reps), True
