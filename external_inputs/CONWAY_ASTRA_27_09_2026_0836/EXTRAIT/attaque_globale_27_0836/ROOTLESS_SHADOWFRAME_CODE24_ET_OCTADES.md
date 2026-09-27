# Sans racines : shadowframe24, code autodual et cubicite des sept octades

**Theoreme uniforme de sous-famille.** Tout reseau integral unimodulaire IMPAIR U de rang24, minimum>=2 et sans racines de norme2 possede24 ombres orthogonales de norme2, dont les doubles sont caracteristiques. Il s'ecrit, apres isometrie, par un code binaire C autodual doublement pair [24,12,8]. Aucune unicite du code ni classification de reseaux n'est invoquee.

Le template E/M/B devient ainsi necessaire sur TOUS les collages sans racines. Il reste conditionnel pour un collage ayant des racines ; le positif E8+U16 de la note harmonique montre qu'un shadowframe ne suit pas dans ce cas.

## 1. Le passage carre du moment a l'orthogonalite

Les deux theoremes theta autonomes donnent, lorsque r=0,

    #caracteristiques(carre8)=48,
    somme_{chi^2=8} chi chi^t=16I24.

La coque se partitionne en24 paires +/-chi, sans point fixe. Choisir une representative par paire et former la matrice CARREE K de24 colonnes. Alors KK^t=8I. Cette matrice est inversible, et K^tK=8I. Les representatives sont donc orthogonales de norme8. Les ombres s_i=chi_i/2 ont Gram2I24 et appartiennent toutes au meme coset Sh.

Le caractere carre de K est essentiel : avec plus de48 caracteristiques, un tight-frame n'est pas automatiquement une base orthogonale.

## 2. Le code associe, sans classification

Utiliser les axes orthonormes e_i=s_i/sqrt2. Pour x dans U, poser a_i=(x,chi_i)=sqrt8*x_i. La caracteristicite donne a_i entier et a_i=x^2 modulo2 pour TOUS les i. Donc U est contenu dans (1/sqrt8)Z24, et les24 coordonnees a ont une meme parite.

Soit U0 le sous-reseau des normes paires, d'indice2 dans U, et L0=sqrt2 U0. Il est contenu dans Z24 et de covolume2^13. Comme s_i-s_j et s_i+s_j sont des differences de deux ombres du meme coset, ils appartiennent a U ; leurs normes4 sont paires. Ainsi L0 contient2D24.

On a exactement L0 inter 2Z24=2D24. Sinon un vecteur2z avec somme z impaire permettrait, modulo2D24, d'obtenir2e_i dans L0. Cela donnerait sqrt2*e_i dans U, de norme2, interdit.

Le code C=L0 modulo2 a donc cardinal

    |C|=[L0:2D24]=2^25/2^13=2^12.

Il a dimension12. Pour b,d dans L0, l'integralite de (b/sqrt2,d/sqrt2) impose b.d pair ; C est orthogonal a lui-meme, donc AUTODUAL par dimension. La norme paire b^2/2 impose b^2=0 modulo4, donc les poids de C sont divisibles par4 : C est DOUBLEMENT PAIR.

Un mot nonzero de poids4 permettrait de choisir un releve b avec quatre coordonnees +/-1 et toutes les autres nulles. En effet les differences de deux releves de meme parite valent2z ; changer un seul signe ajuste la parite de somme z, donc permet une difference dans2D24. Le vecteur b/sqrt2 aurait norme2. Ainsi le poids minimal est>=8.

Il est exactement8. S'il etait>=12, les boules de Hamming de rayon4 autour des2^12 mots seraient disjointes. Chacune contient

    1+24+276+2024+10626=12951 >4096=2^24/2^12

mots, contradiction. Le code a donc parametres [24,12,8].

Les poids pairs impliquent que le mot tout-un est dans Cperp=C. Les complements sont donc des mots de C. Les seuls poids sont0,8,12,16,24. La projection sur deux coordonnees est surjective, sinon Cperp aurait un mot de poids<=2. Le deuxieme moment des poids et la complementarite donnent, en notant t=A8=A16,

    552 +296t +132(4094-2t)=2^10*24*23,

donc A8=A16=759 et A12=2576. Ce compte ne prouve ni ne suppose l'unicite d'un code de ces parametres.

## 3. Forme explicite du reseau entier

