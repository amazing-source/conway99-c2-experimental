# Test global de capacite des sept blocs dans une enveloppe Golay explicite

## Hypotheses supplementaires

Ce test est CONDITIONNEL. On utilise l'enveloppe explicite U_Golay de la campagne0803, avec les coordonnees entieres divisees par sqrt(8), les4096 mots du code binaire engendre par le polynome donne, et deux charges r_1,r_2 de norme7 orthogonales. Leurs coordonnees sont les deux lignes B. Toutes les normes3 de U_Golay sont les mots de signes E correspondants aux4096 mots du code. La coque complete de norme3 de leur orthogonal N0 se reconstruit en imposant EB^t=0.

Le helper n'affirme pas que tout collage uniforme de rang24 soit cette enveloppe, ni qu'un shadowframe existe en general. La coque704 du choix0803 est un cas fixe de cette reconstruction, pas une hypothese imposee a des charges arbitraires.

Une selection candidate de SEPT blocs se code par M : h_c=2M_c/sqrt(8), chaque ligne est une octade signee, MM^t=8I. Le template physique demande huit colonnes de poids1 et seize de poids3.

## Premiere coupe : la demi-somme doit etre un vecteur entier du reseau

Pour le vrai reseau physique N, poser z=(sum_c h_c)/2. Ses produits avec les h sont2 et ses produits avec les u sont-(sum_c C_cp)/2, des entiers. Donc z appartient a N*, tandis que2z appartient a N. Comme det(N) est impair, N*/N n'a aucune2-torsion et z appartient a N. Sa norme vaut7.

Dans les coordonnees du template, Z=sum_c M_c. Chaque coordonnee est impaire, et vaut+/-1 ou+/-3. L'orthogonalite des sept lignes donne sum_j Z_j^2=56, donc exactement QUATRE coordonnees ont valeur absolue3. Elles appartiennent aux seize colonnes de poids3, hors des huit gros coefficients des deux charges B.

Pour que Z/sqrt(8) appartienne a U_Golay, il faut simultanement

    support des (Z_j-1)/2 modulo2 dans le code Golay,
    sum_j Z_j divisible par8.

Une violation ferme la selection des sept blocs entiere, dans cette enveloppe. Tester une seule jauge suffit : changer les signes des h modifie z par des vecteurs h entiers. Les64 lignes de demi-sommes signees, modulo signe global, sont ainsi toutes presentes et de norme7. Ce n'est pas une assertion qu'une selection quelconque de sept octades orthogonales satisfait le test.

## Deuxieme coupe : les42 directions D7 doivent etre disponibles simultanement

Pour une ligne de norme3 candidate u=E/sqrt(8), les produits avec les sept blocs sont

    (h_c,u)=M_c E/4.

Une racine physique doit avoir exactement DEUX produits non nuls, chacun+1 ou-1. A signe global de u pres, chaque support {c,d} doit fournir les DEUX directions orthogonales : les signes egaux et les signes opposes. Cela fait42 classes, distinctes deux a deux.

Pour chaque bloc, preparer trois ensembles de lignes de la coque complete : Z_c pour le produit0, P_c pour+1 et N_c pour-1. Pour un support {c,d}, poser

    F_cd=intersection des Z_k pour k hors {c,d},
    classe+ =F_cd intersect ((P_c intersect P_d) union (N_c intersect N_d)),
    classe- =F_cd intersect ((P_c intersect N_d) union (N_c intersect P_d)).

Si l'une de ces42 classes est vide, AUCUNE selection des42 u de cette enveloppe ne peut prolonger les SEPT blocs fixes. Les intersections se font par bitsets, sans produit cartesien de completions d'etoiles. Les valeurs +/-2 ou superieures ne sont admises dans aucune classe.

Un PASS signifie uniquement que chaque classe possede au moins un candidat. Il n'impose pas les produits mutuels T, les dix voisins de chaque ligne, CT=0, les budgets lambda/mu, P0, le frame ou l'indice de generation. Les42 vecteurs devront ensuite appartenir a UNE MEME selection satisfaisant tout cela. [G18_G20_QUARANTE_DEUX_GENERATEURS.md](G18_G20_QUARANTE_DEUX_GENERATEURS.md) fixe l'indice physique necessaire.

## Source et certificat

[G18_G20_SEPT_BLOCS_CAPACITE.mjs](G18_G20_SEPT_BLOCS_CAPACITE.mjs) est un module sans execution a l'import. Il reconstruit le code et la coque sur appel, puis retourne les masques des42 classes. Il controle aussi l'alignement de chaque colonne de M avec B :4*poids(M_j)+B_1j^2+B_2j^2=14. Une refutation contient la selectionM complete, les chargesB, leurs hashes, le hash du code/de la coque et la classe vide ou le defaut de demi-somme. La completude est fournie par la reconstruction depuis les4096 mots, pas par une liste arbitraire de candidats. Un rejeu independant doit refaire cette reconstruction et comparer les hashes ; le champ booleen complete_shell_reconstructed n'est jamais une preuve a lui seul.

Les petits tests joints comparent les intersections de bitsets a des profils abstraits explicites. Ils verifient aussi l'appartenance exacte des deux charges0803 au reseau Golay. Ce sont des tests de source, pas des graphes positifs ni une couverture de toutes les sept selections. Aucun type ou genre g18/g20 n'est exclu par la livraison du helper seule.
