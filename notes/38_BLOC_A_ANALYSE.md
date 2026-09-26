# 38 — Le bloc A (degré 6) : où se trouve la contradiction (26/09/2026, travail mathématique, tests minuscules)

Demande de l'utilisateur : accélérer le calcul, ou le remplacer par des mathématiques, sans arrêter les processus en cours.

## 1. La seule configuration survivante de M1 n = 3
Après le filtre à bloc A générique, M1 n = 3 se réduit à **une** configuration, invariante par (0 1 2)(3 4 5) :
- T = triangle tordu {0,1,2} ;
- In(0) = {3,4}, In(1) = {4,5}, In(2) = {3,5}, chacun avec un chemin β ;
- blocs 3, 4, 5 de degré 2, avec structures liées : In(3) = {1,4}, In(4) = {2,5}, In(5) = {0,3} ;
- A = 6.

Les queues vérifient f = 8, ce qui est compatible avec 28.5.

## 2. Où est la contradiction (PL de sondage, quelques secondes chacun ; guides, pas des preuves)
- **Premier ordre** (S, PPE, couplage, lignes locales), A variable : faisable. Le second ordre est donc nécessaire.
- **Toutes les lignes (P2)** : écart 56.

| sous-famille de lignes (P2) gardées | lignes | écart |
|---|---|---|
| paires partageant un bloc | 105 | 23,8 |
| paires disjointes | 105 | 29,7 |
| **les deux paires contiennent A** | **15** | **0,78** |
| au moins une paire contient A | 105 | 3,5 |
| aucune paire ne contient A | 105 | 29,7 |
| paires dans T ∪ {A} | 15 | 0 |

**Lecture.** Les **15 identités entre paires {A,x} et {A,y}** suffisent, avec les lignes linéaires.
- Pour une orbite Z hors A, on pose a_Z(x) = φ_Z({A,x}). Ces identités s'écrivent

  **Σ_Z a_Z a_Zᵀ = 12I + 12J − 2D_A**, et Σ_Z a_Z = 20·𝟏,

  où D_A est la matrice d'adjacence (multi) du graphe D en A. Les orbites de A n'apportent que des constantes.
- Contrôles automatiques (ils tiennent tous) :
  - Σ_Z (Σ_x a_Z(x))² = 480 ;
  - pour tout cycle B de D_A, Σ_Z (Σ_{x∈B} a_Z(x))² = 12|B|² + 8|B|, identique à la somme imposée par l'équilibre en A.

## 3. Le système local de A seul ne suffit pas (résultat NÉGATIF, `scripts/A_local_lemma.py`)
- **Inconnues** : les 30 vecteurs a_Z ∈ {0,1,2}⁶.
- **Contraintes**, toutes démontrées :
  - Σ_x a_Z(x) = 4 (μ = 2 en (A,±)) ;
  - a_Z(pivot) = 0 (F1) ;
  - Σ_{Z∋x} a_Z(x) = 4 (les deux sœurs A libres en x ont 2 voisins chacune) ;
  - au plus un Z avec a_Z(x) = 2 (19.1) ;
  - équilibre en A sur les cycles de D_A ;
  - l'identité de Gram ci-dessus.
- **Résultat** : **faisable** pour les 4 types de D_A (6-cycle, 4 + 2, 3 + 3, 2 + 2 + 2), en quelques secondes.
- **Il n'y a donc pas de lemme universel « aucun bloc de degré 6 » à partir de A seul.** La contradiction de n = 3 couple les identités
  de A avec le reste de la configuration : cycles libres des autres blocs, structures liées en 3, 4 et 5.

## 4. Conséquence pour l'accélération
- Le coût des familles à A vient du branchement sur la structure de A. Une piste saine :
  - énumérer seulement la **partition de A en cycles** (41 cas au lieu de 130 structures) ;
  - imposer l'équilibre en A comme **filtre exact de colonnes** (valable dès que la partition est fixée) ;
  - ajouter en priorité les identités (P2) des paires {A,x}, {A,y}.
- Aucun calcul en cours n'est modifié.
