"""Readable H-beta certificates (note 32 §7): for each skeleton class, solve the column LP, take the (P2)+(PPE) multiplier matrix W,
round 2W to integers, and test whether ONE aggregated identity  sum_{a,b} W~_ab (P2/PPE)[a,b]  plus the linear rows is already
infeasible.  Usage: python hb_round_all.py <k> <K>  -> logs/hb_round_<k>.jsonl"""
import sys, json, copy, time, gzip, glob
from collections import defaultdict
import numpy as np
sys.path.insert(0, "scripts")
import hb_pairlevel as H, hb_colmodel as CM, hb_colmodel_all as A
PAIRS = H.PAIRS; PI = {R: t for t, R in enumerate(PAIRS)}
k, K = int(sys.argv[1]), int(sys.argv[2])
cls, mult = A.classes()
f = open("logs/hb_round_%d.jsonl" % k, "w")
for idx, key in enumerate(cls):
    if idx % K != k: continue
    t0 = time.time()
    cm = CM.ColModel([tuple(z) for z in key], True); full = cm.solve()
    y = np.array(cm.h.getSolution().row_dual)[:len(cm.rows)]
    W = np.zeros((21, 21)); p2rows = {}
    for r, row in enumerate(cm.rows):
        nm = row[3]
        if nm[0] == 'D': W[PI[nm[1]], PI[nm[1]]] += y[r]; p2rows[PI[nm[1]], PI[nm[1]]] = r
        if nm[0] == 'P2': a, b = PI[nm[1]], PI[nm[2]]; W[a, b] += y[r] / 2; W[b, a] += y[r] / 2; p2rows[min(a, b), max(a, b)] = r
    Wt = np.round(2 * W)
    base = [row for row in cm.rows if row[3][0] not in ('D', 'P2')]
    terms = defaultdict(float); rhs = 0.0
    for (a, b), r in p2rows.items():
        w = Wt[a, b] * (1 if a == b else 2) / 2
        if w == 0: continue
        tr, rh, _, _ = cm.rows[r]
        for col, v in tr: terms[col] += w * v
        rhs += w * rh
    c2 = copy.copy(cm); c2.rows = base + [(list(terms.items()), rhs, 'eq', ('agg',))]
    one = c2.solve()
    f.write(json.dumps({"idx": idx, "mult": mult[key], "full": full, "one_identity_rounded": one,
                        "Wt": [[int(v) for v in row] for row in Wt], "secs": round(time.time() - t0, 1)}) + "\n"); f.flush()
f.close()
