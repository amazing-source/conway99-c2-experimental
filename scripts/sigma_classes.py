"""Twisted graphs T (even subgraphs of K7, note 35) compatible with a sister pattern Sigma (T avoids Sigma), up to Aut(Sigma).
Prints one task line per class: '<edges of T or none> <sister edges>', T sorted by decreasing size (fewer orientations first).
Usage: python sigma_classes.py <sister edges, e.g. 01,12,02>"""
import sys, itertools
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
N = 7
S = [tuple(sorted(map(int, e))) for e in sys.argv[1].split(",")]
basis = [{(0, a), (0, b), (a, b)} for a, b in itertools.combinations(range(1, N), 2)]
G0 = nx.Graph(); G0.add_nodes_from(range(N)); G0.add_edges_from(S)
auts = [dict(m) for m in GraphMatcher(G0, G0).isomorphisms_iter()]
classes = set()
for mask in range(1 << 15):
    T = set()
    for t in range(15):
        if mask >> t & 1: T ^= basis[t]
    if T & set(S): continue
    classes.add(min(tuple(sorted(tuple(sorted((g[a], g[b]))) for a, b in T)) for g in auts))
for T in sorted(classes, key=lambda T: (-len(T), T)):
    print(("edges=" + ",".join("%d%d" % e for e in T)) if T else "none", ",".join("%d%d" % e for e in S))
