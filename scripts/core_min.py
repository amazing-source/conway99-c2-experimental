"""Deletion-based minimal unsatisfiable subset (MUS) over constraint groups (selectors from core_sib.build_sel).
Start from the core saved by core_sib.py (data/core_<pairs>.json, last round) or recompute; then for each group g in the current core
try to drop it: solve under (core - g); if UNSAT, adopt the returned (smaller) core.  Incremental CaDiCaL, per-call conflict budget.
Usage: python core_min.py <pairs e.g. 12,34,56,67> <per_call_seconds>
"""
import json, os, sys, time, threading
from collections import Counter
from pysat.solvers import Solver
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from core_sib import build_sel, describe  # noqa

M = 7

def main():
    pairs = [tuple(int(c) for c in p) for p in sys.argv[1].split(",")]
    per_call = float(sys.argv[2]) if len(sys.argv) > 2 else 60
    tag = "_".join("%d%d" % p for p in pairs)
    hard, sels, pool, outer, A, B = build_sel(M)
    for (i, j) in pairs:
        U = outer.index((i, j, 0)); V = outer.index((i, j, 1))
        hard.append([A[U, V]]); hard.append([B[U, V]])
    name2sel = {sels[s]: s for s in sels}
    corefile = os.path.join(HERE, "..", "data", "core_%s.json" % tag)
    with Solver(name="cadical195", bootstrap_with=hard) as s:
        if os.path.exists(corefile):
            last = json.load(open(corefile))["rounds"][-1]["core"]
            core = []
            for nm in last:
                key = tuple(int(x) if x.lstrip("-").isdigit() else (eval(x) if x.startswith("(") else x) for x in nm)
                core.append(name2sel[key])
            print("loaded core of size", len(core), flush=True)
        else:
            assert not s.solve(assumptions=sorted(sels)); core = sorted(set(s.get_core()))
        core = sorted(core)
        i = 0; t0 = time.time(); undecided = []
        while i < len(core):
            g = core[i]
            trial = core[:i] + core[i + 1:]
            timer = threading.Timer(per_call, s.interrupt); timer.start()
            res = s.solve_limited(assumptions=trial, expect_interrupt=True)
            timer.cancel(); s.clear_interrupt()
            if res is False:
                newcore = sorted(set(s.get_core() or trial))
                core = [c for c in core if c in set(newcore)]  # keep order
                # position i now holds the next candidate (g removed or core shrank)
                i = min(i, len(core))
                print("  drop %-28s -> core %d  (%.0fs)" % (str(sels[g]), len(core), time.time() - t0), flush=True)
            else:
                if res is None: undecided.append(g)
                i += 1
                print("  keep %-28s (%s)" % (str(sels[g]), "SAT" if res else "unknown"), flush=True)
        types, orbs, blocks, names = describe(core, sels, outer)
        print("MUS size %d types %s undecided %d" % (len(core), dict(types), len(undecided)), flush=True)
        json.dump({"pairs": pairs, "mus": [list(map(str, sels[c])) for c in core],
                   "undecided": [list(map(str, sels[c])) for c in undecided]},
                  open(os.path.join(HERE, "..", "data", "mus_%s.json" % tag), "w"))

if __name__ == "__main__":
    main()
