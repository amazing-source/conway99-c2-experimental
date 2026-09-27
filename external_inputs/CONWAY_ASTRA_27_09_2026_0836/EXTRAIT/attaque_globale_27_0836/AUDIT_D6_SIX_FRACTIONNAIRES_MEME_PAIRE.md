# D6^4 : six blocs fractionnaires sur une meme paire sont impossibles

**Statut : seconde preuve mathematique et rejeu exact independants.** La famille fermee a f_A=6 et f_B=0 : six des sept h sont des spinor-pairs sur la MEME paire opposee A,C. Le resultat vaut sans P0, pour g18 et g20 dans le modele D6^4/C4. Il ne ferme ni D6^4 entierement, ni les regimes mixtes f_A=2,f_B=4 et f_A=4,f_B=2.

## 1. La trace commune force le septieme bloc et les normales

Les42 u sont des spinor-pairs sur des composantes adjacentes. Chacun projette avec norme3/2 sur A+C, donc leur contribution a la trace du frame sur cet espace12 est63.

Les six h fractionnaires sur A,C contribuent18. Le septieme h est entier : la parite deja acquise impose un nombre pair de h fractionnaires sur chaque paire opposee, donc il ne peut etre le seul fractionnaire B,D. Chaque normale y de norme7 est dans une classe impaire, a un spinor dans l'une des A,C, et y_A+C^2>=3/2.

La trace commune vaut7*12=84. Ses minimums63+18+3 atteignent deja84. Il s'ensuit h7_A+C=0 et, pour chaque normale, y_A+C^2=3/2. Le septieme h, de norme4 et entier horsA,C, est donc quatre unites dans B (ou D, cas symetrique) ; le type deux-plus-deux sur les composantes opposees est interdit par les caracteristiques.

Chaque normale a un spinor minimal sur une des A,C, l'autre A/C nulle. Sa classe est necessairement une seule arete de glue : une classe de trois aretes aurait une classe v entiere non nulle dans l'autre A/C. Elle a donc un spinor dans B ou D et une composante entiere dans l'autre B/D.

## 2. Pourquoi chaque normale a quatre unites et des spinors minimaux

Les288 caracteristiques chi=2(+/-e_B+/-e_D) voient tous les u avec produit+/-1. L'energie56 donne |(chi,y)|<=3 ; d'ou max|y_B|+max|y_D|<=3/2.

La norme residuelle sur B+D est11/2. Si la composante entiere est nonzero, son maximum est>=1. Le maximum du spinor est donc1/2, et celui de la composante entiere1. Il reste exactement quatre unites dans la composante entiere.

Si la composante entiere est nulle, le spinor de norme11/2 aurait deux coordonnees d'absolu3/2, les autres d'absolu1/2. Une racine D6 additionnant ces deux coordonnees a produit absolu3 avec y. Cela viole la borne commune aux deux normales, (alpha,y1)^2+(alpha,y2)^2<=6. Les normales ont donc toutes le profil H1 : deux spinors minimaux adjacents et quatre unites dans l'autre B/D.

## 3. L'energie exacte ne laisse que deux motifs de centres

Le h7 a un support O de quatre coordonnees de B. Les six h fractionnaires ont chacun un centre unitaire dans B ou D. L'orthogonalite avec h7 interdit les centres de B dans O, ne laissant que deux coordonnees de B disponibles.

Noter m_B(x),m_D(y) les nombres de centres et t_B(x)=m_B(x)+1_O(x). Pour chaque caracteristique chi=2(+/-e_Bx+/-e_Dy), la contribution des sept h vaut4k, avec k=t_B(x)+m_D(y). Les deux normales ont des produits+/-1 ou+/-3. L'energie EXACTE est

    56=42+4k+(chi,y1)^2+(chi,y2)^2.

Les seuls cas sont k=1 (carres1+9) ou k=3 (carres1+1). K=0 et k=2 sont impossibles, pas seulement non optimaux.

Sur les quatre positions O, t_B=1. Il s'ensuit que chaque m_D vaut0 ou2. Sur les deux positions horsO, m_B vaut1 ou3. La somme des six centres et l'interdiction de k=5 donnent exactement :

* deux centres simples dans B horsO et deux centres doubles dans D ;
* deux centres triples dans B horsO et aucun centre dans D.

Le petit rejeu explore les1716 compositions possibles de six centres dans les huit positions disponibles. Il retrouve15 placements du premier motif et1 du second, sans utiliser les masques du producteur.

## 4. Dans les deux motifs, les normales ont le meme quatre-support

Une normale H1 demi-entiere dans B et unitaire dans D peut avoir un produit d'absolu3 avec chi sur CHAQUE position de B et sur chacune de ses quatre positions unitaires de D (choisir les deux signes en accord). Ces positions doivent donc avoir k=1, car k=3 impose deux produits d'absolu1.

Dans le premier motif, t_B=1 partout et m_D=2 sur deux positions. Une normale avec spinorD/unitesB est impossible : une position unitaireB et un centreD donneraient k=3 avec produit3. Les deux normales ont donc spinorB et unitesD, avec les quatre unites exactement hors des deux centresD. Leurs quatre-supports sont identiques.

Dans le second motif, les deux positions horsO ont t_B=3. Une normale avec spinorB/unitesD est impossible. Les deux normales ont spinorD/unitesB, les quatre unites exactement dansO. Leurs quatre-supports sont encore identiques.

Sur ces quatre positions, les ratios des signes de y1 et y2 valent+/-1. Deux ratios sont egaux. La racine D6 qui additionne leurs signes a produit absolu2 avec chacune des normales. Sa projection sur N a alors norme

    2-(4+4)/7=6/7,

non nulle et inferieure au gap dual8/7. Contradiction. Aucune orthogonalite de U ou P0 supplementaire n'est utilisee.

## 5. Controle de la coupe matricielle plus faible

Les memes traces et profils rendent exactes les equations P^tQ=0 et PP^t+QQ^t=16I-4XX^t pour les deux matrices6x6 de signes des spinors et les centres unitaires X. Les contributions y_A y_C^t et h7_A h7_C^t sont nulles APRES les profils du paragraphe1, pas par la seule description du glue.

La preuve abstraite qu'aucune matrice6x6 de signes ne peut avoir rang3 et trois valeurs singulieres carrees12 est correcte : son rowspace3 ne contient que huit vertices du cube au plus, donc quatre lignes projectives au plus. Trois lignes imposeraient trois vecteurs orthogonaux de longueur6, impossibles. Quatre lignes donnent un Gram pondere12(I-zz^t) ; les multiplicités positives de somme6 doivent etre2,2,1,1, et les deux lignes de poids1 auraient produit absolu6, donc seraient la meme ligne projective. Cette sous-coupe ferme les centres tous distincts, et le profil3+1+1+1 par repartition spectrale. La preuve des paragraphes1-4 ferme la strate entiere et ne repose pas sur ces equations matricielles.

## 6. Portee

La conclusion s'applique seulement lorsque six h fractionnaires portent la meme paire opposee. Les nombres0,2,4, ainsi que les six fractionnaires repartis2+4 sur les deux paires, restent ouverts dans cet audit. Aucune selection physique42+7 dans D6^4 n'est construite, aucune exclusion globale g18/g20 n'est annoncee.
