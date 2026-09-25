import itertools, sys
from collections import Counter
sys.path.insert(0, "scripts")
import m1_blocks as MB
p,s,u,q,r,C,A = 0,1,2,3,4,5,6
arcs = [(q,s),(q,u),(s,r),(u,r),(r,p),(p,q),(r,q),(p,C),(q,C),(r,C),(C,s),(C,u)] + [(m,A) for m in range(6)]
In = {c: [a for (a,b) in arcs if b == c] for c in range(7)}
n = 3; T = [0,1,2]; tw = {frozenset((0,1)), frozenset((1,2)), frozenset((0,2))}
d = {c: len(In[c]) for c in range(7)}
Tw = {c: ([T[(c-1)%n], T[(c+1)%n]] if c < n else []) for c in range(7)}
outdeg = {c: 6 - d[c] - len(Tw[c]) for c in range(7)}
f = {c: 2*outdeg[c] + len(Tw[c]) for c in range(7)}
print("In:", In, "\nTw:", Tw, "\nf:", f)
for cs in [('P', (C, q)), ('P', (q, C)), ('L', tuple(sorted((C, q))))]:
  for cu in [('P', (C, q)), ('P', (q, C)), ('L', tuple(sorted((C, q))))]:
    choice = [('P', (r,)), cs, cu, ('C', tuple(sorted(In[q]))), ('C', tuple(sorted(In[r]))), ('C', tuple(sorted(In[C]))), ('A', None)]
    dedges = []
    for c in range(7):
        ch = choice[c]
        if ch[0] == 'A': continue
        if ch[0] == 'C':
            I = list(ch[1])
            if len(I) == 2: a,b = I; dedges += [(c,a,b),(c,a,b)]
            else: a,b,e = I; dedges += [(c,a,b),(c,b,e),(c,e,a)]
            continue
        P1, P2 = Tw[c]
        if ch[0] == 'L': a,b = ch[1]; dedges += [(c,a,b),(c,a,b),(c,P1,P2)]; continue
        seq = [P1] + list(ch[1]) + [P2]
        for x, y in zip(seq, seq[1:]): dedges.append((c,x,y))
    comps = {c: MB.components_for(c, choice, In, Tw, n, d) for c in range(7)}
    fails = []
    for j in range(7):
        if f[j] == 0 or f[j] > 8: continue
        free = []
        for idx,(c,x,y) in enumerate(dedges):
            if x == j: free.append((('e',idx,0), c, (c,j,y)))
            if y == j: free.append((('e',idx,1), c, (c,j,x)))
        if j != A: free.append((('A',j,0), A, None)); free.append((('A',j,1), A, None))
        if len(free) != f[j]: fails.append((j,'mismatch',len(free))); continue
        ids = [fr[0] for fr in free]; byid = {fr[0]: fr for fr in free}
        sis = set(frozenset((a_[0], b_[0])) for a_, b_ in itertools.combinations(free, 2) if a_[1] == b_[1] and frozenset((j, a_[1])) not in tw)
        ok = False
        for es in MB.two_regular_graphs(ids, sis):
            nb = {v: [] for v in ids}
            for (x_, w_) in es: nb[x_].append(w_); nb[w_].append(x_)
            if any(len(set(nb[a_]) & set(nb[b_])) > 1 for s_ in sis for (a_, b_) in [tuple(s_)]): continue
            good = True
            for v in ids:
                trip = byid[v][2]
                if trip is None: continue
                nvec = Counter(byid[w][1] for w in nb[v])
                i_, jj, k_ = trip
                if not MB.feasible_exact(i_, jj, k_, comps, {rr: nvec.get(rr, 0) for rr in range(7) if rr not in (i_, jj)}): good = False; break
            if good: ok = True; break
        if not ok: fails.append(j)
    print("s:", cs, " u:", cu, "-> failing blocks:", fails)
