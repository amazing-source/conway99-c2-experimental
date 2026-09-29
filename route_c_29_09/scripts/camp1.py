import sys, os, time, pickle, numpy as np, numba as nb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["FD_LEMMA_U"] = "1"
import frame_dfs as FD, bench as B
from footprint_tables import forbid_table
FT = {}
def ftab(n, Y):
    if (n, Y) not in FT: FT[(n, Y)] = np.array(forbid_table(n, Y), dtype=np.bool_)
    return FT[(n, Y)]
@nb.njit(cache=True)
def mark(Aabs, F, nw):
    nT, nH = Aabs.shape; inc = np.zeros((nH, nw), np.uint64); dele = np.zeros(nH, np.bool_)
    for x in range(nT):
        for i in range(nH):
            if F[x, 0, Aabs[x, i]]: dele[i] = True
        for i in range(nH):
            ri = Aabs[x, i]
            if ri == 0: continue
            for j in range(i + 1, nH):
                rj = Aabs[x, j]
                if rj != 0 and F[x, ri, rj]:
                    inc[i, j >> 6] |= np.uint64(1) << np.uint64(j & 63); inc[j, i >> 6] |= np.uint64(1) << np.uint64(i & 63)
    return inc, dele
def run(L, ps, use, lim=2_000_000):
    G = L["G"]; H = ps["H"].astype(np.int64); W = ps["W"].astype(np.int64); V = H @ G @ W.T
    HS = ps["HS"].astype(np.int64); WS = ps["WS"].astype(np.int64); target = ps["target"]; flex = ps["flex"]; whit = np.abs(WS) == 3
    t0 = time.time(); keep = np.ones(len(H), bool); inc = None; ntest = 0
    if use:
        Y = np.array([ps["y1"], ps["y2"]]) if "y1" in ps else None
        Tl, Fl = [], []
        for n, X in ((2, L["R"]), (3, L["X3"]), (4, L["X4"])):
            Yx = ((X @ G @ Yv.T) ** 2).sum(1)
            for Yval in np.unique(Yx):
                F = ftab(n, int(Yval))
                if F[1:3, 1:3].any() or F[0, 1:3].any():
                    sel = X[Yx == Yval]; Tl.append(sel); Fl += [F] * len(sel)
        T = np.vstack(Tl); ntest = len(T)
        Aabs = np.abs(T @ G @ H.T).astype(np.int64); Aabs = np.minimum(Aabs, 4)
        inc, dele = mark(Aabs, np.array(Fl), (len(H) + 63) // 64); keep = ~dele
    ts = time.time() - t0
    idx = np.flatnonzero(keep); H, HS, V = H[idx], HS[idx], V[idx]
    SUP = HS != 0; nH, nW = len(H), len(W)
    CBb = FD.compat_nb(H @ G, H, FD.pack64(V == 1), FD.pack64(V == -1), FD.pack64(SUP & (target == 1)[None, :]))
    if inc is not None:
        incb = np.unpackbits(inc.view(np.uint8), axis=1, bitorder="little")[:, :len(keep)].astype(bool)[np.ix_(idx, idx)]
        CBb &= ~FD.pack64(incb)
    supn = SUP.sum(1); supp = np.full((nH, max(1, int(supn.max()))), -1, np.int64)
    for i in range(nH): supp[i, :supn[i]] = np.flatnonzero(SUP[i])
    allM = FD.pack64(np.ones((1, nH), bool))[0]; allW = FD.pack64(np.ones((1, nW), bool))[0]
    t1 = time.time()
    nodes, lv, lc, comp, ov, cnt = FD.dfs_general_u(CBb, FD.pack64(SUP.T), supp, supn.astype(np.int64), FD.pack64(V == 0), FD.pack64(V == 1), FD.pack64(V == -1),
        FD.pack64(np.abs(V) == 2), FD.pack64(np.abs(V) == 1), target, flex, FD.pack64(whit), allM, allW, lim, 2000, H, W, V, WS, HS, FD.pack64(whit.T), -1, allM)
    return int(sum(nodes)), comp and cnt[0] == 0, ts, time.time() - t1, (~keep).mean(), ntest
if __name__ == "__main__":
    for lid in ("078", "097"):
        recs = pickle.load(open(os.path.join(B.BD, lid + ".pkl"), "rb"))[:int(sys.argv[1])]; L = B.lat(lid)
        for rec in recs:
            Yv = np.array([rec["y1"], rec["y2"]])
            b = run(L, rec["ps"], False); f = run(L, rec["ps"], True)
            print(lid, "base nodes %7d kill %d dfs %.2fs | filt nodes %7d kill %d setup %.2fs dfs %.2fs Hdel %.0f%% tests %d" % (b[0], b[1], b[3], f[0], f[1], f[2], f[3], 100 * f[4], f[5]), flush=True)
