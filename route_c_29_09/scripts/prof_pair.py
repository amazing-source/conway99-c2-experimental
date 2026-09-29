"""Stage-by-stage profile of one pair search (FD_SYM=1 path), on cached bench pairs. Usage: python prof_pair.py <id> <n>"""
import sys, os, time, pickle, collections, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["FD_LEMMA_U"] = "1"; os.environ["FD_SYM"] = "1"; os.environ["FD_PREBUDGET"] = "0"
import frame_dfs as FD, bench as B
lid = "%03d" % int(sys.argv[1]); n = int(sys.argv[2])
recs = pickle.load(open(os.path.join(B.BD, "%s.pkl" % lid), "rb"))[:n]
L = B.lat(lid); G, X3, X4, S2 = L["G"], L["X3"], L["X4"], L["S2"]
T = collections.defaultdict(float); sizes = collections.defaultdict(list)
FD.search(L, recs[0]["y1"], recs[0]["y2"])   # jit warm-up
for rec in recs:
    y1, y2 = rec["y1"], rec["y2"]; Y = np.array([y1, y2])
    t = time.time(); YS = Y @ G @ S2.T; T["yS"] += time.time() - t
    t = time.time(); H = X4[((X4 @ G @ Y.T) == 0).all(axis=1)]; T["H_perp_y (X4 %d)" % len(X4)] += time.time() - t
    t = time.time(); HS = H @ G @ S2.T; H = H[np.abs(HS).max(axis=1) <= 2]; HS = H @ G @ S2.T; T["HS+admissible"] += time.time() - t
    t = time.time(); W = X3[((X3 @ G @ Y.T) == 0).all(axis=1)]; WS = W @ G @ S2.T; T["W,WS"] += time.time() - t
    t = time.time(); V = H @ G @ W.T; T["V=HGW"] += time.time() - t
    t = time.time(); u = [FD.pack64(V == 1), FD.pack64(V == -1), FD.pack64(V == 0), FD.pack64(np.abs(V) == 2), FD.pack64(np.abs(V) == 1)]; T["pack V x5"] += time.time() - t
    SUP = HS != 0
    t = time.time(); CBb = FD.compat_nb(H @ G, H, u[0], u[1], FD.pack64(SUP & (np.abs(YS) == 3).any(axis=0)[None, :])); T["compat_nb"] += time.time() - t
    sizes["nH"].append(len(H)); sizes["nW"].append(len(W))
    t = time.time(); r = FD.search(L, y1, y2); T["TOTAL search()"] += time.time() - t
    for k, v in r["secs"].items(): T["search.secs." + k] += v
    sizes["nodes"].append(sum(r["nodes"]))
for k, v in T.items(): print("%-28s %.3f s/pair" % (k, v / n))
print({k: int(np.median(v)) for k, v in sizes.items()})
