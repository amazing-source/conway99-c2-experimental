"""Exact necessary-condition filters for the structured Conway-99 Route-(C) frame.

Scope: these filters require the full D7-cell/star structure, not merely seven
orthogonal admissible h vectors.  They may reject solutions of the bare h-stage.
All inputs are exact integer inner products, not rounded floating-point data.
This module does not certify shell enumeration, orbit completeness, or a lattice.

CLI:
  python astra_root_star_filters.py --self-test
  python astra_root_star_filters.py --input cache.json

JSON schema for --input:
  {
    "root_y_sq": [Y(alpha) for one representative of each old root line],
    "h_root_ip": [[(h,alpha) for alpha in roots] for h in candidates],
    "selected": [optional candidate indices of a partial orthogonal h tuple]
  }
The CLI reports singleton deletions and checks the supplied prefix.  It does
not search for a frame.  Roots are OLD roots of U, not shadow roots.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations, product
import json
from pathlib import Path
from typing import Iterable, Sequence


def _int(x: object) -> int:
    if isinstance(x, bool) or not isinstance(x, int):
        raise TypeError("Exact Python integers are required")
    return x


@dataclass(frozen=True)
class Signature:
    ones: int
    twos: int


@dataclass(frozen=True)
class RootState:
    depth: int = 0
    c1: int = 0
    c2: int = 0
    c3: int = 0
    c4: int = 0
    heavy: int = 0

    @property
    def odd_roots(self) -> int:
        return self.c1 | self.c3

    @property
    def touched(self) -> int:
        return self.c1 | self.c2 | self.c3 | self.c4 | self.heavy


class RootFootprintFilter:
    """Bitset implementation; one bit per old root line.

    A full root footprint is: zero; two +/-1 entries; four +/-1 entries;
    or one +/-2 entry.  The latter two require Y(alpha)<=4.
    For Y=5 the only possible footprints are zero or two +/-1 entries.
    """
    def __init__(self, root_y_sq: Sequence[int]):
        self.y = tuple(_int(v) for v in root_y_sq)
        if any(v not in (0, 1, 2, 4, 5) for v in self.y):
            raise ValueError("Apply the original root Y<=6 filter first; expected Y in {0,1,2,4,5}")
        self.nroots = len(self.y)
        self.all_roots = (1 << self.nroots) - 1
        self.y5 = sum(1 << i for i, v in enumerate(self.y) if v == 5)

    def signature(self, root_ip: Sequence[int]) -> Signature:
        if len(root_ip) != self.nroots:
            raise ValueError("Incorrect root inner-product row length")
        one = two = 0
        for i, value in enumerate(root_ip):
            a = abs(_int(value))
            if a > 2:
                raise ValueError("A norm-4 h and a norm-2 root must have |inner product|<=2")
            if a == 1:
                one |= 1 << i
            elif a == 2:
                two |= 1 << i
        return Signature(one, two)

    def advance(self, state: RootState, sig: Signature) -> RootState | None:
        """None is a proven rejection under the module's structured-frame hypotheses.

        Orthogonality, shadow coverage, and all other search conditions remain
        the caller's responsibility.  The state must have been produced here.
        """
        if not 0 <= state.depth < 7:
            raise ValueError("Can append only to a prefix of length 0 through 6")
        if (sig.ones | sig.twos) & ~self.all_roots or sig.ones & sig.twos:
            raise ValueError("Invalid signature bit masks")
        if sig.twos & (self.y5 | state.touched):
            return None
        if sig.ones & state.heavy:
            return None
        if sig.ones & state.c4:
            return None
        m = sig.ones
        old_light = state.c1 | state.c2 | state.c3 | state.c4
        c4 = (state.c4 & ~m) | (state.c3 & m)
        c3 = (state.c3 & ~m) | (state.c2 & m)
        c2 = (state.c2 & ~m) | (state.c1 & m)
        c1 = (state.c1 & ~m) | (m & ~old_light)
        if (c3 | c4) & self.y5:
            return None
        nxt = RootState(state.depth + 1, c1, c2, c3, c4, state.heavy | sig.twos)
        if nxt.depth == 7 and nxt.odd_roots:
            return None
        return nxt

    def availability_obstruction(self, state: RootState, candidates: Iterable[Signature]) -> bool:
        """True if an odd current root has no possible future +/-1 touch.

        The supplied candidate list must contain every possible next/future h
        in the current search domain.  An incomplete list is not a certificate.
        This deliberately ignores joint feasibility, and is a relaxation.
        """
        if not state.odd_roots:
            return False
        available = 0
        for sig in candidates:
            available |= sig.ones
        return bool(state.odd_roots & ~available)


def static_root_compatible(a: Signature, b: Signature) -> bool:
    """An additional compatibility condition, independent of y1,y2.

    This does NOT test Euclidean orthogonality.
    """
    return not ((a.twos & (b.ones | b.twos)) or (b.twos & (a.ones | a.twos)))


def star_energy_lower_bound(a: Sequence[int]) -> int:
    """Necessary lower bound on 7||x||^2-Y(x) from a partial list (x,h_i).

    Uses integer star conjugates and the l1 bound.  Unknown h coefficients
    are dropped, never set to zero as an assumption.
    """
    aa = sorted((abs(_int(v)) for v in a), reverse=True)
    if len(aa) > 7:
        raise ValueError("At most seven selected h vectors")
    squares = sum(v * v for v in aa)
    best = 0
    total = 0
    for t, value in enumerate(aa, 1):
        total += value
        best = max(best, 3 * total - t * (t - 1) // 2)
    best = max(best, (3 * sum(aa) + 1) // 2)
    return squares + best


def integer_star_slack(a: Sequence[int], budget: int, lam: Sequence[int]) -> int:
    """Exact slack for an integer-star dual witness.

    budget=7||x||^2-(x,y1)^2-(x,y2)^2.
    Extend lam by zeros at all unchosen h positions.
    Negative slack certifies impossibility of the node.
    """
    a = tuple(_int(v) for v in a)
    lam = tuple(_int(v) for v in lam)
    budget = _int(budget)
    if len(a) != len(lam) or len(a) > 7:
        raise ValueError("Matching a, lam of length at most seven required")
    t = sum(v & 1 for v in lam)
    penalty = 3 * sum(v * v for v in lam) - t * (7 - t) // 2
    return budget - sum(v * v for v in a) - 3 * sum(v * w for v, w in zip(a, lam)) + penalty


def integer_star_candidate_allowed(
    x_u: int, h_u: Sequence[int], lam: Sequence[int], slack: int
) -> bool:
    """Necessary condition for a norm-3 candidate u actually to enter the frame.

    x_u=(x,u); h_u=((h_i,u)); lam and slack are from integer_star_slack.
    Removing an impossible u is sound; nonemptiness is not feasibility.
    """
    if len(h_u) != len(lam):
        raise ValueError("Mismatched h_u and lam")
    b = _int(x_u)
    c = sum(_int(v) * _int(w) for v, w in zip(h_u, lam))
    delta = b * b - c * b + c * c // 4
    return slack >= 0 and delta <= slack


def enforce_cell_arc_consistency(domains: Sequence[int], compatibility: Sequence[int]) -> list[int] | None:
    """Safe pairwise support closure for forced Same/Opp cells.

    Each domain is a bitset of possible norm-3 vector LINES for one cell.
    compatibility[u] contains distinct vector lines compatible with u:
      |(u,v)|<=1, disjoint new-root hit sets, and any other proved conditions.
    It should be symmetric and have zero diagonal.  One vector is required in
    every cell.  This routine only enforces pairwise supports, not a clique.
    """
    n = len(compatibility)
    universe = (1 << n) - 1
    comp = tuple(_int(v) for v in compatibility)
    for i, mask in enumerate(comp):
        if mask < 0 or mask & ~universe or mask & (1 << i):
            raise ValueError("Invalid compatibility mask or nonzero diagonal")
        todo = mask
        while todo:
            bit = todo & -todo
            j = bit.bit_length() - 1
            if not (comp[j] & (1 << i)):
                raise ValueError("Compatibility must be symmetric")
            todo ^= bit
    ds = [_int(d) for d in domains]
    if any(d < 0 or d & ~universe for d in ds):
        raise ValueError("Invalid domain")
    if any(not d for d in ds):
        return None
    changed = True
    while changed:
        changed = False
        for i, domain in enumerate(ds):
            keep = 0
            todo = domain
            while todo:
                bit = todo & -todo
                u = bit.bit_length() - 1
                if all(i == j or comp[u] & other for j, other in enumerate(ds)):
                    keep |= bit
                todo ^= bit
            if not keep:
                return None
            if keep != domain:
                ds[i] = keep
                changed = True
    return ds


def self_test() -> dict[str, object]:
    # This verifies finite arithmetic and code, not existence of a full frame.
    C = []
    names = []
    for i, j in combinations(range(7), 2):
        for sign in (1, -1):
            col = [0] * 7
            col[i], col[j] = 1, sign
            C.append(tuple(col))
            names.append((i, j, sign))
    scalar_checks = 0
    for c in range(-12, 13):
        for b in range(-12, 13):
            assert b * b - c * b + c * c // 4 >= 0
            scalar_checks += 1
    lambda_checks = 0
    for lam in product((-1, 0, 1), repeat=7):
        lhs = sum((sum(x * y for x, y in zip(lam, col)) ** 2) // 4 for col in C)
        t = sum(v & 1 for v in lam)
        rhs = 3 * sum(v * v for v in lam) - t * (7 - t) // 2
        assert lhs == rhs
        lambda_checks += 1
    profile_checks = 0
    admitted_profiles = {}
    for a in product((-2, -1, 0, 1, 2), repeat=7):
        E = sum(v * v for v in a)
        if E > 8 or sum(a) % 2:
            continue
        n1 = sum(abs(v) == 1 for v in a)
        n2 = sum(abs(v) == 2 for v in a)
        bound = star_energy_lower_bound(a)
        for Y in (0, 1, 2, 4, 5):
            by_bound = bound <= 14 - Y
            by_theorem = (n2 == 0 and n1 in (0, 2)) or (Y <= 4 and ((n2 == 0 and n1 == 4) or (n2 == 1 and n1 == 0)))
            assert by_bound == by_theorem, (a, Y, bound)
            profile_checks += 1
            if by_theorem:
                admitted_profiles.setdefault(str(Y), set()).add((n1, n2))
    # Explicit INTEGER STAR positive controls, not full lattice-frame controls.
    def star_control(a, chosen):
        b = [int(name in chosen) for name in names]
        image = [sum(col[i] * value for col, value in zip(C, b)) for i in range(7)]
        assert image == [3 * v for v in a]
        energy = sum(v * v for v in a) + sum(v * v for v in b)
        assert star_energy_lower_bound(a) == energy
        return energy
    controls = {
        "one_2": star_control((2, 0, 0, 0, 0, 0, 0), {(0,j,s) for j in (1,2,3) for s in (1,-1)}),
        "two_1": star_control((1, 1, 0, 0, 0, 0, 0), {(0,1,1),(0,2,1),(1,2,-1),(0,3,1),(1,3,-1)}),
        "four_1": star_control((1, 1, 1, 1, 0, 0, 0), {(i,j,1) for i,j in combinations(range(4),2)}),
    }
    # Prefix controls, including a legal heavy and a forbidden heavy/light mix.
    F = RootFootprintFilter([0, 4, 5])
    state = RootState()
    legal_rows = ([2,1,1],[0,1,1],[0,1,0],[0,1,0],[0,0,0],[0,0,0],[0,0,0])
    for row in legal_rows:
        state = F.advance(state, F.signature(row))
        assert state is not None
    G = RootFootprintFilter([0])
    s = G.advance(RootState(), G.signature([2]))
    assert s is not None and G.advance(s, G.signature([1])) is None
    F5 = RootFootprintFilter([5])
    s = RootState()
    for _ in range(2):
        s = F5.advance(s, F5.signature([1]))
        assert s is not None
    assert F5.advance(s, F5.signature([1])) is None
    # Equality-case u filter: a=2, Y=4 -> slack zero.
    slack = integer_star_slack([2], 10, [1])
    assert slack == 0
    assert integer_star_candidate_allowed(1, [1], [1], slack)
    assert integer_star_candidate_allowed(0, [1], [1], slack)
    assert not integer_star_candidate_allowed(-1, [1], [1], slack)
    assert not integer_star_candidate_allowed(1, [0], [1], slack)
    # AC keeps a known compatible triple; independently nonempty cells can die.
    tri = [0b110, 0b101, 0b011]
    assert enforce_cell_arc_consistency([1,2,4], tri) == [1,2,4]
    assert enforce_cell_arc_consistency([1,2], [0,0]) is None
    return {
        "status": "PASS",
        "scalar_conjugate_checks": scalar_checks,
        "D7_penalty_checks": lambda_checks,
        "signed_root_profile_Y_checks": profile_checks,
        "profiles_n1_n2": {k: sorted(v) for k,v in admitted_profiles.items()},
        "integer_star_positive_control_energies": controls,
        "scope": "Arithmetic/code controls only; no cached 078/097 pairs were tested; no lattice exclusion or speedup established.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps(self_test(), indent=2))
    if args.input:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        F = RootFootprintFilter(data["root_y_sq"])
        signatures = [F.signature(row) for row in data["h_root_ip"]]
        singletons = [i for i,sig in enumerate(signatures) if F.advance(RootState(), sig) is None]
        state = RootState()
        killed_at = None
        selected = data.get("selected", [])
        if len(selected) > 7:
            raise ValueError("At most seven selected indices")
        for position, i in enumerate(selected, 1):
            i = _int(i)
            if not 0 <= i < len(signatures):
                raise ValueError("Selected candidate index out of range")
            nxt = F.advance(state, signatures[i])
            if nxt is None:
                killed_at = position
                break
            state = nxt
        print(json.dumps({"singleton_kills": singletons, "prefix_killed_at_depth": killed_at,
                          "prefix_not_rejected": killed_at is None,
                          "warning": "Not rejected does not mean feasible. Orthogonality and other constraints were not checked."}, indent=2))
    if not args.self_test and not args.input:
        parser.error("Specify --self-test and/or --input")


if __name__ == "__main__":
    main()
