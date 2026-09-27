# Moment collectif exact des caracteristiques8

**Theoreme autonome.** Soit U integral positif unimodulaire impair de rang24, minimum>=2. Poser r=#racines de norme2, R=somme_{alpha^2=2} alpha alpha^t, et S2={chi/2 : chi caracteristique, chi^2=8}. Alors

    somme_{s dans S2} s s^t = (4+r/4) I_24 -2 R.

Equivalent : somme_{chi^2=8} chi chi^t = (16+r) I_24 -8R. La formule 4I+R n'est pas correcte en general ; elle lui est equivalente seulement lorsque R=(r/12)I, c'est-a-dire lorsque la coque des racines est un2-design.

## 1. Poisson pondere et base en poids14

Soit P(x)=x^t Qx avec Q symetrique reel de trace0. La derivee seconde de l'integrale gaussienne, et l'annulation du terme constant par trace Q=0, donnent

    Fourier[P(x) exp(pi*i*tau*x^2)](y)
      =(-i*tau)^(-12) tau^(-2) P(y) exp(-pi*i*y^2/tau).

Ainsi la serie Theta_{U,P}=somme P(x)q^(x^2) satisfait

    Theta_{U,P}|_14 S = Theta_{U,P},
    Theta_{U,P}|_14 T^2 = Theta_{U,P},
    Theta_{U,P}|_14(TS) = Theta_{Sh,P}.

Le caractere est bien TRIVIAL ; oublier le facteur tau^(-2) dans Fourier produirait un mauvais signe. L'holomorphie aux cusps suit de Poisson et de la convergence des series ponderees positives.

Reprendre A=theta2^4, B=theta4^4, C=theta3^4, Delta8=AB/16 et f_j=theta3^(24-8j)Delta8^j. Poser D=A-B. On a

    D|_2 S=D, D|_2 T^2=D, D|_2(TS)=B+C.

Les quatre Df_j sont donc holomorphes de poids14 sur Gamma_theta ; chacune commence par -q^j. Elles forment une base : si F=O(q^4), le produit norme F(F|T)(F|TS) est holomorphe de poids42 sur SL2(Z) et d'ordre>=4 en Q. La valence donne un total42/12=7/2, donc F=0. La preuve d'indice3 et de valence est detaillee dans THEOREME_CARACTERISTIQUE8_THETA.md, sans classification des formes ou des reseaux.

## 2. Un seul coefficient pondere subsiste

Le coefficient constant de Theta_{U,P} est0 car P(0)=0. Le coefficient q est0 par min U>=2. Dans l'expansion somme d_j Df_j, cela force d_0=d_1=0.

La constante de sa transformee shadow vaut -2d_3/4096, les autres termes commencant en q^2,q^4,q^6. Elle est nulle car le shadow ne contient pas0 ; meme si0 y appartenait, P(0)=0. Donc d_3=0.

Le coefficient q^2 dans Df_2 vaut-1. On obtient d_2=-somme_{alpha^2=2}P(alpha). Le coefficient q^2 dans (Df_2)|TS vaut2, puisque (B+C)(0)=2 et (f_2|TS) commence par q^2. Finalement

    somme_{s dans S2}P(s) = -2 somme_{alpha^2=2}P(alpha).

Cette identite vaut pour toute quadratique harmonique. L'operateur M_S+2R est donc scalaire. Son trace vaut2|S2|+4r=2(48+r)+4r=96+6r ; en divisant par24, on trouve le scalaire4+r/4 annonce.

## 3. Contre-test construit qui distingue les signes

Construire U16=D8^2+<(s,v),(v,s)> avec s=(1/2)^8, v=e_1. Le glue a quatre classes00,sv,vs,cc. Les deux generateurs ont norme3 et produit1, donc U16 est integral unimodulaire impair et min2.

Prendre U=E8 orthogonal U16, ou E8=D8+Zs. Il existe464 racines :240 dans E8,112 dans chacune des deux composantes D8. L'operateur R vaut60I sur E8 et28I sur les seize autres directions.

Les caracteristiques8 sont toutes nulles sur E8. Dans U16, elles sont exactement :

* les256 vecteurs (+/-1)^8 dans une composante et0 dans l'autre, avec un nombre IMPAIR de signes moins ;
* les256 vecteurs (+/-2e_i,+/-2e_j), une unite double dans chacune des deux composantes.

Ce sont bien des caracteristiques sur D8^2 et les deux glues. La description est exhaustive :2U16 est entier, les parites sont constantes dans chaque bloc8 ; un bloc impair coute au moins8, et dans le cas entier pair les parites des glues imposent une unite double dans chaque bloc. Une composante E8 nonzero d'une caracteristique coute au moins8, et U16 impair interdit une caracteristique nulle, donc elle ne peut intervenir au carre total8.

Il y a512 caracteristiques, comme48+464. L'operateur du shadow vaut0 sur E8 et64I sur les autres dimensions. C'est exactement120I-2R. La candidate4I+R donnerait64I sur E8 et32I ailleurs : elle est donc falsifiee par ce vrai reseau positif.

## 4. Coupe sur le meme repere physique49

Dans un collage portant le repere physique, toutes les caracteristiques8 satisfont |(chi,h_c)|<=2, et leurs produits sur u_o et y_i sont +/-1 ou +/-3. Cela suit de l'energie56 :42 produits roots impairs plus2 produits norm7 impairs coutent deja44. Un bloc avec produit4 couterait16 de plus. Les trois profils restent ceux du theoreme scalaire.

L'identite collective donne notamment, pour chaque u_o,

    nombre{chi^2=8 : |(chi,u_o)|=3}
       = r/4 - somme_{alpha^2=2}(alpha,u_o)^2.

Pour chaque h_c elle donne

    nombre{chi^2=8 : |(chi,h_c)|=2}
       =16+r-2 somme_{alpha^2=2}(alpha,h_c)^2.

Pour chaque normale y_i de norme7 elle donne

    nombre{chi^2=8 : |(chi,y_i)|=3}
       =8+3r/4-somme_{alpha^2=2}(alpha,y_i)^2.

Ces comptes sont entiers non negatifs. Ils concernent le MEME repere et toute la coque8, sans supposer24 caracteristiques orthogonales. Ils ne constituent pas, seuls, une contradiction globale. La matrice R est celle de toutes les racines du collage U, et non seulement de N ou Nmax.

Le meme coefficient pondere q^3 donne un controle de la coque3 complete. Le coefficient de q^3 dans Df_2 vaut24 ; celui de q^3 dans la serie scalaire vaut4096, independamment de r. Ainsi

    #vecteurs_U(carre3)=4096,
    somme_{u^2=3 dans U}u u^t=(512+2r)I_24-24R.

Son rang doit etre au moins22 si le collage porte le repere42, puisque ces42 generateurs doivent engendrer un span22. Il s'agit d'une coupe sur la coque COMPLETE d'un collage donne, pas d'une borne de rang universelle pour toutes les coques. Dans le contre-test E8+U16, cet operateur vaut0 sur E8 et768I ailleurs ; la coque3 n'a que16 directions, bien que le reseau ait rang24.

Lorsque r=0, les48 caracteristiques8 se groupent en24 paires. Le moment16I donne une matrice CARREE de24 representantes avec KK^t=8I, donc K^tK=8I. Le shadowframe24 est alors demontre. ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md developpe ce corollaire et sa construction binaire sans supposer l'unicite d'un code.

Le source verifier_moments_caracteristique8.mjs controle les quatre normalisations ponderees et les operateurs du contre-test explicite. Aucun catalogue SRG, aucun solveur, aucune classification de reseaux n'est utilise.
