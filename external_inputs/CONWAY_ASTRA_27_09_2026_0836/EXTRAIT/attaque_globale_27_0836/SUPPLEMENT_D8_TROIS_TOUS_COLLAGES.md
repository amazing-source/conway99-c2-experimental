# Tous les collages unimodulaires de D8³ sont incompatibles avec le repère physique

**Statut : démontré après contre-audit indépendant ; trois classifications exactes concordantes.** Supplément séparé : aucune des14 pièces du manifeste ALGÈBRE0836 n'est modifiée.

## 1. Cadre et prérequis

Supposer qu'une enveloppe intégrale unimodulaire U de rang24, de minimum au moins2, contienne le repère physique49 et ses deux normales de carré7. Le réseau physique N a rang22, les42 u de carré3 l'engendrent intégralement, et min(N*)≥8/7. Ces propriétés sont communes à g18 et g20, sans P0.

Supposer que U contienne trois D8 orthogonaux engendrés par des racines. Leur somme R=D8³ a plein rang, determinant64. L'indice [U:R] est donc8. Le discriminant R*/R est F2⁶, somme de trois plans symplectiques. Un collage intégral unimodulaire correspond à un sous-espace Lagrangien L de dimension3 pour la forme 2(·,·) modulo2.

Dans chaque composante, noter les classes0,v,s,c=s+v. Les minima sont0,1,2,2. Pour les produits symplectiques, les trois classes non nulles sont deux à deux de produit1, et chacune a produit0 avec elle-même. Le carré modulo2 est1 pour v et0 pour s,c.

Le minimum d'une classe triple est la somme de ces trois minima. Les accroissements de carré sont pairs. Les classes de minimum1 sont les singletons v ; les classes de minimum2 sont les singletons s,c et les doubles v.

Trois obstacles acquis peuvent être appliqués d'abord :

* Une singleton v donnerait un vecteur de carré1, contraire au minimum de U.
* Une singleton s ou c étend D8 en E8 unimodulaire, donc détache un facteur E8. Dans un réseau de minimum2, un vecteur de carré3 ne peut avoir une composante E8 non nulle : seul E8 serait pair, et une composante complémentaire non nulle coûterait au moins2 de plus. Les42 u seraient dans l'orthogonal de dimension16, impossible pour N de rang22.
* Une double-v ajoute des racines reliant les deux D8 et forme D16 ; ce sous-système contient D12, interdit par [G18_G20_D12_COLLAGE.md](../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md). Ce dernier lemme utilise le repère commun, même pour un sous-espace de racines extérieur à N, sans P0.

Les collages pairs n'ont aucun vecteur de carré3, et ne peuvent porter les42 u.

## 2. Preuve directe du piège local, sans dénombrement

Le repère fournit déjà un vecteur de carré3. Sa classe dans R*/R n'est pas nulle, puisque R est pair. Les classes de minimum1 ayant été exclues, elle a minimum3. Deux formes existent : vvv ou un v, un spinor et un zéro.

### Une classe vvv

Tout autre mot de minimum3 est de la forme v-spinor-0. Son produit symplectique avec vvv vaut1, donc il ne peut appartenir au même Lagrangien. La coque3 entière a alors uniquement la classe vvv : ses projections dans chacune des trois composantes D8 sont des unités entières.

### Une classe v-spinor-0

Après permutation des composantes et échange s,c dans une composante, prendre a=(v,s,0). Une autre classe de minimum3 dont le centre v est différent se traite exhaustivement comme suit.

| Autre classe | Obstruction |
|---|---|
| (0,v,t), t=s ouc | Produit symplectique1 avec a. |
| (t,0,v), t=s ouc | Produit symplectique1 avec a. |
| (0,c,v) | Produit symplectique1 avec a. |
| (0,s,v) | Sa somme avec a est(v,0,v), double-v interdite. |
| (t,v,0), t=s ouc | Avec a, elle forme un Lagrangien complet de dimension2 dans les deux premières composantes. |

Dans le dernier cas, le discriminant des deux premières composantes est non dégénéré de dimension4. L'orthogonal de ce plan y est le plan lui-même. Le troisième générateur du Lagrangien de dimension3 doit donc, après soustraction d'une combinaison des deux premiers, donner un mot singleton non nul dans la troisième composante. Il serait v, s ou c, déjà interdit.

Ainsi toute classe de coque3 a son v dans la première composante. Dans cette composante, **les projections de tous les vecteurs de la coque3 sont entières**, de classe0 ou v. Cette conclusion ne dépend pas des signes, ni du nombre de vecteurs choisis dans chaque classe.

