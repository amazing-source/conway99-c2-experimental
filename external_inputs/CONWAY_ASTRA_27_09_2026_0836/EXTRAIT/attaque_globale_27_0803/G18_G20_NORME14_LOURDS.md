# Coupe uniforme sur les coefficients lourds d'une norme2

## Cadre commun

On suppose un SRG(99,14,1,2) avec l'involution du cadre : un sommet fixe x, sept orbites interieures et42 orbites de racines. Le secteur impair est

    S = [[-I7,C],[C^t,T]],
    CC^t = 12I7, CT = 0, T^2+T = 12I42-C^t C.

Les42 colonnes de C sont les racines e_i+e_j et e_i-e_j, une paire par support {i,j}. Le changement simultane de signe d'une colonne et de sa coordonnee est seulement une convention pour representer son orbite.

Pour le raccord au reseau, H=3I49-S est le Gram de sept generateurs h_i de norme4, orthogonaux, et42 generateurs u_p de norme3. On suppose un reseau integral contenant ces generateurs et un vecteur v de norme2. Le tight frame donne

    a=( (v,h_i), (v,u_p) ),
    sum a_i^2=7||v||^2=14, Sa=-4a,
    C a_roots=-3 a_interieurs.

Le vecteur impair physique phi prend a_i et -a_i sur les deux sommets de chaque orbite, et0 sur x. Ses valeurs satisfont A phi=-4phi. Cauchy donne |a_i|<=2, puisque les normes des generateurs sont4 et3. Aucune hypothese P0 n'est utilisee dans les coupes qui suivent.

## Deux coefficients lourds sont impossibles

Ce lemme s'applique aussi directement a tout eigenvecteur impair entier de norme14 sur les49 orbites, avec coefficients dans {0,+1,-1,+2,-2}.

Soit k le nombre d'orbites dont le coefficient a une valeur absolue2, et l le nombre de coefficients de valeur absolue1. Alors4k+l=14, donc k<=3. Chacun des ensembles P={phi>0} et N={phi<0} contient m=k+l=14-3k sommets, avec k sommets de poids2.

Pour un sommet p de P de poids2, l'equation propre impose

    somme des poids des voisins de p dans N
      =8+somme des poids des voisins de p dans P >=8.

Il a donc au moins8-k voisins DISTINCTS dans N : les k poids2 peuvent apporter seulement k unites au-dela du nombre de voisins. Si k>=2, deux sommets lourds p,q de P ont au moins

    (8-k)+(8-k)-(14-3k)=2+k

voisins communs dans N. C'est au moins4, alors que toute paire distincte d'un SRG(99,14,1,2) a au plus2 voisins communs. Contradiction. Ainsi k<=1.

Cette coupe ne postule ni un type W, ni des prolongements locaux independants, ni un residu propre a une etoile.

## Raccord au minimum du reseau

Pour la suite seulement, on utilise le lemme uniforme excluant les vecteurs de norme1 : le reseau integral considere a minimum au moins2. Cette propriete est une hypothese explicite de cette section ; les booles d'un moteur ne la prouvent pas.

Si (v,u_p)=+/-2, alors v-sign((v,u_p))u_p est un vecteur du meme reseau de norme

    2+3-2*2=1.

Il est non nul et contredit ce minimum. Tous les coefficients racines appartiennent donc a {0,+1,-1}. Par le lemme precedent, il reste soit aucun coefficient lourd, soit un unique coefficient interieur a_i=2 epsilon, epsilon dans {+1,-1}.

## Un lourd interieur laisse au plus un autre interieur actif

Supposons a_i=2 epsilon. Le vecteur v'=v-epsilon h_i appartient au meme reseau et conserve la norme2. Sur une racine p incidente a i, sa coordonnee devient

    a'_p=a_p+epsilon C_ip,

car (h_i,u_p)=-C_ip. Les coefficients racines de v et de v' ont tous valeur absolue au plus1. Ainsi

    a_p dans {0,-epsilon C_ip}

sur les12 colonnes incidentes a i. La relation C a_roots=-3 a_interieurs impose que exactement6 de ces colonnes aient un coefficient non nul.

Soit r le nombre des autres interieurs actifs. Le lourd consomme4 unites de norme ; les10 restantes sont des coefficients +/-1. Il reste donc10-r racines actives, dont6 incidentes a i et4-r hors i.

Pour chaque autre interieur actif j, la charge demandee est +/-3. Les deux racines sur le support {i,j}, si toutes deux sont actives, donnent des contributions opposees a j ; si une seule est active, sa contribution vaut +/-1. Leur contribution totale a une valeur absolue au plus1. Les racines hors i doivent donc apporter une valeur absolue au moins2 a j, et comportent au moins deux incidences a j.

Il y a au total2(4-r) incidences de racines hors i. Donc2r<=2(4-r), soit r<=2. Si r=2, chaque incidence des deux racines hors i doit appartenir aux deux interieurs actifs j,k. Ces racines ont necessairement le meme support {j,k} et sont les deux racines distinctes e_j+e_k et e_j-e_k. Avec coefficients +/-1, leurs deux charges sont

    (alpha+beta,alpha-beta), alpha,beta dans {+1,-1}.

L'une est nulle, l'autre vaut +/-2. Elles ne peuvent donc apporter une valeur absolue2 aux DEUX interieurs actifs. Contradiction. Ainsi r<=1.

Il reste a imposer la parite du MEME C global. Chaque colonne D7 a une somme paire, donc C a_roots=-3 a_interieurs implique somme(a_interieurs)=0 modulo2. Le lourd est pair ; le nombre r d'autres interieurs actifs est donc pair. Comme r<=1, on obtient r=0. Le cas lourd restant a exactement la forme suivante :

| Autres interieurs actifs | Racines actives incidentes au lourd | Racines actives hors de son bloc |
| ---: | ---: | ---: |
|0|6|4|

La reflexion v -> v-epsilon h_i remplace les six racines incidentes actives par les six complementaires et change le signe du lourd. Elle ne justifie aucune equivalence entre placements physiques W/ombres.

## Portee et reste ouvert

La contradiction k>=2 est prouvee par les budgets SRG reels. Le raccord au minimum et la reduction r<=1 sont des contraintes uniformes du MEME reseau et du MEME vecteur global. Elles ne sont pas issues d'assemblages de Schur locaux.

Dans le cas sans lourd, la meme parite impose un nombre pair d'interieurs actifs. La capacite3r<=2(14-r) donne r<=5, donc r dans {0,2,4}.

Restent ouverts le cas sans lourd (14 coefficients +/-1) et l'unique forme lourde du tableau. Aucun minimum>=3 n'est acquis ici ; aucune borne g>=21 ni exclusion entiere g18/g20 n'en decoule encore. Le petit source JS joint verifie seulement les capacites finies et les identites de signes utilisees, pas l'existence ou l'inexistence d'un graphe.
