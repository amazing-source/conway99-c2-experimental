# Fermeture de l’étoile A111111 (3,3)

26 septembre 2026. **Démontré**, avec deux calculs exacts indépendants du signe et contrôles sur H(2,3) et BvLS.

**Théorème.** Une involution d’un srg(99,14,1,2) ne peut avoir une droite-bloc de type A111111 (3,3). L’hypothèse P=0 n’est pas nécessaire.

Cette preuve ferme la dernière classe laissée ouverte dans ../coupures_et_torsion/PREUVE_A33.md. Elle ne ferme pas toutes les étoiles sans classe fermée et ne prouve pas l’impossibilité générale d’une involution.

## 1. Le raccord qui manquait

Le calcul précédent avait établi que l’espace V₀ des torsions équilibrées de cette étoile a dimension r₀≤1. La formule de rang de C1 imposait alors g⁻=20 et ρ=0, sans contradiction de rang.

Le nouveau raccord est un **conflit de type de forme quadratique**. Le bloc connu, de rang 14 modulo 7, est non scindé. Il ne peut se compléter en une forme hyperbolique de rang 20 en ajoutant seulement trois plans hyperboliques. Il lui faut un résidu non scindé de dimension au moins deux.

On obtient le renforcement

    g⁻ ≥ 24 − 2r₀,

au lieu du seul minorant 22−2r₀. Avec r₀≤1, cela donne g⁻≥22, contraire à g⁻≤20.

## 2. Cadre global et signe

Sur les 49 coordonnées impaires, S est entière symétrique et S²+S=12I. Poser H=3I−S modulo 7 et g=g⁻=rang H. La forme

    G = F₇⁴⁹ / ker H,   ⟨[u],[v]⟩ = uᵀHv

est non dégénérée de dimension g. C’est l’opposée de β⁻ du complément au dossier n°6. Multiplier une forme hyperbolique par −1 conserve son caractère hyperbolique.

Les résultats de genre du dossier n°6 donnent g pair, g≤20 et **G hyperbolique**. Voici le raccord de signe, pour préciser ce qui est utilisé.

Avec les représentants canoniques, soit M le nombre d’arêtes négatives dans le bloc racines×racines de S. Alors 1ᵀS1=497−4M. Les sept sommes de lignes des blocs valent 11,9,7,5,3,1,−1 : leurs carrés somment à 7 modulo 8. Les sommes de lignes des 42 racines sont paires et somment à 462−4M ; leurs carrés somment donc à 4 modulo 8. De S²+S=12I, on tire

    3 + (497−4M) ≡ 12·49 ≡ 4 (mod 8),

ce qui impose M pair.

La formule d’oddité déjà certifiée dans le dossier n°6 s’écrit

    22 + 6g + 4δ ≡ 6 + 4M (mod 8).

Elle impose g pair puis δ≡g/2 modulo 2. Par le raccord du réseau propre avec la forme β⁻, le caractère du discriminant de β⁻ est (−1)^(g/2), celui d’une forme hyperbolique en dimension g sur F₇. À g=22, la partie unimodulaire de Λ₋₄⁻ serait vide, et son déterminant 7²² forcerait le signe +1, contrairement à δ≡11. Comme g≤22 par le rang rationnel, g≤20.

Les faits de réseau et l’oddité sont les acquis de C1/structures fournis dans les dossiers ; leur application au bloc dégénéré ci-dessous est le nouveau pas.

## 3. Le bloc A33 est non scindé

Les douze étiquettes sont 0,…,11. Écrire

    σ(i)=i xor 1,
    τ=(0 5)(1 2)(3 4)(6 11)(7 8)(9 10).

L’appariement interne est μ=σ. Les six paires σ sont les autres blocs, et σ/τ forme deux cycles C₆.

Prendre les sept coordonnées des blocs et les douze orbites contenant le bloc c, représentées par (c,+)(a). Soit C la matrice 7×12 dont la ligne c vaut 1 partout, et les six autres lignes valent +1 puis −1 sur leur paire σ. Alors

    CᵀC = J + I − Pσ,

et le Gram connu H_I, sur 19 coordonnées, est

    H_I = [[4I₇, −C], [−Cᵀ, 3I₁₂−Pσ+Pτ]].

Le complément de Schur sur 4I₇ est, modulo 7,

    Q = I + Pσ + Pτ − 2J.

Sur chaque C₆, I+Pσ+Pτ a un noyau de dimension deux. L’ajout −2J tue la direction constante commune aux deux composantes ; la différence des deux constantes demeure non nulle. Donc rang Q=7, puis rang H_I=14.

Pour J₀={0,1,2,3,6,7,8}, le mineur principal de la matrice entière I+Pσ+Pτ−2J a déterminant **−5**, soit 2 modulo 7. Ainsi

    det_red H_I ≡ 4⁷·2 ≡ 1 (mod 7),

à un carré près. En dimension 14, une forme hyperbolique a discriminant de caractère χ((−1)⁷)=−1. Le discriminant de H_I étant carré, **sa partie non dégénérée est non scindée**.

Contrôle distinct : le mineur principal entier de H_I sur les sept blocs et les étiquettes J₀ vaut 3 508 800, soit 1 modulo 7. Les deux valeurs entières sont différentes parce que le Schur entier n’est pas Q ; leur comparaison n’est faite que modulo 7.

## 4. Dimension de l’image du bloc

