# Une famille entière de sept appuis est exclue dans l'enveloppe Golay fixe

**Statut : démontré par preuve couvrante, après contre-audit humain indépendant ; contrôle de 128 polarités exactes joint.** Ce résultat porte sur les SEPT h du même repère physique, avec les deux normales fixes du contre-modèle 0803. Il ne repose pas sur un essai de septuplet et ne ferme pas tous les repères de toutes les enveloppes.

## 1. Hypothèses et lien avec le repère physique

Utiliser les coordonnées de l'enveloppe explicite du dossier 0803 : u=E/√8, h=2M/√8, r_i=B_i/√8. Les E physiques sont des mots de signes ±1 ; les sept lignes M sont des octades signées 0,±1 du code binaire C. Le même repère donne

    EᵀE + 4MᵀM + BᵀB = 56I24,
    MMᵀ = 8I7.

Les deux B sont impairs, de carré 56, avec quatre coefficients absolus 3 chacun ; leurs deux supports de gros coefficients sont disjoints. Cette structure a été acquise par les profils caractéristiques dans le template de rang 24. On ne la transporte pas à une enveloppe avec racines sans repère d'ombres.

Noter A le support de leurs huit gros coefficients. L'équation diagonale, avec 42 signes dans chaque colonne E, impose

    Σ_c M_cj² = 1 si j∈A, et 3 si j∉A.                    (1)

Ainsi les sept appuis O_c de poids 8 sont des mots de C, et chaque coordonnée appartient à une ou trois octades. Leur somme binaire est 1_24.

Le lemme ci-dessous ne suppose ni les signes de M, ni leur orthogonalité, ni la disponibilité des 42 u. Il ferme donc une famille complète d'appuis avant ces choix supplémentaires.

## 2. Lemme binaire uniforme

Soient sept appuis de poids 8 dans 24 coordonnées, avec répétitions permises, tels que chaque coordonnée apparaît une ou trois fois. Si le rang binaire de ces sept appuis est au plus quatre, alors

    A = {coordonnées apparaissant une fois}

est dans leur espace binaire engendré. En fait A est soit l'une des octades, soit le complément de la réunion de deux octades disjointes. Son poids est huit, puisque 7·8=|A|+3(24−|A|).

### Réduction au nombre de supports de multiplicité impaire

Poser V=span_F2(O_1,...,O_7) et e=1_24. La somme des sept appuis vaut e, donc e∈V. Une octade est non nulle et distincte de e. Deux octades distinctes ont des classes distinctes dans V/<e> : si elles différaient de e, leurs poids seraient 8 et 16, et non deux fois 8.

Le quotient a dimension au plus trois. Les supports distincts de multiplicité impaire ont des classes distinctes non nulles et leur somme est zéro dans ce quotient. Leur nombre est impair, au plus sept. Un seul est impossible. Cinq sont impossibles aussi : dans F2³, la somme des sept vecteurs non nuls est zéro, tandis que la somme d'un ensemble de cinq serait celle des deux vecteurs distincts complémentaires, donc non nulle. Il reste trois ou sept supports impairs.

### Trois supports impairs

Leur somme vaut e dans V, pas seulement dans le quotient : leur somme est précisément la somme des sept lignes, les répétitions paires disparaissant. Trois octades de poids total 24 dont la somme binaire est e sont disjointes et partitionnent les 24 coordonnées.

Une multiplicité de support est au plus trois, par la borne de colonne. Les seuls profils sont les suivants, à permutation près.

| Multiplicités des supports distincts | Conclusion explicite pour A |
|---|---|
| 3,3,1 | A est l'octade de multiplicité 1. |
| 3,2,1,1 | L'octade de multiplicité 3 est disjointe de l'octade de multiplicité 2, sinon une colonne apparaîtrait au moins cinq fois. A est le complément de leur réunion. |
| 2,2,1,1,1 | Les trois octades impaires forment le trio disjoint. Les deux octades de multiplicité 2 sont disjointes, sinon une colonne apparaîtrait cinq fois. A est le complément de leur réunion. |

