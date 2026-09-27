# Trace uniforme : grands sous-systemes A dans le meme frame

## Hypotheses

N est le reseau integral de rang22 du frame global SRG, avec sept h_c de norme4 et42 u_p de norme3. Dans toute extension INTEGRALE L contenant N, leur operateur commun est

    somme_c h_c tensor h_c + somme_p u_p tensor u_p = 7 P_N.

La borne duale acquise min(N*)>=8/7 implique que chaque u_p a produit0,+1 ou-1 avec toute racine de norme2 de L. Le raccord, valable meme si L a des normes1, est donne dans [G18_G20_E8_MINUSCULE.md](G18_G20_E8_MINUSCULE.md). On n'utilise ni P0, ni type d'etoile, ni une completion locale.

Supposons que L porte un sous-systeme A_n, dans le sous-espace E de dimension n realise par somme x_i=0 dans R^(n+1), avec les racines e_i-e_j.

## Les projections minuscules sont explicites

Pour x=proj_E(u_p), les differences x_i-x_j sont entieres et de valeur absolue au plus1. Il y a donc soit un seul niveau, auquel cas x=0, soit deux niveaux distants de1. Si k des n+1 coordonnees sont au niveau haut, la condition somme x_i=0 donne

    x_i=(n+1-k)/(n+1) sur k coordonnees,
    x_i=-k/(n+1) sur les n+1-k autres,
    ||x||^2=k(n+1-k)/(n+1).

Comme ||u_p||^2=3, seules les valeurs k telles que k(n+1-k)<=3(n+1) sont possibles. Pour n>=20, k=4 est deja exclu : 4(n-3)>3(n+1). Par symetrie k et n+1-k, et par croissance jusqu'au milieu, il reste k<=3 ou k>=n-2. Le maximum de norme projetee est donc

    q_n = 3(n-2)/(n+1).

## La trace utilise le meme espace N

Si dim L=22+d, la trace du frame sur E est

    7 trace(P_E P_N) >= 7(n-d).

En effet trace(P_E P_Nperp)<=d. En majorant chaque projection h_c par sa norme4 et chaque projection u_p par q_n, on obtient la condition necessaire

    7(n-d) <= 42 q_n + 28.

Pour une surlattice integrale de meme rang22, d=0. Cette condition echoue pour n=20,21,22. Pour une extension de dimension au plus24, d<=2 : elle echoue pour n=22,23,24. Les comparaisons entieres sont :

| Cas | n | 7(n-d)(n+1) | 42*3(n-2)+28(n+1) | Ecart strict |
|---|---:|---:|---:|---:|
| Meme rang22 | 20 | 2940 | 2856 | 84 |
| Meme rang22 | 21 | 3234 | 3010 | 224 |
| Meme rang22 | 22 | 3542 | 3164 | 378 |
| Dimension au plus24 | 22 | 3220 | 3164 | 56 |
| Dimension au plus24 | 23 | 3528 | 3318 | 210 |
| Dimension au plus24 | 24 | 3850 | 3472 | 378 |

Ainsi aucun A_n de rang n>=20 ne peut etre contenu dans N ou dans une surlattice integrale de meme rang. Aucun A_n de rang n>=22 ne peut etre contenu dans une extension integrale de dimension au plus24.

## Portee et controles

Ce sont des exclusions de familles de SYSTEMES DE RACINES dans un espace commun. Elles ne prouvent pas g>=21. A19 dans N et A21 dans une extension de dimension24 ne sont pas fermes par cette trace ; les bornes correspondantes ne sont pas strictes. La preuve n'impose jamais un frame7I sur tout L.

[G18_G20_A20_FRAME.mjs](G18_G20_A20_FRAME.mjs) controle par fractions entieres les valeurs k admissibles, le maximum q_n et les six ecarts stricts. Il inclut les deux cas-frontieres non conclus. Ce controle court ne reconstruit aucun graphe et ne fait aucune recherche locale.
