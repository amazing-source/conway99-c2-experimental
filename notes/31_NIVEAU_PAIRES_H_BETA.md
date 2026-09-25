# 31 — Le système « niveau paires » mord sur H-β (26/09/2026)

Session principale C2. **Statut :**
- les identités sont DÉRIVÉES à la main et contrôlées sur un vrai graphe, BvLS ;
- les tests sont de **petits tests** (moins de 5 min chacun, règle du 25/09), à réponses définitives seulement ;
- les UNKNOWN ne sont **pas** des résultats et sont signalés comme tels.
- Ce n'est **pas** une preuve de la mort de H-β. C'est une **piste forte, mesurée**.

## 1. Le système au niveau des paires
**Inconnues.** Pour une orbite Z et une paire de blocs R, φ_Z(R) est le nombre de voisins d'un représentant de Z parmi les 4 racines
de R. Les valeurs **proches** sont connues par le squelette et les cycles libres :
- φ_Z(P_Z) = 0 ;
- F1 : φ_Z({i,r}) = 2[r = k] ;
- φ_Z({j,r}) = n_r(Z), lu sur le cycle libre en j.

Les **10 valeurs lointaines** de chaque orbite (paires disjointes de P_Z) sont inconnues, dans {0,1,2}.

**Contraintes** (toutes démontrées) :
- **(L)** Pour t ∉ {i,j}, on a Σ_{R∋t} φ_Z(R) = 4 : μ = 2 en (t,±), et λ en k.
- **(PPE)** Σ_Z φ_Z(R)² = 32. C'est la diagonale de (P2) avec e(R) = 0, soit 16.1 : 4 doubles, dont les 2 partenaires D.
- **(S)** Σ_Z φ_Z(R) = 24.
- **(C)** Couplage : E[R][R′] = E[R′][R], avec E[R][R′] = Σ_{Y⊂R} φ_Y(R′).
- **(P2)** Pour R ≠ R′ : Σ_Z φ_Z(R) φ_Z(R′) = 16 − E[R][R′] − 4[R ∩ R′ ≠ ∅].

Ce sont les λ/μ sommés sur R × R′ (C1, notes/116 ; « structures »). Rederivé ici, **indépendamment de k** hors diagonale. La
diagonale générale est 2k + 4 − e(R).

**Contrôle sur un vrai graphe** (`scripts/p2_control_bvls.py`, `logs/p2_control_bvls.log`) : BvLS srg(243,22,1,2) avec x ↦ −x.
- (L) : 0 violation ;
- (S) : 40 = 2(k − 2) ;
- (C) : 0 asymétrie ;
- (P2) : **0 violation sur 3 025** (diagonale incluse).

**Niveaux.** F1 = (L) + (PPE). F2 = F1 + (S) + (C), le premier ordre complet. P2 = F2 + les identités hors diagonale.
- F2 est **linéaire** dans les indicatrices a = [φ = 1] et b = [φ = 2], puisque φ² = a + 4b. Sa relaxation LP donne donc, quand elle
  est infaisable, un certificat de Farkas **rationnel et vérifiable**, c'est-à-dire un comptage pondéré.

## 2. Résultats (définitifs sauf mention)
Scripts : `hb_pairlevel.py`, `hb_levers.py`, `hb_levers_general.py`, `hb_lp_ppe.py`, `hb_relaxed.py`.

**Contrôles.**
- Sans l'identité (PPE), les cycles symétriques du circulant sont en majorité faisables : 20 sur 22.
- Le modèle aux cycles variables, fixés à un cycle F2-faisable, redonne FAISABLE ; fixés à un cycle F2-infaisable, redonne INFAISABLE.

| cas | F1 | F2 | P2 |
|---|---|---|---|
| circulant (+2,+3), cycles Z₇-symétriques (22 choix) | 3 infaisables (LP) | **21 infaisables sur 22** (LP : 20) | la survivante F2 : UNKNOWN |
| circulant, cycles **aléatoires non symétriques** (33) | UNKNOWN à 8 s | **33 sur 33 infaisables** | — |
| H-β **général** : 6 classes d'orientation × 6 (ordres et cycles aléatoires) | — | **36 sur 36 infaisables** | — |
| H-β général, LP de F2 (30 aléatoires) | — | **30 sur 30 LP-infaisables** (certificats rationnels) | — |
| circulant, **cycles laissés variables** (squelette seul) | — | **faisable** (7 s) | UNKNOWN à 270 s |

**Lecture.**
- En H-β, le premier ordre complet (système local + PPE + couplage) tue **la configuration typique**, par un certificat linéaire.
- Chez « structures », sur le tout-tordu à 1 triangle, ce même modèle était LP-faisable. La différence vient des paires ancrées de H-β
  (sœurs, doubles proches, n_k = 1), qui chargent le budget par paire.
- Des affectations de cycles **rares survivent** au premier ordre, par exemple le cycle symétrique 10 : aucun double proche, un
  seul n_k = 1 par bloc. Elles demandent (P2).

## 3. Budget simple (à la main)
Pour Z = (i,j,k), on a fardbl(Z) ≥ 1 si n_k(Z) = 1 (car Rdbl = Rzero + n_k) ou si Z a un double proche (n_t = 2 : degré ≤ 2 sur 3
arêtes, donc un zéro). Les deux cas sont disjoints par la règle typée.

Avec Σ_Z fardbl = 42 − N_proche, on obtient :

  **#{Z : n_k(Z) = 1} + 2·N_proche ≤ 42.**

Cela tue exactement les 3 cycles symétriques LP-infaisables en F1 (B = 49). Ce budget est trop faible pour les autres : les
certificats F2 sont denses, avec environ 270 lignes pondérées.

## 4. Ce qui reste, et le coût d'une preuve complète
- Une preuve de « H-β impossible » par cette voie demanderait d'énumérer, par squelette (environ 550 classes à symétrie près), les
  affectations de cycles libres. Il faudrait élaguer par LP (certificats rationnels vérifiables), puis traiter les feuilles
  survivantes par F2 entier et (P2).
- C'est un **calcul conséquent**, hors du cadre des petits tests. Il ne se fera pas sans décision explicite de l'utilisateur.
- La voie « à la main » consisterait à trouver la structure des survivants du premier ordre (peu de doubles proches, peu de
  n_k = 1), à la démontrer comme lemme local, puis à tuer ces survivants par (P2).
