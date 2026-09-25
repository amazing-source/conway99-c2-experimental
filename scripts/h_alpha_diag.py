import sys, time, itertools
sys.path.insert(0, "scripts")
import m1_blocks4 as M
from collections import Counter
t0 = time.time(); seen = set(); reps = []
for In, Ab in M.orientations(7):
    ar = M.arcs_of(In)
    if ar in seen: continue
    orb = set()
    for s in (1, -1):
        for r in range(7):
            orb.add(frozenset((((s * a + r) % 7), ((s * b + r) % 7)) for (a, b) in ar))
    seen |= orb; reps.append((In, Ab, len(orb)))
# which lemma kills 1-alpha skeletons: pre-check (28.x) vs orbit-profile vs 2-factor; record block offset from alpha block
res = Counter()
for In, Ab, w in reps:
    for choice in itertools.product(*M.options(7, In, Ab)):
        al = [c for c in range(7) if choice[c][0] == 'L']
        if len(al) != 1: continue
        c = al[0]
        consec = abs(In[c][0] - In[c][1]) % 7 in (1, 6)
        st = Counter()
        ok = M.check(7, In, choice, False, Ab, st)
        if ok: res['SURVIVES'] += 1; continue
        if not st: res[('pre-28x', 'In consecutive' if consec else 'In chord')] += 1
        else:
            (reason, j), = st.items() if len(st) == 1 else [(list(st)[0], 0)]
            res[(reason[0], 'offset', (reason[1] - c) % 7, 'In=' + str(sorted((x - c) % 7 for x in In[c])))] += 1
for k, v in sorted(res.items(), key=str): print(k, v)
print("time %.0fs" % (time.time() - t0))
