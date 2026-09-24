"""E4: does adding the (implied) consequences of Lemma S1 make sib-rich instances easy for CDCL?

Sib pair p = {i,j}: orbits U0=(i,j,0), U1=(i,j,1) with a=b=1 between them.  Implied constraints added (all consequences of the exact model):
 (L1) V avoiding p        : Q[V,U0] + Q[V,U1] = 1                       (Lemma S1 (4))
 (L2) V touching one of p : Q[V,U0] = Q[V,U1] = 0
 (L3) s_V := [Q[V,U0]=1] for V avoiding p ; for V avoiding p : sum_{W avoiding} Q[V,W]*[s_W==s_V] = 3 and *[s_W!=s_V] = 2   (Lemma S1 (5))
 (L4) V touching exactly one block of p : sum_{W avoiding} Q[V,W]*s_W = 3 and Q[V,W]*(1-s_W) = 3                           (Lemma S1 (6))
Q[V,W] = a_VW + b_VW.  Modes: base (model + sib units only) vs lemma (model + sib units + L1..L4).
Usage: python sib_lemma_sat.py <pairs e.g. 12 or 12,34> <mode base|lemma> <tlimit>
"""
import json, os, sys, time, multiprocessing as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
M = 7


def add_lemma(cnf, pool, outer, A, B, p):
    from pysat.card import CardEnc, EncType
    i, j = p
    U0 = outer.index((i, j, 0)); U1 = outer.index((i, j, 1))
    N = len(outer)
    avoid = [V for V in range(N) if not ({outer[V][0], outer[V][1]} & {i, j})]
    one = [V for V in range(N) if len({outer[V][0], outer[V][1]} & {i, j}) == 1]
    def eq(lits, k):
        cnf.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    def AND(x, y):
        z = pool.id(("and", x, y)); cnf.extend([[-z, x], [-z, y], [z, -x, -y]]); return z
    def XNOR(x, y):
        z = pool.id(("xnor", x, y)); cnf.extend([[-z, -x, y], [-z, x, -y], [z, x, y], [z, -x, -y]]); return z
    s = {}
    for V in avoid:
        eq([A[V, U0], B[V, U0], A[V, U1], B[V, U1]], 1)                                  # L1
        sv = pool.id(("s", p, V)); s[V] = sv
        cnf.extend([[-sv, A[V, U0], B[V, U0]], [sv, -A[V, U0]], [sv, -B[V, U0]]])        # s_V <-> Q[V,U0]=1
    for V in one:
        cnf.extend([[-A[V, U0]], [-B[V, U0]], [-A[V, U1]], [-B[V, U1]]])                  # L2
    for V in avoid:                                                                       # L3
        same, diff = [], []
        for W in avoid:
            if W == V: continue
            e = XNOR(s[V], s[W]); ne = -e
            for x in (A[V, W], B[V, W]):
                same.append(AND(x, e)); diff.append(AND(x, ne))
        eq(same, 3); eq(diff, 2)
    for V in one:                                                                         # L4
        l1, l0 = [], []
        for W in avoid:
            for x in (A[V, W], B[V, W]):
                l1.append(AND(x, s[W])); l0.append(AND(x, -s[W]))
        eq(l1, 3); eq(l0, 3)


def worker(pairs, mode, q):
    import orbit_sat
    from pysat.solvers import Solver
    cnf, pool, outer, rep, trep, A, B = orbit_sat.build(M, "none")
    for p in pairs:
        U0 = outer.index((p[0], p[1], 0)); U1 = outer.index((p[0], p[1], 1))
        cnf.append([A[U0, U1]]); cnf.append([B[U0, U1]])
        if mode == "lemma": add_lemma(cnf, pool, outer, A, B, p)
    t1 = time.time()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        res = s.solve(); st = s.accum_stats(); model = s.get_model() if res else None
    lift_ok = None
    if res:
        Mx, lift_ok = orbit_sat.lift(M, outer, rep, trep, A, B, model)
    q.put({"result": {True: "SAT", False: "UNSAT"}[res], "solve_s": round(time.time() - t1, 1), "stats": st, "lift_ok": lift_ok,
           "vars": pool.top, "clauses": len(cnf.clauses)})


if __name__ == "__main__":
    pairs = [tuple(int(c) for c in x) for x in sys.argv[1].split(",")]
    mode = sys.argv[2]; tlimit = float(sys.argv[3])
    q = mp.Queue(); pr = mp.Process(target=worker, args=(pairs, mode, q)); t0 = time.time(); pr.start(); pr.join(tlimit)
    if pr.is_alive():
        pr.terminate(); pr.join(); r = {"result": "TIMEOUT", "solve_s": tlimit}
    else:
        r = q.get() if not q.empty() else {"result": "ERROR"}
    rec = {"pairs": pairs, "mode": mode, "tlimit": tlimit, "wall": round(time.time() - t0, 1), **r}
    with open(os.path.join(HERE, "..", "data", "sib_lemma_sat.jsonl"), "a") as f: f.write(json.dumps(rec) + "\n")
    print(json.dumps(rec))
