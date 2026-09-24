# Défauts de domination des carrés D (lemme de Wilbrink–Brouwer) — DÉRIVÉ

Lemme (Wilbrink–Brouwer ; utilisé par Lou–Murin 2014, Azarija–Marc 2018) : pour un sous-graphe **induit** H (N sommets, M arêtes, degrés dᵢ) d'un
srg(n,k,λ,μ), avec x_j = #{sommets hors de H ayant j voisins dans H} :
  Σ_j C(j−1,2) x_j = x₀ + x₃ + 3x₄ + 6x₅ + … = (n−N) − (kN − 2M) + λM + μ(C(N,2) − M) − Σᵢ C(dᵢ,2)   (« défaut » de H).

Pour une orbite U (racine α) et son partenaire D(U) (racine β), soit H_U = {x} ∪ {sommets intérieurs des blocs de α et β} ∪ {±α, ±β}
(sous-graphe σ-invariant, arêtes toutes forcées sauf le carré D, donc induit connu) :

| type de D(U) | H_U | N | M | Σ C(dᵢ,2) | défaut |
|---|---|---|---|---|---|
| sib (β sœur) | {x, ±eᵢ, ±eⱼ, P_ij} = grille | 9 | 18 | 54 | **0** (code parfait, théorème G1) |
| one (α = e₁+e₂, β = e₁+e₃) | {x, ±e₁, ±e₂, ±e₃, ±α, ±β} | 11 | 21 | 63 | **2** |
| dis (α = e₁+e₂, β = e₃+e₄) | {x, ±e₁…±e₄, ±α, ±β} | 13 | 24 | 76 | **8** |

Conséquences (σ-invariance : les sommets hors de H_U vont par paires σ, donc x_j pair) :
- **one** : (x₀, x₃) ∈ {(2,0), (0,2)}, x_{≥4} = 0 : exactement une paire σ de sommets « spéciaux » — soit deux racines sur les 4 autres blocs non
  adjacentes au carré D, soit deux sommets ayant 3 voisins dans H_U ; tous les autres ont 1 ou 2 voisins dans H_U.
- **dis** : x₀ + x₃ + 3x₄ = 8 avec x₀, x₃, x₄ pairs.
- **sib** : aucun sommet spécial (tout sommet extérieur a exactement un voisin dans la grille).

Statut : conséquences locales exactes du modèle (donc « redondantes » au sens du dépôt) mais elles donnent un **langage de défauts** : sib = défaut 0
(rigide, et le théorème certifié montre que les grilles par x sont rares) ; les cas one/dis ont des défauts 2 et 8 qui localisent les écarts à la
structure de Hamming. Piste : un comptage global de ces paires spéciales (sur les 21 carrés D) pourrait donner une identité ou une inégalité nouvelle.
