# Le repère physique impose un petit polaire intégral de dimension au plus deux

**Statut : démontré, après contre-audit humain indépendant et contrôle exact propre.** Le résultat ferme la famille unimodulaire D8³ décrite ci-dessous pour le même repère 42+7, dans les deux cas g18 et g20. Il ne ferme pas toutes les enveloppes unimodulaires de rang 24.

## 1. Hypothèses physiques et génération intégrale

Dans un espace euclidien de dimension 22, le réseau physique N est engendré par sept vecteurs h_c de carré 4 et quarante-deux vecteurs u_o de carré 3, avec Gram

    H = [4I7, −C ; −Cᵀ, 3I42−T].

Les colonnes de C sont les quarante-deux directions D7 : pour chaque paire de blocs i,j, deux sœurs orientables comme e_i+e_j et e_i−e_j. On garde les identités entières

    CCᵀ=12I7, CT=0, T²+T=12I42−CᵀC,
    3h_c + Σ_o C_co u_o = 0.

Les propriétés arithmétiques acquises du réseau physique sont : N a rang 22, déterminant impair, et tout vecteur non nul de N* a carré au moins 8/7. Cette borne duale n'est pas revendiquée comme nouvelle. Les hypothèses ne comprennent pas P0.

Rappelons la génération entière, car elle relie la même sélection des quarante-deux u au polaire ci-dessous. Poser U(v)=Σ_o v_o u_o et h(a)=Σ_c a_c h_c. Les produits avec tous les générateurs et l'identité

    (3I−T)(T+4I)=CᵀC

donnent

    U((T+4I)v)=−h(Cv).

Pour une paire de sœurs orientées comme ci-dessus, v=e_++e_- donne Cv=2e_i. On a U((T+4I)v)=−2h_i et U(C_iᵀ)=−3h_i. Donc

    h_i = U((T+4I)v−C_iᵀ).

Les coefficients sont entiers. Ainsi Γ42=Σ_o Z u_o=N. La preuve et sa généralisation aux paramètres impairs sont détaillées dans [G18_G20_QUARANTE_DEUX_GENERATEURS.md](G18_G20_QUARANTE_DEUX_GENERATEURS.md).

## 2. Théorème du petit polaire : une contrainte sur la même sélection

Supposer N placé dans un espace euclidien de dimension 24. Définir

    A(S) = { z : z²≤1 et (z,u_o) est entier pour les 42 u_o choisis }.

Alors

    span_R A(S) ⊂ N⊥, donc dim span_R A(S) ≤ 2.                 (P)

En effet, Γ42=N implique que x=proj_N(z) est dans N*. La projection ne peut augmenter le carré, donc x²≤1. La borne duale 8/7 force x=0. Tous les z considérés sont donc dans l'orthogonal de N, de dimension deux.

Les z ne sont pas supposés appartenir à l'enveloppe unimodulaire ni à son dual. Ce sont des directions de test du polaire de la sélection. Trois directions indépendantes de carré au plus 1, intégrales contre les mêmes 42 u, donnent déjà une contradiction.

En particulier, si la coque de carré 3 d'une enveloppe est contenue dans Z24 pour un repère orthonormal, tous ses axes appartiennent à A(S) pour toute sélection de 42 vecteurs de cette coque. Aucun repère physique ne peut alors se placer dans cette enveloppe. Il suffit même que les 42 vecteurs soient entiers sur une tranche orthogonale de dimension au moins trois.

Cette obstruction utilise la génération entière et le gap dual en même temps. Une simple sélection de 42 vecteurs de carré 3 qui engendre l'espace réel n'a pas cette propriété.

## 3. Application uniforme au collage D8³

Dans R8, poser D8={x∈Z8 : Σx_i est pair}, s=(1/2,...,1/2), v=e_1 et c=s+v modulo D8. Les quatre classes 0,v,s,c ont respectivement minima 0,1,2,2. Les classes 0,v sont entières ; s,c sont demi-entières. Les accroissements de carré au sein d'une classe sont pairs.

Ajouter à D8³ les classes

    a=(s,s,0), b=(0,s,s), t=(v,v,v).

Les trois classes sont indépendantes et leurs produits sont entiers : a²=b²=4, t²=3, a·b=2 et a·t=b·t=1. Le réseau U est donc intégral impair ; son indice 8 dans D8³ et det(D8³)=64 donnent det U=1. Les huit classes et minima sont

| Classe | 000 | ss0 | 0ss | s0s | vvv | ccv | vcc | cvc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Minimum | 0 | 4 | 4 | 4 | 3 | 5 | 5 | 5 |

La coque de carré 3 est donc exactement la classe vvv minimale : un vecteur ±e_i dans chacune des trois composantes. Elle a 16³=4096 vecteurs, tous entiers.

