# Journal du laboratoire expérimental C2

Règles : dépôts `conway99-involution` et `conway99-lab-archive` en LECTURE SEULE (empreintes initiales dans `logs/readonly_snapshot_*_start.txt`).
Tout ce qui est produit ici reste ici. Environnement Python isolé : `.venv` (numpy, sympy, scipy, networkx, python-sat, ortools, galois).
Étiquettes : ÉTABLI · DÉRIVÉ · OBSERVÉ · CONJECTURE · HEURISTIQUE · SPÉCULATION · RÉFUTÉ.

## 2026-09-23

### Phase 0 — isolation et assimilation
- Laboratoire créé ; empreintes SHA-256 des 387 fichiers du dépôt `conway99-involution` et liste (taille, date) des 11 593 fichiers de l'archive enregistrées.
- Lecture complète : README, LAB_INSTRUCTIONS, NOTE, AUDIT, HANDOFF, LAB summary, BRIEFING/DEEP_THOUGHT (phase 2), WHAT_WOULD_HELP,
  RESEARCH_MEMORY, dossier_chercheurs_fr.tex, scripts de phase 2 (s1_structure, spectral_orderly, method-transfer, symbreak, cube_and_conquer).
- Scripts utiles copiés (pas importés depuis le dépôt, pour ne pas y écrire de `__pycache__`) dans `scripts/vendor/`.
- Cartes écrites : `notes/00_CARTE_ETAT_C2.md`, `notes/01_CARTE_METHODES.md`.

### Première observation structurelle (avant toute recherche externe)
Les 99 sommets d'un Conway-99 enraciné en x (N(x) = 7K₂) s'identifient **canoniquement** aux 99 vecteurs de norme ≤ 2 de Z⁷
(0 ; ±eᵢ ; ±eᵢ±eⱼ), c'est-à-dire à la **boule de Hamming de rayon 2 de F₃⁷** (1 + 14 + 84 = 99 = 2m²+1). Les adjacences forcées sont exactement
« différer d'un vecteur unité modulo 3 ». Les extérieurs sont les **84 racines de D₇**, σ = −1, le groupe des relabellisations est W(B₇) = 2⁷⋊S₇.
Même chose pour m = 11 : 243 = |B₂(F₃¹¹)| et BvLS est le graphe de cosets du code de Golay ternaire **parfait** ; pour m = 2 : code parfait trivial.
Voir `notes/02_Z7_HAMMING.md`.

### Phase 1 — divergence (recherches annexes)
Recherches web (sources et mécanismes dans `notes/external_bridges/B01…B05`) : codes parfaits / Lloyd / codes complètement réguliers ; p-rangs
(mémoire de van Eijl 1991, lu : bornes par caractères modulaires) ; nombres de Frame et algèbres modulaires (arXiv 2512.06541) ; conditions de Krein et
nombres d'intersection triples (Coolsaet–Jurišić, Vidali) ; réseaux unimodulaires impairs (aucun de minimum ≥ 3 en dim ≤ 22) ; graphes signés à deux
valeurs propres ; compléments étoilés (Azarija–Marc 2018, lu en entier : mécanisme extrait) ; Ishida (involutions du Moore 57) ; graphes amplement
réguliers ; ETF (Sustik–Tropp–Dhillon–Heath). Calculs : `scripts/krein.py` → paramètres de Krein entiers pour m = 2, 11 et de dénominateur 49 pour
m = 7, 56, 497 (OBSERVÉ ; les cas ouverts sont exactement 7 | d).
Idées : `IDEES.md` (16 pistes, dont 10 hors vocabulaire Q/S/D/SAT).

### Phase 2 — convergence/falsification (expériences courtes, toutes non certifiées)
- I-05 (harmoniques des racines) : RÉFUTÉ sur BvLS. N01 (triangles signés) : fausse piste corrigée. Voir NEGATIVE_RESULTS.
- **E1 profil des grilles** (`data/grid_profile.jsonl`) : g paires sœurs imposées. g ≥ 14 : UNSAT en 20–30 s partout ; certaines configurations à
  g = 5, 7, 10 UNSAT < 60 s, d'autres TIMEOUT ; g ≤ 3 : TIMEOUT.
