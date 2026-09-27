"""Local probe of one block type of C1's tier lists (note 45): CNF as sat_local_batch.py (lex-leader under Stab_B6, prefix 6),
solved by pysat's CaDiCaL 1.9.5 in a child process that the parent terminates after SECS (pysat's interrupt does not stop
cadical195 here).  Usage: python local_tier_probe.py <c1_tiers dir> <TYPES.json> <i> <SECS> [--enc2] [--cuts]     prints one PROBE line
--cuts: structures' lemma cuts (NOTE_S29 s.9, sat_local2.encode(cuts=True)); SAT -> logs/tiers/<file>_<i>_local_satsol.json
--enc2: structures' second encoding (sat_local2.py, iota-pairs; same far/edge indexing, so C1's lex-leader applies unchanged)"""
import sys, os, time, itertools, multiprocessing as mp


def solve(tdir, types_file, i, q, enc2=False, cuts=False):
    sys.path.insert(0, os.path.join(tdir, '..', 'structures')); sys.path.insert(0, tdir)
    import json
    from sat_local import encode
    if enc2: from sat_local2 import encode
    from fullblock_symmetry import lexleader_clauses
    from pivot_types import stabiliser
    from pysat.solvers import Solver
    rec = json.load(open(types_file))[i]; t0 = time.time()
    cnf, pool, far, edges = encode(rec['mu'], rec['tau'], (), cuts=True) if cuts else encode(rec['mu'], rec['tau'], ())
    G = stabiliser(rec['mu'], rec['tau']); cnt = itertools.count()
    if len(G) > 1:
        cnf.extend(lexleader_clauses(rec['mu'], lambda z, e: pool.id(('x', z, e)), lambda: pool.id(('lex', next(cnt))), prefix_roots=6, G=G))
    q.put(('encoded', len(G), pool.top, len(cnf.clauses), round(time.time() - t0, 1)))
    with Solver(name='cadical195', bootstrap_with=cnf.clauses) as s:
        res = s.solve()
        if res:
            model = set(l for l in s.get_model() if l > 0)
            phi = {str(list(far[z])): list(edges[e]) for z in range(60) for e in range(60) if pool.id(('x', z, e)) in model}
            os.makedirs('logs/tiers', exist_ok=True)
            json.dump({'cfg': {'mu': rec['mu'], 'tau': rec['tau'], 'types_file': os.path.basename(types_file), 'index': i,
                       'encoding': 2 if enc2 else 1, 'cuts': cuts}, 'Phi': phi},
                      open('logs/tiers/%s_%04d_local_satsol.json' % (os.path.basename(types_file)[:-5], i), 'w'), indent=1)
    q.put(('done', {True: 'SAT', False: 'UNSAT'}[res], round(time.time() - t0)))


if __name__ == '__main__':
    tdir, tf, i, secs = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4])
    q = mp.Queue(); p = mp.Process(target=solve, args=(tdir, tf, i, q, '--enc2' in sys.argv, '--cuts' in sys.argv)); p.start(); t0 = time.time(); info = None; res = None
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
    print("PROBE%s %s %d: %s  (|Stab|, vars, clauses, encode s) = %s  %.0fs" % ((" enc2" if "--enc2" in sys.argv else "") + (" cuts" if "--cuts" in sys.argv else ""), os.path.basename(tf), i, res[0] if res else "UNKNOWN (stopped)", info, time.time() - t0), flush=True)
