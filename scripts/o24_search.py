"""Finish line (C), envelope O24: frame search, per (y1, y2) class (C1's 141 orbit reps, data/finishC/o24_ypairs.json from
conway99-c1 48eabf2, in C1's coordinates: points 0..22 = F23, 23 = infinity, Golay = span of golay_basis).
- Pipeline per class:
  1. SUPPORTS: 7 octads with point multiplicity 1 on A = T1 u T2 and 3 elsewhere. Each is generated once: the octads covering A,
     each branched on the first uncovered point of A, then a sorted combination of octads disjoint from A.
  2. SIGNS: signed octads h = 2e 1_O / sqrt8 (even number of minus signs, up to the global sign, by the W(B7) symmetry), with
     h . y1 = h . y2 = 0 and pairwise orthogonal.
  3. ENERGY prune: for every norm-3 x, sum_c (h_c, x)^2 + sum_j (y_j, x)^2 <= 21 (diagonal of (F) against x).
  4. u: for each o = e_i +- e_j, S_o = {x norm 3, x ⊥ y1, y2, (h_c, x) = -C_co for all c}; pick one per o with
     3 h_c + sum_o C_co u_o = 0 and u_o != +-u_o'; then check (F) exactly.
Usage: python o24_search.py <class index> [step]      step = supports | signs | full"""
import sys, json, time, itertools
from collections import Counter
LAB = __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
D = json.load(open(LAB + "/data/finishC/o24_ypairs.json"))


def code_words():
    basis = D["golay_basis"]; words = set()
    for mask in range(1 << 12):
        w = 0
        for r in range(12):
            if mask >> r & 1: w ^= basis[r]
        words.add(w)
    wt = Counter(bin(w).count("1") for w in words)
    assert len(words) == 4096 and wt == Counter({0: 1, 8: 759, 12: 2576, 16: 759, 24: 1}), wt
    return words


WORDS = code_words()
OCTADS = sorted(w for w in WORDS if bin(w).count("1") == 8)
PTS = lambda w: [i for i in range(24) if w >> i & 1]


def ys(cl):
    """y_j = a_j / sqrt8 in C1's normal form: a1 = 1 - 4*1_T1; a2 = eps_D (1 - 4*1_T2)"""
    T1, T2, Dset = set(cl["T1"]), set(cl["T2"]), set(cl["D"])
    a1 = [(-3 if i in T1 else 1) for i in range(24)]
    a2 = [(-3 if i in T2 else 1) * (-1 if i in Dset else 1) for i in range(24)]
    for a in (a1, a2):
        n3 = sum(1 << i for i in range(24) if a[i] % 4 == 3)
        assert n3 in WORDS and sum(a) % 8 == 0 and sum(v * v for v in a) == 56, "y not in O24"
    assert sum(p * q for p, q in zip(a1, a2)) == 0, "y1 not orthogonal to y2"
    return a1, a2


def supports(A):
    """all sets of 7 octads with multiplicity 1 on A, 3 off A"""
    Aset = sum(1 << i for i in A); out = []
    disjoint = [o for o in OCTADS if not (o & Aset)]
    def rec(chosen, mult, covered):
        if covered == Aset:
            k = 7 - len(chosen)
            for comb in itertools.combinations(disjoint, k):
                m = list(mult)
                ok = True
                for o in comb:
                    for i in PTS(o):
                        m[i] += 1
                        if m[i] > 3: ok = False; break
                    if not ok: break
                if ok and all(m[i] == (1 if Aset >> i & 1 else 3) for i in range(24)): out.append(tuple(chosen) + comb)
            return
        if len(chosen) >= 7: return
        p = next(i for i in range(24) if Aset >> i & 1 and not covered >> i & 1)
        for o in OCTADS:
            if not (o >> p & 1) or (o & covered): continue          # p uncovered, and no point of A covered twice
            pts = PTS(o)
            if any(mult[i] >= 3 for i in pts): continue
            for i in pts: mult[i] += 1
            rec(chosen + [o], mult, covered | (o & Aset))
            for i in pts: mult[i] -= 1
    rec([], [0] * 24, 0)
    return out


if __name__ == "__main__":
    k = int(sys.argv[1]); step = sys.argv[2] if len(sys.argv) > 2 else "supports"
    cl = D["orbits"][k]; a1, a2 = ys(cl); A = sorted(set(cl["T1"]) | set(cl["T2"]))
    print("class %d: T1 %s T2 %s |D| %d A octad %s" % (k, cl["T1"], cl["T2"], len(cl["D"]), cl["A_is_octad"]), flush=True)
    t0 = time.time(); S = supports(A)
    print("  supports: %d seven-octad sets (%.1fs)" % (len(S), time.time() - t0), flush=True)
