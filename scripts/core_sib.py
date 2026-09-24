"""Microscope: UNSAT cores of the exact orbit model under forced sib pairs.

Each model constraint gets a selector literal (clauses become (-sel OR clause)); product-gate definitions stay hard.
Constraint groups: R[U], D[U], I[U,c], PS[U,V] (same-side (P)), PC[U,V] (cross (P)).
We solve under assumptions = all selectors (+ forced sib units as hard clauses), take the core, then trim it by
re-solving under the core only (a few rounds), and report which blocks / orbits / constraint types the core uses.
Usage: python core_sib.py <pairs like 12,13,14> <rounds>
"""
import itertools, json, os, sys, time
from collections import Counter
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver

HERE = os.path.dirname(os.path.abspath(__file__))
M = 7


def build_sel(m):
    k = 2 * m
    outer = [(i, j, e) for i in range(1, m + 1) for j in range(i + 1, m + 1) for e in (0, 1)]
    N = len(outer)
    rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
    trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
    pool = IDPool(); hard = []; soft = {}   # soft: selector -> (name, clauses)
    A, B = {}, {}
    for U in range(N):
        for V in range(U + 1, N):
            A[U, V] = A[V, U] = pool.id(("a", U, V)); B[U, V] = B[V, U] = pool.id(("b", U, V))
    def prod(x, y):
        key = ("p", min(x, y), max(x, y))
        new = key not in pool.obj2id
        p = pool.id(key)
        if new: hard.extend([[-p, x], [-p, y], [p, -x, -y]])
        return p
    sels = {}
    def eq(name, lits, kk):
        s = pool.id(("sel",) + name); sels[s] = name
        if kk < 0 or kk > len(lits): cls = [[]]
        else: cls = CardEnc.equals(lits=lits, bound=kk, vpool=pool, encoding=EncType.seqcounter).clauses
        hard.extend([[-s] + c for c in cls])
    inner = [(i, s) for i in range(1, m + 1) for s in (0, 1)]
    for U in range(N):
        others = [V for V in range(N) if V != U]
        eq(("R", U), [A[U, V] for V in others] + [B[U, V] for V in others], k - 2)
        eq(("D", U), [prod(A[U, V], B[U, V]) for V in others], 1)
        for c in inner:
            partner = (c[0], 1 - c[1]); lits = []
            for V in others:
                if c in rep[V]: lits.append(A[U, V])
                if c in trep[V]: lits.append(B[U, V])
            eq(("I", U, c), lits, 1 if (c in rep[U] or partner in rep[U]) else 2)
    for U in range(N):
        for V in range(U + 1, N):
            Ws = [W for W in range(N) if W != U and W != V]
            same = [prod(A[U, W], A[V, W]) for W in Ws] + [prod(B[U, W], B[V, W]) for W in Ws]
            cross = [prod(A[U, W], B[V, W]) for W in Ws] + [prod(B[U, W], A[V, W]) for W in Ws]
            eq(("PS", U, V), same + [A[U, V]], 2 - len(rep[U] & rep[V]))
            eq(("PC", U, V), cross + [B[U, V]], 2 - len(rep[U] & trep[V]))
    return hard, sels, pool, outer, A, B


def describe(core, sels, outer):
    names = [sels[s] for s in core]
    types = Counter(n[0] for n in names)
    orbs = Counter()
    blocks = Counter()
    for n in names:
        us = [x for x in n[1:] if isinstance(x, int)]
        for U in us:
            orbs[outer[U]] += 1
            i, j, e = outer[U]; blocks[i] += 1; blocks[j] += 1
    return types, orbs, blocks, names


if __name__ == "__main__":
    pairs = [tuple(int(c) for c in p) for p in sys.argv[1].split(",")]
    rounds = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    t0 = time.time()
    hard, sels, pool, outer, A, B = build_sel(M)
    for (i, j) in pairs:
        U = outer.index((i, j, 0)); V = outer.index((i, j, 1))
        hard.append([A[U, V]]); hard.append([B[U, V]])
    print("built: vars %d clauses %d selectors %d (%.1fs)" % (pool.top, len(hard), len(sels), time.time() - t0), flush=True)
    assum = sorted(sels)
    log = []
    with Solver(name="cadical195", bootstrap_with=hard) as s:
        for r in range(rounds):
            t1 = time.time()
            res = s.solve(assumptions=assum)
            if res:
                print("SAT under assumptions (round %d)" % r); break
            core = sorted(set(s.get_core() or []))
            types, orbs, blocks, names = describe(core, sels, outer)
            print("round %d: core %d constraints (%.1fs)  types %s" % (r, len(core), time.time() - t1, dict(types)), flush=True)
            print("   blocks touched (multiplicity):", dict(sorted(blocks.items())), flush=True)
            log.append({"round": r, "core": [list(map(str, sels[c])) for c in core], "types": dict(types)})
            if len(core) == len(assum): break
            assum = core
    out = os.path.join(HERE, "..", "data", "core_%s.json" % "_".join("%d%d" % p for p in pairs))
    json.dump({"pairs": pairs, "rounds": log}, open(out, "w"))
    print("saved", out)
