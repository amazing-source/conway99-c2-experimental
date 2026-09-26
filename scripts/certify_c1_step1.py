"""Exact certification of C1's 48 pair-level models (3K2_or14, step 1; conway99-c1 commit df835e0,
data/k3k2_step1_models/case_NN.npz) with structures' certify.py (vendored, commit 746ee31): certify -> tree, then an
independent re-check of every tree with certify.check (exact rationals).  Output: logs/c1_step1_certs.jsonl.
Usage: python certify_c1_step1.py [maxnodes]"""
import sys, os, json, glob, time
import numpy as np, scipy.sparse as sp
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor_structures"))
from certify import certify, check
maxn = int(sys.argv[1]) if len(sys.argv) > 1 else 400
out = open("logs/c1_step1_certs.jsonl", "w"); stat = {}
for f in sorted(glob.glob("external_c1/data/k3k2_step1_models/case_*.npz")):
    z = np.load(f); A = sp.csr_matrix((z['A_data'], z['A_indices'], z['A_indptr']), shape=tuple(z['A_shape']))
    lo, hi, lb, ub = z['lo'], z['hi'], z['lb'], z['ub']
    t0 = time.time(); r = certify(A, lo, hi, lb, ub, maxnodes=maxn)
    ok = check(A, lo, hi, lb, ub, r['tree']) if r['status'] == 'dead' else False
    key = r['status'] + ('/' + r.get('level', '') if r['status'] == 'dead' else '') + ('/checked' if ok else '')
    stat[key] = stat.get(key, 0) + 1
    out.write(json.dumps({"case": os.path.basename(f), "status": r['status'], "level": r.get('level'), "nodes": r['nodes'],
                          "checked": ok, "tree": r.get('tree')}) + chr(10)); out.flush()
    print(os.path.basename(f), r['status'], r.get('level', r.get('why', '')), r['nodes'], "check", ok, "%.1fs" % (time.time() - t0)); sys.stdout.flush()
print("SUMMARY", stat)
