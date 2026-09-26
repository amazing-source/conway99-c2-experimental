"""Tail-lemma filter for AD configurations (anchored + doubly-disjoint pairs, no half pairs; note 41).  39.4: at every block k,
M_k = {x : {k,x} anchored at k} and F_k = {x : {k,x} anchored at x or doubly-disjoint} are unions of components of G_k.
In AD the D-graph at a block of in-degree d is forced up to type: d = 2 digon, d = 3 triangle, d = 6 (A) a cycle type; so the
one-block squares (pivot i, arms j, k) are known from the orientation except at A.
Lemma 24.1: square (pivot i, arms j, k) => in G_k the component of i (inside F_k) has >= 3 + [j in it] blocks.
  => dead if |F_k| <= 2, or |F_k| = 3 and j in F_k (the component would be all of F_k, contain j, and need 4).
Dis version (note 39): dis square X in {i,j}, partner in {k,l} => in G_k the component of l (inside F_k) has
  >= 2 + [i in it] + [j in it] blocks  => dead if |F_k| < 2, or |F_k| = 2 and F_k meets {i,j} ... (only the certain part is used).
Usage: python ad_tail_filter.py   (runs on logs/ad2_reps.json)"""
import json, itertools
N = 7
DD = [(0, 1), (2, 3)]
def analyse(rep):
    head = {}
    for k, h in rep.items():
        a, b = map(int, k.split(",")); head[(a, b)] = h
    In = {c: [x for x in range(N) if x != c and head.get((min(c, x), max(c, x))) == c] for c in range(N)}
    F = {c: {x for x in range(N) if x != c and x not in In[c]} for c in range(N)}
    reasons = []
    for i in range(N):
        d = len(In[i])
        if d in (2, 3):                                   # digon / triangle: every pair of arms carries a square
            for j, k in itertools.permutations(In[i], 2):
                if len(F[k]) <= 2: reasons.append("square pivot %d arms %d,%d: |F_%d| = %d" % (i, j, k, k, len(F[k])))
                elif len(F[k]) == 3 and j in F[k]: reasons.append("square pivot %d arms %d,%d: F_%d = %s contains %d" % (i, j, k, k, sorted(F[k]), j))
        if d == 6:                                        # A: some cycle through each arm; every arm k has at least one neighbour j
            for k in In[i]:
                if len(F[k]) <= 2: reasons.append("A=%d arm %d: |F_%d| = %d" % (i, k, k, len(F[k])))
    for (i, j) in DD:                                     # dis squares: partner pair = the other dd pair
        for (k, l) in DD:
            if {i, j} & {k, l}: continue
            for kk, ll in ((k, l), (l, k)):
                if len(F[kk]) < 2: reasons.append("dis square %d%d->%d%d: |F_%d| = %d" % (i, j, k, l, kk, len(F[kk])))
    return reasons
reps = json.load(open("logs/ad2_reps.json"))
alive = [t for t, r in enumerate(reps) if not analyse(r)]
print("AD2 orientation classes: %d ; killed by the tail lemma: %d ; alive: %d" % (len(reps), len(reps) - len(alive), len(alive)))
print("alive reps:", alive[:40])
print("rep 0 reasons:", analyse(reps[0])[:3])
