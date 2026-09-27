"""Local probe of one block type of C1's tier lists (note 45): CNF as sat_local_batch.py (lex-leader under Stab_B6, prefix 6),
solved by pysat's CaDiCaL 1.9.5 in a child process that the parent terminates after SECS (pysat's interrupt does not stop
cadical195 here).  Usage: python local_tier_probe.py <c1_tiers dir> <TYPES.json> <i> <SECS>     prints one PROBE line"""
import sys, os, time, itertools, multiprocessing as mp


def solve(tdir, types_file, i, q):
    sys.path.insert(0, os.path.join(tdir, '..', 'structures')); sys.path.insert(0, tdir)
    import json
    from sat_local import encode
    from fullblock_symmetry import lexleader_clauses
    from pivot_types import stabiliser
    from pysat.solvers import Solver
    rec = json.load(open(types_file))[i]; t0 = time.time()
    cnf, pool, far, edges = encode(rec['mu'], rec['tau'], ())
    G = stabiliser(rec['mu'], rec['tau']); cnt = itertools.count()
    if len(G) > 1:
        cnf.extend(lexleader_clauses(rec['mu'], lambda z, e: pool.id(('x', z, e)), lambda: pool.id(('lex', next(cnt))), prefix_roots=6, G=G))
    q.put(('encoded', len(G), pool.top, len(cnf.clauses), round(time.time() - t0, 1)))
    with Solver(name='cadical195', bootstrap_with=cnf.clauses) as s:
        res = s.solve()
    q.put(('done', {True: 'SAT', False: 'UNSAT'}[res], round(time.time() - t0)))


if __name__ == '__main__':
    tdir, tf, i, secs = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4])
    q = mp.Queue(); p = mp.Process(target=solve, args=(tdir, tf, i, q)); p.start(); t0 = time.time(); info = None; res = None
    while time.time() - t0 < secs and p.is_alive():
        try:
            m = q.get(timeout=5)
            if m[0] == 'encoded': info = m[1:]
            else: res = m[1:]; break
        except Exception: pass
    if res is None:
        try:
            m = q.get(timeout=1)
            if m[0] == 'done': res = m[1:]
        except Exception: pass
    if p.is_alive(): p.terminate()
    print("PROBE %s %d: %s  (|Stab|, vars, clauses, encode s) = %s  %.0fs" % (os.path.basename(tf), i, res[0] if res else "UNKNOWN (stopped)", info, time.time() - t0), flush=True)
