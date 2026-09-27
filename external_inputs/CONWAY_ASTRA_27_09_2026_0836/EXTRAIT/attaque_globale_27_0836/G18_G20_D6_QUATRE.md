# D6^4 : coque complete et classification des blocs de norme4

## Un modele global rootful, pas un graphe

Dans quatre espaces orthogonaux R^6 indices par i=0,1,2,3, prendre Q=D6^4. Chaque D6 a determinant4 et trois classes non nulles dans son discriminant : v de minimum1, et s,c de minimum3/2. Les classes s et c forment une base de F2^2, avec 2b(s,s)=2b(c,c)=1 et2b(s,c)=0.

Choisir s_i=(1/2,...,1/2) et c_i=(-1/2,1/2,...,1/2) dans la composante i. Definir

    g_i=c_i+s_(i+1 modulo4),
    U=Q+sum_i Z g_i.

Les quatre glues ont produits entiers et classes independantes. Leur groupe a ordre16 ; U est donc integral unimodulaire de rang24, det(U)=4^4/16^2=1. La norme minimale de chaque classe s'obtient par addition des minima des quatre composantes :

| Sous-ensemble des quatre glues | Nombre | Minimum |
|---|---:|---:|
| Vide | 1 | 0 |
| Une arete | 4 | 3 |
| Deux aretes adjacentes | 4 | 4 |
| Deux aretes opposees | 2 | 6 |
| Trois aretes | 4 | 5 |
| Quatre aretes | 1 | 4 |

Il n'y a pas de norme1, ni de racine supplementaire dans une classe non nulle. Le systeme de racines est exactement D6^4. Les normes3 sont les quatre cosets d'une seule arete : deux spinors de minimum3/2, chacun avec32 signes de la parite prescrite. Il y a4*32^2=4096 normes3.

## La coque3 engendre U

Fixer une de ces familles et changer deux signes dans son spinor d'une composante. La difference de deux normes3 donne un vecteur +/-e_a+/-e_b de D6. Ces differences engendrent le D6 de chaque composante. Les quatre baselines g_i sont elles-memes de norme3 et ajoutent les quatre classes independantes. Ainsi la coque3 engendre U integralement.

Son Gram modulo2 a donc rang24, puisque U est unimodulaire. Le source joint donne64 normes3 explicites qui suffisent deja, et controle le rang24 modulo2. Cela REFUTE la borne generale 'coque3 de rang modulo2 au plus20 dans les collages rootful restant apres E8/D12'. Ce modele ne porte pas de frame49 construit ; ni sept blocs physiques, ni dix voisins par racine, ni budgets SRG ne sont annonces.

Le glue, le minimum, la coque et sa generation ont ete relus independamment par g18_audit_neuf.

## Caracteristiques de norme8

L'integralite des produits caracteristiques avec toutes les roots D6 impose que, dans chaque composante, les six coordonnees soient entieres et de meme parite. Une composante impaire coute au moins6 ; une coordonnee non nulle dans les composantes paires coute au moins4. Une caracteristique de norme8 ne peut donc contenir de composante impaire.

Elle est de la forme2(+/-e_a +/-e_b). La condition caracteristique sur les glues g_i de norme impaire exige t_i+t_(i+1)=1 modulo2, ou t_i indique la composante de chaque coordonnee2. Ses deux coordonnees se trouvent donc dans deux composantes OPPOSEES du cycle. Il y a

    2 * 6^2 * 4 =288

caracteristiques de norme8, toutes explicites. Chaque norme3 de la coque est plate pour elles : son produit est toujours+1 ou-1, puisque une arete du cycle rencontre exactement une des deux composantes opposees.

## Les deux inegalites necessaires pour chaque h physique

Supposons maintenant un vrai frame49 dans U, avec les42 u de norme3, sept h de norme4, et deux normales y de norme7. Pour une caracteristique chi de norme8, le frame entier de constante7 donne

    sum_u (u,chi)^2 + sum_h (h,chi)^2 + sum_y (y,chi)^2 =56.