La serie scalaire theta donne4096 vecteurs de norme3. Choisir l'un d'eux u0. Dans les axes precedents, ses24 coordonnees a sont impaires et leur somme de carres vaut24 ; elles sont toutes +/-1. Inverser les axes pour obtenir u0=1/sqrt8.

L'integralite avec u0 impose, pour b dans L0, somme b=0 modulo4. Le reseau

    {b dans Z24 : b modulo2 dans C, somme b=0 modulo4}

a le meme indice2^13 que L0, et le contient : ils sont egaux. La condition de somme fournit un bit supplementaire sur le reseau preimage du code, puisqu'ajouter2e_i change la somme de2. Enfin U=U0 union(u0+U0). On obtient

    U={a/sqrt8 : a_i=m modulo2 pour tous i,
       {i:a_i=m+2 modulo4} dans C,
       somme a_i=0 modulo8}.

Les4096 vecteurs de norme3 sont exactement les signwords a_i=+/-1 associes aux4096 mots de C. La preuve identifie une construction par C, sans appeler ce code unique ni invoquer une classification externe.

## 4. Le template physique E/M/B est maintenant uniforme ici

Les42 u physiques ont la forme E_o/sqrt8 avec E_o dans{+/-1}^24 et leurs mots de signes dans C. Les h ont la forme M_c/sqrt2 avec M_c entier. Pour les deux normales y_i de norme7, poser B_i=sqrt8*y_i ; leurs coordonnees sont impaires.

L'energie contre chaque caracteristique chi_j=sqrt8e_j vaut56. Les42 produits E coutent42 et les deux produits B coutent au moins2. Elle interdit |2M_cj|>=4 et |B_ij|>=5. Donc M a entrees0,+/-1, chaque ligne a poids8 et appartient a C : les sept h sont des OCTADES signees, avec un nombre pair de signes moins. Chaque ligne B a quatre entrees d'absolu3 et vingt d'absolu1 ; leurs quatre-supports sont disjoints.

Dans chacune des24 colonnes, l'energie impose poids(M_colonne)=1 si un B vaut3, et poids3 sinon. Il y a huit colonnes de poids1 et seize de poids3. Les identites exactes du meme repere sont

    EE^t=8(3I-T), MM^t=8I7, ME^t=-4Inc, Inc E=-6M,
    BB^t=56I2, EB^t=MB^t=0,
    E^tE+4M^tM+B^tB=56I24.

Ici Inc est la matrice d'incidence D7 ; le code binaire est C. Les deux objets ne sont pas identifies.

## 5. Chaque octade porte un multigraphe cubique sans triple arete

Fixer un h et orienter les12 u incidentes pour que (h,u)=-1. Sur les huit positions de son octade, les produits de signes M_j E_oj ont somme-4 : exactement DEUX positions valent+1, les six autres-1. Associer a chaque u l'arete de ses deux positions minoritaires.

La relation 3h=-somme_12u donne, sur chaque position de l'octade, somme_12 M_jE_oj=-6. La position figure donc exactement trois fois comme minoritaire. Les12 aretes forment un multigraphe cubique sur huit sommets.

Deux u ayant la MEME arete minoritaire ont les memes huit signes sur l'octade. Leur difference binaire d est un mot du code et est disjointe de l'octade O. Elle ne peut avoir poids12 : alors O+d aurait poids20, et son complement, egalement dans le code, aurait poids4. Les seules possibilites pour deux u distinctes sont donc poids8 ou16, donnant Gram(u,u')=+1 ou-1, jamais0.

Dans le secteur local physique, T_star est la difference de deux matrices de matchings, T_star=P_mu-P_eta (les coins annules, si les matchings coincident, ne changent pas l'argument). Trois occurrences de la meme arete obligeraient leurs trois Gram mutuels a etre nonzero, donc formeraient un triangle dans l'union des deux matchings. Un triangle n'admet pas de coloration propre de ses aretes en deux couleurs : impossible. Toute arete minoritaire a donc multiplicite<=2.

Cette derniere coupe utilise le code, la meme octade et les matchings physiques ; le centroid seul ne suffit pas. Elle ne ferme pas tous les multigraphes cubiques ni tous les repères49.

## 6. Verification et portee

verifier_rootless_code24.mjs controle les indices, la borne de Hamming, les moments de poids, les trois profils energetiques, les28 paires minoritaires, la difference code disjointe d'une octade et les huit colorations possibles d'un triangle. La preuve universelle est analytique et algebrique ; ce petit controle n'est pas une enumeration de tous les codes ou collages.
