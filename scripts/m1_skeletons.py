# Sound skeleton filter for the M1 mixtures (one twisted cycle T, all other pairs anchored, no disjoint squares).
# Applies ONLY lemmas proved by hand (notes 26-28):
#   degree rules: T-blocks d<=2; non-T d in {0,2,3,6}; at most one d=6 block (A)
#   SL (28.1): at a third block, at most one closed D-cycle, length <= 3  -> non-T d in {0,2,3} has one closed cycle on In(k)
#   SL-dist at C-blocks (non-T, d=3, closed triangle S=In(k)): every orbit (i,j,k) with third block k has j in S
#   28.4: closed linked L_c={a,b}; orbit (i,j,k) with {i,k}={a,b}, j not in {a,b}; k certain (4,2) with j not in L_k -> kill
#   28.5: closed linked L_c={a,b} with {a,b} anchored a->b  =>  f_a = 2*out_a + t_a >= 8
# CONSERVATIVE: block A's internal D-structure is NOT enumerated (its squares/linked pairs are ignored), so this can only
# under-kill. Output: survivors per (a, c, n).
import itertools, sys
from collections import Counter
N = 7

def run(n):
    T = list(range(n))
    tw = {frozenset((T[m], T[(m + 1) % n])) for m in range(n)}
    pairs = [(u, v) for u in range(N) for v in range(u + 1, N) if frozenset((u, v)) not in tw]
    out = Counter()
    for bits in range(1 << len(pairs)):
        In = {c: [] for c in range(N)}
        for t, (u, v) in enumerate(pairs):
            a, b = (u, v) if (bits >> t) & 1 else (v, u)
            In[b].append(a)
        d = {c: len(In[c]) for c in range(N)}
        ok = True; A = [c for c in range(N) if d[c] == 6]
        if len(A) > 1: continue
        for c in range(N):
            if c < n and d[c] > 2: ok = False; break
            if c >= n and d[c] not in (0, 2, 3, 6): ok = False; break
        if not ok: continue
        # symmetry reduction is not attempted; we count labelled skeletons
        Tw = {c: ([T[(c - 1) % n], T[(c + 1) % n]] if c < n else []) for c in range(N)}
        outdeg = {c: 6 - d[c] - len(Tw[c]) for c in range(N)}
        f = {c: 2 * outdeg[c] + len(Tw[c]) for c in range(N)}
        def anchored_tail(a, b):
            # pair {a,b} anchored: return tail (the block pointing to the other), None if twisted
            if frozenset((a, b)) in tw: return None
            return a if a in In[b] else b
        # D-structure options per block
        opts = []
        for c in range(N):
            if c in A:
                opts.append([('A',)]); continue
            if c >= n:
                opts.append([('C', tuple(sorted(In[c])))]); continue   # closed cycle on In (length d)
            I = In[c]; P1, P2 = Tw[c]
            if d[c] == 0: opts.append([('P', ())])
            elif d[c] == 1: opts.append([('P', (I[0],))])
            else: opts.append([('L', tuple(sorted(I))), ('P', (I[0], I[1])), ('P', (I[1], I[0]))])
        for choice in itertools.product(*opts):
            orbits = []; linked = {}; cert42 = {}; cert33 = {}
            for c in range(N):
                ch = choice[c]
                if ch[0] == 'A': continue
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
            bad = False
            for (i, j, k) in orbits:                       # SL-dist at C-blocks
                if k in cert33 and j not in cert33[k]: bad = True; break
            if not bad:
                for c, L in linked.items():                 # 28.5
                    a, b = sorted(L); tail = anchored_tail(a, b)
                    if tail is not None and f[tail] < 8: bad = True; break
            if not bad:
                for c, L in linked.items():                 # 28.4
                    for (i, j, k) in orbits:
                        if {i, k} == L and j not in L and k in cert42 and j not in cert42[k]:
                            bad = True; break
                    if bad: break
            if not bad:
                a_ = len(A); cc = sum(1 for c in range(n, N) if d[c] == 3)
                out[(a_, cc, n)] += 1
                break      # skeleton (orientation) survives with at least one choice
    return out

if __name__ == "__main__":
    tot = Counter()
    for n in range(3, 8):
        r = run(n); tot.update(r)
        print("n =", n, dict(sorted(r.items()))); sys.stdout.flush()
    print("surviving labelled orientations per (a, c, n):", dict(sorted(tot.items())))
