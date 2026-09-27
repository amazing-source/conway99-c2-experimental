# Trois regimes du support global lourd de norme14

## Meme vecteur, memes sommets

On utilise la reduction de [G18_G20_NORME14_LOURDS.md](G18_G20_NORME14_LOURDS.md) : une racine v de norme2 du reseau global a un unique coefficient interieur2, aucun autre interieur actif, six orbites racines actives incidentes a ce bloc, et quatre orbites racines actives externes. On oriente son eigenvecteur physique phi pour avoir phi(c+)=2 et phi(c-)=-2.

I est l'ensemble de ses six sommets racines positifs incidents : ils sont voisins de c-, pas de c+. Leurs mates sigma(I) sont voisins de c+. E est l'ensemble de ses quatre sommets racines positifs externes ; ils ne sont voisins d'aucun des deux interieurs c+,c-. Toutes ces dix racines ont poids1. On travaille sur CES sommets reels du meme graphe, pas sur des possibilites locales independantes.

Poser A=adj[I union E,I union E] et B=adj[I union E,sigma(I union E)]. A et B sont symetriques0/1, avec diagonale nulle. La diagonale de B est nulle parce que les mates racines sont non adjacents. A et B peuvent avoir simultanement une entree1 : c'est alors une paire double D reelle.

## Capacites fournies par les interieurs lourds

Le graphe induit par N(c-) est un matching. A_II est donc un matching. Pour p dans I, la paire non adjacente(c+,p) a deja le commun c- ; elle peut avoir au plus un autre commun dans sigma(I). Ainsi B_II est aussi un matching.

Pour e dans E, les paires(e,c+) et(e,c-) sont non adjacentes. Elles montrent que chacune des colonnes B_IE et A_IE comporte au plus deux1. En particulier

    X = nombre de1 de B_IE <=8,
    Y = nombre de1 de A_IE <=8.

L'equation propre Agraph phi=-4phi impose, sur les dix racines positives,

    B1-A1 = 2 sur I,
    B1-A1 = 4 sur E.

Les deux unites deja recues par I proviennent du voisin c- de poids-2. La sommation sur I donne

    X-Y = 12+2(a-b),

ou a=e(A_II) et b=e(B_II). Les deux matchings donnent a,b<=3 ; X<=8 et Y>=0 imposent b-a>=2. Il reste seulement

    (a,b) = (0,2), (1,3), (0,3).

Chaque p dans I a au moins un voisin dans sigma(E) : sa ligne propre donne t_p=2+deg_AII(p)+deg_AIE(p)-deg_BII(p)>=1. Les quatre racines externes ne sont donc pas un decor libre : elles recoivent entre6 et8 incidences opposees depuis I.

## Matrices externes forcees

La sommation sur E donne

    e(B_EE)-e(A_EE)=(16-(X-Y))/2.

Si X-Y=8, alors X=8,Y=0 et cette difference vaut4. Si X-Y=6, elle vaut5.

Un B_EE complet K4 rend chaque paire de sommets positifs externes deja commune a deux sommets negatifs externes. A_EE ne pourrait donc contenir aucune arete. Cela contredit la difference4 ou5 ; B_EE n'est jamais complet.

Pour une difference4, l'autre possibilite a examiner est e(B_EE)=5 et e(A_EE)=1. Comme Y=0, chaque sommet externe satisfait

    colonne(B_IE)=4-deg_BEE+deg_AEE <=2.

Les deux sommets de degre2 de B_EE ne peuvent toucher l'arete A_EE. Celle-ci serait donc entre les deux sommets de degre3, qui ont deja deux communs dans sigma(E). C'est impossible pour une paire adjacente (lambda=1). Il reste e(B_EE)=4,A_EE=0. La meme formule impose deg_BEE>=2 partout, donc B_EE est un C4.

Pour une difference5, la seule possibilite restante est B_EE=K4 moins une arete,A_EE=0.

## Tableau exact des regimes necessaires

| Regime | a=e(A_II) | b=e(B_II) | B_EE | A_EE | X | Y |
| --- | ---: | ---: | --- | --- | ---: | ---: |
|R1|0|2|C4|0|8|0|
|R2|1|3|C4|0|8|0|
|R3|0|3|K4 moins une arete|0|6+Y|0,1 ou2|

R1/R2 : toutes les colonnes de B_IE ont degre2. Ses lignes ont degres(2,2,1,1,1,1). En R1, les deux lignes de degre2 sont les deux sommets non couverts par B_II. En R2, ce sont les deux sommets couverts par A_II. Dans R2, ces deux lignes n'ont aucun voisin commun dans sigma(E), car leur paire est adjacente et a deja c- comme commun.

R3 : les deux sommets de l'arete manquante de B_EE ont chacun degre2 dans B_IE et degre0 dans A_IE. Les deux autres ont degre1 ou2 dans B_IE, et respectivement0 ou1 dans A_IE. Cela impose X=6+Y et Y<=2.

Toute arete A_IE en R3 est AUSSI une arete B_IE. En effet, soit p dans I adjacent a e dans E. Une telle colonne e ne peut etre qu'un sommet de degre3 dans B_EE. Si p a d voisins dans E, sa ligne propre donne1+d voisins dans sigma(E). Parmi eux, au moins1+d-[e dans B_IE(p)] sont aussi voisins de e, puisque e est adjacent aux trois autres sommets de sigma(E). Le plafond lambda=1 force d=1 et e dans B_IE(p). C'est une paire double D. Ces aretes A_IE forment un matching : deux doubles incidents a une meme orbite fourniraient quatre communs a ses deux mates, contre mu=2.

## Portee et circularite

La preuve utilise des capacites physiques(lambda,mu), le meme eigenvecteur et les deux interieurs fixes de son support. Elle n'impose pas CT=0 une seconde fois en l'appelant nouveau filtre. Elle ne requiert pas P0 ; P0 pourra ajouter la disjonction des supports de bloc pour D et l'absence d'aretes entre soeurs.

Ce tableau ne prouve pas que ces trois regimes ont des completions. Il ne les exclut pas non plus : les racines de coefficient0, les contraintes T/W globales et les budgets restants sont toujours necessaires. Aucune conclusion g>=21, aucune exclusion entiere g18/g20, ni aucun graphe ne sont revendiques.

Le petit JS joint teste les4096 paires de graphes externes etiquetes pour chaque difference et la consequence locale de lambda en R3. Il ne cherche ni les matrices globales42, ni une completion SRG.
