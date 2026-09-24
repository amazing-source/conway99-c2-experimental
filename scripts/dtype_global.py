"""Experiment E3: global D-type patterns.  Force every D-edge to be of a given type (sib / one / dis) or forbid a type,
and see which patterns are quickly UNSAT (uncertified CaDiCaL, hard wall-clock limit).
Types of an orbit pair (U,V): sib = same block pair, one = exactly one shared block, dis = no shared block.
'only_T'  : a=b=1 forbidden on every pair not of type T  (all 21 D-edges of type T)
'no_T'    : a=b=1 forbidden on every pair of type T
"""
import json, os, sys, time, multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
OUT = os.path.join(HERE, "..", "data", "dtype_global.jsonl")
M = 7


def ptype(U, V):
    (i, j, e), (k, l, f) = U, V
    sh = len({i, j} & {k, l})
    return {2: "sib", 1: "one", 0: "dis"}[sh]


def worker(mode, q):
    import orbit_sat
    from pysat.solvers import Solver
    cnf, pool, outer, rep, trep, A, B = orbit_sat.build(M, "none")
    kind, T = mode.split("_")
    extra = []
    N = len(outer)
    for U in range(N):
        for V in range(U + 1, N):
            t = ptype(outer[U], outer[V])
            if (kind == "only" and t != T) or (kind == "no" and t == T):
                extra.append([-A[U, V], -B[U, V]])
    t1 = time.time()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses + extra) as s:
        res = s.solve(); st = s.accum_stats(); model = s.get_model() if res else None
    lift_ok = None
    if res:
        Mx, lift_ok = orbit_sat.lift(M, outer, rep, trep, A, B, model)
        import numpy as np
        np.savetxt(os.path.join(HERE, "..", "data", "SOLUTION_%s.txt" % mode), Mx, fmt="%d")
    q.put({"result": {True: "SAT", False: "UNSAT"}[res], "solve_s": round(time.time() - t1, 1), "stats": st, "lift_ok": lift_ok})


def run(mode, tlimit):
    q = mp.Queue(); p = mp.Process(target=worker, args=(mode, q)); p.start(); p.join(tlimit)
    if p.is_alive():
        p.terminate(); p.join(); return {"result": "TIMEOUT", "solve_s": tlimit}
    return q.get() if not q.empty() else {"result": "ERROR"}


if __name__ == "__main__":
    tlimit = float(sys.argv[1]) if len(sys.argv) > 1 else 300
    modes = sys.argv[2].split(",") if len(sys.argv) > 2 else ["only_sib", "only_one", "only_dis", "no_sib", "no_one", "no_dis"]
    par = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    def job(md):
        r = run(md, tlimit); rec = {"mode": md, "tlimit": tlimit, **r}
        with open(OUT, "a") as f: f.write(json.dumps(rec) + "\n")
        print(md, r["result"], r.get("solve_s"), flush=True)
    with ThreadPoolExecutor(max_workers=par) as ex:
        list(ex.map(job, modes))
