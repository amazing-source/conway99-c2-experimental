# Une involution avec g⁻=16 force un prisme

26 septembre 2026. g⁻ désigne le 7-rang du secteur antisymétrique de l'involution.

**Théorème.** Soit Γ un srg(99,14,1,2) possédant une involution σ. Soit S sa matrice d'adjacence sur les 49 coordonnées antisymétriques, et g⁻=rang₇(S−3I). Si g⁻=16, Γ contient un prisme triangulaire induit. En combinant avec les acquis de genre, **P=0 implique g⁻∈{18,20}**.

**Statut : démontré avec une couverture finie vérifiée exactement par deux implémentations.** La preuve utilise les faits de genre des dossiers n°6 et de la campagne A33 : g⁻ pair, g⁻≤20, forme antisymétrique modulo 7 hyperbolique. Elle ne démontre ni l'impossibilité de toute involution, ni P>0 aux rangs 18 et 20. Aucun solveur SAT, CP ou PLNE n'a été utilisé. Les vérifications Python ont été exécutées à distance, pas sur le PC de l'utilisateur.

Le nouveau pas ne suppose pas qu'une étoile A33 apparaisse. Il couvre **toutes les étoiles possibles sous P=0**. L'objet utilisé est la forme de Witt du bloc dégénéré, couplée à l'espace entier de ses torsions équilibrées et aux comptes exacts des ombres appariées.

## 1. Acquis et couverture combinatoire

Une involution fixe seulement x, retourne les sept blocs de N(x), et groupe les 84 racines en 42 orbites. Deux racines d'une même orbite ne sont pas adjacentes. Le partenaire double D forme un couplage parfait des orbites.

Sous P=0, les supports des deux orbites d'un carré D sont disjoints : un bloc commun donnerait un prisme préservé par σ. Une arête simple entre orbites sœurs donne elle aussi un prisme avec une droite par x. Ainsi, dans l'étoile d'un bloc c, il n'y a ni partenaire double interne ni arête entre sœurs.

Orienter les douze racines w_a de cette étoile pour qu'elles contiennent (c,+). Noter s l'appariement des douze étiquettes des six autres blocs, μ l'appariement positif w_a~w_μ(a), et τ l'appariement négatif w_a~σw_τ(a). Les comptes avec (c,+) et (c,−) donnent exactement un voisin de chaque sorte. μ et τ sont sans point fixe et n'ont pas d'arête commune. Leur union est un graphe 2-régulier alterné.

Un cycle alterné de longueur quatre donne un prisme : si ses arêtes positives sont 12 et 34, les triangles {(c,+),w₁,w₂} et {(c,−),σw₃,σw₄} ont pour barreaux (c,+)(c,−), w₁σw₄ et w₂σw₃. Il ne reste donc que **C₁₂ ou C₆⊔C₆**. s évite leurs arêtes. Ces arguments sont aussi écrits dans ../automorphismes_1_2/involution/quotient_exact.md §5 et etoiles_et_schur.md §1.

On fixe chaque cycle signé canonique, arêtes positives puis négatives alternées, et parcourt tous les appariements s évitant les arêtes. Les rotations paires et réflexions impaires préservent les signes ; pour deux C₆, on ajoute l'échange des composantes.

| Cycle signé | Appariements étiquetés | Classes sous les automorphismes signés |
|---|---:|---:|
| C₁₂ | 3 326 | 362 |
| C₆⊔C₆ | 3 328 | 79 |
| Total | 6 654 | **441** |

Ce n'est pas une classification de graphes complets. C'est une couverture des données d'une étoile nécessaire dans tout graphe sans prisme. Le premier catalogue et une nouvelle génération indépendante donnent les mêmes nombres et représentants.

## 2. Une borne de Witt tenant compte des torsions

Travailler sur F₇. Poser H=3I−S et G=F₇⁴⁹/ker H, muni du Gram H. Les acquis de genre donnent G hyperbolique, dim G=g⁻. Leur application à A33 était écrite dans ../fermeture_A33/PREUVE.md §2 ; aucune nouvelle hypothèse de genre n'est ajoutée ici.

Prendre les sept coordonnées de blocs et les douze orbites de l'étoile. La matrice Z de taille 7×12 a une ligne constante pour c et, sur chaque paire s des autres blocs, une ligne (+1,−1). Alors ZᵀZ=J+I−P_s. Le bloc connu est

    H_I = [[4I₇, −Z], [−Zᵀ, 3I₁₂−W]],   W=P_μ−P_τ.

Son complément de Schur est

    K = I₁₂−W+2P_s−2J   (mod 7).

Poser r=7+rang K et t=18−r. Comme K1=0 et 12≠0 modulo 7, son noyau est la somme directe de la constante et d'un espace V de dimension t, constitué des f de somme nulle. Le vecteur universel z_c=(3 au bloc c, 1 sur l'étoile) est dans le noyau global. Une torsion f∈V fournit un vecteur de noyau local (2Zf,f).

Soit V₀ le sous-espace des torsions dont ce vecteur, prolongé par zéro aux trente autres orbites, appartient aussi au noyau global. Écrire r₀=dim V₀. L'image U des dix-neuf coordonnées dans G vérifie exactement

    dim U = 18−r₀,   rang(U)=r,   dim rad(U)=t−r₀.

**Lemme de Witt.** Dans une forme hyperbolique de dimension g, un sous-espace de rang r et de radical de dimension h impose

    g ≥ r+2h+ε,

où ε=0 pour r pair et la partie non dégénérée scindée, ε=2 pour r pair et cette partie non scindée, et ε=1 pour r impair.

Preuve : quotienter rad(U)⊥ par rad(U). Le quotient est hyperbolique de dimension g−2h. La partie non dégénérée de U y a un complément orthogonal. Si elle est paire non scindée, son complément doit être pair non scindé, donc de dimension au moins deux. Si elle est impaire, le complément est impair, donc de dimension au moins un. Dans le cas pair scindé, la seule borne nécessaire est zéro. ∎

Il en résulte la **borne simultanée**

    g⁻ ≥ 18+t−2r₀+ε.                         (1)

Le caractère du discriminant réduit de H_I est celui de K : det(4I₇) est carré. En dimension paire r, le signe scindé vaut (−1)^(r/2).

## 3. Neuf types seulement peuvent atteindre g⁻=16

Le tableau suivant est obtenu par congruence symétrique en JavaScript, puis par rang et mineur principal maximal sur Sage, dans une seconde implémentation.

| r | Caractère du discriminant | t | ε | Nombre de types |
|---:|---:|---:|---:|---:|
| 15 | −1 | 3 | 1 | 1 |
| 16 | −1 | 2 | 2 | 13 |
| 16 | +1 | 2 | 0 | 8 |
| 17 | −1 | 1 | 1 | 16 |
| 17 | +1 | 1 | 1 | 58 |
| 18 | −1 | 0 | 0 | 142 |
| 18 | +1 | 0 | 2 | 203 |

Les 419 types de rang 17 ou 18 sont exclus par le rang. Les treize types de rang 16 non scindés sont exclus par (1), même avec r₀=t. Restent les huit types de rang 16 scindés et le type de rang 15. **Pour chacun, (1) à g⁻=16 impose r₀=t. Toutes les torsions doivent donc s'équilibrer.**

Leurs indices, à partir de zéro dans catalogue_441.json, sont 202, 246, 277, 281, 300, 303, 309, 360 et 389. μ et τ sont lus sur les arêtes positives et négatives du cycle canonique ; le fichier donne tous les appariements s. Seul 389 appartient à la famille 2C₆ ; les huit autres sont C₁₂.

Le rang local minimal vaut 15. Comme g⁻ est pair, tout cas P=0 a déjà g⁻≥16 ; il suffit désormais d'exclure ces neuf types.

## 4. Les deux ensembles de paires et les comptes exacts

Il faut distinguer les deux appariements interdits :

- Les soixante racines lointaines sont les paires z∈E(K₁₂−s), identifiées à leurs deux voisins intérieurs ; σz=sz.
- Leur ombre F(z), soit leurs deux voisins parmi les w_a, appartient à E(K₁₂−μ). F est une bijection entre ces deux ensembles de soixante paires.

Pourquoi la bijection ? Un lointain a exactement deux voisins dans N(c,+) ; ils sont dans l'étoile. Une paire non partenaire de cette étoile a c,+ comme premier voisin commun et un unique second voisin commun, lointain. Une paire partenaire a déjà son unique voisin commun c,+. Ces comptes donnent la bijection.

Pour a,b étiquettes, les deux tableaux entiers forcés sont

    K₂[a,b] = 2−[a=b]−[b=s(a)]−[b=μ(a)]−[b=τs(a)],
    K₃[a,b] = 2−[b=τ(a)]−[b=s(a)]−[b=τμ(a)]−[b=μτ(a)].   (2)

K₂ compte les lointains z contenant a avec b∈F(z). En effet le compte λ/μ entre l'intérieur a et w_b vaut 2−[a=b] ; les trois autres termes retranchent ses voisins communs dans la boule.

K₃ compte les lointains z avec a∈F(z) et b∈F(sz). Le compte entre w_a et σw_b vaut 2−[b=τ(a)] ; les trois derniers termes retranchent le voisin intérieur partagé et les deux voisins communs possibles dans les deux étoiles.

Une torsion f∈V₀ satisfait, pour chaque racine z,

    f(F(z))−f(F(sz))+2[f(z)−f(sz)] = 0   (mod 7),         (3)

avec f({a,b})=f(a)+f(b). C'est exactement la ligne extérieure de H(2Zf,f)=0 : Z_extᵀZf=f(z)−f(sz), et la contribution signée de l'étoile vaut f(F(z))−f(F(sz)). À g⁻=16, (3) doit tenir pour **une base entière de V**, et non seulement pour une direction choisie.

Pour chaque orbite {z,sz}, on énumère donc les couples ordonnés distincts (e,f) d'ombres dans K₁₂−μ. On conserve seulement les couples qui n'utilisent aucun zéro de K₂, dont la contribution à K₃ ne dépasse pas les capacités de (2), et qui satisfont toutes les congruences (3). Toute réalisation réelle doit choisir une colonne de ce domaine pour chaque orbite. Les contraintes entre lointains ne sont pas utilisées ; leur omission agrandit les domaines et ne rend pas la réfutation plus forte artificiellement.

## 5. Six domaines vides et deux budgets d'apex impossibles

Comme μ et τ sont sans arête commune, K₃[b,b]=2 pour toute étiquette b. Chaque couple d'ombres qui se rencontre en b contribue exactement deux à cette diagonale. Deux ombres distinctes ont au plus une étiquette commune. Il faut donc **exactement douze couples ayant un centre, un par étiquette**, et dix-huit couples d'ombres disjointes.

| Type | Dimension t | Total de colonnes | Orbites autorisant un centre | Obstruction |
|---:|---:|---:|---:|---|
| 202 | 2 | 1 872 | 8 | domaine vide |
| 246 | 2 | 1 994 | 14 | certificat du §6 |
| 277 | 2 | 1 860 | 6 | au moins 12 centres requis |
| 281 | 3 | 211 | 0 | domaine vide |
| 300 | 2 | 1 860 | 6 | au moins 12 centres requis |
| 303 | 2 | 2 303 | 8 | domaine vide |
| 309 | 2 | 2 023 | 8 | domaine vide |
| 360 | 2 | 2 340 | 3 | domaine vide |
| 389 | 2 | 1 872 | 8 | domaine vide |

Pour les six types à domaine vide, une orbite sans choix suffit. Pour 277 et 300, même en ignorant l'unicité des centres et toutes les autres équations globales, six orbites au plus peuvent fournir les douze centres nécessaires. Contradiction. Les domaines complets, leurs tailles et les orbites vides sont dans domaines_neuf_types.json et sorties_independantes.txt.

## 6. Un certificat entier ferme le dernier type

Le type 246 est C₁₂, avec

    μ=(0 1)(2 3)(4 5)(6 7)(8 9)(10 11),
    τ=(0 11)(1 2)(3 4)(5 6)(7 8)(9 10),
    s=(0 3)(1 4)(2 6)(5 9)(7 10)(8 11).

Une base de V, avec des représentants entiers des résidus, est

    f₁=(−1,−2,−2,2,−2,3,3,2,−3,3,2,2),
    f₂=(−1,0,−1,1,0,1,1,0,1,−1,0,−1).

Les trente représentants z<sz sont ordonnés lexicographiquement. Pour une colonne (z,e,f), construire son vecteur c de 348 comptes :

1. 60 comptes d'utilisation des ombres, une unité en e et en f ;
2. 144 comptes K₂, dans l'ordre des lignes a puis des colonnes b : incidence z×e plus sz×f ;
3. 144 comptes K₃ : incidence e×f plus f×e.

Le total d'une vraie réalisation est exactement

    b = (1⁶⁰, vec K₂, vec K₃).

Le certificat fournit un prix entier p∈Z³⁴⁸, douze prix α_b pour les centres, dix-huit prix identiques α_dis=25 pour les couples disjoints, et trente prix β_z. **Pour chacune des 1 994 colonnes autorisées**, les deux vérificateurs contrôlent

    p·c + α_centre-ou-disjoint + β_z ≤ 0.               (4)

La somme de trente colonnes d'une réalisation utiliserait chaque centre une fois, dix-huit couples disjoints, et chaque orbite z une fois. En sommant (4), on obtient

    0 ≥ p·b + Σα + Σβ = 90.

**Contradiction.** Le dernier type est exclu.

Le fichier certificat_246.json contient les **408 coefficients entiers**. Les ordres sont explicités ci-dessus. Les deux programmes donnent maximum du membre de gauche individuel =0 et somme cible =90. Le certificat ne dépend d'aucun flottant, ni d'un verdict opaque de solveur. Sa recherche a employé onze itérations de prix entiers avec un algorithme d'affectation écrit ici. La première direction testée est (0,0) : **aucune identité d'énergie quadratique supplémentaire n'est nécessaire à cette fermeture**. Les valeurs d'énergie 60 et 16 sont des sorties de découverte, pas des ingrédients de (4).

## 7. Vérification indépendante et contrôles

Le premier calcul utilise une élimination de Gauss et une congruence symétrique écrites en JavaScript. Il réutilise notre catalogue ancien. Le second programme reconstruit le catalogue sans le lire, utilise Sage pour les noyaux et les mineurs maximaux, puis une recherche de domaines écrite séparément. Ses bases de torsion n'ont pas besoin d'être identiques à celles du premier programme. Tous les histogrammes et les neuf domaines coïncident ; les 1 994 inégalités du certificat sont revérifiées.

Les programmes contrôlent aussi les identités (2) et la bijection d'ombre sur deux graphes construits intégralement, avec σ(v)=−v :

| Graphe réel | Étiquettes de l'étoile | Lointains | Entrées K₂/K₃ contrôlées |
|---|---:|---:|---:|
| H(2,3), 9 sommets | 2 | 0 | 8 |
| BvLS, 243 sommets | 20 | 180 | 800 |

Les nombres de voisins communs de tous les couples de sommets sont contrôlés avant ces tests. Le contrôle H(2,3) des ombres est vide ; le contrôle BvLS ne l'est pas. Les raccords algébriques de Witt avaient déjà été testés sur ces deux graphes dans la campagne A33. On ne leur applique pas les contraintes de genre propres à 99/modulo 7 : leurs spectres et leur premier de recollement diffèrent, et ils possèdent des prismes.

Le répertoire conserve la preuve, le catalogue, les rangs et signes, les neuf domaines, le certificat, les deux vérificateurs, le programme de découverte, les contrôles positifs et leurs sorties. DOSSIER_COMPLET.md est une version autonome avec annexes de sources et de certificats.

