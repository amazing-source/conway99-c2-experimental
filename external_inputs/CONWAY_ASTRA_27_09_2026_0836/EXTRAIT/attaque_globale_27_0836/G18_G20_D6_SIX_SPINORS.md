# Coupe uniforme des six blocs spinoriels dans D6^4

## Portee et hypotheses

On travaille dans le collage integral unimodulaire U de racines D6^4, avec glues c_i+s_(i+1) sur un cycle A-B-C-D. On suppose le MEME repere physique : 42 vecteurs u de norme3, sept h mutuellement orthogonaux de norme4, et deux normales y1,y2 orthogonales de norme7. Leur frame complet vaut7I24. Le sous-reseau N engendre par les49 vecteurs satisfait N_R=J_R^perp, ou J=7I2 est primitif dans U, et min(N*) >=8/7. N lui-meme n'est pas suppose primitif dans U. Aucun choix local independant de normale n'est admis.

La conclusion est seulement : parmi les sept h, SIX ne peuvent pas etre de typeIII avec spinors sur la meme paire opposee A,C. Le regime symetrique B,D est aussi ferme. Cela n'exclut pas D6^4, un type local, g18 ou g20.

Les ingredients acquis sont repris dans G18_G20_D6_QUATRE.md : les288 caracteristiques de norme8 sont2(+/-e_A +/-e_C) ou2(+/-e_B +/-e_D) ; chaque u est plat pour chacune ; les h sont plats aussi. Les h de norme4 sont donc les typesI,II,III de cette note. Les demi-coordonnees d'une normale de norme7 occupent deux composantes adjacentes.

## Borne commune des deux normales

Pour toute root alpha de U, proj_N(alpha) est non nulle : autrement alpha appartiendrait au J primitif, dont le minimum est7. Cette projection est dans N*. Comme alpha^2=2,

    (alpha,y1)^2+(alpha,y2)^2 <= 14-8 =6.          (R)

Les produits sont entiers. En particulier, une normale n'a pas de produit absolu3 avec une root.

Pour une caracteristique chi de norme8, les42 u contribuent42 au frame. Les produits des deux normales avec chi sont impairs, et chaque h actif contribue4. Si k h sont actifs,

    4k+(y1,chi)^2+(y2,chi)^2 =14.                (C)

Les deux produits normaux sont impairs, de valeur absolue1 ou3. La somme de leurs carres ne peut etre que2 ou10 (18 est trop grand). Il suit exactement

    k=1 ou k=3.

Pour k=3, les DEUX normales sont plates pour chi. Une normale lourde de produit absolu3 est possible seulement pour k=1. Cette conclusion vaut pour les144 paires de caracteristiques, simultanement pour le meme frame ; elle ne suppose pas24 ombres orthogonales.

## La diagonale force le septieme h et les profils normaux

Supposons six h de typeIII ayant leurs spinors sur A,C. Chacun a un centre unitaire dans B ouD. Les42 u ont au total42 incidences spinorielles sur A,C ; les six h en ont12 ; les deux normales en ont2. La somme des contributions de base, sur une coordonnee quelconque de A et une quelconque de C, est donc

    (42+12+2)/4 =14.

La diagonale totale est exactement7+7=14. Tous les exces, positifs, sont donc nuls sur A,C. Le septieme h ne peut avoir aucune coordonnee dans A,C. La classification des h plats impose qu'il soit de typeI : quatre unites dans B ouD. Echanger B etD permet de fixer ces quatre unites dans B. L'orthogonalite interdit a chacun des six centres d'occuper leur support.

Les normales n'ont aucune unite ni demi-coordonnee lourde sur A,C. Dans B,D, leur norme restante peut a priori etre faite de quatre unites, d'une demi-coordonnee3/2 et de deux unites, ou de deux demi-coordonnees3/2. Le second profil viole max|y_B|+max|y_D|<=3/2, qui suit de (C). Le troisieme donne un produit absolu3 avec une root D6, interdit par (R). Les classes de trois glues exigeraient une unite dans A ouC, deja exclue.

Ainsi chaque normale a deux spinors MINIMAUX sur une arete du cycle et exactement quatre unites dans l'autre composante B/D. Elle est soit demi-entiere sur B avec quatre unites dans D, soit demi-entiere sur D avec quatre unites dans B.

## Six centres contre les deux normales communes

Noter m_B(x),m_D(z) les multiplicites des centres sur les deux composantes. Poser

    t_B(x)=m_B(x)+1_[x dans supp(h7)],
    t_D(z)=m_D(z).

Pour chi=2(+/-e_B,x +/-e_D,z), le nombre de h actifs est k=t_B(x)+t_D(z), quelle que soit l'orientation des deux signes. Il est exactement1 ou3.

Les quatre coordonnees du support de h7 ont t_B=1. Il suit m_D(z) dans{0,2} pour les SIX coordonnees D. Les deux autres coordonnees B ont t_B=m_B dans{1,3}. Les six centres se partagent donc ainsi :

* deux centres simples B et deux centres doubles D ;
* deux centres triples B et aucun centre D.

Le partage intermediaire1+3 sur B laisserait un centre double D ; leur paire donnerait k=5. Les deux partages affiches sont ainsi exhaustifs, sans aucun calcul spectral.

Une normale demi-entiere sur B a des valeurs absolues1/2 sur SES SIX coordonnees B. Une unite de cette normale en D donne un produit absolu3 pour l'une des deux orientations de chi. Par (C), ses quatre unites D doivent donc toutes satisfaire k=1 pour CHAQUE coordonnee B, soit

    max(t_B)+m_D(z) <=1.                         (1)

Symetriquement, les quatre unites B d'une normale demi-entiere sur D doivent satisfaire

    t_B(x)+max(m_D) <=1.                         (2)

Dans le premier partage, max(m_D)=2 et (2) interdit toute normale demi-entiere sur D. Les deux normales sont donc demi-entieres sur B. Leurs quatre unites D sont necessairement le MEME complement des deux centres doubles.

Dans le second partage, max(t_B)=3 et (1) interdit toute normale demi-entiere sur B. Les deux normales sont demi-entieres sur D. Leurs quatre unites B sont necessairement le MEME support de h7 : sur les deux autres coordonnees, t_B=3 interdit (2).

Dans les deux cas, les quatre coordonnees unitaires communes portent deux listes de signes. Parmi quatre ratios +/-1, deux sont egaux. La root alpha=e_i+epsilon e_j correspondant a ces deux axes a produit absolu2 avec CHACUNE des normales. Ainsi

    (alpha,y1)^2+(alpha,y2)^2 =8,

en contradiction avec (R). Le regime six spinors sur A,C est impossible.

## Controle fini et statut

G18_G20_D6_SIX_SPINORS.mjs controle les1716 distributions des six centres sur les deux positions B autorisees et les six positions D. Il retrouve16 distributions satisfaisant exactement k dans{1,3} : quinze choix des deux centres doubles D et le choix3+3 dans B. Son test d'exclusion travaille meme sur une relaxation plus large : il conserve seulement k<=3, (1),(2), puis la necessite de ne pas partager trois unites entre les normales. Il relaxe les parites de glue et tous les signes, et autorise meme la repetition de leur support. Zero paire survit. Un controle separe des256 paires de signes sur quatre axes retrouve chaque fois une root-temoin de (R).

Cette verification ne remplace pas les lemmes physiques du frame ; elle controle le dernier argument combinatoire fini. La coupe concerne les six blocs simultanes et les deux normales du meme collage. Les regimes quatre-plus-deux ou moins de blocs spinoriels restent ouverts ici.
