> Mise à jour : **A33 est maintenant entièrement exclue**, y compris à g⁻20. Voir [la fermeture par le signe de Witt](../fermeture_A33/PREUVE.md). Le présent rapport conserve l’étape antérieure sur les coupures et les certificats.

# Deux avancées : coupures de blocs et torsion de l’étoile A33

26 septembre 2026. Recherche conduite seul. Dépôts amazing-source lus strictement en lecture seule ; petits calculs exacts exécutés à distance sur SageMathCell. Aucun calcul lourd local.

## 1. A111111 (3,3) : g⁻=20 est maintenant forcé

**Démontré par quinze certificats entiers, vérifiés par une seconde implémentation**, complétés par une exclusion humaine déjà connue de C1.

L’espace de torsion possède 400 directions projectives. La réduction par le groupe de 72 automorphismes donne 17 classes. Les certificats excluent quinze classes, et la preuve élémentaire exclut une autre : il reste une seule classe, de douze directions. Parmi les 375 directions mixtes laissées par C1, **363 sont ainsi éliminées**.

Toutes les coordonnées de chaque direction restante sont non nulles. L’évaluation en une étiquette est donc injective sur l’espace équilibré V₀ : **r₀=dim V₀≤1**. La formule de C1

    g⁻=22−2r₀+ρ, ρ≥0,

et son plafond g⁻≤20 imposent alors **r₀=1, ρ=0 et g⁻=20**. Toute la strate A33 à g⁻=16 ou 18 est exclue.

**Limite :** A33 à g⁻=20 reste indécis. Le résultat ne ferme ni toutes les étoiles sans classe fermée ni l’involution générale.

Le nouvel objet utile est le système des **ombres appariées avec leurs centres et leurs charges entières**. Une paire d’ombres est sécante ou disjointe ; les comptes K₃ imposent douze centres distincts et dix-huit paires disjointes. Le certificat couple cette partition à la bijection des soixante ombres, à K₂, à K₃ et à l’énergie exacte des charges. Les contraintes traitées séparément laissaient passer ces classes.

[Preuve complète A33](PREUVE_A33.md). [Quinze certificats avec tous les coefficients](certificats_A33.json). [Vérificateur indépendant](verifier_A33_independant.py). [Sorties exactes](sorties_A33_independantes.txt).

Le vérificateur reconstruit les 400 points et leurs 17 orbites, puis contrôle chaque inégalité entière sur tous les choix admissibles. Certaines marges sont d’une seule unité ; elles sont contrôlées sans flottants. Il utilise seulement la bibliothèque standard Python et peut être lancé dans une cellule distante avec le JSON joint. Aucun lancement local n’est requis. Le programme de recherche utilise NumPy et un algorithme d’affectation écrit ici ; aucune garantie d’optimalité n’est nécessaire pour vérifier un certificat.

## 2. Norme 10 : toute la strate à cinq blocs est fermée

**Démontré à la main**, sous la réduction plate stable : valeurs +1 sur m racines, −1 sur leurs images par l’involution, supports de même signe stables, quatre voisins de signe opposé par racine. La norme carrée en coordonnées d’orbites vaut m ; le support réel a 2m sommets. **Aucune hypothèse P=0 n’intervient** dans ce nouveau résultat.

Le nouvel objet est le multigraphe des orbites racines extérieures, pondéré par leur nombre t de voisins positifs. Les degrés pondérés sont prescrits bloc par bloc. Deux blocs inutilisés imposent l’égalité des poids à l’intérieur de leur paire et à l’intérieur des cinq autres blocs. Le budget exact des défauts rend cette égalité impossible :

    m²−17m+62 ≥0 serait nécessaire.

Cette condition échoue pour **m=6,…,11**. À m=10, les deux côtés sont séparés d’au moins quatre unités. Cela ferme uniformément tous les supports de norme 10 à cinq blocs.

À six blocs, il reste seulement trois profils extérieurs (N₀,N₁,N₂,N₃) :

    (1,24,5,2), (2,21,8,1), (3,18,11,0).

Aucun poids ≥4 ; les deux petits blocs portent au plus une orbite sélectionnée entre eux. S’ils en portent une, toutes les inégalités se saturent et localisent les zéros et les poids 3. **La strate à six blocs est rigidifiée, pas exclue. Celle à sept blocs reste ouverte.** La norme 9 entière n’est pas fermée non plus.

[Preuve humaine et portée exacte](PREUVE_COUPURE_NORME10.md). [Vérification indépendante et contrôles](verifier_coupure_norme10.py). [Sorties](sorties_normes_et_controles.txt).

## 3. Contrôles et dernier cas concret

Les vrais graphes H(2,3) et BvLS passent exactement la bijection et les matrices K₂/K₃ avec leurs propres paramètres. Une fonction propre plate impaire de H(2,3) passe aussi le double comptage global ; elle est non nulle sur des intérieurs et ne relève pas du théorème « racines seulement ».

Le représentant A33 restant est

    (1,2,4,1,2,4 ; 3,5,6,3,5,6) mod 7.

Les deux composantes portent les résidus quadratiques non nuls et leurs opposés. Il reste à réaliser ses soixante ombres en respectant simultanément K₂/K₃ et ρ=0, puis à vérifier la compatibilité avec les autres blocs et les résidus lointains. La dernière borne trouvée vaut 83,9623 pour une énergie imposée de 84 : **elle ne prouve rien contre cette classe**.

Une exploration supplémentaire, restreinte aux bijections équivariantes pour l’action multiplicative F₇×, a épuisé 1 163 nœuds sans solution. Ce test n’a qu’une implémentation et impose une symétrie supplémentaire ; il n’est utilisé dans aucune des conclusions démontrées. [Programme exploratoire](exploration_F7_equivariante.py).

Les coupures de Schur conjointes et le relèvement modulo 4 précédemment certifiés restent disponibles pour le raccord global. Aucune nouvelle exclusion de la branche sans symétrie n’est acquise dans cette reprise.

## 4. Reprise et sources

[État de reprise](ETAT_REPRISE.md). [Empreintes des artefacts](SHA256SUMS.txt).

Réductions créditées à [C1, note 129](https://github.com/amazing-source/conway99-c1/blob/c4b22393b28cd1f400ab291d3152a3be8d85bf3a/notes/129_Q7_SECTEUR_IMPAIR_INVOLUTION.md) et à [structures, formulation compacte](https://github.com/amazing-source/conway99-structures-lab/blob/2e13d68e155d9de862e8d7c8fe14441d11a70184/astra/PROBLEMES_OUVERTS_INVOLUTION.md). Nos certificats et la coupure nouvelle sont décrits séparément de ces acquis.

Ni l’involution exclue ni l’involution imposant un prisme ne sont établies. La poursuite programmée reste active.