- **Noyau UNSAT d'allsib** : 745 contraintes (D 40, I 289, PS 236, PC 180, aucune (R)) touchant les 7 blocs.
- **LEMME S1 (DÉRIVÉ, `notes/03_LEMME_S1_paires_soeurs.md`)** : une paire sœur est un code parfait local ; partition exacte des 40 racines
  complémentaires **ssi m = 7** (2(m−2) = C(m−2,2)) ; vérifié comme empilement de densité 1/2 sur BvLS. Donne une **partition équitable** de Γ en
  6 cellules (quotient de spectre {14, 3³, (−4)²} — cohérent).
- E4 : le lemme S1 ajouté explicitement rend allsib UNSAT en 3,9 s / 623 conflits (contre ~20 s) ; pas de gain sur une configuration à 5 paires.
- E2 : 1 paire, 2 disjointes, 2 adjacentes, triangle : TIMEOUT 600 s.
- E5 : **H-COVER** (« UNSAT rapide ssi les paires sœurs couvrent les 7 blocs ») : couverture minimale {12,34,56,67} UNSAT 32 s ✓ ; P4+P3 couvrant UNSAT
  ✓ ; mais K₆ sur 1..6 (bloc 7 libre) UNSAT 33 s ✗ → hypothèse réfutée dans le sens « non couvert ⇒ difficile ». Étoile K₁,₆ couvrante : TIMEOUT
  300 s ✗ → réfutée aussi dans l'autre sens.
- **Théorème G1 (DÉRIVÉ, général)** : toute grille 3×3 d'un srg(99,14,1,2) est un code parfait (tout sommet extérieur a exactement un voisin dans la
  grille) ⇔ k ∈ {4,14} ; ensemble intrigant de valeur propre 3 ; partition équitable à 18 cellules (spectre vérifié). Note `notes/04_…`.
  Pont littérature B06 (Bamberg–De Clerck–Durante ; le résumé automatique qui prétendait que l'article traite PQ(2,6,2) était faux — vérifié).
- E6 (300 s) : UNSAT : copies isomorphes de la couverture minimale (21–24 s), K3+K2+K2, K13+P3 (104 s), K2+P5, K2+spider (18 s), K2+K3pendant
  (199 s, bloc 6 libre), K3+K3 (139 s), K4+K2 (17 s), C6 (205 s). TIMEOUT : spider (bloc 6 libre), 3K2+{13}, K2+K₁,₄ (couvrant), P6.
  Conclusion provisoire : les configurations riches en grilles par x meurent, de façons variées ; pas de critère simple (ni couverture, ni nombre de
  paires disjointes) — la frontière reflète surtout l'heuristique du solveur. Configuration minimale connue : K2+K2+P3 (4 grilles par x).
- E4 (une seule paire + lemme S1 explicite) : TIMEOUT 900 s. Le cas sib n'est pas trivialisé par le lemme.
- E7 (propagation de grille en e₆ pour {56,67}) : TIMEOUT 600 s ; E8 (exactement {12} ; exactement {12,34}) : TIMEOUT 900 s ; E3 (tout one,
  tout dis, aucune sib) : TIMEOUT 600 s. Non concluants.
- Antériorité vérifiée : G1 = application du lemme de Wilbrink–Brouwer ; Lou–Murin (MIT PRIMES 2014) : « grille moins une arête ⇒ grille »,
  n'excluent pas les grilles (un résumé de moteur de recherche laissait croire le contraire : vérifié à la source).

### Phase 3 — certification (Docker autorisé par l'utilisateur à 21:15)
- Docker Desktop démarré ; `.wslconfig` d'origine sauvegardé dans `logs/wslconfig_original_backup.txt`, configuration labo 8 Go / 13 CPU appliquée
  (à restaurer en fin de session).
- CNF (LF) : base identique octet pour octet à `k14_none.cnf` audité (sha256 a59d3e04… recalculé), + unités. `data/cnf/MANIFEST.txt`.
- kissat 4.0.4 + DRAT + drat-trim : **VERIFIED** pour allsib, K2+K2+P3, K3+K2+K2, K2+P5, K2+araignée, P4+P3, K1,3+P3, K3+K3 (18–236 s).
  Note `notes/06_THEOREME_GRILLES_PAR_X.md`.
- Vague 2 (CaDiCaL, survivants maximaux) : K₁,₁,₄, S8, S7a, S7b, S7c, S6 UNSAT (70–600 s) → 57 graphes Σ survivants, ≤ 8 arêtes.
- Boucle automatique `scripts/sib_loop.py` lancée (900 s, 6 en parallèle, 3 itérations max) ; état `data/sib_state.json`.
- Minimisation glucose du noyau de K2+K2+P3 : 339 → 175 contraintes (en cours).
- Défauts de domination des carrés D (`notes/07_…`) : 0 (sib), 2 (one), 8 (dis).

### Phase 4 — changement de régime, prismes, comparaison C3 (soir du 2026-09-23)
- Remarque de l'utilisateur : trop prudent (certification DRAT systématique = l'ancien pipeline). Boucle `sib_loop.py` **arrêtée** ; plus de
  certification systématique, retour aux idées risquées.