Les42 premiers termes valent42. Les deux normales ont norme impaire, donc leurs produits caracteristiques sont impairs et contribuent au moins2. Aucun h ne peut alors avoir produit absolu4 : son seul carre16 donnerait deja60>56. Les produits avec les h sont pairs, donc de valeur absolue au plus2.

Pour les composantes opposees A,C et B,D, ceci equivaut exactement a

    max_a |h_A,a| + max_c |h_C,c| <=1,
    max_b |h_B,b| + max_d |h_D,d| <=1.                  (1)

## Classification COMPLETE des normes4 passant(1)

Trois types restent. Les signes sont ceux du coset indique, et toutes les permutations permises dans les composantes sont admises.

| Type | Coordonnees non nulles | Classe de glue | Nombre de vecteurs |
|---|---|---|---:|
| I | Quatre unites +/-1 dans UNE composante D6 | 0 | 960 |
| II | Deux unites dans chacune de DEUX composantes ADJACENTES | 0 | 14400 |
| III | Spinors minimaux sur deux composantes opposees, une unite dans une composante intermediaire | Deux aretes adjacentes | 49152 |

Preuve d'exhaustivite : une classe non entiere de norme4 doit etre l'une des quatre classes de deux aretes adjacentes, car les autres ont minimum>4 ou parite impaire. Sa norme4 est deja son minimum3/2+1+3/2, donc elle est exactement du typeIII.

Une norme4 entiere est soit une seule coordonnee+/-2, soit quatre unites. La coordonnee2 viole(1). Dans la classe0, la parite paire des sommes D6 impose le profil4 dans une composante ou2+2. Deux composantes opposees violent(1), deux adjacentes donnent le typeII. La seule autre classe entiere est v dans les quatre composantes ; ses quatre unites, une par composante, violent(1). Le typeI passe(1).

Les comptes sont4*C(6,4)*2^4=960 ;4*C(6,2)^2*2^4=14400 ;4*32^2*12=49152. La coque de candidats h individuels a donc64512 vecteurs. Ce ne sont pas64512 blocs d'un frame valide ; ils doivent encore etre selectionnes SEPT ENSEMBLE, orthogonaux, dans le meme frame avec42 u et deux normales.

## Deux contraintes collectives encore necessaires

Les normales ont leurs demi-coordonnees dans deux composantes adjacentes : seules les classes d'une ou de trois aretes ont parite impaire et peuvent porter une norme7. Si f_A compte les h fractionnaires dont les spinors occupent A,C, et f_B ceux occupant B,D, alors f_A et f_B sont pairs. En effet, sur une coordonnee d'une composante i, la diagonale du frame modulo1 compte(1/4)(n_i+f_i+m_i), ou n_i est le nombre de u incident, et m_i le nombre des deux normales fractionnaires dans i. Pour deux composantes opposees, n_i+n_j=42, m_i+m_j=2 et f_i=f_j, donc44+2f_i est divisible par4. Ainsi il y a0,2,4 ou6 h fractionnaires parmi les sept.

Cette parite peut aussi se retrouver depuis la primitive des sept blocs ; elle n'est pas annoncee comme independante si cette primitive est deja imposee. Elle ne ferme pas la selection septuple.

Une autre borne utile pour les normales vient du minimum dual : pour toute root alpha de U, sa projection sur N est non nulle (sinon alpha serait dans le primitif7I2, de minimum7). Elle appartient a N*, donc

    (alpha,y_1)^2+(alpha,y_2)^2 <=6.

Le membre gauche est un entier, puisque y_i appartient a U ; la borne exacte avant arrondi est14-8=6. Aucun produit absolu3 avec une root n'est possible. Cette coupe concerne les deux normales COMMUNES ; elle ne les choisit pas separement selon les sept h.

## Statut

Le modele de coque et la classification des candidats h sont demontres. L'existence ou l'impossibilite de SEPT h de ces types, orthogonaux et completant le frame physique avec ses42 u et ses deux normales, reste OUVERTE dans cette note. Aucune exclusion globale g18/g20, ni aucun graphe, n'est revendiquee.
