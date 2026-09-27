# Racines de corang un : fermeture uniforme contre-auditée

**Statut : démontré et confirmé par le contre-audit indépendant AUDIT_RACINES_CORANG_UN.md.** Le nom de fichier initial est conservé pour les références d'audit. Cette note ferme une famille supplémentaire et garde explicites les faits de systèmes de racines utilisés.

## Proposition acquise

Soit L un réseau intégral positif de rang22, de minimum au moins2 et de discriminant7 élémentaire de dimension2. Supposons qu'il contienne le frame physique des sept v_c de norme4 et des42 u_o de norme3, de rang réel22, avec 3v_c+ΣC_co u_o=0.

Alors le système de ses racines de norme2 ne peut avoir rang21.

Cette proposition s'applique aussi au sur-réseau maximal de déterminant49 du cas g18. Elle n'utilise pas que les42 u_o engendrent L intégralement. Le seul span réel du frame est utilisé.

## 1. Données des racines

Le système de norme2 est simplement lacé et se décompose en facteurs A,D,E. Les seuls facteurs de rang au plus21 dont le discriminant contient7 sont A6, A13 et A20. Leur partie7 est cyclique d'ordre7. Les deux possibilités de deux facteurs7 sont A6² et A13⊕A6 ; trois facteurs7 donnent A6³, avec trois dimensions de racines restantes.

Dans A_n, la classe k du dual a minimum

    k(n+1−k)/(n+1),  0≤k≤n.

Cette formule se démontre en équilibrant les coordonnées entières d'un représentant du dual. Elle donne :

- A6 : minimum de classe non nulle 6/7,10/7 ou12/7 ;
- A13 : la classe d'ordre2 a minimum7/2 ;
- A20 : les classes d'ordre3 ont minimum14/3.

Pour la partie7, A6 a coefficient6 modulo7 et A13 a coefficient5 (classe2, norme12/7). Les deux sont non carrés. Ainsi les deux formes7 des possibilités A6² et A13⊕A6 sont anisotropes en dimension2. Une droite7 non nulle est également anisotrope.

## 2. Réduction primitive de corang un

Noter R le réseau engendré par toutes les racines de norme2, de rang21, et M=L∩span_R(R) sa clôture primitive. Son complément J=M⊥∩L est de rang1 ; écrire J=<r>, r²=m.

La partie7 de R a dimension a≤3 et est élémentaire. La partie7 de M est le quotient d'un sous-espace isotrope de celle de R. Noter d la dimension du collage R→M sur7, et a'=a−2d. Le discriminant7 de M est encore élémentaire.

Le collage M⊕J→L est injectif sur chacun des deux discriminants, parce que M et J sont primitifs. Celui de J est cyclique. La partie7 du collage a donc ordre7^j, avec j=0 ou1. Écrire b=v7(m). La valuation des déterminants donne

    a'+b−2j=2.

Si j=1 et b≥2, la classe d'ordre7 dans J# a norme m/49, entière. L'isotropie du collage exigerait donc une classe isotrope non nulle dans le discriminant7 de M.

On obtient les seules strates possibles :

| Partie7 primitive M | a' | b | j |
|---|---:|---:|---:|
| droite | 1 | 1 | 0 |
| plan anisotrope | 2 | 0 | 0 |
| espace3 non saturé | 3 | 1 | 1 |

La strate a'=0 donnerait un discriminant cyclique de rang1 pour L, incompatible avec son discriminant élémentaire de dimension2. Les strates j=1,b=3 pour a'=1 et j=1,b=2 pour a'=2 sont exclues par l'absence de classe isotrope.

Dans la première strate, M vient soit d'un seul facteur7, soit de A6³ saturé par une ligne isotrope. Dans la seconde il vient des deux facteurs7 anisotropes.

## 3. Un ou deux facteurs7 non collés

Avec a=1 ou2, d=0 et j=0 : aucun collage7 ne touche les facteurs A6/A13/A20 dans L.

Si un facteur A6 apparaît, il se détache intégralement, puisqu'il n'a aucun autre premier discriminant. Un vecteur de norme3 ne peut avoir une composante non nulle dans cet A6 et une composante non nulle dans le complément, tous deux de minimum au moins2. Il ne peut non plus appartenir à A6 seul, qui est pair. Tous les u_o sont donc orthogonaux à A6, et les v_c le sont par leur relation physique. Cela contredit le rang réel22 du frame.

S'il ne reste qu'un facteur A13 ou A20, un u_o ne peut utiliser une classe non7 pour le coupler au complément : ces classes coûtent respectivement7/2 ou14/3, plus que sa norme3. Tous les u_o ont donc leur projection intégrale dans ce facteur A. La sous-lattice de L où cette classe est nulle se décompose A⊥L0. Elle est intégrale de minimum au moins2. Le même raisonnement rend chaque u_o orthogonal à A. La relation des v_c donne la contradiction de span.

