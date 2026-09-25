# 29 — Le cœur de C2 : formulation commune, identités exactes, et ce qui reste (26/09/2026)

**Statut.** Formulation et identités, toutes DÉRIVÉES à la main. Aucune contradiction ici : c'est la base de travail commune avec
« structures » et C1.

## 1. Définition
Le **cœur** regroupe les configurations en Σ = ∅ où, en tout bloc c, **G_c est connexe** (type (6)). Dans le cœur :
- l'équilibre (24.0) est vide ;
- les profils (27.1) se réduisent aux totaux (C6, C8) et à F1 ;
- les budgets 18.x ne saturent pas ;
- les réseaux sont vides (N09, N24).

Exemples :
- le tout-tordu sans triangle ou à un seul triangle, dont (7,7,7) ;
- **H-β** : T hamiltonien ; en chaque bloc, le chemin D passe par les deux paires ancrées ; le graphe D est un seul 21-cycle.

## 2. Structure exacte du budget des doubles (tout-tordu pur ; les mélanges s'y ramènent)
- **Par paire P′.** Chaque paire est « doublée » (φ = 2) par exactement 2 orbites (16.1 : un partenaire D a φ = 2, via F1).
  - Parmi les 20 orbites lointaines de P′, on a Σ_x φ_x(P′) = 16 (4 étiquettes × 8 voisins lointains, divisé par 2). Donc
    #doubles − #zéros = −4.
  - En tout-tordu pur, une paire tordue n'a aucun double proche. On a donc **exactement 2 doubles, 6 zéros et 12 simples** par
    paire.
  - Avec des paires ancrées, il y a au plus 1 double proche par paire ancrée, soit 5 ou 6 zéros.
- **Par orbite x = (i, j, k).** Sur ses 10 paires lointaines, Σφ = 8, donc **#zéros − #doubles = 2**.
  - Le lemme D donne, sur R_x : doubles_R − zéros_R = n_k.
  - Sur les paires y : Σ_r y_r = 2 − n_k sur 4 paires.
- Ces deux vues sont cohérentes : Σ_x (zéros − doubles) = 84 = 21 × 4. Elles ne mordent qu'avec des doubles **forcés et
  localisés**, ce qui manque dans le cœur (aucun triangle ni cycle fermé).

## 3. L'objet local du cœur : le problème de l'étoile libre, en forme matricielle
Bloc c ; X = les 12 vecteurs signés des autres blocs ; σ = −1 ; μ, τ = les couplages en e_c. Dans le cœur « un bloc », μ et τ n'ont
aucune σ-paire (n_s = 0).
- **Φ est une bijection** de E(K₁₂ − σ) (les 60 racines lointaines z = {a, a′}) vers E(K₁₂ − μ) (les paires non μ).
- On note R (60 × 12) l'incidence racine–vecteur, et W = P_Φ W₀ l'incidence image–vecteur. Alors :
  - RᵀR = J + 9I − P_σ ;
  - WᵀW = J + 9I − P_μ ;
  - **RᵀW = 2J − I − P_σ − P_μ − P_{τσ}**, soit (ii) sous forme matricielle ;
  - **WᵀΠW = C_t**, soit (iii), où Π : z ↦ σz et RᵀΠ = P_σRᵀ.
- **Positivité.** Le Gram de [R | W | ΠW] est ⪰ 0 pour les 2 903 types (note 23 §2). Ce n'est pas une obstruction.
- **Ombre mod 2.** Pour tout S ⊂ X, l'ensemble Φ⁻¹(δ_cible S) a pour sommets de degré impair exactement
  (I + P_σ + P_μ + P_{τσ})·1_S (mod 2).
- **Faces.** G_a = Φ(étoile de a) a 10 arêtes. Ses degrés sont : 1 en a, σa, μa et τσa (génériquement), 2 ailleurs. C'est donc
  deux chemins plus des cycles.
  - Chaque paire non μ est dans exactement deux faces, celles des deux vecteurs de sa racine.
  - (iv) (note 23 §6) : κ = Φ∘σ∘Φ⁻¹ envoie deux arêtes adjacentes de G_a sur deux arêtes disjointes de G_{−a} = κ(G_a).

## 4. H-β : structure exacte
- T = Z₇ ; les cordes sont orientées de façon eulérienne (2 entrants, 2 sortants en chaque bloc).
- En c, le chemin P_c – {c,X_c} – {c,Y_c} – P_{c+1} passe par In(c) = {X_c, Y_c}.
- **La réunion « couplage D ∪ couplage sœurs » sur les 42 orbites est un seul 42-cycle** (le graphe D sur les paires est un
  21-cycle).
- En chaque bloc, les 6 orbites libres (Out(c) × 2, plus deux libres tordues) forment un seul 6-cycle libre.
- Toutes les identités locales sont satisfaites avec du jeu.

## 5. Leviers globaux candidats (à discuter avec les pairs)
- (a) **Topologie de l'étoile libre.** Recoller les faces G_a en pseudo-surface ; chercher une contradiction d'Euler ou
  d'orientabilité (piste de la note 23, jamais exploitée).
- (b) **Parité ou cohomologie** sur les cycles libres et les torsions, sur le patron de la note 17. Le produit des signes S le long
  de chaque cycle libre vaut (−1)^{L/2}. Le produit global vaut −1 automatiquement : il faudrait une seconde expression de ce
  produit.
- (c) **Rang 7-adique.** Les sous-matrices principales entièrement connues de S − 3I sont les étoiles plus les intérieurs, soit
  19 × 19, sous le plafond 22. Il faudrait des mineurs non principaux partiellement connus : c'est le programme de C1.
- (d) **Réflexions σ_v** (note 14). C2 ⟺ σ_x ∈ Aut ; ρ_c = σ_x σ_{e_c} est inversé par σ_x. Le lemme de propagation (P) reste le
  plus direct, et le plus dur.
