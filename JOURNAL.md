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
  en C2, n₃ ≡ 0 (mod 6). [**FAUX**, corrigé plus bas (note 20) : n₃/3 ≡ n_one (mod 2).]
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

### Phase 6 — reset intellectuel (24/09, sur demande de l'utilisateur)
Consigne : ne plus imiter C3, aucune piste privilégiée (Δ compris), creuser en profondeur **un** mouvement conceptuel absent de
l'historique, et ménager la machine (processeur et RAM limités : calculs mono-fil courts en priorité minimale).
- **Mouvement choisi : t comme RÉFLEXION PONCTUELLE**, et ce qu'elle induit sur les structures parfaites (notes 11–13).
  - **Théorème R1 (DÉRIVÉ, preuve écrite)** : une grille Λ ∌ x est disjointe de tΛ ; le couplage π entre elles est parfait ;
    φ = t∘π est une involution de point fixe unique w ∈ N(x) ; les étiquettes sont partitionnées ; φ fixe le type D des racines.
  - **Conjecture R2** (φ = réflexion ponctuelle) : vraie dans BvLS, 990/990 (`scripts/bvls_grid_phi.py`). En C2, test court
    `grid_offx_phi.py SS phi` : TIMEOUT 300 s.
  - Translations locales ρᵢ = t∘ι_{eᵢ} : « translation partout » implique allsib, donc impossible (DÉRIVÉ).
  - X_Γ (triangles + carrés μ) est localement isomorphe au complexe de H(7,3). Points fixes de t : étoile de x + 21 centres de carrés D.
    Lefschetz : tr(t|H₂) − tr(t|H₁) = 21 ; χ(X/t) = 869.
  - Aucune 22-coclique de Delsarte n'est t-invariante (DÉRIVÉ). Les paires de grilles sont des ensembles intrigants t-invariants de taille 18.
- 24 théorèmes rêvés (note 12). Réfutés proprement : Krein gradué à deux points (`graded_krein.py`, tous ≥ 0 même pour des involutions
  hypothétiques) ; « existence de grille » via les fréquences d'ordre 7 (N10).
- Recherche ciblée (deux agents, en profondeur) : systèmes triples de Hall et caractérisations locales de Hamming ; Ishida et nombres
  d'intersection triples.
- Test « partition en 11 grilles » (`grid_spread.py`, ≈ 4 500 variables de couplage) : TIMEOUT 300 s (N13), pic à 1,9 Go de RAM.
- **Recherche en profondeur des mécanismes externes (note 14)** :
  - Hall 1960 et Bondarenko–Radchenko 2013 donnent exactement le mécanisme du mouvement « réflexion » : réflexions automorphes ⇒
    translations ⇒ structure affine sur F₃ ⇒ 3^m sommets. C2 = « Hall en un seul point » (au plus une réflexion est automorphe).
  - L'étape de BR qui propage (N(v) base propre, g = k) échoue ici : le 1-voisinage est de rang 14 dans V₋₄ (dim 44), et le résidu
    de dimension 30 porte toute l'inconnue. Lemme manquant formulé : (P) propagation, équivalent à la mort de C2.
  - Défauts de Hall en x (DÉRIVÉ) :
    - σ_v(x) = σ_x(v) seulement pour les 4n_sib ≤ 28 coins sib ;
    - au plus 28 orbites de droites D-fermantes sur 42 ;
    - multiplicité des milieux m(a,b), de moyenne 1 ± J/… ;
    - J_x par la configuration à 7 points M_p(q) = M_q(p).
  - Makhnev 1988 (réf. [7] de Reimbayev) : descente 99 → 33 sous n₃ = 0, régime opposé à C2. Hamming local, Cameron : inapplicables.
  - Ishida étendu aux modules des droites, arêtes et carrés μ : identité vérifiée partout (6 = 6, 0 = 0, 0 = 0), mécanisme vide (N14).

