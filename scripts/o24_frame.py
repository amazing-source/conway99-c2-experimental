"""Finish line (C), envelope O24 (the odd Leech lattice, rootless; note 46 s.8): exact search for the physical frame (F).
O24 = { a/sqrt8 : a_i = m (mod 2), {i : a_i = m + 2 (mod 4)} in Golay, sum(a) = 0 (mod 8) }, following Sol (0836, rootless case).
- 3-shell: the 4096 sign vectors s/sqrt8 whose negative support is a codeword.
- Norm-4 vectors: signed octads 2 e 1_O / sqrt8 (an even number of minus signs), and (+-4, +-4, 0^22)/sqrt8.
Frame (C1's exact form): 7 h_c of norm 4, pairwise orthogonal; 42 u_o in the 3-shell with (h_c, u_o) = -C_co; T = -Gram(u) off the
diagonal, in {0, +-1}; 3 h_c + sum_o C_co u_o = 0; T^2 + T = 12 I - C^T C and C T = 0; 2 normals y of norm 7 orthogonal to everything.
Diagonal of (F): mult(i) = 1 on the 8 positions of the +-3 of the normals, 3 elsewhere, so the h_c are 7 signed octads.
Step 1 (this file, 'step1'): the 7-octad sets with point multiplicities 1^8 3^16, with the first octad fixed (M24 is transitive
on octads).  Usage: python o24_frame.py step1"""
import sys, itertools, json, time
from collections import Counter


def golay():
    """extended binary Golay code [24,12,8]: quadratic-residue code of length 23 (generator polynomial below) + parity bit"""
    g = [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1]            # x^11 + x^10 + x^6 + x^5 + x^4 + x^2 + 1, low degree first
    rows = []
    for s in range(12):
        v = [0] * 23
        for k, c in enumerate(g):
            if c: v[(k + s) % 23] = 1
        rows.append(v + [sum(v) % 2])
    words = set()
    for mask in range(1 << 12):
        w = [0] * 24
        for r in range(12):
            if mask >> r & 1: w = [a ^ b for a, b in zip(w, rows[r])]
        words.add(tuple(w))
    return sorted(words)


def check_golay(C):
    wt = Counter(sum(w) for w in C)
    assert len(C) == 4096 and wt == Counter({0: 1, 8: 759, 12: 2576, 16: 759, 24: 1}), wt
    return True


def step1(C):
    octads = [frozenset(i for i in range(24) if w[i]) for w in C if sum(w) == 8]
    O1 = octads[0]; rest = [o for o in octads if o != O1 and len(o & O1) in (0, 2, 4)]
    sols = []; t0 = time.time()

    def rec(chosen, mult, start):
        if len(chosen) == 7:
            if all(m in (1, 3) for m in mult): sols.append(list(chosen))
            return
        left = 7 - len(chosen)
        # every point must end with multiplicity >= 1, so the uncovered points need enough octads left
        if sum(1 for m in mult if m == 0) > 8 * left: return
        for k in range(start, len(rest)):
            o = rest[k]
            if any(len(o & p) not in (0, 2, 4) for p in chosen): continue
            if any(mult[i] >= 3 for i in o): continue
            for i in o: mult[i] += 1
            chosen.append(o); rec(chosen, mult, k + 1); chosen.pop()
            for i in o: mult[i] -= 1

    mult = [0] * 24
    for i in O1: mult[i] = 1
    rec([O1], mult, 0)
    return octads, sols, time.time() - t0


if __name__ == "__main__":
    C = golay(); check_golay(C); print("Golay code OK: 4096 words, weights 1/759/2576/759/1", flush=True)
    if sys.argv[1:] == ["step1"]:
        octads, sols, dt = step1(C)
        inv = Counter(tuple(sorted(Counter(len(a & b) for a, b in itertools.combinations(s, 2)).items())) for s in sols)
        print("step 1: %d seven-octad sets with multiplicities 1^8 3^16 containing the fixed octad (%.0fs)" % (len(sols), dt))
        print("intersection-size profiles (size: number of pairs):", dict(inv))
        json.dump([[sorted(o) for o in s] for s in sols], open("logs/o24_step1.json", "w"))
