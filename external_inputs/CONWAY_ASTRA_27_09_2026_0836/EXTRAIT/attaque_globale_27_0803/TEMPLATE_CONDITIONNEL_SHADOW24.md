# Template conditionnel : sept blocs et deux lignes pondérées dans le shadowframe24

## Hypothèse supplémentaire

Cette note ne démontre pas que le collage unimodulaire U de rang24 soit sans racines. On suppose explicitement l'existence de24 vecteurs s_j orthogonaux, de norme2, tels que2s_j soient caractéristiques de U. La présence de ce shadowframe est une hypothèse supplémentaire ; aucune classification de réseaux n'est invoquée ici.

U contient le réseau physique N de rang22 et deux vecteurs r1,r2 orthogonaux à N et entre eux, de norme7. Les sept v_c de norme4 et les42 u_o de norme3 sont ceux de la note SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.

## Matrices exactes

Poser

    E_oj=2(u_o,s_j),    M_cj=(v_c,s_j),
    B_ij=2(r_i,s_j).

Les42 lignes de E sont des mots de signes de longueur24. En effet, E_oj est impair et Parseval SUR LES24 vecteurs donne Σ_j E_oj²=8u_o²=24. Chaque carré est au moins1, donc chaque coefficient vaut±1. La norme3 seule ne suffirait pas à obtenir cette conclusion pour une caractéristique isolée.

M est entier ; B a tous ses coefficients impairs. Les trois profils de caractéristique8, appliqués à2s_j, imposent M_cj∈{0,1,−1} et B_ij∈{±1,±3}.

On a BBᵀ=56I2. Chaque ligne B possède donc quatre coefficients de valeur absolue3 et vingt de valeur absolue1. Les deux ensembles de quatre sont disjoints, car un profil de caractéristique8 n'autorise pas les deux produits absolus3 dans la même colonne.

Ainsi :

- les huit colonnes appartenant à un des deux ensembles de quatre ont un seul coefficient non nul dans M ;
- les seize autres colonnes ont trois coefficients non nuls dans M.

La totalité des sept blocs est donc codée par une matrice M de7 lignes orthogonales, chacune de poids8, avec seize colonnes de poids3 et huit de poids1.

Les relations de Gram et d'orthogonalité donnent

    EEᵀ=8(3I42−T),   MMᵀ=8I7,
    MEᵀ=−4C,        BBᵀ=56I2,
    EBᵀ=0,          MBᵀ=0.

La relation physique fournit aussi CE=−6M. Enfin, le frame7I sur N et le projecteur sur l'orthogonal de rang2 donnent

    EᵀE+4MᵀM+BᵀB=56I24.

Ces constantes se vérifient directement par Parseval : les coordonnées de u_o sont E_o/(2√2), celles de v_c sont M_c/√2, et celles de r_i sont B_i/(2√2).

Pour deux u_o distincts, leur produit est0,1 ou−1. Les distances entre les42 mots de E sont donc12,8 ou16, respectivement. Mais les distances seules ne conservent pas le modèle : il faut aussi les deux lignes pondérées B, la matrice des sept blocs M, CE=−6M et toutes les relations précédentes.

## Un petit invariant binaire

Réduire M modulo2. Les sept lignes ont poids8 et deux lignes se recouvrent en un nombre pair de coordonnées, parce que leur produit signé est nul. Elles engendrent donc un code binaire doublement pair. Chaque colonne de M a poids impair, donc la somme des sept lignes est le mot constant de poids24.

Il y a huit colonnes de poids1 et seulement sept supports possibles pour celles-ci : deux colonnes au moins ont le même support binaire. Ce fait ne contredit pas l'existence d'un code plus grand ; il donne seulement une relation de poids2 dans le dual du sous-code engendré par M. On ne remplace pas ce sous-code par un code autodual sans preuve.

## Portée

Ce template est un objet fini global, portant simultanément les42 mots, les sept blocs et les deux charges du collage. L'hypothèse du shadowframe, et a fortiori l'absence de racines dans U, ne sont pas acquises par cette note. Aucun choix de E,M,B satisfaisant toutes les équations n'est produit, et aucune exclusion globale de g20 n'est affirmée.

L'audit indépendant confirme les constantes, les profils et la nécessité de Parseval sur les24 vecteurs pour rendre E plat.

