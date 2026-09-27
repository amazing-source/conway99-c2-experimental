# Exclusion uniforme d'un E8 par les42 generateurs minuscules

## Hypotheses globales

N est le reseau integral reel de dimension22 engendre par les49 vecteurs du Gram H=3I49-S : sept h_i de norme4 et42 u_p de norme3. Il n'a pas de vecteur de norme1. Ses relations communes sont

    3h_i + sum_p C_ip u_p =0.

Elles impliquent que les42 u_p engendrent deja l'espace reel de N. On n'utilise ni un type W, ni P0, ni une completion separee des sept etoiles.

Un vecteur alpha de norme2 dans N, ou dans une extension INTEGRALE N' de minimum au moins2, satisfait

    (u_p,alpha) dans {0,+1,-1}.

En effet, Cauchy donne une valeur absolue au plus2, et une valeur +/-2 rendrait u_p-sign((u_p,alpha))alpha de norme3+2-4=1 dans N'. Ces projections sont donc des poids minuscules pour tout systeme de racines de N'.

## Lemme elementaire E8

Dans un espace orthonormal de dimension8, prendre les240 racines E8 : les112 vecteurs +/-e_i+/-e_j et les128 demi-vecteurs (+/-1/2,...,+/-1/2) comportant un nombre pair de signes moins.

Si x a des produits ENTIERS de valeur absolue au plus1 avec ces240 racines, alors x=0.

Les produits avec e_i-e_j et e_i+e_j imposent x_i-x_j et x_i+x_j entiers. Toutes les coordonnees sont donc entieres ou toutes demi-entieres. La borne sur ces memes racines donne |x_i|+|x_j|<=1 pour i!=j.

Dans le cas entier, au plus une coordonnee est non nulle, et elle vaut +/-1. Ce vecteur non nul aurait produit +/-1/2 avec la demi-racine (1/2,...,1/2), ce qui contredit l'INTEGRALITE.

Dans le cas demi-entier, les huit valeurs absolues sont exactement1/2. Le produit avec (1/2,...,1/2) est entier seulement si le nombre de signes moins est pair. Alors x est lui-meme une racine E8. Son produit avec cette racine vaut2 et contredit la borne1.

## Consequence pour le meme reseau global

Supposons un sous-systeme E8 de racines de norme2, dans N ou dans N'. Pour chaque u_p, sa projection x_p sur l'espace de cet E8 satisfait le lemme ; elle est donc nulle. Les relations3h_i+sum C_ip u_p=0 rendent aussi tous les h_i orthogonaux a cet E8.

Si E8 est dans N, tous ses huit axes sont orthogonaux a l'espace entier de N alors qu'ils lui appartiennent : contradiction. Une autre verification consiste a restreindre le tight frame7I a E8 : les42 u_p n'y contribuent pas et les sept h_i seuls ne peuvent fournir un operateur de rang8. La premiere preuve utilise plus fortement les relations communes et n'a pas besoin de compter ces sept rangs separement.

## Extension integrale, meme de minimum1

La borne duale uniforme acquise dans [AUDIT_NORME1_ET_METRIQUES.md](AUDIT_NORME1_ET_METRIQUES.md) donne min(N*)>=8/7. Pour expliciter le raccord, si y appartient a N* et ||y||^2<=1, ses coefficients a_i=(y,u_i) sont entiers, Sa=-4a et somme a_i^2<=7. Un coefficient absolu2 est impossible par sa ligne : il reste au plus3 en somme absolue, contre6 ou8 demandes. Si a est non nul, il est donc ternaire de support m<=7. Le double compte D=m(m-7)-7e-somme d_i^2>=0 force m>=7 ; et le cas m=7 est exclu par le lemme physique uniforme deja audite. Ainsi y=0. Comme somme a_i^2 est un entier, le premier y non nul a norme au moins8/7.

Soit L une extension INTEGRALE contenant N. Tout w dans L de norme1 a projection sur N dans N* de norme au plus1 ; cette projection est donc nulle. Toutes les normes1 de L sont orthogonales a N.

Si (u_p,alpha)=+/-2 pour une racine alpha de L, w=u_p-sign((u_p,alpha))alpha aurait norme1 et serait orthogonal a N. Sa projection nulle imposerait proj_N(alpha)=+/-u_p, de norme3, alors que ||alpha||^2=2. Contradiction. Les42 u_p restent donc minuscules pour les racines de L, MEME si L possede des vecteurs de norme1.

Un E8 de L serait par consequent contenu dans N^perp. Il est impossible lorsque dim(L)-22<8, c'est-a-dire dim(L)<=29. Cela couvre en particulier tout collage integral en dimension24. Il ne faut pas supposer un tight frame7I24 : il vaut seulement sur N22. L'integralite de L et la borne duale commune sont indispensables ; son minimum>=2 ne l'est plus.

## Portee

Cette preuve ferme uniformement une famille de SYSTEMES DE RACINES globaux : aucun sous-systeme E8 de N ni de toute extension integrale de dimension au plus29. Elle ne classe pas les composantes A/D/E6/E7, ne prouve pas l'absence de toute racine de norme2 et ne donne pas encore g>=21. Elle ne suppose pas que le choix initial des49 generateurs est invariant sous les reflexions du systeme de racines.

Le JS joint regenere les240 racines et controle exactement les273 candidats restant apres les bornes +/-e_i+/-e_j, avec des produits rationnels represented par des entiers multiples de4. Il constitue un contre-controle fini du lemme, pas une recherche de graphe.
