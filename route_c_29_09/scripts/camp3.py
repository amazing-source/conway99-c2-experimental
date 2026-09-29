# Lever 1: characteristic-vector trap pushed to h's. For z char. norm 16: Y_z + sum_{selected h}(z,h)^2 <= 70 (42 from the u, rest >= 0).
import sys, os, time, pickle, numpy as np, numba as nb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["FD_LEMMA_U"] = "1"
import frame_dfs as FD, bench as B, camp2
@nb.njit(cache=True)
def mark(A2, slack, nw):
    nT, nH = A2.shape; inc = np.zeros((nH, nw), np.uint64); dele = np.zeros(nH, np.bool_)
    for x in range(nT):
        for i in range(nH):
            if A2[x, i] > slack[x]: dele[i] = True
        for i in range(nH):
            if A2[x, i] == 0 or dele[i]: continue
            for j in range(i + 1, nH):
                if A2[x, j] != 0 and A2[x, i] + A2[x, j] > slack[x]:
                    inc[i, j >> 6] |= np.uint64(1) << np.uint64(j & 63); inc[j, i >> 6] |= np.uint64(1) << np.uint64(i & 63)
    return inc, dele
def run(L, rec, lim=2_000_000):
    G = L["G"]; ps = rec["ps"]; y1, y2 = rec["y1"], rec["y2"]; FD.char_trap(L, y1, y2)
    ZG = L["_ZG"]; Yz = (ZG @ y1) ** 2 + (ZG @ y2) ** 2; sel = Yz >= 34
    H = ps["H"].astype(np.int64); A2 = ((ZG[sel] @ H.T) ** 2).astype(np.int64); slack = (70 - Yz[sel]).astype(np.int64)
    t0 = time.time(); inc, dele = mark(A2, slack, (len(H) + 63) // 64); ts = time.time() - t0
    keep = ~dele; idx = np.flatnonzero(keep)
    W = ps["W"].astype(np.int64); V = H @ G @ W.T; HS = ps["HS"].astype(np.int64); WS = ps["WS"].astype(np.int64)
    target, flex = ps["target"], ps["flex"]; whit = np.abs(WS) == 3
    out = []
    for use in (False, True):
        ix = idx if use else np.arange(len(H)); Hh, HSh, Vh = H[ix], HS[ix], V[ix]; SUP = HSh != 0; nH = len(Hh)
        CBb = FD.compat_nb(Hh @ G, Hh, FD.pack64(Vh == 1), FD.pack64(Vh == -1), FD.pack64(SUP & (target == 1)[None, :]))
        if use:
            ib = np.unpackbits(inc.view(np.uint8), axis=1, bitorder="little")[:, :len(H)].astype(bool)[np.ix_(idx, idx)]; CBb &= ~FD.pack64(ib)
        supn = SUP.sum(1); supp = np.full((nH, max(1, int(supn.max()))), -1, np.int64)
        for i in range(nH): supp[i, :supn[i]] = np.flatnonzero(SUP[i])
        allM = FD.pack64(np.ones((1, nH), bool))[0]; allW = FD.pack64(np.ones((1, len(W)), bool))[0]; t1 = time.time()
        r = FD.dfs_general_u(CBb, FD.pack64(SUP.T), supp, supn.astype(np.int64), FD.pack64(Vh == 0), FD.pack64(Vh == 1), FD.pack64(Vh == -1), FD.pack64(np.abs(Vh) == 2),
            FD.pack64(np.abs(Vh) == 1), target, flex, FD.pack64(whit), allM, allW, lim, 2000, Hh, W, Vh, WS, HSh, FD.pack64(whit.T), -1, allM)
        out.append((int(sum(r[0])), bool(r[3] and r[5][0] == 0), time.time() - t1))
    return out, dele.mean(), ts, int(sel.sum())
for lid in ("078", "097"):
    L = B.lat(lid); recs = pickle.load(open(os.path.join(B.BD, lid + ".pkl"), "rb")); k = 0
    for rec in recs:
        if FD.char_trap(L, rec["y1"], rec["y2"]) is not None: continue
        (b, f), dl, ts, nz = run(L, rec); k += 1
        print(lid, "base %7d k%d %.2fs | lev1 %7d k%d %.2fs  Hdel %.0f%%  mark %.2fs z=%d" % (b[0], b[1], b[2], f[0], f[1], f[2], 100 * dl, ts, nz), flush=True)
        if k == 4: break