Les axes d'une seule composante, de dimension huit, suffisent dans (P). Le repère physique 42+7 est impossible dans U, pour g18 et g20. Cette preuve n'utilise ni une coque caractéristique, ni un repère d'ombres, ni les deux normales de carré 7 ; seul le plongement de N dans l'espace de rang 24 intervient.

La conclusion est indépendante du choix d'un repère orthonormal : une isométrie transporte simultanément la coque, les directions de test et leurs produits. Elle ne suppose pas que ces axes soient des vecteurs de U.

## 4. Second certificat : la coque a un Gram de rang 20 modulo deux

Le résultat fournit aussi une obstruction à la sélection, indépendante de la borne duale. Comme Γ42=N et det N est impair, le Gram 42×42 des u physiques doit avoir rang 22 sur F2 : la matrice des générateurs sur N/2N est surjective et la forme réduite de N est non dégénérée.

Pour toute la coque 3 de U(D8³), le signe des unités disparaît modulo deux. Les 512 triplets non signés ont pour espace engendré

    W = {x∈F2^24 : parité(x_bloc1)=parité(x_bloc2)=parité(x_bloc3)}.

L'espace W a dimension 22. Son orthogonal standard est engendré par

    1_bloc1+1_bloc2, 1_bloc2+1_bloc3.

Ces deux vecteurs sont dans W, car les blocs ont huit coordonnées. Le radical de la restriction à W a donc dimension deux ; le rang du Gram de toute la coque est exactement 20. Toute sous-sélection a rang de Gram au plus 20, contre les 22 requis par le repère physique.

Le contrôle propre [controle_coque3_D8_et_trialite.mjs](controle_coque3_D8_et_trialite.mjs) vérifie ces rangs sur une base de 22 vecteurs et les 512 triplets. Il n'énumère pas une matrice 4096×4096. Son [résultat exact](controle_coque3_D8_et_trialite.json) donne rang d'espace 22, rang de Gram 20, radical 2 et coque 4096.

Plus généralement, une enveloppe dont le Gram modulo deux de toute la coque 3 a rang ≤21 ne peut contenir les 42 u physiques. Cela constitue une condition sur une coque complète, et non une exclusion de toutes les enveloppes de même genre.

## 5. Version locale D4 : les 42 projections doivent mêler au moins deux classes

Supposer que l'enveloppe contient une composante orthogonale D4 et que toutes les projections des 42 u sur cette composante appartiennent aux classes 0 et une seule classe non nulle a∈{v,s,c} de D4*/D4. Alors cette sélection est impossible.

Une trialité préservant D4 envoie a vers v. Après cette isométrie, les projections sont entières dans quatre axes orthonormaux. Ces quatre axes ont carré 1 et produit entier avec les mêmes 42 u ; le théorème (P) donnerait un sous-espace de dimension quatre dans N⊥, de dimension deux.

La trialité est explicite. Pour s=(1/2)^4, la matrice suivante, divisée par deux, préserve D4 et envoie s vers e_1 :

    [1  1  1  1]
    [1  1 −1 −1]
    [1 −1  1 −1]
    [1 −1 −1  1].

Sa préservation de D4 vient de l'intégralité des sorties quand la somme des entrées est paire, et de la parité de leur somme. Une inversion d'une coordonnée préserve aussi D4 et échange s,c. Leur composition traite c. Les vingt-quatre racines D4 et les huit représentants minimaux de chacune des classes s,c ont été contrôlés exactement dans le même source.

Cette version locale, trouvée également par g18_combinatoire_neuve, est plus forte que l'hypothèse « une seule lettre dans chacune des six composantes D4 ». Dans un collage D4⁶, **chaque composante** doit mêler au moins deux classes non nulles parmi les 42 vecteurs sélectionnés. Ce n'est pas une affirmation sur tous les collages D4⁶ : certaines coques mêlent effectivement plusieurs classes, et restent hors de cette coupe.

## 6. Preuve indépendante par les 51 vecteurs et limites

Une autre preuve, n'utilisant pas le gap dual, est donnée dans [EXCLUSION_FRAME_D8_TROIS.md](EXCLUSION_FRAME_D8_TROIS.md) et son contrôle indépendant. Elle emploie les caractéristiques explicites de carré 8 pour exclure les h demi-entiers, puis l'identité diagonale du repère 49+2 pour rendre les deux normales entières. Le sous-réseau entier d'U a indice 4 ; il ne peut contenir N⊕7I2 d'indice impair 49 ou 343.

Les preuves concernent la même sélection physique, et non la seule existence d'un réseau de rang 22, déterminant 49, minimum 3. Le contre-modèle Golay du dossier 0803 conserve toutes ses propriétés : sa coque 3 n'est pas entière dans vingt-quatre axes et aucune sélection physique complète n'y est encore établie. Aucun type local ni genre g18/g20 n'est déclaré fermé par le présent résultat.