- Bilan des certificats (drat-trim VERIFIED) : 20 configurations de Σ interdites, dont 7 issues de la boucle (g06/g07/g08, empreintes dans
  `data/cnf/MANIFEST.txt`). **Σ ∈ 53 graphes, ≤ 7 arêtes (ÉTABLI, DRAT seul)** ; 50 si l'on ajoute K₄, S6, S7a, S8 (UNSAT solveur, sans preuve).
  g07_ca15a23af4 : UNKNOWN à 900 s.
- Prismes et n₃ (`notes/08_…`, DÉRIVÉ) : Σ c = 6P, c̄ = 4 − 2n₃/2079 (Reimbayev, arXiv 2508.03377). **n₃ < 2079 ⇒ une grille existe** ;
  en C2, n₃ ≡ 0 (mod 6).
- L'utilisateur révèle que C3 est résolu ailleurs (preuve Lean). À sa demande : comparaison de `conway99-c3-experimental` (invariant « après le
  rang » : discriminants des deux spécialisations de Z₃[C₃], ~1 jour, sans solveur) et de `conway99-c3` (cas, SAT, cubes, DRAT : rien de décidé).
  Clones dans `external_c3/` (hors des dépôts en lecture seule).
- Transfert à C2 (`notes/09_TRANSFERT_C3.md`, `scripts/milgram_check.py`, `logs/milgram_check.txt`) :
  à p = 2, l'analogue exact de la contradiction C3 donne seulement ρ₊ + ρ₋ pair. **Mécanisme vide pour une involution** : les caractères de C₂
  sont rationnels, et le recollement équivaut à la formule de Milgram du réseau total (N09).
  Sous-produit indépendant de σ (DÉRIVÉ) : **rang₇(A − 3I) est impair et D₇(N₃) est de type moins**, pour tout srg(99,14,1,2).
  Prédictions testées sur Paley(9), T(7), L₂(7), Paley(49) : toutes ✓. La prédiction non triviale (type à p = 5 sur T(7)) est confirmée.
- Correction de mon message à l'utilisateur : j'avais présenté la parité de rang₇ comme propre à C2. Elle ne l'est pas.

### Phase 5 — quartier libre (nuit du 23 au 24/09)
- **Invariants de Brown tordus** (`notes/10_…`, `scripts/brown_twist.py`) : les formes b(y, f(A,P)y) contredisent le verdict « vide » de N09.
  Lemme des blocs de rang 1 : β(F; a, a′) = a·t₊ + a′·t₋ (mod 8). Validé : 0 désaccord sur 32 768 formes, pour Paley(9), L₂(7) et Paley(49).
  Conséquences C2 (DÉRIVÉ) : ρ₊, rang₇(S − 3I), rang₇(S_out − 3I) et rang₇(Q_out − 3I) sont **pairs**.
  Le système de genres de C2 reste cohérent : ce sont des parités, pas une contradiction, parce que 7 ≡ −1 (mod 4).
