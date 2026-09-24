# 13 — Nouveaux objets auxiliaires C2 (salve « reset », 24/09/2026)

Aucun de ces objets n'est présent dans l'architecture précédente (étages Q/S, D, Σ, réseaux ±). Chacun vient avec ce qui est **démontré**
à son sujet (DÉRIVÉ) et ce qui reste conjectural.

## O1. Paires de grilles induites par t : (Λ, tΛ, π, φ) (note 11)
DÉRIVÉ (théorème R1) :
- une grille hors de x est disjointe de son image ;
- les arêtes entre Λ et tΛ forment un couplage parfait π ;
- φ = t∘π est une involution de Λ de point fixe unique w ∈ N(x) ;
- D(u) ∩ Λ = {φ(u)} si φ(u) ~ u, et ∅ sinon ;
- les 12 demi-étiquettes des autres blocs sont partitionnées entre les racines de Λ.

La valeur de φ fixe le type de carré D :
- si φ(α) = β (même droite par w) : type sib ou one ;
- si φ(α) est un coin colinéaire à α : type dis ;
- sinon : partenaire D hors de Λ ∪ tΛ.

Conjecture R2 : φ est la réflexion ponctuelle (vraie dans BvLS, 990/990 ; en C2, test court TIMEOUT).

## O2. Le 2-complexe X_Γ (triangles = droites, carrés = carrés μ)
DÉRIVÉ :
- **Structure** : 99 sommets, 693 arêtes, 231 triangles, 2079 carrés ; χ(X) = 1716.
- **Liens** : le lien de chaque sommet est K₁₄, avec ses arêtes colorées « triangle » (7K₂) et « carré » (le graphe cocktail CP(7)).
  **C'est exactement le lien du complexe de Hamming H(7,3)** : X_Γ est localement isomorphe au complexe triangles + carrés de H(7,3).
- **Points fixes de t** : l'étoile de x (7 médianes des triangles {x, eᵢ, −eᵢ}), plus **les 21 centres des carrés D**. En effet, t tourne
  chaque carré D d'un demi-tour, et les carrés D sont les seuls carrés t-invariants. On a χ(X^t) = 22.
- **Formules de Lefschetz et de Riemann–Hurwitz** : tr(t | H₂(X;Q)) − tr(t | H₁(X;Q)) = 21 et χ(X/t) = (1716 + 22)/2 = 869.
  Vérification au niveau des chaînes : tr(t | C₀, C₁, C₂) = 1, −7, 14.
- **Reformulation** (à consolider avec la littérature, recherche en cours) : si tous les coins se ferment (n₃ = 0), le complexe complété
  par les cellules produits se relève en celui de H(7,3), donc 99 divise 3⁷ : absurde. **La non-existence équivaut à dire que la courbure
  2n₃ = Σ(4 − c) ne peut pas être répartie de façon cohérente.** En C2, la courbure en x vaut au moins 28.

## O3. Négations de carte ι_y et translations locales ρᵢ = t∘ι_{eᵢ}
- ι_y : bijection de V qui envoie chaque sommet sur celui de coordonnées opposées dans la carte en y. On a ι_x = t (un automorphisme) ;
  les autres ne sont pas des automorphismes a priori, et t ι_y t = ι_{ty}.
- ρ₁ = t∘ι_{e₁} parcourt la droite {x, e₁, −e₁} : x → e₁ → −e₁ → x. Il envoie les demi-étiquettes intérieures des autres blocs sur R⁺
  (racines contenant e₁), R⁺ sur R⁻, et R⁻ sur les demi-étiquettes.
- En demi-étiquettes, on pose κ = −M₁ (négation composée avec le couplage local en e₁) et ω = appariement parfait R⁻ → R⁺, où l'unique
  voisin de −e₁ + h contenant e₁ est e₁ + ω(h). Alors ρ₁³ restreint aux demi-étiquettes vaut κωκωκ.
