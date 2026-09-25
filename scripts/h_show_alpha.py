import itertools, sys
sys.path.insert(0, "scripts")
exec(open("scripts/h_linked_exclusion.py", encoding="utf-8").read().split("def run():")[0])
for arcs in orientations():
    In = {c: sorted(a for (a, b) in arcs if b == c) for c in range(N)}
    modes = ['A'] * N
    if killed(In, modes) is None:
        print("all-alpha survivor: In =", In, " arcs:", sorted(arcs))
