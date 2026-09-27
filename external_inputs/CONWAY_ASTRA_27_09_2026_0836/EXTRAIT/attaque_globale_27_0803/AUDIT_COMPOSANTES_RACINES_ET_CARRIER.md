# Portee adverse des composantes de racines et du carrier lourd

Ces coupes uniformes portent toutes le MEME frame reel22 et ses produits prescrits. Elles ne ferment ni toutes les racines, ni les branches courtes restantes, ni toutes les involutions.

## Produits minuscules sans hypothese de minimum sur une extension

Pour un generateur u de norme3 et une racine alpha de norme2 d'une extension integrale, (u,alpha) vaut0,+/-1. La preuve utilise la borne duale acquise8/7 : un produit+/-2 ferait une norme1 orthogonale a N, donc une projection de alpha sur N egale a+/-u, de norme3>2. Le minimum2 de l'extension n'est pas necessaire.

## D_n>=13 dans toute extension integrale de rang<=24

La projection x d'un u sur D_n a des coordonnees toutes entieres ou toutes demi-entieres, avec |x_i|+|x_j|<=1. Elle est donc0,+/-e_i ou un demi-spinor de norme n/4. Pour n>=13, le demi-spinor coute plus que3 et est impossible.

Les42 projections u contribuent alors au plus42 a la somme des normes projetees, et les sept h au plus28. Le frame est7I_N, pas7I_L. Pour E=span D_n,

    7 tr(P_E P_N)<=70,
    tr(P_E P_N)>=n-(dim L-22)>=n-2.

Pour n>=13, le membre gauche est au moins77. Cette preuve n'a pas suppose E subset N.

## D11/D12 dans N ou Nmax de rang22

Sans demi-spinor, la meme somme serait<=70, contraire a7n=77 ou84. Un u porte donc un demi-spinor.

D12 : la projection du u a deja norme3, donc u est entierement dans D12span. Adjoindre ce spinor a D12 donne un reseau integral de rang12, d'index2 et determinant1. Un sous-reseau unimodulaire se detache orthogonalement d'un reseau integral. L'indecomposabilite acquise du reseau22 interdit ce facteur.

D11 : ecrire u=p+b avec p^2=11/4 et b^2=1/4. Comme4p appartient a D11,4b=4u-4p appartient au reseau. D11 direct-sum Z(4b) a determinant16. La classe de u a ordre4, des produits entiers et norme3 ; son adjonction donne determinant1/rang12. Ce facteur est encore interdit. On n'a pas suppose que p lui-meme appartenait au reseau.

## D12 incline dans une extension de rang24

Sans demi-spinor, la trace de la premiere preuve atteint son unique valeur possible10. Chaque projection de u vaut+/-e_i, chaque h est dans E=span D12, et U=N^perp, de dimension2, est contenu dans E. Posons H0=span des sept h. Dans E, le frame s'ecrit

    Mdiag+4P_H0=7I-7P_U.

Mdiag est la matrice des nombres de projections u sur chaque axe. Les sous-espaces U,H0 et leur complement ont dimensions2,7,3 ; Mdiag a donc valeurs propres0,3,7. P_H0 est son projecteur spectral3 et est un sous-espace d'axes. Pour chaque projection u=+/-e_i, somme_c(h_c,u)^2 vaut alors0 ou4, alors que la colonne C impose exactement2. Contradiction.

Avec demi-spinor, le u est entierement dans E et engendre avec D12 un P=D12+ unimodulaire de rang12. Dans le decoupage L=P direct-sum Q, la projection de chaque u est dans P et est minuscule pour D12. Les+/-e_i n'appartiennent pas a P ; elle vaut donc0 ou un spinor de norme3. Les u sont purs dans P/Q. T et T^2 deviennent bloc-diagonaux, puis la connexite du graphe D7 non orthogonal met tous les u, et les h, dans un facteur de rang12. Leur span22 rend cela impossible. Il n'est pas necessaire de supposer min Q>=2.

Le resultat ferme D12 dans toute extension integrale de rang<=24. D11 incline dans une extension24 n'est pas ferme par cette note.

## Grandes composantes A_n

Une projection minuscule sur A_n est0 ou un poids de norme k(n+1-k)/(n+1). A norme<=3 et n>=20, k<=3 ou est le complement d'une de ces valeurs : k=4 coute deja4(n-3)/(n+1)>3. Le maximum autorise est3(n-2)/(n+1).

La trace du frame est donc au plus42*3(n-2)/(n+1)+28. Elle est strictement inferieure a7n pour n20..22 dans un reseau de rang22 contenant le frame, et a7(n-2) pour n22..24 dans une extension de rang24. Ces composantes sont exclues. A20/A21 dans une extension24 ne sont pas fermes par cette inegalite.

## Carrier lourd : les trois regimes et P0

L'unique coefficient double interieur d'une norme2 laisse six racines positives incidentes I et quatre externes E. Les capacites physiques donnent AII/BII matchings, AIE/BIE colonnes de degre<=2 et

    X-Y=12+2(eAII-eBII),
    2(eBEE-eAEE)+X-Y=16.

Il reste(eAII,eBII)=(0,2),(1,3),(0,3). Dans les deux premieres, X=8,Y=0 et BEE=C4,AEE=0. Dans la derniere, BEE=K4-e,AEE=0 et X=6+Y,Y<=2. Toute arete AIE de cette derniere branche est un double BIE dans un matching. Ces reductions n'utilisent pas P0 et ne ferment pas le cas lourd.

Sous P0 seulement, les quatre supports de blocs externes sont distincts : une paire soeur simplement adjacente donne un prisme ; une paire soeur non adjacente dans BEE a deux communs negatifs plus un commun interieur. Aucun bloc ne porte les quatre supports : les budgets de communs forcent deux labels+ et deux labels-, puis un prisme induit.

Le second controle dense `verifier_carrier_lourd_indep.mjs/.json` reconstruit les ARETES CONNUES des144 contextes. Il rejette108 contextes par un troisieme commun ; pour chacun des36 restants, il examine les210 sous-ensembles de six sommets et trouve deux triangles disjoints relies par un matching, exactement9 aretes. Cette voie ne reprend pas les masques ou le choix de temoins du producteur. Les autres carriers et les deux branches de normes2 restent ouverts.
