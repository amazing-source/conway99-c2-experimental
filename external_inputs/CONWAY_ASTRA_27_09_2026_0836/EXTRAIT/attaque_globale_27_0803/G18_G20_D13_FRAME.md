# Trace du frame : aucun D_n de rang au moins13 dans un collage24

## Hypotheses communes

N est l'espace/reseau global de dimension22 du Gram H=3I-S. Ses sept generateurs h_i ont norme4 et ses42 generateurs u_p ont norme3. Dans une extension euclidienne integrale L contenant N, le meme frame a pour operateur

    sum_i h_i tensor h_i + sum_p u_p tensor u_p =7 P_N,

ou P_N est la projection orthogonale sur l'espace de N. Ce n'est PAS 7I sur tout L si sa dimension est24.

La borne duale min(N*)>=8/7, deja raccordee dans [G18_G20_E8_MINUSCULE.md](G18_G20_E8_MINUSCULE.md), implique que toute norme1 de L est orthogonale a N. Pour toute racine alpha de norme2 de L, on a donc (u_p,alpha) dans {0,+1,-1}. Une valeur absolue2 ferait u_p-sign((u_p,alpha))alpha de norme1, mais sa projection forcerait proj_N(alpha)=+/-u_p de norme3>2. Aucun minimum>=2 de L n'est suppose.

## Projections sur un D_n

Supposons un sous-systeme D_n de racines de L, normalise par les vecteurs +/-e_i+/-e_j dans un espace E de dimension n. Pour x=proj_E(u_p), les produits avec ces racines sont entiers et de valeur absolue au plus1.

L'integralite impose x_i-x_j et x_i+x_j entiers, donc toutes les coordonnees sont entieres ou toutes demi-entieres. La borne impose |x_i|+|x_j|<=1 pour i!=j.

Ainsi x est soit0 ou+/-e_i, de norme au plus1, soit un demi-vecteur dont toutes les valeurs absolues valent1/2, de norme n/4. Pour n>=13, la seconde possibilite a norme strictement superieure a3 et est impossible pour une projection d'un u_p de norme3. Les42 projections u_p ont donc chacune norme au plus1.

La somme des normes projetees est majoree par

    sum_p ||proj_E u_p||^2 + sum_i ||proj_E h_i||^2 <=42+7*4=70.

## Le defaut commun est au plus deux dimensions

En prenant la trace du MEME frame sur E, le membre gauche vaut

    7 trace(P_E P_N).

Si dim L=22+d, alors

    trace(P_E P_N)
      =n-trace(P_E P_Nperp) >=n-d,

car P_Nperp a rang d et ses d vecteurs orthonormaux ont chacun projection sur E de norme au plus1. Cette inegalite ne suppose pas que E et N s'alignent, ni que L se decompose orthogonalement comme reseau.

Pour dim L<=24, on a d<=2. Si n>=13, la trace est donc au moins7(n-2)>=77, en contradiction avec70.

Il n'existe donc AUCUN sous-systeme D_n de rang n>=13 dans une extension INTEGRALE L de dimension au plus24 contenant N. Cela inclut les surlattices de meme espace reel N22 ; dans ce cas, la trace vaut exactement7n et le conflit est encore plus fort.

Plus generalement, lorsque n>=13, la meme preuve necessite n<=10+d dans toute extension integrale de dimension22+d. La borne n>=13 est indispensable dans le passage excluant les poids demi-entiers : elle ne permet pas d'exclure D11 ou D12, dont les poids spinoriels ont norme au plus3.

## Portee

Cette fermeture porte sur une famille de SYSTEMES DE RACINES du meme reseau/collage global, pas sur des types d'etoiles independants. Elle n'utilise pas P0. Les autres composantes A/D de petit rang/E6/E7 demeurent ouvertes ; aucune borne g>=21 ni exclusion entiere g18/g20 n'est annoncee.

La table JS jointe donne les douze ecarts stricts pour13<=n<=24. Les preuves des classes de coordonnees et du defaut de projection sont humaines ; cette table n'est pas une recherche ni une certification de graphe.
