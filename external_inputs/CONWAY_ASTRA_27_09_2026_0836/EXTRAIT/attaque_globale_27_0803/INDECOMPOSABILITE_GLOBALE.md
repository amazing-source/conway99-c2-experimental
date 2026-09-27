# Indécomposabilité uniforme du réseau global des sept blocs

## Résultat acquis

Le réseau intégral positif N de Gram H=3I−S, provenant du cadre SRG(99,14,1,2) avec involution, est orthogonalement indécomposable. Il en va de même de toute surlattice intégrale L de rang22 contenant N et de minimum au moins2.

Le lemme uniforme min N≥2 est établi séparément. Pour la surlattice de déterminant49 obtenue au genre18, min L≥2 suit de L⊂N# et min N#≥8/7 : ses normes étant entières, aucun vecteur de norme1 ne peut apparaître.

Cette fermeture concerne tous les modèles décomposés, sans hypothèse P0 et sans choix d'un type local. Elle ne ferme pas les réseaux indécomposables des genres18 ou20.

## 1. Hypothèses exactes

La matrice signée globale est

    S=[−I7  C ; Cᵀ  T],
    CCᵀ=12I7, CT=0, T²+T=12I42−CᵀC.

Les colonnes de C sont, à orientation près, les42 directions e_i+e_j et e_i−e_j, i<j, de D7. H=3I49−S est positif de rang22, et H²=7H.

Noter v_c les sept générateurs blocs et u_o les42 générateurs racines du réseau de Gram H. On a

    v_c²=4, (v_c,v_d)=0 pour c≠d,
    u_o²=3, (v_c,u_o)=−C_co,
    (u_p,u_q)=−T_pq pour p≠q.

Les relations physiques entières et le frame réel sont

    3v_c+Σ_o C_co u_o=0,
    Σ_c v_c⊗v_c+Σ_o u_o⊗u_o=7I22.

On suppose L intégral positif, de rang22, contenant ces49 vecteurs et de minimum au moins2. La première preuve utilise seulement la pureté des u_o, le carré de T et les relations physiques.

## 2. Preuve courte par la connexité de D7

Supposons L=L1⊥...⊥Lk, somme orthogonale de réseaux intégraux non nuls. Chaque composante non nulle d'un vecteur de L a norme au moins2. Comme u_o a norme3, il ne peut avoir deux composantes non nulles. Chaque u_o appartient donc à un seul facteur.

La partition des u_o par facteurs rend T diagonale par blocs : les produits de deux u_o de facteurs différents sont nuls. T² est diagonale pour la même partition. Pour p,q dans des facteurs différents, l'identité entière du carré impose

    0=(T²+T)_pq=−(CᵀC)_pq.

Les colonnes C_p,C_q doivent donc être orthogonales.

Or le graphe sur les42 directions D7, dont une arête signifie un produit non nul, est connexe. Deux directions sur des paires d'indices partageant exactement un indice ont produit±1. Le graphe des paires d'indices de K7 est connexe. Les deux directions e_i+e_j et e_i−e_j, qui sont orthogonales entre elles, sont reliées par une direction e_i±e_k avec k distinct de i,j.

Une partition de ce graphe connexe ne peut avoir toutes ses arêtes à l'intérieur des parties que si une seule partie est non vide. Tous les42 u_o appartiennent au même facteur, disons L1.

La relation 3v_c=−Σ C_co u_o place chaque v_c dans le span réel de L1. Puisque v_c appartient à L, sa projection sur les autres facteurs est nulle et v_c appartient à L1. Les49 générateurs engendrent N de rang22. Le facteur L1 a donc déjà rang22 ; les autres facteurs ont rang0. La décomposition est triviale.

L'argument ne suppose pas que L soit engendré intégralement par les42 u_o, ni que leur relation divisée par3 soit un changement de base entier.

## 3. Seconde preuve par les sept projections

Cette preuve donne un contrôle indépendant des coefficients et explique pourquoi aucun bloc ne se partage en deux racines de norme2.

Fixer un facteur Lj de la décomposition précédente. Poser α_c=proj_Lj(v_c) et G_cd=(α_c,α_d), entier. Noter Cj la sous-matrice de C sur les u_o de Lj. En projetant la relation physique puis en prenant le produit avec α_d, on obtient

    3G=Cj Cjᵀ.

Pour deux blocs distincts c,d, seules deux colonnes de C contribuent au produit : les deux directions D7 sur cette paire. Leurs contributions sont opposées. Une sous-sélection a donc somme0,1 ou−1. Comme G_cd est entier et 3G_cd égale cette somme, G_cd=0. Ainsi G est diagonale.

Le frame projeté sur Lj est

    Σ_c α_c⊗α_c+Σ_{o dans Lj} u_o⊗u_o=7I_Lj.

Appliqué à α_d, le second opérateur vaut3α_d, par la relation physique. Le premier vaut donc4α_d. En prenant tous les produits, on obtient G²=4G. G étant diagonale, chaque α_c² vaut0 ou4.

Ainsi v_c est entier dans un seul facteur : ses projections ne peuvent avoir les normes2 et2. Les deux incidences non nulles de chaque u_o imposent que ses deux blocs appartiennent à son facteur. K7 est connexe ; tous les blocs et tous les u_o sont dans le même facteur.

## 4. Ce qui rend le résultat non automatique

L'identité T²+T=12I−CᵀC est spectrale. Elle ne suffit pas seule à interdire une décomposition arbitraire de l'espace réel : les valeurs propres fournissent précisément des sous-espaces orthogonaux.

L'étape nouvelle est intégrale : un vecteur de norme3 dans un réseau de minimum2 doit être pur dans une décomposition orthogonale du réseau. Cette partition discrète des42 générateurs est ensuite incompatible avec la connexité des incidences des sept blocs. La décomposition spectrale de l'espace réel ne partitionne pas les u_o de cette façon.

Si le minimum1 était permis, un u_o pourrait se partager en composantes de normes1 et2, et la preuve ne s'appliquerait plus. Aucun résultat de cette note n'est transféré au vrai contrôle H(2,3), dont le réseau possède effectivement des vecteurs de norme1 et dont le facteur spectral est3.

## 5. Conséquences et limites

Les candidats décomposés de rang22 sont exclus uniformément comme réseaux portant ce frame global. En particulier, le modèle de genre K11⊕K11 ne peut être une telle N, indépendamment de sa vieille violation du minimum dual. Ce n'est pas une nouvelle exclusion de ce modèle : celui-ci était déjà éliminé par sa norme duale5/7. Le gain est le lemme universel d'indécomposabilité.

L'argument n'exclut pas encore les réseaux dont le système de racines de norme2 a rang21 ou22. Un système de racines se décompose orthogonalement dans son propre span, mais ses facteurs ne sont pas nécessairement des facteurs orthogonaux du réseau N : un collage peut les coupler. Cette distinction doit être gardée avant toute utilisation de classifications de racines.

Il n'est obtenu ici ni minimum3, ni absence de racines dans le collage unimodulaire24, ni exclusion de g18 ou g20.

## 6. Vérification et audit

La connexité de D7 est démontrée ci-dessus et vérifiée séparément sur42 sommets : chaque sommet a20 voisins et le graphe a420 arêtes. Le contrôle n'énumère aucun type local, graphe99 ou système de contraintes.

Les deux preuves ont été communiquées au contre-auditeur indépendant. Sa relecture confirme la première ; sa seconde vérification de 3G=Cj Cjᵀ, des contributions0/±1 et de G²=4G ne nécessite ni classification A3 ni hypothèse P0.

