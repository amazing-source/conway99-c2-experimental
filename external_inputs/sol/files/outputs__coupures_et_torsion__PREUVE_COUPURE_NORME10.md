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