Dans les trois cas, A est une somme binaire de e et d'appuis présents, donc appartient à V.

### Sept supports impairs : une preuve par huit caractères

Les sept appuis sont distincts, chacun apparaît une fois, et le quotient V/<e> est F2³. Ce sont ses sept classes non nulles. Une coordonnée définit une forme linéaire sur V qui prend la valeur 1 sur e ; il existe huit types possibles, indexés par x∈F2³. Noter n_x leur multiplicité.

Écrire les sept caractères non triviaux du groupe F2³ comme χ_a(x)=(-1)^(a·x). Chaque octade a une polarité σ_a∈{−1,+1} et sa valeur binaire est (1−σ_a χ_a(x))/2. Son poids huit donne

    Σ_x n_x σ_a χ_a(x) = 8.

L'inversion de Fourier, avec Σn_x=24, donne

    n_x = 3 + S_x,  où S_x=Σ_{a≠0} σ_a χ_a(x).            (2)

Sur un type présent, la multiplicité de colonne est (7−S_x)/2, donc vaut 1 ou 3 : S_x vaut 5 ou 1. Sur un type absent, (2) donne S_x=−3. Orthogonalité des sept caractères : Σ_x S_x=0 et Σ_x S_x²=56.

Si p,q,r sont les nombres de types de valeurs 5,1,−3, on obtient

    p+q+r=8, 5p+q−3r=0, 25p+q+9r=56,
    donc (p,q,r)=(1,4,3).

Le type unique x_0 où S=5 a multiplicité huit ; ce sont exactement les coordonnées A. À x_0, six caractères polarisés valent +1 et un seul vaut −1, pour un indice a_0. Après translation par x_0, les polarités sont donc toutes +1 sauf celle d'a_0. Aux quatre autres types présents, χ_a0 vaut −1 ; l'octade d'indice a_0 vaut alors zéro. Cette octade vaut un sur x_0 et sur les trois types absents. Elle est exactement A. Le lemme est prouvé dans tous les cas.

## 3. Application aux deux normales réellement construites en 0803

Dans le cas fixe, les gros coefficients sont aux coordonnées

    D1={0,1,2,9}, D2={3,4,13,15},
    A=D1∪D2, masque binaire 41503.

Le code se régénère depuis son polynôme propre, sans classification externe. A n'appartient pas à C ; un générateur qui a un produit impair avec A est imprimé dans le certificat. Comme les sept appuis O_c appartiennent à C, le lemme impose

    rang_F2 span(O_1,...,O_7) ≥ 5.                         (3)

Toutes les familles d'appuis de rang binaire ≤4 sont donc exclues **en une fois**, quels que soient les signes des sept h et les 42 u que l'on proposerait ensuite. Les appuis de rang 5,6,7 restent ouverts par cette coupe. Une paire de normales différente dont A serait une octade n'est pas fermée par ce raisonnement.

## 4. Contrôle exact et portée rootless

[controle_sept_octades_rang4.mjs](controle_sept_octades_rang4.mjs) vérifie les 128 polarités du cas à sept supports impairs, les profils de multiplicités dans F2³, et le syndrome non nul d'A dans le code propre. La preuve du §2 couvre tous les cas sans dépendre de cette enumeration. Le résultat est [controle_sept_octades_rang4.json](controle_sept_octades_rang4.json).

Le template octades est explicite dans l'enveloppe construite en 0803. Le nouveau théorème de l'auditeur montre également qu'une enveloppe unimodulaire impaire de rang 24 sans racines possède un repère d'ombres orthogonales ; le lemme binaire s'applique alors dès que son template est identifié, sans supposer un repère d'ombres supplémentaire. L'application numérique A=41503 concerne toutefois notre enveloppe et notre paire de normales fixes : elle ne prétend ni à l'unicité du code ni à l'exclusion de toutes les paires de normales.

Ce résultat complète les sept tests de capacité et de demi-somme ; il ne constitue pas un graphe, un genre fermé, ou un remplacement des contraintes mutuelles T et λ/μ.