Une première exploration avait confondu les appariements interdits s et μ dans les ombres. Elle a été corrigée avant la production du certificat. **Les résultats retenus ici utilisent racines K₁₂−s et ombres K₁₂−μ**, distinction testée sur BvLS. Les essais distants interrompus ou incomplets ne servent pas de preuve ; seule la passe indépendante achevée, terminant par G16_NO_PRISM_EXCLUDED True, est retenue.

## 8. Conséquence et étape suivante

Toute étoile sous P=0 est dans le catalogue ; aucune ne peut apparaître à g⁻=16. Donc g⁻=16 force P≥1. Avec le minimum local 15, la parité de g⁻ et son plafond 20, le cas sans prisme est réduit à **g⁻=18 ou 20**.

La borne (1) précise déjà l'attaque de g⁻=18 :

- les 203 types de rang 18 non scindés sont interdits par le signe ;
- les 74 types de rang 17 exigent r₀=1=t ;
- les treize types de rang 16 non scindés exigent r₀=2=t ;
- les huit types de rang 16 scindés exigent r₀≥1 ;
- l'unique type de rang 15 exige r₀≥2 ;
- les 142 types de rang 18 non scindés n'ont pas de torsion locale forcée par (1).

Cela ne les exclut pas tous. Les étoiles de rang 18 non scindées sont le prochain verrou sans torsion disponible ; il faudra y contrôler les résidus ou plusieurs étoiles ensemble. À g⁻=20, (1) seule laisse davantage de liberté.

**Restent indécis :** P>0 pour toute involution, l'involution sans hypothèse P=0, les dernières familles de normes 9 et 10, et le cas sans symétrie. Cette campagne n'autorise aucune affirmation de non-existence globale. La poursuite programmée reste active.


---

## Annexe — ETAT_REPRISE.md

````text
# Reprise — couverture de g⁻=16

26 septembre 2026. Résultat nouveau : **une involution avec g⁻=16 force un prisme**, donc **P=0 ⇒ g⁻∈{18,20}** avec les acquis de genre.

## Terminé et vérifié

- Couverture de toutes les étoiles à P=0 : 3 326 appariements sur C12 / 362 classes, 3 328 sur 2C6 / 79 classes, total 441.
- Nouvelle borne de Witt : g⁻≥18+t−2r0+ε, t=18−rang(H_I), ε=0/2 suivant le type en rang pair, ε=1 en rang impair.
- À g⁻=16, seuls 202,246,277,281,300,303,309,360,389 restent ; pour chacun r0=t.
- Six types ont une orbite sans aucune paire d'ombres admissible.
- Types 277 et 300 : seuls six couples peuvent avoir un centre, contre douze requis.
- Type 246 : 1 994 colonnes, certificat entier de 408 coefficients, chaque membre de gauche ≤0 et somme cible =90. Contradiction 0≥90.
- JS : rang, congruence, noyaux, domaines, certificat ; Sage/Python indépendant : catalogue régénéré, rangs et mineurs, autres bases de noyaux, domaines et certificat. Accord complet.
- Contrôles de K2/K3 et bijection d'ombre : H(2,3), 8 entrées (lointains vides), BvLS, 800 entrées et 180 lointains. Graphes construits et tous les λ/μ contrôlés.
- Sources distantes et copies locales comparées exactement par empreinte FNV de transfert ; manifeste SHA256 séparé. Aucun Python exécuté localement et aucun solveur externe.

## Garde-fous

- Racines : K12−s ; ombres : K12−μ. Une exploration initiale avait confondu ces deux ensembles ; tous les résultats retenus ont été corrigés et indépendamment refaits.
- Des essais SageMathCell incomplets et un export contenant une ancienne faute de frappe ont été abandonnés. La source conservée et son corps indépendant correspondent à la passe finale réussie.
- La recherche du certificat a essayé la direction (0,0) en premier et trouvé l'écart 90 en onze itérations. Les énergies 60 et 16 ne servent pas à cette preuve.
- Le théorème dépend des acquis de genre du dossier n°6 : g⁻ pair, ≤20, forme H mod7 hyperbolique. Son nouveau contenu est l'application uniforme aux 441 types.
- Aucune carte locale survivante ne prouve l'existence d'un graphe complet. Aucun prisme forcé à g⁻=18 ou 20 n'est encore démontré.

## Prochain sous-problème concret

Attaquer g⁻=18 avec les mêmes domaines, **sans refaire g⁻=16** :

1. Les 74 étoiles de rang17 et les 13 de rang16 non scindées doivent prolonger toute leur torsion. Tester directement (3) sur une base entière de leur noyau, domaines et budget de douze centres, puis certificats entiers si nécessaire.
2. Les 8 étoiles de rang16 scindées exigent au moins une direction équilibrée ; le type de rang15 en exige au moins deux. La fermeture de tout V à g16 ne suffit pas pour ces exigences plus faibles.
3. 203 étoiles de rang18 non scindées sont déjà interdites à g18 par le signe. Les **142 étoiles de rang18 scindées** sont sans torsion locale forcée ; leur traitement demande le résidu ou le couplage de plusieurs étoiles. Ne pas prétendre les fermer par la borne de Witt seule.
4. Préserver les contrôles m2/m11 en adaptant le premier et les valeurs propres ; aucun transfert de l'hyperbolicité propre à 99 ne doit leur être imposé.

Le cas sans symétrie, la clôture complète des normes 9/10 et l'involution générale restent ouverts. La cible globale de l'automation n'est pas atteinte : **elle reste active**.

Lire PREUVE.md et DOSSIER_COMPLET.md ; les scripts et les sorties sont voisins. Les seules sources de projet consultées pendant cette campagne étaient nos fichiers déjà produits dans ce fil.

````


---

## Annexe — certificat_246.json

````json
{
  "price": [-8,9,-8,7,6,4,7,-6,3,-17,-1,3,3,-1,1,3,-4,-1,0,1,2,8,8,-1,9,-10,0,-6,3,-6,-16,-1,-1,7,-4,6,2,2,-7,4,2,2,-10,0,-12,7,-2,8,-8,8,1,7,3,-4,3,-3,2,7,-2,-9,-6,-5,-3,1,0,5,5,-2,3,-3,4,1,-4,-4,-1,-3,-4,-1,1,4,5,-1,5,3,-5,0,-6,-1,1,2,3,3,7,-3,3,-4,-2,6,1,-8,3,-4,-1,5,-3,3,1,-1,1,-3,-3,1,-2,-5,0,3,2,1,4,1,4,2,6,-4,-3,-9,-2,7,-5,2,-3,5,5,-3,2,-5,3,-3,-8,-1,0,8,-1,3,0,4,2,6,4,0,-6,-3,1,-7,-3,2,0,4,3,-5,1,-2,-2,7,-9,1,4,-2,1,0,2,11,4,6,2,-3,-3,-12,0,-8,3,4,2,2,1,2,-1,-3,-4,0,-3,-3,-3,3,-3,5,2,7,7,-5,-2,-1,-5,-5,0,6,3,-12,3,-7,-1,2,-5,9,-6,2,6,0,-5,-3,2,3,0,1,-1,5,2,-2,3,-5,0,-1,-4,-5,-5,4,-2,8,1,8,-12,-3,-1,0,0,4,8,2,7,-7,4,-2,3,2,-4,0,0,4,1,3,-1,1,4,-3,-7,3,-5,4,4,0,4,-1,7,-10,3,-4,-1,0,-5,8,1,4,0,-1,2,-10,3,-3,2,1,4,2,3,-1,-1,0,1,-1,0,2,-5,-1,-2,7,-1,7,2,1,0,-5,0,-11,9,5,8,-7,1,-10,-10,-1,-5,0,-6,4,-6,2,1,4,4,3,3,0,0,-6,0,1,2,-2,8,-2,-3,-4,-3,2,-11,4,1,0],
  "dual_left": [62,49,50,54,42,56,58,47,53,47,46,59,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25],
  "dual_right": [-3,-78,-3,-77,-83,0,-79,-82,-1,-82,-14,-11,-7,-69,-1,-10,-69,-4,-73,-11,-75,-74,-10,-81,-16,-81,-9,-83,-13,-9],
  "bound":90,
  "iteration":10
}

````


---

## Annexe — verifier_JS.mjs

````javascript
// Exact verification over F7 and Z. No package or solver.
import fs from 'node:fs/promises';
const directory=new URL('./',import.meta.url);
var catalogResearch=JSON.parse(await fs.readFile(new URL('catalogue_441.json',directory),'utf8'));
var cert=JSON.parse(await fs.readFile(new URL('certificat_246.json',directory),'utf8'));
var mod7New=x=>((x%7)+7)%7;
var inv7New=x=>[0,1,4,5,2,3,6][mod7New(x)];
function rankNew(A){var b=A.map(r=>r.map(mod7New));var r=0;for(var j=0;j<b[0].length&&r<b.length;j++){var i=r;while(i<b.length&&!b[i][j])i++;if(i===b.length)continue;[b[r],b[i]]=[b[i],b[r]];var q=inv7New(b[r][j]);b[r]=b[r].map(x=>mod7New(x*q));for(i=r+1;i<b.length;i++){q=b[i][j];if(q)b[i]=b[i].map((x,k)=>mod7New(x-q*b[r][k]));}r++;}return r;}
function congruenceNew(A){var b=A.map(r=>r.map(mod7New)),rank=0,disc=1;while(b.length){var n=b.length,i=b.findIndex((row,j)=>row[j]);if(i>=0){var p=[i,...Array.from({length:n},(_,j)=>j).filter(j=>j!==i)];b=p.map(j=>p.map(k=>b[j][k]));var d=b[0][0],q=inv7New(d);disc=mod7New(disc*d);rank++;b=b.slice(1).map((row,j)=>row.slice(1).map((x,k)=>mod7New(x-b[j+1][0]*q*b[0][k+1])));}else{var pair=null;for(i=0;i<n&&!pair;i++)for(var j=i+1;j<n;j++)if(b[i][j]){pair=[i,j];break;}if(!pair)break;var p=[...pair,...Array.from({length:n},(_,j)=>j).filter(j=>!pair.includes(j))];b=p.map(j=>p.map(k=>b[j][k]));var d=b[0][1],q=inv7New(d);disc=mod7New(disc*(-d*d));rank+=2;b=b.slice(2).map((row,j)=>row.slice(2).map((x,k)=>mod7New(x-q*(b[j+2][0]*b[1][k+2]+b[j+2][1]*b[0][k+2]))));}}return {rank,disc,char:[1,2,4].includes(disc)?1:-1};}
function kernelNew(A){var b=A.map(r=>r.map(mod7New)),r=0,piv=[];for(var j=0;j<b[0].length&&r<b.length;j++){var i=r;while(i<b.length&&!b[i][j])i++;if(i===b.length)continue;[b[r],b[i]]=[b[i],b[r]];var q=inv7New(b[r][j]);b[r]=b[r].map(x=>mod7New(x*q));for(i=0;i<b.length;i++)if(i!==r){q=b[i][j];if(q)b[i]=b[i].map((x,k)=>mod7New(x-q*b[r][k]));}piv.push(j);r++;}var free=Array.from({length:b[0].length},(_,i)=>i).filter(i=>!piv.includes(i));return free.map(j=>{var v=Array(b[0].length).fill(0);v[j]=1;for(var i=0;i<r;i++)v[piv[i]]=mod7New(-b[i][j]);return v;});}
function dataFixedNew(index){var item=catalogResearch[index],s=Array(12),mu=Array(12),tau=Array(12);for(var [a,b] of item.Q_pairs)s[a]=b,s[b]=a;for(var a=0;a<12;a++)for(var b=0;b<12;b++){if(item.C[a][b]===1)mu[a]=b;if(item.C[a][b]===-1)tau[a]=b;}var K=item.C.map((row,a)=>row.map((v,b)=>(a===b?1:0)-v+2*(s[a]===b)-2));var full=kernelNew(K);var basis=[];for(var v of full){var sum=mod7New(v.reduce((a,b)=>a+b,0)*inv7New(12));var f=v.map(x=>mod7New(x-sum));if(rankNew([...basis,f])>basis.length)basis.push(f);}var K2=Array.from({length:12},(_,a)=>Array.from({length:12},(_,b)=>2-(a===b)-(b===s[a])-(b===mu[a])-(b===tau[s[a]])));var K3=Array.from({length:12},(_,a)=>Array.from({length:12},(_,b)=>2-(b===tau[a])-(b===s[a])-(b===tau[mu[a]])-(b===mu[tau[a]])));var roots=[],shadows=[];for(var a=0;a<12;a++)for(var b=a+1;b<12;b++){if(b!==s[a])roots.push([a,b]);if(b!==mu[a])shadows.push([a,b]);}var seen=new Set(),pairs=[];for(var z of roots){var key=z.join(',');if(seen.has(key))continue;var sz=z.map(a=>s[a]).sort((a,b)=>a-b);seen.add(key);seen.add(sz.join(','));pairs.push([z,sz]);}return {index,s,mu,tau,basis,K2,K3,pairs,shadows};}
function columnsNew(data,checks){var domains=[];for(var [z,sz] of data.pairs){var opts=[];for(var e of data.shadows){if(z.some(a=>e.some(b=>data.K2[a][b]<1)))continue;for(var f of data.shadows){if(e[0]===f[0]&&e[1]===f[1] || sz.some(a=>f.some(b=>data.K2[a][b]<1)))continue;var k3=new Map();for(var b of e)for(var d of f){var k=b*12+d;k3.set(k,(k3.get(k)||0)+1);}for(var b of f)for(var d of e){var k=b*12+d;k3.set(k,(k3.get(k)||0)+1);}if([...k3].some(([k,v])=>v>data.K3[Math.floor(k/12)][k%12]))continue;if(checks.some(v=>mod7New(e.reduce((a,b)=>a+v[b],0)-f.reduce((a,b)=>a+v[b],0)+2*(z.reduce((a,b)=>a+v[b],0)-sz.reduce((a,b)=>a+v[b],0)))))continue;opts.push([e,f]);}}domains.push({z,sz,n:opts.length,choices:opts});}return domains;}
function assert(v,m){if(!v)throw Error(m);}
var eligible=[];var histogram={};
for(var index=0;index<catalogResearch.length;index++){
 var item=catalogResearch[index],s=Array(12);for(var [a,b] of item.Q_pairs)s[a]=b,s[b]=a;
 var K=item.C.map((row,a)=>row.map((v,b)=>(a===b?1:0)-v+2*(s[a]===b)-2));
 var form=congruenceNew(K),r=7+form.rank,t=18-r,eps=r%2?1:(form.char===(-1)**(r/2)?0:2);
 var key=[r,form.char,t,eps,18+t+eps].join(',');histogram[key]=(histogram[key]||0)+1;
 if(r<=16&&18+t-2*t+eps<=16)eligible.push(index);
}
assert(eligible.join(',')==='202,246,277,281,300,303,309,360,389','coverage');
console.log('WITT_HIST',histogram);console.log('G16_ELIGIBLE',eligible);
for(var index of eligible){
 var data=dataFixedNew(index),domains=columnsNew(data,data.basis);
 var empty=domains.filter(d=>!d.n).map(d=>d.z);
 var wedgeable=domains.filter(d=>d.choices.some(([e,f])=>e.some(x=>f.includes(x)))).length;
 console.log('DOMAINS',JSON.stringify({index,torsion:data.basis.length,columns:domains.reduce((a,d)=>a+d.n,0),empty,wedgeable,sizes:domains.map(d=>d.n)}));
 if(![246,277,300].includes(index))assert(empty.length>0,'empty domain');
 if([277,300].includes(index))assert(wedgeable===6,'apex budget');
 if(index!==246)continue;
 var checked=0,maxlhs=-Infinity;var ei=new Map(data.shadows.map((e,i)=>[e.join(','),i]));
 for(var [k,d] of domains.entries())for(var [e,f] of d.choices){
  var center=e.find(x=>f.includes(x));
  var lhs=cert.price[ei.get(e.join(','))]+cert.price[ei.get(f.join(','))]+cert.dual_right[k]+cert.dual_left[center??12];
  for(var a of d.z)for(var b of e)lhs+=cert.price[60+12*a+b];
  for(var a of d.sz)for(var b of f)lhs+=cert.price[60+12*a+b];
  for(var a of e)for(var b of f)lhs+=cert.price[204+12*a+b]+cert.price[204+12*b+a];
  assert(lhs<=0,'certificate column');checked++;maxlhs=Math.max(maxlhs,lhs);
 }
 var bound=cert.price.slice(0,60).reduce((a,b)=>a+b,0)+cert.dual_left.reduce((a,b)=>a+b,0)+cert.dual_right.reduce((a,b)=>a+b,0);
 for(var a=0;a<12;a++)for(var b=0;b<12;b++)bound+=cert.price[60+12*a+b]*data.K2[a][b]+cert.price[204+12*a+b]*data.K3[a][b];
 assert(checked===1994&&bound===90&&maxlhs===0,'final certificate');
 console.log('CERTIFICATE',JSON.stringify({checked,maxlhs,bound,verified:true}));
}
console.log('G16_NO_PRISM_EXCLUDED',true);

