# Audit de deux contraintes collectives, sans fermeture generale

## 1. Sept octades de rang binaire<=4

La preuve de SEPT_OCTADES_RANG_BINAIRE_PETIT.md est correcte. Voici les points qui rendent sa couverture exhaustive.

Pour sept supports de poids8, colonnes de multiplicite1 ou3, leur somme binaire est le tout-un e. Dans V/<e>, dimension<=3, deux octades distinctes restent distinctes : une difference egale a e donnerait un poids16 a l'une d'elles. Les supports de multiplicite impaire sont donc des classes nonzero distinctes, en nombre impair, de somme0. Dans F2^3, un ou cinq sont impossibles ; il reste trois ou sept.

Avec trois, les trois octades impaires partitionnent les24 coordonnees, car leur poids total24 et leur somme tout-un interdisent tout recouvrement. La borne de colonne3 interdit une multiplicite>3. Les seuls profils possibles sont3,3,1 ;3,2,1,1 ;2,2,1,1,1. Dans les derniers profils, les deux supports repetes sont disjoints (sinon une colonne aurait multiplicite>=5). A est une octade ou le complement de deux octades disjointes, donc appartient a V.

Avec sept, chaque coordonnee est l'un des huit types de formes lineaires sur V prenant1 sur e. La transformee de Fourier des sept poids8 donne n_x=3+S_x. Un type present a S=5 ou1, un type absent S=-3. Les deux moments des caracteres donnent exactement une valeur5, quatre valeurs1, trois valeurs-3. Apres translation au type unique5, les polarites sont toutes positives sauf une. L'octade correspondante vaut1 exactement sur les huit coordonnees de multiplicite1 : c'est A.

Ainsi A est dans le span des sept octades. Pour les deux normales FIXES0803, A a masque41503 et son produit avec le generateur8391395 du code propre est impair. A n'est pas dans le code ; tout heptade de rang<=4 est donc exclu pour cette paire fixe. Cela impose rang>=5, pas rang exactement5. A peut appartenir au code pour une autre paire de normales ; aucune de ces paires n'est exclue par le lemme seul.

Le second controle joint construit directement les56 polarites admissibles depuis le type unique et l'indice exceptionnel, plutot que reutiliser la boucle productrice sur128 choix. Il verifie les poids et multiplicites, puis le coupon de syndrome.

## 2. Classification individuelle D6^4

Le modele D6^4/glue cycle4 de la note de combinatoire existe ; son Gram de coque3 est de rang24 modulo2, et aucune borne universelle20 n'est licite. Les16 classes et leurs minima ont ete controles independamment dans verifier_D11_et_coque_D6.mjs.

Ses288 caracteristiques8 sont exactement2(+/-e_i+/-e_j), avec les deux indices dans des composantes opposees. Une composante impaire d'une caracteristique coute6 ; aucun ajout ne peut completer a8, tandis que deux coordonnees paires doubles couvrent les quatre contraintes glues impaires exactement lorsqu'elles sont dans des composantes opposees.

Pour un h physique, la borne |(chi,h)|<=2 est donc equivalente aux deux inegalites max|h_A|+max|h_C|<=1 et max|h_B|+max|h_D|<=1. La classification complete des normes4 qui les passent est correcte :

* quatre unites dans une composante :4*binom(6,4)*16=960 ;
* deux unites dans chacune de deux composantes adjacentes :4*binom(6,2)^2*16=14400 ;
* spinors minimaux sur deux composantes opposees et une unite intermediaire :4*32^2*12=49152.

Une seule coordonnee2, deux-plus-deux dans des composantes opposees, ou quatre unites dans les quatre classes v, violent la borne. Les seules classes nonentieres de norme4 sont les quatre paths de deux glues adjacentes, de cout minimal3/2+1+3/2 ; elles donnent exactement le troisieme type. Les classes de parite impaire ou de minimum>4 n'ajoutent rien. Le total64512 est donc acquis pour des candidats INDIVIDUELS, pas pour sept blocs simultanes.

## 3. Deux contraintes sur les memes normales et les memes sept h

Dans D6^4, chaque u de coque3 et chaque normale de norme7 ont des demi-coordonnees dans deux composantes adjacentes. Les h fractionnaires du troisieme type ont leurs deux composantes spinor opposees. La diagonale du frame, sommee sur une paire de composantes opposees, impose44+2f=0 modulo4, donc le nombre f de tels h sur chaque paire opposee est pair. Cela autorise0,2,4 ou6 h fractionnaires, sans fermer la selection.

Pour toute racine alpha du collage U, sa projection sur span N est dans N*. Elle est nonzero : sinon alpha serait dans le primitif J=<y_1,y_2>=7I2, de minimum7. Le gap dual8/7 donne donc

    (alpha,y_1)^2+(alpha,y_2)^2 <=6.

Les deux produits sont entiers et doivent etre testes avec les MEMES normales. Le raccord utilise la primitivite de J acquise dans le collage, et ne suppose pas que les racines mixtes soient absentes.

## 4. Limites

Le heptade de rang>=5 de la paire fixe reste ouvert. Sept blocs de la classification D6^4 et leurs deux normales communes restent ouverts. Le template octades general reste uniforme seulement si le collage est sans racines, comme prouve dans ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md. Aucune famille restante n'est declaree fermee par ce seul audit.
