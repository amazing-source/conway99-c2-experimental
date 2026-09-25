# Refinement of m1_skeletons.py: for surviving orientations with a block A (d=6), ALSO enumerate A's D-structure
# (all 2-regular loopless multigraphs on the 6 pairs {A,m}: 60 six-cycles, 45 (4+2), 10 (3+3), 15 (2+2+2) = 130)
# and apply the same proved rules including A's squares and A's closed linked pairs (28.4, 28.5, SL-dist at C-blocks).
# Still sound (only proved lemmas), still conservative elsewhere.
import itertools, sys
from collections import Counter
exec(open("scripts/m1_skeletons.py", encoding="utf-8").read().split("def run(n):")[0])

def cycle_structures(V):
    V = list(V); res = []
    def cycles_through(first, rest, length):
        for comb in itertools.combinations(rest, length - 1):
            for perm in itertools.permutations(comb):
                if length > 2 and perm[0] > perm[-1]: continue
                yield (first,) + perm
    def rec(remaining, acc):
        if not remaining: res.append(list(acc)); return
        first, rest = remaining[0], remaining[1:]
        for L in range(2, len(remaining) + 1):
            if len(remaining) - L == 1: continue
            for cyc in cycles_through(first, rest, L):
                rec([v for v in remaining if v not in cyc], acc + [cyc])
    rec(V, []); return res

def run(n):
    T = list(range(n))
    tw = {frozenset((T[m], T[(m + 1) % n])) for m in range(n)}
    pairs = [(u, v) for u in range(N) for v in range(u + 1, N) if frozenset((u, v)) not in tw]
    out = Counter(); outA = Counter()
    for bits in range(1 << len(pairs)):
        In = {c: [] for c in range(N)}
        for t, (u, v) in enumerate(pairs):
            a, b = (u, v) if (bits >> t) & 1 else (v, u)
            In[b].append(a)
        d = {c: len(In[c]) for c in range(N)}
        A = [c for c in range(N) if d[c] == 6]
        if len(A) != 1: continue
        if any((c < n and d[c] > 2) or (c >= n and d[c] not in (0, 2, 3, 6)) for c in range(N)): continue
        Ab = A[0]
        Tw = {c: ([T[(c - 1) % n], T[(c + 1) % n]] if c < n else []) for c in range(N)}
        outdeg = {c: 6 - d[c] - len(Tw[c]) for c in range(N)}
        f = {c: 2 * outdeg[c] + len(Tw[c]) for c in range(N)}
        def tail(a, b):
            if frozenset((a, b)) in tw: return None
            return a if a in In[b] else b
        opts = []
        for c in range(N):
            if c == Ab: opts.append([('A', cs) for cs in cycle_structures(In[c])]); continue
            if c >= n: opts.append([('C', tuple(sorted(In[c])))]); continue
            I = In[c]
            if d[c] == 0: opts.append([('P', ())])
            elif d[c] == 1: opts.append([('P', (I[0],))])
            else: opts.append([('L', tuple(sorted(I))), ('P', (I[0], I[1])), ('P', (I[1], I[0]))])
        cc = sum(1 for c in range(n, N) if d[c] == 3)
        survived = False
        for choice in itertools.product(*opts):
            orbits = []; linked = {}; cert42 = {}; cert33 = {}
            for c in range(N):
                ch = choice[c]
                if ch[0] == 'A':
                    for cyc in ch[1]:
                        if len(cyc) == 2:
                            a, b = cyc; orbits += [(c, a, b), (c, b, a)]
                            linked.setdefault(('A', c, a, b), set(cyc))
                        else:
                            for x, y in zip(cyc, cyc[1:] + cyc[:1]): orbits += [(c, x, y), (c, y, x)]
                    continue
                if ch[0] == 'C':
                    I = list(ch[1])
                    if len(I) == 2:
                        a, b = I; orbits += [(c, a, b), (c, b, a)]; linked[c] = set(I); cert42[c] = set(I)
                    elif len(I) == 3:
                        a, b, e = I
                        for (x, y) in ((a, b), (b, e), (e, a)): orbits += [(c, x, y), (c, y, x)]
                        cert33[c] = set(I)
                    continue
                P1, P2 = Tw[c]
                if ch[0] == 'L':
                    a, b = ch[1]; orbits += [(c, a, b), (c, b, a), (c, P1, P2), (c, P2, P1)]
                    linked[c] = {a, b}; cert42[c] = {a, b}
                else:
                    seq = [P1] + list(ch[1]) + [P2]
                    for x, y in zip(seq, seq[1:]): orbits += [(c, x, y), (c, y, x)]
            bad = any(k in cert33 and j not in cert33[k] for (i, j, k) in orbits)
            if not bad:
                for key, L in linked.items():
                    a, b = sorted(L); t_ = tail(a, b)
                    if t_ is not None and f[t_] < 8: bad = True; break
            if not bad:
                for key, L in linked.items():
                    for (i, j, k) in orbits:
                        if {i, k} == L and j not in L and k in cert42 and j not in cert42[k]:
                            bad = True; break
                    if bad: break
            if not bad:
                survived = True; break
        if survived: out[(1, cc, n)] += 1
    return out

tot = Counter()
for n in range(3, 7):
    r = run(n); tot.update(r); print("n =", n, dict(sorted(r.items()))); sys.stdout.flush()
print("with A's structure enumerated, surviving labelled orientations:", dict(sorted(tot.items())))
