"""All H-beta skeletons up to D7 (note 32): column-model LP with (P2), one LP per skeleton class, exact certificate check.
Usage: python hb_colmodel_all.py <worker k> <workers K>   -> logs/hb_colall_<k>.jsonl  (one line per class)
Each line: class index, canonical orbit list, LP min slack, certificate verdict, (y^T b, LB, UB), nonzero rational duals by row name."""
import sys, time, json, itertools
from fractions import Fraction
sys.path.insert(0, "scripts")
import hb_pairlevel as H, hb_colmodel as CM, m1_blocks4 as M4
N = H.N

def skeleton_from(In, bits):
    orbits = []
    for c in range(N):
        A, B = In[c] if not (bits >> c) & 1 else In[c][::-1]
        seq = [(c - 1) % N, A, B, (c + 1) % N]
        for x, y in zip(seq, seq[1:]): orbits += [(c, x, y), (c, y, x)]
    return orbits

def canon(orbits):
    best = None
    for s in (1, -1):
        for r in range(N):
            img = tuple(sorted(tuple((s * v + r) % N for v in z) for z in orbits))
            if best is None or img < best: best = img
    return best

def classes():
    seen = {}; out = []
    for In, Ab in M4.orientations(7):
        for bits in range(128):
            orb = skeleton_from(In, bits); key = canon(orb)
            if key in seen: seen[key] += 1; continue
            seen[key] = 1; out.append(key)
    return out, seen

if __name__ == "__main__":
    k, K = int(sys.argv[1]), int(sys.argv[2])
    cls, mult = classes()
    if k == 0: print("skeleton classes:", len(cls), "| total skeletons:", sum(mult.values())); sys.stdout.flush()
    f = open("logs/hb_colall_%d.jsonl" % k, "w")
    for idx, key in enumerate(cls):
        if idx % K != k: continue
        t0 = time.time()
        orbits = [tuple(z) for z in key]
        cm = CM.ColModel(orbits, True)
        obj = cm.solve()
        rec = {"idx": idx, "mult": mult[key], "orbits": orbits, "ncols": len(cm.cols), "slack": obj}
        if obj > 1e-6:
            ok, info = cm.certificate_ok(); rec["cert"] = ok; rec["bounds"] = info
            y = cm.h.getSolution().row_dual
            rec["y"] = [[str(cm.rows[r][3]), str(Fraction(y[r]).limit_denominator(10 ** 7))] for r in range(len(cm.rows)) if abs(y[r]) > 1e-10]
        else:
            rec["cert"] = None
        rec["secs"] = round(time.time() - t0, 1)
        f.write(json.dumps(rec) + "\n"); f.flush()
    f.close()
