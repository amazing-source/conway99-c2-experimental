"""Rapid hypothesis bench for the route-(C) h-stage (C2, 28/09 night).
build: python bench.py build <id> <source> <n>   source = pairs json (gpairs) or stream file; caches pair_setup + baseline search time
test : python bench.py test <hyp> [ids]           runs hypothesis function HYP[hyp](ps) on every cached pair (12 procs), prints
                                                  kill rate, mean cost, and soundness vs baseline verdicts (a kill of a non-EXCLUDED pair = BUG)
Cache: data/bench/<id>.pkl (list of dicts: k, y1, y2, ps, verdict, t_base)."""
import sys, os, json, time, pickle, random, collections, numpy as np
from fractions import Fraction as F
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("FD_LEMMA_U", "1")
import frame_dfs as FD
LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BD = os.path.join(LAB, "data", "bench"); os.makedirs(BD, exist_ok=True)
_L = {}


def lat(lid):
    if lid not in _L:
        rec = json.load(open(os.path.join(LAB, "external_runs", "structures_3eceb4d", "U", "%s.json" % lid)))
        _L[lid] = FD.lattice_data(rec["gens"])
    return _L[lid]


def load_pairs(src):
    if src.endswith(".txt"):
        out = []
        for l in open(src):
            r = json.loads(l)
            if "o" in r and "y1" in r: out.append((r["y1"], r["y2"]))
        return out
    return [tuple(p) for p in json.load(open(src))["pairs"]]


def _one(args):
    lid, k, y1a, y2a = args
    L = lat(lid); Binv = np.linalg.inv(np.array([[float(x) for x in r] for r in L["B"]]))
    yy = [np.rint(np.array([float(F(x)) for x in c]) @ Binv).astype(np.int64) for c in (y1a, y2a)]
    os.environ["FD_PREBUDGET"] = "0"
    t0 = time.time(); r = FD.search(L, yy[0], yy[1]); tb = time.time() - t0
    ps, why = FD.pair_setup(L, yy[0], yy[1])
    return {"lid": lid, "k": k, "y1": yy[0], "y2": yy[1], "ps": ps, "verdict": r["verdict"], "t_base": tb,
            "nodes": r.get("nodes"), "secs": r.get("secs")}


def build(lid, src, n):
    P = load_pairs(src); random.seed(7); ks = random.sample(range(len(P)), min(n, len(P)))
    with ProcessPoolExecutor(12) as ex:
        res = list(ex.map(_one, [(lid, k, P[k][0], P[k][1]) for k in ks]))
    pickle.dump(res, open(os.path.join(BD, "%s.pkl" % lid), "wb"))
    c = collections.Counter(r["verdict"][:40] for r in res)
    print("%s: %d pairs cached; baseline mean %.2fs/pair; verdicts %s" % (lid, len(res), np.mean([r["t_base"] for r in res]), dict(c)))


HYP = {}


def hyp(name):
    def deco(f): HYP[name] = f; return f
    return deco


def _test(args):
    name, rec = args
    import bench as B, bench_hyps  # noqa  (registers hypotheses into module 'bench')
    L = B.lat(rec["lid"]); t0 = time.time()
    try: kill = B.HYP[name](L, rec)
    except Exception as e: kill = "ERR %s" % repr(e)[:80]
    return rec["lid"], rec["verdict"], kill, time.time() - t0, rec["t_base"]


def test(name, ids):
    import bench_hyps  # noqa
    recs = []
    for lid in ids: recs += pickle.load(open(os.path.join(BD, "%s.pkl" % lid), "rb"))
    t0 = time.time()
    with ProcessPoolExecutor(12) as ex:
        out = list(ex.map(_test, [(name, r) for r in recs]))
    by = collections.defaultdict(list)
    for lid, v, kill, t, tb in out: by[lid].append((v, kill, t, tb))
    for lid, rows in by.items():
        kills = sum(1 for v, k_, t, tb in rows if k_ is True); errs = sum(1 for r in rows if isinstance(r[1], str))
        bugs = sum(1 for v, k_, t, tb in rows if k_ is True and not v.startswith("EXCLUDED"))
        mt = np.mean([t for _, _, t, _ in rows]); mb = np.mean([tb for *_, tb in rows])
        # projected cost with the hypothesis as a pre-filter: t_h always + baseline on survivors
        proj = np.mean([t + (0 if k_ is True else tb) for v, k_, t, tb in rows])
        print("%-12s %s: kill %d/%d (%.0f%%)  test %.3fs  base %.2fs  -> projected %.2fs/pair (x%.1f)  errors %d  UNSOUND-KILLS %d" % (
            name, lid, kills, len(rows), 100.0 * kills / len(rows), mt, mb, proj, mb / proj, errs, bugs))
    print("wall %.0fs" % (time.time() - t0))


if __name__ == "__main__":
    if sys.argv[1] == "build": build("%03d" % int(sys.argv[2]), sys.argv[3], int(sys.argv[4]))
    else: test(sys.argv[2], ["%03d" % int(x) for x in sys.argv[3:]] or ["078", "097"])
