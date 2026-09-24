# Lemme S1 — une paire sœur est un « code parfait » local, exactement à m = 7

## Cadre (langage des racines, DÉRIVÉ)
Γ enraciné en x, N(x) = mK₂. Sommet intérieur (i,s) ↔ vecteur (−1)^s eᵢ ∈ Z^m ; sommet extérieur {(i,s),(j,t)} ↔ racine (−1)^s eᵢ + (−1)^t eⱼ de D_m ;
σ = −1. Pour une paire de blocs p = {i,j}, P_p = {±eᵢ±eⱼ} (4 racines = deux orbites sœurs). Deux racines de P_p non opposées sont **sœurs**.
La paire p est **sœur (sib)** si les deux orbites de P_p sont partenaires par D, i.e. chaque α ∈ P_p est adjacente à ses deux sœurs
(⇔ les deux droites de x en blocs i, j engendrent une grille 3×3).

## Énoncé (DÉRIVÉ, preuve ci-dessous ; vérifié numériquement sur BvLS m = 11 : `logs/sib_partition_check.log`)
Si p est sœur, alors pour α ∈ P_p : N_H(α) = {deux sœurs} ⊔ N₀(α) où
1. N₀(α) évite les blocs i et j, |N₀(α)| = 2(m−2) ;
2. les quatre ensembles N₀(α), α ∈ P_p, sont deux à deux disjoints ;
3. donc ils couvrent 8(m−2) des 4·C(m−2,2) racines évitant i, j : **partition ⇔ 2(m−2) = C(m−2,2) ⇔ m ∈ {2, 7}** ; à m = 11 : exactement la moitié.
4. (m = 7) Chaque racine β évitant p est adjacente à **exactement une** racine c_p(β) ∈ P_p, et c_p(−β) = −c_p(β).
5. (m = 7) H induit sur les 40 racines évitant p un graphe 5-régulier ; la partition en 4 classes N₀(α) est **équitable** de matrice quotient
   [[1,1,1,2],[1,1,2,1],[1,2,1,1],[2,1,1,1]] (ordre : α, sœur, sœur, −α), valeurs propres {5, 1, −1, −1}.
6. (m = 7) Une racine β touchant exactement un des blocs i, j (disons β ∋ ε eᵢ) a exactement un voisin dans N₀(α) si α a le même signe ε sur le bloc i,
   et deux sinon (6 voisins évitant p au total).

## Preuve
(I) : parmi les voisins extérieurs de α = a eᵢ + b eⱼ, exactement un contient a eᵢ, un contient −a eᵢ, un contient b eⱼ, un contient −b eⱼ.
Les deux sœurs a eᵢ − b eⱼ et −a eᵢ + b eⱼ occupent ces quatre places ⇒ les 10 autres voisins (s = 0) évitent les blocs i, j. (1)
α et −α : voisins communs = D(α) = les deux sœurs (μ = 2) ⇒ N₀(α) ∩ N₀(−α) = ∅. α et une sœur α' (adjacentes, λ = 1) : leur voisin commun est le sommet
intérieur partagé ⇒ N₀(α) ∩ N₀(α') = ∅. (2), puis (3) par comptage, (4) par (3) et σ-équivariance.
(5) Soit β évitant p, α_c = c_p(β). λ(α_c, β) = 1 et le voisin commun n'est ni intérieur (étiquettes disjointes) ni une sœur de α_c (seul α_c ∈ P_p est
voisin de β) : il est dans N₀(α_c). Pour α' sœur de α_c : μ = 2, un voisin commun est α_c, donc exactement un dans N₀(α'). Pour −α_c : ses sœurs sont celles
de α_c, non voisines de β, donc deux voisins communs dans N₀(−α_c). Total 5, ce que confirme (I).
(6) même raisonnement avec |α ∩ β| ∈ {0,1}. ∎

## Portée
- C'est la première raison **structurelle spécifique à m = 7** trouvée dans ce laboratoire : l'égalité 2(m−2) = C(m−2,2) n'a lieu que pour m ∈ {2,7}.
  À m = 11 (BvLS, toutes les paires sœurs) la même structure est un empilement de densité 1/2, sans rigidité.
- Toute paire sœur à m = 7 est un « code parfait 1-dominant » local (4 racines dominant parfaitement le D₅ complémentaire).
- Deux paires sœurs disjointes p, q : c_p restreinte à P_q est une bijection σ-équivariante P_q → P_p **qui envoie sœurs sur sœurs** (DÉRIVÉ).
  Les 12 racines sur les 3 blocs restants se répartissent en 4 « alignées » (troisièmes points des 4 droites {α, φ⁻¹(α), ·}) et 8 « anti-alignées ».
- En allsib : les 10 voisins s=0 de chaque racine sont **exactement un par paire du K₅ complémentaire**, et ses 5 droites extérieures forment une
  **quasi-1-factorisation de K₅** ; les applications c_p forment une « connexion » à valeurs dans D₄ (groupe du carré des sœurs) sur le graphe de Kneser
  KG(7,2), avec des conditions d'holonomie sur les triangles-droites. (Piste pour une preuve humaine de « allsib impossible ».)
