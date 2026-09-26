# Deux campagnes complètes : torsion A33, coupure de norme 10 et fermeture par le signe de Witt

26 septembre 2026 — dossier autonome, preuves, certificats complets, programmes et sorties exactes.

Ce document réunit les campagnes « coupures et torsion » et « fermeture A33 ». Les trois preuves sont d’abord présentées pour lecture ; une archive textuelle contient ensuite les **23 fichiers originaux**, avec leurs empreintes et un extracteur permettant de les reconstituer sans dépendre des fichiers du projet.

## Résultats au terme des deux campagnes

| Sujet | Première campagne | Deuxième campagne : état actuel |
|---|---|---|
| A111111 (3,3) | Quinze certificats et un cas humain éliminent 388/400 directions, dont 363/375 directions mixtes ; r₀≤1, donc g⁻=20 et ρ=0 sont forcés. | **Toute la strate est exclue**, sans hypothèse P=0 : le signe de Witt impose g⁻≥24−2r₀≥22, contre g⁻≤20. |
| Norme 10, cinq blocs | **Exclusion uniforme sous la réduction plate stable**, sans hypothèse P=0. La coupure sépare deux sommes supposées égales d’au moins quatre unités. | Résultat conservé. |
| Norme 10, six blocs | Trois profils (N₀,N₁,N₂,N₃) : (1,24,5,2), (2,21,8,1), (3,18,11,0). Au plus une orbite sélectionnée entre les deux petits blocs ; rigidité supplémentaire au cas d’égalité. | **Ouvert**. |
| Involution générale ; autres étoiles ; normes 9/10 restantes | Ouverts. | **Toujours ouverts**. |

Les exclusions A33 s’appuient sur les réductions et les faits de genre de C1/structures explicités dans les preuves. La coupure de norme 10 suppose la réduction plate stable explicitement décrite ; elle ne ferme pas toutes les normes 10.

**Documents historiques.** Les mentions « dernière classe indécise », « A33 à g⁻=20 ouvert » et le champ full_A33_excluded=false dans le JSON original décrivent la fin de la première campagne. La preuve de la deuxième campagne ferme précisément ce résidu. Les coefficients des quinze certificats sont conservés sans modification. Une tentative non concluante ou une restriction d’équivariance ne devient pas un certificat d’exclusion.

## Sommaire