Le noyau local de H_I a dimension cinq. Il est formé du vecteur propre universel z_c, de valeur 3 au bloc c et 1 sur les douze orbites, et des quatre torsions

    φ=(a,b,−a−b,a,b,−a−b ; d,e,−d−e,d,e,−d−e).

Pour une torsion, les coordonnées aux blocs sont 2Cφ modulo 7 et celles de l’étoile sont φ. Le vérificateur reconstruit aussi cinq vecteurs de noyau local, contrôle leur indépendance et vérifie 120 identités de couplage extérieur sur les quatre torsions et les trente orbites. La ligne extérieure d’une orbite z est nulle exactement si

    φ(Φ(z)) − φ(Φ(σz)) + 2[φ(z)−φ(σz)] = 0 (mod 7).

C’est la définition de V₀. Le vecteur universel est dans le noyau global indépendamment de Φ. Par conséquent, l’intersection du noyau global avec les vecteurs portés par I a dimension exactement 1+r₀.

L’image U des 19 coordonnées dans G a donc

    dim U = 18−r₀,
    rang de la forme sur U = 14,
    dim rad U = 4−r₀.

Cela donne le raccord de dimensions directement ; il n’est pas nécessaire de supposer séparément la formule avec ρ.

## 5. Lemme de Witt pour un bloc dégénéré

**Lemme.** Soit G une forme hyperbolique non dégénérée sur un corps fini de caractéristique impaire. Soit U⊆G, avec radical de dimension h, dont la partie non dégénérée a dimension paire r et est non scindée. Alors

    dim G ≥ r + 2h + 2.

**Preuve.** Poser R=rad U. R est totalement isotrope et U⊆R^⊥. Le quotient R^⊥/R est hyperbolique de dimension dim G−2h. U/R y est non dégénéré et non scindé. Son complément orthogonal doit lui aussi être non scindé, puisque leur somme est hyperbolique. Un complément non scindé de dimension paire ne peut avoir dimension zéro ; sa dimension est au moins deux. D’où la borne. ∎

C’est une application du découpage de Witt classique, et non un nouveau théorème général de classification des réseaux. L’avancement est le calcul du défaut de Witt du bloc A33 et son couplage avec la torsion équilibrée.

Appliquer le lemme avec r=14 et h=4−r₀ donne

    g ≥ 14 + 2(4−r₀) + 2 = 24−2r₀.

## 6. Les certificats antérieurs donnent r₀≤1

La couverture des 400 directions de P³(F₇), par le groupe de taille 72, a été vérifiée indépendamment dans ../coupures_et_torsion/verifier_A33_independant.py. Quinze certificats entiers et un domaine impossible excluent seize des dix-sept classes. Les douze directions de la dernière classe sont représentées par

    (1,2,4,1,2,4 ; 3,5,6,3,5,6).

Elles n’ont aucune coordonnée nulle. Ainsi tout φ∈V₀ non nul a φ(0)≠0. L’évaluation φ↦φ(0) est une application linéaire injective V₀→F₇. Donc r₀≤1.

Les coefficients complets, les inégalités vérifiées pour chaque choix d’ombres et les sorties sont conservés dans ../coupures_et_torsion/. Leur statut n’est pas changé par cette preuve.

Le nouveau lemme donne alors g≥22, alors que le genre impose g≤20. **Contradiction. Toute la strate A33 est fermée.**

Dans la formulation précédente g=22−2r₀+ρ, le même pas exige ρ≥2 : le cas r₀=1,ρ=0,g=20 est précisément celui qui manquait.

## 7. Vérifications, portée et limites

Deux implémentations du signe ont été exécutées à distance :

- Sage : rang et choix d’un mineur principal de rang maximal ; rang 14, déterminant 1 modulo 7.
- Python standard écrit séparément : élimination symétrique par congruence, pivots de taille un ou deux, et Bareiss entier. Rang 14, discriminant 1 ; mineurs −5 et 3 508 800.

Le second programme vérifie aussi, sur les vrais graphes H(2,3) et BvLS, la décomposition relative de Witt, ses rangs et ses discriminants :

| Contrôle | Premier | Rang du bloc | Rang total | Rang de couplage du radical | Rang du résidu |
|---|---:|---:|---:|---:|---:|
| H(2,3), 9 sommets | 3 | 2 | 2 | 0 | 0 |
| BvLS, 243 sommets | 3 | 20 | 35 | 4 | 7 |

Dans les deux cas, la relation χ(disc total)=χ(disc bloc)·χ(−1)^h·χ(disc résidu) est contrôlée directement. Les contraintes de genre propres à 99/modulo 7 ne sont pas transplantées à ces autres paramètres. Ces contrôles testent le raccord algébrique, pas un témoin A33.

Les explorations préliminaires des congruences seules et des ombres filtrées λ/μ+Schur n’ont pas donné de contradiction ; elles ne constituent pas la preuve de fermeture.

**Restent ouverts :** les autres étoiles sans classe fermée, dont les étoiles totalement libres à t=0, les familles avec carrés disjoints, l’involution générale et le cas sans symétrie. Les normes 9 et 10 sur six ou sept blocs ne sont pas fermées par ce théorème. Aucune cible globale de l’automation n’étant résolue, elle reste active.

Programmes : verifier_signe_et_controles.py, verifier_signe_sage.py. Sorties : sorties_independantes.txt, sorties_sage.txt. Aucun solveur externe, aucune exécution Python locale, aucun dépôt distant modifié.