### Phase 7 — R2, types locaux, recollement (24/09, suite ; note 15)
Demande : preuve humaine de R2 en supposant φ(a) ≠ −a, lien avec le programme Δ et avec le théorème annoncé du dépôt C3 ;
puis (suggestions relayées « à prendre avec des pincettes ») classer les φ survivants, étudier (φ, τ, ω), recoller deux grilles.
- **Formule des multiplicités** : m(u,v) = 2 − [u ~ φ(v)] − [φ(u) ~ v] − [φ(u) = v] (DÉRIVÉ).
- **Théorème 15.3 (DÉRIVÉ)** : R2 complète ⇒ a, b, c, d dans quatre blocs distincts, avec un motif rigide des coins. Elle est donc
  **fausse** dès qu'une droite de Λ en w est sœur.
- **Énumération exacte** (`r2_label_constraints.py`, `r2_types.py`) :
  - 1194 types locaux à symétrie près (W(B₆) × D₄), 263 formes de φ, 20 types « droites R2 ». Une preuve locale de R2 est impossible.
  - Le filtre S1-vu-depuis-w n'élimine rien de plus.
- **(φ, τ, ω, H)** :
  - τ n'est forcé que sur les échanges P–P ;
  - l'ombre Φ n'existe que pour 56 types ;
  - l'ordre 3 apparaît pour certains choix, jamais pour tous. Pour la réflexion, ⟨Φ, ν⟩ est le groupe de Klein.
- **Symétries candidates g** : 112 types en ont une. Aucune ne peut se propager en C2 (Aut = ⟨t⟩, et g fixerait x et w).
- **C3** : inutile ici (|Aut Γ| ≤ 3 suffit). Le README du dépôt C3 (23/09) dit que la conclusion n'est pas encore acquise ; il a été
  lu seul, pour l'énoncé.
- **Incompatibilité** : R2 complète en w ⇒ σ_w ∉ Aut.
- **Recollement de deux grilles** partageant une droite (`r2_two_grids.py`, sans étiquettes, 4 s) :
  - 3977 paires (φ, φ′) compatibles sur 8325 ;
  - aucun φ éliminé.
- **Tests SAT locaux** (`r2_local_sat.py`, relaxation touchant S) : T3 et T1 en TIMEOUT à 240 s.

### Phase 8 — relaxations de moments (24/09, soir ; note 16)
Plan relayé : relaxation SoS de degré 2 sur les arêtes libres, symétrisée, avec contraintes multipliées ; puis cran ciblé si réalisable.
- **Prémisse corrigée** : 1722 variables (à t près), pas 210. 210 est le nombre de vraies arêtes de type II.
- **Tailles** (Burnside sur W(B₇)) :
  - 4 moments d'ordre 1, 142 d'ordre 2 ;
  - PSD réduite à 243 × 243 par la représentation régulière.
