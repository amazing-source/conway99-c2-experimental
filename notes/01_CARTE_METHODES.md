# Carte des méthodes déjà essayées sur C2 (et ce qu'elles ne voyaient pas)

| Méthode | Formulation précise | Résultat | Ce qu'elle *n'utilise pas* (angle mort) |
|---|---|---|---|
| Programme de symétrie (littérature) | matrices d'orbites p = 3,5,7,11 | exclut tout sauf \|Aut\| ∈ {1,2,3} ; p = 2 jamais calculé | — |
| Rigidité | Makhnev + λ=1 | t = σ, D couplage | — |
| SAT (CNF seqcounter) modèle complet | 666 183 var / 1,51 M clauses | 7 × 8 h UNKNOWN | arithmétique globale (spectre, rangs), symétrie |
| SAT Stage Q | 1,2 M var / 2,5 M clauses | 3 × 2 h UNKNOWN | les signes ; la structure non linéaire |
| CP-SAT | même modèle | UNKNOWN | idem |
| Cubes (ligne de U₀) | 13/149/1164 cubes | sib : 3 × 20 min UNKNOWN | — |
| DFS ligne par ligne | bornes Gram | plafond de nœuds | — |
| Recuit | bit-flip / structuré | plateau ≈ 1550 | — |
| Générateur spectral (phase 2, `psd_gen.py`) | filtres d'entrelacement PSD sur 4 projecteurs | sain sur BvLS m=11 (domaines réduits à partir de la ligne ~15, forcés après ~35) ; jamais lancé comme recherche à m=7 | — |
| mod 2 | rang_F2(S)=27, rang(Γ̄+Sh)=20, LCD | filtres | la *forme quadratique* mod 2 (Arf), les poids |
| 2-adique | Z₂[C₂]-réseaux libres (Broué) | ⇔ rang 27 | — |
| mod 3 | rang 22, M idempotent rang 27 | filtres | — |
| Smith Z₂, Z₃ | triviales | épuisé pour S | — |
| **7-adique** | (S−3I)² = −7(S−3I) | **jamais étudié** (q:7) | tout |
| Ishida (trace-rang) | sur sommets, arêtes, triangles, quadrilatères | a₁=14 seulement ; identités triviales | modules plus riches (Terwilliger, paires) |
| Fourier/Z₈ (phase 2) | exactitude ⇔ S²+S−12I ≡ 0 mod 8 étant donné Q | critère, pas d'obstruction | — |
| s=1/s=0 (phase 2) | types de M_c, triangles | comptes ; allsib UNSAT 33 s (non certifié) | la structure géométrique (grilles, directions) |
| « Kneser 2-lift » | n₀ ∈ {8,9,10} | aucune identité | — |
| LP/SDP degré 2 | jugé inutile (non lancé) | — | contraintes de degré 4, multi-points |
| Recensement ordre 7 | 208 formules | rien sur n₃ ; parité suggérée (q:parite) | — |

## Domaines ABSENTS de tous les fichiers C2 (candidats pour la divergence)
- Le système de racines D₇ / le réseau Z⁷ (les 99 sommets = vecteurs de norme ≤ 2 de Z⁷ ; σ = −1). *Non trouvé dans les fichiers C2.*
- Le point de vue « boule de Hamming de rayon 2 dans F₃⁷ » et les codes parfaits (BvLS = graphe de cosets du code de Golay ternaire).
- Les réseaux entiers de Gram S+4I (rang 27) et 3I−S (rang 22) : trames serrées entières, 7-élémentaires.
- Géométrie d'incidence : grilles 3×3, quadrangles partiels PQ(2,6,2), complexe triangles+carrés.
- Systèmes de transitions / circuits eulériens (structure s=1 sur le graphe cocktail CP(7)).
- Algèbre de Terwilliger + involution ; configurations cohérentes à deux points.
- Formes quadratiques sur F₂ (invariant d'Arf) au-delà du rang.
- Méthodes « Lloyd » (codes parfaits), équipartitions / couleurs parfaites, revêtements.