- [Première campagne A33 : certificats et dimension équilibrée](#preuve-a33-campagne1)
- [Coupure : norme 10 à cinq blocs, profils à six blocs](#preuve-norme10)
- [Fermeture complète A33 par le signe de Witt](#preuve-a33-fermeture)
- [Index et archive intégrale des 23 fichiers](#archive-integrale)
- [Extraire les fichiers et reproduire les vérifications](#reproduction)

Les vérifications déjà effectuées ont tourné à distance. Cet assemblage ne relance aucun programme de recherche ni aucun solveur sur le PC.

<a id="preuve-a33-campagne1"></a>

## Première campagne — A33 : preuve et certificats

Étape antérieure : la dernière classe y est encore ouverte. Sa fermeture est donnée dans la troisième preuve.

### A111111 (3,3) : torsion équilibrée de dimension au plus un et g⁻=20 forcé

26 septembre 2026. **Démontré par certificats entiers, vérifiés par un second programme indépendant**, puis conséquence humaine sur la dimension. Le cas A33 à g⁻=20 reste ouvert.

#### Résultat concret

Pour l'étoile A111111 (3,3), les 400 directions projectives de torsion se répartissent en 17 classes. Quinze classes sont exclues par nos nouveaux certificats ; une se ferme par une obstruction élémentaire déjà connue. Il reste **une classe de douze directions**.

Toutes ces directions sont non nulles en chacune des douze coordonnées. Cela donne immédiatement **r₀≤1**, où r₀ est la dimension de la torsion équilibrée. Avec la formule de C1 et son plafond g⁻≤20, on obtient

    r₀=1, ρ=0, g⁻=20.

Ainsi **A111111 (3,3) est impossible à g⁻=16 et à g⁻=18**. Son existence à g⁻=20 n'est pas tranchée. Ni l'involution générale ni l'étoile totalement libre générale ne sont exclues.

L'état précédent de C1 laissait 375 directions mixtes dans treize classes : nos certificats en éliminent **363**, et douze demeurent indécises. Il s'agit d'une exclusion sur toutes les données de cette strate, sans tirage aléatoire de boules.

#### 1. Cadre exact

Les douze étiquettes sont 0,…,11 ; σ(i)=i xor 1. Ici μ=σ et

    τ=(0 5)(1 2)(3 4)(6 11)(7 8)(9 10).

Les deux composantes du graphe alterné σ/τ sont C₆ et C₆. Les racines lointaines z sont les soixante paires d'étiquettes de blocs différents, groupées en trente paires z/σz. Les ombres e=Φ(z) parcourent exactement une fois les soixante arêtes de K₁₂−μ.

Les contraintes compactes de structures sont :

    #{z : a∈z, b∈Φ(z)} = K₂[a,b],
    #{z : b∈Φ(z), d∈Φ(σz)} = K₃[b,d],

avec

    K₂[a,b]=2−[a=b]−2[b=σa]−[b=τσa],
    K₃[b,d]=2−[d=σb]−[d=τb]−[d=τσb]−[d=στb].

La bijection et ces deux matrices sont nécessaires dans une vraie SRG avec involution. Le problème traité n'impose aucune absence de prismes.

La torsion est ker₇(I+P_σ+P_τ), de dimension quatre. Sur chaque composante, elle s'écrit

    (a,b,−a−b,a,b,−a−b) mod 7.

Une torsion φ est équilibrée si, pour chaque paire z/σz,

    φ(Φ(z))−φ(Φ(σz))+2[φ(z)−φ(σz)] ≡ 0 mod 7.       (1)

φ(e) désigne la somme des deux valeurs de φ sur une paire e.

Sources des réductions : [C1, note 129](https://github.com/amazing-source/conway99-c1/blob/c4b22393b28cd1f400ab291d3152a3be8d85bf3a/notes/129_Q7_SECTEUR_IMPAIR_INVOLUTION.md) et [structures, formulation compacte](https://github.com/amazing-source/conway99-structures-lab/blob/2e13d68e155d9de862e8d7c8fe14441d11a70184/astra/PROBLEMES_OUVERTS_INVOLUTION.md). Dépôts consultés exclusivement en lecture seule.

#### 2. Objet utilisé : les ombres appariées et leur centre

La bijection transporte l'involution sur les soixante arêtes. Une paire e/f est soit sécante, avec un centre b=e∩f, soit disjointe.

K₃[b,b]=2 pour chaque b ; une paire sécante contribue deux à cette entrée. Donc les trente paires d'ombres contiennent exactement **douze paires sécantes, une de chaque centre**, et dix-huit paires disjointes. Ce fait était déjà connu ; l'avancement est de le coupler simultanément à l'usage unique de chaque ombre, aux deux matrices de comptes et au relèvement entier de (1).

Pour une direction projective, choisir un représentant entier

    ψ=(a,b,−a−b,a,b,−a−b ; c,d,−c−d,c,d,−c−d).

Alors les trente charges

    q_z=[ψ(e)−ψ(f)+2(ψ(z)−ψ(σz))]/7

sont entières sous (1). L'énergie exacte, déjà obtenue par C1, est

    Σ q_z² = E(ψ) = 3‖ψ‖²/2.                          (2)

Le nouveau test contraint ces charges et leurs centres **avec toutes les ombres et tous les comptes**, et non par leurs seules sommes séparées.

##### Vérification indépendante de l'énergie

Soient Y et W les matrices d'incidence des ombres et des racines, et R la permutation z↔σz. On a

    YYᵀ=9I+J−P_σ,    YRYᵀ=K₃,
    WWᵀ=9I+J−P_σ,    WRWᵀ=J−I+9P_σ,
    WYᵀ=K₂.

Le carré total des charges avant division par 49 est donc

    ψᵀ(YYᵀ−K₃)ψ
      +4ψᵀ(WWᵀ−WRWᵀ)ψ
      +4ψᵀK₂ᵀ(I−P_σ)ψ.

Sur le sous-espace périodique indiqué, ψᵀP_σψ=−‖ψ‖²/2 et (I+P_σ+P_τ)ψ=0. La formule se réduit à 49·3‖ψ‖²/2. Le second programme vérifie aussi cette réduction par arithmétique entière, séparément de la génération des certificats. K₂ n'étant pas symétrique, le produit croisé doit être écrit dans cet ordre ; le vérificateur initial avait une transposition erronée, corrigée avant les sorties finales.

#### 3. Forme du certificat : une inégalité par choix d'ombres

Pour chaque paire lointaine Z, on énumère tous les choix ordonnés e/f distincts qui :

- respectent les zéros de K₂ ;
- ne dépassent individuellement aucune capacité de K₃ ;
- vérifient la congruence (1).

Tout choix d'une vraie solution figure dans ce domaine. On ne suppose pas que ces conditions individuelles suffisent à construire une solution.

Un certificat contient des coefficients entiers :

- λ_e pour chacune des soixante ombres ;
- γ_ab et δ_bd pour les deux matrices de comptes ;
- α_b pour les douze centres, α_* pour une paire disjointe ;
- β_Z pour les trente paires lointaines ;
- une échelle entière s, valant 100 ou 1000.

Sur chaque choix admissible, le vérificateur contrôle exactement

    s q_Z² ≥ λ_e+λ_f
              + γ·contribution_K₂(Z,e,f)
              + δ·contribution_K₃(e,f)
              + α_centre + β_Z.                       (3)

En sommant sur une solution, les ombres apparaissent chacune une fois, les centres chacun une fois, les dix-huit paires disjointes chacune avec α_*, et les matrices valent exactement K₂ et K₃. Ainsi

    sE ≥ Σλ + γ·K₂ + δ·K₃ + Σ_b α_b +18α_*+Σ_Z β_Z.

Le membre de droite est le nombre B du certificat. Si B>sE, contradiction. **Aucun arrondi ni calcul flottant n'intervient dans la validité.**

Les coefficients ont été trouvés par une recherche de potentiels entiers et un algorithme d'affectation écrit ici. Leur validité ne dépend ni de la convergence de cette recherche ni de son résultat optimal : le second programme relit chaque colonne et contrôle (3).

#### 4. Couverture des directions et sorties exactes

Le groupe qui préserve σ et τ a 72 éléments. Le vérificateur le reconstruit par permutations, puis reconstruit les 400 points de l'espace projectif P³(F₇). Il vérifie que les dix-sept orbites sont disjointes et couvrent tous les points.

| Classe | Taille projective | Multiplicateur du représentant | E | Échelle s | B | Verdict |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 6 | 1 | 6 | 100 | 900 | exclue |
| 1 | 6 | 1 | 18 | 100 | 2000 | exclue |
| 2 | 4 | 1 | 42 | 100 | 4249 | exclue |
| 3 | 18 | 1 | 12 | 100 | 1245 | exclue |
| 4 | 36 | 1 | 30 | 100 | 3021 | exclue |
| 5 | 36 | 1 | 24 | 100 | 2401 | exclue |
| 6 | 72 | 2 | 66 | 1000 | 66014 | exclue |
| 7 | 36 | 1 | 84 | 1000 | 84017 | exclue |
| 8 | 36 | 1 | 78 | 1000 | 78060 | exclue |
| 9 | 9 | 1 | 36 | — | — | domaine impossible, preuve humaine |
| 10 | 36 | 1 | 60 | 100 | 6021 | exclue |
| 11 | 18 | 1 | 96 | 100 | 9659 | exclue |
| 12 | 18 | 1 | 90 | 1000 | 90001 | exclue |
| 13 | 9 | 1 | 36 | 1000 | 36014 | exclue |
| 14 | 36 | 1 | 60 | 1000 | 60019 | exclue |
| 15 | 12 | 1 | 84 | 1000 | 84054 | exclue |
| 16 | 12 | 1 | 84 | 10000 | 839623 | **indécise**, cette borne n'exclut rien |

La classe 6 a été certifiée après multiplication par 2 modulo 7 et choix d'un autre représentant entier périodique. Cela conserve exactement la condition d'équilibre projective. La validité de la nouvelle inégalité et de sa nouvelle énergie est vérifiée séparément.

Pour la classe 9, ψ=(1,1,−2,1,1,−2) sur les deux composantes. Les sommes sur les ombres prennent les résidus {2,3,6}, dont les différences valent {0,1,3,4,6}. Pour z={2,5}, la congruence exige la différence 5, impossible. Cette exclusion reproduit celle de C1 ; elle n'est pas présentée comme nouvelle.

Les quinze certificats ont été vérifiés indépendamment, sur tous les choix admissibles. Les fichiers contiennent les coefficients complets, pas seulement ces nombres.

#### 5. Conséquence humaine : la dimension équilibrée s'effondre

La classe restante est représentée par

    φ=(1,2,4,1,2,4 ; 3,5,6,3,5,6) mod 7.

Chaque composante utilise, deux fois chacune, les trois résidus quadratiques non nuls ou leurs opposés. Toutes les douze coordonnées sont non nulles. L'action du groupe et la multiplication scalaire préservent cette propriété.

Soit V₀ l'espace linéaire des torsions équilibrées d'une éventuelle solution. D'après les certificats, tout φ∈V₀ non nul a φ(0)≠0. L'application linéaire

    V₀ → F₇, φ ↦ φ(0)

est donc injective. **dim V₀=r₀≤1.** C'est une preuve humaine, sans classification supplémentaire des plans projectifs.

En contrôle distinct, le programme vérifie que les douze directions restantes ne contiennent aucune des huit directions d'une droite projective entière ; leur intersection avec une telle droite est au plus trois.

Pour A33, t=4. La formule démontrée par C1 donne

    g⁻=18+t−2r₀+ρ =22−2r₀+ρ,   ρ≥0.

Avec g⁻≤20 et r₀≤1, nécessairement

    r₀=1, ρ=0, g⁻=20.

C'est le raccord qui manquait entre l'exclusion finie des directions et un résultat uniforme sur le rang.

#### 6. Contrôles, limites et prochaine cible

Les vrais graphes H(2,3) et BvLS passent la bijection et les deux matrices compactes, avec leurs propres paramètres. Ils ne sont pas des étoiles A33 : on ne leur applique pas cette exclusion.

La recherche de la classe 16 n'a produit ni certificat d'impossibilité ni solution intégrale de Φ. Une borne 83,9623 pour une énergie imposée de 84 est **insuffisante**, quelle que soit sa proximité. La restriction multiplicative F₇× est une tentative supplémentaire ; elle n'autorise aucune conclusion générale si elle échoue.

Le verrou s'est réduit à une direction équilibrée unique, de type résidus quadratiques opposés, avec g⁻=20 et ρ=0. La prochaine question porte sur la réalisation de ses soixante ombres, ou sur la compatibilité de ces conditions avec le résidu lointain et les autres blocs. Les étoiles totalement libres à t=0 et les autres types ne sont pas fermés par ce résultat.

Fichiers : [certificats_A33.json](#source-06) ; [verifier_A33_independant.py](#source-13) ; [chercher_certificat_A33.py](#source-07) ; [sorties_A33_independantes.txt](#source-09). Les programmes ont tourné à distance sur SageMathCell. Aucun SAT, CP, PLNE ou solveur externe n'a été utilisé ; aucun calcul lourd local ni dépôt distant modifié.

<a id="preuve-norme10"></a>

## Première campagne — norme 10 : coupure et profils

Hypothèse indispensable : réduction plate stable, avec support uniquement sur les racines.

### Coupure de deux blocs inutilisés : fermeture de la norme 10 à cinq blocs

26 septembre 2026. **Démontré à la main.** Les vérifications numériques ci-jointes ne remplacent pas la preuve. Aucun solveur ni calcul lourd local.

#### Hypothèses et portée

On suppose Γ = srg(99,14,1,2), muni de l'involution fixant x et retournant les sept blocs. On travaille sous la **réduction plate stable** d'un vecteur de L_T : +1 sur P={p_i}, −1 sur Q=σP, zéro ailleurs ; P et Q sont stables, ont chacun m sommets racines, et chaque p_i a quatre voisins dans Q. Sa norme carrée en coordonnées d'orbites vaut m ; le support dans Γ a 2m sommets.

Le résultat ci-dessous n'utilise **pas P=0**. Il ne prouve pas que tous les vecteurs de norme 10 sont impossibles. Il ferme toute leur strate à cinq blocs, sous les hypothèses explicites précédentes.

#### 1. Nouvel objet de travail : le multigraphe pondéré des racines extérieures

Pour z hors de P∪Q, l'équation propre donne t_z=|N(z)∩P|=|N(z)∩Q|. L'involution conserve t. Une orbite racine extérieure est représentée par une arête entre ses deux blocs, de poids t. Chaque paire de blocs comporte deux orbites ; celles sélectionnées dans P∪Q sont retirées.

On note h_c le nombre de points de P contenant c_+, égal au nombre contenant c_−. Ainsi Σ h_c=m et le bloc c touche 2h_c orbites sélectionnées.

Les comptes déjà établis donnent, sur les **orbites racines extérieures** :

    Σ t = 4m ;
    Σ_{orbites incidentes à c} t = 2m − 6h_c.             (1)

La première égalité vient du compte global Σ_{sommets extérieurs}t=10m, après retrait des intérieurs : leur contribution est 2Σh_c=2m, puis on divise par deux.

Posons p(0)=0 et p(t)=(t−1)(t−2)/2 pour t≥1. Soient R₀ le nombre d'orbites racines extérieures de poids zéro, et Π=Σ p(t) sur toutes les orbites racines extérieures. Si u blocs sont inutilisés, le compte exact des sommets extérieurs de poids zéro donne

    R₀ + Π + Σ_{c:h_c>0} p(h_c)
        = (m² − 19m + 98)/2 − u.                       (2)

Tout terme du membre de gauche est non négatif.

Ce multigraphe n'est pas un graphe SRG construit. C'est un objet nécessaire dont les degrés pondérés et le coût des défauts sont fixés exactement.

#### 2. Théorème de la coupure

**Théorème.** Sous les hypothèses ci-dessus, si 6≤m≤11, le support utilise au moins six blocs.

Supposons deux blocs inutilisés a,b, et prenons I={a,b}. Les orbites extérieures se répartissent en celles internes à I, celles traversant sa coupure, et celles dans les cinq autres blocs.

Notons T_I et T_F les sommes des poids dans les deux parties internes. Par (1), la somme des degrés pondérés en a et b vaut 4m, égale à la somme de tous les poids. Donc

    2T_I + T_coupure = T_I + T_coupure + T_F,
    soit T_I = T_F.                                     (3)

Il y a deux orbites dans I. Dans les cinq autres blocs, il y a 2·C(5,2)−m=20−m orbites extérieures, puisque tout le support y est contenu. Ainsi

    T_F ≥ 20−m−R₀.

Pour tout entier t≥0, t≤2+p(t). Les deux orbites de I vérifient donc

    T_I ≤ 4+Π.

Comme u≥2, (2) impose

    R₀+Π ≤ (m²−19m+94)/2.

En combinant avec (3), on obtient la condition nécessaire

    20−m ≤ 4+(m²−19m+94)/2,
    soit m²−17m+62 ≥ 0.                                 (4)

Mais le polynôme est strictement négatif pour chaque entier m=6,…,11. Contradiction. ∎

**À m=10 :** R₀+Π≤2, T_F≥10−R₀ et T_I≤6−R₀. Les deux sommes censées être égales sont séparées d'au moins quatre unités. C'est une exclusion uniforme, sans choix d'étiquetage.

**Corollaire.** À norme 10, la strate à cinq blocs est fermée. Avec le lemme h_c≤2 déjà démontré, restent seulement les supports à six ou sept blocs. À norme 9, la même coupure donne une seconde preuve du plancher six blocs. À norme 8, le résultat antérieur sept blocs reste plus fort.

#### 3. Norme 10 à six blocs : trois profils et une nouvelle interdiction

À six blocs, il y a quatre gros blocs h=2, deux petits h=1 et un bloc inutilisé. Par (2),

    R₀+Π=3.                                             (5)

Les gros blocs ont huit orbites racines extérieures et une somme de poids huit : leur somme de t−1 vaut zéro. Le bloc inutilisé a une somme de poids vingt ; la somme globale vaut quarante. La coupure d'un seul bloc donne donc une somme de poids vingt sur les vingt orbites extérieures internes aux six blocs utilisés. Leur somme de t−1 est aussi zéro.

##### Au moins une orbite racine de poids zéro, et aucun poids ≥4

Si un poids est ≥4, il consomme au moins trois unités de Π. L'égalité (5) force alors R₀=0, un seul poids 4 et tous les autres poids au plus 2. Sans poids zéro, l'égalité t−1=0 aux gros blocs et dans les six blocs utilisés impose que tous leurs poids soient 1. Les poids supérieurs à 1 sont donc limités aux quatre orbites entre le bloc inutilisé et les petits blocs.

Or Σ C(t,2)=11 sur les orbites racines extérieures : après le poids 4, il reste cinq poids 2. Il faudrait six orbites de poids supérieur à 1 dans quatre emplacements. Impossible.

Si R₀=0 sans poids ≥4, (5) donne trois poids 3 ; le même compte ΣC(t,2)=11 impose en plus deux poids 2. Cinq emplacements seraient encore nécessaires, pour quatre disponibles.

Donc R₀≥1 et tous les poids sont dans {0,1,2,3}. Les seuls profils de nombres d'orbites sont :

| R₀ | N₁ | N₂ | N₃ |
|---:|---:|---:|---:|
| 1 | 24 | 5 | 2 |
| 2 | 21 | 8 | 1 |
| 3 | 18 | 11 | 0 |

##### Les deux petits blocs ne portent pas deux orbites sélectionnées

Soit c le nombre d'orbites sélectionnées entre les deux petits blocs. Il existe 6−c orbites extérieures évitant les quatre gros blocs.

La masse positive Σ(t−1)_+ vaut N₂+2N₃=11−N₃. Sur les orbites évitant les gros blocs, elle est au plus 6−c+N₃. Toute autre unité positive touche au moins un gros bloc. Aux gros blocs, elle doit être compensée par une incidence de poids zéro ; ces incidences sont au plus 2R₀. Par conséquent

    11−N₃ ≤ 6−c+N₃+2R₀ = 12−c,

où N₃+R₀=3. Donc **c≤1**. Les deux orbites sœurs entre les petits blocs ne peuvent pas toutes deux appartenir au support.

Si c=1, toutes les bornes sont des égalités : les orbites nulles relient deux gros blocs ; tous les poids 3 évitent les gros blocs ; les cinq orbites extérieures qui évitent les gros blocs ont poids 2 ou 3 ; et aucune orbite de poids supérieur à 1 ne relie deux gros blocs.

Ces conclusions rigidifient la strate à six blocs ; elles ne l'excluent pas.

#### 4. Vérification indépendante et contrôles

Un programme distinct énumère les profils extérieurs de la strate à cinq blocs, retire les deux orbites de la paire inutilisée, puis recherche dix orbites pour la partie opposée de la coupure. Aucun des 32 choix possibles, sur les trois profils, n'égalise les sommes. Cela vérifie le raccord combinatoire sans réutiliser l'inégalité de la preuve.

Les contrôles réels H(2,3) et BvLS passent la formulation compacte bijection/K₂/K₃ avec leurs propres paramètres. Une fonction propre plate impaire de H(2,3) vérifie aussi le double comptage global. Elle est non nulle sur des intérieurs et n'entre donc pas dans l'hypothèse « racines seulement » de notre théorème. Les constantes 4m et sept blocs ne sont pas transférées à ces graphes.

Fichier : [verifier_coupure_norme10.py](#source-14) ; [sorties_normes_et_controles.txt](#source-11). Calculs exécutés à distance sur SageMathCell ; aucun programme lourd n'a tourné sur le PC.

<a id="preuve-a33-fermeture"></a>

## Deuxième campagne — fermeture complète A33

État actuel : exclusion de toute A111111 (3,3), sans supposer P=0.

### Fermeture de l’étoile A111111 (3,3)

26 septembre 2026. **Démontré**, avec deux calculs exacts indépendants du signe et contrôles sur H(2,3) et BvLS.

**Théorème.** Une involution d’un srg(99,14,1,2) ne peut avoir une droite-bloc de type A111111 (3,3). L’hypothèse P=0 n’est pas nécessaire.

Cette preuve ferme la dernière classe laissée ouverte dans ../coupures_et_torsion/PREUVE_A33.md. Elle ne ferme pas toutes les étoiles sans classe fermée et ne prouve pas l’impossibilité générale d’une involution.

#### 1. Le raccord qui manquait

Le calcul précédent avait établi que l’espace V₀ des torsions équilibrées de cette étoile a dimension r₀≤1. La formule de rang de C1 imposait alors g⁻=20 et ρ=0, sans contradiction de rang.

Le nouveau raccord est un **conflit de type de forme quadratique**. Le bloc connu, de rang 14 modulo 7, est non scindé. Il ne peut se compléter en une forme hyperbolique de rang 20 en ajoutant seulement trois plans hyperboliques. Il lui faut un résidu non scindé de dimension au moins deux.

On obtient le renforcement

    g⁻ ≥ 24 − 2r₀,

au lieu du seul minorant 22−2r₀. Avec r₀≤1, cela donne g⁻≥22, contraire à g⁻≤20.

#### 2. Cadre global et signe

Sur les 49 coordonnées impaires, S est entière symétrique et S²+S=12I. Poser H=3I−S modulo 7 et g=g⁻=rang H. La forme

    G = F₇⁴⁹ / ker H,   ⟨[u],[v]⟩ = uᵀHv

est non dégénérée de dimension g. C’est l’opposée de β⁻ du complément au dossier n°6. Multiplier une forme hyperbolique par −1 conserve son caractère hyperbolique.

Les résultats de genre du dossier n°6 donnent g pair, g≤20 et **G hyperbolique**. Voici le raccord de signe, pour préciser ce qui est utilisé.

Avec les représentants canoniques, soit M le nombre d’arêtes négatives dans le bloc racines×racines de S. Alors 1ᵀS1=497−4M. Les sept sommes de lignes des blocs valent 11,9,7,5,3,1,−1 : leurs carrés somment à 7 modulo 8. Les sommes de lignes des 42 racines sont paires et somment à 462−4M ; leurs carrés somment donc à 4 modulo 8. De S²+S=12I, on tire

    3 + (497−4M) ≡ 12·49 ≡ 4 (mod 8),

ce qui impose M pair.

La formule d’oddité déjà certifiée dans le dossier n°6 s’écrit

    22 + 6g + 4δ ≡ 6 + 4M (mod 8).

Elle impose g pair puis δ≡g/2 modulo 2. Par le raccord du réseau propre avec la forme β⁻, le caractère du discriminant de β⁻ est (−1)^(g/2), celui d’une forme hyperbolique en dimension g sur F₇. À g=22, la partie unimodulaire de Λ₋₄⁻ serait vide, et son déterminant 7²² forcerait le signe +1, contrairement à δ≡11. Comme g≤22 par le rang rationnel, g≤20.

Les faits de réseau et l’oddité sont les acquis de C1/structures fournis dans les dossiers ; leur application au bloc dégénéré ci-dessous est le nouveau pas.

#### 3. Le bloc A33 est non scindé

Les douze étiquettes sont 0,…,11. Écrire

    σ(i)=i xor 1,
    τ=(0 5)(1 2)(3 4)(6 11)(7 8)(9 10).

L’appariement interne est μ=σ. Les six paires σ sont les autres blocs, et σ/τ forme deux cycles C₆.

Prendre les sept coordonnées des blocs et les douze orbites contenant le bloc c, représentées par (c,+)(a). Soit C la matrice 7×12 dont la ligne c vaut 1 partout, et les six autres lignes valent +1 puis −1 sur leur paire σ. Alors

    CᵀC = J + I − Pσ,

et le Gram connu H_I, sur 19 coordonnées, est

    H_I = [[4I₇, −C], [−Cᵀ, 3I₁₂−Pσ+Pτ]].

Le complément de Schur sur 4I₇ est, modulo 7,

    Q = I + Pσ + Pτ − 2J.

Sur chaque C₆, I+Pσ+Pτ a un noyau de dimension deux. L’ajout −2J tue la direction constante commune aux deux composantes ; la différence des deux constantes demeure non nulle. Donc rang Q=7, puis rang H_I=14.

Pour J₀={0,1,2,3,6,7,8}, le mineur principal de la matrice entière I+Pσ+Pτ−2J a déterminant **−5**, soit 2 modulo 7. Ainsi

    det_red H_I ≡ 4⁷·2 ≡ 1 (mod 7),

à un carré près. En dimension 14, une forme hyperbolique a discriminant de caractère χ((−1)⁷)=−1. Le discriminant de H_I étant carré, **sa partie non dégénérée est non scindée**.

Contrôle distinct : le mineur principal entier de H_I sur les sept blocs et les étiquettes J₀ vaut 3 508 800, soit 1 modulo 7. Les deux valeurs entières sont différentes parce que le Schur entier n’est pas Q ; leur comparaison n’est faite que modulo 7.

#### 4. Dimension de l’image du bloc

Le noyau local de H_I a dimension cinq. Il est formé du vecteur propre universel z_c, de valeur 3 au bloc c et 1 sur les douze orbites, et des quatre torsions

    φ=(a,b,−a−b,a,b,−a−b ; d,e,−d−e,d,e,−d−e).

Pour une torsion, les coordonnées aux blocs sont 2Cφ modulo 7 et celles de l’étoile sont φ. Le vérificateur reconstruit aussi cinq vecteurs de noyau local, contrôle leur indépendance et vérifie 120 identités de couplage extérieur sur les quatre torsions et les trente orbites. La ligne extérieure d’une orbite z est nulle exactement si

    φ(Φ(z)) − φ(Φ(σz)) + 2[φ(z)−φ(σz)] = 0 (mod 7).

C’est la définition de V₀. Le vecteur universel est dans le noyau global indépendamment de Φ. Par conséquent, l’intersection du noyau global avec les vecteurs portés par I a dimension exactement 1+r₀.

L’image U des 19 coordonnées dans G a donc

    dim U = 18−r₀,
    rang de la forme sur U = 14,
    dim rad U = 4−r₀.

Cela donne le raccord de dimensions directement ; il n’est pas nécessaire de supposer séparément la formule avec ρ.

#### 5. Lemme de Witt pour un bloc dégénéré

**Lemme.** Soit G une forme hyperbolique non dégénérée sur un corps fini de caractéristique impaire. Soit U⊆G, avec radical de dimension h, dont la partie non dégénérée a dimension paire r et est non scindée. Alors

    dim G ≥ r + 2h + 2.

**Preuve.** Poser R=rad U. R est totalement isotrope et U⊆R^⊥. Le quotient R^⊥/R est hyperbolique de dimension dim G−2h. U/R y est non dégénéré et non scindé. Son complément orthogonal doit lui aussi être non scindé, puisque leur somme est hyperbolique. Un complément non scindé de dimension paire ne peut avoir dimension zéro ; sa dimension est au moins deux. D’où la borne. ∎

C’est une application du découpage de Witt classique, et non un nouveau théorème général de classification des réseaux. L’avancement est le calcul du défaut de Witt du bloc A33 et son couplage avec la torsion équilibrée.

Appliquer le lemme avec r=14 et h=4−r₀ donne

    g ≥ 14 + 2(4−r₀) + 2 = 24−2r₀.

#### 6. Les certificats antérieurs donnent r₀≤1

La couverture des 400 directions de P³(F₇), par le groupe de taille 72, a été vérifiée indépendamment dans ../coupures_et_torsion/verifier_A33_independant.py. Quinze certificats entiers et un domaine impossible excluent seize des dix-sept classes. Les douze directions de la dernière classe sont représentées par

    (1,2,4,1,2,4 ; 3,5,6,3,5,6).

Elles n’ont aucune coordonnée nulle. Ainsi tout φ∈V₀ non nul a φ(0)≠0. L’évaluation φ↦φ(0) est une application linéaire injective V₀→F₇. Donc r₀≤1.

Les coefficients complets, les inégalités vérifiées pour chaque choix d’ombres et les sorties sont conservés dans ../coupures_et_torsion/. Leur statut n’est pas changé par cette preuve.

Le nouveau lemme donne alors g≥22, alors que le genre impose g≤20. **Contradiction. Toute la strate A33 est fermée.**

Dans la formulation précédente g=22−2r₀+ρ, le même pas exige ρ≥2 : le cas r₀=1,ρ=0,g=20 est précisément celui qui manquait.

#### 7. Vérifications, portée et limites

Deux implémentations du signe ont été exécutées à distance :

- Sage : rang et choix d’un mineur principal de rang maximal ; rang 14, déterminant 1 modulo 7.
- Python standard écrit séparément : élimination symétrique par congruence, pivots de taille un ou deux, et Bareiss entier. Rang 14, discriminant 1 ; mineurs −5 et 3 508 800.

Le second programme vérifie aussi, sur les vrais graphes H(2,3) et BvLS, la décomposition relative de Witt, ses rangs et ses discriminants :

| Contrôle | Premier | Rang du bloc | Rang total | Rang de couplage du radical | Rang du résidu |
|---|---:|---:|---:|---:|---:|
| H(2,3), 9 sommets | 3 | 2 | 2 | 0 | 0 |
| BvLS, 243 sommets | 3 | 20 | 35 | 4 | 7 |

Dans les deux cas, la relation χ(disc total)=χ(disc bloc)·χ(−1)^h·χ(disc résidu) est contrôlée directement. Les contraintes de genre propres à 99/modulo 7 ne sont pas transplantées à ces autres paramètres. Ces contrôles testent le raccord algébrique, pas un témoin A33.

Les explorations préliminaires des congruences seules et des ombres filtrées λ/μ+Schur n’ont pas donné de contradiction ; elles ne constituent pas la preuve de fermeture.

**Restent ouverts :** les autres étoiles sans classe fermée, dont les étoiles totalement libres à t=0, les familles avec carrés disjoints, l’involution générale et le cas sans symétrie. Les normes 9 et 10 sur six ou sept blocs ne sont pas fermées par ce théorème. Aucune cible globale de l’automation n’étant résolue, elle reste active.

Programmes : verifier_signe_et_controles.py, verifier_signe_sage.py. Sorties : sorties_independantes.txt, sorties_sage.txt. Aucun solveur externe, aucune exécution Python locale, aucun dépôt distant modifié.

<a id="archive-integrale"></a>

## Archive intégrale — originaux complets

Chaque bloc délimité BEGIN_FILE / END_FILE restitue exactement le contenu du fichier indiqué. Les empreintes sont celles des octets UTF-8 d’origine. Les deux manifestes originaux ont été vérifiés avant assemblage.

| Fichier | Octets | SHA256 |
|---|---:|---|
| [outputs/coupures_et_torsion/ETAT_REPRISE.md](#source-01) | 3398 | face6ab0745c15587bcf9e9a8e1db3a2d66cebc653e2d92fb52aabb4740cc977 |
| [outputs/coupures_et_torsion/PREUVE_A33.md](#source-02) | 10995 | 9e621fe6f601db5bc24cfc52a0e31d88cf252348cacfda3642b574d270d48cbb |
| [outputs/coupures_et_torsion/PREUVE_COUPURE_NORME10.md](#source-03) | 7734 | 2d69e7fbcae837316f9e29475f094e47212c884862cbff17d74ecd7cc7224e85 |
| [outputs/coupures_et_torsion/RAPPORT.md](#source-04) | 6464 | 2fb17552b1fe6dcf82f4188bac4007757c734a60161a9cf9120bb6900e017f4a |
| [outputs/coupures_et_torsion/SHA256SUMS.txt](#source-05) | 1175 | 1c1ebc166646043148aff919802e42ec62b5bb89826107f0c11e81824cabf63f |
| [outputs/coupures_et_torsion/certificats_A33.json](#source-06) | 96486 | cebf1108de5dd4b9cbb3d8a016a8ff80c1bc41d2db1981a74b5e5a78167b430f |
| [outputs/coupures_et_torsion/chercher_certificat_A33.py](#source-07) | 5897 | 1d41aebd49621a917fdb4e1b4ae9b9348c92f71a9800eedf6f6bdc36b49d2bbb |
| [outputs/coupures_et_torsion/exploration_F7_equivariante.py](#source-08) | 3324 | 9220bf2581ef3bbeaba761727fa418adbe2019bd43b23ee143dd20c5218955ea |
| [outputs/coupures_et_torsion/sorties_A33_independantes.txt](#source-09) | 2272 | 97b3052a58c8bad9ec7157cb69c884593e00d3a06197d26e3fb2940d2e364ae3 |
| [outputs/coupures_et_torsion/sorties_F7_equivariantes.txt](#source-10) | 247 | 88f8c72d4ffb5d0b3bc9def8e692ec54db6ad32547d9aae5dd7e124263c122f9 |
| [outputs/coupures_et_torsion/sorties_normes_et_controles.txt](#source-11) | 740 | 8b29414396899c7dbfc53c879d08d15f1407a3d4b12e500e837ffe69486618f6 |
| [outputs/coupures_et_torsion/tentative_classe16.json](#source-12) | 99 | 0d7bf08f1b0fc26f1d543bb40d120899d22e2a84c2a2b774dbe5524089ee2ac6 |
| [outputs/coupures_et_torsion/verifier_A33_independant.py](#source-13) | 4503 | e157c07e410e4fa90902f269ed8985d9f7993fd3436fbc9fa10c9ed73bc044db |
| [outputs/coupures_et_torsion/verifier_coupure_norme10.py](#source-14) | 4082 | 4dcd2b59b5f4639ab50d476df8655cd972de040eb9b1c89abec866e64c768900 |
| [outputs/fermeture_A33/ETAT_REPRISE.md](#source-15) | 1942 | 6b3a00d4ef9f00c718b766ef87fcb92eb6c93c6b6afe38b41ae5ed28c19151ca |
| [outputs/fermeture_A33/PREUVE.md](#source-16) | 9474 | 0fb7e92932462c59e7d9397464c0e6921c39aab935b258499f93ae72c2b157fe |
| [outputs/fermeture_A33/RAPPORT.md](#source-17) | 1208 | 7647997418da354ff2ad19f797f98800bf218dbf9902358b9595e5bc7fb38593 |
| [outputs/fermeture_A33/SHA256SUMS.txt](#source-18) | 693 | 1036e4c12325fbe7da5e3af785f823b06c53a11f4bfa05f76637e8bc71ae9db8 |
| [outputs/fermeture_A33/explorations_preliminaires.txt](#source-19) | 443 | d862ae8303009c46198696353489fbfb3fa0d6103aa9792ad2409f81a4b76791 |
| [outputs/fermeture_A33/sorties_independantes.txt](#source-20) | 1177 | 5e9f389f63cc8d32735ce7699c1ec193069406121bc10bd2e1489984040e0994 |
| [outputs/fermeture_A33/sorties_sage.txt](#source-21) | 153 | 7e22cab521559a8df8da7e0bcad58572af5f462e2a3cef4a0020cd2654614854 |
| [outputs/fermeture_A33/verifier_signe_et_controles.py](#source-22) | 7091 | ace66dcf030e93953f2cdc439f0554dcab8f6ba30f8cb4effb98c725fe9a99c0 |
| [outputs/fermeture_A33/verifier_signe_sage.py](#source-23) | 644 | 5e91098ee780ecd0a3fcd93df5dd064144518971025f9cee8264d0f14afa59bb |

<a id="source-01"></a>

### outputs/coupures_et_torsion/ETAT_REPRISE.md

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/ETAT_REPRISE.md" bytes="3398" sha256="face6ab0745c15587bcf9e9a8e1db3a2d66cebc653e2d92fb52aabb4740cc977" -->
```markdown
# Mise à jour prioritaire — A33 entièrement fermée

Lire ../fermeture_A33/PREUVE.md et ETAT_REPRISE.md. Le bloc impair A33 a rang14 et discriminant carré, donc est non scindé. Le lemme de Witt donne g⁻≥24−2r₀ ; les certificats précédents donnent r₀≤1, d’où g⁻≥22 contre g⁻≤20. Toute A111111 (3,3) est exclue, y compris la dernière classe à g⁻20. Deux implémentations du signe et contrôles H(2,3)/BvLS passent. La mention historique « A33 g⁻20 ouverte » ci-dessous est dépassée. Les autres étoiles, l’involution générale et les normes9/10 six/sept blocs restent ouvertes ; automation active.

# État de reprise — coupures et torsion A33

26 septembre 2026. Lire RAPPORT.md, PREUVE_A33.md et PREUVE_COUPURE_NORME10.md. Cette entrée actualise les rapports précédents sur la torsion A33.

## Acquis nouveaux

1. Sous la réduction plate stable des vecteurs de L_T portés par les racines, m=6,…,11 exige au moins six blocs, sans P=0. Preuve humaine par une coupure de deux blocs inutilisés. Toute la norme10 à cinq blocs est fermée. À six blocs : profils (1,24,5,2), (2,21,8,1), (3,18,11,0), aucun t≥4, au plus une orbite sélectionnée entre les petits blocs ; égalités structurelles si une. Strates six/sept ouvertes.
2. A33 : quinze certificats entiers indépendamment revérifiés et une exclusion humaine de C1 couvrent 388/400 directions projectives. Treize classes mixtes de C1 : douze exclues, la dernière de taille12 indécise (363/375 directions éliminées).
3. Les douze directions restantes n’ont aucune coordonnée nulle. Évaluation injective ⇒r₀≤1. Avec g⁻=22−2r₀+ρ et g⁻≤20 : r₀=1,ρ=0,g⁻=20. A33 à g⁻16/18 exclu uniformément, pas A33 à g⁻20.
4. Tous les coefficients sont dans certificats_A33.json ; second programme verifier_A33_independant.py ; sorties exactes sauvegardées. Coverage400/17/72 vérifiée. Énergie vérifiée séparément ; transposition K₂ initialement erronée dans le premier brouillon du vérificateur, corrigée avant les sorties finales.
5. Contrôles H(2,3) et BvLS passent bijection/K₂/K₃ avec leurs paramètres. Contrôle H(2,3) du compte global, hors hypothèse racines seules. Pas de SAT/CP/PLNE ni solveur externe ; calculs distants SageMathCell seulement. Dépôts GitHub strictly read-only, recherche seul.

## Cible résiduelle précise

La classe16 est (1,2,4,1,2,4;3,5,6,3,5,6) mod7. Toute réalisation A33 doit équilibrer cette direction et avoirρ=0. La borne obtenue83,9623<84 n’exclut rien. Exploration F₇× équivariante : aucun témoin après1163nœuds (une seule implémentation, restriction non justifiée pour le cas général). Ne pas la transformer en fermeture.

Attaquer la bijection Φ et les matrices K₂/K₃ avec cette unique direction ; chercher une obstruction couplantρ=0 aux charges ou aux autres blocs. Préserver les coupures de Schur conjointes et le relèvement modulo4 déjà certifiés. Ne pas refaire les exclusions des seize autres classes ni un balayage d’énergies seul.

Norme9/six blocs : classification antérieure indépendante1406noyaux, pas de fermeture globale. Norme10/six : utiliser les trois profils et la condition petits–petits≤1 ; sept blocs ouvert. Ni involution⇒prisme ni exclusion générale ni cas asymétrique résolu. Automatisation recherche-conway-automorphismes demeure ACTIVE.

```
<!-- END_FILE -->

<a id="source-02"></a>

### outputs/coupures_et_torsion/PREUVE_A33.md

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/PREUVE_A33.md" bytes="10995" sha256="9e621fe6f601db5bc24cfc52a0e31d88cf252348cacfda3642b574d270d48cbb" -->
```markdown
# A111111 (3,3) : torsion équilibrée de dimension au plus un et g⁻=20 forcé

26 septembre 2026. **Démontré par certificats entiers, vérifiés par un second programme indépendant**, puis conséquence humaine sur la dimension. Le cas A33 à g⁻=20 reste ouvert.

## Résultat concret

Pour l'étoile A111111 (3,3), les 400 directions projectives de torsion se répartissent en 17 classes. Quinze classes sont exclues par nos nouveaux certificats ; une se ferme par une obstruction élémentaire déjà connue. Il reste **une classe de douze directions**.

Toutes ces directions sont non nulles en chacune des douze coordonnées. Cela donne immédiatement **r₀≤1**, où r₀ est la dimension de la torsion équilibrée. Avec la formule de C1 et son plafond g⁻≤20, on obtient

    r₀=1, ρ=0, g⁻=20.

Ainsi **A111111 (3,3) est impossible à g⁻=16 et à g⁻=18**. Son existence à g⁻=20 n'est pas tranchée. Ni l'involution générale ni l'étoile totalement libre générale ne sont exclues.

L'état précédent de C1 laissait 375 directions mixtes dans treize classes : nos certificats en éliminent **363**, et douze demeurent indécises. Il s'agit d'une exclusion sur toutes les données de cette strate, sans tirage aléatoire de boules.

## 1. Cadre exact

Les douze étiquettes sont 0,…,11 ; σ(i)=i xor 1. Ici μ=σ et

    τ=(0 5)(1 2)(3 4)(6 11)(7 8)(9 10).

Les deux composantes du graphe alterné σ/τ sont C₆ et C₆. Les racines lointaines z sont les soixante paires d'étiquettes de blocs différents, groupées en trente paires z/σz. Les ombres e=Φ(z) parcourent exactement une fois les soixante arêtes de K₁₂−μ.

Les contraintes compactes de structures sont :

    #{z : a∈z, b∈Φ(z)} = K₂[a,b],
    #{z : b∈Φ(z), d∈Φ(σz)} = K₃[b,d],

avec

    K₂[a,b]=2−[a=b]−2[b=σa]−[b=τσa],
    K₃[b,d]=2−[d=σb]−[d=τb]−[d=τσb]−[d=στb].

La bijection et ces deux matrices sont nécessaires dans une vraie SRG avec involution. Le problème traité n'impose aucune absence de prismes.

La torsion est ker₇(I+P_σ+P_τ), de dimension quatre. Sur chaque composante, elle s'écrit

    (a,b,−a−b,a,b,−a−b) mod 7.

Une torsion φ est équilibrée si, pour chaque paire z/σz,

    φ(Φ(z))−φ(Φ(σz))+2[φ(z)−φ(σz)] ≡ 0 mod 7.       (1)

φ(e) désigne la somme des deux valeurs de φ sur une paire e.

Sources des réductions : [C1, note 129](https://github.com/amazing-source/conway99-c1/blob/c4b22393b28cd1f400ab291d3152a3be8d85bf3a/notes/129_Q7_SECTEUR_IMPAIR_INVOLUTION.md) et [structures, formulation compacte](https://github.com/amazing-source/conway99-structures-lab/blob/2e13d68e155d9de862e8d7c8fe14441d11a70184/astra/PROBLEMES_OUVERTS_INVOLUTION.md). Dépôts consultés exclusivement en lecture seule.

## 2. Objet utilisé : les ombres appariées et leur centre

La bijection transporte l'involution sur les soixante arêtes. Une paire e/f est soit sécante, avec un centre b=e∩f, soit disjointe.

K₃[b,b]=2 pour chaque b ; une paire sécante contribue deux à cette entrée. Donc les trente paires d'ombres contiennent exactement **douze paires sécantes, une de chaque centre**, et dix-huit paires disjointes. Ce fait était déjà connu ; l'avancement est de le coupler simultanément à l'usage unique de chaque ombre, aux deux matrices de comptes et au relèvement entier de (1).

Pour une direction projective, choisir un représentant entier

    ψ=(a,b,−a−b,a,b,−a−b ; c,d,−c−d,c,d,−c−d).

Alors les trente charges

    q_z=[ψ(e)−ψ(f)+2(ψ(z)−ψ(σz))]/7

sont entières sous (1). L'énergie exacte, déjà obtenue par C1, est

    Σ q_z² = E(ψ) = 3‖ψ‖²/2.                          (2)

Le nouveau test contraint ces charges et leurs centres **avec toutes les ombres et tous les comptes**, et non par leurs seules sommes séparées.

### Vérification indépendante de l'énergie

Soient Y et W les matrices d'incidence des ombres et des racines, et R la permutation z↔σz. On a

    YYᵀ=9I+J−P_σ,    YRYᵀ=K₃,
    WWᵀ=9I+J−P_σ,    WRWᵀ=J−I+9P_σ,
    WYᵀ=K₂.

Le carré total des charges avant division par 49 est donc

    ψᵀ(YYᵀ−K₃)ψ
      +4ψᵀ(WWᵀ−WRWᵀ)ψ
      +4ψᵀK₂ᵀ(I−P_σ)ψ.

Sur le sous-espace périodique indiqué, ψᵀP_σψ=−‖ψ‖²/2 et (I+P_σ+P_τ)ψ=0. La formule se réduit à 49·3‖ψ‖²/2. Le second programme vérifie aussi cette réduction par arithmétique entière, séparément de la génération des certificats. K₂ n'étant pas symétrique, le produit croisé doit être écrit dans cet ordre ; le vérificateur initial avait une transposition erronée, corrigée avant les sorties finales.

## 3. Forme du certificat : une inégalité par choix d'ombres

Pour chaque paire lointaine Z, on énumère tous les choix ordonnés e/f distincts qui :

- respectent les zéros de K₂ ;
- ne dépassent individuellement aucune capacité de K₃ ;
- vérifient la congruence (1).

Tout choix d'une vraie solution figure dans ce domaine. On ne suppose pas que ces conditions individuelles suffisent à construire une solution.

Un certificat contient des coefficients entiers :

- λ_e pour chacune des soixante ombres ;
- γ_ab et δ_bd pour les deux matrices de comptes ;
- α_b pour les douze centres, α_* pour une paire disjointe ;
- β_Z pour les trente paires lointaines ;
- une échelle entière s, valant 100 ou 1000.

Sur chaque choix admissible, le vérificateur contrôle exactement

    s q_Z² ≥ λ_e+λ_f
              + γ·contribution_K₂(Z,e,f)
              + δ·contribution_K₃(e,f)
              + α_centre + β_Z.                       (3)

En sommant sur une solution, les ombres apparaissent chacune une fois, les centres chacun une fois, les dix-huit paires disjointes chacune avec α_*, et les matrices valent exactement K₂ et K₃. Ainsi

    sE ≥ Σλ + γ·K₂ + δ·K₃ + Σ_b α_b +18α_*+Σ_Z β_Z.

Le membre de droite est le nombre B du certificat. Si B>sE, contradiction. **Aucun arrondi ni calcul flottant n'intervient dans la validité.**

Les coefficients ont été trouvés par une recherche de potentiels entiers et un algorithme d'affectation écrit ici. Leur validité ne dépend ni de la convergence de cette recherche ni de son résultat optimal : le second programme relit chaque colonne et contrôle (3).

## 4. Couverture des directions et sorties exactes

Le groupe qui préserve σ et τ a 72 éléments. Le vérificateur le reconstruit par permutations, puis reconstruit les 400 points de l'espace projectif P³(F₇). Il vérifie que les dix-sept orbites sont disjointes et couvrent tous les points.

| Classe | Taille projective | Multiplicateur du représentant | E | Échelle s | B | Verdict |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 6 | 1 | 6 | 100 | 900 | exclue |
| 1 | 6 | 1 | 18 | 100 | 2000 | exclue |
| 2 | 4 | 1 | 42 | 100 | 4249 | exclue |
| 3 | 18 | 1 | 12 | 100 | 1245 | exclue |
| 4 | 36 | 1 | 30 | 100 | 3021 | exclue |
| 5 | 36 | 1 | 24 | 100 | 2401 | exclue |
| 6 | 72 | 2 | 66 | 1000 | 66014 | exclue |
| 7 | 36 | 1 | 84 | 1000 | 84017 | exclue |
| 8 | 36 | 1 | 78 | 1000 | 78060 | exclue |
| 9 | 9 | 1 | 36 | — | — | domaine impossible, preuve humaine |
| 10 | 36 | 1 | 60 | 100 | 6021 | exclue |
| 11 | 18 | 1 | 96 | 100 | 9659 | exclue |
| 12 | 18 | 1 | 90 | 1000 | 90001 | exclue |
| 13 | 9 | 1 | 36 | 1000 | 36014 | exclue |
| 14 | 36 | 1 | 60 | 1000 | 60019 | exclue |
| 15 | 12 | 1 | 84 | 1000 | 84054 | exclue |
| 16 | 12 | 1 | 84 | 10000 | 839623 | **indécise**, cette borne n'exclut rien |

La classe 6 a été certifiée après multiplication par 2 modulo 7 et choix d'un autre représentant entier périodique. Cela conserve exactement la condition d'équilibre projective. La validité de la nouvelle inégalité et de sa nouvelle énergie est vérifiée séparément.

Pour la classe 9, ψ=(1,1,−2,1,1,−2) sur les deux composantes. Les sommes sur les ombres prennent les résidus {2,3,6}, dont les différences valent {0,1,3,4,6}. Pour z={2,5}, la congruence exige la différence 5, impossible. Cette exclusion reproduit celle de C1 ; elle n'est pas présentée comme nouvelle.

Les quinze certificats ont été vérifiés indépendamment, sur tous les choix admissibles. Les fichiers contiennent les coefficients complets, pas seulement ces nombres.

## 5. Conséquence humaine : la dimension équilibrée s'effondre

La classe restante est représentée par

    φ=(1,2,4,1,2,4 ; 3,5,6,3,5,6) mod 7.

Chaque composante utilise, deux fois chacune, les trois résidus quadratiques non nuls ou leurs opposés. Toutes les douze coordonnées sont non nulles. L'action du groupe et la multiplication scalaire préservent cette propriété.

Soit V₀ l'espace linéaire des torsions équilibrées d'une éventuelle solution. D'après les certificats, tout φ∈V₀ non nul a φ(0)≠0. L'application linéaire

    V₀ → F₇, φ ↦ φ(0)

est donc injective. **dim V₀=r₀≤1.** C'est une preuve humaine, sans classification supplémentaire des plans projectifs.

En contrôle distinct, le programme vérifie que les douze directions restantes ne contiennent aucune des huit directions d'une droite projective entière ; leur intersection avec une telle droite est au plus trois.

Pour A33, t=4. La formule démontrée par C1 donne

    g⁻=18+t−2r₀+ρ =22−2r₀+ρ,   ρ≥0.

Avec g⁻≤20 et r₀≤1, nécessairement

    r₀=1, ρ=0, g⁻=20.

C'est le raccord qui manquait entre l'exclusion finie des directions et un résultat uniforme sur le rang.

## 6. Contrôles, limites et prochaine cible

Les vrais graphes H(2,3) et BvLS passent la bijection et les deux matrices compactes, avec leurs propres paramètres. Ils ne sont pas des étoiles A33 : on ne leur applique pas cette exclusion.

La recherche de la classe 16 n'a produit ni certificat d'impossibilité ni solution intégrale de Φ. Une borne 83,9623 pour une énergie imposée de 84 est **insuffisante**, quelle que soit sa proximité. La restriction multiplicative F₇× est une tentative supplémentaire ; elle n'autorise aucune conclusion générale si elle échoue.

Le verrou s'est réduit à une direction équilibrée unique, de type résidus quadratiques opposés, avec g⁻=20 et ρ=0. La prochaine question porte sur la réalisation de ses soixante ombres, ou sur la compatibilité de ces conditions avec le résidu lointain et les autres blocs. Les étoiles totalement libres à t=0 et les autres types ne sont pas fermés par ce résultat.

Fichiers : [certificats_A33.json](certificats_A33.json) ; [verifier_A33_independant.py](verifier_A33_independant.py) ; [chercher_certificat_A33.py](chercher_certificat_A33.py) ; [sorties_A33_independantes.txt](sorties_A33_independantes.txt). Les programmes ont tourné à distance sur SageMathCell. Aucun SAT, CP, PLNE ou solveur externe n'a été utilisé ; aucun calcul lourd local ni dépôt distant modifié.

```
<!-- END_FILE -->

<a id="source-03"></a>

### outputs/coupures_et_torsion/PREUVE_COUPURE_NORME10.md

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/PREUVE_COUPURE_NORME10.md" bytes="7734" sha256="2d69e7fbcae837316f9e29475f094e47212c884862cbff17d74ecd7cc7224e85" -->
```markdown
# Coupure de deux blocs inutilisés : fermeture de la norme 10 à cinq blocs

26 septembre 2026. **Démontré à la main.** Les vérifications numériques ci-jointes ne remplacent pas la preuve. Aucun solveur ni calcul lourd local.

## Hypothèses et portée

On suppose Γ = srg(99,14,1,2), muni de l'involution fixant x et retournant les sept blocs. On travaille sous la **réduction plate stable** d'un vecteur de L_T : +1 sur P={p_i}, −1 sur Q=σP, zéro ailleurs ; P et Q sont stables, ont chacun m sommets racines, et chaque p_i a quatre voisins dans Q. Sa norme carrée en coordonnées d'orbites vaut m ; le support dans Γ a 2m sommets.

Le résultat ci-dessous n'utilise **pas P=0**. Il ne prouve pas que tous les vecteurs de norme 10 sont impossibles. Il ferme toute leur strate à cinq blocs, sous les hypothèses explicites précédentes.

## 1. Nouvel objet de travail : le multigraphe pondéré des racines extérieures

Pour z hors de P∪Q, l'équation propre donne t_z=|N(z)∩P|=|N(z)∩Q|. L'involution conserve t. Une orbite racine extérieure est représentée par une arête entre ses deux blocs, de poids t. Chaque paire de blocs comporte deux orbites ; celles sélectionnées dans P∪Q sont retirées.

On note h_c le nombre de points de P contenant c_+, égal au nombre contenant c_−. Ainsi Σ h_c=m et le bloc c touche 2h_c orbites sélectionnées.

Les comptes déjà établis donnent, sur les **orbites racines extérieures** :

    Σ t = 4m ;
    Σ_{orbites incidentes à c} t = 2m − 6h_c.             (1)

La première égalité vient du compte global Σ_{sommets extérieurs}t=10m, après retrait des intérieurs : leur contribution est 2Σh_c=2m, puis on divise par deux.

Posons p(0)=0 et p(t)=(t−1)(t−2)/2 pour t≥1. Soient R₀ le nombre d'orbites racines extérieures de poids zéro, et Π=Σ p(t) sur toutes les orbites racines extérieures. Si u blocs sont inutilisés, le compte exact des sommets extérieurs de poids zéro donne

    R₀ + Π + Σ_{c:h_c>0} p(h_c)
        = (m² − 19m + 98)/2 − u.                       (2)

Tout terme du membre de gauche est non négatif.

Ce multigraphe n'est pas un graphe SRG construit. C'est un objet nécessaire dont les degrés pondérés et le coût des défauts sont fixés exactement.

## 2. Théorème de la coupure

**Théorème.** Sous les hypothèses ci-dessus, si 6≤m≤11, le support utilise au moins six blocs.

Supposons deux blocs inutilisés a,b, et prenons I={a,b}. Les orbites extérieures se répartissent en celles internes à I, celles traversant sa coupure, et celles dans les cinq autres blocs.

Notons T_I et T_F les sommes des poids dans les deux parties internes. Par (1), la somme des degrés pondérés en a et b vaut 4m, égale à la somme de tous les poids. Donc

    2T_I + T_coupure = T_I + T_coupure + T_F,
    soit T_I = T_F.                                     (3)

Il y a deux orbites dans I. Dans les cinq autres blocs, il y a 2·C(5,2)−m=20−m orbites extérieures, puisque tout le support y est contenu. Ainsi

    T_F ≥ 20−m−R₀.

Pour tout entier t≥0, t≤2+p(t). Les deux orbites de I vérifient donc

    T_I ≤ 4+Π.

Comme u≥2, (2) impose

    R₀+Π ≤ (m²−19m+94)/2.

En combinant avec (3), on obtient la condition nécessaire

    20−m ≤ 4+(m²−19m+94)/2,
    soit m²−17m+62 ≥ 0.                                 (4)

Mais le polynôme est strictement négatif pour chaque entier m=6,…,11. Contradiction. ∎

**À m=10 :** R₀+Π≤2, T_F≥10−R₀ et T_I≤6−R₀. Les deux sommes censées être égales sont séparées d'au moins quatre unités. C'est une exclusion uniforme, sans choix d'étiquetage.

**Corollaire.** À norme 10, la strate à cinq blocs est fermée. Avec le lemme h_c≤2 déjà démontré, restent seulement les supports à six ou sept blocs. À norme 9, la même coupure donne une seconde preuve du plancher six blocs. À norme 8, le résultat antérieur sept blocs reste plus fort.

## 3. Norme 10 à six blocs : trois profils et une nouvelle interdiction

À six blocs, il y a quatre gros blocs h=2, deux petits h=1 et un bloc inutilisé. Par (2),

    R₀+Π=3.                                             (5)

Les gros blocs ont huit orbites racines extérieures et une somme de poids huit : leur somme de t−1 vaut zéro. Le bloc inutilisé a une somme de poids vingt ; la somme globale vaut quarante. La coupure d'un seul bloc donne donc une somme de poids vingt sur les vingt orbites extérieures internes aux six blocs utilisés. Leur somme de t−1 est aussi zéro.

### Au moins une orbite racine de poids zéro, et aucun poids ≥4

Si un poids est ≥4, il consomme au moins trois unités de Π. L'égalité (5) force alors R₀=0, un seul poids 4 et tous les autres poids au plus 2. Sans poids zéro, l'égalité t−1=0 aux gros blocs et dans les six blocs utilisés impose que tous leurs poids soient 1. Les poids supérieurs à 1 sont donc limités aux quatre orbites entre le bloc inutilisé et les petits blocs.

Or Σ C(t,2)=11 sur les orbites racines extérieures : après le poids 4, il reste cinq poids 2. Il faudrait six orbites de poids supérieur à 1 dans quatre emplacements. Impossible.

Si R₀=0 sans poids ≥4, (5) donne trois poids 3 ; le même compte ΣC(t,2)=11 impose en plus deux poids 2. Cinq emplacements seraient encore nécessaires, pour quatre disponibles.

Donc R₀≥1 et tous les poids sont dans {0,1,2,3}. Les seuls profils de nombres d'orbites sont :

| R₀ | N₁ | N₂ | N₃ |
|---:|---:|---:|---:|
| 1 | 24 | 5 | 2 |
| 2 | 21 | 8 | 1 |
| 3 | 18 | 11 | 0 |

### Les deux petits blocs ne portent pas deux orbites sélectionnées

Soit c le nombre d'orbites sélectionnées entre les deux petits blocs. Il existe 6−c orbites extérieures évitant les quatre gros blocs.

La masse positive Σ(t−1)_+ vaut N₂+2N₃=11−N₃. Sur les orbites évitant les gros blocs, elle est au plus 6−c+N₃. Toute autre unité positive touche au moins un gros bloc. Aux gros blocs, elle doit être compensée par une incidence de poids zéro ; ces incidences sont au plus 2R₀. Par conséquent

    11−N₃ ≤ 6−c+N₃+2R₀ = 12−c,

où N₃+R₀=3. Donc **c≤1**. Les deux orbites sœurs entre les petits blocs ne peuvent pas toutes deux appartenir au support.

Si c=1, toutes les bornes sont des égalités : les orbites nulles relient deux gros blocs ; tous les poids 3 évitent les gros blocs ; les cinq orbites extérieures qui évitent les gros blocs ont poids 2 ou 3 ; et aucune orbite de poids supérieur à 1 ne relie deux gros blocs.

Ces conclusions rigidifient la strate à six blocs ; elles ne l'excluent pas.

## 4. Vérification indépendante et contrôles

Un programme distinct énumère les profils extérieurs de la strate à cinq blocs, retire les deux orbites de la paire inutilisée, puis recherche dix orbites pour la partie opposée de la coupure. Aucun des 32 choix possibles, sur les trois profils, n'égalise les sommes. Cela vérifie le raccord combinatoire sans réutiliser l'inégalité de la preuve.

Les contrôles réels H(2,3) et BvLS passent la formulation compacte bijection/K₂/K₃ avec leurs propres paramètres. Une fonction propre plate impaire de H(2,3) vérifie aussi le double comptage global. Elle est non nulle sur des intérieurs et n'entre donc pas dans l'hypothèse « racines seulement » de notre théorème. Les constantes 4m et sept blocs ne sont pas transférées à ces graphes.

Fichier : [verifier_coupure_norme10.py](verifier_coupure_norme10.py) ; [sorties_normes_et_controles.txt](sorties_normes_et_controles.txt). Calculs exécutés à distance sur SageMathCell ; aucun programme lourd n'a tourné sur le PC.

```
<!-- END_FILE -->

<a id="source-04"></a>

### outputs/coupures_et_torsion/RAPPORT.md

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/RAPPORT.md" bytes="6464" sha256="2fb17552b1fe6dcf82f4188bac4007757c734a60161a9cf9120bb6900e017f4a" -->
```markdown
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

```
<!-- END_FILE -->

<a id="source-05"></a>

### outputs/coupures_et_torsion/SHA256SUMS.txt

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/SHA256SUMS.txt" bytes="1175" sha256="1c1ebc166646043148aff919802e42ec62b5bb89826107f0c11e81824cabf63f" -->
```text
face6ab0745c15587bcf9e9a8e1db3a2d66cebc653e2d92fb52aabb4740cc977  ETAT_REPRISE.md
9e621fe6f601db5bc24cfc52a0e31d88cf252348cacfda3642b574d270d48cbb  PREUVE_A33.md
2d69e7fbcae837316f9e29475f094e47212c884862cbff17d74ecd7cc7224e85  PREUVE_COUPURE_NORME10.md
2fb17552b1fe6dcf82f4188bac4007757c734a60161a9cf9120bb6900e017f4a  RAPPORT.md
cebf1108de5dd4b9cbb3d8a016a8ff80c1bc41d2db1981a74b5e5a78167b430f  certificats_A33.json
1d41aebd49621a917fdb4e1b4ae9b9348c92f71a9800eedf6f6bdc36b49d2bbb  chercher_certificat_A33.py
9220bf2581ef3bbeaba761727fa418adbe2019bd43b23ee143dd20c5218955ea  exploration_F7_equivariante.py
97b3052a58c8bad9ec7157cb69c884593e00d3a06197d26e3fb2940d2e364ae3  sorties_A33_independantes.txt
88f8c72d4ffb5d0b3bc9def8e692ec54db6ad32547d9aae5dd7e124263c122f9  sorties_F7_equivariantes.txt
8b29414396899c7dbfc53c879d08d15f1407a3d4b12e500e837ffe69486618f6  sorties_normes_et_controles.txt
0d7bf08f1b0fc26f1d543bb40d120899d22e2a84c2a2b774dbe5524089ee2ac6  tentative_classe16.json
e157c07e410e4fa90902f269ed8985d9f7993fd3436fbc9fa10c9ed73bc044db  verifier_A33_independant.py
4dcd2b59b5f4639ab50d476df8655cd972de040eb9b1c89abec866e64c768900  verifier_coupure_norme10.py

```
<!-- END_FILE -->

<a id="source-06"></a>

### outputs/coupures_et_torsion/certificats_A33.json

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/certificats_A33.json" bytes="96486" sha256="cebf1108de5dd4b9cbb3d8a016a8ff80c1bc41d2db1981a74b5e5a78167b430f" -->
```json
{
  "date": "2026-09-26",
  "claim": "A33: balanced torsion dimension at most 1; g_minus=20 forced using C1 rank formula and ceiling",
  "phi_reps": [
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      6,
      0,
      1,
      6
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1,
      5,
      1,
      1,
      5
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      2,
      4,
      1,
      2,
      4
    ],
    [
      0,
      1,
      6,
      0,
      1,
      6,
      0,
      1,
      6,
      0,
      1,
      6
    ],
    [
      0,
      1,
      6,
      0,
      1,
      6,
      0,
      2,
      5,
      0,
      2,
      5
    ],
    [
      0,
      1,
      6,
      0,
      1,
      6,
      1,
      1,
      5,
      1,
      1,
      5
    ],
    [
      0,
      1,
      6,
      0,
      1,
      6,
      1,
      2,
      4,
      1,
      2,
      4
    ],
    [
      0,
      1,
      6,
      0,
      1,
      6,
      1,
      3,
      3,
      1,
      3,
      3
    ],
    [
      0,
      1,
      6,
      0,
      1,
      6,
      2,
      2,
      3,
      2,
      2,
      3
    ],
    [
      1,
      1,
      5,
      1,
      1,
      5,
      1,
      1,
      5,
      1,
      1,
      5
    ],
    [
      1,
      1,
      5,
      1,
      1,
      5,
      1,
      2,
      4,
      1,
      2,
      4
    ],
    [
      1,
      1,
      5,
      1,
      1,
      5,
      1,
      3,
      3,
      1,
      3,
      3
    ],
    [
      1,
      1,
      5,
      1,
      1,
      5,
      2,
      2,
      3,
      2,
      2,
      3
    ],
    [
      1,
      1,
      5,
      1,
      1,
      5,
      2,
      6,
      6,
      2,
      6,
      6
    ],
    [
      1,
      1,
      5,
      1,
      1,
      5,
      3,
      5,
      6,
      3,
      5,
      6
    ],
    [
      1,
      2,
      4,
      1,
      2,
      4,
      1,
      2,
      4,
      1,
      2,
      4
    ],
    [
      1,
      2,
      4,
      1,
      2,
      4,
      3,
      5,
      6,
      3,
      5,
      6
    ]
  ],
  "orbit_sizes": [
    6,
    6,
    4,
    18,
    36,
    36,
    72,
    36,
    36,
    9,
    36,
    18,
    18,
    9,
    36,
    12,
    12
  ],
  "cases": [
    {
      "index": 0,
      "energy": 6,
      "bound_scaled": 900,
      "scale": 100,
      "excluded": true,
      "iterations": 1,
      "seconds": 0.08246707916259766,
      "certificate": {
        "bound": 900,
        "price": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "dual_left": [
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100,
          100
        ],
        "dual_right": [
          -100,
          -100,
          -100,
          -100,
          -100,
          -100,
          -100,
          -100,
          0,
          0,
          -100,
          -100,
          -100,
          -100,
          -100,
          -100,
          0,
          0,
          -100,
          -100,
          -100,
          -100,
          0,
          0,
          0,
          -100,
          -100,
          0,
          -100,
          0
        ]
      }
    },
    {
      "index": 1,
      "energy": 18,
      "bound_scaled": 2000,
      "scale": 100,
      "excluded": true,
      "iterations": 1,
      "seconds": 0.11885356903076172,
      "certificate": {
        "bound": 2000,
        "price": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "dual_left": [
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400,
          400
        ],
        "dual_right": [
          -400,
          -400,
          -400,
          -400,
          -400,
          -400,
          -300,
          -300,
          -300,
          -300,
          -400,
          -400,
          -400,
          -400,
          -300,
          -300,
          -300,
          -300,
          -400,
          -400,
          -300,
          -300,
          -300,
          -300,
          -300,
          -300,
          -300,
          -300,
          -400,
          0
        ]
      }
    },
    {
      "index": 2,
      "energy": 42,
      "bound_scaled": 4249,
      "scale": 100,
      "excluded": true,
      "iterations": 60,
      "seconds": 0.8579058647155762,
      "certificate": {
        "bound": 4249,
        "price": [
          -10,
          -9,
          -8,
          -14,
          6,
          8,
          3,
          12,
          5,
          10,
          -10,
          -7,
          -13,
          -10,
          7,
          4,
          6,
          10,
          4,
          10,
          -10,
          -10,
          7,
          5,
          7,
          11,
          4,
          10,
          -17,
          -6,
          5,
          6,
          5,
          9,
          6,
          6,
          9,
          0,
          9,
          11,
          5,
          7,
          7,
          5,
          4,
          12,
          3,
          12,
          -31,
          -10,
          0,
          -15,
          -13,
          -32,
          30,
          -28,
          -40,
          49,
          -6,
          -30,
          -18,
          0,
          -14,
          -16,
          -15,
          -10,
          14,
          12,
          8,
          13,
          12,
          14,
          0,
          -16,
          -13,
          -12,
          -15,
          -17,
          15,
          10,
          10,
          11,
          12,
          15,
          -13,
          -15,
          -18,
          0,
          -15,
          -13,
          12,
          13,
          10,
          10,
          13,
          16,
          -13,
          -15,
          0,
          -18,
          -17,
          -15,
          14,
          11,
          10,
          11,
          15,
          17,
          -14,
          -15,
          -13,
          -15,
          -18,
          0,
          12,
          12,
          10,
          9,
          14,
          18,
          -12,
          -15,
          -15,
          -17,
          0,
          -16,
          13,
          13,
          10,
          9,
          15,
          15,
          17,
          19,
          17,
          19,
          16,
          19,
          -50,
          0,
          -7,
          -24,
          -54,
          28,
          13,
          12,
          14,
          14,
          12,
          13,
          0,
          -16,
          3,
          -2,
          3,
          -66,
          12,
          13,
          14,
          9,
          9,
          13,
          -56,
          -33,
          12,
          0,
          -52,
          59,
          14,
          15,
          15,
          15,
          11,
          12,
          -9,
          -31,
          0,
          -22,
          42,
          -62,
          8,
          9,
          12,
          7,
          8,
          8,
          -1,
          49,
          -150,
          48,
          2,
          0,
          12,
          10,
          9,
          10,
          10,
          12,
          6,
          -70,
          82,
          -89,
          0,
          8,
          0,
          -6,
          -7,
          -10,
          -6,
          -6,
          7,
          4,
          6,
          0,
          11,
          13,
          -6,
          0,
          -8,
          -7,
          -6,
          -6,
          3,
          2,
          8,
          -1,
          10,
          13,
          -7,
          -8,
          0,
          -5,
          -9,
          -6,
          7,
          2,
          7,
          1,
          11,
          15,
          -10,
          -7,
          -5,
          0,
          -10,
          -7,
          9,
          1,
          2,
          -1,
          12,
          12,
          -6,
          -6,
          -9,
          -10,
          0,
          -8,
          2,
          -1,
          5,
          -2,
          10,
          11,
          -6,
          -6,
          -6,
          -7,
          -8,
          0,
          6,
          3,
          8,
          1,
          10,
          11,
          7,
          3,
          7,
          9,
          2,
          6,
          0,
          -23,
          -18,
          9,
          -21,
          -11,
          4,
          2,
          2,
          1,
          -1,
          3,
          -23,
          0,
          -12,
          -16,
          8,
          2,
          6,
          8,
          7,
          2,
          5,
          8,
          -18,
          -12,
          0,
          -11,
          2,
          1,
          0,
          -1,
          1,
          -1,
          -2,
          1,
          9,
          -16,
          -11,
          0,
          -16,
          10,
          11,
          10,
          11,
          12,
          10,
          10,
          -21,
          8,
          2,
          -16,
          0,
          -15,
          13,
          13,
          15,
          12,
          11,
          11,
          -11,
          2,
          1,
          10,
          -15,
          0
        ],
        "dual_left": [
          707,
          711,
          710,
          715,
          717,
          711,
          717,
          719,
          726,
          757,
          706,
          680,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723,
          723
        ],
        "dual_right": [
          -772,
          -773,
          -770,
          -775,
          -714,
          -712,
          -588,
          -593,
          -473,
          -481,
          -769,
          -769,
          -712,
          -713,
          -583,
          -582,
          -473,
          -475,
          -714,
          -711,
          -587,
          -589,
          -474,
          -472,
          -617,
          -677,
          -595,
          -434,
          -680,
          0
        ]
      }
    },
    {
      "index": 3,
      "energy": 12,
      "bound_scaled": 1245,
      "scale": 100,
      "excluded": true,
      "iterations": 19,
      "seconds": 0.355053186416626,
      "certificate": {
        "bound": 1245,
        "price": [
          -1,
          0,
          0,
          -1,
          4,
          3,
          -3,
          2,
          2,
          3,
          7,
          0,
          -16,
          9,
          1,
          -17,
          9,
          4,
          -12,
          12,
          12,
          -17,
          1,
          11,
          -12,
          -3,
          12,
          -15,
          0,
          -1,
          0,
          0,
          -1,
          3,
          1,
          3,
          4,
          -15,
          11,
          1,
          -15,
          16,
          4,
          13,
          -15,
          3,
          16,
          -16,
          -1,
          1,
          -3,
          1,
          9,
          0,
          -16,
          10,
          12,
          -16,
          -2,
          -2,
          -2,
          0,
          -5,
          2,
          -5,
          0,
          5,
          0,
          1,
          1,
          -1,
          4,
          0,
          -5,
          -6,
          1,
          1,
          -7,
          4,
          2,
          1,
          6,
          4,
          -1,
          2,
          -2,
          -3,
          0,
          -6,
          1,
          3,
          1,
          3,
          4,
          -5,
          2,
          0,
          -5,
          0,
          -1,
          0,
          -6,
          5,
          1,
          0,
          4,
          3,
          -1,
          -3,
          8,
          -12,
          -2,
          4,
          0,
          2,
          11,
          -8,
          3,
          8,
          -11,
          -2,
          -13,
          10,
          -6,
          0,
          3,
          3,
          -9,
          10,
          3,
          -9,
          10,
          2,
          -1,
          0,
          3,
          -4,
          5,
          1,
          0,
          -5,
          2,
          -4,
          1,
          6,
          3,
          1,
          4,
          3,
          -3,
          0,
          -3,
          -4,
          0,
          1,
          -8,
          6,
          2,
          0,
          2,
          -5,
          3,
          4,
          -3,
          -4,
          0,
          -7,
          2,
          4,
          3,
          1,
          4,
          5,
          -4,
          2,
          -3,
          0,
          -2,
          -2,
          -8,
          2,
          12,
          -8,
          2,
          11,
          -10,
          -4,
          11,
          -15,
          -3,
          2,
          0,
          3,
          -8,
          12,
          1,
          -8,
          8,
          -1,
          -12,
          7,
          -4,
          0,
          2,
          0,
          -3,
          -1,
          3,
          1,
          -1,
          5,
          4,
          0,
          5,
          2,
          3,
          -3,
          0,
          -10,
          0,
          8,
          -11,
          4,
          8,
          -8,
          4,
          8,
          -6,
          -1,
          -10,
          0,
          -2,
          -11,
          5,
          3,
          -7,
          6,
          5,
          -7,
          9,
          3,
          0,
          -2,
          0,
          -2,
          0,
          4,
          2,
          3,
          -2,
          3,
          1,
          1,
          8,
          -11,
          -2,
          0,
          -11,
          2,
          9,
          -7,
          4,
          10,
          -7,
          -1,
          -11,
          5,
          0,
          -11,
          0,
          4,
          -6,
          9,
          -1,
          -7,
          9,
          5,
          4,
          3,
          4,
          2,
          4,
          0,
          1,
          0,
          1,
          -1,
          1,
          4,
          8,
          -7,
          2,
          9,
          -6,
          1,
          0,
          -10,
          -1,
          6,
          -10,
          0,
          -8,
          6,
          3,
          -7,
          9,
          0,
          -10,
          0,
          1,
          -13,
          5,
          5,
          4,
          5,
          -2,
          4,
          -1,
          1,
          -1,
          1,
          0,
          0,
          -2,
          2,
          8,
          -7,
          3,
          10,
          -7,
          -1,
          6,
          -13,
          0,
          0,
          -11,
          3,
          -6,
          9,
          1,
          -7,
          9,
          1,
          -10,
          5,
          -2,
          -11,
          0
        ],
        "dual_left": [
          120,
          131,
          139,
          123,
          136,
          140,
          117,
          135,
          144,
          121,
          139,
          137,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116,
          116
        ],
        "dual_right": [
          -6,
          -169,
          -115,
          -68,
          0,
          -166,
          -6,
          -166,
          -108,
          -65,
          -118,
          -73,
          -2,
          -170,
          -1,
          -171,
          -111,
          -68,
          -109,
          -68,
          -109,
          -71,
          -32,
          -158,
          -9,
          -175,
          -115,
          -69,
          -116,
          -74
        ]
      }
    },
    {
      "index": 4,
      "energy": 30,
      "bound_scaled": 3021,
      "scale": 100,
      "excluded": true,
      "iterations": 328,
      "seconds": 4.878125429153442,
      "certificate": {
        "bound": 3021,
        "price": [
          -12,
          -22,
          -17,
          -10,
          12,
          4,
          5,
          13,
          12,
          14,
          1,
          -13,
          -34,
          0,
          14,
          -34,
          35,
          10,
          31,
          -7,
          5,
          -33,
          12,
          37,
          -35,
          12,
          -10,
          32,
          -13,
          -15,
          12,
          2,
          -2,
          12,
          18,
          12,
          10,
          -31,
          37,
          16,
          35,
          -7,
          14,
          36,
          -30,
          12,
          -9,
          31,
          -25,
          -17,
          -12,
          -12,
          28,
          -25,
          22,
          -62,
          -59,
          24,
          -14,
          -10,
          -19,
          0,
          8,
          -23,
          -48,
          10,
          13,
          -54,
          60,
          11,
          46,
          -4,
          0,
          8,
          -43,
          -12,
          13,
          -46,
          11,
          61,
          -53,
          13,
          -4,
          52,
          -13,
          -46,
          8,
          0,
          -47,
          13,
          12,
          -51,
          60,
          16,
          49,
          -1,
          -20,
          8,
          0,
          -22,
          11,
          -46,
          11,
          59,
          -54,
          13,
          -5,
          45,
          -21,
          -8,
          -27,
          -10,
          -9,
          0,
          10,
          25,
          -18,
          10,
          74,
          -26,
          -7,
          -27,
          -6,
          -21,
          0,
          -9,
          12,
          -19,
          25,
          10,
          -27,
          69,
          1,
          -11,
          23,
          14,
          -8,
          23,
          -21,
          0,
          6,
          -16,
          -68,
          57,
          17,
          28,
          -6,
          3,
          28,
          -8,
          0,
          5,
          -54,
          -11,
          61,
          -63,
          7,
          -6,
          30,
          14,
          -6,
          28,
          -12,
          -55,
          5,
          0,
          -64,
          59,
          12,
          23,
          -8,
          0,
          26,
          -10,
          -17,
          3,
          0,
          -23,
          57,
          -63,
          18,
          38,
          1,
          18,
          38,
          3,
          -2,
          26,
          -48,
          -1,
          -91,
          0,
          23,
          -1,
          38,
          21,
          4,
          34,
          -1,
          -46,
          27,
          -4,
          0,
          -95,
          0,
          -9,
          -9,
          -2,
          -10,
          -10,
          2,
          4,
          -2,
          3,
          17,
          14,
          -9,
          0,
          -15,
          -13,
          3,
          -17,
          7,
          19,
          -12,
          7,
          7,
          29,
          -9,
          -15,
          0,
          -9,
          -16,
          3,
          7,
          -12,
          21,
          8,
          30,
          10,
          -2,
          -13,
          -9,
          0,
          -11,
          -13,
          3,
          -2,
          2,
          2,
          11,
          14,
          -10,
          3,
          -16,
          -11,
          0,
          -19,
          5,
          22,
          -15,
          5,
          8,
          30,
          -10,
          -17,
          3,
          -13,
          -19,
          0,
          5,
          -19,
          22,
          5,
          27,
          8,
          2,
          7,
          7,
          3,
          5,
          5,
          0,
          -10,
          -11,
          -6,
          8,
          6,
          4,
          19,
          -12,
          -2,
          22,
          -19,
          -10,
          0,
          -46,
          -10,
          -17,
          25,
          -2,
          -12,
          21,
          2,
          -15,
          22,
          -11,
          -46,
          0,
          -9,
          24,
          -18,
          3,
          7,
          8,
          2,
          5,
          5,
          -6,
          -10,
          -9,
          0,
          7,
          6,
          17,
          7,
          30,
          11,
          8,
          27,
          8,
          -17,
          24,
          7,
          0,
          -94,
          14,
          29,
          10,
          14,
          30,
          8,
          6,
          25,
          -18,
          6,
          -94,
          0
        ],
        "dual_left": [
          309,
          307,
          303,
          319,
          304,
          308,
          290,
          343,
          354,
          283,
          190,
          191,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300,
          300
        ],
        "dual_right": [
          -348,
          -326,
          -333,
          -279,
          -239,
          -320,
          -239,
          -320,
          -231,
          -34,
          -331,
          -277,
          -242,
          -319,
          -242,
          -312,
          -236,
          -30,
          -326,
          -169,
          -324,
          -174,
          0,
          -201,
          -218,
          -337,
          -223,
          -17,
          -232,
          -17
        ]
      }
    },
    {
      "index": 5,
      "energy": 24,
      "bound_scaled": 2401,
      "scale": 100,
      "excluded": true,
      "iterations": 185,
      "seconds": 2.4907467365264893,
      "certificate": {
        "bound": 2401,
        "price": [
          -10,
          -13,
          -14,
          -6,
          8,
          7,
          7,
          11,
          11,
          7,
          6,
          -14,
          -29,
          -3,
          -2,
          0,
          20,
          6,
          3,
          19,
          5,
          -26,
          18,
          19,
          -27,
          22,
          23,
          -27,
          -17,
          -6,
          7,
          7,
          6,
          13,
          15,
          8,
          1,
          0,
          16,
          10,
          9,
          19,
          9,
          9,
          -1,
          15,
          17,
          -3,
          15,
          -34,
          -33,
          16,
          15,
          -38,
          -35,
          15,
          20,
          -86,
          -30,
          20,
          -9,
          0,
          1,
          -8,
          -45,
          29,
          -8,
          -9,
          41,
          -15,
          -16,
          39,
          0,
          19,
          -30,
          -11,
          25,
          -48,
          32,
          31,
          -37,
          28,
          28,
          -37,
          -4,
          -45,
          5,
          0,
          -45,
          33,
          -5,
          -7,
          46,
          -12,
          -11,
          45,
          -16,
          21,
          0,
          -13,
          22,
          -49,
          29,
          29,
          -38,
          25,
          28,
          -38,
          -1,
          -3,
          -40,
          -1,
          -6,
          0,
          25,
          26,
          -24,
          24,
          24,
          -24,
          -20,
          -17,
          15,
          -20,
          0,
          -17,
          1,
          -1,
          31,
          -3,
          -1,
          32,
          14,
          9,
          14,
          15,
          10,
          13,
          -12,
          0,
          -20,
          -12,
          -13,
          -18,
          14,
          9,
          13,
          16,
          9,
          13,
          0,
          -11,
          -21,
          -13,
          -10,
          -19,
          7,
          -33,
          51,
          6,
          -29,
          43,
          -38,
          -43,
          40,
          0,
          -50,
          46,
          13,
          43,
          -37,
          11,
          44,
          -26,
          15,
          11,
          0,
          7,
          12,
          -93,
          13,
          41,
          -37,
          12,
          44,
          -23,
          12,
          14,
          -94,
          9,
          9,
          0,
          5,
          -32,
          51,
          5,
          -29,
          42,
          -41,
          -42,
          46,
          -48,
          0,
          43,
          0,
          -2,
          -5,
          0,
          -1,
          -9,
          7,
          5,
          5,
          4,
          6,
          6,
          -2,
          0,
          -12,
          -1,
          8,
          -7,
          9,
          8,
          -3,
          7,
          8,
          -3,
          -5,
          -12,
          0,
          -9,
          -14,
          4,
          0,
          -2,
          22,
          -1,
          0,
          23,
          0,
          -1,
          -9,
          0,
          -3,
          -9,
          8,
          6,
          2,
          4,
          7,
          7,
          -1,
          8,
          -14,
          -3,
          0,
          -8,
          7,
          5,
          -4,
          5,
          8,
          -3,
          -9,
          -7,
          4,
          -9,
          -8,
          0,
          5,
          4,
          13,
          1,
          2,
          14,
          7,
          9,
          0,
          8,
          7,
          5,
          0,
          9,
          -24,
          4,
          8,
          -23,
          5,
          8,
          -2,
          6,
          5,
          4,
          9,
          0,
          -23,
          6,
          3,
          -23,
          5,
          -3,
          22,
          2,
          -4,
          13,
          -24,
          -23,
          0,
          -23,
          -22,
          27,
          4,
          7,
          -1,
          4,
          5,
          1,
          4,
          6,
          -23,
          0,
          6,
          -23,
          6,
          8,
          0,
          7,
          8,
          2,
          8,
          3,
          -22,
          6,
          0,
          -26,
          6,
          -3,
          23,
          7,
          -3,
          14,
          -23,
          -23,
          27,
          -23,
          -26,
          0
        ],
        "dual_left": [
          262,
          287,
          275,
          264,
          279,
          260,
          281,
          291,
          324,
          297,
          283,
          325,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268,
          268
        ],
        "dual_right": [
          -347,
          -341,
          -324,
          -275,
          -247,
          -249,
          -146,
          -181,
          -177,
          -141,
          -329,
          -276,
          -249,
          -250,
          -148,
          -186,
          -184,
          -142,
          -201,
          -201,
          -240,
          -9,
          0,
          -238,
          -263,
          -260,
          -259,
          -260,
          -314,
          -41
        ]
      }
    },
    {
      "index": 6,
      "multiplier": 2,
      "energy": 66,
      "bound_scaled": 66014,
      "scale": 1000,
      "excluded": true,
      "iterations": 505,
      "seconds": 7.476155519485474,
      "certificate": {
        "bound": 66014,
        "price": [
          -113,
          -161,
          -168,
          -135,
          66,
          100,
          34,
          81,
          119,
          40,
          -242,
          -141,
          -17,
          -272,
          285,
          -99,
          121,
          303,
          -80,
          122,
          -272,
          45,
          -104,
          360,
          11,
          -86,
          380,
          18,
          -165,
          -140,
          73,
          106,
          40,
          91,
          122,
          44,
          288,
          -98,
          118,
          303,
          -77,
          125,
          -105,
          358,
          9,
          -89,
          378,
          12,
          3,
          -14,
          -394,
          -60,
          -177,
          -333,
          272,
          -239,
          -182,
          -128,
          -338,
          2,
          -139,
          0,
          210,
          -139,
          -540,
          178,
          -226,
          548,
          -123,
          -214,
          569,
          -124,
          0,
          273,
          -433,
          -65,
          249,
          -465,
          344,
          -451,
          311,
          360,
          -429,
          306,
          -101,
          -475,
          242,
          0,
          -505,
          214,
          -196,
          580,
          -90,
          -178,
          602,
          -93,
          -93,
          243,
          0,
          -102,
          214,
          -496,
          310,
          -486,
          274,
          328,
          -463,
          271,
          -162,
          470,
          -812,
          -163,
          433,
          0,
          693,
          -961,
          368,
          709,
          -941,
          366,
          -145,
          -808,
          485,
          -151,
          0,
          447,
          -652,
          981,
          -261,
          -637,
          1003,
          -262,
          22,
          864,
          -847,
          17,
          855,
          -854,
          483,
          0,
          261,
          541,
          -1537,
          195,
          24,
          -854,
          869,
          24,
          -860,
          861,
          0,
          1038,
          -594,
          -888,
          1047,
          -667,
          101,
          -57,
          237,
          99,
          -63,
          225,
          -340,
          75,
          -143,
          0,
          68,
          -202,
          105,
          228,
          -50,
          105,
          222,
          -62,
          87,
          -359,
          0,
          136,
          -353,
          -59,
          52,
          -680,
          754,
          50,
          -689,
          745,
          -721,
          836,
          -517,
          -664,
          834,
          0,
          62,
          756,
          -661,
          63,
          758,
          -671,
          294,
          -1301,
          212,
          347,
          0,
          141,
          0,
          -73,
          -84,
          -90,
          -69,
          -78,
          13,
          56,
          -6,
          -16,
          50,
          23,
          -73,
          0,
          13,
          -70,
          -114,
          18,
          -65,
          182,
          -18,
          -101,
          175,
          13,
          -84,
          13,
          0,
          -83,
          17,
          -133,
          136,
          -40,
          36,
          107,
          -48,
          73,
          -90,
          -70,
          -83,
          0,
          -68,
          -79,
          18,
          54,
          -3,
          -16,
          49,
          26,
          -69,
          -114,
          17,
          -68,
          0,
          23,
          -50,
          200,
          -2,
          -83,
          192,
          28,
          -78,
          18,
          -133,
          -79,
          23,
          0,
          153,
          -28,
          61,
          121,
          -28,
          92,
          13,
          -65,
          136,
          18,
          -50,
          153,
          0,
          124,
          -130,
          -95,
          108,
          -136,
          56,
          182,
          -40,
          54,
          200,
          -28,
          124,
          0,
          10,
          112,
          -176,
          6,
          -6,
          -18,
          36,
          -3,
          -2,
          61,
          -130,
          10,
          0,
          -142,
          -8,
          -100,
          -16,
          -101,
          107,
          -16,
          -83,
          121,
          -95,
          112,
          -142,
          0,
          96,
          -143,
          50,
          175,
          -48,
          49,
          192,
          -28,
          108,
          -176,
          -8,
          96,
          0,
          -10,
          23,
          13,
          73,
          26,
          28,
          92,
          -136,
          6,
          -100,
          -143,
          -10,
          0
        ],
        "dual_left": [
          7358,
          7310,
          7259,
          7354,
          7320,
          7277,
          7376,
          7212,
          7331,
          7325,
          7153,
          7336,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537,
          7537
        ],
        "dual_right": [
          -6085,
          -7294,
          -6839,
          -4188,
          -6049,
          -2908,
          -6406,
          -7132,
          -4146,
          -6575,
          -6837,
          -4192,
          -6048,
          -2918,
          -6410,
          -7133,
          -4140,
          -6578,
          0,
          -6572,
          -6222,
          -4945,
          -6819,
          -1530,
          -5827,
          -4094,
          -6735,
          -455,
          -5149,
          -6587
        ]
      }
    },
    {
      "index": 7,
      "energy": 84,
      "bound_scaled": 84017,
      "scale": 1000,
      "excluded": true,
      "iterations": 714,
      "seconds": 13.957514524459839,
      "certificate": {
        "bound": 84017,
        "price": [
          -129,
          -391,
          -160,
          -139,
          99,
          107,
          135,
          110,
          62,
          113,
          -206,
          -162,
          -270,
          -204,
          96,
          210,
          -31,
          109,
          283,
          49,
          -212,
          -393,
          25,
          107,
          404,
          36,
          -58,
          279,
          -172,
          -153,
          105,
          117,
          147,
          124,
          70,
          123,
          90,
          209,
          -33,
          102,
          280,
          47,
          16,
          98,
          392,
          29,
          -67,
          270,
          -253,
          -257,
          56,
          -182,
          -609,
          -81,
          296,
          -509,
          -529,
          664,
          -13,
          -246,
          -149,
          0,
          49,
          -160,
          -309,
          57,
          48,
          -257,
          280,
          41,
          -78,
          478,
          0,
          53,
          -345,
          -109,
          51,
          -348,
          160,
          490,
          -166,
          156,
          322,
          -264,
          -155,
          -305,
          46,
          0,
          -311,
          52,
          76,
          -231,
          303,
          69,
          -50,
          506,
          -130,
          17,
          0,
          -151,
          14,
          -383,
          148,
          481,
          -175,
          144,
          311,
          -276,
          -107,
          -13,
          -354,
          -125,
          -42,
          0,
          286,
          576,
          -619,
          280,
          639,
          -521,
          -187,
          -311,
          3,
          -212,
          0,
          2,
          -56,
          -318,
          754,
          -62,
          -370,
          757,
          13,
          -192,
          212,
          14,
          -184,
          214,
          -201,
          0,
          463,
          -142,
          -663,
          466,
          152,
          349,
          -57,
          160,
          354,
          -51,
          0,
          358,
          -839,
          -106,
          421,
          -741,
          152,
          -227,
          511,
          156,
          -222,
          515,
          -717,
          -1486,
          1319,
          0,
          -1422,
          1421,
          -43,
          326,
          -418,
          -35,
          335,
          -416,
          341,
          926,
          0,
          108,
          874,
          -1998,
          6,
          572,
          -568,
          12,
          582,
          -569,
          296,
          1363,
          -2686,
          216,
          776,
          0,
          62,
          -521,
          627,
          66,
          -506,
          625,
          -791,
          -2012,
          1940,
          -878,
          0,
          1388,
          0,
          -139,
          -171,
          -49,
          -141,
          -171,
          -58,
          -3,
          52,
          -20,
          142,
          172,
          -139,
          0,
          -115,
          -148,
          -71,
          -116,
          -43,
          -35,
          151,
          -1,
          45,
          220,
          -171,
          -115,
          0,
          -176,
          -119,
          -46,
          -1,
          23,
          -57,
          38,
          221,
          109,
          -49,
          -148,
          -176,
          0,
          -148,
          -178,
          -54,
          5,
          56,
          -13,
          146,
          175,
          -141,
          -71,
          -119,
          -148,
          0,
          -118,
          -37,
          -33,
          155,
          2,
          49,
          223,
          -171,
          -116,
          -46,
          -178,
          -118,
          0,
          -1,
          20,
          -60,
          39,
          220,
          109,
          -58,
          -43,
          -1,
          -54,
          -37,
          -1,
          0,
          -173,
          17,
          -50,
          -92,
          82,
          -3,
          -35,
          23,
          5,
          -33,
          20,
          -173,
          0,
          272,
          -171,
          -237,
          222,
          52,
          151,
          -57,
          56,
          155,
          -60,
          17,
          272,
          0,
          15,
          256,
          -283,
          -20,
          -1,
          38,
          -13,
          2,
          39,
          -50,
          -171,
          15,
          0,
          -95,
          82,
          142,
          45,
          221,
          146,
          49,
          220,
          -92,
          -237,
          256,
          -95,
          0,
          105,
          172,
          220,
          109,
          175,
          223,
          109,
          82,
          222,
          -283,
          82,
          105,
          0
        ],
        "dual_left": [
          12704,
          12671,
          12697,
          12697,
          12644,
          12709,
          12678,
          12569,
          12510,
          12683,
          12087,
          11922,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796,
          12796
        ],
        "dual_right": [
          -12600,
          -12712,
          -12726,
          -11814,
          -11803,
          -12484,
          -9262,
          -10865,
          -8774,
          -6492,
          -12755,
          -11817,
          -11777,
          -12458,
          -9236,
          -10840,
          -8737,
          -6457,
          -12591,
          -11100,
          -11312,
          -8223,
          -4926,
          -9497,
          -8224,
          -11832,
          -9954,
          -5386,
          -11429,
          0
        ]
      }
    },
    {
      "index": 8,
      "energy": 78,
      "bound_scaled": 78060,
      "scale": 1000,
      "excluded": true,
      "iterations": 125,
      "seconds": 1.877265453338623,
      "certificate": {
        "bound": 78060,
        "price": [
          -210,
          -327,
          -271,
          -219,
          139,
          140,
          160,
          140,
          138,
          157,
          -236,
          -200,
          -425,
          -221,
          164,
          165,
          79,
          216,
          215,
          80,
          -206,
          -205,
          60,
          59,
          292,
          36,
          37,
          291,
          -261,
          -215,
          166,
          165,
          114,
          157,
          155,
          112,
          178,
          176,
          96,
          228,
          226,
          96,
          60,
          57,
          295,
          41,
          41,
          295,
          -321,
          -100,
          -102,
          -321,
          -322,
          -101,
          -100,
          -319,
          -382,
          361,
          -139,
          -384,
          -225,
          0,
          -86,
          -195,
          -411,
          -74,
          61,
          58,
          405,
          30,
          27,
          410,
          0,
          7,
          -264,
          -127,
          38,
          -275,
          273,
          272,
          -184,
          220,
          221,
          -181,
          -187,
          -380,
          -66,
          0,
          -374,
          -53,
          94,
          94,
          383,
          51,
          50,
          388,
          -128,
          1,
          0,
          -140,
          22,
          -264,
          239,
          237,
          -173,
          188,
          189,
          -171,
          -257,
          -42,
          -285,
          -225,
          -113,
          0,
          514,
          515,
          -525,
          470,
          470,
          -522,
          -120,
          -368,
          -8,
          -146,
          0,
          -43,
          -164,
          -167,
          736,
          -231,
          -230,
          741,
          178,
          139,
          148,
          161,
          147,
          171,
          -163,
          0,
          -205,
          -188,
          -188,
          -200,
          178,
          137,
          149,
          162,
          147,
          172,
          0,
          -165,
          -205,
          -187,
          -187,
          -201,
          65,
          -504,
          637,
          40,
          -486,
          631,
          -1027,
          -1024,
          1183,
          0,
          -1135,
          1620,
          61,
          593,
          -515,
          77,
          594,
          -522,
          522,
          518,
          0,
          480,
          481,
          -2289,
          61,
          590,
          -516,
          77,
          594,
          -523,
          519,
          524,
          -2292,
          486,
          480,
          0,
          68,
          -499,
          642,
          48,
          -484,
          638,
          -1022,
          -1022,
          1621,
          -1131,
          0,
          1141,
          0,
          -151,
          -140,
          -85,
          -137,
          -140,
          13,
          15,
          110,
          48,
          50,
          111,
          -151,
          0,
          -139,
          -145,
          -40,
          -135,
          -14,
          -14,
          145,
          12,
          9,
          146,
          -140,
          -139,
          0,
          -130,
          -145,
          -120,
          71,
          70,
          64,
          122,
          121,
          62,
          -85,
          -145,
          -130,
          0,
          -152,
          -126,
          4,
          3,
          137,
          46,
          44,
          136,
          -137,
          -40,
          -145,
          -152,
          0,
          -155,
          -8,
          -9,
          147,
          14,
          11,
          148,
          -140,
          -135,
          -120,
          -126,
          -155,
          0,
          81,
          82,
          65,
          121,
          122,
          63,
          13,
          -14,
          71,
          4,
          -8,
          81,
          0,
          -144,
          51,
          -128,
          -129,
          49,
          15,
          -14,
          70,
          3,
          -9,
          82,
          -144,
          0,
          50,
          -130,
          -133,
          50,
          110,
          145,
          64,
          137,
          147,
          65,
          51,
          50,
          0,
          93,
          94,
          -212,
          48,
          12,
          122,
          46,
          14,
          121,
          -128,
          -130,
          93,
          0,
          -102,
          92,
          50,
          9,
          121,
          44,
          11,
          122,
          -129,
          -133,
          94,
          -102,
          0,
          91,
          111,
          146,
          62,
          136,
          148,
          63,
          49,
          50,
          -212,
          92,
          91,
          0
        ],
        "dual_left": [
          11984,
          12091,
          11925,
          11967,
          12038,
          11911,
          11870,
          11872,
          11737,
          11951,
          11958,
          11725,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156,
          12156
        ],
        "dual_right": [
          -11984,
          -12110,
          -12036,
          -11273,
          -11710,
          -11709,
          -7674,
          -9303,
          -9312,
          -7682,
          -11987,
          -11290,
          -11747,
          -11747,
          -7691,
          -9291,
          -9302,
          -7704,
          -11434,
          -11431,
          -10127,
          -6116,
          -6120,
          -10140,
          -8803,
          -8798,
          -8808,
          -8808,
          -11296,
          0
        ]
      }
    },
    {
      "index": 10,
      "energy": 60,
      "bound_scaled": 6021,
      "scale": 100,
      "excluded": true,
      "iterations": 47,
      "seconds": 0.672767162322998,
      "certificate": {
        "bound": 6021,
        "price": [
          16,
          -9,
          -9,
          18,
          -12,
          11,
          -11,
          -6,
          19,
          -3,
          18,
          -9,
          -7,
          17,
          -10,
          12,
          -13,
          -4,
          17,
          -3,
          15,
          -70,
          33,
          -39,
          19,
          18,
          -40,
          17,
          -6,
          19,
          -4,
          12,
          -9,
          1,
          21,
          1,
          -7,
          12,
          -6,
          3,
          20,
          2,
          32,
          -39,
          20,
          15,
          -40,
          18,
          -10,
          -13,
          14,
          -9,
          28,
          12,
          -87,
          39,
          34,
          -54,
          14,
          -18,
          -4,
          0,
          -14,
          2,
          2,
          -11,
          6,
          7,
          12,
          8,
          -8,
          0,
          0,
          -4,
          -9,
          0,
          0,
          -11,
          7,
          8,
          12,
          5,
          -8,
          0,
          -26,
          -26,
          27,
          0,
          -34,
          37,
          -14,
          -10,
          34,
          -14,
          -17,
          43,
          15,
          14,
          0,
          8,
          9,
          -56,
          24,
          18,
          -43,
          27,
          23,
          -39,
          14,
          15,
          -57,
          10,
          7,
          0,
          23,
          19,
          -42,
          27,
          23,
          -39,
          -27,
          -25,
          36,
          -35,
          0,
          28,
          -10,
          -11,
          33,
          -14,
          -17,
          42,
          10,
          12,
          4,
          4,
          8,
          6,
          -4,
          0,
          -22,
          4,
          -9,
          -13,
          7,
          8,
          6,
          10,
          6,
          8,
          0,
          -31,
          10,
          -3,
          -9,
          -12,
          -8,
          -9,
          33,
          -6,
          -10,
          34,
          -15,
          -36,
          21,
          0,
          -32,
          28,
          23,
          25,
          -39,
          22,
          23,
          -37,
          18,
          4,
          0,
          12,
          -1,
          -50,
          36,
          37,
          -46,
          35,
          36,
          -48,
          13,
          14,
          -110,
          34,
          -1,
          0,
          -12,
          -11,
          33,
          -16,
          -13,
          30,
          -20,
          -60,
          91,
          -42,
          0,
          20,
          0,
          9,
          -15,
          10,
          11,
          -17,
          15,
          -12,
          11,
          17,
          -10,
          9,
          9,
          0,
          -16,
          11,
          12,
          -17,
          15,
          -14,
          19,
          17,
          -10,
          10,
          -15,
          -16,
          0,
          -19,
          -17,
          30,
          -11,
          24,
          -19,
          -2,
          29,
          -10,
          10,
          11,
          -19,
          0,
          12,
          -17,
          15,
          -11,
          13,
          15,
          -9,
          14,
          11,
          12,
          -17,
          12,
          0,
          -19,
          13,
          -9,
          13,
          16,
          -10,
          12,
          -17,
          -17,
          30,
          -17,
          -19,
          0,
          -10,
          25,
          -14,
          -3,
          30,
          -8,
          15,
          15,
          -11,
          15,
          13,
          -10,
          0,
          -18,
          9,
          11,
          -15,
          4,
          -12,
          -14,
          24,
          -11,
          -9,
          25,
          -18,
          0,
          -37,
          -19,
          34,
          -41,
          11,
          19,
          -19,
          13,
          13,
          -14,
          9,
          -37,
          0,
          8,
          -35,
          28,
          17,
          17,
          -2,
          15,
          16,
          -3,
          11,
          -19,
          8,
          0,
          -19,
          3,
          -10,
          -10,
          29,
          -9,
          -10,
          30,
          -15,
          34,
          -35,
          -19,
          0,
          -41,
          9,
          10,
          -10,
          14,
          12,
          -8,
          4,
          -41,
          28,
          3,
          -41,
          0
        ],
        "dual_left": [
          735,
          727,
          764,
          728,
          733,
          758,
          731,
          772,
          761,
          722,
          774,
          770,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707,
          707
        ],
        "dual_right": [
          -633,
          -631,
          -635,
          -631,
          -577,
          -575,
          -633,
          -634,
          -575,
          -581,
          -826,
          -459,
          -642,
          -739,
          -417,
          -565,
          -733,
          0,
          -738,
          -645,
          -555,
          -419,
          -6,
          -736,
          -601,
          -654,
          -612,
          -122,
          -560,
          -214
        ]
      }
    },
    {
      "index": 11,
      "energy": 96,
      "bound_scaled": 9659,
      "scale": 100,
      "excluded": true,
      "iterations": 15,
      "seconds": 0.24743294715881348,
      "certificate": {
        "bound": 9659,
        "price": [
          15,
          -12,
          -7,
          10,
          -5,
          7,
          7,
          -8,
          5,
          11,
          10,
          -10,
          -9,
          14,
          -7,
          9,
          7,
          -8,
          10,
          7,
          10,
          -54,
          11,
          -30,
          -11,
          11,
          -24,
          -2,
          -7,
          10,
          -1,
          11,
          5,
          -2,
          16,
          7,
          -2,
          8,
          3,
          -4,
          17,
          8,
          12,
          -30,
          -13,
          14,
          -26,
          -1,
          1,
          -9,
          10,
          9,
          20,
          7,
          -25,
          6,
          11,
          -26,
          11,
          3,
          -6,
          0,
          -22,
          1,
          5,
          -21,
          10,
          4,
          7,
          9,
          0,
          13,
          0,
          -9,
          -17,
          1,
          3,
          -25,
          12,
          3,
          5,
          13,
          -2,
          16,
          8,
          6,
          -34,
          0,
          0,
          -25,
          19,
          -12,
          16,
          11,
          -23,
          34,
          -6,
          -8,
          0,
          -10,
          -4,
          15,
          -9,
          19,
          -8,
          -6,
          34,
          -17,
          -9,
          -5,
          12,
          -5,
          -7,
          0,
          -13,
          22,
          -7,
          -8,
          35,
          -15,
          9,
          13,
          -24,
          4,
          0,
          -28,
          14,
          -18,
          11,
          10,
          -25,
          34,
          4,
          4,
          -16,
          10,
          8,
          -19,
          1,
          0,
          -2,
          8,
          -14,
          16,
          12,
          9,
          5,
          5,
          4,
          10,
          0,
          6,
          -22,
          -1,
          11,
          -39,
          14,
          11,
          8,
          7,
          3,
          8,
          0,
          -36,
          20,
          0,
          -60,
          25,
          8,
          7,
          -14,
          12,
          12,
          -13,
          8,
          -8,
          0,
          1,
          33,
          -46,
          6,
          8,
          -13,
          5,
          6,
          -16,
          -6,
          41,
          -51,
          -1,
          21,
          0,
          6,
          10,
          -13,
          4,
          4,
          -14,
          2,
          -55,
          39,
          -6,
          0,
          23,
          0,
          17,
          -32,
          22,
          19,
          -33,
          22,
          -4,
          3,
          22,
          -1,
          11,
          17,
          0,
          -35,
          18,
          20,
          -32,
          22,
          -7,
          2,
          25,
          2,
          14,
          -32,
          -35,
          0,
          -35,
          -32,
          28,
          -27,
          14,
          1,
          -30,
          22,
          -2,
          22,
          18,
          -35,
          0,
          18,
          -33,
          21,
          -8,
          2,
          24,
          -6,
          11,
          19,
          20,
          -32,
          18,
          0,
          -35,
          22,
          -10,
          3,
          24,
          -8,
          13,
          -33,
          -32,
          28,
          -33,
          -35,
          0,
          -27,
          12,
          4,
          -29,
          20,
          -3,
          22,
          22,
          -27,
          21,
          22,
          -27,
          0,
          -10,
          -3,
          21,
          -10,
          7,
          -4,
          -7,
          14,
          -8,
          -10,
          12,
          -10,
          0,
          -26,
          -16,
          32,
          -11,
          3,
          2,
          1,
          2,
          3,
          4,
          -3,
          -26,
          0,
          -4,
          4,
          22,
          22,
          25,
          -30,
          24,
          24,
          -29,
          21,
          -16,
          -4,
          0,
          -17,
          10,
          -1,
          2,
          22,
          -6,
          -8,
          20,
          -10,
          32,
          4,
          -17,
          0,
          -28,
          11,
          14,
          -2,
          11,
          13,
          -3,
          7,
          -11,
          22,
          10,
          -28,
          0
        ],
        "dual_left": [
          1246,
          1253,
          1342,
          1253,
          1252,
          1349,
          1260,
          1322,
          1290,
          1259,
          1255,
          1247,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205,
          1205
        ],
        "dual_right": [
          -858,
          -857,
          -857,
          -856,
          -1103,
          -1107,
          -1105,
          -1097,
          -1020,
          -1022,
          -1399,
          -1246,
          -1168,
          -1292,
          -840,
          -1158,
          -989,
          -1,
          -1295,
          -1175,
          -1155,
          -837,
          0,
          -988,
          -1027,
          -952,
          -1088,
          -283,
          -1090,
          -295
        ]
      }
    },
    {
      "index": 12,
      "energy": 90,
      "bound_scaled": 90001,
      "scale": 1000,
      "excluded": true,
      "iterations": 329,
      "seconds": 4.524826288223267,
      "certificate": {
        "bound": 90001,
        "price": [
          -356,
          -315,
          -311,
          -358,
          185,
          186,
          222,
          180,
          182,
          215,
          -355,
          -316,
          -314,
          -354,
          184,
          186,
          225,
          180,
          181,
          214,
          -522,
          -262,
          193,
          192,
          311,
          209,
          209,
          314,
          -428,
          -514,
          278,
          282,
          197,
          262,
          263,
          187,
          284,
          282,
          193,
          263,
          262,
          181,
          191,
          190,
          306,
          211,
          212,
          312,
          -463,
          -237,
          -236,
          -451,
          -467,
          -237,
          -236,
          -450,
          -482,
          251,
          -243,
          -468,
          -367,
          0,
          -175,
          -137,
          -139,
          -176,
          212,
          213,
          167,
          114,
          111,
          177,
          0,
          -368,
          -176,
          -137,
          -140,
          -176,
          212,
          212,
          170,
          115,
          113,
          175,
          -551,
          -551,
          209,
          0,
          -858,
          213,
          -57,
          -58,
          955,
          -124,
          -125,
          947,
          92,
          89,
          0,
          77,
          80,
          -856,
          538,
          534,
          -752,
          484,
          483,
          -769,
          91,
          95,
          -859,
          79,
          78,
          0,
          536,
          539,
          -757,
          486,
          484,
          -772,
          -553,
          -555,
          216,
          -854,
          0,
          214,
          -57,
          -59,
          955,
          -128,
          -127,
          948,
          137,
          137,
          117,
          145,
          145,
          116,
          -29,
          0,
          -316,
          -73,
          -75,
          -304,
          136,
          136,
          116,
          145,
          145,
          117,
          0,
          -28,
          -314,
          -72,
          -73,
          -308,
          -201,
          -197,
          975,
          -270,
          -280,
          975,
          -1212,
          -1213,
          1298,
          0,
          -1333,
          1458,
          538,
          536,
          -766,
          507,
          513,
          -767,
          466,
          465,
          0,
          383,
          386,
          -2261,
          538,
          539,
          -767,
          509,
          514,
          -765,
          461,
          466,
          -2262,
          387,
          380,
          0,
          -200,
          -199,
          976,
          -272,
          -278,
          973,
          -1214,
          -1215,
          1442,
          -1332,
          0,
          1319,
          0,
          -208,
          -159,
          -188,
          -189,
          -161,
          68,
          66,
          118,
          97,
          97,
          119,
          -208,
          0,
          -159,
          -189,
          -188,
          -160,
          67,
          68,
          122,
          96,
          93,
          120,
          -159,
          -159,
          0,
          -158,
          -168,
          -171,
          111,
          108,
          90,
          144,
          146,
          82,
          -188,
          -189,
          -158,
          0,
          -182,
          -160,
          48,
          49,
          190,
          98,
          91,
          193,
          -189,
          -188,
          -168,
          -182,
          0,
          -169,
          46,
          48,
          195,
          99,
          95,
          193,
          -161,
          -160,
          -171,
          -160,
          -169,
          0,
          109,
          113,
          90,
          147,
          146,
          84,
          68,
          67,
          111,
          48,
          46,
          109,
          0,
          -211,
          -26,
          -168,
          -170,
          -18,
          66,
          68,
          108,
          49,
          48,
          113,
          -211,
          0,
          -29,
          -170,
          -170,
          -16,
          118,
          122,
          90,
          190,
          195,
          90,
          -26,
          -29,
          0,
          12,
          11,
          -187,
          97,
          96,
          144,
          98,
          99,
          147,
          -168,
          -170,
          12,
          0,
          -135,
          20,
          97,
          93,
          146,
          91,
          95,
          146,
          -170,
          -170,
          11,
          -135,
          0,
          20,
          119,
          120,
          82,
          193,
          193,
          84,
          -18,
          -16,
          -187,
          20,
          20,
          0
        ],
        "dual_left": [
          12010,
          12013,
          12088,
          12062,
          12065,
          12087,
          12002,
          12007,
          12067,
          12150,
          12160,
          12048,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424,
          12424
        ],
        "dual_right": [
          -11530,
          -11526,
          -11526,
          -11528,
          -12804,
          -12803,
          -8696,
          -8696,
          -8700,
          -8701,
          -12303,
          -9414,
          -11435,
          -11433,
          -4983,
          -10833,
          -10838,
          -4995,
          -11422,
          -11427,
          -10838,
          -4990,
          -4999,
          -10833,
          -9079,
          -9082,
          -9091,
          -9090,
          -11423,
          0
        ]
      }
    },
    {
      "index": 13,
      "energy": 36,
      "bound_scaled": 36014,
      "scale": 1000,
      "excluded": true,
      "iterations": 217,
      "seconds": 3.158066749572754,
      "certificate": {
        "bound": 36014,
        "price": [
          4,
          -284,
          -283,
          2,
          -21,
          155,
          155,
          -22,
          113,
          117,
          3,
          -287,
          -285,
          5,
          -23,
          156,
          155,
          -22,
          114,
          116,
          38,
          260,
          -83,
          16,
          13,
          -83,
          -20,
          -22,
          -244,
          38,
          16,
          189,
          186,
          15,
          156,
          155,
          16,
          189,
          191,
          14,
          154,
          153,
          -83,
          17,
          17,
          -82,
          -23,
          -24,
          39,
          260,
          5,
          0,
          -249,
          42,
          -288,
          -282,
          -284,
          -284,
          2,
          2,
          -53,
          0,
          -38,
          -66,
          -65,
          -36,
          58,
          25,
          24,
          61,
          45,
          45,
          0,
          -54,
          -34,
          -65,
          -63,
          -39,
          59,
          25,
          23,
          59,
          44,
          45,
          -289,
          -290,
          135,
          0,
          -316,
          138,
          -156,
          222,
          222,
          -157,
          244,
          247,
          132,
          129,
          0,
          108,
          113,
          -271,
          258,
          -192,
          -192,
          257,
          -172,
          -170,
          129,
          130,
          -269,
          111,
          111,
          0,
          256,
          -190,
          -195,
          258,
          -169,
          -172,
          -292,
          -291,
          138,
          -316,
          0,
          136,
          -154,
          225,
          220,
          -156,
          245,
          245,
          245,
          244,
          -157,
          221,
          221,
          -153,
          135,
          0,
          -313,
          137,
          -289,
          -291,
          -169,
          -169,
          258,
          -192,
          -192,
          257,
          0,
          105,
          113,
          -269,
          130,
          128,
          -169,
          -171,
          258,
          -189,
          -198,
          259,
          -268,
          114,
          109,
          0,
          127,
          128,
          246,
          243,
          -156,
          221,
          224,
          -156,
          138,
          -314,
          0,
          133,
          -291,
          -288,
          46,
          47,
          58,
          23,
          26,
          59,
          -38,
          -65,
          -66,
          -34,
          -56,
          0,
          46,
          46,
          59,
          24,
          25,
          60,
          -36,
          -65,
          -67,
          -37,
          0,
          -55,
          0,
          35,
          -62,
          40,
          38,
          -61,
          71,
          -64,
          -67,
          71,
          -65,
          -64,
          35,
          0,
          -63,
          38,
          40,
          -61,
          69,
          -63,
          -65,
          70,
          -67,
          -69,
          -62,
          -63,
          0,
          -57,
          -59,
          -119,
          166,
          71,
          71,
          166,
          71,
          67,
          40,
          38,
          -57,
          0,
          40,
          -58,
          69,
          -63,
          -64,
          68,
          -65,
          -68,
          38,
          40,
          -59,
          40,
          0,
          -57,
          71,
          -62,
          -63,
          70,
          -67,
          -65,
          -61,
          -61,
          -119,
          -58,
          -57,
          0,
          166,
          69,
          71,
          166,
          66,
          72,
          71,
          69,
          166,
          69,
          71,
          166,
          0,
          -59,
          -57,
          -121,
          -61,
          -62,
          -64,
          -63,
          71,
          -63,
          -62,
          69,
          -59,
          0,
          41,
          -56,
          38,
          38,
          -67,
          -65,
          71,
          -64,
          -63,
          71,
          -57,
          41,
          0,
          -60,
          33,
          38,
          71,
          70,
          166,
          68,
          70,
          166,
          -121,
          -56,
          -60,
          0,
          -61,
          -61,
          -65,
          -67,
          71,
          -65,
          -67,
          66,
          -61,
          38,
          33,
          -61,
          0,
          36,
          -64,
          -69,
          67,
          -68,
          -65,
          72,
          -62,
          38,
          38,
          -61,
          36,
          0
        ],
        "dual_left": [
          3711,
          3713,
          3396,
          3722,
          3714,
          3390,
          3395,
          3715,
          3720,
          3393,
          3719,
          3712,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636,
          3636
        ],
        "dual_right": [
          -2869,
          -2869,
          -2875,
          -2871,
          -2696,
          -2696,
          -2702,
          -2697,
          -3767,
          -3766,
          -3596,
          -226,
          -3606,
          0,
          -6,
          -3604,
          -2707,
          -2705,
          0,
          -3601,
          -3602,
          -1,
          -2704,
          -2706,
          -3601,
          -225,
          -2875,
          -2872,
          -2872,
          -2873
        ]
      }
    },
    {
      "index": 14,
      "energy": 60,
      "bound_scaled": 60019,
      "scale": 1000,
      "excluded": true,
      "iterations": 122,
      "seconds": 1.7224183082580566,
      "certificate": {
        "bound": 60019,
        "price": [
          9,
          -224,
          -225,
          11,
          172,
          182,
          -186,
          170,
          232,
          -91,
          12,
          -226,
          -225,
          11,
          174,
          181,
          -185,
          169,
          231,
          -88,
          17,
          -414,
          -62,
          -179,
          361,
          -4,
          -173,
          314,
          -207,
          17,
          244,
          192,
          -130,
          231,
          232,
          -76,
          242,
          189,
          -125,
          231,
          232,
          -77,
          -62,
          -179,
          363,
          -2,
          -176,
          313,
          -21,
          -139,
          -309,
          -7,
          214,
          -345,
          -304,
          126,
          198,
          -685,
          -191,
          47,
          -116,
          0,
          -118,
          -83,
          -85,
          -118,
          133,
          106,
          91,
          98,
          52,
          40,
          0,
          -119,
          -117,
          -83,
          -85,
          -119,
          132,
          108,
          95,
          91,
          54,
          43,
          -226,
          -229,
          125,
          0,
          -280,
          129,
          -488,
          390,
          426,
          -525,
          392,
          286,
          47,
          46,
          0,
          43,
          49,
          -435,
          527,
          -273,
          -249,
          720,
          -228,
          -247,
          45,
          50,
          -438,
          45,
          44,
          0,
          530,
          -275,
          -252,
          723,
          -225,
          -247,
          -228,
          -226,
          130,
          -280,
          0,
          124,
          -486,
          388,
          425,
          -522,
          392,
          283,
          419,
          421,
          -613,
          430,
          431,
          -613,
          653,
          0,
          -674,
          902,
          -752,
          -604,
          -221,
          -220,
          618,
          -266,
          -267,
          618,
          0,
          259,
          230,
          -1328,
          449,
          128,
          -257,
          -258,
          597,
          -275,
          -276,
          597,
          -836,
          517,
          -117,
          0,
          397,
          -89,
          377,
          378,
          -496,
          351,
          348,
          -493,
          650,
          -805,
          0,
          535,
          -726,
          -119,
          -30,
          -28,
          336,
          -47,
          -47,
          334,
          -246,
          268,
          -420,
          -259,
          139,
          0,
          290,
          293,
          -262,
          271,
          272,
          -260,
          -105,
          -529,
          53,
          -101,
          0,
          78,
          0,
          -12,
          -150,
          -16,
          -14,
          -152,
          78,
          24,
          157,
          71,
          -13,
          127,
          -12,
          0,
          -153,
          -14,
          -13,
          -152,
          77,
          25,
          163,
          74,
          -13,
          126,
          -150,
          -153,
          0,
          -144,
          -145,
          158,
          165,
          153,
          -189,
          90,
          148,
          -171,
          -16,
          -14,
          -144,
          0,
          -16,
          -144,
          59,
          24,
          166,
          65,
          -10,
          136,
          -14,
          -13,
          -145,
          -16,
          0,
          -146,
          60,
          22,
          168,
          65,
          -10,
          133,
          -152,
          -152,
          158,
          -144,
          -146,
          0,
          169,
          150,
          -188,
          89,
          148,
          -168,
          78,
          77,
          165,
          59,
          60,
          169,
          0,
          98,
          -145,
          16,
          61,
          -174,
          24,
          25,
          153,
          24,
          22,
          150,
          98,
          0,
          -304,
          100,
          113,
          -251,
          157,
          163,
          -189,
          166,
          168,
          -188,
          -145,
          -304,
          0,
          -133,
          -267,
          180,
          71,
          74,
          90,
          65,
          65,
          89,
          16,
          100,
          -133,
          0,
          35,
          -138,
          -13,
          -13,
          148,
          -10,
          -10,
          148,
          61,
          113,
          -267,
          35,
          0,
          -248,
          127,
          126,
          -171,
          136,
          133,
          -168,
          -174,
          -251,
          180,
          -138,
          -248,
          0
        ],
        "dual_left": [
          7094,
          7093,
          7430,
          7086,
          7086,
          7432,
          7139,
          7271,
          7414,
          7051,
          7213,
          7573,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116,
          7116
        ],
        "dual_right": [
          -5910,
          -5911,
          -5910,
          -5909,
          -4985,
          -4987,
          -5190,
          -5188,
          -7476,
          -7476,
          -7697,
          -4967,
          -6484,
          -1944,
          -3650,
          -7229,
          -5151,
          -6105,
          -1948,
          -6482,
          -7229,
          -3653,
          -6109,
          -5158,
          -6989,
          0,
          -6041,
          -4310,
          -4877,
          -5561
        ]
      }
    },
    {
      "index": 15,
      "energy": 84,
      "bound_scaled": 84054,
      "scale": 1000,
      "excluded": true,
      "iterations": 363,
      "seconds": 5.321535110473633,
      "certificate": {
        "bound": 84054,
        "price": [
          -79,
          -433,
          141,
          -64,
          -267,
          307,
          114,
          -261,
          332,
          130,
          51,
          146,
          -617,
          65,
          312,
          -447,
          240,
          314,
          -426,
          257,
          39,
          -333,
          104,
          229,
          -133,
          105,
          254,
          -117,
          130,
          -72,
          -288,
          289,
          91,
          -282,
          309,
          106,
          312,
          -444,
          246,
          319,
          -421,
          263,
          114,
          241,
          -120,
          119,
          263,
          -105,
          -57,
          -428,
          157,
          -44,
          77,
          148,
          -598,
          88,
          14,
          -355,
          83,
          -118,
          53,
          0,
          96,
          40,
          -636,
          101,
          242,
          -414,
          331,
          253,
          -401,
          335,
          0,
          329,
          -430,
          -273,
          294,
          -431,
          -74,
          514,
          -200,
          -62,
          528,
          -195,
          -645,
          -671,
          865,
          0,
          -710,
          868,
          -465,
          -492,
          1090,
          -454,
          -482,
          1096,
          358,
          317,
          0,
          339,
          280,
          -1281,
          540,
          499,
          -1060,
          551,
          509,
          -1052,
          -28,
          587,
          -1269,
          -40,
          546,
          0,
          227,
          835,
          -974,
          238,
          848,
          -970,
          -368,
          -1042,
          746,
          -384,
          0,
          744,
          -114,
          -792,
          1049,
          -103,
          -784,
          1048,
          252,
          -404,
          320,
          226,
          -422,
          318,
          94,
          0,
          108,
          34,
          -633,
          107,
          -64,
          525,
          -209,
          -88,
          508,
          -211,
          0,
          370,
          -419,
          -286,
          300,
          -426,
          -432,
          -460,
          1104,
          -461,
          -478,
          1100,
          -640,
          -666,
          838,
          0,
          -744,
          839,
          573,
          534,
          -1047,
          543,
          515,
          -1046,
          364,
          325,
          0,
          297,
          252,
          -1310,
          235,
          861,
          -979,
          213,
          841,
          -982,
          -6,
          621,
          -1276,
          -69,
          541,
          0,
          -94,
          -786,
          1043,
          -123,
          -802,
          1036,
          -338,
          -1020,
          747,
          -401,
          0,
          738,
          0,
          -201,
          -55,
          116,
          -191,
          -57,
          168,
          -126,
          40,
          203,
          -95,
          38,
          -201,
          0,
          -127,
          -181,
          180,
          -128,
          -126,
          247,
          -29,
          -95,
          280,
          -30,
          -55,
          -127,
          0,
          -38,
          -117,
          105,
          31,
          -41,
          210,
          65,
          -7,
          214,
          116,
          -181,
          -38,
          0,
          -174,
          -38,
          183,
          -115,
          55,
          210,
          -80,
          54,
          -191,
          180,
          -117,
          -174,
          0,
          -118,
          -107,
          264,
          -11,
          -76,
          298,
          -12,
          -57,
          -128,
          105,
          -38,
          -118,
          0,
          28,
          -44,
          211,
          59,
          -11,
          209,
          168,
          -126,
          31,
          183,
          -107,
          28,
          0,
          -176,
          -47,
          115,
          -188,
          -51,
          -126,
          247,
          -41,
          -115,
          264,
          -44,
          -176,
          0,
          -115,
          -181,
          188,
          -121,
          40,
          -29,
          210,
          55,
          -11,
          211,
          -47,
          -115,
          0,
          -51,
          -126,
          97,
          203,
          -95,
          65,
          210,
          -76,
          59,
          115,
          -181,
          -51,
          0,
          -194,
          -57,
          -95,
          280,
          -7,
          -80,
          298,
          -11,
          -188,
          188,
          -126,
          -194,
          0,
          -131,
          38,
          -30,
          214,
          54,
          -12,
          209,
          -51,
          -121,
          97,
          -57,
          -131,
          0
        ],
        "dual_left": [
          8454,
          8614,
          8477,
          8536,
          8647,
          8472,
          8502,
          8665,
          8483,
          8474,
          8619,
          8449,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266,
          8266
        ],
        "dual_right": [
          -6293,
          -6622,
          -7236,
          -4842,
          -8364,
          -8884,
          -6049,
          -6376,
          -6914,
          -4526,
          -7462,
          -1668,
          -6075,
          -6404,
          -2108,
          -8495,
          -7162,
          -1373,
          -6948,
          -4546,
          -7144,
          -1357,
          0,
          -8375,
          -6312,
          -6637,
          -7217,
          -4818,
          -7484,
          -1691
        ]
      }
    }
  ],
  "human_exclusion": 9,
  "remaining_class": 16,
  "remaining_points": 12,
  "full_A33_excluded": false
}

```
<!-- END_FILE -->

<a id="source-07"></a>

### outputs/coupures_et_torsion/chercher_certificat_A33.py

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/chercher_certificat_A33.py" bytes="5897" sha256="1d41aebd49621a917fdb4e1b4ae9b9348c92f71a9800eedf6f6bdc36b49d2bbb" -->
```python
import json,time
from itertools import combinations
from collections import Counter
MU=[i^1 for i in range(12)]
TAU=[5,2,1,4,3,0,11,8,7,10,9,6]
PHI=[[0,0,0,0,0,0,0,1,6,0,1,6],[0,0,0,0,0,0,1,1,5,1,1,5],[0,0,0,0,0,0,1,2,4,1,2,4],[0,1,6,0,1,6,0,1,6,0,1,6],[0,1,6,0,1,6,0,2,5,0,2,5],[0,1,6,0,1,6,1,1,5,1,1,5],[0,1,6,0,1,6,1,2,4,1,2,4],[0,1,6,0,1,6,1,3,3,1,3,3],[0,1,6,0,1,6,2,2,3,2,2,3],[1,1,5,1,1,5,1,1,5,1,1,5],[1,1,5,1,1,5,1,2,4,1,2,4],[1,1,5,1,1,5,1,3,3,1,3,3],[1,1,5,1,1,5,2,2,3,2,2,3],[1,1,5,1,1,5,2,6,6,2,6,6],[1,1,5,1,1,5,3,5,6,3,5,6],[1,2,4,1,2,4,1,2,4,1,2,4],[1,2,4,1,2,4,3,5,6,3,5,6]]
L=list(range(12))
EDGES=[e for e in combinations(L,2) if e[0]//2!=e[1]//2]
EIDX={e:i for i,e in enumerate(EDGES)}
SIGE=lambda e:tuple(sorted(i^1 for i in e))
REPS=[e for e in EDGES if e<SIGE(e)]
K2=[[2-(a==b)-(b==(a^1))-(b==MU[a])-(b==TAU[a^1]) for b in L] for a in L]
K3=[[2-(d==(b^1))-(d==TAU[MU[b]])-(d==MU[TAU[b]])-(d==TAU[b]) for d in L] for b in L]
BASE=[]
for z in REPS:
    zz=SIGE(z)
    left=[e for e in EDGES if all(K2[a][b]>0 for a in z for b in e)]
    right=[e for e in EDGES if all(K2[a][b]>0 for a in zz for b in e)]
    v=[]
    for e in left:
        for f in right:
            if e==f:continue
            count=Counter((b,d) for b in e for d in f)
            count.update((b,d) for b in f for d in e)
            if any(n>K3[b][d] for (b,d),n in count.items()):continue
            common=set(e)&set(f)
            assert len(common)<=1
            v.append((e,f,next(iter(common)) if common else -1))
    BASE.append(v)
print('A33_BASE',json.dumps({'domain_min':min(map(len,BASE)),'domain_max':max(map(len,BASE))}),flush=True)

def has_matching(doms):
    match={}
    def augment(u,seen):
        for v in doms[u]:
            if v in seen:continue
            seen.add(v)
            if v not in match or augment(match[v],seen):match[v]=u;return True
        return False
    return sum(augment(u,set()) for u in range(len(doms)))

def assignment_cost(cost):
    n=len(cost);u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
    for i in range(1,n+1):
        p[0]=i;j0=0;mn=[10**9]*(n+1);used=[False]*(n+1)
        while True:
            used[j0]=True;i0=p[j0];delta=10**9;j1=0
            for j in range(1,n+1):
                if used[j]:continue
                cur=cost[i0-1][j-1]-u[i0]-v[j]
                if cur<mn[j]:mn[j]=cur;way[j]=j0
                if mn[j]<delta:delta=mn[j];j1=j
            for j in range(n+1):
                if used[j]:u[p[j]]+=delta;v[j]-=delta
                else:mn[j]-=delta
            j0=j1
            if p[j0]==0:break
        while True:
            j1=way[j0];p[j0]=p[j1];j0=j1
            if j0==0:break
    match=[-1]*n
    for j in range(1,n+1):match[p[j]-1]=j-1
    val=sum(cost[i][match[i]] for i in range(n))
    assert val==sum(u[1:])+sum(v[1:])
    assert all(u[i+1]+v[j+1]<=cost[i][j] for i in range(n) for j in range(n))
    return val,match,u[1:],v[1:]

import numpy as np
SCALE=1000
LAG_RESULTS=[]
import sys
CASE_SPECS=json.loads(sys.argv[1]) if len(sys.argv)>1 else [[6,2]]
for index,multiplier in CASE_SPECS:
    phi0=[(multiplier*a)%7 for a in PHI[index]];phi=[]
    for j in (0,6):
        a=phi0[j] if phi0[j]<=3 else phi0[j]-7
        b=phi0[j+1] if phi0[j+1]<=3 else phi0[j+1]-7
        phi.extend([a,b,-a-b,a,b,-a-b])
    energy=3*sum(x*x for x in phi)//2
    cols=[];weights=[];by=[{} for k in REPS]
    for k,z in enumerate(REPS):
        zz=SIGE(z);dz=sum(phi[a] for a in z)-sum(phi[a] for a in zz)
        for e,f,b in BASE[k]:
            charge=sum(phi[a] for a in e)-sum(phi[a] for a in f)+2*dz
            if charge%7:continue
            row=[0]*348;row[EIDX[e]]=1;row[EIDX[f]]=1
            for a in z:
                for d in e:row[60+12*a+d]+=1
            for a in zz:
                for d in f:row[60+12*a+d]+=1
            for a in e:
                for d in f:row[204+12*a+d]+=1
            for a in f:
                for d in e:row[204+12*a+d]+=1
            by[k].setdefault(b,[]).append(len(cols));cols.append(row);weights.append(SCALE*(charge//7)**2)
    C=np.array(cols,dtype=np.int64);W=np.array(weights,dtype=np.int64)
    target=np.array([1]*60+[K2[a][b] for a in L for b in L]+[K3[a][b] for a in L for b in L],dtype=np.int64)
    price=np.zeros(348,dtype=np.int64);best=-10**20;cert=None;start=time.time()
    for it in range(800):
        vals=W-C@price
        dc=[[10**8]*30 for _ in range(30)];arg={}
        for k,dct in enumerate(by):
            for b,idxs in dct.items():
                j=min(idxs,key=lambda j:int(vals[j]));cost=int(vals[j])
                rows=[b] if b>=0 else range(12,30)
                for row in rows:dc[row][k]=cost;arg[row,k]=j
        val,matching,du,dv=assignment_cost(dc)
        bound=val+int(target@price)
        if bound>best:
            best=bound;cert={'price':[int(x) for x in price],'dual_left':du,'dual_right':dv,'bound':int(bound),'iteration':it}
        if bound>SCALE*energy:break
        chosen=[arg[r,k] for r,k in enumerate(matching)]
        usage=C[chosen].sum(axis=0);grad=target-usage
        norm=int(grad@grad)
        if not norm:break
        step=max(1,int((SCALE*energy-bound)//max(1,norm)))
        price+=step*grad
        if it%10==0 and time.time()-start>28:break
    p=np.array(cert['price'],dtype=np.int64);v=W-C@p
    for k,dct in enumerate(by):
        for b,idxs in dct.items():
            rows=[b] if b>=0 else range(12,30)
            for r in rows:
                assert all(int(v[j])>=cert['dual_left'][r]+cert['dual_right'][k] for j in idxs)
    assert cert['bound']==int(target@p)+sum(cert['dual_left'])+sum(cert['dual_right'])
    ans={'index':index,'multiplier':multiplier,'energy':energy,'bound_scaled':int(best),'scale':SCALE,'excluded':best>SCALE*energy,'iterations':it+1,'seconds':time.time()-start,'certificate':cert}
    LAG_RESULTS.append(ans)
    print('A33_LAG',json.dumps(ans),flush=True)

```
<!-- END_FILE -->

<a id="source-08"></a>

### outputs/coupures_et_torsion/exploration_F7_equivariante.py

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/exploration_F7_equivariante.py" bytes="3324" sha256="9220bf2581ef3bbeaba761727fa418adbe2019bd43b23ee143dd20c5218955ea" -->
```python
import itertools,time,json
from sage.all import *
L=list(range(12))
pi=[a^1 for a in L]
tau=[5,2,1,4,3,0,11,8,7,10,9,6]
mu=pi[:]
values=[1,2,4,1,2,4,3,5,6,3,5,6]
eps=[(a%2)^int(values[a] not in (1,2,4)) for a in L]
li={(values[a],eps[a]):a for a in L}
H=[[li[(lam*values[a]%7,eps[a])] for a in L] for lam in range(1,7)]
assert all(h[pi[a]]==pi[h[a]] and h[tau[a]]==tau[h[a]] for h in H for a in L)
def act(p,e):return tuple(sorted(p[a] for a in e))
E=[e for e in itertools.combinations(L,2) if mu[e[0]]!=e[1]]
K2=[[2-int(a==b)-int(pi[a]==b)-int(mu[a]==b)-int(tau[pi[a]]==b) for b in L] for a in L]
K3=[[2-int(pi[a]==b)-int(tau[a]==b)-int(tau[mu[a]]==b)-int(mu[tau[a]]==b) for b in L] for a in L]
O=[];seen=set()
for e in E:
 if e in seen:continue
 orb=sorted(set(act(h,e) for h in H));seen.update(orb);O.append(orb)
oi={e:i for i,orb in enumerate(O) for e in orb}
seen=set();Groups=[]
for i,orb in enumerate(O):
 if i in seen:continue
 j=oi[act(pi,orb[0])]; seen|={i,j}; Groups.append(sorted({i,j}))
Maps=[]
for orb in O:
 cand=[];z=orb[0]
 for k,out in enumerate(O):
  if len(orb)!=len(out):continue
  for e in out:
   m={};ok=True
   for h in H:
    zz,ee=act(h,z),act(h,e)
    if zz in m and m[zz]!=ee:ok=False;break
    m[zz]=ee
   if ok and len(set(m.values()))==len(orb):cand.append((k,m))
 Maps.append(cand)
dom=[]
for grp in Groups:
 dc=[]
 combos=itertools.product(*(Maps[i] for i in grp))
 for cm in combos:
  outs=tuple(k for k,m in cm)
  if len(set(outs))<len(outs):continue
  mp={z:e for k,m in cm for z,e in m.items()}; c2={};c3={}
  for z,e in mp.items():
   for a in z:
    for b in e:c2[a,b]=c2.get((a,b),0)+1
   f=mp[act(pi,z)]
   for a in e:
    for b in f:c3[a,b]=c3.get((a,b),0)+1
  if any(v>K2[a][b] for (a,b),v in c2.items()) or any(v>K3[a][b] for (a,b),v in c3.items()):continue
  if any((sum(values[a] for a in mp[z])-sum(values[a] for a in mp[act(pi,z)])+2*(sum(values[a] for a in z)-sum(values[a] for a in act(pi,z))))%7 for z in mp):continue
  dc.append((sum(1<<k for k in outs),c2,c3,mp))
 dom.append(dc)
print('RHO_F7_SETUP',json.dumps({'orbit_sizes':[len(o) for o in O],'groups':Groups,'domains':[len(d) for d in dom]}),flush=True)
nodes=0;start=time.time();sol=None;stopped=False
cur2=[[0]*12 for _ in L];cur3=[[0]*12 for _ in L]
def fits(c,used):
 mask,d2,d3,mp=c
 return not mask&used and all(cur2[a][b]+v<=K2[a][b] for (a,b),v in d2.items()) and all(cur3[a][b]+v<=K3[a][b] for (a,b),v in d3.items())
def dfs(rem,used,chosen):
 global nodes,sol,stopped
 nodes+=1
 if time.time()-start>8:stopped=True;return False
 if not rem:sol=chosen[:];return True
 ds=[]
 for i in rem:
  cs=[c for c in dom[i] if fits(c,used)]
  if not cs:return False
  ds.append((len(cs),i,cs))
 _,i,cs=min(ds,key=lambda t:t[0]);rr=[j for j in rem if j!=i]
 for c in cs:
  mask,d2,d3,mp=c
  for (a,b),v in d2.items():cur2[a][b]+=v
  for (a,b),v in d3.items():cur3[a][b]+=v
  if dfs(rr,used|mask,chosen+[c]):return True
  for (a,b),v in d2.items():cur2[a][b]-=v
  for (a,b),v in d3.items():cur3[a][b]-=v
  if stopped:return False
 return False
dfs(list(range(len(Groups))),0,[])
ans={'nodes':nodes,'seconds':time.time()-start,'status':'found' if sol else 'timeout' if stopped else 'exhausted'}
if sol:ans['phi']=[[list(z),list(e)] for c in sol for z,e in c[3].items()]
print('RHO_F7_RESULT',json.dumps(ans),flush=True)

```
<!-- END_FILE -->

<a id="source-09"></a>

### outputs/coupures_et_torsion/sorties_A33_independantes.txt

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/sorties_A33_independantes.txt" bytes="2272" sha256="97b3052a58c8bad9ec7157cb69c884593e00d3a06197d26e3fb2940d2e364ae3" -->
```text
A33_INDEPENDENT_COVERAGE {"group": 72, "projective_points": 400, "orbit_sizes": [6, 6, 4, 18, 36, 36, 72, 36, 36, 9, 36, 18, 18, 9, 36, 12, 12]}
A33_INDEPENDENT_CERT {"index": 0, "energy": 6, "bound_scaled": 900, "scale": 100, "columns_checked": 6355, "valid": true}
A33_INDEPENDENT_CERT {"index": 1, "energy": 18, "bound_scaled": 2000, "scale": 100, "columns_checked": 10345, "valid": true}
A33_INDEPENDENT_CERT {"index": 2, "energy": 42, "bound_scaled": 4249, "scale": 100, "columns_checked": 6882, "valid": true}
A33_INDEPENDENT_CERT {"index": 3, "energy": 12, "bound_scaled": 1245, "scale": 100, "columns_checked": 8337, "valid": true}
A33_INDEPENDENT_CERT {"index": 4, "energy": 30, "bound_scaled": 3021, "scale": 100, "columns_checked": 7276, "valid": true}
A33_INDEPENDENT_CERT {"index": 5, "energy": 24, "bound_scaled": 2401, "scale": 100, "columns_checked": 7081, "valid": true}
A33_INDEPENDENT_CERT {"index": 6, "energy": 66, "bound_scaled": 66014, "scale": 1000, "columns_checked": 7116, "valid": true}
A33_INDEPENDENT_CERT {"index": 7, "energy": 84, "bound_scaled": 84017, "scale": 1000, "columns_checked": 7023, "valid": true}
A33_INDEPENDENT_CERT {"index": 8, "energy": 78, "bound_scaled": 78060, "scale": 1000, "columns_checked": 7035, "valid": true}
A33_INDEPENDENT_CERT {"index": 10, "energy": 60, "bound_scaled": 6021, "scale": 100, "columns_checked": 6712, "valid": true}
A33_INDEPENDENT_CERT {"index": 11, "energy": 96, "bound_scaled": 9659, "scale": 100, "columns_checked": 6571, "valid": true}
A33_INDEPENDENT_CERT {"index": 12, "energy": 90, "bound_scaled": 90001, "scale": 1000, "columns_checked": 7046, "valid": true}
A33_INDEPENDENT_CERT {"index": 13, "energy": 36, "bound_scaled": 36014, "scale": 1000, "columns_checked": 7274, "valid": true}
A33_INDEPENDENT_CERT {"index": 14, "energy": 60, "bound_scaled": 60019, "scale": 1000, "columns_checked": 6848, "valid": true}
A33_INDEPENDENT_CERT {"index": 15, "energy": 84, "bound_scaled": 84054, "scale": 1000, "columns_checked": 6711, "valid": true}
A33_SURVIVOR_LINES {"points": 12, "projective_lines_through_pairs": 58, "lines_contained": 0, "maximum_intersection": 3}
A33_HUMAN9 {"edge_weights_mod7": [2, 3, 6], "differences_mod7": [0, 1, 3, 4, 6], "required_difference": 5, "impossible": true}

```
<!-- END_FILE -->

<a id="source-10"></a>

### outputs/coupures_et_torsion/sorties_F7_equivariantes.txt

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/sorties_F7_equivariantes.txt" bytes="247" sha256="88f8c72d4ffb5d0b3bc9def8e692ec54db6ad32547d9aae5dd7e124263c122f9" -->
```text
RHO_F7_SETUP {"orbit_sizes": [6, 6, 6, 6, 6, 6, 6, 3, 6, 6, 3], "groups": [[0, 8], [1, 2], [3, 5], [4, 9], [6], [7, 10]], "domains": [142, 149, 144, 141, 6, 13]}
RHO_SYM_RESULT {"nodes": 1163, "seconds": 1.4013724327087402, "status": "exhausted"}

```
<!-- END_FILE -->

<a id="source-11"></a>

### outputs/coupures_et_torsion/sorties_normes_et_controles.txt

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/sorties_normes_et_controles.txt" bytes="740" sha256="8b29414396899c7dbfc53c879d08d15f1407a3d4b12e500e837ffe69486618f6" -->
```text
NORM10_CUT_INDEPENDENT [{"n0_n1_n2_n3": [2, 20, 10, 0], "unused_pair_choices": 9, "balanced_cut_choices": 0}, {"n0_n1_n2_n3": [1, 23, 7, 1], "unused_pair_choices": 14, "balanced_cut_choices": 0}, {"n0_n1_n2_n3": [0, 26, 4, 2], "unused_pair_choices": 9, "balanced_cut_choices": 0}]
NORM10_SIX_PROFILES {"profiles": [[1, 24, 5, 2], [2, 21, 8, 1], [3, 18, 11, 0]], "small_pair_selected_max": 1}
H23_GLOBAL_CONTROL {"outside_t": [2, 2, 2], "sum": 6, "pair_sum": 3, "root_only_hypothesis": false}
COMPACT_CONTROL {"m": 2, "vertices": 9, "labels": 2, "far": 0, "bijection": true, "K2": true, "K3": true, "free": false}
COMPACT_CONTROL {"m": 11, "vertices": 243, "labels": 20, "far": 180, "bijection": true, "K2": true, "K3": true, "free": false}

```
<!-- END_FILE -->

<a id="source-12"></a>

### outputs/coupures_et_torsion/tentative_classe16.json

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/tentative_classe16.json" bytes="99" sha256="0d7bf08f1b0fc26f1d543bb40d120899d22e2a84c2a2b774dbe5524089ee2ac6" -->
```json
{
  "index": 16,
  "energy": 84,
  "bound_scaled": 839623,
  "scale": 10000,
  "excluded": false
}

```
<!-- END_FILE -->

<a id="source-13"></a>

### outputs/coupures_et_torsion/verifier_A33_independant.py

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/verifier_A33_independant.py" bytes="4503" sha256="e157c07e410e4fa90902f269ed8985d9f7993fd3436fbc9fa10c9ed73bc044db" -->
```python
import json
with open("certificats_A33.json",encoding="utf-8") as fp:
    DATA=json.load(fp)
PHI=DATA["phi_reps"]
CASES=DATA["cases"]
from itertools import combinations,permutations,product
import json
L=range(12);sig=[i^1 for i in L];tau=[5,2,1,4,3,0,11,8,7,10,9,6]
E=list(combinations(L,2));E=[e for e in E if sig[e[0]]!=e[1]]
idx={e:j for j,e in enumerate(E)}
flip=lambda e:tuple(sorted(sig[a] for a in e))
Z=[e for e in E if e<flip(e)]
k2=[[2-int(a==b)-2*int(b==sig[a])-int(b==tau[sig[a]]) for b in L] for a in L]
k3=[[2-int(b==sig[a])-int(b==tau[a])-int(b==tau[sig[a]])-int(b==sig[tau[a]]) for b in L] for a in L]
def norm(p):
 t=pow(next(a for a in p if a),-1,7)
 return tuple((t*a)%7 for a in p)
small=[p for p in permutations(range(6)) if all(p[sig[a]]==sig[p[a]] and p[tau[a]]==tau[p[a]] for a in range(6))]
assert len(small)==6
G=[]
for p,q,swap in product(small,small,range(2)):
 G.append(tuple([p[a]+6*swap for a in range(6)]+[q[a]+6*(1-swap) for a in range(6)]))
assert len(set(G))==72
allpoints=set()
for a,b,c,d in product(range(7),repeat=4):
 if not(a or b or c or d):continue
 allpoints.add(norm((a,b,(-a-b)%7,a,b,(-a-b)%7,c,d,(-c-d)%7,c,d,(-c-d)%7)))
assert len(allpoints)==400
covered=set();osizes=[]
for p in PHI:
 orb={norm(tuple(p[g[i]] for i in L)) for g in G}
 assert not covered&orb
 covered|=orb;osizes.append(len(orb))
assert covered==allpoints
print('A33_INDEPENDENT_COVERAGE',json.dumps({'group':len(G),'projective_points':len(allpoints),'orbit_sizes':osizes}),flush=True)

def quad(A,x,y):return sum(x[a]*A[a][b]*y[b] for a in L for b in L)
CHECKS=[]
for case in CASES:
 p0=[(case.get('multiplier',1)*a)%7 for a in PHI[case['index']]];p=[]
 for j in (0,6):
  a=p0[j] if p0[j]<=3 else p0[j]-7;b=p0[j+1] if p0[j+1]<=3 else p0[j+1]-7
  p.extend((a,b,-a-b,a,b,-a-b))
 energy=3*sum(a*a for a in p)//2
 outGram=[[9*int(a==b)+1-int(b==sig[a]) for b in L] for a in L]
 inGram=outGram
 crossGram=[[1-int(a==b)+9*int(b==sig[a]) for b in L] for a in L]
 pd=[p[a]-p[sig[a]] for a in L]
 cross=quad(k2,pd,p)
 total=quad(outGram,p,p)-quad(k3,p,p)+4*(quad(inGram,p,p)-quad(crossGram,p,p))+4*cross
 assert total==49*energy
 cert=case['certificate'];prices=cert['price'];alpha=cert['dual_left'];beta=cert['dual_right'];scale=case['scale']
 assert all(isinstance(v,int) for v in prices+alpha+beta)
 assert len(set(alpha[12:]))==1
 bound=sum(prices[:60])+sum(prices[60+12*a+b]*k2[a][b]+prices[204+12*a+b]*k3[a][b] for a in L for b in L)+sum(alpha)+sum(beta)
 assert bound==cert['bound'] and bound>scale*energy
 checked=0
 for k,z in enumerate(Z):
  sz=flip(z);dz=sum(p[a] for a in z)-sum(p[a] for a in sz)
  for e in E:
   if any(k2[a][b]==0 for a in z for b in e):continue
   for f in E:
    if e==f or any(k2[a][b]==0 for a in sz for b in f):continue
    if any(k3[a][b]==0 for a in e for b in f):continue
    common=[a for a in e if a in f]
    if common and k3[common[0]][common[0]]<2:continue
    charge=sum(p[a] for a in e)-sum(p[a] for a in f)+2*dz
    if charge%7:continue
    val=prices[idx[e]]+prices[idx[f]]
    val+=sum(prices[60+12*a+b] for a in z for b in e)+sum(prices[60+12*a+b] for a in sz for b in f)
    val+=sum(prices[204+12*a+b] for a in e for b in f)+sum(prices[204+12*a+b] for a in f for b in e)
    val+=alpha[common[0]] if common else alpha[12]
    val+=beta[k]
    assert scale*(charge//7)**2>=val,(case['index'],k,z,e,f)
    checked+=1
 ans={'index':case['index'],'energy':energy,'bound_scaled':bound,'scale':scale,'columns_checked':checked,'valid':True}
 CHECKS.append(ans);print('A33_INDEPENDENT_CERT',json.dumps(ans),flush=True)

last=PHI[16]
survive={norm(tuple(last[g[i]] for i in L)) for g in G}
lines=set()
for p,q in combinations(sorted(survive),2):
 line=frozenset(norm(tuple((a*p[i]+b*q[i])%7 for i in L)) for a,b in product(range(7),repeat=2) if a or b)
 assert len(line)==8
 lines.add(line)
full=[line for line in lines if line<=survive]
print('A33_SURVIVOR_LINES',json.dumps({'points':len(survive),'projective_lines_through_pairs':len(lines),'lines_contained':len(full),'maximum_intersection':max(len(line&survive) for line in lines)}),flush=True)
phi=[1,1,-2,1,1,-2]*2
weights={sum(phi[a] for a in e)%7 for e in E}
differences={(a-b)%7 for a,b in product(weights,repeat=2)}
z=(2,5);sz=flip(z);need=(-2*(sum(phi[a] for a in z)-sum(phi[a] for a in sz)))%7
assert need not in differences
print('A33_HUMAN9',json.dumps({'edge_weights_mod7':sorted(weights),'differences_mod7':sorted(differences),'required_difference':need,'impossible':True}),flush=True)

```
<!-- END_FILE -->

<a id="source-14"></a>

### outputs/coupures_et_torsion/verifier_coupure_norme10.py

<!-- BEGIN_FILE path="outputs/coupures_et_torsion/verifier_coupure_norme10.py" bytes="4082" sha256="4dcd2b59b5f4639ab50d476df8655cd972de040eb9b1c89abec866e64c768900" -->
```python
import itertools,json

def penalty(t):return (t-1)*(t-2)//2 if t else 0
assert all(t<=2+penalty(t) for t in range(1001))
assert all(1-t+t*(t-1)//2==penalty(t) for t in range(1,1001))
PROFILES=[]
for n3 in range(3):
 counts=[2-n3,20+3*n3,10-3*n3,n3]
 assert sum(counts)==32 and sum(t*counts[t] for t in range(4))==40
 assert sum(t*(t-1)//2*counts[t] for t in range(4))==10
 possible=0;equal=0
 for s,t in itertools.product(range(4),repeat=2):
  left=counts[:];left[s]-=1;left[t]-=1
  if min(left)<0:continue
  possible+=1
  sums=set()
  for c0 in range(min(left[0],10)+1):
   for c2 in range(min(left[2],10-c0)+1):
    for c3 in range(min(left[3],10-c0-c2)+1):
     c1=10-c0-c2-c3
     if c1<=left[1]:sums.add(c1+2*c2+3*c3)
  equal+=int(s+t in sums)
 assert equal==0
 PROFILES.append({'n0_n1_n2_n3':counts,'unused_pair_choices':possible,'balanced_cut_choices':equal})
print('NORM10_CUT_INDEPENDENT',json.dumps(PROFILES),flush=True)
SIX=[]
for n0 in range(4):
 n3=3-n0;n2=11-3*n3;n1=32-n0-n2-n3
 if n0==0:
  assert n2+n3>4
 else:
  SIX.append([n0,n1,n2,n3])
  for c in [2]:
   assert 11-n3-(6-c+n3)>2*n0
print('NORM10_SIX_PROFILES',json.dumps({'profiles':SIX,'small_pair_selected_max':1}),flush=True)
# Control of the general global double-count on H(2,3), with an actual flat odd eigenfunction.
V=list(itertools.product(range(3),repeat=2));N={v:{w for w in V if sum(v[i]==w[i] for i in range(2))==1} for v in V}
P={(0,1),(1,0),(2,2)};Q={tuple((-a)%3 for a in p) for p in P}
f={v:int(v in P)-int(v in Q) for v in V}
assert all(sum(f[w] for w in N[v])==-2*f[v] for v in V)
assert all(not N[v]&P for v in P) and all(not N[v]&Q for v in Q)
ts=[len(N[v]&P) for v in V if not f[v]]
assert all(len(N[v]&P)==len(N[v]&Q) for v in V if not f[v])
assert sum(ts)==(4-2)*3 and sum(t*(t-1)//2 for t in ts)==3*(3-1)-3*1
print('H23_GLOBAL_CONTROL',json.dumps({'outside_t':ts,'sum':sum(ts),'pair_sum':sum(t*(t-1)//2 for t in ts),'root_only_hypothesis':False}),flush=True)

import json
from itertools import product,combinations
D5=[(1,0,0,0,0),(2,0,0,0,0),(0,1,0,0,0),(0,2,0,0,0),(0,0,1,0,0),(0,0,2,0,0),(0,0,0,1,0),(0,0,0,2,0),(0,0,0,0,1),(0,0,0,0,2),(1,0,2,1,2),(2,0,1,2,1),(2,1,1,1,2),(1,2,2,2,1),(2,2,2,0,2),(1,1,1,0,1),(2,2,0,1,1),(1,1,0,2,2),(1,2,1,1,0),(2,1,2,2,0),(0,1,2,1,1),(0,2,1,2,2)]
for dimension,directions in [(2,[(1,0),(2,0),(0,1),(0,2)]),(5,D5)]:
    V=list(product(range(3),repeat=dimension));DD=set(directions)
    add=lambda a,b:tuple((x+y)%3 for x,y in zip(a,b))
    neg=lambda a:tuple((-x)%3 for x in a)
    adj=lambda a,b:add(a,neg(b)) in DD
    zero=(0,)*dimension;c=directions[0];nc=neg(c)
    labels=[a for a in directions if a not in (c,nc)];n=len(labels)
    sigma=[labels.index(neg(a)) for a in labels]
    U=[add(c,a) for a in labels]
    mu=[];tau=[]
    for b in range(n):
        mm=[d for d in range(n) if adj(U[b],U[d])]
        tt=[d for d in range(n) if adj(U[b],neg(U[d]))]
        assert len(mm)==len(tt)==1
        mu.append(mm[0]);tau.append(tt[0])
    far=[a for a in V if a not in (zero,c,nc) and all(not adj(a,t) for t in (zero,c,nc))]
    F={add(labels[a],labels[b]):(a,b) for a,b in combinations(range(n),2) if b!=sigma[a]}
    assert set(F)==set(far) and len(F)==n*(n-2)//2
    Phi={z:tuple(b for b in range(n) if adj(z,U[b])) for z in far}
    assert all(len(e)==2 for e in Phi.values())
    target={e for e in combinations(range(n),2) if e[1]!=mu[e[0]]}
    assert len(set(Phi.values()))==len(Phi) and set(Phi.values())==target
    for a in range(n):
        for b in range(n):
            v=sum(a in F[z] and b in Phi[z] for z in far)
            rhs=2-(a==b)-(b==sigma[a])-(b==mu[a])-(b==tau[sigma[a]])
            assert v==rhs
    for b in range(n):
        for d in range(n):
            v=sum(b in Phi[z] and d in Phi[neg(z)] for z in far)
            rhs=2-(d==sigma[b])-(d==tau[mu[b]])-(d==mu[tau[b]])-(d==tau[b])
            assert v==rhs
    print('COMPACT_CONTROL',json.dumps({'m':len(directions)//2,'vertices':len(V),'labels':n,'far':len(far),'bijection':True,'K2':True,'K3':True,'free':all(mu[i]!=tau[i] for i in range(n))}),flush=True)

```
<!-- END_FILE -->

<a id="source-15"></a>

### outputs/fermeture_A33/ETAT_REPRISE.md

<!-- BEGIN_FILE path="outputs/fermeture_A33/ETAT_REPRISE.md" bytes="1942" sha256="6b3a00d4ef9f00c718b766ef87fcb92eb6c93c6b6afe38b41ae5ed28c19151ca" -->
```markdown
# Reprise — A33 entièrement fermée

26 septembre 2026. Lire PREUVE.md et sorties_independantes.txt.

**Démontré et vérifié indépendamment :** A111111 (3,3) ne se réalise sous aucune involution d’un srg(99,14,1,2). P=0 n’est pas utilisé. La dernière classe de douze torsions est fermée par un conflit de Witt.

Chaîne exacte :
- bloc impair de 19 coordonnées : rang mod7=14, discriminant réduit carré (1) ; partie non scindée ;
- image du bloc de dimension18−r₀, radical de dimension4−r₀ ;
- espace global hyperbolique ⇒ g⁻≥24−2r₀ ;
- quinze certificats et un cas humain conservés dans ../coupures_et_torsion/ donnent r₀≤1 ;
- g⁻≥22, contre le genre g⁻≤20.

Deux calculs du signe : Sage et Python standard symétrique/Bareiss, résultats identiques. Contrôles H(2,3) et BvLS avec décomposition relative et discriminants revérifiés.

La conclusion ancienne « A33 à g⁻20 ouverte » est dépassée. Les anciennes recherches d’énergie restent des étapes historiques. Ne pas relancer A33.

**Suite utile :** appliquer le défaut de Witt aux autres blocs dégénérés dont le rang est pair, puis chercher si leur signe impose une dimension équilibrée plus grande que celle autorisée par les ombres. Pour un bloc non scindé de rang r=18−t, cela impose g⁻≥18+t−2r₀+2. Vérifier chaque type avant toute exclusion. Les blocs de rang impair demandent un autre raccord de signe.

Priorités conservées : autres étoiles sans classe fermée, carrés disjoints ; normes9/six blocs (1406 noyaux partiels nécessaires non prolongés) ; normes10/six blocs (trois profils, couplage petit–petit≤1) et sept blocs. Norme10/cinq blocs déjà exclue. Aucune fermeture générale de l’involution ni du cas sans symétrie.

Automation active : aucune cible globale atteinte. Aucun SAT/CP/PLNE, aucun calcul Python sur le PC, aucun dépôt consulté ou modifié dans cette reprise.

```
<!-- END_FILE -->

<a id="source-16"></a>

### outputs/fermeture_A33/PREUVE.md

<!-- BEGIN_FILE path="outputs/fermeture_A33/PREUVE.md" bytes="9474" sha256="0fb7e92932462c59e7d9397464c0e6921c39aab935b258499f93ae72c2b157fe" -->
```markdown
# Fermeture de l’étoile A111111 (3,3)

26 septembre 2026. **Démontré**, avec deux calculs exacts indépendants du signe et contrôles sur H(2,3) et BvLS.

**Théorème.** Une involution d’un srg(99,14,1,2) ne peut avoir une droite-bloc de type A111111 (3,3). L’hypothèse P=0 n’est pas nécessaire.

Cette preuve ferme la dernière classe laissée ouverte dans ../coupures_et_torsion/PREUVE_A33.md. Elle ne ferme pas toutes les étoiles sans classe fermée et ne prouve pas l’impossibilité générale d’une involution.

## 1. Le raccord qui manquait

Le calcul précédent avait établi que l’espace V₀ des torsions équilibrées de cette étoile a dimension r₀≤1. La formule de rang de C1 imposait alors g⁻=20 et ρ=0, sans contradiction de rang.

Le nouveau raccord est un **conflit de type de forme quadratique**. Le bloc connu, de rang 14 modulo 7, est non scindé. Il ne peut se compléter en une forme hyperbolique de rang 20 en ajoutant seulement trois plans hyperboliques. Il lui faut un résidu non scindé de dimension au moins deux.

On obtient le renforcement

    g⁻ ≥ 24 − 2r₀,

au lieu du seul minorant 22−2r₀. Avec r₀≤1, cela donne g⁻≥22, contraire à g⁻≤20.

## 2. Cadre global et signe

Sur les 49 coordonnées impaires, S est entière symétrique et S²+S=12I. Poser H=3I−S modulo 7 et g=g⁻=rang H. La forme

    G = F₇⁴⁹ / ker H,   ⟨[u],[v]⟩ = uᵀHv

est non dégénérée de dimension g. C’est l’opposée de β⁻ du complément au dossier n°6. Multiplier une forme hyperbolique par −1 conserve son caractère hyperbolique.

Les résultats de genre du dossier n°6 donnent g pair, g≤20 et **G hyperbolique**. Voici le raccord de signe, pour préciser ce qui est utilisé.

Avec les représentants canoniques, soit M le nombre d’arêtes négatives dans le bloc racines×racines de S. Alors 1ᵀS1=497−4M. Les sept sommes de lignes des blocs valent 11,9,7,5,3,1,−1 : leurs carrés somment à 7 modulo 8. Les sommes de lignes des 42 racines sont paires et somment à 462−4M ; leurs carrés somment donc à 4 modulo 8. De S²+S=12I, on tire

    3 + (497−4M) ≡ 12·49 ≡ 4 (mod 8),

ce qui impose M pair.

La formule d’oddité déjà certifiée dans le dossier n°6 s’écrit

    22 + 6g + 4δ ≡ 6 + 4M (mod 8).

Elle impose g pair puis δ≡g/2 modulo 2. Par le raccord du réseau propre avec la forme β⁻, le caractère du discriminant de β⁻ est (−1)^(g/2), celui d’une forme hyperbolique en dimension g sur F₇. À g=22, la partie unimodulaire de Λ₋₄⁻ serait vide, et son déterminant 7²² forcerait le signe +1, contrairement à δ≡11. Comme g≤22 par le rang rationnel, g≤20.

Les faits de réseau et l’oddité sont les acquis de C1/structures fournis dans les dossiers ; leur application au bloc dégénéré ci-dessous est le nouveau pas.

## 3. Le bloc A33 est non scindé

Les douze étiquettes sont 0,…,11. Écrire

    σ(i)=i xor 1,
    τ=(0 5)(1 2)(3 4)(6 11)(7 8)(9 10).

L’appariement interne est μ=σ. Les six paires σ sont les autres blocs, et σ/τ forme deux cycles C₆.

Prendre les sept coordonnées des blocs et les douze orbites contenant le bloc c, représentées par (c,+)(a). Soit C la matrice 7×12 dont la ligne c vaut 1 partout, et les six autres lignes valent +1 puis −1 sur leur paire σ. Alors

    CᵀC = J + I − Pσ,

et le Gram connu H_I, sur 19 coordonnées, est

    H_I = [[4I₇, −C], [−Cᵀ, 3I₁₂−Pσ+Pτ]].

Le complément de Schur sur 4I₇ est, modulo 7,

    Q = I + Pσ + Pτ − 2J.

Sur chaque C₆, I+Pσ+Pτ a un noyau de dimension deux. L’ajout −2J tue la direction constante commune aux deux composantes ; la différence des deux constantes demeure non nulle. Donc rang Q=7, puis rang H_I=14.

Pour J₀={0,1,2,3,6,7,8}, le mineur principal de la matrice entière I+Pσ+Pτ−2J a déterminant **−5**, soit 2 modulo 7. Ainsi

    det_red H_I ≡ 4⁷·2 ≡ 1 (mod 7),

à un carré près. En dimension 14, une forme hyperbolique a discriminant de caractère χ((−1)⁷)=−1. Le discriminant de H_I étant carré, **sa partie non dégénérée est non scindée**.

Contrôle distinct : le mineur principal entier de H_I sur les sept blocs et les étiquettes J₀ vaut 3 508 800, soit 1 modulo 7. Les deux valeurs entières sont différentes parce que le Schur entier n’est pas Q ; leur comparaison n’est faite que modulo 7.

## 4. Dimension de l’image du bloc

Le noyau local de H_I a dimension cinq. Il est formé du vecteur propre universel z_c, de valeur 3 au bloc c et 1 sur les douze orbites, et des quatre torsions

    φ=(a,b,−a−b,a,b,−a−b ; d,e,−d−e,d,e,−d−e).

Pour une torsion, les coordonnées aux blocs sont 2Cφ modulo 7 et celles de l’étoile sont φ. Le vérificateur reconstruit aussi cinq vecteurs de noyau local, contrôle leur indépendance et vérifie 120 identités de couplage extérieur sur les quatre torsions et les trente orbites. La ligne extérieure d’une orbite z est nulle exactement si

    φ(Φ(z)) − φ(Φ(σz)) + 2[φ(z)−φ(σz)] = 0 (mod 7).

C’est la définition de V₀. Le vecteur universel est dans le noyau global indépendamment de Φ. Par conséquent, l’intersection du noyau global avec les vecteurs portés par I a dimension exactement 1+r₀.

L’image U des 19 coordonnées dans G a donc

    dim U = 18−r₀,
    rang de la forme sur U = 14,
    dim rad U = 4−r₀.

Cela donne le raccord de dimensions directement ; il n’est pas nécessaire de supposer séparément la formule avec ρ.

## 5. Lemme de Witt pour un bloc dégénéré

**Lemme.** Soit G une forme hyperbolique non dégénérée sur un corps fini de caractéristique impaire. Soit U⊆G, avec radical de dimension h, dont la partie non dégénérée a dimension paire r et est non scindée. Alors

    dim G ≥ r + 2h + 2.

**Preuve.** Poser R=rad U. R est totalement isotrope et U⊆R^⊥. Le quotient R^⊥/R est hyperbolique de dimension dim G−2h. U/R y est non dégénéré et non scindé. Son complément orthogonal doit lui aussi être non scindé, puisque leur somme est hyperbolique. Un complément non scindé de dimension paire ne peut avoir dimension zéro ; sa dimension est au moins deux. D’où la borne. ∎

C’est une application du découpage de Witt classique, et non un nouveau théorème général de classification des réseaux. L’avancement est le calcul du défaut de Witt du bloc A33 et son couplage avec la torsion équilibrée.

Appliquer le lemme avec r=14 et h=4−r₀ donne

    g ≥ 14 + 2(4−r₀) + 2 = 24−2r₀.

## 6. Les certificats antérieurs donnent r₀≤1

La couverture des 400 directions de P³(F₇), par le groupe de taille 72, a été vérifiée indépendamment dans ../coupures_et_torsion/verifier_A33_independant.py. Quinze certificats entiers et un domaine impossible excluent seize des dix-sept classes. Les douze directions de la dernière classe sont représentées par

    (1,2,4,1,2,4 ; 3,5,6,3,5,6).

Elles n’ont aucune coordonnée nulle. Ainsi tout φ∈V₀ non nul a φ(0)≠0. L’évaluation φ↦φ(0) est une application linéaire injective V₀→F₇. Donc r₀≤1.

Les coefficients complets, les inégalités vérifiées pour chaque choix d’ombres et les sorties sont conservés dans ../coupures_et_torsion/. Leur statut n’est pas changé par cette preuve.

Le nouveau lemme donne alors g≥22, alors que le genre impose g≤20. **Contradiction. Toute la strate A33 est fermée.**

Dans la formulation précédente g=22−2r₀+ρ, le même pas exige ρ≥2 : le cas r₀=1,ρ=0,g=20 est précisément celui qui manquait.

## 7. Vérifications, portée et limites

Deux implémentations du signe ont été exécutées à distance :

- Sage : rang et choix d’un mineur principal de rang maximal ; rang 14, déterminant 1 modulo 7.
- Python standard écrit séparément : élimination symétrique par congruence, pivots de taille un ou deux, et Bareiss entier. Rang 14, discriminant 1 ; mineurs −5 et 3 508 800.

Le second programme vérifie aussi, sur les vrais graphes H(2,3) et BvLS, la décomposition relative de Witt, ses rangs et ses discriminants :

| Contrôle | Premier | Rang du bloc | Rang total | Rang de couplage du radical | Rang du résidu |
|---|---:|---:|---:|---:|---:|
| H(2,3), 9 sommets | 3 | 2 | 2 | 0 | 0 |
| BvLS, 243 sommets | 3 | 20 | 35 | 4 | 7 |

Dans les deux cas, la relation χ(disc total)=χ(disc bloc)·χ(−1)^h·χ(disc résidu) est contrôlée directement. Les contraintes de genre propres à 99/modulo 7 ne sont pas transplantées à ces autres paramètres. Ces contrôles testent le raccord algébrique, pas un témoin A33.

Les explorations préliminaires des congruences seules et des ombres filtrées λ/μ+Schur n’ont pas donné de contradiction ; elles ne constituent pas la preuve de fermeture.

**Restent ouverts :** les autres étoiles sans classe fermée, dont les étoiles totalement libres à t=0, les familles avec carrés disjoints, l’involution générale et le cas sans symétrie. Les normes 9 et 10 sur six ou sept blocs ne sont pas fermées par ce théorème. Aucune cible globale de l’automation n’étant résolue, elle reste active.

Programmes : verifier_signe_et_controles.py, verifier_signe_sage.py. Sorties : sorties_independantes.txt, sorties_sage.txt. Aucun solveur externe, aucune exécution Python locale, aucun dépôt distant modifié.

```
<!-- END_FILE -->

<a id="source-17"></a>

### outputs/fermeture_A33/RAPPORT.md

<!-- BEGIN_FILE path="outputs/fermeture_A33/RAPPORT.md" bytes="1208" sha256="7647997418da354ff2ad19f797f98800bf218dbf9902358b9595e5bc7fb38593" -->
```markdown
# A111111 (3,3) entièrement exclue

**Résultat démontré, vérifié par deux implémentations.** Une involution de srg(99,14,1,2) ne peut avoir cette étoile. P=0 n’est pas utilisé.

Le bloc connu a rang14 modulo7 et discriminant carré, donc une partie non scindée. Sa complétion dans l’espace global hyperbolique impose g⁻≥24−2r₀. Nos certificats antérieurs donnent r₀≤1 ; le genre donne g⁻≤20. Contradiction.

Le cas qui restait ouvert, r₀=1,ρ=0,g⁻=20, est donc fermé. C’est le signe du résidu qui manquait au seul calcul de rang.

[Preuve complète](PREUVE.md) · [Vérificateur indépendant et contrôles](verifier_signe_et_controles.py) · [Second calcul du signe](verifier_signe_sage.py) · [Sorties exactes](sorties_independantes.txt).

Contrôles H(2,3) et BvLS : décomposition de Witt, rangs et discriminants reproduits ; aucune fausse exclusion. La vérification de la bijection entre les quatre torsions locales et les conditions d’ombres est incluse.

Les autres étoiles sans classe fermée, les carrés disjoints et l’involution générale restent ouverts. Normes9/10 sur six et sept blocs : aucune nouvelle fermeture ici. L’automation reste active.

```
<!-- END_FILE -->

<a id="source-18"></a>

### outputs/fermeture_A33/SHA256SUMS.txt

<!-- BEGIN_FILE path="outputs/fermeture_A33/SHA256SUMS.txt" bytes="693" sha256="1036e4c12325fbe7da5e3af785f823b06c53a11f4bfa05f76637e8bc71ae9db8" -->
```text
6b3a00d4ef9f00c718b766ef87fcb92eb6c93c6b6afe38b41ae5ed28c19151ca  ETAT_REPRISE.md
0fb7e92932462c59e7d9397464c0e6921c39aab935b258499f93ae72c2b157fe  PREUVE.md
7647997418da354ff2ad19f797f98800bf218dbf9902358b9595e5bc7fb38593  RAPPORT.md
d862ae8303009c46198696353489fbfb3fa0d6103aa9792ad2409f81a4b76791  explorations_preliminaires.txt
5e9f389f63cc8d32735ce7699c1ec193069406121bc10bd2e1489984040e0994  sorties_independantes.txt
7e22cab521559a8df8da7e0bcad58572af5f462e2a3cef4a0020cd2654614854  sorties_sage.txt
ace66dcf030e93953f2cdc439f0554dcab8f6ba30f8cb4effb98c725fe9a99c0  verifier_signe_et_controles.py
5e91098ee780ecd0a3fcd93df5dd064144518971025f9cee8264d0f14afa59bb  verifier_signe_sage.py

```
<!-- END_FILE -->

<a id="source-19"></a>

### outputs/fermeture_A33/explorations_preliminaires.txt

<!-- BEGIN_FILE path="outputs/fermeture_A33/explorations_preliminaires.txt" bytes="443" sha256="d862ae8303009c46198696353489fbfb3fa0d6103aa9792ad2409f81a4b76791" -->
```text
Le filtre λ/μ et Schur laisse 5301 colonnes équilibrées ; aucune exclusion par sa recherche bornée de 800 itérations. Borne 83.599 pour énergie 84.
Seul p=2 a terminé avant la fermeture de l’onglet : rang et rang augmenté 264. Aucun verdict sauvegardé pour p=3 ou p=7.
MODULAR_SETUP {"columns": 7119, "equations": 391}
MODULAR_RESULT {"p": 2, "rank": 264, "augmented_rank": 264, "inconsistent": false, "seconds": 2.7141273021698}


```
<!-- END_FILE -->

<a id="source-20"></a>

### outputs/fermeture_A33/sorties_independantes.txt

<!-- BEGIN_FILE path="outputs/fermeture_A33/sorties_independantes.txt" bytes="1177" sha256="5e9f389f63cc8d32735ce7699c1ec193069406121bc10bd2e1489984040e0994" -->
```text
A33_SIGN_INDEPENDENT {"rank": 14, "reduced_discriminant": 1, "pivots": [[4], [4], [4], [4], [4], [4], [4], [6], [3], [2], [3], [4], [0, 1, 0]], "minor_H_integer": 3508800, "minor_Q_integer": -5, "minor_H_mod7": 1, "minor_Q_mod7": 2}
A33_WITT_CONFLICT {"ball_rank": 14, "cross_radical_rank": 3, "residual_rank": 0, "full_rank": 20, "predicted_full_discriminant_character": -1, "required_hyperbolic_character": 1, "contradiction": true}
WITT_POSITIVE_CONTROL {"residual_disc": 1, "witt_relation_verified": true, "m": 2, "vertices": 9, "odd_coordinates": 4, "p": 3, "ball_rank": 2, "full_rank": 2, "image_ball_dimension": 2, "cross_rank": 0, "residual_rank": 0, "disc_ball": 1, "disc_full": 1, "no_false_exclusion": true}
WITT_POSITIVE_CONTROL {"residual_disc": 2, "witt_relation_verified": true, "m": 11, "vertices": 243, "odd_coordinates": 121, "p": 3, "ball_rank": 20, "full_rank": 35, "image_ball_dimension": 24, "cross_rank": 4, "residual_rank": 7, "disc_ball": 1, "disc_full": 2, "no_false_exclusion": true}

A33_KERNEL_BRIDGE {"local_kernel_dimension": 5, "universal_kernel": true, "torsion_basis": 4, "boundary_checks": 120, "balanced_dimension_formula": "dim U = 18-r0"}

```
<!-- END_FILE -->

<a id="source-21"></a>

### outputs/fermeture_A33/sorties_sage.txt

<!-- BEGIN_FILE path="outputs/fermeture_A33/sorties_sage.txt" bytes="153" sha256="7e22cab521559a8df8da7e0bcad58572af5f462e2a3cef4a0020cd2654614854" -->
```text
A33_BALL_SIGN {"rank": 14, "pivots": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15], "det": 1, "square": true, "required_for_hyperbolic_rank20": false}


```
<!-- END_FILE -->

<a id="source-22"></a>

### outputs/fermeture_A33/verifier_signe_et_controles.py

<!-- BEGIN_FILE path="outputs/fermeture_A33/verifier_signe_et_controles.py" bytes="7091" sha256="ace66dcf030e93953f2cdc439f0554dcab8f6ba30f8cb4effb98c725fe9a99c0" -->
```python
import json,itertools,time

def rank_mod(A,p):
 A=[[int(x)%p for x in row] for row in A];r=0
 if not A:return 0
 for c in range(len(A[0])):
  piv=next((i for i in range(r,len(A)) if A[i][c]),None)
  if piv is None:continue
  A[r],A[piv]=A[piv],A[r];iv=pow(A[r][c],-1,p);A[r]=[(x*iv)%p for x in A[r]]
  for i in range(r+1,len(A)):
   if A[i][c]:
    q=A[i][c];A[i]=[(a-q*b)%p for a,b in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r

def sym_disc(A,p):
 A=[[int(x)%p for x in row] for row in A];r=0;disc=1;pivots=[]
 while A:
  n=len(A);i=next((i for i in range(n) if A[i][i]),None)
  if i is not None:
   order=[i]+[j for j in range(n) if j!=i];B=[[A[a][b] for b in order] for a in order];v=B[0][0];iv=pow(v,-1,p)
   disc=disc*v%p;r+=1;pivots.append([v]);A=[[(B[a][b]-B[a][0]*B[0][b]*iv)%p for b in range(1,n)] for a in range(1,n)]
  else:
   pair=next(((a,b) for a in range(n) for b in range(a+1,n) if A[a][b]),None)
   if pair is None:break
   a,b=pair;order=[a,b]+[j for j in range(n) if j not in pair];B=[[A[x][y] for y in order] for x in order];v=B[0][1];iv=pow(v,-1,p)
   disc=disc*(-v*v)%p;r+=2;pivots.append([0,v,0]);A=[[(B[x][y]-(B[x][0]*B[1][y]+B[x][1]*B[0][y])*iv)%p for y in range(2,n)] for x in range(2,n)]
 return r,disc,pivots

def bareiss(A):
 A=[row[:] for row in A];sign=1;prev=1;n=len(A)
 for k in range(n-1):
  if A[k][k]==0:
   i=next((i for i in range(k+1,n) if A[i][k]),None)
   if i is None:return 0
   A[k],A[i]=A[i],A[k];sign=-sign
  v=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=A[i][j]*v-A[i][k]*A[k][j];assert num%prev==0;A[i][j]=num//prev
  for i in range(k+1,n):A[i][k]=0
  prev=v
 return sign*A[-1][-1]

sig=[i^1 for i in range(12)];tau=[5,2,1,4,3,0,11,8,7,10,9,6]
C=[[1 if c==0 else 1 if a==2*(c-1) else -1 if a==2*(c-1)+1 else 0 for a in range(12)] for c in range(7)]
H=[[0]*19 for _ in range(19)]
for c in range(7):
 H[c][c]=4
 for a in range(12):H[c][7+a]=H[7+a][c]=-C[c][a]
for a in range(12):
 for b in range(12):H[7+a][7+b]=3*int(a==b)-int(b==sig[a])+int(b==tau[a])
r,disc,piv=sym_disc(H,7);assert r==14 and disc in (1,2,4)
J=[0,1,2,3,6,7,8];Q=[[int(a==b)+int(b==sig[a])+int(b==tau[a])-2 for b in J] for a in J];qd=bareiss(Q)
I=list(range(7))+[7+a for a in J];hd=bareiss([[H[a][b] for b in I] for a in I])
assert hd%7==1 and qd%7==2 and hd%7==(4**7*qd)%7
print('A33_SIGN_INDEPENDENT',json.dumps({'rank':r,'reduced_discriminant':disc,'pivots':piv,'minor_H_integer':hd,'minor_Q_integer':qd,'minor_H_mod7':hd%7,'minor_Q_mod7':qd%7}),flush=True)
assert (disc*(-1)**3)%7 not in (1,2,4)
print('A33_WITT_CONFLICT',json.dumps({'ball_rank':14,'cross_radical_rank':3,'residual_rank':0,'full_rank':20,'predicted_full_discriminant_character':-1,'required_hyperbolic_character':1,'contradiction':True}),flush=True)

def relative_witt(A,k,p):
 A=[[int(x)%p for x in row] for row in A];r=0;db=1;h=0
 def take(A,pair):
  n=len(A);order=list(pair)+[i for i in range(n) if i not in pair]
  return [[A[i][j] for j in order] for i in order]
 while True:
  i=next((i for i in range(k) if A[i][i]),None)
  if i is not None:
   B=take(A,(i,));v=B[0][0];iv=pow(v,-1,p);db=db*v%p;r+=1;k-=1
   A=[[(B[i][j]-B[i][0]*B[0][j]*iv)%p for j in range(1,len(B))] for i in range(1,len(B))];continue
  pair=next(((i,j) for i in range(k) for j in range(i+1,k) if A[i][j]),None)
  if pair is None:break
  B=take(A,pair);v=B[0][1];iv=pow(v,-1,p);db=db*(-v*v)%p;r+=2;k-=2
  A=[[(B[i][j]-(B[i][0]*B[1][j]+B[i][1]*B[0][j])*iv)%p for j in range(2,len(B))] for i in range(2,len(B))]
 while True:
  pair=next(((i,j) for i in range(k) for j in range(k,len(A)) if A[i][j]),None)
  if pair is None:break
  B=take(A,pair);v=B[0][1];d=B[1][1];iv=pow(v,-1,p);ivv=iv*iv%p;h+=1;k-=1
  A=[[(B[i][j]+d*ivv*B[i][0]*B[0][j]-iv*(B[i][0]*B[1][j]+B[i][1]*B[0][j]))%p for j in range(2,len(B))] for i in range(2,len(B))]
 assert all(A[i][j]==0 for i in range(k) for j in range(len(A)))
 F=[row[k:] for row in A[k:]];rf,df,_=sym_disc(F,p)
 return r,db,h,rf,df

D5=[(1,0,0,0,0),(2,0,0,0,0),(0,1,0,0,0),(0,2,0,0,0),(0,0,1,0,0),(0,0,2,0,0),(0,0,0,1,0),(0,0,0,2,0),(0,0,0,0,1),(0,0,0,0,2),(1,0,2,1,2),(2,0,1,2,1),(2,1,1,1,2),(1,2,2,2,1),(2,2,2,0,2),(1,1,1,0,1),(2,2,0,1,1),(1,1,0,2,2),(1,2,1,1,0),(2,1,2,2,0),(0,1,2,1,1),(0,2,1,2,2)]
for dimension,D,theta in [(2,[(1,0),(2,0),(0,1),(0,2)],1),(5,D5,4)]:
 DD=set(D);neg=lambda a:tuple((-x)%3 for x in a);add=lambda a,b:tuple((x+y)%3 for x,y in zip(a,b));adj=lambda a,b:add(a,neg(b)) in DD
 V=list(itertools.product(range(3),repeat=dimension));zero=(0,)*dimension;c=D[0];nc=neg(c);labels=[a for a in D if a not in (c,nc)];star=[add(c,a) for a in labels]
 blocks=[]
 for a in D:
  if a not in blocks and neg(a) not in blocks:blocks.append(a)
 reps=blocks+star
 assert len(set(reps))==len(reps) and not any(neg(a) in reps for a in reps)
 seen=set(reps)|{neg(a) for a in reps}|{zero}
 for a in V:
  if a not in seen:reps.append(a);seen.update((a,neg(a)))
 S=[[int(adj(a,b))-int(adj(a,neg(b))) for b in reps] for a in reps]
 N=[[S[i][j]-theta*int(i==j) for j in range(len(reps))] for i in range(len(reps))]
 p=3;count=len(blocks)+len(star);idx=list(range(count));A=[[N[i][j] for j in idx] for i in idx]
 g,dg,_=sym_disc(N,p);r,db,_=sym_disc(A,p);d=rank_mod([[row[j] for j in idx] for row in N],p);h=d-r;rho=g-r-2*h
 assert rho>=0 and g==rank_mod(N,p) and r==rank_mod(A,p)
 if rho==0:assert pow(dg*pow(db,-1,p)*pow(-1,h,p)%p,(p-1)//2,p)==1
 rr,ddb,hh,rf,df=relative_witt(N,count,p)
 assert (rr,hh,rf)==(r,h,rho)
 assert pow(dg*pow((ddb*pow(-1,h,p)*df)%p,-1,p)%p,(p-1)//2,p)==1
 ans={'residual_disc':df,'witt_relation_verified':True,'m':len(D)//2,'vertices':len(V),'odd_coordinates':len(reps),'p':p,'ball_rank':r,'full_rank':g,'image_ball_dimension':d,'cross_rank':h,'residual_rank':rho,'disc_ball':db,'disc_full':dg,'no_false_exclusion':True}
 print('WITT_POSITIVE_CONTROL',json.dumps(ans),flush=True)

PHI_BASIS=[[1,0,-1,1,0,-1]+[0]*6,[0,1,-1,0,1,-1]+[0]*6,[0]*6+[1,0,-1,1,0,-1],[0]*6+[0,1,-1,0,1,-1]]
UNIVERSAL=[3]+[0]*6+[1]*12
KERNEL=[UNIVERSAL]
for phi in PHI_BASIS:
 u=[2*sum(C[c][a]*phi[a] for a in range(12)) for c in range(7)]
 f=u+phi;KERNEL.append(f)
 assert all(sum(H[i][j]*f[j] for j in range(19))%7==0 for i in range(19))
assert all(sum(H[i][j]*UNIVERSAL[j] for j in range(19))==0 for i in range(19))
assert rank_mod(KERNEL,7)==5
E=[e for e in itertools.combinations(range(12),2) if sig[e[0]]!=e[1]]
flip=lambda e:tuple(sorted(sig[a] for a in e));Z=[e for e in E if e<flip(e)]
checks=0
for k,z in enumerate(Z):
 sz=flip(z);ds=[0]*7
 for a in z:ds[1+a//2]+=1 if a%2==0 else -1
 e=E[(7*k)%60];f=E[(13*k+5)%60]
 row=[-d for d in ds]+[-int(a in e)+int(a in f) for a in range(12)]
 assert sum(a*b for a,b in zip(row,UNIVERSAL))==0
 for phi,ker in zip(PHI_BASIS,KERNEL[1:]):
  lhs=sum(a*b for a,b in zip(row,ker))
  rhs=-(sum(phi[a] for a in e)-sum(phi[a] for a in f)+2*(sum(phi[a] for a in z)-sum(phi[a] for a in sz)))
  assert lhs==rhs;checks+=1
print('A33_KERNEL_BRIDGE',json.dumps({'local_kernel_dimension':5,'universal_kernel':True,'torsion_basis':4,'boundary_checks':checks,'balanced_dimension_formula':'dim U = 18-r0'}),flush=True)

```
<!-- END_FILE -->

<a id="source-23"></a>

### outputs/fermeture_A33/verifier_signe_sage.py

<!-- BEGIN_FILE path="outputs/fermeture_A33/verifier_signe_sage.py" bytes="644" sha256="5e91098ee780ecd0a3fcd93df5dd064144518971025f9cee8264d0f14afa59bb" -->
```python
import json
from sage.all import matrix,GF
sig=[a^1 for a in range(12)];tau=[5,2,1,4,3,0,11,8,7,10,9,6]
C=matrix(GF(7),7,12,lambda c,a:1 if c==0 else (1 if a==2*(c-1) else -1 if a==2*(c-1)+1 else 0))
P=matrix(GF(7),19,19,lambda a,b:0)
for c in range(7):P[c,c]=4
for c in range(7):
 for a in range(12):P[c,7+a]=-C[c,a];P[7+a,c]=-C[c,a]
for a in range(12):
 for b in range(12):P[7+a,7+b]=3*int(a==b)-int(b==sig[a])+int(b==tau[a])
I=list(P.pivots());r=P.rank();D=int(P.matrix_from_rows_and_columns(I,I).det())
print('A33_BALL_SIGN',json.dumps({'rank':r,'pivots':I,'det':D,'square':D in (1,2,4),'required_for_hyperbolic_rank20':False}),flush=True)

```
<!-- END_FILE -->

<a id="reproduction"></a>

## Extraire les fichiers et reproduire les vérifications

Les preuves et les sorties sont déjà intégralement lisibles ci-dessus. L’extraction et les commandes suivantes sont facultatives ; elles sont fournies pour une reproduction sur une machine disponible. Aucun de ces programmes n’a été relancé lors de l’assemblage de ce fichier.

Copier le programme ci-dessous dans `extraire_campagnes.py` à côté de ce Markdown. Il lit les blocs archivés, vérifie **les 23 tailles et les 23 empreintes SHA-256 avant toute écriture**, puis reconstitue les deux dossiers dans le répertoire choisi. Il exige Python 3.9 ou ultérieur et uniquement la bibliothèque standard.

```python
#!/usr/bin/env python3
"""Reconstitue les 23 fichiers de ce dossier et verifie leurs SHA-256."""
import hashlib
from pathlib import Path, PurePosixPath
import re
import sys

if len(sys.argv) != 3:
    raise SystemExit("Usage: python extraire_campagnes.py DOSSIER.md DESTINATION")
source = Path(sys.argv[1])
destination = Path(sys.argv[2]).resolve()
document = source.read_bytes().decode("utf-8")
pattern = re.compile(
    r'<!-- BEGIN_FILE path="([^"]+)" bytes="(\d+)" sha256="([0-9a-f]{64})" -->\n'
    + r'(' + chr(96) + r'{3,})[^\n]*\n(.*?)\n\4\n<!-- END_FILE -->',
    re.S,
)
records = list(pattern.finditer(document))
if len(records) != 23:
    raise SystemExit("Archive incomplete: %s fichiers, 23 attendus" % len(records))
seen = set()
verified = []
for match in records:
    name, expected_size, expected_hash, fence, contents = match.groups()
    relative = PurePosixPath(name)
    if (relative.is_absolute() or ".." in relative.parts
        or not relative.parts or relative.parts[0] != "outputs"
        or name in seen or "\\" in name):
        raise SystemExit("Chemin invalide ou duplique: " + name)
    seen.add(name)
    payload = contents.encode("utf-8")
    if len(payload) != int(expected_size):
        raise SystemExit("Taille incorrecte: " + name)
    if hashlib.sha256(payload).hexdigest() != expected_hash:
        raise SystemExit("SHA-256 incorrect: " + name)
    target = destination.joinpath(*relative.parts).resolve()
    if not target.is_relative_to(destination):
        raise SystemExit("Chemin hors destination: " + name)
    verified.append((target, payload, name))
for target, payload, name in verified:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)
    print("OK", name)
print("23 fichiers reconstitues, tailles et SHA-256 verifies.")
```

```text
python extraire_campagnes.py CAMPAGNES_A33_NORME10_COMPLETES.md dossier_extrait
```

Pour vérifier les certificats A33 et la coupure de norme 10, se placer dans `dossier_extrait/outputs/coupures_et_torsion`, puis lancer :

```text
python verifier_A33_independant.py
python verifier_coupure_norme10.py
```

Pour le signe de Witt et les contrôles positifs, se placer dans `dossier_extrait/outputs/fermeture_A33`, puis lancer :

```text
python verifier_signe_et_controles.py
```

Ces trois vérificateurs utilisent uniquement la bibliothèque standard Python. Le contrôle indépendant `verifier_signe_sage.py` se lance dans SageMath ; ses sorties exactes figurent dans l’archive. Le programme de découverte `chercher_certificat_A33.py` utilise NumPy : il est conservé pour documenter la recherche, mais la validité des quinze certificats se contrôle avec le vérificateur indépendant sans NumPy. L’exploration F7 équivariante et la tentative de classe 16 sont des essais documentés, **pas des preuves de fermeture générale**.

Les contrôles H(2,3) et BvLS valident les identités générales dans leurs paramètres propres. Ils ne permettent pas de leur appliquer les hypothèses spécifiques à 99 sommets et au premier 7.

Le contrôle d’intégrité de cet assemblage compare chaque bloc extrait à son fichier original, ainsi que les deux manifestes SHA-256. Les résultats mathématiques ne sont pas déduits de ces empreintes : ils reposent sur les preuves et les vérifications exactes incluses.