- DÉRIVÉ :
  1. νων = ω⁻¹ (ν = négation).
  2. Les points fixes de ω sont les h dont le couplage M_h contient la paire sœur du bloc 1 (arcs → 1 du digraphe des sœurs).
  3. **ρ₁ déplace chaque racine de R⁺ le long d'une arête ⟺ ω⁻¹ = κ ⟺ les 6 paires de M_{e₁} sont « D-fermantes »** : chaque droite de
     M_{e₁} se ferme en un carré D.
  4. **Il est impossible que ce soit vrai pour les 7 blocs.** Il y aurait alors 42 paires D-fermantes = 2n_sib + n_one, d'où n_sib = 21,
     soit le cas allsib, certifié impossible.
- Lien avec R2 : R2 ⟺ ρ_w déplace chaque point de Λ le long d'une arête ; c'est une propriété de « translation locale » sur les grilles
  seulement.

## O4. Algèbre de Norton graduée
DÉRIVÉ :
- **Forme cubique** : la forme cubique F_θ(w) = Σ_z w(z)³ **s'annule identiquement sur V_θ⁻** (t impose F(tw) = F(w) et tw = −w).
- **Terme croisé** : Σ u²w = 0 pour u ∈ V⁺ et w ∈ V⁻. La forme cubique se réduit à F(u+w) = F(u) + 3Σ u w².
- **Traces graduées** : les traces ⟨E_i^a ∘ E_j^b, E_k^c⟩ ne dépendent que de (n₀, n₁, n₂) = (1, 14, 84). Elles sont toutes ≥ 0 : pas
  d'obstruction (`scripts/graded_krein.py`).
- Piste ouverte : l'application quadratique V⁻ → V⁺, w ↦ E_θ(w∘w), et ses rangs.

## O5. Côtés D et droites extérieures
DÉRIVÉ :
- chaque droite extérieure porte **au plus un** côté de carré D (deux côtés partageant un sommet u forceraient u′ ~ tu′) ;
- #{droites extérieures portant un côté D} = 2n_one + 4n_dis ≤ 140 ;
- les troisièmes points des côtés d'un carré D forment deux t-orbites : 4 sommets intérieurs pour sib, 2 intérieurs et 2 extérieurs pour
  one, 4 extérieurs pour dis.

## O6. Cocliques de Delsarte (égalité de Hoffman, taille 22)
DÉRIVÉ : **aucune 22-coclique de Delsarte n'est t-invariante.**
- Si x ∉ C, x a exactement 4 voisins dans C, t-stables, donc deux blocs {eᵢ, −eᵢ}, qui sont des arêtes : contradiction.
- Si x ∈ C, il reste 21 points à répartir en t-orbites de taille 2 : impossible.

Les éventuelles cocliques de Delsarte vont donc par paires (C, tC).

## O7. Orbifold quotient Π = Γ/t
50 points (x, 7 orbites intérieures, 42 extérieures). Droites : 7 « demi-droites » de taille 2 par x, et 112 droites de taille 3.
Défaut : 21 paires de points doublement colinéaires (les paires D). Un quadrangle partiel à 21 défauts ; son 2-complexe est X/t
(χ = 869, avec 22 points coniques).

## O8. Code ternaire des droites et réseau des syzygies
- N : matrice d'incidence points × droites (99 × 231) ; NNᵀ = A + 7I (inversible), donc rang N = 99, et ker N est de rang 132.
- DÉRIVÉ : **K_L = ker N ∩ Z²³¹ est pair.** Si Nw = 0, en sommant sur les points, 3Σw_ℓ = 0, donc Σw_ℓ = 0 et Σw_ℓ² ≡ 0 (mod 2).
- Chaque grille donne le vecteur (lignes) − (colonnes) de norme 6 dans K_L ; t agit sur K_L en fixant 7 droites.
- Pistes :
  - déterminant de K_L via NNᵀ (premiers 2, 3, 5, 7) ;
  - densité de vecteurs de norme 6 ;
  - code ternaire span_F₃(droites), avec 3 | taille des droites : chaque droite est isotrope.
