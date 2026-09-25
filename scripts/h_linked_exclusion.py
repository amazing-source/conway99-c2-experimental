# Small check (seconds): which Hamiltonian M1 skeletons H survive Lemma 28.4 (linked-pair exclusion)?
# H: blocks Z7, twisted pairs {m,m+1}; chords {m,m+2},{m,m+3} oriented with in-degree 2 at every block (Eulerian).
# At each block c: 'A' (alpha: linked In pair + direct chain square) or ('B', X, Y) (beta: path P_c - {c,X} - {c,Y} - P_{c+1}).
# Squares at c give orbits (i=c, j, k) for arms (j,k) in both directions.
# G_k = (4,2) with L_k = In(k) iff alpha at k; beta -> (6).
# Lemma 28.4: alpha at c with L_c = {a,b}; an orbit (i,j,k) with {i,k} = {a,b}, j not in {a,b};
#             if alpha at k and j not in In(k) -> contradiction.
# Controls: circulant (m -> m+2, m+3), all alpha, must die (note 27, Th. 27.2); all-beta configurations must survive.
import itertools
N = 7
chords = [(m, (m + 2) % N) for m in range(N)] + [(m, (m + 3) % N) for m in range(N)]

def orientations():
    for bits in range(1 << len(chords)):
        indeg = [0] * N; arcs = []
        for t, (u, v) in enumerate(chords):
            a, b = (u, v) if (bits >> t) & 1 else (v, u)   # a -> b
            indeg[b] += 1; arcs.append((a, b))
        if all(d == 2 for d in indeg):
            yield arcs

def squares(c, mode, In):
    lo, hi = (c - 1) % N, (c + 1) % N
    if mode == 'A':
        a, b = sorted(In[c])
        return [(lo, hi), (a, b)]
    _, X, Y = mode
    return [(lo, X), (X, Y), (Y, hi)]

def killed(In, modes):
    orbits = []
    for c in range(N):
        for (x, y) in squares(c, modes[c], In):
            orbits.append((c, x, y)); orbits.append((c, y, x))   # (i, j, k)
    for c in range(N):
        if modes[c] != 'A':
            continue
        L = set(In[c])
        for (i, j, k) in orbits:
            if {i, k} == L and j not in L and modes[k] == 'A' and j not in In[k]:
                return (c, (i, j, k))
    return None

def run():
    total = surv = surv_alpha = 0
    circ = None
    stats = {}
    for arcs in orientations():
        In = {c: [a for (a, b) in arcs if b == c] for c in range(N)}
        per_block = []
        for c in range(N):
            a, b = In[c]
            per_block.append(['A', ('B', a, b), ('B', b, a)])
        is_circ = all(((m, (m + 2) % N) in arcs and (m, (m + 3) % N) in arcs) for m in range(N))
        for modes in itertools.product(*per_block):
            total += 1
            k = killed(In, modes)
            nA = sum(1 for m in modes if m == 'A')
            if is_circ and nA == N:
                circ = k
            if k is None:
                surv += 1
                stats[nA] = stats.get(nA, 0) + 1
    print("orientations x modes:", total, " survivors:", surv)
    print("survivors by number of alpha blocks:", dict(sorted(stats.items())))
    print("control: circulant all-alpha killed by", circ)

run()
