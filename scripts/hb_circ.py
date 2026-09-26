"""Circulant H-beta skeletons (Z7-invariant orientation and beta order), ALL free-cycle assignments (note 32; capped run approved 26/09).
1. Pairwise tables: for blocks (0, d), d = 1, 2, 3, and every pair of valid cycles, the LP of F2 with only these two blocks fixed
   (others relaxed to the cycle hull).  Infeasible -> certified by an exact rational check.  By Z7 symmetry the tables give every
   block pair (j, j+d).
2. Full assignments consistent with all 21 pairwise tables (backtracking, no LP).
3. LP of F2 at each such leaf (certified when infeasible).  Survivors are written to a json file for the integer / P2 stage.
Usage: python hb_circ.py <orient 23|2m3> <order 0|1>"""
import sys, time, json
sys.path.insert(0, "scripts")
import hb_pairlevel as H, hb_tree as T, hb_dfs as D
N = H.N

def canon(nb):
    return frozenset(frozenset((a, b)) for a, ws in nb.items() for b in ws)

if __name__ == "__main__":
    orient, order = sys.argv[1], int(sys.argv[2])
    t0 = time.time()
    In, orbits = H.skeleton(orient, order)
    inst = T.Instance(orbits); fl = D.FastLP(inst)
    C = len(inst.cycles[0])
    key = {j: {canon(nb): c for c, nb in enumerate(inst.cycles[j])} for j in range(N)}
    # rot[j][c] = index at block j+1 of the rotation of cycle c at block j
    rot = {j: [key[(j + 1) % N][frozenset(frozenset(H.rot(z, 1) for z in e) for e in canon(nb))] for nb in inst.cycles[j]] for j in range(N)}
    def rotate_to0(j, c):             # index at block 0 of cycle c at block j rotated by -j
        # apply rot (7 - j) times starting at block j
        b, cc = j, c
        for _ in range((N - j) % N): cc = rot[b][cc]; b = (b + 1) % N
        assert b == 0; return cc
    def rotate_from0(c, s):           # index at block s of cycle c at block 0 rotated by +s
        b, cc = 0, c
        for _ in range(s): cc = rot[b][cc]; b = (b + 1) % N
        return cc
    tab = {}; stat = {"lp": 0, "cert_ok": 0, "cert_fail": 0}
    for d in (1, 2, 3):
        for a in range(C):
            for b in range(len(inst.cycles[d])):
                obj = fl.solve({0: a, d: b}); stat["lp"] += 1
                ok = obj <= 1e-6
                if not ok:
                    if fl.certificate_ok({0: a, d: b}): stat["cert_ok"] += 1
                    else: stat["cert_fail"] += 1; ok = True          # uncertified -> treat as compatible (conservative)
                tab[d, a, b] = ok
    print("pair tables: %s | compatible fractions:" % stat, {d: round(sum(tab[d, a, b] for a in range(C) for b in range(C)) / C / C, 3) for d in (1, 2, 3)}, "%.0fs" % (time.time() - t0)); sys.stdout.flush()
    def compat(j1, c1, j2, c2):
        d = (j2 - j1) % N
        if d > 3: return compat(j2, c2, j1, c1)
        # rotate so that j1 -> 0
        a = rotate_to0(j1, c1)
        b = c2
        bb, cc = j2, c2
        for _ in range((N - j1) % N): cc = rot[bb][cc]; bb = (bb + 1) % N
        assert bb == d
        return tab[d, a, cc]
    leaves = []
    def bt(assign):
        j = len(assign)
        if j == N: leaves.append(list(assign)); return
        for c in range(len(inst.cycles[j])):
            if all(compat(i, assign[i], j, c) for i in range(j)):
                assign.append(c); bt(assign); assign.pop()
    bt([])
    print("assignments consistent with all pair tables:", len(leaves), "%.0fs" % (time.time() - t0)); sys.stdout.flush()
    surv = []; st2 = {"cert_ok": 0, "cert_fail": 0}
    for L in leaves:
        fx = {j: L[j] for j in range(N)}
        obj = fl.solve(fx)
        if obj <= 1e-6: surv.append(L); continue
        if fl.certificate_ok(fx): st2["cert_ok"] += 1
        else: st2["cert_fail"] += 1; surv.append(L)
    print("leaf LP: %s | LP survivors: %d" % (st2, len(surv)), "%.0fs" % (time.time() - t0))
    json.dump({"orient": orient, "order": order, "survivors": surv}, open("logs/hb_circ_%s_%d.json" % (orient, order), "w"))
