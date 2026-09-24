"""Core minimisation with glucose4 (honours conf_budget) on the selector formulation.
Phase 1: solve under the saved core (data/core_<tag>.json) to warm up; Phase 2: deletion-based MUS with a conflict budget per call
(calls that exhaust the budget are 'undecided' and the group is kept).
Usage: python core_glucose.py <pairs e.g. 12,34,56,67> <conf_budget>
"""
import json, os, sys, time
from pysat.solvers import Solver
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from core_sib import build_sel, describe  # noqa
M = 7

def parse(nm):
    out = []
    for x in nm:
        if x.lstrip("-").isdigit(): out.append(int(x))
        elif x.startswith("("): out.append(eval(x))
        else: out.append(x)
    return tuple(out)

def main():
    pairs = [tuple(int(c) for c in p) for p in sys.argv[1].split(",")]
    budget = int(sys.argv[2])
    tag = "_".join("%d%d" % p for p in pairs)
    hard, sels, pool, outer, A, B = build_sel(M)
    for (i, j) in pairs:
        U = outer.index((i, j, 0)); V = outer.index((i, j, 1))
        hard.append([A[U, V]]); hard.append([B[U, V]])
    name2sel = {v: k for k, v in sels.items()}
    core = sorted(name2sel[parse(nm)] for nm in json.load(open(os.path.join(HERE, "..", "data", "core_%s.json" % tag)))["rounds"][-1]["core"])
    t0 = time.time()
    with Solver(name="glucose4", bootstrap_with=hard) as s:
        r = s.solve(assumptions=core)
        print("warm-up solve under core (%d): %s in %.1fs" % (len(core), r, time.time() - t0), flush=True)
        if r is not False: return
        core = sorted(set(s.get_core()))
        print("core after warm-up:", len(core), flush=True)
        i = 0; undecided = 0
        while i < len(core):
            trial = core[:i] + core[i + 1:]
            s.conf_budget(budget)
            res = s.solve_limited(assumptions=trial)
            if res is False:
                keep = set(s.get_core() or trial)
                core = [c for c in core if c in keep]
                print("  drop -> %d (%.0fs)" % (len(core), time.time() - t0), flush=True)
            else:
                if res is None: undecided += 1
                i += 1
        types, orbs, blocks, names = describe(core, sels, outer)
        print("final core %d (undecided kept %d) types %s blocks %s (%.0fs)" % (len(core), undecided, dict(types), dict(sorted(blocks.items())), time.time() - t0), flush=True)
        json.dump({"pairs": pairs, "core": [list(map(str, sels[c])) for c in core], "undecided_kept": undecided},
                  open(os.path.join(HERE, "..", "data", "mincore_%s.json" % tag), "w"))

if __name__ == "__main__":
    main()
