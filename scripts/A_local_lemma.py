"""A-block local system (note 38).  A = block with d_A = 6 (all six pairs anchored at A), Sigma = empty, one-block squares.
Unknowns: for each of the 30 non-A orbits Z (15 pairs {c,d} of the six other blocks, 2 orbits each) the vector
a_Z(x) = phi_Z({A,x}) in {0,1,2}, x in the six blocks.  Proved constraints:
  (S)  sum_x a_Z(x) = 4                         (mu = 2 at (A,+-): A is a far block of every non-A orbit, k != A)
  (P)  a_Z(c) * a_Z(d) = 0 for Z of {c,d}       (at its pivot c, F1 gives phi({A,c}) = 2[k = A] = 0)
  (F)  sum_{Z containing x} a_Z(x) = 4          (the two A-orbits free at x have 2 free-cycle neighbours each, none sister/A)
  (N)  #{Z : a_Z(x) = 2} <= 1                   (19.1: the two A-sisters at x have <= 1 common neighbour)
  (B)  balance at A: for every cycle B of the D-graph D_A:  sum_{x in B} a_Z(x) = |B| - |{c,d} & B|
  (Q)  second order (P2 on pairs {A,x},{A,y}, PPE): sum_Z a_Z a_Z^T = 12 I + 12 J - 2 D_A   (A-orbits contribute constants)
       (and sum_Z a_Z = 20 * 1, the column sums)
D_A up to S6: 6-cycle, 4-cycle + double edge, two triangles, three double edges.  ILP feasibility per type (CP-SAT)."""
import itertools, sys, time
from ortools.sat.python import cp_model
X = list(range(6))
def types():
    T = {}
    T["6-cycle"] = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]
    T["4-cycle+2"] = [(0,1),(1,2),(2,3),(3,0),(4,5),(4,5)]
    T["3+3"] = [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)]
    T["2+2+2"] = [(0,1),(0,1),(2,3),(2,3),(4,5),(4,5)]
    return T
def cycles_of(edges):
    import networkx as nx
    G = nx.MultiGraph(); G.add_nodes_from(X); G.add_edges_from(edges)
    return [set(c) for c in nx.connected_components(G)]
def solve(edges, secs, useQ=True, useB=True):
    D = [[0] * 6 for _ in X]
    for u, v in edges: D[u][v] += 1; D[v][u] += 1
    m = cp_model.CpModel()
    orbs = [(c, d, s) for c, d in itertools.combinations(X, 2) for s in (0, 1)]
    a = {(z, x): m.NewIntVar(0, 2, "") for z in orbs for x in X}
    for z in orbs:
        c, d, s = z
        m.Add(sum(a[z, x] for x in X) == 4)
        bc = m.NewBoolVar(""); m.Add(a[z, c] == 0).OnlyEnforceIf(bc); m.Add(a[z, d] == 0).OnlyEnforceIf(bc.Not())
    for x in X:
        m.Add(sum(a[z, x] for z in orbs if x in z[:2]) == 4)
        two = []
        for z in orbs:
            if x in z[:2]:
                b2 = m.NewBoolVar(""); m.Add(a[z, x] == 2).OnlyEnforceIf(b2); m.Add(a[z, x] != 2).OnlyEnforceIf(b2.Not()); two.append(b2)
        m.Add(sum(two) <= 1)
    if useB:
        for B in cycles_of(edges):
            for z in orbs:
                m.Add(sum(a[z, x] for x in B) == len(B) - len({z[0], z[1]} & B))
    for x in X: m.Add(sum(a[z, x] for z in orbs) == 20)
    if useQ:
        for x in X:
            for y in X:
                if y < x: continue
                prods = []
                for z in orbs:
                    p = m.NewIntVar(0, 4, ""); m.AddMultiplicationEquality(p, [a[z, x], a[z, y]]); prods.append(p)
                m.Add(sum(prods) == (24 if x == y else 12 - 2 * D[x][y]))
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = secs; s.parameters.num_workers = 4
    st = s.Solve(m)
    return s.StatusName(st)
if __name__ == "__main__":
    for name, E in types().items():
        t0 = time.time()
        r = solve(E, float(sys.argv[1]) if len(sys.argv) > 1 else 120)
        print("%-10s full A-local system: %s (%.0fs)" % (name, r, time.time() - t0)); sys.stdout.flush()