Il ne suffit pas ici de dire que A13 ou A20 se détache de L : leur collage aux autres premiers peut exister. La preuve tue seulement les projections des vecteurs de norme3, puis utilise la sous-lattice où leurs classes sont nulles.

## 4. Trois facteurs A6 : saturation interne

La partie7 de A6³ a huit lignes isotropes, toutes non nulles sur les trois facteurs. Aucun plan de deux facteurs ne contient de ligne isotrope.

Pour toute classe isotrope non nulle, les trois minima de projection sont6/7,10/7 et12/7, dans un ordre quelconque. Leur somme vaut4. C'est aussi vérifiable par les216 triples de classes non nulles : l'isotropie force la somme des numérateurs à être28.

Ainsi, si M est la saturation de A6³ par une ligne isotrope, aucune classe nouvellement adjointe ne peut porter la projection d'un u_o de norme3. Dans la strate primitive restante a'=1,b=1,j=0, aucun autre collage7 n'est ajouté par L. Tous les u_o ont donc leur projection intégrale dans A6³.

La sous-lattice où ces classes sont nulles se décompose A6³⊥L0, avec minimum au moins2. Son facteur A6³ est pair, donc les u_o y sont tous orthogonaux. Le frame ne peut engendrer l'espace réel22.

## 5. Trois facteurs A6 : collage au complément de rang1

Il reste a'=3,b=1,j=1, sans saturation interne. Si la ligne de collage est nulle sur un des trois A6, cet A6 se détache et la preuve du §3 s'applique. Il faut donc que la ligne soit non nulle sur les trois A6.

Les trois dimensions de racines restantes forment A3, A2⊕A1 ou A1³. Leur clôture primitive dans leur propre span est triviale à tous les premiers autres que7 : un collage d'indice2 dans A3 ou A1³ ferait apparaître une norme1 ; A2⊕A1 a déterminant6 sans diviseur carré. Les A6 n'ont aucune partie discriminante aux autres premiers.

Comme L est unimodulaire hors7 et J est de rang1, le discriminant hors7 de M doit être cyclique et anti-isométrique à celui de J. Cela exclut A1³, dont la2-partie est (Z/2)^3. Il reste

    A3 : d0=4,   ou   A2⊕A1 : d0=6,
    m=7d0.

Considérons un u_o ayant une classe7 de collage non nulle. Ses trois projections A6 ont chacune norme au moins6/7, soit un coût total au moins18/7.

Si sa projection dans le dernier système de racines R3 a une classe non nulle, cette projection coûte au moins1/2 : c'est la borne uniforme des classes de A3 et A2⊕A1. Dès lors,

    18/7+1/2=43/14>3.

Si cette classe R3 est nulle, sa classe J hors7 est également nulle, par l'injectivité du collage. Sa projection J est donc un multiple non entier de r/7, de norme au moins m/49=d0/7. Alors

    18/7+d0/7 ≥22/7>3.

Dans les deux cas, le coût dépasse la norme3. Aucun u_o ne peut utiliser la ligne de collage7. Toutes ses projections A6 sont donc intégrales, et la sous-lattice A6³⊥L0 rend le frame orthogonal à A6³, contradiction.

## 6. Portée et contre-audit

Les points décisifs sont la primitivité M,J, la borne cyclique j≤1, l'absence de saturation non7 de R3 sous min L≥2, puis les deux coûts18/7+1/2 et18/7+d0/7. Une classe de projection du dual peut être fractionnaire ; sa norme n'est jamais remplacée par le minimum de L.

La preuve n'applique pas l'indécomposabilité d'un système de racines à celle du réseau entier. Elle garde tous les collages possibles et n'utilise la décomposition que dans une sous-lattice où les classes des42 u_o ont été prouvées nulles.

Le second audit indépendant est acquis : AUDIT_RACINES_CORANG_UN.md et verifier_corang_un_indep.mjs/.json, exécuté exact=true. Il confirme les hypothèses primitives, l'anti-isométrie complète hors7, les classes fractionnaires et les coûts. Le petit contrôle propre verifier_racines_corang_un.mjs/.json confirme également les48 classes isotropes A6³ de minimum4 et les strates arithmétiques. Ces contrôles accompagnent la preuve humaine.

Le résultat nouveau est le rejet du rang21 dans L sous les hypothèses de tête. Avec le rejet séparé du plein rang22, on obtient un rang de racines au plus20. Toute racine de N est une racine de Nmax, donc cette borne se transfère au réseau physique des deux genres.

Un contre-exemple de genre de minimum3 et sans racines est sans rapport avec cette strate de racines de rang21 ; il conserve sa fonction de limite aux arguments de genre. Aucun genre g18/g20 n'est exclu par cette proposition.
