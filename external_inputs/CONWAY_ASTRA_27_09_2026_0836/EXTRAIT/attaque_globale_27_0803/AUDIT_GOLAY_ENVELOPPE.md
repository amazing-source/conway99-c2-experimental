# Audit Golay de l'enveloppe : le frame demeure essentiel

Le contre-modele `CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md` passe la relecture mathematique et une seconde implementation exacte de tous ses ingredients finis. Il satisfait une ENVELOPPE de contraintes de reseaux, mais aucun frame49 physique ni graphe SRG99 n'est realise.

## Construction et indices

Les douze translates du polynome de degre11 engendrent un code de dimension12 sur F2, et l'extension de parite le rend auto-dual en dimension24. La seconde voie utilise des tableaux de24 coordonnees et double recursivement leur span ; elle ne reprend ni les masques de bits ni la boucle sur les messages du producteur. Elle retrouve4096 mots de poids0,8,12,16,24 avec effectifs1,759,2576,759,1. Le mot constant est present, et les produits des douze generateurs sont tous pairs.

Le reseau L est forme par x/sqrt8, avec x=m*ones+2c+4t, c dans le code, et somme x divisible par8. Le poids de c etant multiple de4, cette derniere condition equivaut a somme t paire. L'addition de deux parites impaires remplace c+c' par son complement ; le mot constant du code assure la fermeture. Les poids multiples de4 et l'auto-orthogonalite rendent x.x' divisible par8.

L'index dans Z24 est2^23 pour la parite commune, puis2^12 pour le code, puis2 pour la derniere condition. Au facteur d'echelle sqrt8 en dimension24, det L=1. Pour une parite impaire, la norme est>=24/8=3. Pour une parite paire, une norme<3 requerrait soit un support modulo4 plus petit que le poids minimal8 du code, soit une unique coordonnee+/-4, qui ne satisfait pas la somme modulo8. Le minimum est donc3, et ses4096 normes3 sont exactement les vecteurs de signes du code.

Les deux y de la sortie sont dans L, orthogonaux et de normes7. Leur reseau P=7I2 est primitif : une saturation non triviale aurait index7 et determinant1 en rang2. Un reseau integral positif unimodulaire de rang2 possede une norme1, contraire au minimum3 de L. Ce dernier fait peut se voir par une base reduite : a<=c et |b|<=a/2 donnent1=ac-b^2>=3a^2/4, donc a=1.

Le complement M=P^perp intersect L a donc rang22, determinant49 et discriminant anti-isometrique a celui de P, soit(Z/7)^2. Son minimum est au moins3.

## Certificat de generation exacte

La deuxieme voie retrouve704 signes du code orthogonaux aux deux y. Elle rejoue les22 vecteurs LIVRES dans le JSON du producteur comme un certificat : membership dans le code et dans M, Gram integral et diagonale3, puis determinant49 exact.

Le determinant est calcule par elimination SYMETRIQUE rationnelle, avec fractions BigInt reduites et tous les pivots positifs. Aucun Bareiss ou choix de base modulo101 du producteur n'est repris. Le determinant49 montre que ces22 vecteurs engendrent M integralement. Le graphe de leurs produits non nuls possede131 aretes et est connexe. Sous min M=3, une norme3 doit etre pure dans une decomposition integrale ; cette connexite prouve l'indecomposabilite de M.

## Minimum dual et caracteristiques

Tout v dans M* se colle a une classe b=(k y1+l y2)/7 de P*, avec k,l entre-3 et3 ; b^2<=18/7. Si0<v^2<10/7, le vecteur v+b dans L aurait une norme entiere strictement inferieure a4, donc egale a3. Or les projections sur M des4096 signes ont toutes norme>=11/7. Les huit numerateurs et leurs effectifs, controles independamment, sont

| Numerateur sur7 |11|12|13|16|17|19|20|21|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Effectif |8|12|32|336|336|1032|1636|704|

Cela donne min M*>=10/7. On n'affirme pas que le minimum dual soit exactement10/7.

Dans L, sqrt8*e_i est caracteristique : son produit avec x/sqrt8 vaut x_i, et x^2/8 a la meme parite m que chaque x_i. Sa norme est8 ; toutes les caracteristiques de L sont donc0 modulo8. Une caracteristique chi de M se prolonge en chi+y1+y2 dans M direct-sum P, puis dans L par l'index49 impair. Elle a donc chi^2=2 modulo8. M contient des normes3, donc une caracteristique ne peut etre nulle ; min M=3 exclut le carre2 et force le carre>=10.

## Bilan adverse

Le controle est acquis : rang22, determinant49, discriminant elementaire2, minimum3, dual>=10/7, generation integrale par normes3, indecomposabilite et minimum caracteristique>=10 sont compatibles. Le reseau est sans racines de norme2.

Cette construction ne viole pas les nouvelles coupes sur les systemes de racines de grand rang : son rang des racines est0. Elle ne teste ni CT=0, ni les42 supports D7, ni les sept blocs orthogonaux, ni le tight frame7. Ces conditions portent un seul ensemble de49 vecteurs et restent le chainon manquant. Aucune involution ni SRG99 n'est construite.

`verifier_golay_enveloppe_indep.mjs/.json` a ete execute exit0 en environ0,20seconde. Un premier arret de test etait seulement la distinction JS entre+0 et-0 dans les restes ; les restes ont ete normalises avant le rejeu exact. Aucun resultat mathematique n'a ete ajuste pour faire passer le controle.
