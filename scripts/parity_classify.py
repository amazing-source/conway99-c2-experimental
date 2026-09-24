"""Classification des 1044 graphes Sigma par le seul systeme de parite independant de chi (L1)+(L2)+(L3) (notes/19 §6 bis).
Algebre lineaire exacte sur F2 (pas de SAT).  Sortie : graphes minimaux incoherents (atomes de parite), et bilan sur les survivants.
"""
import sys
import networkx as nx
from networkx.algorithms import isomorphism as iso
sys.path.insert(0, "scripts")
from parity_L12 import system, incons, min_cert
from rs_experiments import edges_str

atlas = [nx.relabel_nodes(g, {i: i + 1 for i in range(7)}) for g in nx.graph_atlas_g() if g.number_of_nodes() == 7]
res = {}
for gi, g in enumerate(atlas):
    E = sorted(tuple(sorted(e)) for e in g.edges())
    if not E:
        res[gi] = False; continue
    eqs, n = system(E)
    res[gi] = incons(eqs, n)
bad = [gi for gi in res if res[gi]]
print("graphes incoherents par parite seule :", len(bad), "sur", len(atlas))
def sub(h, g):
    return iso.GraphMatcher(h, g).subgraph_is_monomorphic()
mins = []
for gi in sorted(bad, key=lambda i: atlas[i].number_of_edges()):
    g = atlas[gi]
    gg = nx.Graph(list(g.edges()))
    if not any(sub(gg, nx.Graph(list(atlas[m].edges()))) for m in mins):
        mins.append(gi)
print("atomes de parite (minimaux) :")
for m in mins:
    E = sorted(tuple(sorted(e)) for e in atlas[m].edges())
    eqs, n = system(E)
    print("   %-24s  certificat : %s" % (edges_str(E), " ".join(e[0] for e in min_cert(eqs, n))))
# survivants
surv = [l.split("aretes")[0].strip() for l in open("data/survivors39.txt", encoding="utf-8")]
from rs_experiments import parse
k = 0
for s in surv:
    E = parse(s) if s != "-" else []
    if not E: continue
    eqs, n = system(E)
    if incons(eqs, n): k += 1
print("survivants (39) tues par la parite seule :", k)