- Littérature 2026 : Akiyama (arXiv 2609.08319) démontre la non-existence de srg(266,45,0,9) par un réseau de Niemeier (argument de
  classe) ; pont B07. Méthode défavorable pour C2 : les repères serrés y sont minces. Autres articles : Reimbayev (ordre 7, 2608.19410) ;
  Thakkar–Severini (réduction forcée + CP-SAT, 2608.11211).
- **Étage S seul** (jamais testé dans le dépôt C2 avec Cᵀ S_out = 0) : modèle CP-SAT `scripts/stage_s_alone.py`. Équations validées sur le
  vrai BvLS (m = 11 : S C = 0 et S² + S = 20I − CCᵀ exacts). Outil S → D `scripts/extend_s_to_q.py`, validé sur BvLS (une seule
  complétion, 55 paires sib).
  Deux recherches lancées à 23:08 et 23:17 : sans symétrie (12 cœurs, 40 min) et avec la symétrie cyclique d'ordre 7 imposée (3 cœurs).
- Résultats de l'étage S seul : **UNKNOWN** en 40 min sur 12 cœurs (sans symétrie) et en 20 min sur 3 cœurs (symétrie cyclique d'ordre 7
  imposée). Le problème n'est pas trivial.
- BreakID sur la CNF de l'étage S : **0 générateur**. Les encodages de cardinalité cassent la symétrie syntaxique ; il faudrait casser les
  symétries à la main (ligne 0 canonique sous son stabilisateur, d'ordre 7 680).
- **Nuit du 23 au 24/09** (l'utilisateur laisse le PC allumé ; note « NE PAS ÉTEINDRE » à l'écran ; processus anti-veille ; économiseur
  d'écran coupé ; charge plafonnée vers 65–70 %, priorité basse), 7 h chacun, lancés à 23:49 (`scripts/night_run.sh`) :
  - A : étage S + couplage D + sommes par bloc (CP-SAT, 4 fils) ;
  - B : étage S seul (CP-SAT, 2 fils) ;
  - C, D : étage S seul (kissat, 1 fil chacun, graines 1 et 2).
  Un UNSAT pour A ou B tuerait C2 (après certification). Une solution de B permettrait de tester « rang₇(S − 3I) pair » et d'essayer la
  complétion S → D.
- Remise en état au retour : `scripts/restore_machine.ps1` (anti-veille, économiseur d'écran, conteneurs, .wslconfig).
- 01:51 et 02:05 : aucun verdict. kissat C ≈ 1,5 M de conflits, kissat D ≈ 1,2 M ; les deux CP-SAT tournent. Charge ≈ 65–75 %, RAM libre
  14 Go ; note et anti-veille actives.
- Énumération des motifs de ligne de la relaxation A (`scripts/row0_patterns_A.py`) : trop lente en Python naïf, arrêtée au bout de
  12 min de CPU pour ménager le processeur. À réécrire : multigraphes 4-réguliers sur les blocs, puis signes.
- Littérature : `Lundle22/conway-99-cyclic-lifts` ne traite que les relevés d'ordre 3 (entiers d'Eisenstein, donc caractère non
  rationnel), rien sur Z₂. Ce qui confirme qu'il n'y a pas de prise « à la Eisenstein » pour C2.
- Borne LP (Delsarte) sur les 84 vecteurs ±z_o de R¹⁵ (norme 10, repère serré de constante 28) : la positivité de P₄ est largement
  satisfaite (le terme diagonal domine), pas d'obstruction. Repère mince, comme prévu (B07).
- **Fin de nuit (07:06)** : les quatre calculs sont **UNKNOWN après 7 h** :
  - A (étage S + D + sommes par bloc, CP-SAT 4 fils) et B (étage S seul, CP-SAT 2 fils) : UNKNOWN en 25 200 s ;
  - C et D (étage S seul, kissat, graines 1 et 2) : UNKNOWN, 158,7 M et 153,8 M de conflits.
  Conclusion : couper le problème en étages ne rend aucun morceau facile. L'étage S seul, comme l'étage Q seul et le modèle complet
  (dépôt C2), résiste à ces budgets. Charge mesurée pendant la nuit : 52 % (compteur « % temps processeur », moyenne sur 30 s).
