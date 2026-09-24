"""E8: exact sib sets.  Force the given sib pairs AND forbid all other sib pairs (n_sib exactly the given set).
If UNSAT fast for a single pair => one grid through x forces another (propagation at x).
Usage: python grid_exact.py "<pairs>" <tlimit>
"""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grid_profile import run  # noqa

if __name__ == "__main__":
    pairs = [(int(x[0]), int(x[1])) for x in sys.argv[1].split()] if sys.argv[1].strip() else []
    tl = float(sys.argv[2])
    r = run(pairs, "nosib_others", tl)
    rec = {"pairs": pairs, "mode": "exact_sib_set", "tlimit": tl, **r}
    with open(os.path.join(HERE, "..", "data", "grid_exact.jsonl"), "a") as f: f.write(json.dumps(rec) + "\n")
    print(json.dumps(rec))