- **Degré 2** (`sos2_relax.py`, cvxpy + Clarabel installés dans `.venv`) :
  - m = 2 réalisable ✓, m = 3 irréalisable ✓, m = 4, 5, 6 réalisables (aveugle à l'intégralité) ;
  - **m = 7 réalisable**, espace affine de dimension 35, y_sœur ∈ [0, 1] ;
  - raison : au degré 2, λ et μ sont fusionnés dans (P).
- **Degré 3, triangles** (`sos3_triangles.py`) :
  - réfute m = 3 et m = 4 ;
  - **m = 5, 6, 7 réalisables**, y_sœur ∈ [0, 1] : même allsib (certifié UNSAT) passe.
- Axes B et C du plan : contenus dans ces relaxations ; C ne peut pas réfuter allsib.

### Phase 9 — pari « C2 n'existe pas » : preuve humaine d'allsib (24/09, nuit ; note 17)
- Allsib se ramène exactement, par le lemme S1, à une connexion à valeurs dans D₄ sur KG(7,2) (`allsib_connection.py`).
  - UNSAT en 31 s ;
  - **LM + H3 suffisent** ; H4 n'est pas nécessaire ; LM seul et H3 + H4 s'arrêtent en TIMEOUT à 300 s.
- **Preuve humaine (DÉRIVÉ)** :
  - λ et μ entre paires disjointes ⇒ le caractère d'échange des t-orbites est un 1-cocycle c sur le complexe des couplages M₇ ;
  - H¹(M₇ ; Z₂) = 0 (calculé : rangs 20 et 85) ⇒ c est un cobord ;
  - μ entre paires qui se coupent ⇒ #{r : c(ij,r) + c(ik,r) = 1} = 3, alors qu'un cobord donne 0 ou 6. Contradiction.
- Patron local → global identifié (rigidité → cocycle → topologie → comptage). La suite : le rejouer sur les autres configurations,
  puis avec les carrés D one/dis (« cocycle à défauts »).

### Phase 10 — système χ des paires sœurs (25/09, nuit ; note 18)
- **Système χ** : la preuve d'allsib, transportée au niveau des orbites (étage Q), pour toute configuration Σ. Contraintes dérivées de (Q1)–(Q4) :
  bij, disj, int, fibre, bloc.
- **Résultats** :
  - 16 des 26 configurations certifiées ou candidates sont χ-UNSAT (moins d'une seconde chacune), **dont g07_ca15a23af4**, resté UNKNOWN
    à 900 s dans le modèle complet ;
  - **g07_ca15a23af4 certifié** à l'étage Q : kissat 38 s, DRAT de 543 Mo VERIFIED ;
  - contrôle croisé par l'étage Q (encodage indépendant) : allsib, K3K3, g07 et les atomes 01, 02, 03 sont UNSAT ;
  - classification des 1044 graphes : 988 χ-UNSAT, 56 χ-SAT, **11 atomes minimaux (CNF χ avec DRAT VERIFIED)** ;
  - Σ : 52 survivants après les certificats, **39 après le système χ**.
- **Preuves humaines** : lemme du triangle (répartition 3 par classe antipodale) et corollaire K₃ + K₂. Le noyau de la preuve humaine est
  vérifié UNSAT, et chacun de ses ingrédients est nécessaire.
- **Suite** : preuves humaines des atomes 02 à 11 ; les 39 survivants ; le système χ à défauts, où une paire D chevauche 1 orbite
  (type one) ou 2 (type dis).

### Phase 11 — systèmes de lignes, système χ signé, lemme des étoiles (24/09, après-midi ; note 19)
- **Méthode.** On écarte le « χ à défauts » : pour les paires D de types one et dis, il n'a pas de domaine canonique. On étudie
  plutôt les systèmes de lignes :
  - RS(S) : l'étage Q, filtré par support ;
  - RSF(S) : le modèle complet, filtré par support. RSF(tout) reproduit K2K2P3.cnf **au sha256 près**.
- **RS(lignes sœurs) ≡ système χ** : 23 contrôles sur 23, puis monotonie.
- **Il manque les signes, pas des lignes.** RSF(lignes sœurs) réfute les 8 configurations χ-SAT certifiées ailleurs, et S6, un
  survivant maximal : **rsf_S6 DRAT VERIFIED**.
- **Système χ signé.** Il s'écrit (sbloc, sbij, sdisj, sint), par une connexion D₄ et des signes σ_p. Contrôles :
  - correction par transfert de modèles, 8 sur 8 ;
  - second encodage « un parmi quatre » ;
  - 3 à 60 fois plus rapide que RSF.
- **Étoiles.**
  - K₁,₃ résiste à tous les solveurs : cadical, CryptoMiniSat avec parités, kissat 1200 s.
  - À χ fixé, c'est réfuté en 0,0 s. La réfutation est une pure parité : 300 cas sur 300.
  - Les certificats se somment en un système **indépendant de χ**, (L1) + (L2).
  - ⇒ **LEMME DES ÉTOILES : trois paires sœurs ne partagent jamais un bloc (degré de Σ ≤ 2).** Preuve humaine par G1, S1(a) et
    μ = 2 (deux fois).
  - Ses deux ingrédients sont vérifiés par SAT dans RSF (Fait A : 9 cas ; Fait B éclaté : 12 cas), puis **certifiés par DRAT**
    (18 CNF, toutes VERIFIED).
  - La parité seule classe les 1044 graphes : K₁,₃ est l'**unique atome**.
- **Survivants : 39 → 12.**
  - 24 tombent par le lemme ;
  - C₅, P₆ et C₄+K₂ tombent par le système signé (**DRAT VERIFIED**, de même que S6).
  - Restent ∅, K₂, P₃, 2K₂, K₃, P₄, P₃+K₂, 3K₂, C₄, P₅, P₄+K₂ et 2P₃, tous SAT sur les lignes sœurs.
- **Modèle complet sur les survivants à 4 arêtes**, kissat 600 s :
  - C₄ : UNSAT, 495 s, DRAT ;
  - P₄+K₂ : UNSAT, 252 s, DRAT ;
  - P₅ et 2P₃ : UNKNOWN.
  → **10 survivants**. Lots en cours : 3 arêtes, 2 arêtes et K₂ en Σ exact, puis P₅ et 2P₃ en Σ exact.
- **Parité des orbites « − »** : toute ligne a un nombre pair de voisins Q = 1 « − ». Contrôlée sur BvLS ; l'étage Q ne la voit pas.
- **Cœur sans grille.**
  - Sondes RS et RSF locales (star(1), 4 blocs, star(1) ∪ star(2), type d_1) : TIMEOUT. Seul d_1 = 5 donne UNSAT, comme contrôle.
  - Étoiles mixtes (arêtes D de type one) : SAT sur leurs lignes. Le mécanisme des étoiles est propre aux grilles.
- **Méthodologie.**
  - Un solveur qui échoue à χ libre mais réussit instantanément à χ fixé signale un certificat global caché. Il faut le chercher à χ
    fixé, puis sommer.
  - Une affirmation non calculée de la première version de la note (« (L1)+(L2) compatibles pour K₁,₃ ») était fausse. Elle a été
    corrigée.
- **Suite (même après-midi), après le commit ef1ff6d.**
  - **Noyaux DRAT des réfutations du modèle complet.** Celui de P₄+K₂ touche 41 lignes, surtout l'étoile du bloc libre 3. Celui de
    C₄ touche 25 lignes, dont toute l'étoile du bloc libre 1.
  - **RSF(lignes sœurs de P₄+K₂ + star(3))** : UNSAT, 100 s, **DRAT VERIFIED**. Vingt lignes suffisent, mais la réfutation est dense.
  - **Lot « étoile libre »** (lignes sœurs + star(c), c libre), kissat 900 s : C₄ et 2P₃ sont UNKNOWN. La suite est en cours.
  - **L(Q), système linéaire des parités de signes** : sur BvLS, rang = 990 = nombre de signes. Les signes sont déterminés par Q, et la
    cohérence de L(Q) impose 7425 conditions linéaires sur le second membre b(Q).
  - Lots en Σ exact sur les survivants à 3 arêtes (600 s) : K₃ et P₄ UNKNOWN. Les autres ont été suspendus au profit des noyaux.
- **CORRECTION (24/09, note 20).** La note 08 affirmait « aucun prisme σ-invariant ⇒ n₃ ≡ 0 (mod 6) ». C'est **faux**.
  - Les prismes σ-invariants sont les {±e_c, ±a, ±b}, où {a,b} est une arête D interne à star(c) ; il y en a 2 n_sib + n_one.
  - BvLS le confirme : 110 = 2·55.
  - La bonne relation est n₃/3 ≡ n_one (mod 2). Les notes 08 et 14, la synthèse et la page sont corrigées.
- **24/09 soir — lemme de l'étoile libre (note 20).**
  - **Réduction.** Si aucun bloc n'est libre, Σ = K₂+K₂+P₃, déjà exclu par DRAT. Donc **lemme de l'étoile libre ⇒ C2 n'existe pas**.
  - **Formulation compacte** du problème local RSF(star(1)) (DÉRIVÉ, validée exactement sur BvLS m = 11). Les données sont deux
    couplages μ, τ de 12 points et une bijection Φ entre les 60 racines lointaines et les 60 paires hors μ, avec trois familles de
    comptes (i), (ii), (iii). On compte 2 903 types (μ, τ) à symétrie B₆ près, dont 4 seulement pour le cube A111111.
  - **Aucun solveur générique ne tranche** : kissat sur RSF (cubes A411, A2211, A42 : UNKNOWN à 900 s), cadical, CP-SAT, MILP,
    recuit.
  - **Calibration.** Avec une solution plantée à m = 7, cadical n'en trouve que 2 sur 3 en moins de 120 s. Un UNKNOWN ne vaut donc
    rien comme indice d'absence. La famille m = 3, 4, 5 est entièrement UNSAT, mais pour des raisons de comptage. À m = 6, certains
    types sont déjà durs.
  - La file des cubes RSF est arrêtée. Suite : un argument à la main sur la formulation compacte, en commençant par A111111.
  - Garde-mémoire v2 : il n'agit que sur une baisse soutenue. Kissat occupe 65 Mo, la machine virtuelle Docker environ 3 Go.
- **24/09 soir — revue complète (note 22, annexes A–D).**
  - Sur demande de l'utilisateur : lecture de C3 (étincelle : « quel invariant après le rang ? » ; note 21) et de C1 (instantané en
    lecture seule, annexe D).
  - Quatre relecteurs indépendants ont scoré chaque idée, tentée ou non. Chaîne jusqu'aux 10 survivants : saine. Formulation compacte :
    complète. Erreurs et surinterprétations corrigées dans les notes 06, 09–16, 19–21, IDEES, NEGATIVE_RESULTS, SYNTHESE, REPRISE.
  - Vérifications personnelles :
    - constructeur RSF identique à l'octet près au CNF certifié ;
    - encodages des 18 faits relus ;
    - cubes de l'étoile libre exhaustifs (10 395) ;
    - n₃ ≥ 2079 − 9N ;
    - S ≡ 0 (mod 4) et z₁₁ ≡ 4n_one (mod 8), à partir de L18 de C1.
  - Diagnostic convergent : tout ce qui a marché est une **parité**, ce qui explique l'échec des solveurs CDCL. Programme : q:parite à
    l'ordre 7, parité linéaire (Gauss), cocycle à défauts.
- **24/09 soir — q:parite (ordre 7), `scripts/order7_burnside.py`.**
  - Burnside mod 2 sur les 208 classes d'ordre 7 (famille indépendante concordant avec Reimbayev corrigé).
  - 4 classes déterminées par la carte et 7 réduites à la main : toutes cohérentes. **Aucune contradiction, aucune contrainte nouvelle.**
  - n_sib n'apparaît qu'avec un poids pair à l'ordre 7 : une parité de |Σ| demanderait l'ordre 9.
  - C1 (construction par RRR) a reçu nos faits utiles et a corrigé ses notes ; il n'élague avec aucun lemme UNSAT.
- **24/09 soir — propagateur de Gauss** (`scripts/gauss_propagator.py`).
  - Construction : IPASIR-UP ; version (q, b) où tous les termes b·b disparaissent mod 2 ; branchement sur le niveau Q.
  - Sain : K₂ SAT avec modèle vérifié.
  - Ne réfute pas K₁,₃ en 300 s, même avec les 18 faits A/B.
  - Diagnostic : la parité du lemme des étoiles vit au niveau χ, grâce au caractère one-hot de S1/G1 ; les bits bruts ne la voient pas.
  - Pour un bloc libre (sans grille), l'analogue doit venir des carrés one/dis : cocycle à défauts, piste principale.

## 2026-09-25 (après-midi) : reprise par la session principale C2, en régime strictement mathématique
- Contexte : l'utilisateur a imposé à la branche C2 un régime **sans aucun solveur** (plus de SAT, CP-SAT, cubes ni DRAT pour
  décider des cas), puis (relais de C1) le retour à la *démarche* de C3. Le carnet principal (`MATH_C2_PROGRAMME.md`, branche
  math-c2-programme) a avancé de son côté : §16 à §23, Théorèmes F, P et D, cas ancrés (6,3,3,3,2,2,2) et (6,0,3⁵) ouverts.
- **Incident.** Croyant créer un nouveau labo, j'ai réinitialisé ce dépôt (`git init`, sans effet) et écrasé README.md, IDEES.md et
  JOURNAL.md. Ils ont été restaurés aussitôt depuis HEAD. D'après le transcript de la session du labo, aucune modification non
  validée de ces trois fichiers n'a été perdue : leur dernière modification précède le commit du 24/09 22:19.
- Note 24 (`notes/24_P2_ARF_LOCAL.md`) : le niveau p = 2 est vide, invariant d'Arf compris. Elle confirme N09 et les notes 09–10.
  Apport : une formule locale de l'Arf, contrôlée dans 50 cas sur 50 (Paley(q²), graphes de réseaux L_m(n), BvLS), qui redonne
  σ_S ≡ 1 (mod 8). Voir aussi N24.