````


---

## Annexe — verifier_independant.py

````python
"""Second programme exécuté sur SageMathCell, langage Python.
Copie de la source achevée, avec le certificat séparé dans le fichier JSON.
Coller ce fichier en une cellule SageMathCell/Python en lui préfixant
cert=<contenu JSON>, ou lancer avec Sage Python depuis ce dossier.
"""
from sage.all import *
from itertools import combinations,product
from collections import Counter
import json,hashlib
if 'cert' not in globals():
 from pathlib import Path
 cert=json.loads(Path(__file__).with_name('certificat_246.json').read_text(encoding='utf8'))

def pairings(left,C):
 if not left:
  yield ()
  return
 a=left[0]
 for b in left[1:]:
  if C[a,b]:continue
  for tail in pairings(tuple(x for x in left if x not in (a,b)),C):yield ((a,b),)+tail

def catalogue():
 out=[]
 for lengths in [(12,),(6,6)]:
  C=matrix(ZZ,12);off=0
  for n in lengths:
   for a in range(n):C[off+a,off+(a+1)%n]=C[off+(a+1)%n,off+a]=1 if a%2==0 else -1
   off+=n
  local=[[(tuple((x+a)%n for x in range(n))) for a in range(0,n,2)]+[tuple((a-x)%n for x in range(n)) for a in range(1,n,2)] for n in lengths]
  autos=local[0] if len(lengths)==1 else [tuple(p)+tuple(x+6 for x in q) for p,q in product(*local)]+[tuple(x+6 for x in p)+tuple(q) for p,q in product(*local)]
  seen=set();labeled=0;count=0
  for pairs in pairings(tuple(range(12)),C):
   labeled+=1
   key=tuple(sorted(pairs))
   if key in seen:continue
   orbit={tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in pairs)) for p in autos}
   seen|=orbit;out.append((C,pairs,lengths));count+=1
  assert labeled==len(seen)
  print('INDEPENDENT_CATALOGUE',lengths,labeled,count,flush=True)
 return out
