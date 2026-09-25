# Same check as h_linked_exclusion.py, plus Lemma 28.5 (proved in note 28 §7):
# in H, an alpha block c whose two in-neighbours a, b are joined by a CHORD (anchored pair) is impossible
# (balance at c forbids the orbits of {a,b} from being adjacent to those of {a,c} in the free 6-cycle at a,
#  which forces a 4-cycle through the two Tw-free labels: contradicts 19.1).
import itertools
exec(open("scripts/h_linked_exclusion.py", encoding="utf-8").read().split("def run():")[0])
def chord(a, b):
    return (a - b) % N not in (1, N - 1)
total = surv = 0; stats = {}; k1 = k2 = 0
for arcs in orientations():
    In = {c: sorted(a for (a, b) in arcs if b == c) for c in range(N)}
    per_block = [['A', ('B', In[c][0], In[c][1]), ('B', In[c][1], In[c][0])] for c in range(N)]
    for modes in itertools.product(*per_block):
        total += 1
        bad55 = any(modes[c] == 'A' and chord(*In[c]) for c in range(N))
        bad54 = killed(In, modes) is not None
        if bad55: k2 += 1
        if bad54: k1 += 1
        if not (bad54 or bad55):
            surv += 1; nA = sum(m == 'A' for m in modes); stats[nA] = stats.get(nA, 0) + 1
print("total", total, "killed by 28.4:", k1, "killed by 28.5:", k2, "survivors:", surv)
print("survivors by number of alpha blocks:", dict(sorted(stats.items())))
