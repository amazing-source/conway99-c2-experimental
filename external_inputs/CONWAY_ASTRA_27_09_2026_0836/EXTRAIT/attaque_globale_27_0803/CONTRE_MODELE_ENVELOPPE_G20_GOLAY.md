# Un contrôle positif global de l'enveloppe arithmétique à déterminant 49

27 septembre 2026. Construction autonome ; aucun dépôt, aucun solveur. Ce réseau n'est pas un graphe de Conway. Il démontre que plusieurs contraintes globales de genre restent compatibles : il faut conserver le repère physique de 49 vecteurs, et pas seulement leurs conséquences arithmétiques.

## Énoncé

Il existe un réseau intégral positif M de rang 22 et de déterminant 49 tel que :

- son groupe discriminant est (Z/7)^2 ;
- son minimum est 3 ;
- il est engendré intégralement par ses vecteurs de norme 3 ;
- il est orthogonalement indécomposable ;
- son dual a minimum au moins 10/7, donc satisfait aussi la borne 8/7 de la campagne ;
- tous ses vecteurs caractéristiques ont un carré congru à 2 modulo 8 et un minimum au moins 10 ;
- son système de racines de norme 2 est vide.

**Statut : DÉMONTRÉ par les arguments ci-dessous, avec les ingrédients finis VÉRIFIÉS EXACTEMENT par deux voies.** La seconde voie et ses empreintes doivent être consultées dans le fichier d'audit associé avant toute annonce d'une vérification indépendante.

Il n'est PAS démontré que M possède le repère physique demandé : sept vecteurs orthogonaux de norme 4 et quarante-deux vecteurs de norme 3 de supports D7, formant ensemble un repère serré de constante 7. Aucune matrice S ni aucun srg ne sont construits ici.

## 1. Le code et le réseau de rang 24

On engendre un code C de longueur 23 par les douze décalages du polynôme

g(X)=X^11+X^9+X^7+X^6+X^5+X+1,

puis on ajoute une coordonnée de parité. L'énumération exacte donne 4096 mots, de poids 0,8,12,16,24, avec effectifs 1,759,2576,759,1. Le code est linéaire, de dimension 12, auto-orthogonal, et contient le mot tout-un. Ce sont des faits finis directement vérifiés, et non une invocation de classification.

Définir L par les vecteurs x/sqrt(8), où x est entier, avec :

1. toutes les coordonnées x_i ont la même parité m ;
2. le support des coordonnées x_i congrues à m+2 modulo 4 est un mot de C ;
3. la somme des coordonnées x_i est divisible par 8.

La linéarité de C et le mot tout-un assurent la fermeture par addition, y compris pour l'addition de deux vecteurs impairs.

Pour l'intégralité, écrire x=m1+2c+4t. Comme le poids de c est divisible par quatre, la troisième condition impose sum(t) pair. Le produit de deux tels vecteurs est divisible par huit : les termes croisés utilisent le poids divisible par quatre et c.d pair. L est donc intégral.

Les trois conditions ont respectivement les indices 2^23,2^12,2. Leur produit est 2^36. Le changement d'échelle par sqrt(8) en rang 24 a covolume 2^-36. L est donc unimodulaire.

Les vecteurs impairs ont norme au moins 24/8=3. Pour les vecteurs pairs, un carré inférieur à trois nécessiterait soit un support de deux/quatre coordonnées congrues à deux modulo quatre, exclu par les poids du code, soit une seule coordonnée +/-4, exclue par la condition de somme. Ainsi min(L)=3. Ses 4096 vecteurs de norme 3 sont exactement les vecteurs de signes associés aux mots du code, divisés par sqrt(8).

## 2. Deux vecteurs orthogonaux de norme 7

Indices de coordonnées de 0 à 23. Poser :

V={0,1,3,4,5,6,7,8,10,11,12,14},
D={0,1,2,9},
D'={3,4,13,15}.

V est un mot de poids 12. D et D' sont disjoints et contiennent chacun deux coordonnées de V et deux hors V. Avec v_i=1-2[ i dans V ], définir

