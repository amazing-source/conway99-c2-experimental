# Classification uniforme de l’enveloppe contenant D6^4

## Théorème
Soit U un réseau entier unimodulaire positif de rang24, minimum au moins2, portant le repère physique42+7 et les deux normales7. Si U contient quatre D6 orthogonaux de rang total24, alors, à permutation et échange des deux classes spinorielles près, son collage est le cycle C4 décrit dans G18_G20_D6_QUATRE.md. L’alternative à deux doubles arêtes contient D12, déjà exclu par la preuve indépendante0803. Aucune classification publiée de réseaux n’est utilisée.

## Preuve par le groupe discriminant
Poser R=D6^4. Son discriminant est F2^8, en prenant pour chaque D6 les deux classes spinorielles s,c de minimum3/2. Leurs produits discriminants multipliés par2 sont diag(1,1) ; s+c est la classe vectorielle v de minimum1. Puisque detR=4^4, le collage H=U/R a cardinal16 et est un code binaire autodual de dimension4. Il est orthogonal à lui-même pour le produit standard, donc tous ses mots ont poids pair. Le mot tout-un appartient à H, puisqu’il est orthogonal à tous ces mots pairs.

Pour un mot de poids binaire w, avec t composantes ayant les deux bits s,c, le minimum de sa classe vaut

    (3/2)(w-2t)+t =3w/2-2t.

La parité de norme vaut donc w/2 modulo2. Si tous les poids de H étaient divisibles par4, U serait pair. Or les42 vecteurs physiques ont norme3. H contient donc un mot de poids2 ou6 ; son complément donne un mot de poids2.

Un mot de poids2 force les deux coordonnées correspondantes à être égales sur tous les mots de H. Ce bloc I2 se scinde dans le code. Le code résiduel autodual de longueur6 possède lui aussi un mot de poids2 : sans cela ses sept mots non nuls auraient poids au moins4, pour une somme au moins28, tandis que la somme exacte des poids est8·6/2=24. Chaque coordonnée prend bien les deux valeurs, sinon un mot de poids1 serait dans le dual et dans le code. Le même argument à longueur4 donne12>8. À longueur2, le dernier code est I2.

Ainsi H est constitué de quatre paires disjointes des huit symboles spinoriels. Une paire située dans le même D6 ajouterait v, de minimum1, impossible. Le multigraphe sur les quatre composantes D6 a donc degré2, sans boucle. Il est soit un cycle C4, soit deux cycles à deux arêtes parallèles.

Dans une double arête entre deux D6, la somme des glues ajoute (v,v), de minimum2. Toutes ses racines ±e_i±e_j reliant les deux composantes sont présentes ; avec leurs D6 elles engendrent D12. Cette possibilité est exclue par G18_G20_D12_COLLAGE.md de la campagne0803.

Le cycle C4 est donc la seule enveloppe possible dans cette famille. Les échanges s↔c sont des changements de signe d’un axe dans D6 ; toutes les orientations du cycle sont isométriques.

## Contrôle fini indépendant de la preuve du code
Le source classer_collage_D6_quatre.mjs parcourt seulement les105 couplages parfaits de huit symboles. Il trouve45 couplages comportant une boucle (minimum1),12 avec deux doubles arêtes (D12),48 réalisations du même cycle C4. Il vérifie également les deux inégalités de somme des poids. Ce contrôle n’énumère aucun type local ni graphe SRG.

## Portée
Cette classification rend les coupes physiques dans le cycle C4 uniformes pour toute cette famille d’enveloppes. Elle ne ferme pas D6^4 à elle seule. L’exclusion collective de six blocs fractionnaires dans une paire opposée est une preuve distincte ; les répartitions0/2/4 et les répartitions mixtes restent ouvertes. Les autres systèmes de racines de U ne sont pas couverts ici.
