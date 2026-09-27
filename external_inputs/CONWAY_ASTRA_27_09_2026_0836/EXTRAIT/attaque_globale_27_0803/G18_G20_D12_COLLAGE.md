# Aucun sous-systeme D12 dans un collage integral de dimension24

## Hypotheses uniformes

L est une extension INTEGRALE, de dimension au plus24, contenant le reseau/espace N22 du meme frame SRG. Les sept h_c sont orthogonaux de norme4 ; les42 u_p ont norme3 et verifient

    (h_c,u_p)=-C_cp, somme_c C_cp^2=2,
    3h_c+sum_p C_cp u_p=0,
    sum_c h_c tensor h_c+sum_p u_p tensor u_p=7P_N.

Les42 u_p engendrent deja N reel. La borne duale min(N*)>=8/7 implique qu'ils sont minuscules pour TOUTE racine de norme2 de L, meme si L contient des normes1 ; voir [G18_G20_E8_MINUSCULE.md](G18_G20_E8_MINUSCULE.md). Aucun type d'etoile ou P0 n'est impose.

Supposons un D12 de racines dans un espace E de dimension12. Les projections de chaque u_p sur E sont0,+/-e_i ou demi-vecteurs(+/-1/2)^12, ces derniers de norme3. Il faut distinguer les deux branches ; on ne peut pas transporter l'indécomposabilite de N a L sans les arguments ci-dessous.

## Aucun generateur u_p n'a une projection spinorielle

Chaque projection u_p a alors norme au plus1. La trace du frame est majoree par42+28=70, tandis que

    7trace(P_E P_N)>=7(12-(dim L-22))>=70.

Si dim L<24, la derniere borne est strictement plus grande que70. En dimension24, toutes les inegalites doivent etre des egalites :

* U=N^perp, de dimension2, est contenu dans E ;
* tous les h_c sont contenus dans E ;
* chaque projection de u_p est +/-e_i, de norme1.

Poser H0=span(h_1,...,h_7), de dimension7, orthogonal a U. En prenant le frame sur E et en notant m_i le nombre de projections u_p sur l'axe i, on obtient

    M=diag(m_i)=7I_E-7P_U-4P_H0.

Les trois espaces U,H0,(U+H0)^perp ont respectivement dimensions2,7,3, et M y vaut0,3,7. Comme M est diagonale, son espace propre3 est un ensemble de sept axes de coordonnees. C'est H0.

Pour tout u_p dont la projection vaut +/-e_i,

    somme_c (h_c,u_p)^2=4||P_H0 e_i||^2 dans {0,4}.

Mais le MEME C global donne cette somme egale a2 pour chaque racine. Contradiction. La branche sans spinor est impossible.

## Un generateur u_p a une projection spinorielle

Cette projection a deja norme3 : le generateur u_p entier est dans E. Le reseau

    P=D12+Z u_p

est integral, de rang12 et determinant1. En effet D12={z dans Z12 : somme z_i paire} a determinant4 ; le demi-vecteur u_p a ordre2 modulo D12 et norme3. L'indice est2 et le determinant est4/2^2=1.

Un sous-reseau integral unimodulaire P se detache de toute extension integrale L : la projection de tout x dans L est dans P*=P, donc L=P orthogonalement somme Q, avec dim Q<=12.

Les projections des autres u sur P sont dans P et restent minuscules pour D12. Les vecteurs +/-e_i n'appartiennent pas a P (ils ont une somme entiere impaire). Il reste0 ou des demi-vecteurs de norme3. Un u est donc ENTIEREMENT dans P ou ENTIEREMENT dans Q.

Voici le raccord de facteur qui interdit cette partition, sans supposer min(Q)>=2. Les u engendrant N reel et etant purs, cet espace est stable par les projections P/Q. Pour un facteur F parmi P,Q, poser h_cF=proj_F h_c. Ces vecteurs sont dans le facteur integral. La relation commune donne

    3(h_cF,h_dF)=sum_{u_p dans F} C_cp C_dp.

Pour c!=d, les seules colonnes concernees sont les deux racines D7 de support {c,d}, avec produits opposes+1 et-1. Le membre droit est0,+1 ou-1. L'integralite du membre gauche force (h_cF,h_dF)=0. Pour c=d, t=||h_cF||^2 donne3t=n_cF, le nombre de racines incidentes porteuses dans F.

Le frame sur h_cF, qui appartient a N reel, donne alors

    7t=t^2+n_cF=t^2+3t.

Ainsi t=0 ou4. Chaque h_c est entierement dans un facteur. Chaque paire de blocs c,d porte deux colonnes D7 non nulles sur c et d ; une telle racine u a produit non nul avec ces deux h. Ils sont donc dans le meme facteur. Le graphe des sept blocs est complet : tous les h_c et tous les u_p sont dans un seul facteur.

Ce facteur a dimension au plus12, mais ils engendrent N22. Contradiction. La branche spinorielle est elle aussi impossible.

## Portee exacte

Aucun D12 de racines n'existe dans une extension integrale de dimension au plus24 contenant ce frame commun N22. Avec [G18_G20_D13_FRAME.md](G18_G20_D13_FRAME.md), cela exclut uniformement tous les sous-systemes D_n de rang n>=12 de ces collages. La preuve ne suppose pas que D12 appartient a N, ni que L a minimum2, ni un frame7I24.

Les petits D, les A et E6/E7 restent ouverts ; cette fermeture de familles ne prouve pas encore g>=21 et n'exclut pas tous les genres g18/g20. Le source court joint verifie les chiffres de trace et les alternatives entieres de facteur, pas une completion locale ou un graphe.
