# Audit adverse : collage, E8 et les sept blocs simultanes

Cette note utilise le MEME reseau reel N de rang22, de Gram H=3I-S, avec H^2=7H. Elle ne construit pas sept completions locales independantes. Les sept coefficient-relations ont Gram standard21I ; les colonnes -H e_c ont Gram standard28I ; les generateurs interieurs h_c de N ont Gram4I. Modulo7, beta(Hx,Hy)=x^tHy est la forme non degeneree sur im H, tandis que le produit standard y est nul.

## 1. Provenance de la borne duale

La borne min N* >=8/7 est DEJA acquise dans `outputs/dossier6_involution/NOTE_RESEAU_MINIMUM.md`, sections2-3. La premiere note de ce dossier0803 en donne un double compte exact, avec le sommet fixe qui contredit directement le cas limite. Cette borne n'est pas une nouveaute0803. Le controle court lie l'ancienne preuve et le vrai controle BvLS par leurs SHA sans recalculer le graphe BvLS localement.

Pour toute extension INTEGRALE L de N, meme de rang superieur, un vecteur w de norme1 est orthogonal a N. En effet, sa projection x sur l'espace de N appartient a N*, et x^2<=1 ; la borne duale force x=0. Dans une extension du MEME rang22, il n'y a donc aucune norme1. Dans un rang superieur, elles peuvent exister seulement dans l'orthogonal de N.

## 2. Exclusion E8 sans supposer le minimum de l'extension

Soit alpha une racine de norme2 d'une extension integrale L, et soit u un des42 generateurs de norme3. Cauchy et l'integralite donnent (u,alpha) entier de valeur absolue au plus2. Si sa valeur est2s, s=+/-1, w=u-s alpha a norme1. Par la section1, w est orthogonal a N, d'ou proj_N(alpha)=s u. Cette projection aurait norme3, superieure a alpha^2=2. Ainsi

    (u,alpha) dans {0,+1,-1}.

Si L porte un sous-systeme E8, proj_E8(u) a des produits entiers de valeur absolue au plus1 avec ses240 racines. L'argument elementaire en coordonnees montre que cette projection est nulle :

- les racines +/-e_i+/-e_j forcent toutes les coordonnees entieres ou toutes demi-entieres et |x_i|+|x_j|<=1 ;
- dans le cas entier, un seul +/-1 serait possible, mais son produit avec la demi-racine constante serait +/-1/2 ;
- dans le cas demi-entier, toutes les valeurs absolues valent1/2. L'integralite avec la demi-racine constante force un nombre pair de signes moins, donc x est une racine E8 et a produit2 avec elle-meme.

Les42 u sont donc orthogonaux a E8. Les relations physiques

    3 h_c + somme_o C_co u_o =0

impliquent que les sept h_c le sont aussi. Le sous-espace E8 est alors dans N^perp. Il ne peut exister dans une extension de rang24, dont cet orthogonal est de dimension2. La meme conclusion vaut en rang<=29. Dans N lui-meme, c'est immediatement impossible. Cette coupe ne ferme ni A/D/E6/E7, ni toutes les racines de norme2.

## 3. Collage unimodulaire24 et ses limites

On suppose ici une surlattice integrale L de N, de rang22 et determinant49, avec discriminant7 anisotrope de dimension2. Cette hypothese doit etre explicite : le determinant du N initial est7^(22-g), donc il n'est pas toujours49. Dans le regimeg18, passer a une surlattice de determinant49 exige le relèvement isotrope ancien ; ce passage ne vient pas des calculs finis de cette note.

Le discriminant de J=7I2 est egalement anisotrope sur F7. Une anti-isometrie existe, et le graphe de cette anti-isometrie dans L* direct-sum J* donne un reseau U integral, de rang24, d'indice49 dans L direct-sum J et de determinant1. Il est impair puisque J contient des normes7. L et J sont primitifs et orthogonaux dans U.

Min L* >=8/7 exclut les normes1 de U : une projection non nulle sur L aurait deja norme>=8/7 ; une projection nulle force le vecteur dans J, de minimum7. Ce collage sans normes1 et sa limite figuraient DEJA dans l'ancien dossier6.

Une racine MIXTE de U peut cependant avoir projection y=b/7 sur J et projection x dans L*, avec

    7y^2 in {1,2,4,5},
    7x^2 in {13,12,10,9} respectivement.

Ce sont des possibilites arithmetiques necessaires, pas des vecteurs construits. Elles montrent pourquoi min L>=3 n'implique pas min U>=3 : la projection x n'est pas necessairement dans L. L'exclusion E8 de la section2 s'applique a U ; la disparition de toutes ses racines n'est pas acquise.

## 4. Primitive des sept blocs et collage2-primaire

Pour toute surlattice integrale L de determinant impair contenant N, la cloture primitive des sept h_c est

    P=2Z7 + Z*ones,
    det P=2^12, A_P=(Z/4)^6.

