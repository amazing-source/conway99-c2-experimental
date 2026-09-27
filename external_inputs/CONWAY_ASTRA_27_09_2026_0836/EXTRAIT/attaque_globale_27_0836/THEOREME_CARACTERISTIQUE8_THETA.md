# Entree uniforme : une caracteristique de carre8 sans shadowframe

**Theoreme.** Soit U un reseau integral positif unimodulaire IMPAIR de rang24 et de minimum au moins2. Le nombre de ses vecteurs caracteristiques de carre8 est exactement

    48 + nombre de vecteurs de U de carre2.

En particulier, il en existe au moins48. Aucun repere de24 ombres orthogonales ni classification des reseaux n'est suppose. Le theoreme s'applique aux collages24 acquis en0803, donc les trois profils physiques de caracteristique8 deviennent un point d'entree uniforme. Il ne prouve pas l'existence d'un shadowframe24.

## 1. Conventions et transformations par Poisson

Poser q=exp(pi*i*tau), Im tau>0, et

    Theta_U(tau)=somme_{x dans U} q^(x,x),
    theta3=somme_{n dans Z} q^(n^2),
    theta4=somme_{n dans Z} (-1)^n q^(n^2),
    theta2=somme_{n dans Z} q^((n+1/2)^2).

On utilise l'action f|_k gamma=(c*tau+d)^(-k) f((a*tau+b)/(c*tau+d)). Les transformations T:tau->tau+1 et S:tau->-1/tau se deduisent des sommes et de Poisson sur Z :

    theta3|T=theta4, theta4|T=theta3,
    theta2(tau+1)=exp(pi*i/4) theta2(tau),
    theta3(-1/tau)=(-i*tau)^(1/2) theta3(tau),
    theta2(-1/tau)=(-i*tau)^(1/2) theta4(tau),
    theta4(-1/tau)=(-i*tau)^(1/2) theta2(tau).

Poisson sur U, de covolume1, donne Theta_U(-1/tau)=(-i*tau)^12 Theta_U(tau). Comme(-i)^12=1 et les normes sont entieres, Theta_U est de poids12, avec caractere TRIVIAL, sur Gamma_theta=<S,T^2>.

Un vecteur caracteristique kappa existe : x->(x,x) modulo2 est une forme lineaire sur U/2U ; l'unimodularite rend le Gram modulo2 inversible et fournit kappa dans U tel que(kappa,x)=(x,x) modulo2.

Poisson avec le facteur(-1)^(kappa,x) donne exactement

    Theta_U|_12(TS) = Theta_Sh,
    Sh=kappa/2+U.

Le facteur de Poisson est encore(-i)^12=1. Ainsi aucune phase ni facteur2 n'est cache dans la serie du shadow. Elle est bornee a l'infini, puisque Sh est un coset d'un reseau positif. Les cusps de Gamma_theta sont representes par infini et1 ; cette formule prouve l'holomorphie de Theta_U a tous les cusps, sans supposer une congruence prealable sur kappa^2.

Le groupe Gamma_theta est l'image inverse du sous-groupe{I,S} dans SL2(F2), d'ordre2 dans le groupe d'ordre6. Pour justifier l'image inverse, le noyau Gamma(2) est engendre par -I, T^2 et ST^2S^{-1}. Une reduction euclidienne de la premiere colonne (a,c), avec a impair et c pair, le prouve : les operations a->a+2mc et c->c+2ma choisies avec quotient pair le plus proche reduisent strictement le plus grand module jusqu'a (1,0) ou (-1,0) ; le cas d'egalite des modules est exclu par les parites. La matrice restante est +/-T^{2m}. Ces generateurs sont dans <S,T^2>, et S represente l'autre element du sous-groupe modulo2. L'indice est donc3. Ses trois cosets a gauche sont representes par I,T,TS ; leurs six elements modulo2 sont egalement controles dans le petit source.

## 2. Pourquoi il n'y a que quatre coefficients : preuve de la base

Poser A=theta2^4, B=theta4^4, C=theta3^4 et

    Delta8=AB/16,
    f_j=theta3^(24-8j) Delta8^j, j=0,1,2,3.

Chaque f_j est une forme holomorphe de poids12 et de caractere trivial sur Gamma_theta. Sous S, A et B s'echangent avec signe moins, C prend signe moins ; dans les puissances presentes, ces signes s'annulent. Sous T^2, tout est invariant. Aux deux cusps, les series ont des exposants non negatifs. A l'infini, f_j commence par q^j avec coefficient1.

Voici une preuve autonome de la dimension necessaire. Supposons F de poids12, holomorphe sur Gamma_theta et aux cusps, avec F=O(q^4). Son produit norme

    P=F (F|_12 T) (F|_12 TS)

est une forme holomorphe de poids36 sur SL2(Z) : les trois facteurs se permutent sous toute matrice, par la decomposition en cosets. A l'infini, les deux premiers facteurs sont O(q^4), le troisieme est borne. P est donc O(q^8)=O(Q^4), avec Q=exp(2pi*i*tau).

La formule de valence sur SL2(Z) est

    ord_infini P + (1/2)ord_i P + (1/3)ord_rho P
      + somme_autres_points ord_z P = poids(P)/12 =3.

