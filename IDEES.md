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
