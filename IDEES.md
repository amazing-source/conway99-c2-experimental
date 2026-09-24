# IDEES — pistes du laboratoire expérimental C2

Format : nom · statut · origine · langage · différence avec l'existant · upside · test de falsification · résultat · décision.
Statuts : OUVERTE / EN TEST / SURVIT / RÉFUTÉE / ABANDONNÉE / REDONDANTE.

---
## I-01 GRILLES (rigidité « de Hamming » au point fixe)
- **Statut** : EN TEST (signal fort, voir résultat).
- **Origine** : pont B01 (codes parfaits) ; observation : BvLS et Paley(9) sont « allsib » ; phase 2 : allsib UNSAT en 33 s.
- **Langage** : géométrie d'incidence (quadrangle partiel PQ(2,6,2), grilles 3×3), boule de Hamming B₂(F₃⁷).
- **Différence** : sib/one/dis n'a servi que de découpage de symétrie ; personne n'a demandé *combien* d'arêtes D sœurs (= grilles par x) sont possibles.
- **Upside** : un lemme « au plus g₀ grilles par x » (ou « jamais deux paires sœurs adjacentes ») réduirait drastiquement le cas sib, et fournirait un
  mécanisme expliquant pourquoi m = 7 diffère de m = 11. Si « aucune paire sœur » était démontrable, le cas sib serait clos à la main.
- **Test** : E1 (`scripts/grid_profile.py`) : imposer g paires sœurs, 60 s CaDiCaL. E2 (`grid_small.py`) : petites configurations.
- **Résultat (OBSERVÉ, non certifié)** : g = 21…14 : UNSAT en 20–30 s pour toutes les configurations testées ; g = 10 (3 tirages) et g = 7 : UNSAT < 50 s.
  Toutes les configurations à ≤ 3 paires (K2, 2K2, P3, K3, K13, P4, 3K2, P3+K2) : TIMEOUT 600 s. Couverture minimale K2+K2+P3 ({12,34,56,67}) :
  UNSAT 21–32 s (3 copies isomorphes). Couvrantes à 5 paires : UNSAT 18–104 s. Étoile K₁,₆ (couvrante) : TIMEOUT 300 s. 3K2+{13} (bloc 7 libre) :
  TIMEOUT 300 s. Denses non couvrantes (K₆, K₅, K₅+67) : UNSAT ~30 s. H-COVER réfutée comme équivalence ; « couvrant avec ≥ 2 paires disjointes
  ⇒ rapide » tient sur toutes les données.
