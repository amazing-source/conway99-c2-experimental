"""E6: map the boundary 'fast UNSAT vs hard' for sets of sib pairs (graphs on the 7 blocks).
Usage: python grid_map.py <tlimit> <parallel>
"""
import json, os, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grid_profile import run  # noqa

OUT = os.path.join(HERE, "..", "data", "grid_map.jsonl")
def E(s): return [(int(a), int(b)) for a, b in s.split()]
CONFIGS = [
    # isomorphic copies of the minimal cover K2+K2+P3 (sanity: should behave like {12,34,56,67}, UNSAT ~30 s)
    ("iso_cover4_a", E("12 13 45 67")),
    ("iso_cover4_b", E("12 34 35 67")),
    # 3K2 + one edge NOT covering block 7
    ("3K2+13_unc7", E("12 34 56 13")),
    # earlier 60-s timeouts, now 300 s
    ("spider5_unc6", E("14 25 37 45 57")),
    ("K2+K3pend_unc6", E("12 34 35 37 57")),
    # covering (all 7 blocks), 5 edges
    ("cov_K3+K2+K2", E("12 13 23 45 67")),
    ("cov_K13+P3", E("12 13 14 56 67")),
    ("cov_K2+P5", E("12 34 45 56 67")),
    ("cov_K2+K14", E("12 34 35 36 37")),
    ("cov_K2+spider", E("12 34 45 56 47")),
    # non-covering (block 7 free)
    ("unc_P6", E("12 23 34 45 56")),
    ("unc_C6", E("12 23 34 45 56 16")),
    ("unc_K3+K3", E("12 13 23 45 46 56")),
    ("unc_K4+K2", E("12 13 14 23 24 34 56")),
    ("unc_K33", E("14 15 16 24 25 26 34 35 36")),
    ("unc_3K2", E("12 34 56")),
    ("unc_K4", E("12 13 14 23 24 34")),
]

if __name__ == "__main__":
    tlimit = float(sys.argv[1]) if len(sys.argv) > 1 else 300
    par = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    def job(c):
        name, P = c
        r = run(P, None, tlimit)
        rec = {"name": name, "pairs": P, "tlimit": tlimit, **r}
        with open(OUT, "a") as f: f.write(json.dumps(rec) + "\n")
        print(name, len(P), r["result"], r.get("solve_s"), flush=True)
    with ThreadPoolExecutor(max_workers=par) as ex:
        list(ex.map(job, CONFIGS))