cat=catalogue();assert len(cat)==441
F7=GF(7);rows=[];eligible=[]
for index,(C,pairs,lengths) in enumerate(cat):
 sig=[0]*12;Q=matrix(ZZ,12)
 for a,b in pairs:sig[a]=b;sig[b]=a;Q[a,b]=Q[b,a]=1
 K=(identity_matrix(ZZ,12)-C+2*Q-2*ones_matrix(ZZ,12)).change_ring(F7)
 rk=K.rank();piv=list(K.pivots());disc=K.matrix_from_rows_and_columns(piv,piv).det();char=1 if disc.is_square() else -1
 r=7+rk;t=18-r
 eps=1 if r%2 else (0 if char==(-1)**(r//2) else 2)
 lower=18+t+eps
 if lower-2*t<=16 and r<=16:eligible.append(index)
 rows.append([index,r,int(disc),char,t,eps,lower])
print('INDEPENDENT_WITT_HIST',json.dumps(sorted((str(k),v) for k,v in Counter(tuple(r[1:2]+r[3:]) for r in rows).items())),flush=True)
assert eligible==[202,246,277,281,300,303,309,360,389],eligible
print('G16_ELIGIBLE',eligible,flush=True)

def data(index):
 C,pairs,lengths=cat[index];s=[0]*12;mu=[0]*12;tau=[0]*12
 for a,b in pairs:s[a]=b;s[b]=a
 for a in range(12):
  mu[a]=next(b for b in range(12) if C[a,b]==1)
  tau[a]=next(b for b in range(12) if C[a,b]==-1)
 Q=matrix(F7,12,lambda a,b:int(s[a]==b))
 K=identity_matrix(F7,12)-C.change_ring(F7)+2*Q-2*ones_matrix(F7,12)
 ker=K.right_kernel();basis=[]
 for v in ker.basis():
  w=v-sum(v)/F7(12)*vector(F7,[1]*12)
  if vector_space_span(basis+[w],F7).dimension()>len(basis):basis.append(w)
 E=[e for e in combinations(range(12),2) if e[1]!=mu[e[0]]]
 roots=[e for e in combinations(range(12),2) if e[1]!=s[e[0]]]
 flip=lambda z:tuple(sorted(s[a] for a in z))
 Z=[z for z in roots if z<flip(z)]
 k2=matrix(ZZ,12,lambda a,b:2-int(a==b)-int(b==s[a])-int(b==mu[a])-int(b==tau[s[a]]))
 k3=matrix(ZZ,12,lambda a,b:2-int(b==tau[a])-int(b==s[a])-int(b==tau[mu[a]])-int(b==mu[tau[a]]))
 return s,mu,tau,[tuple(map(int,p)) for p in basis],E,Z,[list(map(int,row)) for row in k2.rows()],[list(map(int,row)) for row in k3.rows()],flip

def vector_space_span(rows,field):
 return matrix(field,len(rows),12,list(sum((list(row) for row in rows),[]))).row_space()

counts=[]
for index in eligible:
 s,mu,tau,basis,E,Z,k2,k3,flip=data(index);domains=[];wedges=[]
 for z in Z:
  sz=flip(z);options=[]
  for e in E:
   if any(k2[a][b]==0 for a in z for b in e):continue
   for f in E:
    if e==f or any(k2[a][b]==0 for a in sz for b in f):continue
    if any(k3[a][b]==0 for a in e for b in f) or (set(e)&set(f) and k3[min(set(e)&set(f))][min(set(e)&set(f))]<2):continue
    if any((sum(p[a] for a in e)-sum(p[a] for a in f)+2*(sum(p[a] for a in z)-sum(p[a] for a in sz)))%7 for p in basis):continue
    options.append((e,f))
  domains.append(options);wedges.append(any(set(e)&set(f) for e,f in options))
 ans={'index':index,'torsion':len(basis),'columns':sum(map(len,domains)),'empty':[list(Z[k]) for k,x in enumerate(domains) if not x],'wedgeable':sum(wedges),'sizes':list(map(len,domains))}
 counts.append(ans);print('INDEPENDENT_DOMAINS',json.dumps(ans),flush=True)
 if index not in [246,277,300]:assert ans['empty']
 if index in [277,300]:assert ans['wedgeable']==6<12
 if index==246:
  assert ans['columns']==1994
  price=cert['price'];alpha=cert['dual_left'];beta=cert['dual_right']
  assert len(price)==348 and len(alpha)==len(beta)==30 and len(set(alpha[12:]))==1
  ei={e:k for k,e in enumerate(E)};checked=0;maxlhs=-10**9
  for k,options in enumerate(domains):
   z=Z[k];sz=flip(z)
   for e,f in options:
    shared=set(e)&set(f)
    lhs=price[ei[e]]+price[ei[f]]+beta[k]+(alpha[next(iter(shared))] if shared else alpha[12])
    lhs+=sum(price[60+12*a+b] for a in z for b in e)+sum(price[60+12*a+b] for a in sz for b in f)
    lhs+=sum(price[204+12*a+b] for a in e for b in f)+sum(price[204+12*a+b] for a in f for b in e)
    assert lhs<=0,(k,e,f,lhs)
    checked+=1;maxlhs=max(maxlhs,lhs)
  bound=sum(price[:60])+sum(price[60+12*a+b]*k2[a][b]+price[204+12*a+b]*k3[a][b] for a in range(12) for b in range(12))+sum(alpha)+sum(beta)
  assert bound==90 and bound>0
  print('INDEPENDENT_CERTIFICATE',json.dumps({'columns_checked':checked,'bound':int(bound),'max_column_lhs':int(maxlhs),'verified':True}),flush=True)
print('G16_NO_PRISM_EXCLUDED',True,flush=True)

````


---

## Annexe — chercher_certificat_246.py

````python
from sage.all import *
import numpy as np,json,time
from itertools import combinations
from collections import Counter
pairs=[(0,3),(1,4),(2,6),(5,9),(7,10),(8,11)]
s=list(range(12))
for a,b in pairs:s[a]=b;s[b]=a
mu=[i^1 for i in range(12)]
tau=[11,2,1,4,3,6,5,8,7,10,9,0]
F=[[-1,-2,-2,2,-2,3,3,2,-3,3,2,2],[-1,0,-1,1,0,1,1,0,1,-1,0,-1]]
E=[e for e in combinations(range(12),2) if mu[e[0]]!=e[1]]
R=[e for e in combinations(range(12),2) if s[e[0]]!=e[1]]
flip=lambda e:tuple(sorted(s[a] for a in e))
Z=[z for z in R if z<flip(z)]
EI={e:i for i,e in enumerate(E)}
K2=[[2-int(a==b)-int(b==s[a])-int(b==mu[a])-int(b==tau[s[a]]) for b in range(12)] for a in range(12)]
K3=[[2-int(b==tau[a])-int(b==s[a])-int(b==tau[mu[a]])-int(b==mu[tau[a]]) for b in range(12)] for a in range(12)]
cols=[];weights=[];by=[{} for z in Z]
for k,z in enumerate(Z):
 sz=flip(z)
 for e in E:
  if any(K2[a][b]<1 for a in z for b in e):continue
  for f in E:
   if e==f or any(K2[a][b]<1 for a in sz for b in f):continue
   counts=Counter((b,d) for b in e for d in f)
   counts.update((b,d) for b in f for d in e)
   if any(n>K3[b][d] for (b,d),n in counts.items()):continue
   qs=[sum(p[a] for a in e)-sum(p[a] for a in f)+2*(sum(p[a] for a in z)-sum(p[a] for a in sz)) for p in F]
   if any(q%7 for q in qs):continue
   qs=[q//7 for q in qs]
   row=[0]*348;row[EI[e]]=1;row[EI[f]]=1
   for a in z:
    for b in e:row[60+12*a+b]+=1
   for a in sz:
    for b in f:row[60+12*a+b]+=1
   for a in e:
    for b in f:row[204+12*a+b]+=1
   for a in f:
    for b in e:row[204+12*a+b]+=1
   shared=set(e)&set(f);center=next(iter(shared)) if shared else -1
   by[k].setdefault(center,[]).append(len(cols));cols.append(row);weights.append(qs)
C=np.array(cols,dtype=np.int64);charges=np.array(weights,dtype=np.int64)
target=np.array([1]*60+sum(K2,[])+sum(K3,[]),dtype=np.int64)
def assignment(cost):
 n=len(cost);u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
 for i in range(1,n+1):
  p[0]=i;j0=0;mn=[10**12]*(n+1);used=[False]*(n+1)
  while True:
   used[j0]=True;i0=p[j0];delta=10**12;j1=0
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
 return val,match,u[1:],v[1:]
def qform(p):
 quad=lambda M,x,y:sum(x[a]*M[a][b]*y[b] for a in range(12) for b in range(12))
 GO=[[9*int(a==b)+1-int(b==mu[a]) for b in range(12)] for a in range(12)]
 GI=[[9*int(a==b)+1-int(b==s[a]) for b in range(12)] for a in range(12)]
 GR=[[1-int(a==b)+9*int(b==s[a]) for b in range(12)] for a in range(12)]
 df=[p[a]-p[s[a]] for a in range(12)]
 n=quad(GO,p,p)-quad(K3,p,p)+4*(quad(GI,p,p)-quad(GR,p,p))+4*quad(K2,df,p)
 assert n%49==0
 return n//49
print('DOMAIN',len(cols),'ENERGIES',list(map(qform,F)),flush=True)
results=[]
for aa,bb in [(0,0),(0,1),(1,0),(1,-1),(1,1),(1,-2),(1,2)]:
 psi=[aa*F[0][i]+bb*F[1][i] for i in range(12)];energy=qform(psi);W=1000*(aa*charges[:,0]+bb*charges[:,1])**2
 price=np.zeros(348,dtype=np.int64);best=-10**30;cert=None;start=time.time()
 for it in range(500):
  values=W-C@price;dc=[[10**10]*30 for k in range(30)];arg={}
  for k,dct in enumerate(by):
   for b,idxs in dct.items():
    j=min(idxs,key=lambda j:int(values[j]));cost=int(values[j])
    for row in ([b] if b>=0 else range(12,30)):dc[row][k]=cost;arg[row,k]=j
  val,matching,du,dv=assignment(dc);bound=val+int(target@price)
  if bound>best:best=bound;cert={'price':list(map(int,price)),'dual_left':du,'dual_right':dv,'bound':int(bound),'iteration':int(it)}
  if bound>1000*energy:break
  chosen=[arg[r,k] for r,k in enumerate(matching)];usage=C[chosen].sum(axis=0);grad=target-usage;norm=int(grad@grad)
  if not norm:break
  step=max(1,int((1000*energy-bound)//max(1,norm)))
  price+=step*grad
  if time.time()-start>12:break
 ans={'weights':[int(aa),int(bb)],'energy':int(energy),'bound':int(best),'excluded':bool(best>1000*energy),'iterations':int(it+1)}
 if ans['excluded']:
  vals=W-C@np.array(cert['price'],dtype=np.int64)
  for k,dct in enumerate(by):
   for b,idxs in dct.items():
    for row in ([b] if b>=0 else range(12,30)):
     assert all(int(vals[j])>=cert['dual_left'][row]+cert['dual_right'][k] for j in idxs)
  ans['certificate']=cert
 results.append(ans);print('CERT246',json.dumps(ans),flush=True)
 if ans['excluded']:break
print('DONE',flush=True)

````


---

## Annexe — controles_positifs.py

````python
from itertools import product,combinations
import json
D5=[(1,0,0,0,0),(2,0,0,0,0),(0,1,0,0,0),(0,2,0,0,0),(0,0,1,0,0),(0,0,2,0,0),(0,0,0,1,0),(0,0,0,2,0),(0,0,0,0,1),(0,0,0,0,2),(1,0,2,1,2),(2,0,1,2,1),(2,1,1,1,2),(1,2,2,2,1),(2,2,2,0,2),(1,1,1,0,1),(2,2,0,1,1),(1,1,0,2,2),(1,2,1,1,0),(2,1,2,2,0),(0,1,2,1,1),(0,2,1,2,2)]
def check(dim,D):
 V=list(product(range(3),repeat=dim));ds=set(D);zero=(0,)*dim
 add=lambda a,b:tuple((x+y)%3 for x,y in zip(a,b))
 neg=lambda a:tuple(-x%3 for x in a)
 adj=lambda a,b:add(a,neg(b)) in ds
 nbr={a:{add(a,d) for d in D} for a in V}
 for a in V:
  for b in V:
   if a!=b:assert len(nbr[a]&nbr[b])==(1 if adj(a,b) else 2)
 c=D[0];nc=neg(c);labels=[d for d in D if d not in (c,nc)];n=len(labels)
 stars=[add(c,a) for a in labels]
 s=[labels.index(neg(a)) for a in labels]
 mu=[];tau=[]
 for w in stars:
  p=[b for b,v in enumerate(stars) if adj(w,v)]
  q=[b for b,v in enumerate(stars) if adj(w,neg(v))]
  assert len(p)==len(q)==1
  mu.append(p[0]);tau.append(q[0])
 roots=[e for e in combinations(range(n),2) if e[1]!=s[e[0]]]
 far=[add(labels[a],labels[b]) for a,b in roots]
 assert len(set(far))==len(far)
 shadows={z:tuple(b for b,w in enumerate(stars) if adj(z,w)) for z in far}
 expected={e for e in combinations(range(n),2) if e[1]!=mu[e[0]]}
 assert set(shadows.values())==expected and len(shadows)==len(expected)
 k2=[[2-int(a==b)-int(b==s[a])-int(b==mu[a])-int(b==tau[s[a]]) for b in range(n)] for a in range(n)]
 k3=[[2-int(b==tau[a])-int(b==s[a])-int(b==tau[mu[a]])-int(b==mu[tau[a]]) for b in range(n)] for a in range(n)]
 for a in range(n):
  for b in range(n):
   got2=sum(a in e and b in shadows[z] for e,z in zip(roots,far))
   got3=sum(a in shadows[z] and b in shadows[neg(z)] for z in far)
   assert got2==k2[a][b],('K2',a,b,got2,k2[a][b])
   assert got3==k3[a][b],('K3',a,b,got3,k3[a][b])
 print('POSITIVE_CONTROL',json.dumps({'vertices':len(V),'labels':n,'far_roots':len(far),'SRG':True,'shadow_bijection':True,'K2_K3_entries_checked':2*n*n}),flush=True)
check(2,[(1,0),(2,0),(0,1),(0,2)])
check(5,D5)
print('CONTROLS_COMPLETE',True)

````


---

## Annexe — sorties_decouverte.txt

````text
DOMAIN 1994 ENERGIES [60, 16]
CERT246 {"weights":[0,0],"energy":0,"bound":90,"excluded":true,"iterations":11,"certificate":{"price":[-8,9,-8,7,6,4,7,-6,3,-17,-1,3,3,-1,1,3,-4,-1,0,1,2,8,8,-1,9,-10,0,-6,3,-6,-16,-1,-1,7,-4,6,2,2,-7,4,2,2,-10,0,-12,7,-2,8,-8,8,1,7,3,-4,3,-3,2,7,-2,-9,-6,-5,-3,1,0,5,5,-2,3,-3,4,1,-4,-4,-1,-3,-4,-1,1,4,5,-1,5,3,-5,0,-6,-1,1,2,3,3,7,-3,3,-4,-2,6,1,-8,3,-4,-1,5,-3,3,1,-1,1,-3,-3,1,-2,-5,0,3,2,1,4,1,4,2,6,-4,-3,-9,-2,7,-5,2,-3,5,5,-3,2,-5,3,-3,-8,-1,0,8,-1,3,0,4,2,6,4,0,-6,-3,1,-7,-3,2,0,4,3,-5,1,-2,-2,7,-9,1,4,-2,1,0,2,11,4,6,2,-3,-3,-12,0,-8,3,4,2,2,1,2,-1,-3,-4,0,-3,-3,-3,3,-3,5,2,7,7,-5,-2,-1,-5,-5,0,6,3,-12,3,-7,-1,2,-5,9,-6,2,6,0,-5,-3,2,3,0,1,-1,5,2,-2,3,-5,0,-1,-4,-5,-5,4,-2,8,1,8,-12,-3,-1,0,0,4,8,2,7,-7,4,-2,3,2,-4,0,0,4,1,3,-1,1,4,-3,-7,3,-5,4,4,0,4,-1,7,-10,3,-4,-1,0,-5,8,1,4,0,-1,2,-10,3,-3,2,1,4,2,3,-1,-1,0,1,-1,0,2,-5,-1,-2,7,-1,7,2,1,0,-5,0,-11,9,5,8,-7,1,-10,-10,-1,-5,0,-6,4,-6,2,1,4,4,3,3,0,0,-6,0,1,2,-2,8,-2,-3,-4,-3,2,-11,4,1,0],"dual_left":[62,49,50,54,42,56,58,47,53,47,46,59,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25],"dual_right":[-3,-78,-3,-77,-83,0,-79,-82,-1,-82,-14,-11,-7,-69,-1,-10,-69,-4,-73,-11,-75,-74,-10,-81,-16,-81,-9,-83,-13,-9],"bound":90,"iteration":10}}
DONE

````


---

## Annexe — sorties_independantes.txt

````text
INDEPENDENT_CATALOGUE (12,) 3326 362
INDEPENDENT_CATALOGUE (6, 6) 3328 79
INDEPENDENT_WITT_HIST [["(15, -1, 3, 1, 22)", 1], ["(16, -1, 2, 2, 22)", 13], ["(16, 1, 2, 0, 20)", 8], ["(17, -1, 1, 1, 20)", 16], ["(17, 1, 1, 1, 20)", 58], ["(18, -1, 0, 0, 18)", 142], ["(18, 1, 0, 2, 20)", 203]]
G16_ELIGIBLE [202, 246, 277, 281, 300, 303, 309, 360, 389]
INDEPENDENT_DOMAINS {"index": 202, "torsion": 2, "columns": 1872, "empty": [[0, 3], [0, 6], [0, 9], [1, 7], [1, 8], [3, 6]], "wedgeable": 8, "sizes": [154, 0, 12, 18, 0, 154, 213, 0, 12, 18, 278, 24, 24, 154, 0, 0, 24, 24, 24, 24, 0, 154, 24, 24, 278, 12, 18, 175, 18, 12]}
INDEPENDENT_DOMAINS {"index": 246, "torsion": 2, "columns": 1994, "empty": [], "wedgeable": 14, "sizes": [26, 99, 26, 123, 122, 26, 108, 114, 26, 98, 31, 31, 31, 98, 26, 31, 98, 26, 122, 31, 123, 98, 31, 114, 31, 99, 31, 122, 26, 26]}
INDEPENDENT_CERTIFICATE {"columns_checked": 1994, "bound": 90, "max_column_lhs": 0, "verified": true}
INDEPENDENT_DOMAINS {"index": 277, "torsion": 2, "columns": 1860, "empty": [], "wedgeable": 6, "sizes": [39, 16, 39, 39, 240, 16, 39, 160, 16, 16, 16, 160, 39, 16, 39, 39, 240, 16, 16, 39, 240, 16, 39, 160, 16, 39, 39, 16, 16, 39]}
INDEPENDENT_DOMAINS {"index": 281, "torsion": 3, "columns": 211, "empty": [[1, 2], [1, 11], [2, 4], [4, 11]], "wedgeable": 0, "sizes": [6, 3, 6, 6, 21, 3, 6, 10, 3, 3, 0, 14, 3, 3, 3, 6, 34, 0, 0, 34, 6, 3, 3, 14, 3, 3, 6, 0, 3, 6]}
INDEPENDENT_DOMAINS {"index": 300, "torsion": 2, "columns": 1860, "empty": [], "wedgeable": 6, "sizes": [39, 16, 39, 39, 240, 16, 39, 160, 16, 16, 16, 160, 39, 16, 240, 39, 39, 16, 16, 39, 39, 240, 16, 160, 16, 39, 39, 16, 16, 39]}
INDEPENDENT_DOMAINS {"index": 303, "torsion": 2, "columns": 2303, "empty": [[0, 5], [0, 6], [0, 11], [1, 7], [1, 10], [6, 11]], "wedgeable": 8, "sizes": [187, 36, 24, 0, 0, 187, 36, 24, 296, 0, 36, 24, 187, 0, 36, 24, 0, 296, 296, 36, 36, 187, 24, 24, 24, 24, 36, 36, 187, 0]}
INDEPENDENT_DOMAINS {"index": 309, "torsion": 2, "columns": 2023, "empty": [[0, 5], [0, 6], [0, 11], [1, 7], [1, 10], [5, 11]], "wedgeable": 8, "sizes": [201, 18, 24, 0, 0, 171, 18, 24, 227, 0, 24, 24, 227, 0, 24, 24, 0, 227, 238, 24, 18, 171, 24, 24, 24, 24, 24, 18, 201, 0]}
INDEPENDENT_DOMAINS {"index": 360, "torsion": 2, "columns": 2340, "empty": [[0, 3], [0, 5], [0, 6], [0, 9], [0, 11], [1, 2], [1, 4], [1, 8], [1, 10], [2, 5], [2, 8], [2, 11], [3, 4], [3, 10], [4, 10]], "wedgeable": 3, "sizes": [636, 36, 0, 36, 0, 0, 36, 0, 36, 0, 0, 36, 0, 36, 0, 36, 0, 36, 636, 36, 0, 0, 36, 0, 0, 36, 0, 36, 636, 0]}
INDEPENDENT_DOMAINS {"index": 389, "torsion": 2, "columns": 1872, "empty": [[0, 3], [0, 6], [0, 9], [1, 7], [1, 8], [3, 9]], "wedgeable": 8, "sizes": [154, 0, 12, 18, 0, 213, 154, 0, 18, 12, 278, 24, 24, 0, 0, 154, 24, 24, 24, 24, 154, 0, 24, 24, 278, 18, 12, 175, 12, 18]}
G16_NO_PRISM_EXCLUDED True

````


---

## Annexe — sorties_controles.txt

````text
POSITIVE_CONTROL {"vertices": 9, "labels": 2, "far_roots": 0, "SRG": true, "shadow_bijection": true, "K2_K3_entries_checked": 8}
POSITIVE_CONTROL {"vertices": 243, "labels": 20, "far_roots": 180, "SRG": true, "shadow_bijection": true, "K2_K3_entries_checked": 800}
CONTROLS_COMPLETE True

````


---

## Annexe — verification_JS_certificat.json

````json
{
  "columns": 1994,
  "maxLhs": 0,
  "bound": 90
}
````


---

## Annexe — donnees_type_246.json

````json
{
  "index": 246,
  "s": [
    3,
    4,
    6,
    0,
    1,
    9,
    2,
    10,
    11,
    5,
    7,
    8
  ],
  "mu": [
    1,
    0,
    3,
    2,
    5,
    4,
    7,
    6,
    9,
    8,
    11,
    10
  ],
  "tau": [
    11,
    2,
    1,
    4,
    3,
    6,
    5,
    8,
    7,
    10,
    9,
    0
  ],
  "basis": [
    [
      6,
      5,
      5,
      2,
      5,
      3,
      3,
      2,
      4,
      3,
      2,
      2
    ],
    [
      6,
      0,
      6,
      1,
      0,
      1,
      1,
      0,
      1,
      6,
      0,
      6
    ]
  ],
  "K2": [
    [
      1,
      1,
      2,
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2,
      2
    ],
    [
      1,
      1,
      2,
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2,
      2
    ],
    [
      2,
      2,
      1,
      1,
      2,
      1,
      1,
      2,
      2,
      2,
      2,
      2
    ],
    [
      1,
      2,
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      1
    ],
    [
      2,
      1,
      1,
      2,
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2
    ],
    [
      2,
      2,
      2,
      2,
      1,
      1,
      2,
      2,
      2,
      1,
      1,
      2
    ],
    [
      2,
      1,
      1,
      2,
      2,
      2,
      1,
      1,
      2,
      2,
      2,
      2
    ],
    [
      2,
      2,
      2,
      2,
      2,
      2,
      1,
      1,
      2,
      1,
      1,
      2
    ],
    [
      1,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      1,
      1,
      2,
      1
    ],
    [
      2,
      2,
      2,
      2,
      2,
      1,
      1,
      2,
      1,
      1,
      2,
      2
    ],
    [
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      1,
      1,
      2,
      1,
      1
    ],
    [
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      1,
      1,
      2,
      1,
      1
    ]
  ],
  "K3": [
    [
      2,
      2,
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2,
      1,
      1
    ],
    [
      2,
      2,
      1,
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2,
      1
    ],
    [
      1,
      1,
      2,
      2,
      1,
      2,
      1,
      2,
      2,
      2,
      2,
      2
    ],
    [
      1,
      1,
      2,
      2,
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2
    ],
    [
      2,
      1,
      1,
      1,
      2,
      2,
      1,
      2,
      2,
      2,
      2,
      2
    ],
    [
      2,
      2,
      2,
      1,
      2,
      2,
      1,
      1,
      2,
      1,
      2,
      2
    ],
    [
      2,
      2,
      1,
      2,
      1,
      1,
      2,
      2,
      1,
      2,
      2,
      2
    ],
    [
      2,
      2,
      2,
      2,
      2,
      1,
      2,
      2,
      1,
      1,
      1,
      2
    ],
    [
      2,
      2,
      2,
      2,
      2,
      2,
      1,
      1,
      2,
      2,
      1,
      1
    ],
    [
      2,
      2,
      2,
      2,
      2,
      1,
      2,
      1,
      2,
      2,
      1,
      1
    ],
    [
      1,
      2,
      2,
      2,
      2,
      2,
      2,
      1,
      1,
      1,
      2,
      2
    ],
    [
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2,
      1,
      1,
      2,
      2
    ]
  ],
  "pairs": [
    [
      [
        0,
        1
      ],
      [
        3,
        4
      ]
    ],
    [
      [
        0,
        2
      ],
      [
        3,
        6
      ]
    ],
    [
      [
        0,
        4
      ],
      [
        1,
        3
      ]
    ],
    [
      [
        0,
        5
      ],
      [
        3,
        9
      ]
    ],
    [
      [
        0,
        6
      ],
      [
        2,
        3
      ]
    ],
    [
      [
        0,
        7
      ],
      [
        3,
        10
      ]
    ],
    [
      [
        0,
        8
      ],
      [
        3,
        11
      ]
    ],
    [
      [
        0,
        9
      ],
      [
        3,
        5
      ]
    ],
    [
      [
        0,
        10
      ],
      [
        3,
        7
      ]
    ],
    [
      [
        0,
        11
      ],
      [
        3,
        8
      ]
    ],
    [
      [
        1,
        2
      ],
      [
        4,
        6
      ]
    ],
    [
      [
        1,
        5
      ],
      [
        4,
        9
      ]
    ],
    [
      [
        1,
        6
      ],
      [
        2,
        4
      ]
    ],
    [
      [
        1,
        7
      ],
      [
        4,
        10
      ]
    ],
    [
      [
        1,
        8
      ],
      [
        4,
        11
      ]
    ],
    [
      [
        1,
        9
      ],
      [
        4,
        5
      ]
    ],
    [
      [
        1,
        10
      ],
      [
        4,
        7
      ]
    ],
    [
      [
        1,
        11
      ],
      [
        4,
        8
      ]
    ],
    [
      [
        2,
        5
      ],
      [
        6,
        9
      ]
    ],
    [
      [
        2,
        7
      ],
      [
        6,
        10
      ]
    ],
    [
      [
        2,
        8
      ],
      [
        6,
        11
      ]
    ],
    [
      [
        2,
        9
      ],
      [
        5,
        6
      ]
    ],
    [
      [
        2,
        10
      ],
      [
        6,
        7
      ]
    ],
    [
      [
        2,
        11
      ],
      [
        6,
        8
      ]
    ],
    [
      [
        5,
        7
      ],
      [
        9,
        10
      ]
    ],
    [
      [
        5,
        8
      ],
      [
        9,
        11
      ]
    ],
    [
      [
        5,
        10
      ],
      [
        7,
        9
      ]
    ],
    [
      [
        5,
        11
      ],
      [
        8,
        9
      ]
    ],
    [
      [
        7,
        8
      ],
      [
        10,
        11
      ]
    ],
    [
      [
        7,
        11
      ],
      [
        8,
        10
      ]
    ]
  ],
  "shadows": [
    [
      0,
      2
    ],
    [
      0,
      3
    ],
    [
      0,
      4
    ],
    [
      0,
      5
    ],
    [
      0,
      6
    ],
    [
      0,
      7
    ],
    [
      0,
      8
    ],
    [
      0,
      9
    ],
    [
      0,
      10
    ],
    [
      0,
      11
    ],
    [
      1,
      2
    ],
    [
      1,
      3
    ],
    [
      1,
      4
    ],
    [
      1,
      5
    ],
    [
      1,
      6
    ],
    [
      1,
      7
    ],
    [
      1,
      8
    ],
    [
      1,
      9
    ],
    [
      1,
      10
    ],
    [
      1,
      11
    ],
    [
      2,
      4
    ],
    [
      2,
      5
    ],
    [
      2,
      6
    ],
    [
      2,
      7
    ],
    [
      2,
      8
    ],
    [
      2,
      9
    ],
    [
      2,
      10
    ],
    [
      2,
      11
    ],
    [
      3,
      4
    ],
    [
      3,
      5
    ],
    [
      3,
      6
    ],
    [
      3,
      7
    ],
    [
      3,
      8
    ],
    [
      3,
      9
    ],
    [
      3,
      10
    ],
    [
      3,
      11
    ],
    [
      4,
      6
    ],
    [
      4,
      7
    ],
    [
      4,
      8
    ],
    [
      4,
      9
    ],
    [
      4,
      10
    ],
    [
      4,
      11
    ],
    [
      5,
      6
    ],
    [
      5,
      7
    ],
    [
      5,
      8
    ],
    [
      5,
      9
    ],
    [
      5,
      10
    ],
    [
      5,
      11
    ],
    [
      6,
      8
    ],
    [
      6,
      9
    ],
    [
      6,
      10
    ],
    [
      6,
      11
    ],
    [
      7,
      8
    ],
    [
      7,
      9
    ],
    [
      7,
      10
    ],
    [
      7,
      11
    ],
    [
      8,
      10
    ],
    [
      8,
      11
    ],
    [
      9,
      10
    ],
    [
      9,
      11
    ]
  ]
}
````


---

## Annexe — domaines_neuf_types.json

````json
[
  {
    "index": 202,
    "t": 2,
    "empty": [
      [
        0,
        3
      ],
      [
        0,
        6
      ],
      [
        0,
        9
      ],
      [
        1,
        7
      ],
      [
        1,
        8
      ],
      [
        3,
        6
      ]
    ],
    "wedgeable": 8,
    "domain_sizes": [
      154,
      0,
      12,
      18,
      0,
      154,
      213,
      0,
      12,
      18,
      278,
      24,
      24,
      154,
      0,
      0,
      24,
      24,
      24,
      24,
      0,
      154,
      24,
      24,
      278,
      12,
      18,
      175,
      18,
      12
    ]
  },
  {
    "index": 246,
    "t": 2,
    "empty": [],
    "wedgeable": 14,
    "domain_sizes": [
      26,
      99,
      26,
      123,
      122,
      26,
      108,
      114,
      26,
      98,
      31,
      31,
      31,
      98,
      26,
      31,
      98,
      26,
      122,
      31,
      123,
      98,
      31,
      114,
      31,
      99,
      31,
      122,
      26,
      26
    ]
  },
  {
    "index": 277,
    "t": 2,
    "empty": [],
    "wedgeable": 6,
    "domain_sizes": [
      39,
      16,
      39,
      39,
      240,
      16,
      39,
      160,
      16,
      16,
      16,
      160,
      39,
      16,
      39,
      39,
      240,
      16,
      16,
      39,
      240,
      16,
      39,
      160,
      16,
      39,
      39,
      16,
      16,
      39
    ]
  },
  {
    "index": 281,
    "t": 3,
    "empty": [
      [
        1,
        2
      ],
      [
        1,
        11
      ],
      [
        2,
        4
      ],
      [
        4,
        11
      ]
    ],
    "wedgeable": 0,
    "domain_sizes": [
      6,
      3,
      6,
      6,
      21,
      3,
      6,
      10,
      3,
      3,
      0,
      14,
      3,
      3,
      3,
      6,
      34,
      0,
      0,
      34,
      6,
      3,
      3,
      14,
      3,
      3,
      6,
      0,
      3,
      6
    ]
  },
  {
    "index": 300,
    "t": 2,
    "empty": [],
    "wedgeable": 6,
    "domain_sizes": [
      39,
      16,
      39,
      39,
      240,
      16,
      39,
      160,
      16,
      16,
      16,
      160,
      39,
      16,
      240,
      39,
      39,
      16,
      16,
      39,
      39,
      240,
      16,
      160,
      16,
      39,
      39,
      16,
      16,
      39
    ]
  },
  {
    "index": 303,
    "t": 2,
    "empty": [
      [
        0,
        5
      ],
      [
        0,
        6
      ],
      [
        0,
        11
      ],
      [
        1,
        7
      ],
      [
        1,
        10
      ],
      [
        6,
        11
      ]
    ],
    "wedgeable": 8,
    "domain_sizes": [
      187,
      36,
      24,
      0,
      0,
      187,
      36,
      24,
      296,
      0,
      36,
      24,
      187,
      0,
      36,
      24,
      0,
      296,
      296,
      36,
      36,
      187,
      24,
      24,
      24,
      24,
      36,
      36,
      187,
      0
    ]
  },
  {
    "index": 309,
    "t": 2,
    "empty": [
      [
        0,
        5
      ],
      [
        0,
        6
      ],
      [
        0,
        11
      ],
      [
        1,
        7
      ],
      [
        1,
        10
      ],
      [
        5,
        11
      ]
    ],
    "wedgeable": 8,
    "domain_sizes": [
      201,
      18,
      24,
      0,
      0,
      171,
      18,
      24,
      227,
      0,
      24,
      24,
      227,
      0,
      24,
      24,
      0,
      227,
      238,
      24,
      18,
      171,
      24,
      24,
      24,
      24,
      24,
      18,
      201,
      0
    ]
  },
  {
    "index": 360,
    "t": 2,
    "empty": [
      [
        0,
        3
      ],
      [
        0,
        5
      ],
      [
        0,
        6
      ],
      [
        0,
        9
      ],
      [
        0,
        11
      ],
      [
        1,
        2
      ],
      [
        1,
        4
      ],
      [
        1,
        8
      ],
      [
        1,
        10
      ],
      [
        2,
        5
      ],
      [
        2,
        8
      ],
      [
        2,
        11
      ],
      [
        3,
        4
      ],
      [
        3,
        10
      ],
      [
        4,
        10
      ]
    ],
    "wedgeable": 3,
    "domain_sizes": [
      636,
      36,
      0,
      36,
      0,
      0,
      36,
      0,
      36,
      0,
      0,
      36,
      0,
      36,
      0,
      36,
      0,
      36,
      636,
      36,
      0,
      0,
      36,
      0,
      0,
      36,
      0,
      36,
      636,
      0
    ]
  },
  {
    "index": 389,
    "t": 2,
    "empty": [
      [
        0,
        3
      ],
      [
        0,
        6
      ],
      [
        0,
        9
      ],
      [
        1,
        7
      ],
      [
        1,
        8
      ],
      [
        3,
        9
      ]
    ],
    "wedgeable": 8,
    "domain_sizes": [
      154,
      0,
      12,
      18,
      0,
      213,
      154,
      0,
      18,
      12,
      278,
      24,
      24,
      0,
      0,
      154,
      24,
      24,
      24,
      24,
      154,
      0,
      24,
      24,
      278,
      18,
      12,
      175,
      12,
      18
    ]
  }
]
````


## Annexe — catalogue_441.json (JSON compact, complet)

````json
[{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,7],[8,10],[9,11]],"orbit_size":2},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,8],[7,10],[9,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,9],[7,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,9],[7,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,10],[7,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,11],[7,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,7],[5,9],[6,10],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,7],[5,9],[6,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,7],[5,10],[6,9],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,7],[5,11],[6,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,8],[5,9],[6,10],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,8],[5,9],[6,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,8],[5,10],[6,9],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,8],[5,10],[6,11],[7,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,8],[5,11],[6,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,8],[5,11],[6,10],[7,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,9],[5,7],[6,11],[8,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,9],[5,8],[6,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,9],[5,11],[6,8],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,10],[5,11],[6,8],[7,9]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,11],[5,7],[6,9],[8,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,11],[5,8],[6,9],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,11],[5,8],[6,10],[7,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,11],[5,10],[6,8],[7,9]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,5],[6,8],[7,10],[9,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,5],[6,9],[7,10],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,5],[6,9],[7,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,5],[6,11],[7,9],[8,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,8],[7,10],[9,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,9],[7,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,9],[7,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,10],[7,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,11],[7,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,7],[5,8],[6,10],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,7],[5,9],[6,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,7],[5,9],[6,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,7],[5,10],[6,8],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,7],[5,10],[6,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,7],[5,11],[6,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,8],[5,7],[6,10],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,8],[5,9],[6,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,8],[5,9],[6,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,8],[5,10],[6,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,8],[5,10],[6,11],[7,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,8],[5,11],[6,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,8],[5,11],[6,10],[7,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,9],[5,7],[6,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,9],[5,7],[6,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,9],[5,8],[6,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,9],[5,8],[6,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,9],[5,10],[6,8],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,9],[5,11],[6,8],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,10],[5,7],[6,8],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,10],[5,7],[6,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,10],[5,8],[6,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,10],[5,8],[6,11],[7,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,10],[5,9],[6,8],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,11],[5,7],[6,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,11],[5,8],[6,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,11],[5,8],[6,10],[7,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,11],[5,9],[6,8],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,6],[4,9],[7,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,6],[4,9],[7,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,6],[4,10],[7,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,6],[4,11],[7,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,7],[4,8],[6,10],[9,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,7],[4,9],[6,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,7],[4,9],[6,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,7],[4,10],[6,8],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,7],[4,10],[6,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,7],[4,11],[6,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,8],[4,7],[6,10],[9,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,8],[4,9],[6,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,8],[4,9],[6,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,8],[4,10],[6,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,8],[4,10],[6,11],[7,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,8],[4,11],[6,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,8],[4,11],[6,10],[7,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,9],[4,6],[7,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,9],[4,6],[7,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,9],[4,7],[6,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,9],[4,7],[6,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,9],[4,8],[6,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,9],[4,8],[6,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,9],[4,10],[6,8],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,10],[4,6],[7,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,10],[4,7],[6,8],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,10],[4,7],[6,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,10],[4,8],[6,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,10],[4,8],[6,11],[7,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,10],[4,9],[6,8],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,11],[4,6],[7,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,11],[4,7],[6,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,11],[4,8],[6,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,11],[4,8],[6,10],[7,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,5],[4,9],[7,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,5],[4,9],[7,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,5],[4,10],[7,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,5],[4,11],[7,9],[8,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,8],[5,10],[9,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,9],[5,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,9],[5,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,10],[5,8],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,10],[5,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,11],[5,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,7],[5,10],[9,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,9],[5,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,9],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,7],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,11],[7,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,11],[5,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,11],[5,10],[7,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,7],[5,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,7],[5,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,8],[5,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,8],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,10],[5,7],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,10],[5,8],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,11],[5,8],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,7],[5,8],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,7],[5,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,8],[5,7],[9,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,8],[5,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,9],[5,7],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,9],[5,8],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,11],[4,7],[5,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,11],[4,8],[5,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,11],[4,9],[5,8],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,5],[4,9],[6,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,5],[4,9],[6,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,5],[4,10],[6,8],[9,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,5],[4,10],[6,9],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,6],[4,9],[5,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,6],[4,9],[5,11],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,6],[4,10],[5,8],[9,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,6],[4,10],[5,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,6],[4,11],[5,9],[8,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,8],[4,9],[5,10],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,8],[4,9],[5,11],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,8],[4,10],[5,9],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,8],[4,10],[5,11],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,8],[4,11],[5,9],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,8],[4,11],[5,10],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,9],[4,6],[5,11],[8,10]],"orbit_size":4},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,9],[4,8],[5,10],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,9],[4,8],[5,11],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,9],[4,10],[5,8],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,9],[4,10],[5,11],[6,8]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,9],[4,11],[5,8],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,9],[4,11],[5,10],[6,8]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,10],[4,8],[5,9],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,10],[4,8],[5,11],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,10],[4,9],[5,8],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,10],[4,9],[5,11],[6,8]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,10],[4,11],[5,8],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,10],[4,11],[5,9],[6,8]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,11],[4,8],[5,9],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,11],[4,8],[5,10],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,11],[4,9],[5,8],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,11],[4,10],[5,8],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,7],[3,11],[4,10],[5,9],[6,8]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,5],[4,9],[6,10],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,5],[4,9],[6,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,6],[4,9],[5,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,6],[4,9],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,6],[4,10],[5,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,6],[4,10],[5,11],[7,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,6],[4,11],[5,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,6],[4,11],[5,10],[7,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,7],[4,9],[5,10],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,7],[4,9],[5,11],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,7],[4,10],[5,9],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,7],[4,10],[5,11],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,7],[4,11],[5,9],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,7],[4,11],[5,10],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,9],[4,7],[5,10],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,9],[4,7],[5,11],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,9],[4,10],[5,7],[6,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,9],[4,11],[5,7],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,10],[4,7],[5,9],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,10],[4,7],[5,11],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,10],[4,9],[5,7],[6,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,10],[4,11],[5,7],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,11],[4,7],[5,9],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,11],[4,7],[5,10],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,11],[4,9],[5,7],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,8],[3,11],[4,10],[5,7],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,5],[4,6],[7,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,5],[4,7],[6,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,5],[4,8],[6,10],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,5],[4,8],[6,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,6],[4,7],[5,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,6],[4,8],[5,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,6],[4,8],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,6],[4,10],[5,8],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,6],[4,11],[5,8],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,7],[4,8],[5,10],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,7],[4,8],[5,11],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,7],[4,10],[5,8],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,7],[4,10],[5,11],[6,8]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,7],[4,11],[5,8],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,7],[4,11],[5,10],[6,8]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,8],[4,7],[5,10],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,8],[4,7],[5,11],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,8],[4,11],[5,7],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,10],[4,7],[5,8],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,10],[4,7],[5,11],[6,8]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,10],[4,11],[5,7],[6,8]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,11],[4,7],[5,8],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,11],[4,7],[5,10],[6,8]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,11],[4,8],[5,7],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,9],[3,11],[4,10],[5,7],[6,8]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,5],[4,6],[7,9],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,5],[4,7],[6,8],[9,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,5],[4,7],[6,9],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,6],[4,7],[5,8],[9,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,6],[4,7],[5,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,6],[4,8],[5,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,6],[4,9],[5,8],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,7],[4,8],[5,9],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,7],[4,8],[5,11],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,7],[4,9],[5,8],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,7],[4,11],[5,8],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,8],[4,7],[5,9],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,8],[4,7],[5,11],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,8],[4,11],[5,7],[6,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,9],[4,7],[5,8],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,9],[4,7],[5,11],[6,8]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,9],[4,11],[5,7],[6,8]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,11],[4,7],[5,8],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,11],[4,7],[5,9],[6,8]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,11],[4,8],[5,7],[6,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,10],[3,11],[4,9],[5,7],[6,8]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,5],[4,6],[7,9],[8,10]],"orbit_size":2},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,6],[4,8],[5,9],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,6],[4,9],[5,8],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,7],[4,8],[5,9],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,7],[4,8],[5,10],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,7],[4,9],[5,8],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,7],[4,10],[5,8],[6,9]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,8],[4,7],[5,10],[6,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,9],[4,10],[5,7],[6,8]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,10],[4,7],[5,8],[6,9]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,2],[1,11],[3,10],[4,9],[5,7],[6,8]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,5],[6,9],[7,10],[8,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,6],[5,9],[7,10],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,7],[5,9],[6,10],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,7],[5,10],[6,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,8],[5,9],[6,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,8],[5,9],[6,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,8],[5,10],[6,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,8],[5,11],[6,9],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,9],[5,8],[6,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,9],[5,8],[6,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,10],[5,8],[6,9],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,11],[5,8],[6,9],[7,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,7],[4,9],[6,10],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,7],[4,10],[6,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,8],[4,9],[6,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,8],[4,9],[6,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,8],[4,10],[6,9],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,9],[4,7],[6,10],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,9],[4,8],[6,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,9],[4,8],[6,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,10],[4,7],[6,9],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,5],[2,10],[4,8],[6,9],[7,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,7],[4,9],[5,10],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,7],[4,10],[5,9],[8,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,8],[4,9],[5,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,8],[4,9],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,8],[4,10],[5,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,8],[4,11],[5,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,9],[4,7],[5,10],[8,11]],"orbit_size":2},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,9],[4,8],[5,10],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,9],[4,8],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,9],[4,11],[5,8],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,7],[2,5],[4,10],[6,9],[8,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,7],[2,6],[4,10],[5,9],[8,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,7],[2,8],[4,9],[5,10],[6,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,7],[2,8],[4,9],[5,11],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,7],[2,8],[4,10],[5,11],[6,9]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,7],[2,8],[4,11],[5,9],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,7],[2,8],[4,11],[5,10],[6,9]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,5],[4,9],[6,10],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,5],[4,9],[6,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,6],[4,9],[5,10],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,6],[4,9],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,6],[4,10],[5,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,6],[4,11],[5,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,7],[4,9],[5,10],[6,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,7],[4,9],[5,11],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,7],[4,10],[5,11],[6,9]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,7],[4,11],[5,9],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,8],[2,7],[4,11],[5,10],[6,9]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,9],[2,5],[4,8],[6,10],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,9],[2,5],[4,8],[6,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,9],[2,6],[4,8],[5,10],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,9],[2,6],[4,8],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,9],[2,6],[4,11],[5,8],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,3],[1,10],[2,5],[4,7],[6,9],[8,11]],"orbit_size":1},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,5],[2,8],[3,9],[6,10],[7,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,5],[2,8],[3,9],[6,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,5],[2,9],[3,8],[6,10],[7,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,5],[2,9],[3,8],[6,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,8],[3,9],[5,10],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,8],[3,9],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,8],[3,10],[5,9],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,8],[3,11],[5,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,9],[3,8],[5,10],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,9],[3,8],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,9],[3,10],[5,8],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,9],[3,11],[5,8],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,10],[3,8],[5,9],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,10],[3,9],[5,8],[7,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,11],[3,8],[5,9],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,6],[2,11],[3,9],[5,8],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,7],[2,8],[3,9],[5,10],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,7],[2,8],[3,9],[5,11],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,7],[2,8],[3,10],[5,9],[6,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,7],[2,8],[3,11],[5,9],[6,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,7],[2,9],[3,8],[5,10],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,7],[2,9],[3,8],[5,11],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,7],[2,9],[3,10],[5,8],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,7],[2,10],[3,9],[5,8],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,7],[2,11],[3,9],[5,8],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,6],[3,10],[5,9],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,6],[3,11],[5,9],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,7],[3,9],[5,10],[6,11]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,7],[3,9],[5,11],[6,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,7],[3,10],[5,9],[6,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,7],[3,11],[5,9],[6,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,9],[3,6],[5,11],[7,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,9],[3,7],[5,10],[6,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,9],[3,7],[5,11],[6,10]],"orbit_size":12},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,10],[3,6],[5,9],[7,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,8],[2,11],[3,6],[5,9],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,9],[2,6],[3,11],[5,8],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,9],[2,7],[3,8],[5,10],[6,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,9],[2,7],[3,10],[5,8],[6,11]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,9],[2,8],[3,6],[5,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,9],[2,8],[3,7],[5,11],[6,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,9],[2,11],[3,6],[5,8],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,4],[1,9],[2,11],[3,7],[5,8],[6,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,4],[2,8],[3,9],[6,11],[7,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,4],[2,9],[3,8],[6,11],[7,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,6],[2,8],[3,9],[4,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,6],[2,9],[3,8],[4,11],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,6],[2,11],[3,8],[4,9],[7,10]],"orbit_size":6},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,7],[2,8],[3,9],[4,10],[6,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,7],[2,8],[3,10],[4,9],[6,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,7],[2,9],[3,8],[4,10],[6,11]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,8],[2,7],[3,10],[4,9],[6,11]],"orbit_size":1},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,5],[1,8],[2,11],[3,6],[4,9],[7,10]],"orbit_size":2},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,6],[1,4],[2,8],[3,9],[5,11],[7,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,6],[1,4],[2,9],[3,8],[5,11],[7,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,6],[1,4],[2,11],[3,9],[5,8],[7,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,8],[3,9],[4,10],[5,11]],"orbit_size":1},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,8],[3,9],[4,11],[5,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,9],[3,8],[4,11],[5,10]],"orbit_size":3},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,7],[1,6],[2,9],[3,8],[4,11],[5,10]],"orbit_size":1},{"cycles":[12],"C":[[0,1,0,0,0,0,0,0,0,0,0,-1],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[-1,0,0,0,0,0,0,0,0,0,1,0]],"Q_pairs":[[0,9],[1,4],[2,11],[3,6],[5,8],[7,10]],"orbit_size":1},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,7],[8,10],[9,11]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,8],[7,10],[9,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,9],[7,10],[8,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,9],[7,11],[8,10]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,3],[4,6],[5,11],[7,9],[8,10]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,5],[6,8],[7,10],[9,11]],"orbit_size":9},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,5],[6,9],[7,10],[8,11]],"orbit_size":6},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,8],[7,10],[9,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,9],[7,10],[8,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,9],[7,11],[8,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,10],[7,9],[8,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,4],[3,6],[5,11],[7,9],[8,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,6],[4,9],[7,10],[8,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,6],[4,9],[7,11],[8,10]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,5],[3,6],[4,11],[7,9],[8,10]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,5],[4,9],[7,10],[8,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,5],[4,9],[7,11],[8,10]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,8],[5,10],[9,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,9],[5,10],[8,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,9],[5,11],[8,10]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,10],[5,8],[9,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,7],[4,10],[5,9],[8,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,7],[5,10],[9,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,9],[5,10],[7,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,9],[5,11],[7,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,7],[9,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,9],[7,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,11],[7,9]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,11],[5,9],[7,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,8],[4,11],[5,10],[7,9]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,7],[5,10],[8,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,7],[5,11],[8,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,8],[5,11],[7,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,10],[5,7],[8,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,10],[5,8],[7,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,11],[5,7],[8,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,9],[4,11],[5,8],[7,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,7],[5,8],[9,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,7],[5,9],[8,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,8],[5,7],[9,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,8],[5,9],[7,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,9],[5,7],[8,11]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,10],[4,9],[5,8],[7,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,11],[4,8],[5,9],[7,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,11],[4,9],[5,7],[8,10]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,2],[1,6],[3,11],[4,9],[5,8],[7,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,5],[6,9],[7,10],[8,11]],"orbit_size":1},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,3],[1,4],[2,6],[5,9],[7,10],[8,11]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,7],[4,9],[5,10],[8,11]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,7],[4,10],[5,9],[8,11]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,8],[4,9],[5,11],[7,10]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,8],[4,11],[5,9],[7,10]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,9],[4,7],[5,10],[8,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,11],[4,8],[5,9],[7,10]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,3],[1,6],[2,11],[4,9],[5,8],[7,10]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,8],[3,9],[4,10],[5,11]],"orbit_size":6},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,8],[3,9],[4,11],[5,10]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,8],[3,10],[4,9],[5,11]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,8],[3,10],[4,11],[5,9]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,8],[3,11],[4,10],[5,9]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,9],[3,8],[4,11],[5,10]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,9],[3,10],[4,11],[5,8]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,9],[3,11],[4,8],[5,10]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,9],[3,11],[4,10],[5,8]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,10],[3,11],[4,8],[5,9]],"orbit_size":6},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,7],[2,11],[3,9],[4,10],[5,8]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,7],[3,10],[4,9],[5,11]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,7],[3,10],[4,11],[5,9]],"orbit_size":72},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,7],[3,11],[4,10],[5,9]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,9],[3,10],[4,11],[5,7]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,9],[3,11],[4,7],[5,10]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,9],[3,11],[4,10],[5,7]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,10],[3,7],[4,9],[5,11]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,10],[3,7],[4,11],[5,9]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,10],[3,9],[4,11],[5,7]],"orbit_size":18},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,8],[2,11],[3,7],[4,9],[5,10]],"orbit_size":36},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,9],[2,8],[3,11],[4,10],[5,7]],"orbit_size":12},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,9],[2,10],[3,7],[4,8],[5,11]],"orbit_size":6},{"cycles":[6,6],"C":[[0,1,0,0,0,-1,0,0,0,0,0,0],[1,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,-1,0,0,0,0,0,0,0],[0,0,0,-1,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,0,1,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,1],[0,0,0,0,0,0,-1,0,0,0,1,0]],"Q_pairs":[[0,6],[1,11],[2,10],[3,9],[4,8],[5,7]],"orbit_size":6}]
````


