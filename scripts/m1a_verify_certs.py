"""Independent re-check of the stored H-beta certificates (note 32).  For each skeleton class in logs/m1a_res_*.jsonl:
rebuild the column model from the stored orbit list, read the stored rational multipliers y (keyed by row name), and check in
exact arithmetic that y^T b lies outside [LB, UB], the range of y^T A x over the box (x_c in [0,1], slack of every '<=' row in
[0, rhs]).  No LP solver is used here.
Usage: python hb_verify_certs.py [max_classes]"""
import sys, json, glob, time, gzip
from fractions import Fraction
from collections import defaultdict
sys.path.insert(0, "scripts")
import m1a_colmodel as CM

def check(rec):
    orbits = [tuple(z) for z in rec["orbits"]]
    cm = CM.ColModel(orbits, True)
    byname = {str(r[3]): i for i, r in enumerate(cm.rows)}
    y = {}
    for name, val in rec["y"]:
        if name not in byname: return False, "unknown row " + name
        y[byname[name]] = Fraction(val)
    c = defaultdict(Fraction); yb = Fraction(0)
    for r, yr in y.items():
        terms, rhs, kind, name = cm.rows[r]
        yb += yr * rhs
        for col, v in terms: c[col] += yr * v
    UB = LB = Fraction(0)
    for col in range(len(cm.cols)):
        cv = c.get(col, Fraction(0)); UB += max(cv, 0); LB += min(cv, 0)
    for r, (terms, rhs, kind, name) in enumerate(cm.rows):
        if kind == 'le' and r in y:
            cv = y[r] * rhs; UB += max(cv, 0); LB += min(cv, 0)
    return (yb > UB or yb < LB), (float(yb), float(LB), float(UB))

if __name__ == "__main__":
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 9
    k, K = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (0, 1)
    t0 = time.time(); ok = bad = 0; mult = 0
    files = sorted(glob.glob("logs/m1a_res_*.jsonl"))
    if files: recs = [json.loads(l) for f in files for l in open(f)]
    else: recs = [json.loads(l) for f in sorted(glob.glob("logs/m1a_certs/m1a_res_*.jsonl.gz")) for l in gzip.open(f, "rt")]
    recs = sorted(recs, key=lambda r: r["idx"])
    for rec in recs[:lim]:
        if rec["idx"] % K != k: continue
        if rec.get("cert") is not True: bad += 1; print("class", rec["idx"], "has no certificate"); continue
        v, info = check(rec)
        if v: ok += 1; mult += rec["mult"]
        else: bad += 1; print("class", rec["idx"], "FAILED", info)
    print("verified:", ok, "| failed or missing:", bad, "| skeletons covered:", mult, "| %.0fs" % (time.time() - t0))
