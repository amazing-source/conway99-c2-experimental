# Deux contre-audits de l'indecomposabilite uniforme

Hypotheses : N est le MEME reseau integral de rang22 de Gram H=3I-S, S=[-I7,C;C^t,T], avec H^2=7H et min N>=2. Les42 colonnes de C sont les42 racines D7. Les generateurs u_o de norme3 et h_c de norme4 satisfont

    (h_c,u_o)=-C_co,
    3h_c+somme_o C_co u_o=0,
    T^2+T=12I-C^t C.

Le minimum est la consequence deja acquise de min N*>=8/7. Aucune hypothese P0, catalogue local, solveur ou congruence de rang ne figure ici.

## Premiere preuve : connexite des42 lignes D7

Supposons N decompose en facteurs orthogonaux integraux. Tout u de norme3 appartient entierement a un facteur : deux projections non nulles auraient chacune une norme entiere>=2.

La matrice3I-T des produits entre les42 u est donc bloc-diagonale selon leurs facteurs. T et T^2 le sont aussi. Pour deux u_p,u_q appartenant a des facteurs distincts, l'identite T^2+T=12I-C^tC impose

    C_p^t C_q=0.

Or le graphe des42 lignes D7, avec une arete quand leur produit est non nul, est connexe. Deux supports de deux indices partageant exactement un indice ont produit+/-1. Deux soeurs de meme support, de produit0, sont reliees par une ligne utilisant un troisieme indice. Toutes les42 lignes sont ainsi connectees.

Il est impossible de partitionner les u en facteurs distincts sans qu'une arete non orthogonale traverse la partition. Tous les u appartiennent au meme facteur. Les sept relations3h_c+somme C_co u_o=0 mettent chaque h_c dans le meme sous-espace. Puisque tous les49 generateurs engendrent N, la decomposition est triviale.

## Deuxieme preuve : aucun bloc ne peut etre partage

Pour un facteur L_j, noter alpha_c la projection de h_c et C_j la sous-matrice des u appartenant a ce facteur. Les alpha appartiennent au facteur integral. Les produits des relations avec alpha donnent exactement

    3G=C_j C_j^t, G_cd=(alpha_c,alpha_d).

Pour c!=d, seules les deux lignes D7 de support{c,d} contribuent. Leurs contributions sont opposees. Toute sous-selection en donne0,+1 ou-1. Comme G est entier, 3G_cd ne peut prendre ces valeurs que si G_cd=0.

Le frame total est7I. L'operateur des generateurs u de ce facteur envoie alpha_c sur3alpha_c par la meme relation. L'operateur des projections h l'envoie donc sur4alpha_c. En prenant les produits avec les autres alpha,

    G^2=4G.

G etant diagonale, chaque projection h a norme0 ou4. Il n'y a pas de bloc partage en deux normes2. Une ligne D7 incidente a deux blocs a des produits non nuls avec eux ; leur facteur doit donc etre celui de u. Les21 paires de blocs forment K7 connexe, et tous les generateurs sont dans un unique facteur.

Cette seconde preuve valide aussi la preuve plus longue initiale par les familles F_c de taille<=2 et le reseau A3, mais elle n'a pas besoin de cette classification.

## Portee

N est indecomposable. Toute surlattice integrale L de minimum>=2, de MEME rang22 et contenant N, l'est egalement : le raisonnement met N dans un facteur unique, dont le sous-espace contient deja tout l'espace reel de L. Pour une extension de rang superieur, il prouve seulement que N est dans un facteur unique ; il ne ferme pas un complement orthogonal.

Ce resultat ne prouve ni min N>=3, ni g>=21, ni l'absence d'involutions. Les branches courtes de norme2 restent ouvertes.

`verifier_indecomposabilite_courte.mjs` controle les42 lignes,420 aretes, connexite et chemins explicites entre les soeurs ; les quatre sous-selections par paire donnant0,+/-1 ; et les seuls nombres d'incidences compatibles avec le Gram diagonal0/4. Ces verifications finies sont des certificats des etapes discretes, pas une recherche de graphes SRG.
