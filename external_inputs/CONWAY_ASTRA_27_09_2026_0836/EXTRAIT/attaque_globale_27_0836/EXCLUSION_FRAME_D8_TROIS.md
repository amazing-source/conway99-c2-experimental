# Une famille unimodulaire24 exclue par le repere physique49

**Statut : preuve directe et controle exact independant.** Le reseau U construit ci-dessous existe. Ce qui est impossible est d'y placer le repere physique complet 42+7, avec ses deux normales orthogonales de norme7. Le resultat vaut pour g18 et g20, sans P0. Il ne classe pas tous les reseaux unimodulaires24.

## 1. Reseau, glue et sous-reseau entier

Dans R^8 poser D8={x entier : somme x_i paire}, s=(1/2,...,1/2), v=e_1. Le discriminant D8*/D8 a quatre classes 0,s,v,c=s+v. Leurs minima sont respectivement 0,2,1,2. Les classes s et c sont demi-entieres, avec respectivement un nombre pair et impair de signes moins dans leurs vecteurs minimaux.

Dans D8^3 ajouter les trois classes

    a=(s,s,0), b=(0,s,s), t=(v,v,v).

Elles engendrent huit classes :

    000, ss0, 0ss, s0s, vvv, ccv, vcc, cvc.

Leurs couts minimaux sont 0,4,4,4,3,5,5,5. Les produits a^2=b^2=4, t^2=3, a.b=2 et a.t=b.t=1 sont entiers. Le reseau U ainsi obtenu est donc integral impair ; son indice8 dans D8^3 et det(D8^3)=64 donnent det U=1.

Le sous-reseau U_Z des vecteurs dont toutes les coordonnees sont entieres contient exactement les classes000 et vvv. Ainsi [U:U_Z]=4.

## 2. Coques et caracteristiques explicites

La coque de norme3 est exactement la classe vvv minimale : dans chaque composante, une unite +/-e_i. Elle comporte16^3=4096 vecteurs, tous entiers.

Un vecteur non entier de norme4 appartient necessairement a ss0, 0ss ou s0s et est minimal dans ses deux composantes spinor. Il a deux blocs de huit coordonnees +/-1/2, chacun avec un nombre pair de signes moins.

Pour chacune des trois composantes et chaque choix de huit signes +/-1 avec un nombre pair de signes moins, le vecteur chi forme de ces huit signes et nul ailleurs est caracteristique de U, et chi^2=8. En effet ses produits sur les racines de D8 sont pairs, ses produits sur a et b sont pairs puisque (s,chi)=4-n_minus est pair, et son produit sur t est impair. Cela verifie la parite sur tous les generateurs de U.

Si h est un vecteur non entier de norme4, choisir une composante spinor de h et prendre chi avec les memes signes sur cette composante. Le nombre de signes moins est pair, et (chi,h)=4.

## 3. Le repere interdit les sept blocs demi-entiers

Supposons que U contienne le repere physique de quarante-deux u_o de norme3, sept h_c de norme4 et deux y_i de norme7. Les deux y sont orthogonaux entre eux et au span22 du repere. L'identite tight-frame est

    somme_o u_o u_o^t + somme_c h_c h_c^t + y_1 y_1^t + y_2 y_2^t =7 I_24.

Pour toute caracteristique chi de norme8, elle donne

    56 = somme_o(chi,u_o)^2 + somme_c(chi,h_c)^2
           + (chi,y_1)^2 + (chi,y_2)^2.

Les quarante-deux premiers produits et les deux derniers sont impairs, donc coutent au moins42+2. Un h demi-entier fournit une caracteristique explicite avec produit4, et ajouterait16 : 60>56. Tous les sept h sont donc entiers. Cette etape ne suppose pas vingt-quatre caracteristiques orthogonales.

## 4. L'identite diagonale rend les normales entieres

Les u et h sont entiers. Dans chaque coordonnee j, l'identite diagonale impose y_1j^2+y_2j^2 entier. Or U est contenu dans (1/2 Z)^24. Un carre demi-entier vaut1/4 modulo1 ; avec une ou deux coordonnees demi-entieres, la somme des deux carres vaut1/4 ou1/2 modulo1. Aucun de ces cas n'est entier. Les deux y sont donc eux aussi entiers.

Le reseau N engendre par les u et h, plus J=<y_1,y_2>, est ainsi contenu dans U_Z. Mais

    [U:N orthogonal J] =sqrt(det N * det J)
                      =7^((24-g)/2),

soit49 en g20 ou343 en g18. Cet indice impair devrait etre divisible par [U:U_Z]=4, contradiction.

## 5. Portee et controle

La conclusion exclut uniformement cette famille D8^3/glue pour le repere physique49, et uniquement cette famille. Elle ne dit pas qu'U n'existe pas, que toutes les extensions sont de cette forme, ni que g18/g20 soit globalement ferme.

Le source verifier_frame_D8_trois.mjs regenere les huit classes, leurs produits,384 caracteristiques explicites et tous les signes spinor d'une composante. Il recalcule les coques3 et4, le residu des carres demi-entiers et les indices49/343. Aucun catalogue local ni solveur n'est utilise. H(2,3)/BvLS gardent leurs parametres propres ; ils ne sont pas places artificiellement dans ce collage24.