Tous les termes sont non negatifs pour une forme holomorphe. L'ordre>=4 est impossible si P n'est pas nul ; donc F=0. Pour rappeler la preuve de cette formule : appliquer le principe de l'argument au domaine |Re tau|<=1/2, |tau|>=1, tronque en hauteur. Les deux bords verticaux sont identifies par T. Les deux moities du cercle sont identifiees par S ; leur changement d'argument, issu du facteur tau^k, fournit k/12. Les petits arcs autour des points fixes ont respectivement les fractions1/2 et1/3, et le bord superieur fournit l'ordre en Q. Ceci est un calcul de contour, et non une classification de formes ou de reseaux.

On peut maintenant soustraire a n'importe quelle forme de poids12 les quatre f_j, successivement, pour annuler ses coefficients q^0,q^1,q^2,q^3. Le reste est O(q^4), donc nul. Les f_j sont independants par leurs quatre ordres initiaux. Il s'agit bien d'une base de dimension4, avec les bonnes normalisations.

Ainsi

    Theta_U = theta3^24 + a theta3^16 Delta8
                           + b theta3^8 Delta8^2 + c Delta8^3.

## 3. Coefficients physiques et absence de norme1

Les developpements commencent par

    theta3=1+2q+O(q^4),
    Delta8=q-8q^2+28q^3+O(q^4).

Le coefficient de q dans theta3^24 est48 et celui de theta3^16 Delta8 est1. Min U>=2 impose donc a=-48.

Le coefficient de q^2 est1104+24a+b=b-48. Il compte exactement les racines de norme2 de U ; par positivite,

    b=48+#roots(U)>=48.

Il reste a eliminer c, sans supposer que U soit sans racines.

## 4. Oddness elimine c, et Poisson compte les caracteristiques8

Les transformations au cusp1 donnent

    C|_2(TS)=-A,
    Delta8|_4(TS)=-BC/16.

Par consequent la serie du shadow est

    Theta_Sh=A^6 - (a/16) A^4 BC
                    + (b/256) A^2 B^2 C^2
                    - (c/4096) B^3 C^3.

Sa constante vaut-c/4096. Si0 appartenait a Sh, kappa appartiendrait a2U et toutes les normes de U seraient paires. L'IMPARITE de U exclut cette possibilite ; Theta_Sh n'a donc pas de constante, et c=0.

A=16q+O(q^3), B=C=1+O(q). Le premier terme contribue a partir de q^6, le second a partir de q^4, et le troisieme a partir de q^2 avec coefficientb. Il n'y a pas de terme de norme plus petite. Le coefficient q^2 de Theta_Sh est donc b.

Multiplier un vecteur de Sh par2 est une bijection de Sh sur l'ensemble kappa+2U des vecteurs caracteristiques de U. La norme2 dans Sh equivaut au carre8 pour la caracteristique. Donc

    #caracteristiques_U(carre8)=b=48+#roots(U).

La congruence caracteristique^2=0 modulo8 suit egalement de la forme de Theta_Sh, dont tous les exposants sont pairs. Il n'est pas necessaire de l'invoquer avant le calcul.

## 5. Portee sur le probleme physique49

Les collages U24 de0803 sont integraux, unimodulaires, impairs et de minimum>=2. Le theoreme leur fournit UNE caracteristique de carre8, et meme au moins48, sans postuler de24 vecteurs orthogonaux. Les trois profils de produits avec le frame physique49 et les deux directions de norme7 sont donc uniformement disponibles.

On ne deduit pas que ces caracteristiques puissent etre choisies orthogonales, ni qu'un shadowframe24 existe. Les matrices E/M/B de0803 restent conditionnelles tant que ce repere n'est pas demontre. Le compte b seul est modulaire : il ne fournit pas une contradiction avec le frame49, et aucune elimination complete de g18/g20 ne decoule de cette note.

Le theoreme harmonique ajoute ensuite un resultat precis : lorsque U est SANS RACINES, ses48 caracteristiques8 forment24 paires orthogonales. Dans cette sous-famille seulement, le shadowframe est acquis ; la preuve et le code associe figurent dans ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md. Ce corollaire ne s'applique pas aux collages ayant des racines.

## 6. Second controle de normalisations et positifs

Le source autonome `verifier_theta_caracteristique8.mjs` calcule les series exactes jusqu'a q^8, avec coefficients entiers verifies. Il controle la base triangulaire, les quatre transforms shadow, a=-48, roots=b-48, constante-c/4096 et coefficient shadowq^2=b lorsque c=0.

Le vrai reseau positif Golay de0803, unimodulaire impair24/min3, donne b=48. Le source retrouve4096 normes3 et98256 normes4 : ce dernier compte est aussi obtenu directement par759 octades fois128 signes, plus4*binom(24,2) vecteurs de type4^2. Les48 caracteristiques de carre8 y sont explicitement +/-sqrt8*e_i.

La limite paire est controlee avec la serie du reseau E8^3 : min2 mais non impair, c=-4096, constante shadow1. Le theoreme impair n'y est pas applique. Les positifs H(2,3)/BvLS de0803 gardent leurs propres rangs et parametres3/9 ; ils ne sont pas poses comme unimodulaires24.
