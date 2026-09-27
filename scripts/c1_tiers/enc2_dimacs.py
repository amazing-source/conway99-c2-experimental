"""C2: DIMACS export of structures' SECOND encoding (sat_local2.py, iota-pairs) for record i of a C1 types file, with C1's
lex-leader under Stab_B6(mu, tau) (prefix 6).  Both encodings index far roots and non-mu pairs identically (checked), and every
other variable is determined by x, so the symmetry breaking on x is sound here too.
Usage: python enc2_dimacs.py TYPES.json I OUTDIR [--cuts] [--digon] [--path]      writes OUTDIR/type_%04d_enc2.cnf
--cuts: structures' lemma cuts (NOTE_S29 s.9; sat_local2.encode(cuts=True)), named in the CNF comment"""
import sys, os, json, itertools, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.environ.get('SAT_LOCAL_DIR', os.path.join(HERE, '..', 'structures'))); sys.path.insert(0, HERE)
from sat_local2 import encode
from fullblock_symmetry import lexleader_clauses
from pivot_types import stabiliser
types, i, od = json.load(open(sys.argv[1])), int(sys.argv[2]), sys.argv[3]
rec = types[i]; t0 = time.time()
cuts = '--cuts' in sys.argv; digon = '--digon' in sys.argv; path = '--path' in sys.argv
cnf, pool, far, edges = encode(rec['mu'], rec['tau'], (), cuts=cuts, digon=digon, **({'path': True} if path else {}))
G = stabiliser(rec['mu'], rec['tau']); cnt = itertools.count()
if len(G) > 1:
    cnf.extend(lexleader_clauses(rec['mu'], lambda z, e: pool.id(('x', z, e)), lambda: pool.id(('lex', next(cnt))), prefix_roots=6, G=G))
os.makedirs(od, exist_ok=True); path = os.path.join(od, 'type_%04d_enc2%s.cnf' % (i, ('c' if cuts else '') + ('d' if digon else '') + ('p' if path else '')))
cnf.to_file(path, comments=['c C2 enc2_dimacs (structures sat_local2' + (' + lemma cuts NOTE_S29 s.9' if cuts else '') + (' + DIGON balance (C1)' if digon else '') + (' + PATH excess (C1)' if path else '') + ' + C1 lex-leader) type %d mu %s tau %s |Stab| %d prefix 6' % (i, rec['mu'], rec['tau'], len(G))])
print('%d %s |Stab|=%d vars=%d clauses=%d DIMACS %s (%.0fs)' % (i, rec.get('anch_tw'), len(G), pool.top, len(cnf.clauses), path, time.time() - t0))