Les huit axes orthonormaux de cette composante ont donc des produits entiers avec les mêmes42 u. Comme ils engendrent N intégralement, les projections des axes sur N appartiennent à N* et ont carré≤1. La borne8/7 les force toutes à zéro. Un sous-espace de dimension8 serait alors contenu dans N⊥, de dimension2 : contradiction.

Cela ferme **toutes** les enveloppes intégrales unimodulaires de rang24 contenant D8³ et ce repère, pas seulement le collage initial ss0/0ss/vvv. Aucune classification de lattices24 n'est invoquée ; seule la présence de trois D8 orthogonaux de racines est supposée.

## 3. Classification complémentaire des glues encore admissibles

Le calcul exact des135 Lagrangiens confirme les strates suivantes, dans cet ordre de filtrage.

| Strate | Nombre |
|---|---:|
| Collages pairs, aucune coque3 |30|
| Collages impairs avec minimum1 |37|
| Impairs sans minimum1, avec singleton spinor/E8 |24|
| Impairs précédents exclus, avec double-v/D16 |12|
| Impairs sans ces obstacles |32|

Les32 derniers sont déjà fermés par le §2. À permutation des composantes et échanges s,c indépendants près, ils ont exactement deux formes.

* **Forme A, huit glues :** engendrée par(s,s,0), (0,s,s), (v,v,v). Sa seule classe3 est vvv. Les huit glues s'obtiennent en choisissant s ouc dans chaque composante.
* **Forme B, vingt-quatre glues :** engendrée par(v,s,0), (v,0,s), (s,v,v). La coque3 a les deux classes(v,s,0) et(v,0,s). Les permutations et échanges s,c donnent24 glues distinctes. Le centre v est commun aux deux classes.

Ces deux formes ont chacune4096 vecteurs de carré3 :4096 dans la classe vvv, ou2048 dans chacune des deux classes v-spinor-0.

Pour vérifier la seconde forme humainement, fixer les deux classes3 a=(v,s,0), b=(v,0,s). Un troisième générateur avec coefficient s nul dans la première composante produirait, modulo leur span, une singleton v. Les deux possibilités restantes sont représentées par(s,v,v) et(c,v,v). Elles sont échangées par s↔c dans la première composante. Avec les choix des spinors dans les deux autres composantes et du centre v, cela donne3·2³=24.

L'existence d'une seconde classe3, utile pour ce dénombrement mais inutile pour la preuve du §2, se voit aussi par les coûts. Le collage impair contient quatre classes de carré impair. Un mot de minimum5 porte v en un centre et deux spinors ; au plus un tel mot par centre est possible, sinon leur somme est une singleton v ou une double-v. Après a=(v,s,0), un mot de minimum5 au premier centre donnerait une singleton spinor par différence. Il reste au plus deux mots de minimum5, donc une seconde classe3. Le tableau du §2 impose le même centre v.

## 4. Certificats séparés et portée

[classifier_collages_D8_trois.mjs](classifier_collages_D8_trois.mjs) énumère les sous-espaces dimension3 par formes RREF3×6, filtre la symplecticité, recalcule les minima et toute la coque de classes3, puis vérifie les deux orbites sous48 isométries du discriminant. Le résultat [classifier_collages_D8_trois.json](classifier_collages_D8_trois.json) conserve les135 certificats, les huit mots de chaque glue et une composante entière pour chaque survivant.

Le parent a refait les135 collages par une voie indépendante et retrouve135/32 et8+24. L'auditeur a terminé une troisième voie par extensions orthogonales, différente de RREF : mêmes strates et mêmes32 glues, toutes de coque4096. Il contrôle aussi les36 paires orthogonales de classes3 dont les centres diffèrent, qui produisent une somme interdite ou saturent deux composantes. Voir [AUDIT_FAMILLE_COMPLETE_D8_TROIS.md](AUDIT_FAMILLE_COMPLETE_D8_TROIS.md) et [verifier_collages_D8_independant.json](verifier_collages_D8_independant.json). Le dénombrement soutient la preuve mais n'en est pas une boîte noire : le §2 est couvrant à lui seul.

Le résultat n'exclut pas toutes les enveloppes de rang24, ni g18/g20. D4⁶ et D6⁴ demandent leurs contraintes propres ; on ne leur attribue pas le piège de coque entière de D8³. Les14 pièces du manifeste ALGÈBRE0836 restent immuables ; ce supplément est un ajout séparé.
