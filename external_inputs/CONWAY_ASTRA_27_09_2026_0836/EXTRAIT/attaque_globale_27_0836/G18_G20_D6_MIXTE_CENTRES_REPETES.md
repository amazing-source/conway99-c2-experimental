# D6^4 : centres distincts dans un regime mixte4+2

## Hypotheses exactes

On garde le repere physique de G18_G20_D6_SIX_SPINORS.md : U est le cycle-glue integral unimodulaire de racines D6^4, les42 u, les sept h et les deux normales y sont les MEMES vecteurs du frame7I24 ; J=7I2 est primitif et min(N*) >=8/7. Aucun P0 n'est utilise.

Cette piece suppose quatre h de typeIII spinoriels sur A,C, deux h de typeIII spinoriels sur B,D, et le septieme h de typeI ENTIER, quatre unites dans A ouC. La conclusion est : les QUATRE centres des premiers h doivent etre distincts, DEUX dans B et DEUX dans D. La strate mixte entiere n'est pas exclue. Le cas du septieme h de typeII n'est pas couvert. Une permutation cyclique donne la version symetrique.

## La trace puis les diagonales utilisent les deux normales communes

La contribution du frame sur A,C, en trace, est :63 pour les42 u, 12 pour les quatre h spinoriels A,C, 2 pour les deux centres des h spinoriels B,D, et4 pour le h entier. Le total est81, alors que7I sur ces douze dimensions a trace84. Les deux normales y contribuent donc EXACTEMENT3.

Chaque normale de norme7 a un spinor sur une composante A/C et un sur une composante B/D. Sa contribution minimale sur A,C est3/2. Les deux contributions sont ainsi toutes deux minimales : chaque normale a six coordonnees de valeur absolue1/2 dans une composante A/C, et aucune coordonnee dans l'autre. Il n'y a aucun exces normal sur A,C.

Les diagonales A,C ont ensuite une couverture entiere constante, de somme1 entre les deux composantes. Les quatre unites du h entier et les deux centres des h B,D couvrent ainsi exactement les SIX axes d'une seule composante A/C, une fois chacun. Ce fait est une consequence ; on ne choisit pas ces centres separement selon une normale.

Sur B,D, les contributions de base par coordonnees sont celles des42 incidences spinorielles des u, des quatre incidences des deux h spinoriels B,D, et des deux incidences normales. Leur somme est

    (42+4+2)/4 =12.

Il reste exactement2 dans la somme de deux diagonales opposees. Noter t_B,t_D les couvertures entieres constantes (centres des quatre h A,C et exces des normales). Alors

    t_B,t_D sont entiers >=0 ; t_B+t_D=2.            (1)

Pour chaque axe, m_B(x)<=t_B et m_D(z)<=t_D, ou m compte les quatre centres.

## Tout centre repete force trois axes normaux communs

Une multiplicite>=3 est directement incompatible avec(1). Si un centre double est dans B, il force t_B=2,t_D=0. Tous les quatre centres sont alors dans B, et aucun exces normal n'est possible dans D.

Les profils normaux deviennent tres simples. Leurs spinors sur A/C sont deja minimaux. Une demi-coordonnee3/2 dans B avec des unites D violerait la borne caracteristique max|y_B|+max|y_D|<=3/2. Deux demi-coordonnees3/2 dans B violeraient la borne root commune

    (alpha,y1)^2+(alpha,y2)^2 <=6

pour la root sur ces deux axes. Aucun exces D n'est permis. Chaque normale est donc minimale demi-entiere sur D, avec QUATRE unites dans B. Une coordonnee unique2 est aussi interdite par la borne caracteristique ; les glues de trois aretes exigeraient une unite A/C et sont exclues par la trace precedente.

La diagonale B donne exactement

    1_[x unite de y1] + 1_[x unite de y2] =2-m_B(x).   (2)

Les quatre centres ont les profils2+2 ou2+1+1. Il y a donc au moins TROIS axes B non centres. Sur chacun, le membre droit de(2) vaut2 ; les deux normales portent toutes deux une unite. Parmi trois ratios de signes +/-1, deux sont egaux. La root alpha sur ces deux axes a alors produit absolu2 avec chacune des normales. La somme de ses carres vaut8, contre la borne6. Le cas d'un centre double dans D est symetrique.

Toute repetition est exclue ; les quatre centres doivent etre distincts.

## Les quatre centres doivent se partager deux par composante

Ecrire b1,b2 les deux vecteurs spinoriels des h B,D sur B, et d1,d2 ceux sur D. Leurs coordonnees ont valeur absolue1/2. Noter

    sigma_i=b2_i/b1_i, tau_j=d2_j/d1_j, dans{+1,-1}.

Les centres deja prouves distincts donnent m_B(i),m_D(j) dans{0,1}. Pour chaque paire d'axes, les deux orientations des caracteristiques chi_BD recoivent r et2-r contributions actives des deux h spinoriels B,D. Avec les centres des quatre autres h, les nombres actifs sont m_B+m_D+r et m_B+m_D+2-r. Tous deux doivent etre1 ou3. Si m_B+m_D est0 ou2, les deux spinors doivent etre actifs dans des orientations opposees ; si cette somme est1, leurs orientations doivent coincider. Ceci equivaut exactement a

    sigma_i*tau_j = -(-1)^(m_B(i)+m_D(j)).

Il existe donc un signe epsilon commun tel que

    sigma_i=epsilon*(-1)^m_B(i),
    tau_j=-epsilon*(-1)^m_D(j).

Si b centres se trouvent dans B et d=4-b dans D, le produit des deux parties spinorielles vaut

    (b1,b2)+(d1,d2)
       =epsilon*((6-2b)-(6-2d))/4
       =epsilon*(2-b).

Leurs centres sur A/C sont distincts, comme prouve par la diagonale ; ils ont produit0. L'orthogonalite des deux h impose donc b=2 et d=2. Ce corollaire couple les memes deux h dans les36 paires d'axes ; il ne choisit pas leurs signes separement pour chaque caracteristique.

## Controle exact et limite

Le source joint regenere les1365 distributions de quatre centres sur douze axes ;870 ont une repetition. Les diagonales(1) en laissent150 contextes repetes, exactement les profils2+2 et2+1+1 sur une seule composante. Il enumere les270 paires ORDONNEES de supports unitaires normaux couvrant(2), autorisant toutes les parites et tous les signes. Chaque paire partage au moins trois axes, donc zero passe la borne root necessaire. Il controle aussi les64 cas de signes locaux du corollaire, puis les cinq profils b=0..4 avec les deux signes epsilon : seul le partage2+2 est orthogonal.

Ce controle est une relaxation : il n'affirme aucune completion SRG des centres distincts qui restent. Il confirme seulement la couverture de la sous-famille refutee, sans solveur, sans catalogue local et sans extension aux autres profils de h7.
