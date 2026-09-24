"""Microscope experiment E1 ("grid profile"): how many sib D-edges (= grids through the fixed vertex x) can a C2 Conway graph have?

A block pair {i,j} is "sib" when the two sister orbits (i,j,0),(i,j,1) are D-partners (a=b=1), i.e. when the two lines of x in blocks i,j span
a 3x3 grid. BvLS (m=11) and Paley9 (m=2) have ALL pairs sib; phase 2 reported allsib UNSAT at m=7 in 33 s (uncertified).
For a set P of block pairs we add the units a=b=1 on every pair of P ("at least these grids") to the exact orbit CNF (orbit_sat.build(7,'none'))
and run CaDiCaL 1.9.5 in a subprocess with a hard wall-clock limit (pysat's interrupt does not stop cadical195).
Output: one JSON line per configuration in data/grid_profile.jsonl.  A timeout is not evidence; UNSAT here is uncertified (no DRAT).
"""
import itertools, json, multiprocessing as mp, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
OUT = os.path.join(HERE, "..", "data", "grid_profile.jsonl")
M = 7
BLOCKS = list(range(1, M + 1))
ALLPAIRS = list(itertools.combinations(BLOCKS, 2))


def worker(pairs, extra, q):
    import orbit_sat
    from pysat.solvers import Solver
    t0 = time.time()
    cnf, pool, outer, rep, trep, A, B = orbit_sat.build(M, "none")
    units = []
    for (i, j) in pairs:
        U = outer.index((i, j, 0)); V = outer.index((i, j, 1))
        units += [A[U, V], B[U, V]]
    cls = [[u] for u in units]
    if extra == "nosib_others":   # the other pairs are NOT sib
        for (i, j) in ALLPAIRS:
            if (i, j) in pairs: continue
            U = outer.index((i, j, 0)); V = outer.index((i, j, 1))
            cls.append([-A[U, V], -B[U, V]])
    with Solver(name="cadical195", bootstrap_with=cnf.clauses + cls) as s:
        t1 = time.time()
        res = s.solve()
        st = s.accum_stats()
        model = s.get_model() if res else None
    lift_ok = None
    if res:
        Mx, lift_ok = orbit_sat.lift(M, outer, rep, trep, A, B, model)
    q.put({"result": {True: "SAT", False: "UNSAT"}[res], "solve_s": round(time.time() - t1, 1), "build_s": round(t1 - t0, 1),
           "stats": st, "lift_ok": lift_ok})


def run(pairs, extra, tlimit):
    q = mp.Queue()
    p = mp.Process(target=worker, args=(pairs, extra, q)); p.start()
    p.join(tlimit)
    if p.is_alive():
        p.terminate(); p.join()
        return {"result": "TIMEOUT", "solve_s": tlimit}
    return q.get() if not q.empty() else {"result": "ERROR"}


def graph_type(nonsib):
    """canonical label of the complement graph (non-sib pairs) up to S7: sorted degree sequence + edge count (coarse)"""
    deg = {b: 0 for b in BLOCKS}
    for (i, j) in nonsib: deg[i] += 1; deg[j] += 1
    return "e%d_deg%s" % (len(nonsib), "".join(str(d) for d in sorted(deg.values(), reverse=True)))


def configs():
    out = []
    # g = 21 .. 17 : representatives of complement graphs by (edges, degree sequence) -- enumerate all subsets, keep one per type
    for e in range(0, 5):
        seen = {}
        for ns in itertools.combinations(ALLPAIRS, e):
            t = graph_type(ns)
            if t not in seen: seen[t] = ns
        for t, ns in sorted(seen.items()):
            out.append((21 - e, t, [p for p in ALLPAIRS if p not in ns]))
    # lower g: random subsets
    rng = random.Random(7)
    for g in (14, 10, 7, 5, 3, 2, 1):
        for rep in range(3):
            P = rng.sample(ALLPAIRS, g)
            out.append((g, "rand%d" % rep, sorted(P)))
    return out


if __name__ == "__main__":
    tlimit = float(sys.argv[1]) if len(sys.argv) > 1 else 60
    par = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    cf = configs()
    print("configurations:", len(cf), flush=True)
    from concurrent.futures import ThreadPoolExecutor
    def job(c):
        g, t, P = c
        r = run(P, None, tlimit)
        rec = {"g": g, "type": t, "pairs": P, "tlimit": tlimit, **r}
        with open(OUT, "a") as f: f.write(json.dumps(rec) + "\n")
        print(g, t, r["result"], r.get("solve_s"), flush=True)
        return rec
    with ThreadPoolExecutor(max_workers=par) as ex:
        list(ex.map(job, cf))
