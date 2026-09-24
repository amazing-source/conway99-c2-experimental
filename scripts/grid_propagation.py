"""E7: grid propagation test.  Given sib pairs (grids through x), is a further grid forced?

Root <-> label: a e_i + b e_j (i<j, a,b = +-1) <-> {(i,s_a),(j,s_b)} with s=0 for +, 1 for -; orbit (i,j,s_a^s_b), side s_a.
adj(root u, root v) = a[U,V] if side(u)==side(v) else b[U,V]  (U != V).
Test grid(y; l1, l2) at an inner vertex y = +e_c between the sister lines m_p = {e_c, e_c +- e_p} and m_q = {e_c, e_c +- e_q}:
corners K_ab = unique outer common neighbour of (e_c + a e_p) and (e_c + b e_q); grid <=> Row_+ & Row_- & Col_+ & Col_-.
We add the clause NOT grid and ask CaDiCaL (hard time limit).  UNSAT => the grid is forced (uncertified).
Usage: python grid_propagation.py "<sib pairs e.g. 56 67>" <c> <p> <q> <tlimit>
"""
import json, os, sys, time, itertools, multiprocessing as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
M = 7


def root_bits(root, outer):
    """root: dict {block: sign}.  returns (orbit index, side)"""
    (i, a), (j, b) = sorted(root.items())
    sa, sb = (0 if a > 0 else 1), (0 if b > 0 else 1)
    return outer.index((i, j, sa ^ sb)), sa


def adj_lit(r1, r2, outer, A, B):
    """None if r2 = -r1 (same orbit: never adjacent, u !~ sigma u)."""
    U, su = root_bits(r1, outer); V, sv = root_bits(r2, outer)
    if U == V:
        return None
    return A[U, V] if su == sv else B[U, V]


def worker(pairs, c, p, q, q_out):
    import orbit_sat
    from pysat.solvers import Solver
    cnf, pool, outer, rep, trep, A, B = orbit_sat.build(M, "none")
    for (i, j) in pairs:
        U0 = outer.index((i, j, 0)); U1 = outer.index((i, j, 1))
        cnf.append([A[U0, U1]]); cnf.append([B[U0, U1]])
    others = [k for k in range(1, M + 1) if k not in (c, p, q)]
    cand = [dict([(i, a), (j, b)]) for i, j in itertools.combinations(others, 2) for a in (1, -1) for b in (1, -1)]
    def AND(*xs):
        z = pool.id(("and",) + tuple(xs))
        cnf.extend([[-z, x] for x in xs]); cnf.append([z] + [-x for x in xs]); return z
    K = {}
    for a in (1, -1):
        for b in (1, -1):
            u = {c: 1, p: a}; v = {c: 1, q: b}
            K[a, b] = [AND(adj_lit(g, u, outer, A, B), adj_lit(g, v, outer, A, B)) for g in cand]
    def rowcol(k1, k2):
        terms = []
        for x, g in enumerate(cand):
            for y, h in enumerate(cand):
                if x == y: continue
                e = adj_lit(g, h, outer, A, B)
                if e is None: continue
                terms.append(AND(K[k1][x], K[k2][y], e))
        r = pool.id(("rc", k1, k2))
        cnf.extend([[-r] + terms]); cnf.extend([[r, -t] for t in terms]); return r
    R = [rowcol((1, 1), (1, -1)), rowcol((-1, 1), (-1, -1)), rowcol((1, 1), (-1, 1)), rowcol((1, -1), (-1, -1))]
    cnf.append([-x for x in R])           # NOT grid
    t1 = time.time()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        res = s.solve(); st = s.accum_stats()
    q_out.put({"result": {True: "SAT", False: "UNSAT"}[res], "solve_s": round(time.time() - t1, 1), "stats": st})


if __name__ == "__main__":
    pairs = [(int(x[0]), int(x[1])) for x in sys.argv[1].split()]
    c, p, q = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); tl = float(sys.argv[5])
    qq = mp.Queue(); pr = mp.Process(target=worker, args=(pairs, c, p, q, qq)); t0 = time.time(); pr.start(); pr.join(tl)
    if pr.is_alive():
        pr.terminate(); pr.join(); r = {"result": "TIMEOUT", "solve_s": tl}
    else:
        r = qq.get() if not qq.empty() else {"result": "ERROR"}
    rec = {"pairs": pairs, "vertex": c, "lines": [p, q], **r}
    with open(os.path.join(HERE, "..", "data", "grid_propagation.jsonl"), "a") as f: f.write(json.dumps(rec) + "\n")
    print(json.dumps(rec))
