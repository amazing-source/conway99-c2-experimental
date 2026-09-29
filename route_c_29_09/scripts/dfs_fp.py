import numpy as np, numba as nb
from frame_dfs import popc, leaf_general
U1 = np.uint64(1)
@nb.njit(cache=True)
def dfs_fp(compat, through, supp, suppn, Z, Pp, Pn, Bd, NZ, target, isflex, whitb, allM, allW, node_limit, cap, Hc, Wc, V, WS, HS, hitb, p0, fmask, TAn, TAx, TAr, TC, OKT, nT):
    """GENERAL mode + C1 LEMMA U+ (notes/145): a frame word hits (at 3/2) ONLY new roots that end at w = 1 and are not y-hits, and has the
    D7 pattern on the 7 h (exactly two (u,h) = +-1). At a node a word is VALID iff: no |(u,h)| = 2 and <= 2 nonzero on the chosen h,
    no 3/2-hit on a y-hit point, none on a flex point already covered >= 2 (monotone). The cells (Same/Opp) and the counting checks
    use the valid words only; a flex point at w <= 2 without a valid hitter must reach 3; at the leaf a w = 1 flex point needs a
    hitter with exactly 2 nonzero.
    GENERAL mode (flex points): target[p] = 1 or 3 exactly, or 0 for a flex point (final coverage 1 or 3). Pending points:
    exact points with need > 0, flex points with coverage 0 or 2. Branch on a pending point (smallest-index member through it);
    with no pending point, on the smallest-index remaining member (all candidates). Saturated: exact need 0, flex coverage 3."""
    nMw = compat.shape[1]; nWw = Z.shape[1]; npt = target.shape[0]; nW = Wc.shape[0]
    cand = np.zeros((8, nMw), np.uint64); Cs = np.zeros((8, nMw), np.uint64)
    nzw = np.zeros((8, nMw), np.int64); nnz = np.zeros(8, np.int64)
    need = np.zeros((8, npt), np.int64); cov = np.zeros((8, npt), np.int64)
    ge1 = np.zeros((8, nWw), np.uint64); ge2 = np.zeros((8, nWw), np.uint64); good = np.zeros((8, nWw), np.uint64)
    ge3 = np.zeros((8, nWw), np.uint64); bad = np.zeros((8, nWw), np.uint64); vm = np.zeros(nWw, np.uint64)
    P = np.zeros(8, np.int64); curj = np.zeros(8, np.int64); nodes = np.zeros(8, np.int64)
    leaves = np.zeros((cap, 7), np.int64); leafcov = np.zeros((cap, npt), np.int64); nleaves = 0; overflow = False
    counts = np.zeros(3, np.int64)
    slots = np.zeros((12, nW), np.int64); slen = np.zeros(12, np.int64); part = np.zeros((13, npt), np.int64); pos = np.zeros(13, np.int64)
    allowed = np.zeros(nWw, np.uint64)
    cT = np.zeros((8, nT, 4), np.int64)
    for w in range(nMw):
        cand[0, w] = allM[w]; nzw[0, w] = w
    nnz[0] = nMw
    for w in range(nWw): good[0, w] = allW[w]
    for i in range(npt):
        need[0, i] = target[i]
        if target[i] == 1:
            for w in range(nWw): bad[0, w] |= hitb[i, w]
    total = 0; stop = False; d = 0; action = 0
    while True:
        if action == 0:
            nodes[d] += 1; total += 1
            if node_limit > 0 and total >= node_limit: stop = True
            if stop:
                action = 2; continue
            if d == 7:
                valid = True
                for i in range(npt):
                    if isflex[i]:
                        if cov[d, i] != 1 and cov[d, i] != 3:
                            valid = False; break
                        if cov[d, i] == 1:                                   # Lemma U at the leaf: a hitter with exactly 2 nonzero
                            hv = False
                            for w in range(nWw):
                                if good[d, w] & ge2[d, w] & ~ge3[d, w] & ~bad[d, w] & hitb[i, w]:
                                    hv = True; break
                            if not hv:
                                valid = False; break
                    elif need[d, i] != 0:
                        valid = False; break
                if valid:
                    counts[0] += 1
                    res = leaf_general(P, cov[d], isflex, whitb, Hc, Wc, V, WS, HS, Z, Pp, Pn, allW, slots, slen, part, pos, npt, allowed)
                    if res >= 1: counts[1] += 1
                    if res == 2:
                        counts[2] += 1
                        if nleaves < cap:
                            for x in range(7): leaves[nleaves, x] = P[x]
                            for i in range(npt): leafcov[nleaves, i] = cov[d, i]
                            nleaves += 1
                        else: overflow = True
                action = 2; continue
            left = 7 - d; best = -1; bkey = 1 << 30; pruned = False
            for i in range(npt):
                if isflex[i]:
                    c = cov[d, i]
                    if c >= 3: r = 0
                    else:
                        hv = False
                        for w in range(nWw):
                            if good[d, w] & ~ge3[d, w] & ~bad[d, w] & hitb[i, w]:
                                hv = True; break
                        if hv: r = 1 if (c == 0 or c == 2) else 0
                        else: r = 3 - c                                      # Lemma U: w = 1 impossible, must reach 3
                else:
                    r = need[d, i]
                if r > left:
                    pruned = True; break
                if r > 0:
                    n = 0
                    for t in range(nnz[d]):
                        w = nzw[d, t]; n += popc(cand[d, w] & through[i, w])
                    if n < r:
                        pruned = True; break
                    if n - r < bkey:
                        best = i; bkey = n - r
            if pruned:
                action = 2; continue
            if d == 0 and p0 >= 0: best = p0                             # C2 28/09: symmetry breaking (forced first point)
            if best >= 0:
                for t in range(nnz[d]):
                    w = nzw[d, t]; Cs[d, w] = cand[d, w] & through[best, w]
                    if d == 0 and p0 >= 0: Cs[d, w] &= fmask[w]
            else:                                                        # no pending point: any remaining member
                for t in range(nnz[d]):
                    w = nzw[d, t]; Cs[d, w] = cand[d, w]
            curj[d] = 0
            action = 1; continue
        elif action == 1:
            j = -1
            while curj[d] < nnz[d]:
                w = nzw[d, curj[d]]; x = Cs[d, w]
                if x != 0:
                    low = x & (~x + U1)
                    j = w * 64 + popc(low - U1); Cs[d, w] = x ^ low
                    break
                curj[d] += 1
            if j < 0:
                action = 2; continue
            P[d] = j
            e1 = d + 1
            for w in range(nWw):
                good[e1, w] = good[d, w] & ~Bd[j, w]
                ge1[e1, w] = ge1[d, w] | NZ[j, w]
                ge2[e1, w] = ge2[d, w] | (ge1[d, w] & NZ[j, w])
                ge3[e1, w] = ge3[d, w] | (ge2[d, w] & NZ[j, w])
                bad[e1, w] = bad[d, w]
            for q in range(suppn[j]):                                        # flex points reaching coverage >= 2: their hitters die
                x = supp[j, q]
                if isflex[x] and cov[d, x] + 1 >= 2:
                    for w in range(nWw): bad[e1, w] |= hitb[x, w]
            for w in range(nWw): vm[w] = good[e1, w] & ~ge3[e1, w] & ~bad[e1, w]
            left = 7 - e1; ok = True
            for x in range(e1):
                if not ok: break
                for y in range(x + 1, e1):
                    c = P[x]; e = P[y]; same = np.uint64(0); opp = np.uint64(0)
                    for w in range(nWw):
                        zo = vm[w]
                        for f in range(e1):
                            if f != x and f != y: zo &= Z[P[f], w]
                        same |= ((Pp[c, w] & Pp[e, w]) | (Pn[c, w] & Pn[e, w])) & zo
                        opp |= ((Pp[c, w] & Pn[e, w]) | (Pn[c, w] & Pp[e, w])) & zo
                    if same == 0 or opp == 0:
                        ok = False; break
            if ok and left > 0:
                n = 0
                for w in range(nWw): n += popc(vm[w] & ~ge1[e1, w])
                if n < left * (left - 1): ok = False
                else:
                    for x in range(e1):
                        c = P[x]; n = 0
                        for w in range(nWw): n += popc(NZ[c, w] & vm[w] & ~ge2[e1, w])
                        if n < 2 * left:
                            ok = False; break
            if ok:
                for x in range(nT):
                    for q in range(4): cT[e1, x, q] = cT[d, x, q]
                for k in range(TAn[j]):
                    x = TAx[j, k]; r = TAr[j, k]; cT[e1, x, r - 1] += 1
                    if cT[e1, x, 0] > 7 or cT[e1, x, 1] > 7 or cT[e1, x, 2] > 7 or cT[e1, x, 3] > 1: ok = False; break
                    if not OKT[TC[x], cT[e1, x, 0], cT[e1, x, 1], cT[e1, x, 2], cT[e1, x, 3]]: ok = False; break
            if ok:
                for i in range(npt):
                    need[e1, i] = need[d, i]; cov[e1, i] = cov[d, i]
                cnt = 0
                for t in range(nnz[d]):
                    w = nzw[d, t]; v = cand[d, w] & compat[j, w]
                    if v != 0:
                        cand[e1, w] = v; nzw[e1, cnt] = w; cnt += 1
                nnz[e1] = cnt
                for q in range(suppn[j]):
                    x = supp[j, q]; cov[e1, x] += 1
                    sat = False
                    if isflex[x]:
                        sat = cov[e1, x] == 3
                    else:
                        need[e1, x] -= 1; sat = need[e1, x] == 0
                    if sat:
                        for t in range(cnt):
                            w = nzw[e1, t]; cand[e1, w] &= ~through[x, w]
                d = e1; action = 0; continue
            cand[d, j >> 6] &= ~(U1 << np.uint64(j & 63))
            action = 1; continue
        else:
            if d == 0: break
            d -= 1; j = P[d]
            cand[d, j >> 6] &= ~(U1 << np.uint64(j & 63))
            action = 2 if stop else 1
    return nodes, leaves[:nleaves], leafcov[:nleaves], not stop, overflow, counts