## Annexe — rangs_et_signes_441.json (JSON compact, complet)

````json
[{"index":0,"cycles":[12],"t":2,"rank":16,"disc_K":6,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,2],[1,3],[4,6],[5,7],[8,10],[9,11]]},{"index":1,"cycles":[12],"t":1,"rank":17,"disc_K":3,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,6],[5,8],[7,10],[9,11]]},{"index":2,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,3],[4,6],[5,9],[7,10],[8,11]]},{"index":3,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,6],[5,9],[7,11],[8,10]]},{"index":4,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,6],[5,10],[7,9],[8,11]]},{"index":5,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,6],[5,11],[7,9],[8,10]]},{"index":6,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,3],[4,7],[5,9],[6,10],[8,11]]},{"index":7,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,7],[5,9],[6,11],[8,10]]},{"index":8,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,7],[5,10],[6,9],[8,11]]},{"index":9,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,7],[5,11],[6,9],[8,10]]},{"index":10,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,8],[5,9],[6,10],[7,11]]},{"index":11,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,8],[5,9],[6,11],[7,10]]},{"index":12,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,8],[5,10],[6,9],[7,11]]},{"index":13,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,8],[5,10],[6,11],[7,9]]},{"index":14,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,3],[4,8],[5,11],[6,9],[7,10]]},{"index":15,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,3],[4,8],[5,11],[6,10],[7,9]]},{"index":16,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,9],[5,7],[6,11],[8,10]]},{"index":17,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,9],[5,8],[6,11],[7,10]]},{"index":18,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,9],[5,11],[6,8],[7,10]]},{"index":19,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,10],[5,11],[6,8],[7,9]]},{"index":20,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,11],[5,7],[6,9],[8,10]]},{"index":21,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,11],[5,8],[6,9],[7,10]]},{"index":22,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,11],[5,8],[6,10],[7,9]]},{"index":23,"cycles":[12],"t":2,"rank":16,"disc_K":6,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,2],[1,3],[4,11],[5,10],[6,8],[7,9]]},{"index":24,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,5],[6,8],[7,10],[9,11]]},{"index":25,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,5],[6,9],[7,10],[8,11]]},{"index":26,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,5],[6,9],[7,11],[8,10]]},{"index":27,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,5],[6,11],[7,9],[8,10]]},{"index":28,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,6],[5,8],[7,10],[9,11]]},{"index":29,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,6],[5,9],[7,10],[8,11]]},{"index":30,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,6],[5,9],[7,11],[8,10]]},{"index":31,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,6],[5,10],[7,9],[8,11]]},{"index":32,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,6],[5,11],[7,9],[8,10]]},{"index":33,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,7],[5,8],[6,10],[9,11]]},{"index":34,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,7],[5,9],[6,10],[8,11]]},{"index":35,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,7],[5,9],[6,11],[8,10]]},{"index":36,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,7],[5,10],[6,8],[9,11]]},{"index":37,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,7],[5,10],[6,9],[8,11]]},{"index":38,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,7],[5,11],[6,9],[8,10]]},{"index":39,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,8],[5,7],[6,10],[9,11]]},{"index":40,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,8],[5,9],[6,10],[7,11]]},{"index":41,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,8],[5,9],[6,11],[7,10]]},{"index":42,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,8],[5,10],[6,9],[7,11]]},{"index":43,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,8],[5,10],[6,11],[7,9]]},{"index":44,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,8],[5,11],[6,9],[7,10]]},{"index":45,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,8],[5,11],[6,10],[7,9]]},{"index":46,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,9],[5,7],[6,10],[8,11]]},{"index":47,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,9],[5,7],[6,11],[8,10]]},{"index":48,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,9],[5,8],[6,10],[7,11]]},{"index":49,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,9],[5,8],[6,11],[7,10]]},{"index":50,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,9],[5,10],[6,8],[7,11]]},{"index":51,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,9],[5,11],[6,8],[7,10]]},{"index":52,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,10],[5,7],[6,8],[9,11]]},{"index":53,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,10],[5,7],[6,9],[8,11]]},{"index":54,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,10],[5,8],[6,9],[7,11]]},{"index":55,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,10],[5,8],[6,11],[7,9]]},{"index":56,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,10],[5,9],[6,8],[7,11]]},{"index":57,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,11],[5,7],[6,9],[8,10]]},{"index":58,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,11],[5,8],[6,9],[7,10]]},{"index":59,"cycles":[12],"t":1,"rank":17,"disc_K":5,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,11],[5,8],[6,10],[7,9]]},{"index":60,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,11],[5,9],[6,8],[7,10]]},{"index":61,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,6],[4,9],[7,10],[8,11]]},{"index":62,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,6],[4,9],[7,11],[8,10]]},{"index":63,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,6],[4,10],[7,9],[8,11]]},{"index":64,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,6],[4,11],[7,9],[8,10]]},{"index":65,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,7],[4,8],[6,10],[9,11]]},{"index":66,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,7],[4,9],[6,10],[8,11]]},{"index":67,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,7],[4,9],[6,11],[8,10]]},{"index":68,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,7],[4,10],[6,8],[9,11]]},{"index":69,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,7],[4,10],[6,9],[8,11]]},{"index":70,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,7],[4,11],[6,9],[8,10]]},{"index":71,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,8],[4,7],[6,10],[9,11]]},{"index":72,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,8],[4,9],[6,10],[7,11]]},{"index":73,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,8],[4,9],[6,11],[7,10]]},{"index":74,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,8],[4,10],[6,9],[7,11]]},{"index":75,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,8],[4,10],[6,11],[7,9]]},{"index":76,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,8],[4,11],[6,9],[7,10]]},{"index":77,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,8],[4,11],[6,10],[7,9]]},{"index":78,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,9],[4,6],[7,10],[8,11]]},{"index":79,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,9],[4,6],[7,11],[8,10]]},{"index":80,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,9],[4,7],[6,10],[8,11]]},{"index":81,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,9],[4,7],[6,11],[8,10]]},{"index":82,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,9],[4,8],[6,10],[7,11]]},{"index":83,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,9],[4,8],[6,11],[7,10]]},{"index":84,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,9],[4,10],[6,8],[7,11]]},{"index":85,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,10],[4,6],[7,9],[8,11]]},{"index":86,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,10],[4,7],[6,8],[9,11]]},{"index":87,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,10],[4,7],[6,9],[8,11]]},{"index":88,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,10],[4,8],[6,9],[7,11]]},{"index":89,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,10],[4,8],[6,11],[7,9]]},{"index":90,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,10],[4,9],[6,8],[7,11]]},{"index":91,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,11],[4,6],[7,9],[8,10]]},{"index":92,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,11],[4,7],[6,9],[8,10]]},{"index":93,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,11],[4,8],[6,9],[7,10]]},{"index":94,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,11],[4,8],[6,10],[7,9]]},{"index":95,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,5],[4,9],[7,10],[8,11]]},{"index":96,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,5],[4,9],[7,11],[8,10]]},{"index":97,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,5],[4,10],[7,9],[8,11]]},{"index":98,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,5],[4,11],[7,9],[8,10]]},{"index":99,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,8],[5,10],[9,11]]},{"index":100,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,9],[5,10],[8,11]]},{"index":101,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,9],[5,11],[8,10]]},{"index":102,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,10],[5,8],[9,11]]},{"index":103,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,10],[5,9],[8,11]]},{"index":104,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,11],[5,9],[8,10]]},{"index":105,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,7],[5,10],[9,11]]},{"index":106,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,8],[4,9],[5,10],[7,11]]},{"index":107,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,8],[4,9],[5,11],[7,10]]},{"index":108,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,7],[9,11]]},{"index":109,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,9],[7,11]]},{"index":110,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,11],[7,9]]},{"index":111,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,8],[4,11],[5,9],[7,10]]},{"index":112,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,11],[5,10],[7,9]]},{"index":113,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,7],[5,10],[8,11]]},{"index":114,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,7],[5,11],[8,10]]},{"index":115,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,9],[4,8],[5,10],[7,11]]},{"index":116,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,8],[5,11],[7,10]]},{"index":117,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,10],[5,7],[8,11]]},{"index":118,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,10],[5,8],[7,11]]},{"index":119,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,11],[5,8],[7,10]]},{"index":120,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,10],[4,7],[5,8],[9,11]]},{"index":121,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,10],[4,7],[5,9],[8,11]]},{"index":122,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,10],[4,8],[5,7],[9,11]]},{"index":123,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,10],[4,8],[5,9],[7,11]]},{"index":124,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,10],[4,9],[5,7],[8,11]]},{"index":125,"cycles":[12],"t":1,"rank":17,"disc_K":5,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,10],[4,9],[5,8],[7,11]]},{"index":126,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,11],[4,7],[5,9],[8,10]]},{"index":127,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,11],[4,8],[5,9],[7,10]]},{"index":128,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,11],[4,9],[5,8],[7,10]]},{"index":129,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,7],[3,5],[4,9],[6,10],[8,11]]},{"index":130,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,5],[4,9],[6,11],[8,10]]},{"index":131,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,5],[4,10],[6,8],[9,11]]},{"index":132,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,5],[4,10],[6,9],[8,11]]},{"index":133,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,6],[4,9],[5,10],[8,11]]},{"index":134,"cycles":[12],"t":2,"rank":16,"disc_K":6,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,2],[1,7],[3,6],[4,9],[5,11],[8,10]]},{"index":135,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,6],[4,10],[5,8],[9,11]]},{"index":136,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,6],[4,10],[5,9],[8,11]]},{"index":137,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,6],[4,11],[5,9],[8,10]]},{"index":138,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,7],[3,8],[4,9],[5,10],[6,11]]},{"index":139,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,8],[4,9],[5,11],[6,10]]},{"index":140,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,7],[3,8],[4,10],[5,9],[6,11]]},{"index":141,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,8],[4,10],[5,11],[6,9]]},{"index":142,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,7],[3,8],[4,11],[5,9],[6,10]]},{"index":143,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,8],[4,11],[5,10],[6,9]]},{"index":144,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,9],[4,6],[5,11],[8,10]]},{"index":145,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,9],[4,8],[5,10],[6,11]]},{"index":146,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,9],[4,8],[5,11],[6,10]]},{"index":147,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,9],[4,10],[5,8],[6,11]]},{"index":148,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,9],[4,10],[5,11],[6,8]]},{"index":149,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,9],[4,11],[5,8],[6,10]]},{"index":150,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,9],[4,11],[5,10],[6,8]]},{"index":151,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,10],[4,8],[5,9],[6,11]]},{"index":152,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,10],[4,8],[5,11],[6,9]]},{"index":153,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,7],[3,10],[4,9],[5,8],[6,11]]},{"index":154,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,10],[4,9],[5,11],[6,8]]},{"index":155,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,10],[4,11],[5,8],[6,9]]},{"index":156,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,7],[3,10],[4,11],[5,9],[6,8]]},{"index":157,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,11],[4,8],[5,9],[6,10]]},{"index":158,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,11],[4,8],[5,10],[6,9]]},{"index":159,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,7],[3,11],[4,9],[5,8],[6,10]]},{"index":160,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,7],[3,11],[4,10],[5,8],[6,9]]},{"index":161,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,7],[3,11],[4,10],[5,9],[6,8]]},{"index":162,"cycles":[12],"t":1,"rank":17,"disc_K":5,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,5],[4,9],[6,10],[7,11]]},{"index":163,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,5],[4,9],[6,11],[7,10]]},{"index":164,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,6],[4,9],[5,10],[7,11]]},{"index":165,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,6],[4,9],[5,11],[7,10]]},{"index":166,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,6],[4,10],[5,9],[7,11]]},{"index":167,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,6],[4,10],[5,11],[7,9]]},{"index":168,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,6],[4,11],[5,9],[7,10]]},{"index":169,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,6],[4,11],[5,10],[7,9]]},{"index":170,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,7],[4,9],[5,10],[6,11]]},{"index":171,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,7],[4,9],[5,11],[6,10]]},{"index":172,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,7],[4,10],[5,9],[6,11]]},{"index":173,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,7],[4,10],[5,11],[6,9]]},{"index":174,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,7],[4,11],[5,9],[6,10]]},{"index":175,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,7],[4,11],[5,10],[6,9]]},{"index":176,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,9],[4,7],[5,10],[6,11]]},{"index":177,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,9],[4,7],[5,11],[6,10]]},{"index":178,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,9],[4,10],[5,7],[6,11]]},{"index":179,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,9],[4,11],[5,7],[6,10]]},{"index":180,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,10],[4,7],[5,9],[6,11]]},{"index":181,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,10],[4,7],[5,11],[6,9]]},{"index":182,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,10],[4,9],[5,7],[6,11]]},{"index":183,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,10],[4,11],[5,7],[6,9]]},{"index":184,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,11],[4,7],[5,9],[6,10]]},{"index":185,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,8],[3,11],[4,7],[5,10],[6,9]]},{"index":186,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,11],[4,9],[5,7],[6,10]]},{"index":187,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,8],[3,11],[4,10],[5,7],[6,9]]},{"index":188,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,5],[4,6],[7,10],[8,11]]},{"index":189,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,5],[4,7],[6,10],[8,11]]},{"index":190,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,5],[4,8],[6,10],[7,11]]},{"index":191,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,5],[4,8],[6,11],[7,10]]},{"index":192,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,6],[4,7],[5,10],[8,11]]},{"index":193,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,6],[4,8],[5,10],[7,11]]},{"index":194,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,6],[4,8],[5,11],[7,10]]},{"index":195,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,6],[4,10],[5,8],[7,11]]},{"index":196,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,6],[4,11],[5,8],[7,10]]},{"index":197,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,7],[4,8],[5,10],[6,11]]},{"index":198,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,7],[4,8],[5,11],[6,10]]},{"index":199,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,7],[4,10],[5,8],[6,11]]},{"index":200,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,7],[4,10],[5,11],[6,8]]},{"index":201,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,7],[4,11],[5,8],[6,10]]},{"index":202,"cycles":[12],"t":2,"rank":16,"disc_K":1,"char":1,"supplement_Witt":0,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,7],[4,11],[5,10],[6,8]]},{"index":203,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,8],[4,7],[5,10],[6,11]]},{"index":204,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,8],[4,7],[5,11],[6,10]]},{"index":205,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,8],[4,11],[5,7],[6,10]]},{"index":206,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,10],[4,7],[5,8],[6,11]]},{"index":207,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,10],[4,7],[5,11],[6,8]]},{"index":208,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,10],[4,11],[5,7],[6,8]]},{"index":209,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,11],[4,7],[5,8],[6,10]]},{"index":210,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,11],[4,7],[5,10],[6,8]]},{"index":211,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,9],[3,11],[4,8],[5,7],[6,10]]},{"index":212,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,9],[3,11],[4,10],[5,7],[6,8]]},{"index":213,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,5],[4,6],[7,9],[8,11]]},{"index":214,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,5],[4,7],[6,8],[9,11]]},{"index":215,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,5],[4,7],[6,9],[8,11]]},{"index":216,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,6],[4,7],[5,8],[9,11]]},{"index":217,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,6],[4,7],[5,9],[8,11]]},{"index":218,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,6],[4,8],[5,9],[7,11]]},{"index":219,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,6],[4,9],[5,8],[7,11]]},{"index":220,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,7],[4,8],[5,9],[6,11]]},{"index":221,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,7],[4,8],[5,11],[6,9]]},{"index":222,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,7],[4,9],[5,8],[6,11]]},{"index":223,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,7],[4,11],[5,8],[6,9]]},{"index":224,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,8],[4,7],[5,9],[6,11]]},{"index":225,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,8],[4,7],[5,11],[6,9]]},{"index":226,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,8],[4,11],[5,7],[6,9]]},{"index":227,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,9],[4,7],[5,8],[6,11]]},{"index":228,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,9],[4,7],[5,11],[6,8]]},{"index":229,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,9],[4,11],[5,7],[6,8]]},{"index":230,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,11],[4,7],[5,8],[6,9]]},{"index":231,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,11],[4,7],[5,9],[6,8]]},{"index":232,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,10],[3,11],[4,8],[5,7],[6,9]]},{"index":233,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,10],[3,11],[4,9],[5,7],[6,8]]},{"index":234,"cycles":[12],"t":2,"rank":16,"disc_K":3,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,2],[1,11],[3,5],[4,6],[7,9],[8,10]]},{"index":235,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,11],[3,6],[4,8],[5,9],[7,10]]},{"index":236,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,11],[3,6],[4,9],[5,8],[7,10]]},{"index":237,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,11],[3,7],[4,8],[5,9],[6,10]]},{"index":238,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,11],[3,7],[4,8],[5,10],[6,9]]},{"index":239,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,11],[3,7],[4,9],[5,8],[6,10]]},{"index":240,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,11],[3,7],[4,10],[5,8],[6,9]]},{"index":241,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,11],[3,8],[4,7],[5,10],[6,9]]},{"index":242,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,11],[3,9],[4,10],[5,7],[6,8]]},{"index":243,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,11],[3,10],[4,7],[5,8],[6,9]]},{"index":244,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,11],[3,10],[4,9],[5,7],[6,8]]},{"index":245,"cycles":[12],"t":1,"rank":17,"disc_K":6,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,5],[6,9],[7,10],[8,11]]},{"index":246,"cycles":[12],"t":2,"rank":16,"disc_K":4,"char":1,"supplement_Witt":0,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,6],[5,9],[7,10],[8,11]]},{"index":247,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,4],[2,7],[5,9],[6,10],[8,11]]},{"index":248,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,7],[5,10],[6,9],[8,11]]},{"index":249,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,8],[5,9],[6,10],[7,11]]},{"index":250,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,8],[5,9],[6,11],[7,10]]},{"index":251,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,8],[5,10],[6,9],[7,11]]},{"index":252,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,8],[5,11],[6,9],[7,10]]},{"index":253,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,4],[2,9],[5,8],[6,10],[7,11]]},{"index":254,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,9],[5,8],[6,11],[7,10]]},{"index":255,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,10],[5,8],[6,9],[7,11]]},{"index":256,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,4],[2,11],[5,8],[6,9],[7,10]]},{"index":257,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,5],[2,7],[4,9],[6,10],[8,11]]},{"index":258,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,5],[2,7],[4,10],[6,9],[8,11]]},{"index":259,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,5],[2,8],[4,9],[6,10],[7,11]]},{"index":260,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,5],[2,8],[4,9],[6,11],[7,10]]},{"index":261,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,5],[2,8],[4,10],[6,9],[7,11]]},{"index":262,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,5],[2,9],[4,7],[6,10],[8,11]]},{"index":263,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,5],[2,9],[4,8],[6,10],[7,11]]},{"index":264,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,5],[2,9],[4,8],[6,11],[7,10]]},{"index":265,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,5],[2,10],[4,7],[6,9],[8,11]]},{"index":266,"cycles":[12],"t":1,"rank":17,"disc_K":5,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,5],[2,10],[4,8],[6,9],[7,11]]},{"index":267,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,7],[4,9],[5,10],[8,11]]},{"index":268,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,7],[4,10],[5,9],[8,11]]},{"index":269,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,8],[4,9],[5,10],[7,11]]},{"index":270,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,8],[4,9],[5,11],[7,10]]},{"index":271,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,8],[4,10],[5,9],[7,11]]},{"index":272,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,8],[4,11],[5,9],[7,10]]},{"index":273,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,6],[2,9],[4,7],[5,10],[8,11]]},{"index":274,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,6],[2,9],[4,8],[5,10],[7,11]]},{"index":275,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,9],[4,8],[5,11],[7,10]]},{"index":276,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,9],[4,11],[5,8],[7,10]]},{"index":277,"cycles":[12],"t":2,"rank":16,"disc_K":2,"char":1,"supplement_Witt":0,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,7],[2,5],[4,10],[6,9],[8,11]]},{"index":278,"cycles":[12],"t":1,"rank":17,"disc_K":5,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,7],[2,6],[4,10],[5,9],[8,11]]},{"index":279,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,7],[2,8],[4,9],[5,10],[6,11]]},{"index":280,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,7],[2,8],[4,9],[5,11],[6,10]]},{"index":281,"cycles":[12],"t":3,"rank":15,"disc_K":5,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,3],[1,7],[2,8],[4,10],[5,11],[6,9]]},{"index":282,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,7],[2,8],[4,11],[5,9],[6,10]]},{"index":283,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,7],[2,8],[4,11],[5,10],[6,9]]},{"index":284,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,8],[2,5],[4,9],[6,10],[7,11]]},{"index":285,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,8],[2,5],[4,9],[6,11],[7,10]]},{"index":286,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,8],[2,6],[4,9],[5,10],[7,11]]},{"index":287,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,8],[2,6],[4,9],[5,11],[7,10]]},{"index":288,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,8],[2,6],[4,10],[5,9],[7,11]]},{"index":289,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,8],[2,6],[4,11],[5,9],[7,10]]},{"index":290,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,8],[2,7],[4,9],[5,10],[6,11]]},{"index":291,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,8],[2,7],[4,9],[5,11],[6,10]]},{"index":292,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,8],[2,7],[4,10],[5,11],[6,9]]},{"index":293,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,8],[2,7],[4,11],[5,9],[6,10]]},{"index":294,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,8],[2,7],[4,11],[5,10],[6,9]]},{"index":295,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,9],[2,5],[4,8],[6,10],[7,11]]},{"index":296,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,9],[2,5],[4,8],[6,11],[7,10]]},{"index":297,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,9],[2,6],[4,8],[5,10],[7,11]]},{"index":298,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,9],[2,6],[4,8],[5,11],[7,10]]},{"index":299,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,9],[2,6],[4,11],[5,8],[7,10]]},{"index":300,"cycles":[12],"t":2,"rank":16,"disc_K":2,"char":1,"supplement_Witt":0,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,10],[2,5],[4,7],[6,9],[8,11]]},{"index":301,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,5],[2,8],[3,9],[6,10],[7,11]]},{"index":302,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,5],[2,8],[3,9],[6,11],[7,10]]},{"index":303,"cycles":[12],"t":2,"rank":16,"disc_K":2,"char":1,"supplement_Witt":0,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,5],[2,9],[3,8],[6,10],[7,11]]},{"index":304,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,5],[2,9],[3,8],[6,11],[7,10]]},{"index":305,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,6],[2,8],[3,9],[5,10],[7,11]]},{"index":306,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,6],[2,8],[3,9],[5,11],[7,10]]},{"index":307,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,6],[2,8],[3,10],[5,9],[7,11]]},{"index":308,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,6],[2,8],[3,11],[5,9],[7,10]]},{"index":309,"cycles":[12],"t":2,"rank":16,"disc_K":2,"char":1,"supplement_Witt":0,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,6],[2,9],[3,8],[5,10],[7,11]]},{"index":310,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,6],[2,9],[3,8],[5,11],[7,10]]},{"index":311,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,6],[2,9],[3,10],[5,8],[7,11]]},{"index":312,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,6],[2,9],[3,11],[5,8],[7,10]]},{"index":313,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,6],[2,10],[3,8],[5,9],[7,11]]},{"index":314,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,6],[2,10],[3,9],[5,8],[7,11]]},{"index":315,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,6],[2,11],[3,8],[5,9],[7,10]]},{"index":316,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,6],[2,11],[3,9],[5,8],[7,10]]},{"index":317,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,7],[2,8],[3,9],[5,10],[6,11]]},{"index":318,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,7],[2,8],[3,9],[5,11],[6,10]]},{"index":319,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,7],[2,8],[3,10],[5,9],[6,11]]},{"index":320,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,7],[2,8],[3,11],[5,9],[6,10]]},{"index":321,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,7],[2,9],[3,8],[5,10],[6,11]]},{"index":322,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,7],[2,9],[3,8],[5,11],[6,10]]},{"index":323,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,7],[2,9],[3,10],[5,8],[6,11]]},{"index":324,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,7],[2,10],[3,9],[5,8],[6,11]]},{"index":325,"cycles":[12],"t":1,"rank":17,"disc_K":6,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,7],[2,11],[3,9],[5,8],[6,10]]},{"index":326,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,8],[2,6],[3,10],[5,9],[7,11]]},{"index":327,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,8],[2,6],[3,11],[5,9],[7,10]]},{"index":328,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,8],[2,7],[3,9],[5,10],[6,11]]},{"index":329,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,8],[2,7],[3,9],[5,11],[6,10]]},{"index":330,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,8],[2,7],[3,10],[5,9],[6,11]]},{"index":331,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,8],[2,7],[3,11],[5,9],[6,10]]},{"index":332,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,8],[2,9],[3,6],[5,11],[7,10]]},{"index":333,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,8],[2,9],[3,7],[5,10],[6,11]]},{"index":334,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,8],[2,9],[3,7],[5,11],[6,10]]},{"index":335,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,8],[2,10],[3,6],[5,9],[7,11]]},{"index":336,"cycles":[12],"t":1,"rank":17,"disc_K":5,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,8],[2,11],[3,6],[5,9],[7,10]]},{"index":337,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,9],[2,6],[3,11],[5,8],[7,10]]},{"index":338,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,9],[2,7],[3,8],[5,10],[6,11]]},{"index":339,"cycles":[12],"t":1,"rank":17,"disc_K":4,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,9],[2,7],[3,10],[5,8],[6,11]]},{"index":340,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,9],[2,8],[3,6],[5,11],[7,10]]},{"index":341,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,9],[2,8],[3,7],[5,11],[6,10]]},{"index":342,"cycles":[12],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,4],[1,9],[2,11],[3,6],[5,8],[7,10]]},{"index":343,"cycles":[12],"t":1,"rank":17,"disc_K":6,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,4],[1,9],[2,11],[3,7],[5,8],[6,10]]},{"index":344,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,5],[1,4],[2,8],[3,9],[6,11],[7,10]]},{"index":345,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,5],[1,4],[2,9],[3,8],[6,11],[7,10]]},{"index":346,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,5],[1,6],[2,8],[3,9],[4,11],[7,10]]},{"index":347,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,5],[1,6],[2,9],[3,8],[4,11],[7,10]]},{"index":348,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,5],[1,6],[2,11],[3,8],[4,9],[7,10]]},{"index":349,"cycles":[12],"t":1,"rank":17,"disc_K":6,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,5],[1,7],[2,8],[3,9],[4,10],[6,11]]},{"index":350,"cycles":[12],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,5],[1,7],[2,8],[3,10],[4,9],[6,11]]},{"index":351,"cycles":[12],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,5],[1,7],[2,9],[3,8],[4,10],[6,11]]},{"index":352,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,5],[1,8],[2,7],[3,10],[4,9],[6,11]]},{"index":353,"cycles":[12],"t":2,"rank":16,"disc_K":3,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,5],[1,8],[2,11],[3,6],[4,9],[7,10]]},{"index":354,"cycles":[12],"t":2,"rank":16,"disc_K":3,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,6],[1,4],[2,8],[3,9],[5,11],[7,10]]},{"index":355,"cycles":[12],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,4],[2,9],[3,8],[5,11],[7,10]]},{"index":356,"cycles":[12],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,4],[2,11],[3,9],[5,8],[7,10]]},{"index":357,"cycles":[12],"t":2,"rank":16,"disc_K":3,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,6],[1,7],[2,8],[3,9],[4,10],[5,11]]},{"index":358,"cycles":[12],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,7],[2,8],[3,9],[4,11],[5,10]]},{"index":359,"cycles":[12],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,7],[2,9],[3,8],[4,11],[5,10]]},{"index":360,"cycles":[12],"t":2,"rank":16,"disc_K":4,"char":1,"supplement_Witt":0,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,7],[1,6],[2,9],[3,8],[4,11],[5,10]]},{"index":361,"cycles":[12],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,9],[1,4],[2,11],[3,6],[5,8],[7,10]]},{"index":362,"cycles":[6,6],"t":2,"rank":16,"disc_K":5,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,2],[1,3],[4,6],[5,7],[8,10],[9,11]]},{"index":363,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,6],[5,8],[7,10],[9,11]]},{"index":364,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,6],[5,9],[7,10],[8,11]]},{"index":365,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,6],[5,9],[7,11],[8,10]]},{"index":366,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,3],[4,6],[5,11],[7,9],[8,10]]},{"index":367,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,5],[6,8],[7,10],[9,11]]},{"index":368,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,5],[6,9],[7,10],[8,11]]},{"index":369,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,6],[5,8],[7,10],[9,11]]},{"index":370,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,6],[5,9],[7,10],[8,11]]},{"index":371,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,6],[5,9],[7,11],[8,10]]},{"index":372,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,4],[3,6],[5,10],[7,9],[8,11]]},{"index":373,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,4],[3,6],[5,11],[7,9],[8,10]]},{"index":374,"cycles":[6,6],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,5],[3,6],[4,9],[7,10],[8,11]]},{"index":375,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,5],[3,6],[4,9],[7,11],[8,10]]},{"index":376,"cycles":[6,6],"t":2,"rank":16,"disc_K":6,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,2],[1,5],[3,6],[4,11],[7,9],[8,10]]},{"index":377,"cycles":[6,6],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,5],[4,9],[7,10],[8,11]]},{"index":378,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,5],[4,9],[7,11],[8,10]]},{"index":379,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,8],[5,10],[9,11]]},{"index":380,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,9],[5,10],[8,11]]},{"index":381,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,9],[5,11],[8,10]]},{"index":382,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,10],[5,8],[9,11]]},{"index":383,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,7],[4,10],[5,9],[8,11]]},{"index":384,"cycles":[6,6],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,7],[5,10],[9,11]]},{"index":385,"cycles":[6,6],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,9],[5,10],[7,11]]},{"index":386,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,8],[4,9],[5,11],[7,10]]},{"index":387,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,7],[9,11]]},{"index":388,"cycles":[6,6],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,9],[7,11]]},{"index":389,"cycles":[6,6],"t":2,"rank":16,"disc_K":2,"char":1,"supplement_Witt":0,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,10],[5,11],[7,9]]},{"index":390,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,11],[5,9],[7,10]]},{"index":391,"cycles":[6,6],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,8],[4,11],[5,10],[7,9]]},{"index":392,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,7],[5,10],[8,11]]},{"index":393,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,9],[4,7],[5,11],[8,10]]},{"index":394,"cycles":[6,6],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,9],[4,8],[5,11],[7,10]]},{"index":395,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,10],[5,7],[8,11]]},{"index":396,"cycles":[6,6],"t":1,"rank":17,"disc_K":5,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,10],[5,8],[7,11]]},{"index":397,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,11],[5,7],[8,10]]},{"index":398,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,9],[4,11],[5,8],[7,10]]},{"index":399,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,10],[4,7],[5,8],[9,11]]},{"index":400,"cycles":[6,6],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,10],[4,7],[5,9],[8,11]]},{"index":401,"cycles":[6,6],"t":0,"rank":18,"disc_K":5,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,10],[4,8],[5,7],[9,11]]},{"index":402,"cycles":[6,6],"t":1,"rank":17,"disc_K":5,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,10],[4,8],[5,9],[7,11]]},{"index":403,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,10],[4,9],[5,7],[8,11]]},{"index":404,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,10],[4,9],[5,8],[7,11]]},{"index":405,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,2],[1,6],[3,11],[4,8],[5,9],[7,10]]},{"index":406,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,11],[4,9],[5,7],[8,10]]},{"index":407,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,2],[1,6],[3,11],[4,9],[5,8],[7,10]]},{"index":408,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,4],[2,5],[6,9],[7,10],[8,11]]},{"index":409,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,4],[2,6],[5,9],[7,10],[8,11]]},{"index":410,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,6],[2,7],[4,9],[5,10],[8,11]]},{"index":411,"cycles":[6,6],"t":0,"rank":18,"disc_K":6,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,6],[2,7],[4,10],[5,9],[8,11]]},{"index":412,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,3],[1,6],[2,8],[4,9],[5,11],[7,10]]},{"index":413,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,8],[4,11],[5,9],[7,10]]},{"index":414,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,9],[4,7],[5,10],[8,11]]},{"index":415,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,11],[4,8],[5,9],[7,10]]},{"index":416,"cycles":[6,6],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,3],[1,6],[2,11],[4,9],[5,8],[7,10]]},{"index":417,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,7],[2,8],[3,9],[4,10],[5,11]]},{"index":418,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,7],[2,8],[3,9],[4,11],[5,10]]},{"index":419,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,6],[1,7],[2,8],[3,10],[4,9],[5,11]]},{"index":420,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,7],[2,8],[3,10],[4,11],[5,9]]},{"index":421,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,7],[2,8],[3,11],[4,10],[5,9]]},{"index":422,"cycles":[6,6],"t":2,"rank":16,"disc_K":3,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,6],[1,7],[2,9],[3,8],[4,11],[5,10]]},{"index":423,"cycles":[6,6],"t":1,"rank":17,"disc_K":6,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,7],[2,9],[3,10],[4,11],[5,8]]},{"index":424,"cycles":[6,6],"t":2,"rank":16,"disc_K":6,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,6],[1,7],[2,9],[3,11],[4,8],[5,10]]},{"index":425,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,7],[2,9],[3,11],[4,10],[5,8]]},{"index":426,"cycles":[6,6],"t":2,"rank":16,"disc_K":6,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,6],[1,7],[2,10],[3,11],[4,8],[5,9]]},{"index":427,"cycles":[6,6],"t":1,"rank":17,"disc_K":1,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,7],[2,11],[3,9],[4,10],[5,8]]},{"index":428,"cycles":[6,6],"t":1,"rank":17,"disc_K":2,"char":1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,8],[2,7],[3,10],[4,9],[5,11]]},{"index":429,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,8],[2,7],[3,10],[4,11],[5,9]]},{"index":430,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,8],[2,7],[3,11],[4,10],[5,9]]},{"index":431,"cycles":[6,6],"t":1,"rank":17,"disc_K":3,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,8],[2,9],[3,10],[4,11],[5,7]]},{"index":432,"cycles":[6,6],"t":0,"rank":18,"disc_K":1,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,8],[2,9],[3,11],[4,7],[5,10]]},{"index":433,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,6],[1,8],[2,9],[3,11],[4,10],[5,7]]},{"index":434,"cycles":[6,6],"t":1,"rank":17,"disc_K":6,"char":-1,"supplement_Witt":1,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,8],[2,10],[3,7],[4,9],[5,11]]},{"index":435,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,8],[2,10],[3,7],[4,11],[5,9]]},{"index":436,"cycles":[6,6],"t":0,"rank":18,"disc_K":3,"char":-1,"supplement_Witt":0,"lower_when_r0_zero":18,"r0_min_g20":0,"r0_min_g18":0,"r0_min_g16":1,"Q_pairs":[[0,6],[1,8],[2,10],[3,9],[4,11],[5,7]]},{"index":437,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,8],[2,11],[3,7],[4,9],[5,10]]},{"index":438,"cycles":[6,6],"t":0,"rank":18,"disc_K":4,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,9],[2,8],[3,11],[4,10],[5,7]]},{"index":439,"cycles":[6,6],"t":2,"rank":16,"disc_K":3,"char":-1,"supplement_Witt":2,"lower_when_r0_zero":22,"r0_min_g20":1,"r0_min_g18":2,"r0_min_g16":3,"Q_pairs":[[0,6],[1,9],[2,10],[3,7],[4,8],[5,11]]},{"index":440,"cycles":[6,6],"t":0,"rank":18,"disc_K":2,"char":1,"supplement_Witt":2,"lower_when_r0_zero":20,"r0_min_g20":0,"r0_min_g18":1,"r0_min_g16":2,"Q_pairs":[[0,6],[1,11],[2,10],[3,9],[4,8],[5,7]]}]
````


## Annexe — acquis de genre et lemme de Witt de la campagne A33

Le texte suivant conserve les preuves et les références internes utilisées ; son exclusion propre à A33 précède la nouvelle couverture g16.

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
