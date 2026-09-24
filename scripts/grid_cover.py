"""E5: test hypothesis H-COVER (sib pairs covering all 7 blocks => fast UNSAT; leaving a block uncovered => hard).
Usage: python grid_cover.py <tlimit> <parallel>
"""
import json, os, sys, itertools
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grid_profile import run  # noqa

OUT = os.path.join(HERE, "..", "data", "grid_cover.jsonl")
K6 = list(itertools.combinations(range(1, 7), 2))
CONFIGS = [
    ("cover4_K2K2P3", [(1, 2), (3, 4), (5, 6), (6, 7)]),
    ("cover6_star7", [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7)]),
    ("K6_on_1to6_uncover7", K6),
    ("cover5_P3P3K2", [(1, 2), (2, 3), (4, 5), (5, 6), (6, 7)][:0] or [(1, 2), (2, 3), (4, 5), (5, 6), (3, 7)]),
    ("K5_on_1to5_plus_67", list(itertools.combinations(range(1, 6), 2)) + [(6, 7)]),
    ("K5_on_1to5_uncover67", list(itertools.combinations(range(1, 6), 2))),
]

if __name__ == "__main__":
    tlimit = float(sys.argv[1]) if len(sys.argv) > 1 else 300
    par = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    def job(c):
        name, P = c
        r = run(P, None, tlimit)
        rec = {"name": name, "pairs": P, "tlimit": tlimit, **r}
        with open(OUT, "a") as f: f.write(json.dumps(rec) + "\n")
        print(name, len(P), r["result"], r.get("solve_s"), flush=True)
    with ThreadPoolExecutor(max_workers=par) as ex:
        list(ex.map(job, CONFIGS))
