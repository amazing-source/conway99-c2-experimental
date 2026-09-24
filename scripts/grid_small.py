"""Experiment E2: which SMALL sets of sib block pairs (grids through x) are already contradictory?  (uncertified CaDiCaL, hard time limit)
Usage: python grid_small.py <tlimit> <parallel>
Configurations are graphs on the 7 blocks (edges = forced sib pairs), up to S7.
"""
import json, os, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grid_profile import run  # noqa

OUT = os.path.join(HERE, "..", "data", "grid_small.jsonl")
CONFIGS = [
    ("K2", [(1, 2)]),
    ("2K2_disjoint", [(1, 2), (3, 4)]),
    ("P3_adjacent", [(1, 2), (1, 3)]),
    ("K3_triangle", [(1, 2), (1, 3), (2, 3)]),
    ("K13_star", [(1, 2), (1, 3), (1, 4)]),
    ("P4_path", [(1, 2), (2, 3), (3, 4)]),
    ("3K2_matching", [(1, 2), (3, 4), (5, 6)]),
    ("P3+K2", [(1, 2), (1, 3), (4, 5)]),
]

if __name__ == "__main__":
    tlimit = float(sys.argv[1]) if len(sys.argv) > 1 else 120
    par = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    def job(c):
        name, P = c
        r = run(P, None, tlimit)
        rec = {"name": name, "pairs": P, "tlimit": tlimit, **r}
        with open(OUT, "a") as f: f.write(json.dumps(rec) + "\n")
        print(name, r["result"], r.get("solve_s"), flush=True)
    with ThreadPoolExecutor(max_workers=par) as ex:
        list(ex.map(job, CONFIGS))
