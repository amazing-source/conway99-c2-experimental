"""Survivants chi-SAT maximaux (parmi les 39 de data/survivors39.txt) pour la relation « sous-graphe »."""
import sys
import networkx as nx
from networkx.algorithms import isomorphism as iso
sys.path.insert(0, "scripts")
from rs_experiments import parse, edges_str
L = [l.split("aretes")[0].strip() for l in open("data/survivors39.txt", encoding="utf-8")]
G = [(s, nx.Graph(parse(s)) if s != "-" else nx.Graph()) for s in L]
for g in G:
    g[1].add_nodes_from(range(1, 8))
def sub(h, g):   # g sous-graphe de h
    return iso.GraphMatcher(h, g).subgraph_is_monomorphic()
mx = [s for s, g in G if not any(t != s and h.number_of_edges() > g.number_of_edges() and sub(h, g) for t, h in G)]
print(len(mx)); print("\n".join(mx))