Pour le voir, ecrire x=(1/4) somme a_c h_c. Les produits avec les h_c sont entiers. Les produits avec toutes les42 u imposent a_i+a_j et a_i-a_j divisibles par4, donc tous a_c sont0 ou tous2 modulo4. Le second cas donne z=(1/2) somme h_c. Comme z appartient a N*, 2z appartient a N et det N est impair, z appartient deja a N.

Posons K=P^perp intersect L. P est primitif, de discriminant purement2-primaire, et L est unimodulaire sur Z2. Il s'ensuit

    rang K=15,
    [L:P direct-sum K]=2^12,
    A_K,2 anti-isometrique a A_P,
    det K=2^12 det L.

Il n'y a pas d'indice impair cache, puisque le groupe de collage s'injecte dans A_P. Les projections de chaque u sur P et K sont dans P* et K*, de normes respectives1/2 et5/2. Les42 classes d'ordre4 prescrites sont distinctes. C'est un objet de reseaux portant simultanement tous les blocs ; K n'est ni ker C de dimension35 standard, ni l'orthogonal beta de dimension11/13 modulo7. Ses identites de frame sont necessaires mais automatiques a H ; le contenu supplementaire est l'existence des42 courtes classes dans le MEME K.

## 5. Trois profils caracteristiques du collage24

Le vecteur chi0=somme42 u est caracteristique sur L, de carre2 modulo8. La parite M pair a deja une preuve globale propre. Chi0+r1+r2 est caracteristique sur L direct-sum J et sur U, car l'indice49 est impair ; son carre vaut0 modulo8. Toutes les caracteristiques de U different de2U et ont donc carre0 modulo8.

Si chi est une caracteristique de U de norme8, ecrire ses projections x sur L et y sur J, ses produits racines impairs, ses produits blocs2a_c et ses produits J=b_i impairs. Le frame donne

    b1^2+b2^2+4 somme a_c^2+8n3+24n5=14.

Il n'y a que trois profils, a permutation et signe pres :

| Produits J en valeur absolue | n3 | somme a_c^2 |
|---|---:|---:|
|1,1|0|3|
|1,1|1|1|
|1,3|0|1|

Le produit racine5 est impossible et les a_c valent0,+/-1. La borne10 des caracteristiques DANS L ne s'applique pas a la projection x dans L*.

Dans le profil du milieu, l'unique racine r de produit3s touche l'unique bloc actif i et satisfait a_i C_ir=-s. Les dix voisins simples t ont tous produit (x,u_t)=-s T_rt. Cela s'obtient soit par saturation de la ligne propre demandant12, soit par reflexion chi -> chi-2s u_r : la norme8 reste inchangee, le bloc actif migre a l'autre endpoint, et aucune autre racine de produit3 ne peut etre creee. Ces contraintes ne ferment pas le profil.

## 6. Pas de reseau de racines de plein rang22

Cette nouvelle coupe utilise seulement min N>=2, la classification ADE des systemes finis de racines simplementlaces et det N=7^(22-g), avec g18/g20. Posons R le reseau engendre par toutes les racines de norme2 de N. Supposons son rang22. Alors

    v7(det R)=22-g+2 v7([N:R]).

En rang<=22, les seules composantes ADE dont le determinant est divisible par7 sont A6,A13,A20, de determinants7,14,21. Chacune apporte une valuation1 et coute au moins six rangs. Donc la valuation totale est au plus3. Pour g18, la valuation requise est au moins4 : impossible.

Pour g20, la valuation est exactement2, et [N:R] est premier a7. R contient donc soit deux A6, soit A13 et A6. Une composante A6 a discriminant exclusivement7-primaire. Le collage R subset N d'indice premier a7 ne peut avoir aucune composante non nulle sur ce facteur : A6 se detache orthogonalement dans N.

Tout u de norme3 est alors orthogonal a ce A6. Sinon sa projection A6 serait une norme paire>=2 ; une projection non nulle dans son complement integral serait de norme>=2, donnant une somme>=4. Une projection exclusivement dans A6 ne peut avoir norme3 puisque A6 est pair. Les42 u sont donc tous orthogonaux a A6, et les sept relations rendent aussi tous les h_c orthogonaux. Cela contredit le fait qu'ils engendrent N22.

Conclusion uniforme : rang R<=21. Le rang21 n'est PAS exclu et aucune absence generale de racines n'est acquise.

## 7. Controle exact borne et limites

`verifier_collage_E8_P.mjs` est une deuxieme voie independante :240 racines E8/273 candidats, determinant P par Bareiss entier,4096 classes et64 elements de2-torsion,2401 produits d'une anti-isometrie de F7^2, les trois profils caracteristiques8 et1176 reflexions. L'execution donne exact=true en environ0,2seconde. Elle ne cherche aucun graphe, n'enumere aucun catalogue local et ne remplace pas les preuves humaines de collage.

Les positifs H(2,3) et BvLS gardent leurs eigenvaleurs1/-2 et4/-5, leurs facteurs3/9 et leur premier3. Le vrai petit H(2,3) reconstruit par le controle court conserve une norme1 ; le controle BvLS acquis est lie en lecture seule. Aucune constante99/F7, P0 ou determinant49 ne leur est imposee.
