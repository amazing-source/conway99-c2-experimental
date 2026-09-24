"""Test the maximal surviving sib graphs (from sib_graph_survivors.py) with CaDiCaL ('at least' semantics), hard time limit.
Blocks are relabelled 0..6 -> 1..7.  Usage: python grid_survivors_test.py <tlimit> <parallel>
"""
import json, os, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grid_profile import run  # noqa

OUT = os.path.join(HERE, "..", "data", "grid_survivors.jsonl")
MAXIMAL = {
    "K114": [(0, 4), (0, 5), (1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)],
    "S8": [(0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (1, 4), (2, 5), (4, 5)],
    "S7a": [(0, 3), (0, 4), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4)],
    "S7b": [(0, 2), (0, 3), (0, 5), (1, 2), (1, 5), (2, 4), (4, 5)],
    "S7c": [(1, 2), (1, 5), (2, 3), (2, 4), (3, 6), (4, 5), (5, 6)],
    "K16e": [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (3, 6)],
    "S6": [(0, 1), (1, 5), (1, 6), (3, 6), (4, 5), (5, 6)],
}

if __name__ == "__main__":
    tl = float(sys.argv[1]) if len(sys.argv) > 1 else 900
    par = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    def job(item):
        name, E = item
        P = sorted((min(a, b) + 1, max(a, b) + 1) for a, b in E)
        r = run(P, None, tl)
        rec = {"name": name, "pairs": P, "tlimit": tl, **r}
        with open(OUT, "a") as f: f.write(json.dumps(rec) + "\n")
        print(name, len(P), r["result"], r.get("solve_s"), flush=True)
    with ThreadPoolExecutor(max_workers=par) as ex:
        list(ex.map(job, MAXIMAL.items()))
