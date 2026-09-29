"""How many distinct (y1, y2-hit-set) groups does a pair list really contain? Usage: python hitset_groups.py <id> <pairs json | stream txt> [max_pairs]"""
import sys, os, json, collections, numpy as np
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frame_dfs as FD, bench
lid = "%03d" % int(sys.argv[1]); P = bench.load_pairs(sys.argv[2]); mx = int(sys.argv[3]) if len(sys.argv) > 3 else len(P)
L = bench.lat(lid); G = L["G"]; S2 = L["S2"]; Binv = np.linalg.inv(np.array([[float(x) for x in r] for r in L["B"]]))
cv = lambda c: np.rint(np.array([float(F(x)) for x in c]) @ Binv).astype(np.int64)
groups = collections.defaultdict(int); y1s = set(); hits_only = collections.defaultdict(int)
for y1a, y2a in P[:mx]:
    y1, y2 = cv(y1a), cv(y2a)
    h1 = tuple(np.flatnonzero(np.abs(y1 @ G @ S2.T) == 3)); h2 = tuple(np.flatnonzero(np.abs(y2 @ G @ S2.T) == 3))
    groups[(tuple(y1), h2)] += 1; y1s.add(tuple(y1)); hits_only[tuple(sorted(h1 + h2))] += 1
n = min(mx, len(P))
print(json.dumps({"id": lid, "pairs": n, "distinct_y1": len(y1s), "groups_(y1,y2hits)": len(groups), "reduction": round(n / len(groups), 1),
                  "distinct_total_hit_sets": len(hits_only), "reduction_if_by_hitset_only": round(n / len(hits_only), 1)}))
