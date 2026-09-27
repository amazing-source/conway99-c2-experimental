# Seconde preuve du rejet du rang21 des racines

La proposition auditee est conditionnelle et uniforme. Soit L un reseau integral positif de rang22, de minimum>=2, de determinant49 et discriminant7 elementaire de dimension2. Il contient le frame physique h_1,...,h_7,u_1,...,u_42 de rang REEL22, avec h_c^2=4, u_o^2=3 et3h_c+somme C_co u_o=0. On n'exige pas que le frame engendre L integralement. Sous ces hypotheses, les racines de norme2 de L ne peuvent avoir rang21.

Le determinant49 et la longueur2 du discriminant sont des hypotheses essentielles. Le relèvement maximal du regimeg18 doit etre fourni par la preuve ancienne ; cette note ne le cree pas. Elle ne ferme pas les reseaux sans racines ni les genres de determinant49.

## Reduction primitive et tableau entier

Supposons R, engendre par toutes les racines, de rang21. La classification ADE donne comme seuls facteurs7 A6,A13,A20, de valuations1. Il y en a a<=3. Soit M=L intersect span(R) la cloture primitive et J=M^perp intersect L=<r>, r^2=m. Les parties7 de R et M sont elementaires. La saturation interne a dimension d et laisse a'=a-2d.

Le groupe de collage M direct-sum J subset L s'injecte dans les deux discriminants, car les facteurs sont primitifs. Celui de J est cyclique, celui de M7 elementaire : sa7-partie a ordre7^j avec j<=1. Avec b=v7(m),

    a'+b-2j=2.

Les plans7 de A6^2 et A13+A6 sont anisotropes, de coefficients(6,6) ou(6,5) sur F7. Donc aucune saturation interne n'est possible dans ces plans. Une droite7 n'a pas non plus de classe isotrope non nulle. Les seules saturations possibles sont celles de A6^3, par une ligne.

Si a'=0, j=0 et b=2, le discriminant7 de L serait cyclique d'ordre49, et non elementaire de longueur2. Si a'=1,j=1, alors b=3 ; si a'=2,j=1, b=2. Dans ces deux cas, le sous-groupe d'ordre7 de J* a une norme entiere, puisque m/49 est entier. La classe de M devrait alors etre isotrope non nulle, impossible pour la droite ou les deux plans anisotropes. Il reste exactement

| a' | b | j |
|---:|---:|---:|
|1|1|0|
|2|0|0|
|3|1|1|

## Un ou deux facteurs7

Pour a=1/2 sans saturation interne, j=0 : les projections7 du collage L sont nulles. Une composante A6, dont le discriminant est exclusivement7, se detache orthogonalement dans L. Tout u de norme3 est orthogonal a cette composante paire de minimum2 : une projection non nulle coute>=2, et le reste, s'il est non nul, est un vecteur de L de norme>=2.

Sans A6, il reste A13 ouA20. La classe7 est nulle ; les seules classes non7 ont minima7/2 ou14/3, trop grands pour u^2=3. La projection de chaque u appartient donc a A13 ouA20 lui-meme. Soustraire cette projection laisse un vecteur de L. Le meme minimum2 et la parite du facteur rendent la projection nulle. Les sept relations rendent les h orthogonaux eux aussi, ce qui contredit le span reel22.

## A6^3 avec saturation interne

Dans A6, le minimum de la classe k est k(7-k)/7. Toute classe isotrope non nulle dans A6^3 est non nulle sur les trois facteurs, car les sous-plans sont anisotropes. Ses trois numerateurs de minimum sont6,10,12, dans un ordre quelconque : la somme vaut28, donc le minimum de cette projection est4.

La saturation interne par une ligne ne peut donc fournir aucune classe de projection a un u de norme3. Dans la strate a'=1,b=1,j=0, L ne rajoute aucune autre classe7. Les u ont toutes leurs projections integrales dans A6^3 ; elles sont nulles par le minimum2 et la parite, puis les h le sont aussi. Contradiction de span.

## A6^3 avec collage au complement de rang1

Il reste a'=3,b=1,j=1, sans saturation interne7. Si la ligne de collage s'annule sur un A6, ce facteur se detache et donne la contradiction precedente. Sinon ses trois composantes sont non nulles.

Les trois rangs de racines restants forment R3=A3, A2+A1 ouA1^3. Leur saturation non7 est triviale : les classes integrales non nulles d'A3 et d'A1^3 ont un representant de norme1, interdit dans L ; A2+A1 n'a aucune classe integrale non nulle. Les A6 n'ont pas d'autre premier discriminant, donc M=R.

L est unimodulaire hors7. Le collage primitif impose l'anti-isometrie COMPLETE des discriminants non7 de M et J. Celui de J est cyclique. A1^3, de discriminant(Z/2)^3, est impossible. Il reste R3=A3 de determinant d0=4 ouA2+A1 de determinant d0=6, et

    m=7d0.

Si un u utilise la classe7 de collage, ses trois projections A6 coutent au moins18/7. Si sa classe R3 est non nulle, elle coute au moins1/2, donnant43/14>3. Si elle est nulle, sa classe J non7 est aussi nulle par l'injection du collage. Sa projection J est alors un multiple non entier de r/7, de norme>=m/49=d0/7. Le cout total est>=22/7>3.

Ainsi aucun u ne peut utiliser la classe7 non nulle. Ses projections A6 sont integrales ; soustraire une projection non nulle laisserait soit un vecteur de L de norme<=1, soit un u exclusivement dans un facteur pair. Dans les deux cas c'est impossible. Les u, puis les h, sont orthogonaux a A6^3. Contradiction finale de span.

## Statut et controle

La preuve candidate `RACINES_CORANG_UN_CANDIDAT.md` passe ce contre-audit complet. Les hypotheses primitives, les classes fractionnaires et tous les collages non7 ont ete traites. La conclusion acquise est le rejet du rang21 dans L sous les hypotheses de tete. Avec le rejet separe du plein rang22, les racines de L ont donc rang<=20.

`verifier_corang_un_indep.mjs` est une seconde implementation arithmetique :216 triples de classes A6,48 isotropes de minimum4, deux plans anisotropes, toutes les strates de valuation, les discriminants de rang3, et les couts strictement>3. Les operations sont des entiers ou fractions explicites ; aucun catalogue local ni solveur n'est utilise. Ce controle accompagne la preuve humaine et ne la remplace pas.
