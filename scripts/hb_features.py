"""Local features of a pair / pair-couple in an H-beta skeleton (note 34), to look for a UNIFORM certificate matrix W."""
import sys
sys.path.insert(0, "scripts")
N = 7
def P(a, b): return frozenset((a % N, b % N))

def skeleton_info(orbits):
    # D-edges at pivot c: orbit (c, x, y) matched to orbit of {c, y}
    info = {}
    for (i, j, k) in orbits:
        info.setdefault(P(i, j), []).append((i, j, k))
    return info

def pair_type(R, orbits):
    a, b = sorted(R)
    if (b - a) % N in (1, N - 1): return 'T'
    piv = {z[0] for z in orbits if P(z[0], z[1]) == R}
    head = piv.pop()
    # role: A (next to P_head = {head-1, head}) or B
    for (i, j, k) in orbits:
        if i == head and P(i, j) == R:
            if k == (head - 1) % N: return 'A'
            if k == (head + 1) % N: return 'B'
    return 'A?'  # both orbits of an A-chord: one has k = head-1, other k = B ; B-chord: k = A or head+1

def role(b, R, orbits):
    """role of block b in pair R: for T {c,c+1}: 'L' if b == c else 'R'; for chords: 'h' (head) or 't' (tail)"""
    a1, a2 = sorted(R)
    if (a2 - a1) % N in (1, N - 1):
        c = a1 if (a2 - a1) % N == 1 else a2
        return 'L' if b == c else 'R'
    piv = {z[0] for z in orbits if P(z[0], z[1]) == R}
    return 'h' if b in piv else 't'

def dadj(R, S, orbits):
    """number of D-edges between orbits of R and orbits of S"""
    return sum(1 for (i, j, k) in orbits if P(i, j) == R and P(i, k) == S)

def feature(R, S, orbits):
    if R == S: return ('diag', pair_type(R, orbits))
    I = R & S
    tR, tS = pair_type(R, orbits), pair_type(S, orbits)
    if I:
        b = next(iter(I))
        f1 = (tR, role(b, R, orbits)); f2 = (tS, role(b, S, orbits))
        lo, hi = sorted([f1, f2])
        return ('share', lo, hi, dadj(R, S, orbits) + dadj(S, R, orbits))
    # disjoint: T-adjacency count between the blocks and chord relations
    tadj = sum(1 for x in R for y in S if (x - y) % N in (1, N - 1))
    lo, hi = sorted([tR, tS])
    return ('disj', lo, hi, tadj)
