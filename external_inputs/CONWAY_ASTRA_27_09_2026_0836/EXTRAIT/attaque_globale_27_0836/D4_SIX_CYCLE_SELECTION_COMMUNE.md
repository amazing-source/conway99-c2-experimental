# D4⁶ avec collage du cycle six : au moins six classes doivent être choisies

**Statut : démontré par preuve couvrante, après contre-audit humain indépendant ; contrôle exact de 64 classes puis 256 familles.** Ce résultat porte sur les classes des mêmes 42 vecteurs physiques. Il ne ferme pas tout le collage D4⁶, ni g18 ou g20.

## 1. Une enveloppe intégrale explicite

Dans chaque composante D4, noter v=e_1 et s=(1/2)^4 modulo D4. Les trois classes non nulles v,s,c=v+s ont minimum 1. Soit A la matrice d'adjacence du cycle C6 sur les indices0,...,5. Au réseau D4⁶, adjoindre six classes a_i : v dans la composante i, s dans ses deux voisines, et zéro ailleurs.

Pour un masque binaire a de six sommets, la classe résultante a pour composante v a_j+s( Aa )_j. Les six générateurs sont indépendants, car leurs coefficients v sont les six vecteurs unitaires. Les produits sont entiers : chaque produit v·s=1/2 dû à une arête du cycle apparaît deux fois, et un chevauchement s·s vaut1. Le carré d'un générateur est3. Ainsi le collage est intégral impair, d'indice2⁶ dans D4⁶ ; det(D4⁶)=2¹² donne det U=1.

Le poids d'une classe est le nombre de composantes non nulles. Les accroissements de carré au sein d'une classe sont pairs, et chaque composante non nulle a minimum1. Le contrôle propre des64 masques établit que le poids minimal non nul est3 et que les seules classes de poids3 sont :

* six classes a_i, avec v en i et s aux deux voisines ;
* deux classes t_0,t_1, avec v sur l'une des deux parts {0,2,4} ou {1,3,5} et zéro ailleurs.

Il existe aussi une réduction humaine courte : |a|≥4 donne immédiatement poids≥4 ; |a|=1 donne les six bases ; |a|=2 donne poids4 ou6 selon la distance. Pour |a|=3, les gaps cycliques sont, à ordre près, (1,1,4), (1,2,3) ou (2,2,2). Seul le dernier masque ne crée aucun voisin de parité impaire hors de a, et donne les deux triades alternées.

La coque3 complète comprend donc huit classes, chacune avec8³=512 vecteurs minimaux. Les racines D4 du collage ont carré2 ; on ne confond pas le minimum3 des classes ajoutées avec le minimum2 du réseau entier.

## 2. Le petit polaire contraint chaque composante

Les quarante-deux u du repère physique engendrent N intégralement. Le gap dual de N impose que toute tranche de dimension au moins trois ne puisse porter leurs projections dans 0 et une seule classe minuscule : une trialité D4 rendrait les quatre axes intégraux contre N, et leurs projections duales de carré≤1 seraient nulles. Ils ne pourraient tenir dans N⊥ de dimension deux.

Ici les classes de coque3 utilisent seulement 0,v,s, jamais c. **Dans chacune des six composantes, les mêmes42 u doivent donc employer v et s.** Cette assertion concerne les classes effectivement utilisées, pas la simple disponibilité des huit classes de la coque complète.

Le lemme et la trialité explicite sont donnés dans [OBSTRUCTION_COQUE3_ET_D8_CUBE.md](OBSTRUCTION_COQUE3_ET_D8_CUBE.md).

## 3. Couverture simultanée du cycle : au moins six classes

Noter B l'ensemble des indices des bases a_i effectivement utilisées. Pour obtenir la lettre s en chaque composante, chaque sommet du cycle doit avoir un voisin dans B. Les deux triades n'apportent aucune lettre s.

Le cycle est biparti, avec trois sommets par part. Les voisins de chaque sommet sont deux des trois sommets de la part opposée. Une seule base dans une part manque l'un des trois sommets opposés. Il faut donc au moins deux bases dans chaque part, soit |B|≥4.

Pour couvrir v, une composante absente de B ne peut recevoir v que de la triade de sa part. On obtient exactement les familles suivantes.

| Nombre de bases utilisées | Condition sur les triades | Nombre de familles qualifiantes |
|---|---|---:|
| 4 : deux bases dans chaque part | Les deux triades sont obligatoires pour les deux sommets absents. | 9 |
| 5 | La triade de la part du sommet absent est obligatoire ; l'autre est facultative. | 6·2=12 |
| 6 | Les deux triades sont facultatives. | 4 |

Parmi les2⁸=256 familles de classes, exactement25 passent cette condition nécessaire. Le nombre de classes utilisées est au moins6 ; la distribution des familles survivantes est16 de taille6,8 de taille7 et1 de taille8.

Les231 autres familles sont impossibles pour le repère physique entier, même avant de choisir les signes ou de vérifier les produits T. Un certificat d'une famille rejetée est une composante où v ou s manque : la trialité et le petit polaire donnent la contradiction. Les25 familles restantes ne sont pas déclarées réalisables.

## 4. Certificat et limites

[controle_D4_cycle6_classes.mjs](controle_D4_cycle6_classes.mjs) construit le collage depuis C6, recalcule ses64 classes, vérifie les produits des six générateurs et les huit classes exactes de coque3, puis traite les256 sous-ensembles directement par composante. Il compare à la formule9+12+4 et imprime, pour chaque rejet, une composante et une lettre manquante. Son [résultat](controle_D4_cycle6_classes.json) est autonome.

La coupe est commune à g18 et g20, sans P0. Elle n'invoque aucune classification de lattices, aucun rang20 universel modulo2 pour D4⁶, aucun shadowframe, ni l'existence d'un graphe. Elle combine la même sélection des42 u avec les six composantes de cette enveloppe déterminée.