- **Théorie (DÉRIVÉ)** : lemme S1 (`notes/03_…`) puis **théorème G1** (`notes/04_…`) : toute grille d'un Conway-99 est un code parfait / ensemble
  intrigant positif (k = 14 est le seul k non trivial de la famille où c'est le cas). Explique la rigidité des paires sœurs à m = 7.
- **Décision** : priorité 1 ; chercher la configuration minimale contradictoire puis sa preuve humaine (E7 : propagation de grilles).

## I-17 THÉORIE DES GRILLES (général, hors involution)
- **Statut** : SURVIT (théorème G1 démontré ; conséquences en cours).
- **Origine** : pont B06 (ensembles intrigants de Bamberg–De Clerck–Durante ; sous-quadrangles serrés de Payne–Thas) + observation allsib.
- **Langage** : géométrie finie (quadrangles partiels), ensembles intrigants, codes parfaits dans les graphes.
- **Différence** : aucune trace de « grille » dans les fichiers C2 ; énoncé indépendant de l'involution.
- **Upside** : toute obstruction du type « pas de grille » (ou « grilles rares ») + un argument forçant des grilles tuerait des cas entiers ;
  les grilles hors de x donnent des vecteurs propres creux (±1, support ≤ 9) de S pour 3, i.e. des vecteurs courts du réseau N₊ (pont avec I-03).
- **Tests** : partition équitable à 18 cellules (spectre OK) ; Gram des grilles ; intrigants négatifs (|T| ∈ {22,…,77}).

## I-18 PROPAGATION DES GRILLES (Hamming local ⇒ contradiction ?)
- **Statut** : EN TEST (E7). Deux paires sœurs adjacentes {5,6},{6,7} forcent-elles la grille en e₆ entre {e₆, e₆±e₅} et {e₆, e₆±e₇} ?
  Si oui : lemme de propagation (les coins de cette grille sont des racines sur les 4 autres blocs — « repliement » de e₅+e₆+e₇ comme dans le Golay).

## I-20 … I-26 (second tour de divergence, évaluées en quelques minutes — ABANDONNÉES sauf mention)
- I-20 Formule de masse de Siegel / comptage d'isométries rationnelles de dénominateur 7 (W = 2S+I, W² = 49I) : les contraintes de support ne sont
  pas invariantes par le groupe algébrique ; pas de prise. ABANDONNÉE.
- I-21 Quotient à 50 sommets ↔ graphe de Hoffman–Singleton (50 sommets, degré 7) : coïncidence numérique ; Q n'est pas 7-régulier. ABANDONNÉE.
- I-22 Structure de Fano sur les 7 blocs (point k ↦ couplage des 6 autres par les droites de k) : n'induit qu'une direction par racine, pas la
  quasi-1-factorisation d'allsib ; et Aut = ⟨σ⟩ interdit toute symétrie d'ordre 7. ABANDONNÉE.
- I-23 Restreindre BvLS à 7 des 11 coordonnées (M₁₁ 4-transitif : une seule classe) : degrés ≈ 9 au lieu de 14 (densité 1/2 du lemme S1). ABANDONNÉE.
- I-24 Carrés μ de type D : un carré D est dans une grille ⇔ il est de type sib (DÉRIVÉ) ; les carrés one/dis ne sont dans aucune grille. GARDÉE comme fait.
- I-25 Atlas de cartes F₃⁷ (une par sommet, applications de transition) : reformulation sans contenu nouveau tant qu'on n'a pas d'invariant de monodromie.
- I-26 Z₈ (phase 2 : l'étape S est une identité mod 8 une fois Q connu) : observation d'encodage, pas d'obstruction. REDONDANTE.

## I-19 DEGRÉ SŒUR σ_α ET COMPTAGES DE DOMINATION
- **Statut** : OUVERTE. DÉRIVÉ : si σ_α ∈ {0,1,2} = nombre de sœurs adjacentes à α, alors α a 8 + σ_α voisins évitant ses deux blocs, 4 − 2σ_α
  touchant un seul de ses blocs ; pour une paire p, Σ_{β évitant p} |N(β) ∩ P_p| = 32 + 2s_p (s_p = arêtes sœurs de la paire). Densité de domination
  0,8 / 0,9 / 1 selon s_p = 0 / 2 / 4 : la paire sœur est le cas parfait.

## I-02 DÉFAUTS F₃ DES DROITES
- **Statut** : OUVERTE.
- **Origine** : B01 ; coordonnées F₃⁷ canoniques de tous les sommets (diamètre 2).
- **Langage** : F₃-algèbre linéaire, codes ternaires.
- **Différence** : jamais utilisé ; les calculs mod 3 antérieurs portaient sur les matrices Q, S, pas sur le plongement des sommets dans F₃⁷.
- **Idée** : pour chaque droite ℓ (231), δ(ℓ) = Σ_{p∈ℓ} p ∈ F₃⁷ ; δ = 0 ⇔ droite affine. Dans BvLS (coordonnées = représentants de cosets) δ(ℓ) ∈ code de Golay.
  Aφᵢ ≡ −φᵢ + Δᵢ (mod 3) où φᵢ = coordonnée i, Δ(p) = Σ_{ℓ∋p} δ(ℓ). Chercher un sous-espace de F₃⁷ contenant toutes les δ.
- **Upside** : obstruction « à la Lloyd » (3 n'est pas une valeur propre de H(7,3)).
- **Test** : sur BvLS, vérifier δ(ℓ) ∈ Golay ; à m = 7, dériver des identités sur Δ ; tester sur les configurations partielles (cubes).
- **Décision** : priorité 3 (après I-01, qui dit si la structure de Hamming survit localement).

## I-03 7-ADIQUE (ρ, réseaux N±, L±, formes de discriminant)
- **Statut** : OUVERTE.
- **Origine** : B03 (7 | d exactement pour les cas ouverts), B04 (réseaux entiers de l'involution).
- **Langage** : réseaux entiers, formes quadratiques p-adiques, codes auto-orthogonaux sur F₇.
- **Différence** : le contenu 7-adique (q:7) n'a jamais été étudié ; le 2- et 3-adique sont épuisés.
- **Objets** : R_S = lignes de S − 3I mod 7 = code **auto-orthogonal** [49, ρ] sur F₇ engendré par 49 mots de poids 13 ;
  R_S = (N₊ mod 7) ∩ (N₋ mod 7) ; det L₋ = 7^{22−ρ} ; rang₇(A−3I) = R₊ + ρ + 1.
- **Upside** : très grand si une obstruction 7-adique existe (et tuerait peut-être uniformément d ∈ {7, 21, 63}).
- **Test** : (a) calculer ρ sur des solutions partielles/relaxations ; (b) chercher une contrainte arithmétique (poids des mots de R_S, MacWilliams sur F₇,
  sous-réseau engendré par les normes 3) ; (c) contrôle m = 11 avec p = 3.
- **Décision** : priorité 2 (théorique).

## I-04 COMPLÉMENT ÉTOILÉ DE S
- **Statut** : OUVERTE. **Origine** : B05 (Azarija–Marc). **Langage** : reconstruction spectrale, cliques.
- **Différence** : jamais appliqué à C2 ; le complément étoilé n'a que 22 sommets (valeur propre 3 de S) et contient les 7 intérieurs connus.
- **Upside** : moyen (reste une recherche) sauf si un complément étoilé canonique est forcé.
- **Test** : sur BvLS : reconstruire S depuis un complément contenant les intérieurs ; compter les vecteurs candidats.
- **Décision** : priorité 4.

## I-05 HARMONIQUES SUR LES RACINES DE D₇
- **Statut** : OUVERTE. **Origine** : identification des extérieurs aux racines de D₇ (nouvelle). **Langage** : représentations de W(B₇), harmoniques.
- **Idée** : H tue les fonctions linéaires (dim 7) et vaut −2 sur les quadratiques diagonales sans trace (dim 6) : c'est exactement (I). Que fait H sur
  les quadratiques hors diagonale α ↦ Σ M_ij α_i α_j (21-dim) ? Dans BvLS ? Si une contrainte y était *forcée*, ce serait une condition nouvelle.
- **Test** : calcul sur BvLS / Paley(9) (rapide).
- **Décision** : test rapide.

## I-06 SYSTÈMES DE TRANSITIONS SUR LE CROSS-POLYTOPE
- **Statut** : OUVERTE. **Langage** : circuits eulériens, polynôme de Martin / interlacement.
- **Idée** : la structure s=1 = un système de transitions σ-invariant sur le graphe cocktail CP(7) (arêtes = racines de D₇) ; ses circuits = cycles s=1.
- **Upside** : faible à moyen (contraintes de parité ?). **Test** : dans BvLS : 55 cycles de longueur 4 (allsib). **Décision** : basse priorité.

## I-07 LASSERRE / SOMMES DE CARRÉS SYMÉTRISÉES PAR W(B₇)
- **Statut** : OUVERTE. **Langage** : optimisation convexe, représentations.
- **Idée** : l'ensemble des solutions est W(B₇)-invariant ⇒ toute relaxation convexe peut être moyennée ⇒ réduction par blocs. Un certificat dual = preuve.
- **Upside** : preuve vérifiable à la main si un bas degré suffit (peu probable pour tout le problème ; plausible pour allsib / grilles).
- **Test** : degré 2 + produits de Sherali–Adams sur la configuration allsib (UNSAT par SAT) ; doit être faisable à m = 11 (BvLS).
- **Décision** : après I-01 (sert à certifier/expliquer un lemme de grilles).

## I-08 TORSION DU 2-COMPLEXE (droites + carrés μ)
- **Statut** : OUVERTE. **Langage** : topologie algébrique, arbres couvrants simpliciaux (Kalai, Duval–Klivans–Martin).
- **Idée** : X = 99 sommets, 693 arêtes, 231 triangles, 2079 carrés μ (liens de sommets = K₁₄). Pour BvLS, X devrait être le quotient du complexe
  simplement connexe de H(11,3) par le code : H₁ ≅ F₃⁶ (à vérifier). Pour Conway-99 : H₁(X;Z) est un nouvel invariant (le « code » de Γ).
- **Test** : calculer H₁ de BvLS et de Paley(9). **Décision** : test rapide, curiosité à fort potentiel conceptuel.

## I-09 OBJET UNIQUE SUR Z[C₂]
- **Statut** : REDONDANTE. H = a + bσ ∈ M₄₂(Z[C₂]) ; Z[C₂] = {(q,s) : q ≡ s mod 2} : Q et S recollés mod 2 — c'est exactement le théorème F₂ (épuisé).

## I-10 GRAPHE TORDU Γ^t (B = A P_t)
- **Statut** : OUVERTE (basse). B² = A², spectre {14, (±3)²⁷, (±4)²²}, 14 boucles. « 2-marches équivalent » à Γ. Pas de mécanisme identifié.

## I-11 S COMME GRAPHE SIGNÉ À DEUX VALEURS PROPRES / W = 2S+I, W² = 49I
- **Statut** : OUVERTE (basse). Littérature : graphes signés réguliers à 2 valeurs propres classés jusqu'au degré 10 ; ici degré 12 avec boucles.

## I-12 CODES MULTI-PREMIERS (F₂, F₃, F₇) DU MÊME S
- **Statut** : OUVERTE. S mod 3 détermine S (entrées 0, ±1) ; S mod 2 → code LCD [42,20] ; S − 3I mod 7 → code auto-orthogonal [49,ρ].
- **Idée** : contraintes de poids croisées (MacWilliams) entre ces codes. **Décision** : sous-partie de I-03.

## I-13 DIRECTIONS ET PARALLÉLISMES (quand il y a beaucoup de grilles)
- **Statut** : OUVERTE (liée à I-01). En allsib (DÉRIVÉ) : toute droite extérieure utilise 6 blocs ; sa « direction » = bloc manquant ; les 5 droites
  extérieures par α ont les 5 directions hors supp(α) ; pour chaque k, les 60 racines évitant k sont partitionnées en 20 triangles.
  Structure de « résolution » ; la contradiction à m = 7 serait une non-existence de design résoluble.

## I-14 RÉ-ENRACINEMENT (deux centres c, c' reliés par t)
- **Statut** : OUVERTE (basse). La boule autour de c est envoyée sur la boule autour de c' par t : isomorphisme entre deux identifications F₃⁷.

## I-15 ENSEMBLES INTRIGANTS / m-OVOÏDES DANS LE QUADRANGLE PARTIEL
- **Statut** : OUVERTE (basse). Chercher un ensemble naturel (défini par D ou σ) dont l'indicatrice est dans un espace propre + constante.

## I-16 RELAXATION RÉELLE ET INVARIANTS ARITHMÉTIQUES (microscope)
- **Statut** : OUVERTE. Les matrices réelles satisfaisant les identités spectrales : leurs invariants (rang mod p après arrondi ?) — basse.

## I-27 INVARIANT « APRÈS LE RANG » À p = 2 (transfert du mécanisme C3)
- **Statut** : RÉFUTÉE comme obstruction (N09) ; sous-produit DÉRIVÉ gardé. **Origine** : lecture du dépôt C3 expérimental (non indépendante).
- **Langage** : Z₂[C₂]-modules libres, formes Z/4, invariants de Brown, formule de Milgram / de l'oddité.
- **Différence** : première attaque qui compare les deux spécialisations (Q ↔ S) au-delà du rang F₂ (I-09 s'arrêtait au mod 2).
- **Résultat** : l'analogue exact donne ρ₊ + ρ₋ pair ; c'est équivalent à Milgram pour N₃ (indépendant de σ). Les caractères rationnels
  rendent le mécanisme vide pour une involution. Sous-produit : rang₇(A − 3I) impair, D₇(N₃) de type moins (`notes/09_…`).
- **Décision** : ABANDONNÉE pour C2. Pistes dérivées (basses) : classe du réseau √77·N₃* (séries thêta de niveau 77) ; sous-espaces
  isotropes forcés dans D₇(N₃) (le type moins borne leur dimension par ρ/2 − 1 ; les grilles tombent dans le radical).

## I-28 t COMME RÉFLEXION PONCTUELLE — RENORMALISATION SUR LES GRILLES (salve reset)
- **Statut** : SURVIT. Théorème R1 DÉRIVÉ ; conjecture R2 vraie dans BvLS (990/990), ouverte en C2.
- **Origine** : reset demandé par l'utilisateur ; systèmes triples de Hall (les réflexions engendrent la structure affine).
- **Langage** : réflexions ponctuelles, codes parfaits, involutions induites sur des sous-structures.
- **Différence** : t n'est plus une symétrie par laquelle on quotiente, mais un **générateur de structure affine locale**. Les grilles ne
  sont plus comptées : on les regarde se transformer.
- **Upside** : si R2 est vraie et se propage (grilles hors de x ⇒ grilles par x ⇒ …), la structure de Hamming serait forcée de proche en
  proche, jusqu'à une contradiction avec 99 ≠ 3^k.
- **Résultats** :
  - R1 : une grille hors de x est disjointe de son image, avec un couplage parfait π et une involution φ à point fixe unique en
    w ∈ N(x) ; les étiquettes sont partitionnées ; φ fixe le type D.
  - Dans le cas des droites sœurs : **R2 ⟺ {1,j}, {1,k} ∈ Σ** (la propagation de grille, question E7 du labo).
  - « Translation locale partout » (ρᵢ = t∘ι_{eᵢ}) implique allsib : impossible.
- **Décision** : poursuivre. Il faut une preuve de R2, ou un test long quand la machine est libre.
- **Mise à jour (24/09, note 15)** :
  - R2 **complète** est FAUSSE dès qu'une droite de Λ en w est sœur (théorème 15.3) ; elle n'est possible qu'en T3 (quatre blocs), avec
    un motif rigide des coins ;
  - R2 « sur les droites » n'est pas forcée localement (1194 types locaux) ;
  - le chemin R2 ⇒ ρ_w automorphe est bloqué : R2 complète ⇒ σ_w ∉ Aut ;
  - statut : AFFAIBLIE (plus de preuve locale possible) ; reste un dictionnaire entre les grilles et le programme Δ.

## I-29 COMPLEXE X_Γ (triangles + carrés μ) LOCALEMENT ISOMORPHE À CELUI DE H(7,3)
- **Statut** : OUVERTE. Faits DÉRIVÉS : liens identiques (K₁₄ bicolore) ; points fixes de t = étoile de x + 21 centres de carrés D ;
  Lefschetz ; χ(X/t) = 869.
- **Idée** : non-existence ⟺ la courbure 2n₃ = Σ(4 − c) ne se répartit pas de façon cohérente. Un relevé en H(7,3) est impossible, car
  99 ne divise pas 3⁷.
- **Test** : H₁(X; Z) sur Paley(9) et BvLS (attendu : 0 et Z₃⁶).

## I-30 PROGRAMME DE HALL : C2 = « Hall en un seul point » ; lemme de propagation (salve reset, note 14)
- **Statut** : OUVERTE, et mieux posée : la cible est identifiée, pas atteinte.
- **Origine** : Hall 1960 (systèmes triples de Hall) et Bondarenko–Radchenko 2013 (JCTB 103), trouvés par la recherche en profondeur.
- **Objet** : les réflexions ponctuelles σ_v, définies en tout sommet (diamètre 2, λ = 1, μ = 2). C2 ⟺ σ_x ∈ Aut. Au plus une σ_v est
  automorphe (|Aut| ≤ 3).
- **Lemme manquant (P)** : σ_x ∈ Aut ⇒ σ_w ∈ Aut pour un w ≠ x. Équivalent à la mort de C2.
  - Chez BR, l'étape correspondante marche parce que N(v) est une base propre (g = k).
  - Ici le 1-voisinage est de rang 14 sur 44 ; le résidu de dimension 30 est l'inconnue (la matrice de l'étage S sous un autre angle).
- **Défauts de Hall mesurés en x (DÉRIVÉ)** :
  - (H1) σ_v(x) = σ_x(v) ⟺ v est un coin sib : 4n_sib ≤ 28 racines sur 84 ;
  - (H2) au plus 28 orbites de droites D-fermantes sur 42 ;
  - (H3) multiplicité des milieux : moyenne 1 + J/1386 sur les paires adjacentes, 1 − J/8316 sur les autres ;
  - (H4) J_x = #{v = p+q : M_p(q) = M_q(p)} ;
  - (H5) R2 = translation locale sur les grilles.
- **Lecture** : |Σ| ≤ 7 (certifié) dit « loin de Hall autour de x ». Une preuve doit rendre incompatibles « Hall en x » et « loin de
  Hall autour de x ».
- **Tests** :
  - (P_grille) = R2, budget long ;
  - (P_J) : la configuration à 7 points, forcée ou interdite ?
  - (P_rés) : SDP du résidu de dimension 30 avec la symétrie t.

## I-31 RELAXATIONS DE MOMENTS SYMÉTRISÉES (note 16)
- **Statut** : OUVERTE ; outil construit et validé.
- **Outil** : orbites de W(B_m), représentation régulière de l'algèbre commutante, contraintes multipliées.
- **Résultats** :
  - degré 2 : réalisable (N19) ;
  - degré 3 sur les triangles : réalisable à m = 7, et même pour allsib (N20).
- **Test d'étalonnage** : trouver le plus petit cran qui réfute allsib (Sherali-Adams 3 local, Lasserre 2 localisé). La preuve DRAT
  d'allsib existe : son analyse dirait le degré réellement utilisé.
- **Coût** : les crans suivants demandent le comptage des orbites de quadruplets et un SDP plus gros. C'est ici que le matériel
  compte.

## I-32 COCYCLES DE RECOLLEMENT ET COHOMOLOGIE (note 17) — le patron local → global
- **Statut** : SURVIT. Il tue allsib par une preuve humaine.
- **Mécanisme** : rigidité locale (grilles-codes parfaits) ⇒ donnée de recollement Z₂ (échange des t-orbites) ⇒ cocycle (λ/μ) ⇒
  cobord (H¹(M₇ ; Z₂) = 0) ⇒ contradiction avec une équirépartition 3/3 (μ entre paires qui se coupent).
- **Prochaines cibles** :
  - les configurations Σ certifiées (K2+K2+P3, K3+K3…) ;
  - le cocycle à défauts construit sur les carrés D one/dis ;
  - le cœur sans grille.

## I-33 PARITÉ DES CONNEXIONS : au-delà du lemme des étoiles (note 19)
- Le lemme des étoiles est la première obstruction de parité **indépendante de χ** : une combinaison de Faits A et B.
- Piste 1. Chercher des combinaisons analogues impliquant des lignes non sœurs. Au sommet e_c, la bijection μ entre racines évitant c
  et arêtes de K₁₂ − A_c est générale. Il faudrait un analogue du Fait A là où S1 échoue, avec des « termes de défaut » : les racines
  ±w₀, et les racines à ν = 0.
- Piste 2. Donner aux solveurs le certificat sous forme linéaire. Il faut ajouter des variables Z_p(W) = b[U_p⁺,W] ⊕ b[U_p⁻,W], puis les
  équations (L1) et (L2) sur ces variables : Gauss conclut alors instantanément. À généraliser en variables de « côté » pour les
  carrés one.
- Pour les 12 survivants de degré ≤ 2, la parité des lignes sœurs est cohérente (`logs/parity_classify.txt`). Une parité mixte
  lignes sœurs / lignes non sœurs est le candidat naturel.
- **Formulation universelle au sommet e_c** (valable pour toute configuration, grille ou non) :
  - la bijection μ E : avoid(c) → arêtes de K₁₂ − A_c ;
  - le Fait A universel, #{w ∋ +e_ℓ, g ∈ E(w)} = 2 − [A_c(g) ∋ +e_ℓ] − [B_c(g) ∋ +e_ℓ], avec 1 − … si ℓ est l'autre bloc de g ;
  - le Fait B universel : chaque arête de K₁₂ − A_c porte exactement une racine ;
  - l'involution π : E(w) ↦ E(−w) sur les 60 arêtes, sans point fixe.

  Le lemme des étoiles est le cas où trois arêtes de A_c sont des arêtes D sib. Pour les arêtes D one, les défauts rendent les
  comptes impairs (par exemple 1 + 2 = 3), et les étoiles mixtes sont SAT. Une obstruction sans grille devra combiner **toutes** les
  étoiles star(c), c = 1..7, avec un comptage global des types D (piste « cohomologique », comme H¹(M₇) pour allsib).
- **Transfert possible** (à décider par l'utilisateur, hors du labo) : « deg Σ ≤ 2 » et « |Σ| ≤ 4 » sont des cardinalités valides sur
  les variables Y de l'étage Q du dépôt principal, et elles manquent à l'étage Q. Le lemme des étoiles utilise les signes.

## I-34 FINIR LES SURVIVANTS Σ PAR LE MODÈLE COMPLET, DU PLUS RICHE AU PLUS PAUVRE (note 19 §11)
- **C₄ tué** en 495 s (DRAT) dans le modèle complet, alors que toutes les sondes locales échouaient. Le solveur global exploite les
  lignes non sœurs.
- **Ordre** : 4 arêtes en sémantique « au moins », puis 3 arêtes en sémantique exacte (Σ = H, les autres paires interdites sœurs),
  puis 2 arêtes (P₃, 2K₂), puis K₂.
- **K₂ exact est le cas sib du dépôt principal**, réduit par nos résultats : aucune autre paire sœur, et donc une seule grille par x.
  Pour ce cas-là, il faudra un découpage en cubes, piloté par la structure autour de la grille (partition équitable à 18 cellules,
  note 04).
- Σ = ∅ reste le cœur.

## I-35 PROPAGATEUR DE PARITÉ À COEFFICIENTS VARIABLES (note 19 §10)
- **Constat.** Sur BvLS, les parités de (I) et des (P) « cross » forment, à Q fixé, un système linéaire L(Q) de rang plein en les
  signes : 8415 équations, 990 signes, rang 990. Les signes sont déterminés par Q, et la cohérence de L(Q) impose des milliers de conditions
  linéaires sur le second membre b(Q), qui dépend de Q.
- **Obstacle.** Dans CNF + XOR, les coefficients de L dépendent des variables de Q. L'élimination de Gauss ne s'applique qu'une fois Q
  fixé, c'est pourquoi CryptoMiniSat n'a rien gagné, sur K₁,₃ comme sur star(1).
- **Idée d'ingénierie** (hors session, pour la machine prêtée ou le dépôt principal) : un propagateur DPLL(T) qui, à chaque nœud
  partiellement assigné en Q, tient à jour l'élimination de Gauss des équations de L dont le support est déjà fixé, et coupe dès
  qu'elles sont incohérentes. C'est la généralisation mécanique de ce qui a trouvé le lemme des étoiles : réfuter chaque χ par parité,
  puis sommer.
