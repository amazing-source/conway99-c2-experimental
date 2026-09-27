"""beta CUBES for the finish line (A) (C1, 27/09; note 46): the per-label disjunction SEC_v or SEC-dis_v is a tautology, so I(tau)
must be split by the pattern beta (1 = the orbit of the non-pivot label v is dis).
- For a type tau, the non-pivot labels NP (mu v != tau v) are split into:
  - forced dis labels: the units of C1 notes/137, i.e. v or pi v with mu v = pi v or tau v = pi v;
  - free labels.
- Patterns: every subset of the free labels made dis. For fewer than 6 pivots, only those with 2 #piv + #dis >= 12.
- One CNF per pattern: enc2_dimacs.py ... --beta --betadis=<dis labels> (units on beta), then cadical.exe (C1's win64 build) with
  a time cap and no proof (pass 1). One JSON line per cube in logs/cubes_<id>.jsonl.
Completeness: every configuration's heavy block has SOME true beta, among the enumerated patterns (no symmetry reduction here).
Usage: python beta_cubes.py <type id> [cap seconds=300] [workers=2] [extra enc2 flags...]"""
import sys, os, json, time, itertools, subprocess, hashlib
from concurrent.futures import ThreadPoolExecutor
LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TYPES = os.path.join(LAB, "scripts", "structures", "all_types_3308.json")
CAD = os.path.join(LAB, "tools", "win64", "cadical.exe"); PY = sys.executable
FLAGS = ["--cuts", "--digon", "--path", "--twist", "--ident=1", "--balance"]


def patterns(rec):
    mu, tau = rec["mu"], rec["tau"]
    npl = [v for v in range(12) if mu[v] != tau[v]]; piv = 12 - len(npl)
    forced = {v for v in npl if mu[v] == v ^ 1 or tau[v] == v ^ 1}
    forced |= {v ^ 1 for v in forced if (v ^ 1) in npl}
    free = [v for v in npl if v not in forced]
    out = []
    for k in range(len(free) + 1):
        for S in itertools.combinations(free, k):
            dis = sorted(forced | set(S))
            if piv < 6 and 2 * piv + len(dis) < 12: continue
            out.append(dis)
    return npl, sorted(forced), out


def run_cube(tid, dis, cap, extra):
    tag = "t%d_d%s" % (tid, "-".join(map(str, dis)) or "none")
    cnf = os.path.join(LAB, "sat", "cubes", tag + ".cnf")
    env = dict(os.environ, SAT_LOCAL_DIR=os.path.join(LAB, "scripts", "structures"))
    subprocess.run([PY, "enc2_dimacs.py", TYPES, str(tid), os.path.join(LAB, "sat", "cubes")] + FLAGS + extra +
                   ["--beta", "--betadis=" + ",".join(map(str, dis)), "--nolex", "--out=" + cnf],
                   cwd=os.path.join(LAB, "scripts", "c1_tiers"), env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    sha = hashlib.sha256(open(cnf, "rb").read()).hexdigest()[:16]
    t0 = time.time()
    p = subprocess.Popen([CAD, "-q", cnf], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=0x40)   # IDLE_PRIORITY_CLASS
    try: rc = p.wait(timeout=cap)
    except subprocess.TimeoutExpired: p.kill(); p.wait(); rc = None
    st = {20: "UNSAT", 10: "SAT"}.get(rc, "UNKNOWN" if rc is None else "rc%s" % rc)
    return {"id": tid, "dis": dis, "ndis": len(dis), "status": st, "secs": round(time.time() - t0, 1), "cnf_sha": sha}


if __name__ == "__main__":
    tid = int(sys.argv[1]); cap = float(sys.argv[2]) if len(sys.argv) > 2 else 300; nw = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    extra = sys.argv[4:]
    rec = json.load(open(TYPES))[tid]; npl, forced, pats = patterns(rec)
    os.makedirs(os.path.join(LAB, "sat", "cubes"), exist_ok=True)
    out = os.path.join(LAB, "logs", "cubes_%d.jsonl" % tid)
    done = set()
    if os.path.exists(out):
        for l in open(out): done.add(tuple(json.loads(l)["dis"]))
    todo = [d for d in pats if tuple(d) not in done]
    print("type %d: %d pivots, non-pivot labels %s, forced dis %s, %d patterns (%d to run)" % (tid, 12 - len(npl), npl, forced, len(pats), len(todo)), flush=True)
    with ThreadPoolExecutor(nw) as ex:
        for r in ex.map(lambda d: run_cube(tid, d, cap, extra), todo):
            open(out, "a").write(json.dumps(r) + "\n"); print("  dis=%s: %s %.0fs" % (r["dis"], r["status"], r["secs"]), flush=True)
    R = [json.loads(l) for l in open(out)]
    from collections import Counter
    print("CUBES %d: %s | by #dis: %s" % (tid, dict(Counter(r["status"] for r in R)),
          {k: dict(Counter(r["status"] for r in R if r["ndis"] == k)) for k in sorted({r["ndis"] for r in R})}), flush=True)
