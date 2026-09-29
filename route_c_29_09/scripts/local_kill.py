"""Is the stage-1 kill LOCAL? Re-run the general-mode stage-1 DFS (Lemma U+, no symmetry breaking) with the coverage constraints
kept only on a subset S of the new roots (points outside S are dropped: any coverage allowed there) -> a RELAXATION, so a kill of the
restricted problem is a kill of the pair. S = one shadow coset, or the new roots of one component of the Niemeier neighbour.
Usage: python local_kill.py <id> <n_pairs>"""
import sys, os, time, pickle, collections, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["FD_LEMMA_U"] = "1"
import frame_dfs as FD, bench as B


def run_restricted(L, ps, S, node_limit=300_000):
    H, W = ps["H"].astype(np.int64), ps["W"].astype(np.int64); V = ps["V"] if "V" in ps else H @ L["G"] @ W.T
    HS = (ps["HS"] if "HS" in ps else H @ L["G"] @ L["S2"].T)[:, S].astype(np.int64); WS = (ps["WS"] if "WS" in ps else W @ L["G"] @ L["S2"].T)[:, S].astype(np.int64)
    target = ps["target"][S]; flex = ps["flex"][S]; whit = np.abs(WS) == 3
    keep = np.ones(len(H), bool)                       # candidates stay the same (admissibility is a property of h)
    SUP = HS != 0; nH, nW = len(H), len(W)
    CBb = FD.compat_nb(H @ L["G"], H, FD.pack64(V == 1), FD.pack64(V == -1), FD.pack64(SUP & (target == 1)[None, :]))
    supn = SUP.sum(axis=1); supp = np.full((nH, max(1, int(supn.max()))), -1, dtype=np.int64)
    for i in range(nH): supp[i, :supn[i]] = np.flatnonzero(SUP[i])
    allM = FD.pack64(np.ones((1, nH), dtype=bool))[0]; allW = FD.pack64(np.ones((1, nW), dtype=bool))[0]
    t0 = time.time()
    nodes, leaves, lcov, complete, overflow, counts = FD.dfs_general_u(CBb, FD.pack64(SUP.T), supp, supn.astype(np.int64), FD.pack64(V == 0),
        FD.pack64(V == 1), FD.pack64(V == -1), FD.pack64(np.abs(V) == 2), FD.pack64(np.abs(V) == 1), target, flex, FD.pack64(whit), allM, allW,
        node_limit, 2000, H, W, V.astype(np.int64), WS.astype(np.int64), HS.astype(np.int64), FD.pack64(whit.T), -1, allM)
    return ("KILL" if complete and counts[0] == 0 else "alive" if complete else "incomplete"), int(sum(nodes)), time.time() - t0


if __name__ == "__main__":
    lid = "%03d" % int(sys.argv[1]); n = int(sys.argv[2])
    recs = pickle.load(open(os.path.join(B.BD, "%s.pkl" % lid), "rb"))[:n]
    L = B.lat(lid); G, S2, R = L["G"], L["S2"], L["R"]
    IP = S2 @ G @ S2.T                                  # 4 (beta, beta')
    coset = (IP[0] % 4 == 0)                            # same coset as point 0 <=> integer (beta_0, beta)
    # components of the Niemeier neighbour N_j = roots of U + new roots of coset j (2 beta has G-norm 8; root rows are 1x)
    def comps(mask):
        V_ = np.vstack([2 * R, S2[mask]]); P = (V_ @ G @ V_.T) != 0; n_ = len(V_); c = -np.ones(n_, int); k = 0
        for s in range(n_):
            if c[s] >= 0: continue
            st = [s]; c[s] = k
            while st:
                a = st.pop()
                for b in np.flatnonzero(P[a]):
                    if c[b] < 0: c[b] = k; st.append(b)
            k += 1
        cp = c[len(R):]; idx = np.flatnonzero(mask); return [idx[cp == q] for q in sorted(set(cp.tolist()))]
    parts = {"coset A": np.flatnonzero(coset), "coset B": np.flatnonzero(~coset)}
    for nm, m in (("A", coset), ("B", ~coset)):
        for q, ix in enumerate(comps(m)): parts["comp %s%d (%d pts)" % (nm, q, len(ix))] = ix
    print(lid, "points", len(S2), {k: len(v) for k, v in parts.items()}, flush=True)
    tally = collections.defaultdict(collections.Counter); tm = collections.defaultdict(float)
    for k_, rec in enumerate(recs):
        row = []
        for nm, S in parts.items():
            v, nd, t = run_restricted(L, rec["ps"], S); tally[nm][v] += 1; tm[nm] += t; row.append("%s:%s/%dk" % (nm.split(" (")[0], v[:4], nd // 1000))
        print("pair", k_, " ".join(row), flush=True)
    for nm in parts: print("%-22s %s  mean %.2fs" % (nm, dict(tally[nm]), tm[nm] / len(recs)), flush=True)
