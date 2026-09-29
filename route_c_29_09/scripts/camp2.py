import sys, os, time, pickle, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["FD_LEMMA_U"] = "1"
import frame_dfs as FD, bench as B, dfs_fp
from footprint_tables import allowed
AL = {n: allowed(n) for n in (2, 3, 4)}
def okt(n, Y):
    T = np.zeros((8, 8, 8, 2), bool)
    for p, ym in AL[n].items():
        if ym < Y: continue
        c = [p.count(1), p.count(2), p.count(3), p.count(4)]
        T[:c[0] + 1, :c[1] + 1, :c[2] + 1, :c[3] + 1] = True
    return T
def build(L, ps, Yv, H, y4min):
    G = L["G"]; cls, OK, TL, TCl = {}, [], [], []
    for n, X in ((2, L["R"]), (3, L["X3"]), (4, L["X4"])):
        Yx = ((X @ G @ Yv.T) ** 2).sum(1)
        m = Yx >= (y4min if n == 4 else 0); X, Yx = X[m], Yx[m]
        for Yval in np.unique(Yx):
            if (n, Yval) not in cls: cls[(n, Yval)] = len(OK); OK.append(okt(n, int(Yval)))
            sel = X[Yx == Yval]; TL.append(sel); TCl += [cls[(n, Yval)]] * len(sel)
    T = np.vstack(TL); A = np.minimum(np.abs(H @ G @ T.T), 4)
    nzc = (A > 0).sum(1); mx = int(nzc.max()); TAx = np.zeros((len(H), mx), np.int64); TAr = np.zeros((len(H), mx), np.int64)
    for i in range(len(H)):
        ix = np.flatnonzero(A[i]); TAx[i, :len(ix)] = ix; TAr[i, :len(ix)] = A[i, ix]
    return nzc.astype(np.int64), TAx, TAr, np.array(TCl, np.int64), np.array(OK), len(T)
def run(L, ps, Yv, fp, lim=2_000_000, y4min=10):
    G = L["G"]; H = ps["H"].astype(np.int64); W = ps["W"].astype(np.int64); V = H @ G @ W.T
    HS = ps["HS"].astype(np.int64); WS = ps["WS"].astype(np.int64); target = ps["target"]; flex = ps["flex"]; whit = np.abs(WS) == 3
    SUP = HS != 0; nH, nW = len(H), len(W)
    CBb = FD.compat_nb(H @ G, H, FD.pack64(V == 1), FD.pack64(V == -1), FD.pack64(SUP & (target == 1)[None, :]))
    supn = SUP.sum(1); supp = np.full((nH, max(1, int(supn.max()))), -1, np.int64)
    for i in range(nH): supp[i, :supn[i]] = np.flatnonzero(SUP[i])
    allM = FD.pack64(np.ones((1, nH), bool))[0]; allW = FD.pack64(np.ones((1, nW), bool))[0]
    args = (CBb, FD.pack64(SUP.T), supp, supn.astype(np.int64), FD.pack64(V == 0), FD.pack64(V == 1), FD.pack64(V == -1), FD.pack64(np.abs(V) == 2),
            FD.pack64(np.abs(V) == 1), target, flex, FD.pack64(whit), allM, allW, lim, 2000, H, W, V, WS, HS, FD.pack64(whit.T), -1, allM)
    t0 = time.time()
    if fp: ex = build(L, ps, Yv, H, y4min); ts = time.time() - t0; t0 = time.time(); r = dfs_fp.dfs_fp(*args, *ex)
    else: ts = 0; r = FD.dfs_general_u(*args)
    nodes, lv, lc, comp, ov, cnt = r
    return int(sum(nodes)), bool(comp and cnt[0] == 0), ts, time.time() - t0, [int(x) for x in nodes[:6]], (ex[-1] if fp else 0)
if __name__ == "__main__":
    for lid in ("078", "097"):
        recs = pickle.load(open(os.path.join(B.BD, lid + ".pkl"), "rb"))[:int(sys.argv[1])]; L = B.lat(lid)
        for rec in recs:
            Yv = np.array([rec["y1"], rec["y2"]])
            b = run(L, rec["ps"], Yv, False); f = run(L, rec["ps"], Yv, True)
            print(lid, "base %7d k%d %.2fs | fp %7d k%d build %.2fs dfs %.2fs T=%d depth %s" % (b[0], b[1], b[3], f[0], f[1], f[2], f[3], f[5], f[4]), flush=True)
