# Théorème (calcul certifié) : les grilles passant par le point fixe sont rares

## Énoncé
Soit Γ un srg(99,14,1,2) muni d'une involution t (point fixe x). Soit Σ le graphe sur les 7 droites de x dont les arêtes sont les paires de droites
engendrant une grille 3×3 (⇔ arêtes D de type sœur ⇔ « paires sib »). Alors Σ ne contient **aucun** des graphes suivants comme sous-graphe
(non nécessairement induit) :

| Configuration (arêtes forcées) | kissat | conflits | DRAT (drat-trim) | sha256 CNF |
|---|---|---|---|---|
| allsib (K₇, 21 paires) | UNSAT 18 s | 56 755 | VERIFIED | c29eea1c… |
| K2+K2+P3 {12,34,56,67} | UNSAT 24 s | 36 404 | VERIFIED | 7ab7737d… |
| K3+K2+K2 {12,13,23,45,67} | UNSAT 24 s | 45 822 | VERIFIED | 5a19dd87… |
| K2+P5 {12,34,45,56,67} | UNSAT 22 s | 46 621 | VERIFIED | bad48052… |
| K2+araignée {12,34,45,56,47} | UNSAT 22 s | 46 113 | VERIFIED | b288e7b2… |
| P4+P3 {12,23,37,45,56} | UNSAT 43 s | 67 371 | VERIFIED | 53780f60… |
| (en cours) K1,3+P3, K3+K3, K4, C6, K2+K3pendant | | | | |

(Résultats bruts : `data/cert_results.txt` ; journaux `logs/cert_*.kissat.log`, `logs/cert_*.drat.log` ; CNF et empreintes : `data/cnf/`,
`data/cnf/MANIFEST.txt`.)

## Chaîne de confiance
1. Modèle exact (R),(D),(I),(P) ⇔ srg(99,14,1,2) avec involution (dépôt, relu par deux audits ; ÉTABLI).
2. Encodage CNF : base **identique octet pour octet** à `k14_none.cnf` du dépôt (sha256 a59d3e04… recalculé ici), dont le générateur a été validé
   par le contrôle fort `control_bvls.py --cnf` (m = 11, BvLS planté SAT + relèvement, 4/4 bits inversés UNSAT) le 22/09.
3. CNF certifiées = base + clauses unitaires a = b = 1 sur les paires sœurs imposées (sémantique « au moins ces paires »).
4. Invariance : le modèle est invariant par le groupe de relabellisation 2⁶⋊S₇ (vérifié dans le dépôt, `check_symmetry`), qui agit sur les paires
   de blocs comme S₇ ; une configuration UNSAT l'est donc pour toutes ses images par S₇.
5. kissat 4.0.4 (UNSAT, exit 20) + preuve DRAT binaire vérifiée par drat-trim (image `satbox-proof`, drat-trim 2e3b2dc).

## Conséquence (sous réserve des configurations encore en cours) — **PÉRIMÉ** : remplacé par la note 19 (lemme des étoiles, 10 survivants, |Σ| ≤ 4) (revue du 24/09, soir)
Si les 10 configurations minimales sont certifiées, Σ est l'un des **63 graphes** sur 7 sommets qui les évitent (énumération
`scripts/sib_graph_survivors.py`, `logs/sib_graph_survivors_all.log`) ; en particulier **n_sib ≤ 9**. Survivants maximaux : K₁,₁,₄ (9 arêtes),
un graphe à 8 arêtes, quatre à 7 arêtes (dont K₁,₆ + une arête), un à 6 arêtes. (Les tests des survivants maximaux sont en cours.)

## Mécanisme (ce qu'on comprend)
- Théorème G1 : chaque grille est un code parfait (propre à k = 14) ; lemme S1 : partition exacte des 40 racines complémentaires ; connexion D₄ entre
  paires sœurs disjointes (`notes/05_ALLSIB_STRUCTURE.md`).
- Empirique : les contradictions rapides demandent des paires sœurs **disjointes** en nombre suffisant ; les étoiles et petites configurations
  (≤ 3 paires) restent indécises.
- Non compris : la preuve humaine. Noyau UNSAT (non minimal) : 339 contraintes pour K2+K2+P3, 745 pour allsib.
