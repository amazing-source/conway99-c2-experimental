"""Noyau DRAT d'une instance RSF (lignes soeurs + lignes supplementaires) : quels groupes de contraintes sert-il ? (notes/19 §12)
Usage : python core_groups_rsf.py <nom> "<Sigma>" "<paires supplementaires>" [exact]
(le noyau est lu dans data/tmp/<nom>.core.cnf, produit par scripts/core_run.sh)
"""
import sys, collections
sys.path.insert(0, "scripts")
from core_groups import build_labeled_rsf
from rs_experiments import sister_orbits, parse

name, ps, extra = sys.argv[1], sys.argv[2], sys.argv[3]
exact = len(sys.argv) > 4 and sys.argv[4] == "exact"
E = parse(ps)
S = sorted(set(sister_orbits(E) + (sister_orbits(parse(extra)) if extra.strip() else [])))
clauses, labels, outer, A, B = build_labeled_rsf(S, sigma=E, sigma_exact=exact)
where = collections.defaultdict(list)
for t, c in enumerate(clauses):
    where[tuple(sorted(c))].append(t)
core = [tuple(sorted(int(x) for x in l.split()[:-1])) for l in open("data/tmp/%s.core.cnf" % name) if l.strip() and not l.startswith(("c", "p"))]
used = collections.Counter(); unk = 0
for c in core:
    ts = where.get(c)
    if not ts:
        unk += 1; continue
    for lab in set(labels[t] for t in ts):
        used[lab] += 1
sis = set(E)
nm = lambda U: "%d%d%s" % (outer[U][0], outer[U][1], "+-"[outer[U][2]])
tag = lambda U: "S" if outer[U][:2] in sis else "."
kinds = collections.Counter(); rows = collections.Counter(); inner_used = collections.Counter(); pairs = collections.Counter()
for lab, n in used.items():
    kinds[lab[0]] += n
    if lab[0] in ("R", "D", "I"):
        rows[lab[1]] += n
        if lab[0] == "I":
            inner_used[(lab[1], lab[2])] += n
    elif lab[0] in ("Psame", "Pcross"):
        pairs[(lab[1], lab[2], lab[0])] += n
print("%s : noyau de %d clauses (%d non retrouvees) ; |S| = %d lignes" % (name, len(core), unk, len(S)))
print("par type :", dict(kinds))
print("lignes (R/D/I) utilisees : %d/%d :" % (len(rows), len(S)), " ".join(nm(U) + tag(U) for U in sorted(rows)))
print("equations (I) utilisees : %d" % len(inner_used))
byrow = collections.defaultdict(list)
for (U, c) in inner_used:
    byrow[U].append("%s%d" % ("+-"[c[1]], c[0]))
for U in sorted(byrow):
    print("    (I) de %s%s aux sommets : %s" % (nm(U), tag(U), " ".join(sorted(byrow[U]))))
print("equations (P) utilisees : %d" % len(pairs))
cl = collections.Counter()
for (U, V, t) in pairs:
    cl[("S" if tag(U) == "S" else ".") + ("S" if tag(V) == "S" else ".") + " " + t] += 1
print("   par statut :", dict(cl))
for (U, V, t) in sorted(pairs):
    pass
print("   couples :", " ".join("%s-%s%s" % (nm(U), nm(V), "s" if t == "Psame" else "x") for (U, V, t) in sorted(pairs)))
