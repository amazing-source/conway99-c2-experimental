"""Classification exhaustive des graphes Sigma (paires soeurs) sur 7 sommets par le systeme chi (notes/18).

Pour chacun des 1044 graphes a 7 sommets (a isomorphisme pres, atlas de networkx) : statut du systeme chi (SAT / UNSAT).
Le systeme est monotone (plus de paires soeurs = plus de contraintes), donc on donne aussi les graphes chi-UNSAT MINIMAUX
(tout sous-graphe a une arete de moins est chi-SAT) et les graphes chi-SAT MAXIMAUX.
Comparaison avec les 53 survivants certifies (notes/06).
"""
import itertools, time, sys
import networkx as nx
sys.path.insert(0, "scripts")
from chi_system import run

def idle():
    try:
        import ctypes; k = ctypes.windll.kernel32
        k.GetCurrentProcess.restype = ctypes.c_void_p; k.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        k.SetPriorityClass(k.GetCurrentProcess(), 0x40)
    except Exception:
        pass

def key(G):
    return nx.weisfeiler_lehman_graph_hash(G, iterations=4)

if __name__ == "__main__":
    idle()
    t0 = time.time()
    atlas = [G for G in nx.graph_atlas_g() if G.number_of_nodes() == 7]
    print("graphes a 7 sommets : %d" % len(atlas), flush=True)
    status = {}
    reps = {}
    for idx, G in enumerate(atlas):
        S = [tuple(sorted((a + 1, b + 1))) for a, b in G.edges()]
        res, dt, nv = run("g%d" % idx, S)
        status[idx] = res
    unsat = [i for i in status if status[i] == "UNSAT"]
    sat = [i for i in status if status[i] == "SAT"]
    print("chi-UNSAT : %d ; chi-SAT : %d ; %.0f s" % (len(unsat), len(sat), time.time() - t0), flush=True)
    # minimalite : un graphe UNSAT est minimal si chaque suppression d'arete donne un graphe SAT
    def iso_index(H):
        for j, G in enumerate(atlas):
            if G.number_of_edges() == H.number_of_edges() and nx.is_isomorphic(G, H):
                return j
        raise ValueError
    minimal = []
    for i in unsat:
        G = atlas[i]
        ok = True
        for e in list(G.edges()):
            H = G.copy(); H.remove_edge(*e)
            if status[iso_index(H)] == "UNSAT":
                ok = False; break
        if ok:
            minimal.append(i)
    print("chi-UNSAT minimaux (%d) :" % len(minimal))
    for i in sorted(minimal, key=lambda i: atlas[i].number_of_edges()):
        G = atlas[i]
        print("   %2d aretes : %s" % (G.number_of_edges(), " ".join("%d%d" % (a + 1, b + 1) for a, b in G.edges())))
    maximal = []
    for i in sat:
        G = atlas[i]
        ok = True
        for a, b in itertools.combinations(range(7), 2):
            if G.has_edge(a, b):
                continue
            H = G.copy(); H.add_edge(a, b)
            if status[iso_index(H)] == "SAT":
                ok = False; break
        if ok:
            maximal.append(i)
    print("chi-SAT maximaux (%d) :" % len(maximal))
    for i in sorted(maximal, key=lambda i: -atlas[i].number_of_edges()):
        G = atlas[i]
        print("   %2d aretes : %s" % (G.number_of_edges(), " ".join("%d%d" % (a + 1, b + 1) for a, b in G.edges())))
    by_m = {}
    for i in sat:
        by_m.setdefault(atlas[i].number_of_edges(), 0); by_m[atlas[i].number_of_edges()] += 1
    print("chi-SAT par nombre d'aretes :", dict(sorted(by_m.items())))