y_1=(1-4 1_D)/sqrt(8),
y_2=(v-4 v 1_D')/sqrt(8).

Les conditions de L sont vérifiées directement. Les deux normes sont 7, et leur produit est nul.

Le réseau P=Z y_1+Z y_2 est primitif dans L. Une saturation non triviale aurait indice sept et serait unimodulaire de rang deux ; elle aurait un vecteur de norme un, incompatible avec min(L)=3. Par primitivité dans un réseau unimodulaire, M=P^perp dans L a rang 22, déterminant 49 et groupe discriminant anti-isométrique à celui de P, soit (Z/7)^2.

## 3. Une base de norme 3, de déterminant 49

Parmi les 4096 vecteurs de signes, exactement 704 sont orthogonaux aux deux y. Le programme en sélectionne 22 indépendants modulo 101. Leur Gram entier, donné complètement dans le JSON, a déterminant exactement 49, calculé par Bareiss avec contrôle de chaque division.

Ces 22 vecteurs forment donc une base intégrale de M : leur sous-réseau a le même déterminant que M. On obtient min(M)=3, génération par la norme 3, et rang 22 sans calcul approché.

Le support des produits non nuls de cette base est connexe (131 arêtes). Dans une décomposition orthogonale intégrale de M, chaque vecteur de norme 3 appartiendrait entièrement à un facteur puisque min(M)>=3. La connexité mettrait toute la base dans le même facteur. M est donc indécomposable.

## 4. Le minimum du dual

Tout z de M* se recolle à un vecteur b=(k y_1+l y_2)/7 de P*, avec k,l choisis entre -3 et 3. Alors z+b appartient à L et b^2=(k^2+l^2)/7<=18/7.

Si 0<z^2<10/7, le carré de z+b serait un entier positif strictement inférieur à quatre, donc égal à trois. Il serait alors l'un des 4096 vecteurs de signes.

Or les carrés de leurs projections sur M ont exactement les numérateurs suivants, sur le dénominateur sept :

| numérateur | 11 | 12 | 13 | 16 | 17 | 19 | 20 | 21 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| effectif | 8 | 12 | 32 | 336 | 336 | 1032 | 1636 | 704 |

Toutes ces projections ont donc un carré au moins 11/7. Contradiction. Ainsi min(M*)>=10/7.

Cette vérification équivaut notamment à l'absence de vecteur de norme 3 ayant simultanément des produits +/-3 avec les deux y. Elle ne postule aucune propriété d'un graphe.

## 5. Vecteurs caractéristiques

Dans L, sqrt(8)e_i est caractéristique et de carré huit : le produit avec x/sqrt(8) est x_i, et le carré d'un vecteur de L a précisément la parité commune m de ses coordonnées. Comme L est unimodulaire, ses caractéristiques diffèrent de 2L ; leurs carrés sont donc tous nuls modulo huit.

Si chi est une caractéristique de M, chi+y_1+y_2 est caractéristique sur M orthogonal P. L'indice 49 est impair, donc elle reste caractéristique sur L. Comme (y_1+y_2)^2=14, on a chi^2 congru à 2 modulo huit. M a minimum trois et est impair ; une caractéristique non nulle ne peut donc avoir carré deux, et son minimum est au moins dix.

## 6. Ce que ce contrôle autorise à conclure

Il réfute un argument d'impossibilité qui n'utiliserait que le rang 22, le déterminant 49, le groupe discriminant, les deux minima, l'indécomposabilité, l'absence de racines et la génération par des vecteurs de norme trois.

Le verrou supplémentaire est précis : sélectionner les QUARANTE-DEUX vecteurs et les SEPT blocs avec leur repère serré et les produits prescrits. Les 704 vecteurs de norme 3 de M n'ont pas été sélectionnés pour satisfaire ces conditions. Ce contrôle ne réfute ni n'établit l'existence d'une involution de Conway.

Sources et sorties : controle_enveloppe_g20_golay.mjs et .json. Tous les indices, la base 22x24 et son Gram 22x22 sont livrés dans le JSON. Aucun résultat de solveur n'intervient.
