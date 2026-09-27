# Preuves complètes — attaque globale du 27 septembre 2026

Ce dossier rassemble les preuves, les audits adverses et les limites de cette reprise. Il ne démontre pas l’inexistence de l’involution. Les deux valeurs g⁻=18 et g⁻=20 sont traitées par un cadre commun, sans balayage des types locaux.



---

Pièce originale : BILAN_ATTAQUE_GLOBALE.md

# Attaque globale de l'involution : sept blocs, un réseau commun

27 septembre 2026 — reprise de 08 h 03 UTC.

## Résultat de cette campagne

Le balayage local est remplacé par un objet commun aux deux valeurs restantes g^-=18 et g^-=20 : un réseau intégral positif maximal N_max, de rang 22 et de déterminant 49, puis son plongement dans un réseau unimodulaire impair de rang 24.

Les nouveaux résultats globaux, sans hypothèse P=0, sont :

1. N_max est orthogonalement indécomposable.
2. Ses racines de norme 2 engendrent un espace de dimension au plus 20. Les deux strates de rang 22 et 21 sont exclues uniformément.
3. Ses systèmes de racines ne contiennent ni E8, ni D_n pour n>=11, ni A_n pour n>=20. Les limites de transport vers le collage de rang 24 sont précisées dans les preuves : E8 et D_n pour n>=12 y sont également exclus, ainsi que A_n pour n>=22.

Ces exclusions ne sont pas une élimination de g^-=18 ou20. Un contrôle positif explicite montre pourquoi on ne peut pas conclure par le genre seul : il existe un réseau de rang 22, déterminant 49, minimum 3, engendré intégralement par des vecteurs de norme 3, indécomposable, sans racines, avec minimum dual>=10/7 et minimum caractéristique>=10. Il satisfait toutes ces propriétés globales. Le repère physique de42+7 vecteurs n'y est pas construit.

## Cadre exact et périmètre

On accepte les réductions transmises par C1/structures : g^- appartient à{18,20} et la forme discriminante7 du réseau de rang22 est non scindée, de dimension22-g^-. Cela ne constitue pas une nouvelle vérification des dépôts de ces sessions.

Le secteur impair a Gram H=3I-S et H²=7H, avec

S=[-I_7,C ; C^t,T], CC^t=12I, CT=0,
T²+T=12I-C^tC.

Les49 générateurs sont les sept h_c de norme4, orthogonaux, et les42 u_o de norme3. Les colonnes de C sont e_i+e_j et e_i-e_j, pour les21 paires de blocs. On a

3h_c+sum_o C_co u_o=0,
sum_a (x,u_a)^2=7 x².

La borne min(N*)>=8/7 figurait déjà dans la campagne : elle n'est pas annoncée comme une invention. Une preuve autonome complète est conservée dans AUDIT_NORME1_ET_METRIQUES.md. Elle implique min(N)>=2 et protège les saturations intégrales utilisées ci-dessous.

## 1. Les deux valeurs de g entrent dans le même réseau

À g20, N a déjà déterminant49 et un plan discriminant7 anisotrope : N_max=N.

À g18, son espace discriminant7 a dimension4 et est non scindé. Une droite isotrope donne une sur-lattice intégrale N_max d'indice7, de déterminant49, avec plan discriminant anisotrope. Comme N_max est contenu dans N*, ses normes entières sont>=2. Le repère physique et son rang réel22 sont conservés. De plus N_max* est contenu dans N*, donc son minimum reste>=8/7.

Dans les deux cas, on recolle N_max et deux vecteurs orthogonaux y_1,y_2 de norme7. Leurs plans discriminants sont anti-isométriques. Le collage d'indice49 est unimodulaire impair de rang24. Un vecteur de norme1 y serait orthogonal à N_max par la borne duale ; il resterait dans le plan complémentaire, ce qui imposerait une somme de deux carrés entiers égale à7. C'est impossible. Son minimum est donc>=2.

Ce raccord unifie les deux valeurs : l'indice du réseau engendré par le repère physique dans N_max vaut1 ou7. Il ne transforme pas un g18 en une solution physique g20.

Preuve complète : UNIFICATION_G18_G20_RANG24.md ; second audit : AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md et AUDIT_RACINES_CORANG_UN.md.

## 2. Indécomposabilité : une preuve qui prend les42 racines ensemble

Supposer une décomposition orthogonale intégrale. Puisque le minimum est>=2, chaque vecteur de norme3 appartient entièrement à un facteur. T devient donc une matrice par blocs selon les facteurs.

L'identité T²+T=12I-C^tC impose alors que C^tC soit également par blocs. Or le graphe des42 racines D7, reliées quand leur produit est non nul, est connexe : deux supports partageant exactement un bloc ont produit+/-1, et les deux racines d'un même support se relient via un troisième bloc. Tous les42 u_o appartiennent donc au même facteur. Les sept relations y placent également tous les h_c, qui engendrent l'espace réel entier.

C'est une contradiction à toute décomposition non triviale, y compris pour N_max dont le repère peut n'engendrer qu'une sous-lattice d'indice7. Une seconde preuve utilise les sept Grams projetés simultanément : 3G=C_F C_F^t et G²=4G.

Sources : INDECOMPOSABILITE_GLOBALE.md ; AUDIT_INDECOMPOSABILITE.md ; deux programmes et sorties associés.

## 3. Les systèmes de racines de rang21 ou22 sont impossibles

Le discriminant7 de N_max est élémentaire de dimension2. Pour un système de racines de rang22, les seules composantes ADE apportant le premier7 sont A6, A13 et A20. Leurs valuations et l'indice du collage forcent la présence d'un A6 non collé. Ce facteur pair se détacherait ; aucun générateur de norme3 ne pourrait le rencontrer sous min>=2. Cela contredit le rang réel du repère.

Pour un système de rang21, on sature son espace puis on examine le complément de rang1. Le collage sur7 est cyclique et ne laisse que trois strates : une droite, un plan anisotrope, ou trois facteurs A6 avec collage au complément. Les deux premières sont exclues par l'absence de projection utilisable de norme3. Dans la dernière, les trois projections A6 coûtent au moins18/7 ; toute classe résiduelle coûte encore au moins1/2 ou4/7, donnant43/14 ou22/7, strictement supérieurs à3. Une saturation interne isotrope de A6³ coûte déjà4.

Aucun type d'étoile locale n'entre dans cette preuve. Les collages fractionnaires sont conservés ; leurs normes ne sont pas remplacées abusivement par le minimum de la lattice.

Sources : RACINES_CORANG_UN_CANDIDAT.md (statut désormais démontré après audit), AUDIT_RACINES_CORANG_UN.md ; deux implémentations finies indépendantes des classes et coûts.

## 4. Contrôle positif : l'enveloppe reste habitable

Le réseau construit ici est le complément de deux vecteurs de norme7 orthogonaux dans un réseau unimodulaire impair24 défini par un code binaire explicite. Aucun théorème de classification ni recherche bibliographique n'est requis.

Le code est engendré par X^11+X^9+X^7+X^6+X^5+X+1 et ses décalages, puis étendu par une parité. Les4096 mots ont les poids0/8/12/16/24 et les effectifs1/759/2576/759/1.

Le complément contient704 vecteurs de norme3. Vingt-deux d'entre eux ont un Gram de déterminant exactement49 : ils forment une base intégrale, donnée entièrement dans le JSON. Le support de leur Gram est connexe, donc le réseau est indécomposable. L'énumération des4096 projections démontre min(M*)>=10/7. Une preuve élémentaire de parité donne min caractéristique>=10.

Il serait faux d'appeler ce contrôle une solution locale de Conway ou un graphe. Il démontre précisément la compatibilité des propriétés arithmétiques globales ; il ne possède pas un repère physique certifié42+7. Aucun degré10 ni couplageD ni relèvement des signes n'y est affirmé.

Source, base, Gram, sorties, limites : CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md et controle_enveloppe_g20_golay.mjs/.json ; vérification indépendante : verifier_golay_enveloppe_indep.mjs/.json et son audit.

## 5. Le chaînon manquant est un repère global, pas une étoile particulière

Il faut contrôler simultanément la sélection des42 vecteurs de norme3, les sept blocs de norme4 et leurs produits prescrits, dans la lattice commune de déterminant49 ou son collage24.

Une strate concrète est déjà formalisée : si le collage possède un repère de24 ombres orthogonales de norme2, les42 vecteurs deviennent42 mots de signes de longueur24. Ils doivent se coupler à une matrice M de sept octades signées et à deux lignes B à coefficients+/-1,+/-3. Les deux ensembles de quatre gros coefficients de B sont disjoints ; huit colonnes de M ont poids1 et seize poids3. Le système entier global impose

EE^t=8(3I-T), MM^t=8I_7, ME^t=-4C,
BB^t=56I_2, EB^t=MB^t=0,
E^tE+4M^tM+B^tB=56I_24.

C'est un objet combinatoire commun et fini qui couple les sept blocs. Il garde explicitement l'hypothèse du repère d'ombres ; elle n'a pas été prouvée pour tout collage. Aucun sous-système local partiel n'est extrapolé en graphe complet.

Détails : TEMPLATE_CONDITIONNEL_SHADOW24.md.

## 6. Annexes utiles, hypothèses gardées

Les vecteurs de norme2 du réseau correspondent à des vecteurs propres entiers de carré14. Une coupe globale permet au plus un coefficient de valeur absolue2, uniquement intérieur ; sa présence force exactement six racines incidentes et quatre externes. Les autres coefficients intérieurs sont nuls. Le régime plat demeure ouvert.

Sous P=0 seulement, les quatre supports externes du régime lourd sont simples et ne peuvent tous rencontrer un même bloc : les trois régimes signés saturés produiraient alors un prisme induit. Cette famille entière est éliminée par une preuve et deux contrôles, mais les autres carriers restent ouverts.

Ces coupes ne sont pas une fermeture des normes9/10, du régime plat14 ou des deux valeurs de g. Le registre local historique demeure278 cas g18 fermés et163 ouverts, sous ses hypothèses propres P0 ; les présents théorèmes n'ajoutent pas artificiellement un nombre de types fermés.

## 7. Vérifications et livrables

Chaque impossibilité ci-dessus possède une preuve indépendante ou une seconde implémentation des ingrédients finis. Les deux vrais graphes H(2,3) et BvLS sont reconstruits et vérifiés de nouveau avec leurs paramètres propres : r=1,d=3 et r=4,d=9. Les identités signées et les repères passent. La pureté des générateurs de norme3 propre à SRG99 ne leur est pas imposée : leurs générateurs ont normes1 et4.

Aucun solveur SAT/CP/PLNE ni calcul lourd local, aucun Python local, aucun dépôt extérieur n'est utilisé dans cette reprise. Les programmes sont des vérifications JavaScript exactes bornées. Les preuves restent l'argument principal.

La poursuite n'est pas mise en pause : aucune exclusion complète de l'involution ni preuve involution=>prisme n'est obtenue.

Le fichier PREUVES_COMPLETES_ATTAQUE_GLOBALE.md rassemble toutes les preuves et audits de cette reprise. Le manifeste lié livre les SHA256 des programmes, sorties et textes. L'archive précédente de07h36 reste intacte et contient la campagne locale antérieure et toutes ses pièces historiques.


---

Pièce originale : UNIFICATION_G18_G20_RANG24.md

# Unification arithmétique g18 / g20 en un même cadre de rang24

## Énoncé et portée

Les deux cas g18 et g20 du cadre SRG99 avec involution se ramènent à un même objet : une surlattice intégrale Nmax de rang22, de déterminant49 et de discriminant7 anisotrope de dimension2, portant le frame physique original ; puis un collage unimodulaire impair U de rang24 contenant Nmax⊥7I2 primitivement sur chacun des deux facteurs.

L'unification ne supprime aucune contrainte du frame et ne constitue pas une exclusion des deux genres. Dans le cas g18, les49 générateurs engendrent un sous-réseau d'indice7 de Nmax ; ils n'engendrent pas Nmax intégralement.

## 1. Passage au déterminant49

N est le réseau physique de Gram H=3I−S, de rang réel22. Le raccord7-adique acquis donne

    det N=7^(22−g),
    A_N≅F7^(22−g),

avec discriminant non scindé. Pour g20, la dimension est2 et le discriminant est anisotrope ; poser Nmax=N.

Pour g18, la dimension est4 et l'indice de Witt est1. Choisir une ligne isotrope et la relever en une surlattice intégrale donne

    [Nmax:N]=7,  det Nmax=7^4/7²=49.

Son discriminant est le quotient de l'orthogonal de la ligne isotrope par cette ligne : il reste anisotrope de dimension2.

Le minimum dual acquis, min N#≥8/7, donne les deux bornes

    min Nmax≥2,    min Nmax#≥8/7.

La première utilise Nmax⊂N# et l'intégralité des normes ; la seconde utilise Nmax#⊂N#.

## 2. Le frame survit avec son intégralité et son incidence

Les sept v_c et les42 u_o restent des vecteurs entiers de Nmax avec le même Gram H, les mêmes relations3v_c+ΣC_co u_o=0 et le même frame7I22. Leur span réel est tout l'espace de Nmax dans les deux genres.

Le lemme INDECOMPOSABILITE_GLOBALE s'applique donc à Nmax : son minimum2 rend chaque u_o de norme3 pur dans toute décomposition, puis le carré de T et la connexité des42 directions D7 interdisent toute séparation.

La clôture primitive des sept v_c reste

    P=2Z7+Z·1,  det P=2^12,  A_P=(Z/4)^6.

Son orthogonal K dans Nmax a rang15 et déterminant2^12·49. Les42 projections des u_o dans K# restent de norme5/2, dans les42 classes d'ordre4 prescrites. Toute caractéristique de Nmax a carré2 modulo8 et norme au moins10.

Cette partie ne remplace pas les42 générateurs physiques par42 vecteurs de norme3 choisis arbitrairement.

## 3. Collage commun au rang24

Soit J=7I2 avec générateurs orthogonaux r1,r2 de norme7. Son discriminant7 est anisotrope de dimension2. Les formes discriminantes de Nmax et de J sont anti-isométriques : sur F7, les formes non dégénérées de même dimension et de même caractère déterminant sont isométriques, et changer le signe en dimension2 conserve ce caractère.

Coller le graphe d'une anti-isométrie complète donne U. Son indice sur Nmax⊥J est49, donc

    rang U=24,  det U=(49·49)/49²=1.

U est intégral impair, parce qu'il contient les u_o de norme3. Nmax et J sont primitifs dans U : le graphe du collage a une projection injective sur chacun des deux discriminants.

Si v dans U avait norme1, sa projection x sur Nmax appartiendrait à Nmax#. Le minimum dual8/7 imposerait x=0. Alors v appartiendrait à span J, et la primitivité de J donnerait v dans J, de minimum7. Contradiction. Ainsi min U≥2.

On ne déduit pas min U≥3. Des racines mixtes restent arithmétiquement possibles : pour une racine, la norme de la projection J est j/7 avec j∈{1,2,4,5}, et celle de la projection Nmax est (14−j)/7. Des racines dans Nmax lui-même restent aussi possibles.

## 4. Caractéristiques et shadowframe conditionnel

Le vecteur χ0+ r1+r2, où χ0=Σu_o, est caractéristique dans Nmax⊥J. L'indice49 est impair, donc il reste caractéristique dans U. Son carré est0 modulo8 ; toutes les caractéristiques de U ont ce même résidu.

Le frame physique et les deux produits impairs sur r1,r2 donnent min caractéristique U≥8. Les trois profils précis à norme8 sont dans SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.

Si un shadowframe de24 vecteurs orthogonaux de norme2 existe avec leurs doubles caractéristiques, le template E/M/B de TEMPLATE_CONDITIONNEL_SHADOW24 s'applique. L'existence de ce shadowframe n'est pas une conséquence démontrée de cette note.

## 5. L'indice qui conserve le genre original

Le genre original g est conservé par le sous-réseau physique :

    g20 : N=Nmax,
    g18 : [Nmax:N]=7.

Nmax est primitif dans U. N n'est pas primitif dans U pour g18. Dans les deux cas, les49 vecteurs portent toujours les sept blocs, les42 incidencesD7 et les relations entières du graphe. Une recherche dans U doit donc garder ces données et l'indice de génération, sans transformer une génération réelle en génération intégrale.

Un contre-modèle de réseau de déterminant49, de minimum3 et portant beaucoup de vecteurs de norme3 ne résout pas ces conditions du frame. Il montre seulement que le genre, les minima, les caractéristiques et l'indécomposabilité ne suffisent pas à eux seuls.

## 6. Racines : transfert des coupes acquises

Toute racine de N est une racine de Nmax. Toute borne supérieure démontrée pour le rang des racines de Nmax se transfère donc à N.

La preuve RACINES_CORANG_UN_CANDIDAT.md, dont le nom initial est conservé, interdit le rang21 dans Nmax sous les mêmes hypothèses de déterminant49, discriminant élémentaire et présence du frame réel22. Le contre-audit indépendant AUDIT_RACINES_CORANG_UN.md est acquis et traite tous les collages, y compris les classes fractionnaires hors7. Avec le rejet séparé du plein rang22, le rang des racines est donc au plus20 dans Nmax et dans N.

Cette coupe ferme uniformément les familles à21/22 directions de racines indépendantes. L'unification présente et cette borne ne font pas disparaître g18 ou g20.

## 7. Contrôle positif de l'enveloppe et verrou restant

La construction autonome CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md fournit un réseau M0 de rang22 et de déterminant49, avec discriminant7 élémentaire de dimension2, minimum3, minimum dual au moins10/7, minimum caractéristique au moins10 et aucun vecteur de norme2. Il est engendré intégralement par une base de22 vecteurs de norme3, de Gram de déterminant49 ; le support connexe de cette base le rend indécomposable. Les4096 mots du code et les704 vecteurs de norme3 orthogonaux aux deux vecteurs de norme7 sont fournis par un source autonome, sans invocation de classification des réseaux de rang24.

Le contrôle écrit du minimum dual recolle un vecteur du dual à (k r1+l r2)/7, avec |k|,|l|≤3. Si la norme duale était strictement inférieure à10/7, le vecteur recollé aurait norme3 ; or les4096 projections calculées ont toutes norme au moins11/7. Cette contradiction établit la borne10/7 du modèle, qui est plus forte que8/7.

Sources et résultats : controle_enveloppe_g20_golay.mjs et controle_enveloppe_g20_golay.json, avec la base entière22×24 et son Gram22×22. La provenance et le second contrôle sont gérés par le parent et l'audit de ce modèle ; cette note ne refait pas leur exécution.

Ce témoin n'est pas un SRG et ne porte pas un frame physique construit. Il montre que le rang, le déterminant, le discriminant, les minima, la caractéristique, l'indécomposabilité et même une génération exacte par la norme3 ne suffisent pas à fermer g20. Le verrou restant doit utiliser les QUARANTE-DEUX vecteurs sélectionnés et les SEPT blocs simultanément : leurs incidencesD7, leurs produits entiers, le carré de T et leur frame serré de constante7. Dans le cas g18, il doit aussi conserver l'indice7 du sous-réseau physique original.


---

Pièce originale : INDECOMPOSABILITE_GLOBALE.md

# Indécomposabilité uniforme du réseau global des sept blocs

## Résultat acquis

Le réseau intégral positif N de Gram H=3I−S, provenant du cadre SRG(99,14,1,2) avec involution, est orthogonalement indécomposable. Il en va de même de toute surlattice intégrale L de rang22 contenant N et de minimum au moins2.

Le lemme uniforme min N≥2 est établi séparément. Pour la surlattice de déterminant49 obtenue au genre18, min L≥2 suit de L⊂N# et min N#≥8/7 : ses normes étant entières, aucun vecteur de norme1 ne peut apparaître.

Cette fermeture concerne tous les modèles décomposés, sans hypothèse P0 et sans choix d'un type local. Elle ne ferme pas les réseaux indécomposables des genres18 ou20.

## 1. Hypothèses exactes

La matrice signée globale est

    S=[−I7  C ; Cᵀ  T],
    CCᵀ=12I7, CT=0, T²+T=12I42−CᵀC.

Les colonnes de C sont, à orientation près, les42 directions e_i+e_j et e_i−e_j, i<j, de D7. H=3I49−S est positif de rang22, et H²=7H.

Noter v_c les sept générateurs blocs et u_o les42 générateurs racines du réseau de Gram H. On a

    v_c²=4, (v_c,v_d)=0 pour c≠d,
    u_o²=3, (v_c,u_o)=−C_co,
    (u_p,u_q)=−T_pq pour p≠q.

Les relations physiques entières et le frame réel sont

    3v_c+Σ_o C_co u_o=0,
    Σ_c v_c⊗v_c+Σ_o u_o⊗u_o=7I22.

On suppose L intégral positif, de rang22, contenant ces49 vecteurs et de minimum au moins2. La première preuve utilise seulement la pureté des u_o, le carré de T et les relations physiques.

## 2. Preuve courte par la connexité de D7

Supposons L=L1⊥...⊥Lk, somme orthogonale de réseaux intégraux non nuls. Chaque composante non nulle d'un vecteur de L a norme au moins2. Comme u_o a norme3, il ne peut avoir deux composantes non nulles. Chaque u_o appartient donc à un seul facteur.

La partition des u_o par facteurs rend T diagonale par blocs : les produits de deux u_o de facteurs différents sont nuls. T² est diagonale pour la même partition. Pour p,q dans des facteurs différents, l'identité entière du carré impose

    0=(T²+T)_pq=−(CᵀC)_pq.

Les colonnes C_p,C_q doivent donc être orthogonales.

Or le graphe sur les42 directions D7, dont une arête signifie un produit non nul, est connexe. Deux directions sur des paires d'indices partageant exactement un indice ont produit±1. Le graphe des paires d'indices de K7 est connexe. Les deux directions e_i+e_j et e_i−e_j, qui sont orthogonales entre elles, sont reliées par une direction e_i±e_k avec k distinct de i,j.

Une partition de ce graphe connexe ne peut avoir toutes ses arêtes à l'intérieur des parties que si une seule partie est non vide. Tous les42 u_o appartiennent au même facteur, disons L1.

La relation 3v_c=−Σ C_co u_o place chaque v_c dans le span réel de L1. Puisque v_c appartient à L, sa projection sur les autres facteurs est nulle et v_c appartient à L1. Les49 générateurs engendrent N de rang22. Le facteur L1 a donc déjà rang22 ; les autres facteurs ont rang0. La décomposition est triviale.

L'argument ne suppose pas que L soit engendré intégralement par les42 u_o, ni que leur relation divisée par3 soit un changement de base entier.

## 3. Seconde preuve par les sept projections

Cette preuve donne un contrôle indépendant des coefficients et explique pourquoi aucun bloc ne se partage en deux racines de norme2.

Fixer un facteur Lj de la décomposition précédente. Poser α_c=proj_Lj(v_c) et G_cd=(α_c,α_d), entier. Noter Cj la sous-matrice de C sur les u_o de Lj. En projetant la relation physique puis en prenant le produit avec α_d, on obtient

    3G=Cj Cjᵀ.

Pour deux blocs distincts c,d, seules deux colonnes de C contribuent au produit : les deux directions D7 sur cette paire. Leurs contributions sont opposées. Une sous-sélection a donc somme0,1 ou−1. Comme G_cd est entier et 3G_cd égale cette somme, G_cd=0. Ainsi G est diagonale.

Le frame projeté sur Lj est

    Σ_c α_c⊗α_c+Σ_{o dans Lj} u_o⊗u_o=7I_Lj.

Appliqué à α_d, le second opérateur vaut3α_d, par la relation physique. Le premier vaut donc4α_d. En prenant tous les produits, on obtient G²=4G. G étant diagonale, chaque α_c² vaut0 ou4.

Ainsi v_c est entier dans un seul facteur : ses projections ne peuvent avoir les normes2 et2. Les deux incidences non nulles de chaque u_o imposent que ses deux blocs appartiennent à son facteur. K7 est connexe ; tous les blocs et tous les u_o sont dans le même facteur.

## 4. Ce qui rend le résultat non automatique

L'identité T²+T=12I−CᵀC est spectrale. Elle ne suffit pas seule à interdire une décomposition arbitraire de l'espace réel : les valeurs propres fournissent précisément des sous-espaces orthogonaux.

L'étape nouvelle est intégrale : un vecteur de norme3 dans un réseau de minimum2 doit être pur dans une décomposition orthogonale du réseau. Cette partition discrète des42 générateurs est ensuite incompatible avec la connexité des incidences des sept blocs. La décomposition spectrale de l'espace réel ne partitionne pas les u_o de cette façon.

Si le minimum1 était permis, un u_o pourrait se partager en composantes de normes1 et2, et la preuve ne s'appliquerait plus. Aucun résultat de cette note n'est transféré au vrai contrôle H(2,3), dont le réseau possède effectivement des vecteurs de norme1 et dont le facteur spectral est3.

## 5. Conséquences et limites

Les candidats décomposés de rang22 sont exclus uniformément comme réseaux portant ce frame global. En particulier, le modèle de genre K11⊕K11 ne peut être une telle N, indépendamment de sa vieille violation du minimum dual. Ce n'est pas une nouvelle exclusion de ce modèle : celui-ci était déjà éliminé par sa norme duale5/7. Le gain est le lemme universel d'indécomposabilité.

L'argument n'exclut pas encore les réseaux dont le système de racines de norme2 a rang21 ou22. Un système de racines se décompose orthogonalement dans son propre span, mais ses facteurs ne sont pas nécessairement des facteurs orthogonaux du réseau N : un collage peut les coupler. Cette distinction doit être gardée avant toute utilisation de classifications de racines.

Il n'est obtenu ici ni minimum3, ni absence de racines dans le collage unimodulaire24, ni exclusion de g18 ou g20.

## 6. Vérification et audit

La connexité de D7 est démontrée ci-dessus et vérifiée séparément sur42 sommets : chaque sommet a20 voisins et le graphe a420 arêtes. Le contrôle n'énumère aucun type local, graphe99 ou système de contraintes.

Les deux preuves ont été communiquées au contre-auditeur indépendant. Sa relecture confirme la première ; sa seconde vérification de 3G=Cj Cjᵀ, des contributions0/±1 et de G²=4G ne nécessite ni classification A3 ni hypothèse P0.



---

Pièce originale : RACINES_CORANG_UN_CANDIDAT.md

# Racines de corang un : fermeture uniforme contre-auditée

**Statut : démontré et confirmé par le contre-audit indépendant AUDIT_RACINES_CORANG_UN.md.** Le nom de fichier initial est conservé pour les références d'audit. Cette note ferme une famille supplémentaire et garde explicites les faits de systèmes de racines utilisés.

## Proposition acquise

Soit L un réseau intégral positif de rang22, de minimum au moins2 et de discriminant7 élémentaire de dimension2. Supposons qu'il contienne le frame physique des sept v_c de norme4 et des42 u_o de norme3, de rang réel22, avec 3v_c+ΣC_co u_o=0.

Alors le système de ses racines de norme2 ne peut avoir rang21.

Cette proposition s'applique aussi au sur-réseau maximal de déterminant49 du cas g18. Elle n'utilise pas que les42 u_o engendrent L intégralement. Le seul span réel du frame est utilisé.

## 1. Données des racines

Le système de norme2 est simplement lacé et se décompose en facteurs A,D,E. Les seuls facteurs de rang au plus21 dont le discriminant contient7 sont A6, A13 et A20. Leur partie7 est cyclique d'ordre7. Les deux possibilités de deux facteurs7 sont A6² et A13⊕A6 ; trois facteurs7 donnent A6³, avec trois dimensions de racines restantes.

Dans A_n, la classe k du dual a minimum

    k(n+1−k)/(n+1),  0≤k≤n.

Cette formule se démontre en équilibrant les coordonnées entières d'un représentant du dual. Elle donne :

- A6 : minimum de classe non nulle 6/7,10/7 ou12/7 ;
- A13 : la classe d'ordre2 a minimum7/2 ;
- A20 : les classes d'ordre3 ont minimum14/3.

Pour la partie7, A6 a coefficient6 modulo7 et A13 a coefficient5 (classe2, norme12/7). Les deux sont non carrés. Ainsi les deux formes7 des possibilités A6² et A13⊕A6 sont anisotropes en dimension2. Une droite7 non nulle est également anisotrope.

## 2. Réduction primitive de corang un

Noter R le réseau engendré par toutes les racines de norme2, de rang21, et M=L∩span_R(R) sa clôture primitive. Son complément J=M⊥∩L est de rang1 ; écrire J=<r>, r²=m.

La partie7 de R a dimension a≤3 et est élémentaire. La partie7 de M est le quotient d'un sous-espace isotrope de celle de R. Noter d la dimension du collage R→M sur7, et a'=a−2d. Le discriminant7 de M est encore élémentaire.

Le collage M⊕J→L est injectif sur chacun des deux discriminants, parce que M et J sont primitifs. Celui de J est cyclique. La partie7 du collage a donc ordre7^j, avec j=0 ou1. Écrire b=v7(m). La valuation des déterminants donne

    a'+b−2j=2.

Si j=1 et b≥2, la classe d'ordre7 dans J# a norme m/49, entière. L'isotropie du collage exigerait donc une classe isotrope non nulle dans le discriminant7 de M.

On obtient les seules strates possibles :

| Partie7 primitive M | a' | b | j |
|---|---:|---:|---:|
| droite | 1 | 1 | 0 |
| plan anisotrope | 2 | 0 | 0 |
| espace3 non saturé | 3 | 1 | 1 |

La strate a'=0 donnerait un discriminant cyclique de rang1 pour L, incompatible avec son discriminant élémentaire de dimension2. Les strates j=1,b=3 pour a'=1 et j=1,b=2 pour a'=2 sont exclues par l'absence de classe isotrope.

Dans la première strate, M vient soit d'un seul facteur7, soit de A6³ saturé par une ligne isotrope. Dans la seconde il vient des deux facteurs7 anisotropes.

## 3. Un ou deux facteurs7 non collés

Avec a=1 ou2, d=0 et j=0 : aucun collage7 ne touche les facteurs A6/A13/A20 dans L.

Si un facteur A6 apparaît, il se détache intégralement, puisqu'il n'a aucun autre premier discriminant. Un vecteur de norme3 ne peut avoir une composante non nulle dans cet A6 et une composante non nulle dans le complément, tous deux de minimum au moins2. Il ne peut non plus appartenir à A6 seul, qui est pair. Tous les u_o sont donc orthogonaux à A6, et les v_c le sont par leur relation physique. Cela contredit le rang réel22 du frame.

S'il ne reste qu'un facteur A13 ou A20, un u_o ne peut utiliser une classe non7 pour le coupler au complément : ces classes coûtent respectivement7/2 ou14/3, plus que sa norme3. Tous les u_o ont donc leur projection intégrale dans ce facteur A. La sous-lattice de L où cette classe est nulle se décompose A⊥L0. Elle est intégrale de minimum au moins2. Le même raisonnement rend chaque u_o orthogonal à A. La relation des v_c donne la contradiction de span.

Il ne suffit pas ici de dire que A13 ou A20 se détache de L : leur collage aux autres premiers peut exister. La preuve tue seulement les projections des vecteurs de norme3, puis utilise la sous-lattice où leurs classes sont nulles.

## 4. Trois facteurs A6 : saturation interne

La partie7 de A6³ a huit lignes isotropes, toutes non nulles sur les trois facteurs. Aucun plan de deux facteurs ne contient de ligne isotrope.

Pour toute classe isotrope non nulle, les trois minima de projection sont6/7,10/7 et12/7, dans un ordre quelconque. Leur somme vaut4. C'est aussi vérifiable par les216 triples de classes non nulles : l'isotropie force la somme des numérateurs à être28.

Ainsi, si M est la saturation de A6³ par une ligne isotrope, aucune classe nouvellement adjointe ne peut porter la projection d'un u_o de norme3. Dans la strate primitive restante a'=1,b=1,j=0, aucun autre collage7 n'est ajouté par L. Tous les u_o ont donc leur projection intégrale dans A6³.

La sous-lattice où ces classes sont nulles se décompose A6³⊥L0, avec minimum au moins2. Son facteur A6³ est pair, donc les u_o y sont tous orthogonaux. Le frame ne peut engendrer l'espace réel22.

## 5. Trois facteurs A6 : collage au complément de rang1

Il reste a'=3,b=1,j=1, sans saturation interne. Si la ligne de collage est nulle sur un des trois A6, cet A6 se détache et la preuve du §3 s'applique. Il faut donc que la ligne soit non nulle sur les trois A6.

Les trois dimensions de racines restantes forment A3, A2⊕A1 ou A1³. Leur clôture primitive dans leur propre span est triviale à tous les premiers autres que7 : un collage d'indice2 dans A3 ou A1³ ferait apparaître une norme1 ; A2⊕A1 a déterminant6 sans diviseur carré. Les A6 n'ont aucune partie discriminante aux autres premiers.

Comme L est unimodulaire hors7 et J est de rang1, le discriminant hors7 de M doit être cyclique et anti-isométrique à celui de J. Cela exclut A1³, dont la2-partie est (Z/2)^3. Il reste

    A3 : d0=4,   ou   A2⊕A1 : d0=6,
    m=7d0.

Considérons un u_o ayant une classe7 de collage non nulle. Ses trois projections A6 ont chacune norme au moins6/7, soit un coût total au moins18/7.

Si sa projection dans le dernier système de racines R3 a une classe non nulle, cette projection coûte au moins1/2 : c'est la borne uniforme des classes de A3 et A2⊕A1. Dès lors,

    18/7+1/2=43/14>3.

Si cette classe R3 est nulle, sa classe J hors7 est également nulle, par l'injectivité du collage. Sa projection J est donc un multiple non entier de r/7, de norme au moins m/49=d0/7. Alors

    18/7+d0/7 ≥22/7>3.

Dans les deux cas, le coût dépasse la norme3. Aucun u_o ne peut utiliser la ligne de collage7. Toutes ses projections A6 sont donc intégrales, et la sous-lattice A6³⊥L0 rend le frame orthogonal à A6³, contradiction.

## 6. Portée et contre-audit

Les points décisifs sont la primitivité M,J, la borne cyclique j≤1, l'absence de saturation non7 de R3 sous min L≥2, puis les deux coûts18/7+1/2 et18/7+d0/7. Une classe de projection du dual peut être fractionnaire ; sa norme n'est jamais remplacée par le minimum de L.

La preuve n'applique pas l'indécomposabilité d'un système de racines à celle du réseau entier. Elle garde tous les collages possibles et n'utilise la décomposition que dans une sous-lattice où les classes des42 u_o ont été prouvées nulles.

Le second audit indépendant est acquis : AUDIT_RACINES_CORANG_UN.md et verifier_corang_un_indep.mjs/.json, exécuté exact=true. Il confirme les hypothèses primitives, l'anti-isométrie complète hors7, les classes fractionnaires et les coûts. Le petit contrôle propre verifier_racines_corang_un.mjs/.json confirme également les48 classes isotropes A6³ de minimum4 et les strates arithmétiques. Ces contrôles accompagnent la preuve humaine.

Le résultat nouveau est le rejet du rang21 dans L sous les hypothèses de tête. Avec le rejet séparé du plein rang22, on obtient un rang de racines au plus20. Toute racine de N est une racine de Nmax, donc cette borne se transfère au réseau physique des deux genres.

Un contre-exemple de genre de minimum3 et sans racines est sans rapport avec cette strate de racines de rang21 ; il conserve sa fonction de limite aux arguments de genre. Aucun genre g18/g20 n'est exclu par cette proposition.


---

Pièce originale : CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md

# Un contrôle positif global de l'enveloppe arithmétique à déterminant 49

27 septembre 2026. Construction autonome ; aucun dépôt, aucun solveur. Ce réseau n'est pas un graphe de Conway. Il démontre que plusieurs contraintes globales de genre restent compatibles : il faut conserver le repère physique de 49 vecteurs, et pas seulement leurs conséquences arithmétiques.

## Énoncé

Il existe un réseau intégral positif M de rang 22 et de déterminant 49 tel que :

- son groupe discriminant est (Z/7)^2 ;
- son minimum est 3 ;
- il est engendré intégralement par ses vecteurs de norme 3 ;
- il est orthogonalement indécomposable ;
- son dual a minimum au moins 10/7, donc satisfait aussi la borne 8/7 de la campagne ;
- tous ses vecteurs caractéristiques ont un carré congru à 2 modulo 8 et un minimum au moins 10 ;
- son système de racines de norme 2 est vide.

**Statut : DÉMONTRÉ par les arguments ci-dessous, avec les ingrédients finis VÉRIFIÉS EXACTEMENT par deux voies.** La seconde voie et ses empreintes doivent être consultées dans le fichier d'audit associé avant toute annonce d'une vérification indépendante.

Il n'est PAS démontré que M possède le repère physique demandé : sept vecteurs orthogonaux de norme 4 et quarante-deux vecteurs de norme 3 de supports D7, formant ensemble un repère serré de constante 7. Aucune matrice S ni aucun srg ne sont construits ici.

## 1. Le code et le réseau de rang 24

On engendre un code C de longueur 23 par les douze décalages du polynôme

g(X)=X^11+X^9+X^7+X^6+X^5+X+1,

puis on ajoute une coordonnée de parité. L'énumération exacte donne 4096 mots, de poids 0,8,12,16,24, avec effectifs 1,759,2576,759,1. Le code est linéaire, de dimension 12, auto-orthogonal, et contient le mot tout-un. Ce sont des faits finis directement vérifiés, et non une invocation de classification.

Définir L par les vecteurs x/sqrt(8), où x est entier, avec :

1. toutes les coordonnées x_i ont la même parité m ;
2. le support des coordonnées x_i congrues à m+2 modulo 4 est un mot de C ;
3. la somme des coordonnées x_i est divisible par 8.

La linéarité de C et le mot tout-un assurent la fermeture par addition, y compris pour l'addition de deux vecteurs impairs.

Pour l'intégralité, écrire x=m1+2c+4t. Comme le poids de c est divisible par quatre, la troisième condition impose sum(t) pair. Le produit de deux tels vecteurs est divisible par huit : les termes croisés utilisent le poids divisible par quatre et c.d pair. L est donc intégral.

Les trois conditions ont respectivement les indices 2^23,2^12,2. Leur produit est 2^36. Le changement d'échelle par sqrt(8) en rang 24 a covolume 2^-36. L est donc unimodulaire.

Les vecteurs impairs ont norme au moins 24/8=3. Pour les vecteurs pairs, un carré inférieur à trois nécessiterait soit un support de deux/quatre coordonnées congrues à deux modulo quatre, exclu par les poids du code, soit une seule coordonnée +/-4, exclue par la condition de somme. Ainsi min(L)=3. Ses 4096 vecteurs de norme 3 sont exactement les vecteurs de signes associés aux mots du code, divisés par sqrt(8).

## 2. Deux vecteurs orthogonaux de norme 7

Indices de coordonnées de 0 à 23. Poser :

V={0,1,3,4,5,6,7,8,10,11,12,14},
D={0,1,2,9},
D'={3,4,13,15}.

V est un mot de poids 12. D et D' sont disjoints et contiennent chacun deux coordonnées de V et deux hors V. Avec v_i=1-2[ i dans V ], définir

y_1=(1-4 1_D)/sqrt(8),
y_2=(v-4 v 1_D')/sqrt(8).

Les conditions de L sont vérifiées directement. Les deux normes sont 7, et leur produit est nul.

Le réseau P=Z y_1+Z y_2 est primitif dans L. Une saturation non triviale aurait indice sept et serait unimodulaire de rang deux ; elle aurait un vecteur de norme un, incompatible avec min(L)=3. Par primitivité dans un réseau unimodulaire, M=P^perp dans L a rang 22, déterminant 49 et groupe discriminant anti-isométrique à celui de P, soit (Z/7)^2.

## 3. Une base de norme 3, de déterminant 49

Parmi les 4096 vecteurs de signes, exactement 704 sont orthogonaux aux deux y. Le programme en sélectionne 22 indépendants modulo 101. Leur Gram entier, donné complètement dans le JSON, a déterminant exactement 49, calculé par Bareiss avec contrôle de chaque division.

Ces 22 vecteurs forment donc une base intégrale de M : leur sous-réseau a le même déterminant que M. On obtient min(M)=3, génération par la norme 3, et rang 22 sans calcul approché.

Le support des produits non nuls de cette base est connexe (131 arêtes). Dans une décomposition orthogonale intégrale de M, chaque vecteur de norme 3 appartiendrait entièrement à un facteur puisque min(M)>=3. La connexité mettrait toute la base dans le même facteur. M est donc indécomposable.

## 4. Le minimum du dual

Tout z de M* se recolle à un vecteur b=(k y_1+l y_2)/7 de P*, avec k,l choisis entre -3 et 3. Alors z+b appartient à L et b^2=(k^2+l^2)/7<=18/7.

Si 0<z^2<10/7, le carré de z+b serait un entier positif strictement inférieur à quatre, donc égal à trois. Il serait alors l'un des 4096 vecteurs de signes.

Or les carrés de leurs projections sur M ont exactement les numérateurs suivants, sur le dénominateur sept :

| numérateur | 11 | 12 | 13 | 16 | 17 | 19 | 20 | 21 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| effectif | 8 | 12 | 32 | 336 | 336 | 1032 | 1636 | 704 |

Toutes ces projections ont donc un carré au moins 11/7. Contradiction. Ainsi min(M*)>=10/7.

Cette vérification équivaut notamment à l'absence de vecteur de norme 3 ayant simultanément des produits +/-3 avec les deux y. Elle ne postule aucune propriété d'un graphe.

## 5. Vecteurs caractéristiques

Dans L, sqrt(8)e_i est caractéristique et de carré huit : le produit avec x/sqrt(8) est x_i, et le carré d'un vecteur de L a précisément la parité commune m de ses coordonnées. Comme L est unimodulaire, ses caractéristiques diffèrent de 2L ; leurs carrés sont donc tous nuls modulo huit.

Si chi est une caractéristique de M, chi+y_1+y_2 est caractéristique sur M orthogonal P. L'indice 49 est impair, donc elle reste caractéristique sur L. Comme (y_1+y_2)^2=14, on a chi^2 congru à 2 modulo huit. M a minimum trois et est impair ; une caractéristique non nulle ne peut donc avoir carré deux, et son minimum est au moins dix.

## 6. Ce que ce contrôle autorise à conclure

Il réfute un argument d'impossibilité qui n'utiliserait que le rang 22, le déterminant 49, le groupe discriminant, les deux minima, l'indécomposabilité, l'absence de racines et la génération par des vecteurs de norme trois.

Le verrou supplémentaire est précis : sélectionner les QUARANTE-DEUX vecteurs et les SEPT blocs avec leur repère serré et les produits prescrits. Les 704 vecteurs de norme 3 de M n'ont pas été sélectionnés pour satisfaire ces conditions. Ce contrôle ne réfute ni n'établit l'existence d'une involution de Conway.

Sources et sorties : controle_enveloppe_g20_golay.mjs et .json. Tous les indices, la base 22x24 et son Gram 22x22 sont livrés dans le JSON. Aucun résultat de solveur n'intervient.


---

Pièce originale : AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md

# Audit adverse : collage, E8 et les sept blocs simultanes

Cette note utilise le MEME reseau reel N de rang22, de Gram H=3I-S, avec H^2=7H. Elle ne construit pas sept completions locales independantes. Les sept coefficient-relations ont Gram standard21I ; les colonnes -H e_c ont Gram standard28I ; les generateurs interieurs h_c de N ont Gram4I. Modulo7, beta(Hx,Hy)=x^tHy est la forme non degeneree sur im H, tandis que le produit standard y est nul.

## 1. Provenance de la borne duale

La borne min N* >=8/7 est DEJA acquise dans `outputs/dossier6_involution/NOTE_RESEAU_MINIMUM.md`, sections2-3. La premiere note de ce dossier0803 en donne un double compte exact, avec le sommet fixe qui contredit directement le cas limite. Cette borne n'est pas une nouveaute0803. Le controle court lie l'ancienne preuve et le vrai controle BvLS par leurs SHA sans recalculer le graphe BvLS localement.

Pour toute extension INTEGRALE L de N, meme de rang superieur, un vecteur w de norme1 est orthogonal a N. En effet, sa projection x sur l'espace de N appartient a N*, et x^2<=1 ; la borne duale force x=0. Dans une extension du MEME rang22, il n'y a donc aucune norme1. Dans un rang superieur, elles peuvent exister seulement dans l'orthogonal de N.

## 2. Exclusion E8 sans supposer le minimum de l'extension

Soit alpha une racine de norme2 d'une extension integrale L, et soit u un des42 generateurs de norme3. Cauchy et l'integralite donnent (u,alpha) entier de valeur absolue au plus2. Si sa valeur est2s, s=+/-1, w=u-s alpha a norme1. Par la section1, w est orthogonal a N, d'ou proj_N(alpha)=s u. Cette projection aurait norme3, superieure a alpha^2=2. Ainsi

    (u,alpha) dans {0,+1,-1}.

Si L porte un sous-systeme E8, proj_E8(u) a des produits entiers de valeur absolue au plus1 avec ses240 racines. L'argument elementaire en coordonnees montre que cette projection est nulle :

- les racines +/-e_i+/-e_j forcent toutes les coordonnees entieres ou toutes demi-entieres et |x_i|+|x_j|<=1 ;
- dans le cas entier, un seul +/-1 serait possible, mais son produit avec la demi-racine constante serait +/-1/2 ;
- dans le cas demi-entier, toutes les valeurs absolues valent1/2. L'integralite avec la demi-racine constante force un nombre pair de signes moins, donc x est une racine E8 et a produit2 avec elle-meme.

Les42 u sont donc orthogonaux a E8. Les relations physiques

    3 h_c + somme_o C_co u_o =0

impliquent que les sept h_c le sont aussi. Le sous-espace E8 est alors dans N^perp. Il ne peut exister dans une extension de rang24, dont cet orthogonal est de dimension2. La meme conclusion vaut en rang<=29. Dans N lui-meme, c'est immediatement impossible. Cette coupe ne ferme ni A/D/E6/E7, ni toutes les racines de norme2.

## 3. Collage unimodulaire24 et ses limites

On suppose ici une surlattice integrale L de N, de rang22 et determinant49, avec discriminant7 anisotrope de dimension2. Cette hypothese doit etre explicite : le determinant du N initial est7^(22-g), donc il n'est pas toujours49. Dans le regimeg18, passer a une surlattice de determinant49 exige le relèvement isotrope ancien ; ce passage ne vient pas des calculs finis de cette note.

Le discriminant de J=7I2 est egalement anisotrope sur F7. Une anti-isometrie existe, et le graphe de cette anti-isometrie dans L* direct-sum J* donne un reseau U integral, de rang24, d'indice49 dans L direct-sum J et de determinant1. Il est impair puisque J contient des normes7. L et J sont primitifs et orthogonaux dans U.

Min L* >=8/7 exclut les normes1 de U : une projection non nulle sur L aurait deja norme>=8/7 ; une projection nulle force le vecteur dans J, de minimum7. Ce collage sans normes1 et sa limite figuraient DEJA dans l'ancien dossier6.

Une racine MIXTE de U peut cependant avoir projection y=b/7 sur J et projection x dans L*, avec

    7y^2 in {1,2,4,5},
    7x^2 in {13,12,10,9} respectivement.

Ce sont des possibilites arithmetiques necessaires, pas des vecteurs construits. Elles montrent pourquoi min L>=3 n'implique pas min U>=3 : la projection x n'est pas necessairement dans L. L'exclusion E8 de la section2 s'applique a U ; la disparition de toutes ses racines n'est pas acquise.

## 4. Primitive des sept blocs et collage2-primaire

Pour toute surlattice integrale L de determinant impair contenant N, la cloture primitive des sept h_c est

    P=2Z7 + Z*ones,
    det P=2^12, A_P=(Z/4)^6.

Pour le voir, ecrire x=(1/4) somme a_c h_c. Les produits avec les h_c sont entiers. Les produits avec toutes les42 u imposent a_i+a_j et a_i-a_j divisibles par4, donc tous a_c sont0 ou tous2 modulo4. Le second cas donne z=(1/2) somme h_c. Comme z appartient a N*, 2z appartient a N et det N est impair, z appartient deja a N.

Posons K=P^perp intersect L. P est primitif, de discriminant purement2-primaire, et L est unimodulaire sur Z2. Il s'ensuit

    rang K=15,
    [L:P direct-sum K]=2^12,
    A_K,2 anti-isometrique a A_P,
    det K=2^12 det L.

Il n'y a pas d'indice impair cache, puisque le groupe de collage s'injecte dans A_P. Les projections de chaque u sur P et K sont dans P* et K*, de normes respectives1/2 et5/2. Les42 classes d'ordre4 prescrites sont distinctes. C'est un objet de reseaux portant simultanement tous les blocs ; K n'est ni ker C de dimension35 standard, ni l'orthogonal beta de dimension11/13 modulo7. Ses identites de frame sont necessaires mais automatiques a H ; le contenu supplementaire est l'existence des42 courtes classes dans le MEME K.

## 5. Trois profils caracteristiques du collage24

Le vecteur chi0=somme42 u est caracteristique sur L, de carre2 modulo8. La parite M pair a deja une preuve globale propre. Chi0+r1+r2 est caracteristique sur L direct-sum J et sur U, car l'indice49 est impair ; son carre vaut0 modulo8. Toutes les caracteristiques de U different de2U et ont donc carre0 modulo8.

Si chi est une caracteristique de U de norme8, ecrire ses projections x sur L et y sur J, ses produits racines impairs, ses produits blocs2a_c et ses produits J=b_i impairs. Le frame donne

    b1^2+b2^2+4 somme a_c^2+8n3+24n5=14.

Il n'y a que trois profils, a permutation et signe pres :

| Produits J en valeur absolue | n3 | somme a_c^2 |
|---|---:|---:|
|1,1|0|3|
|1,1|1|1|
|1,3|0|1|

Le produit racine5 est impossible et les a_c valent0,+/-1. La borne10 des caracteristiques DANS L ne s'applique pas a la projection x dans L*.

Dans le profil du milieu, l'unique racine r de produit3s touche l'unique bloc actif i et satisfait a_i C_ir=-s. Les dix voisins simples t ont tous produit (x,u_t)=-s T_rt. Cela s'obtient soit par saturation de la ligne propre demandant12, soit par reflexion chi -> chi-2s u_r : la norme8 reste inchangee, le bloc actif migre a l'autre endpoint, et aucune autre racine de produit3 ne peut etre creee. Ces contraintes ne ferment pas le profil.

## 6. Pas de reseau de racines de plein rang22

Cette nouvelle coupe utilise seulement min N>=2, la classification ADE des systemes finis de racines simplementlaces et det N=7^(22-g), avec g18/g20. Posons R le reseau engendre par toutes les racines de norme2 de N. Supposons son rang22. Alors

    v7(det R)=22-g+2 v7([N:R]).

En rang<=22, les seules composantes ADE dont le determinant est divisible par7 sont A6,A13,A20, de determinants7,14,21. Chacune apporte une valuation1 et coute au moins six rangs. Donc la valuation totale est au plus3. Pour g18, la valuation requise est au moins4 : impossible.

Pour g20, la valuation est exactement2, et [N:R] est premier a7. R contient donc soit deux A6, soit A13 et A6. Une composante A6 a discriminant exclusivement7-primaire. Le collage R subset N d'indice premier a7 ne peut avoir aucune composante non nulle sur ce facteur : A6 se detache orthogonalement dans N.

Tout u de norme3 est alors orthogonal a ce A6. Sinon sa projection A6 serait une norme paire>=2 ; une projection non nulle dans son complement integral serait de norme>=2, donnant une somme>=4. Une projection exclusivement dans A6 ne peut avoir norme3 puisque A6 est pair. Les42 u sont donc tous orthogonaux a A6, et les sept relations rendent aussi tous les h_c orthogonaux. Cela contredit le fait qu'ils engendrent N22.

Conclusion uniforme : rang R<=21. Le rang21 n'est PAS exclu et aucune absence generale de racines n'est acquise.

## 7. Controle exact borne et limites

`verifier_collage_E8_P.mjs` est une deuxieme voie independante :240 racines E8/273 candidats, determinant P par Bareiss entier,4096 classes et64 elements de2-torsion,2401 produits d'une anti-isometrie de F7^2, les trois profils caracteristiques8 et1176 reflexions. L'execution donne exact=true en environ0,2seconde. Elle ne cherche aucun graphe, n'enumere aucun catalogue local et ne remplace pas les preuves humaines de collage.

Les positifs H(2,3) et BvLS gardent leurs eigenvaleurs1/-2 et4/-5, leurs facteurs3/9 et leur premier3. Le vrai petit H(2,3) reconstruit par le controle court conserve une norme1 ; le controle BvLS acquis est lie en lecture seule. Aucune constante99/F7, P0 ou determinant49 ne leur est imposee.


---

Pièce originale : AUDIT_COMPOSANTES_RACINES_ET_CARRIER.md

# Portee adverse des composantes de racines et du carrier lourd

Ces coupes uniformes portent toutes le MEME frame reel22 et ses produits prescrits. Elles ne ferment ni toutes les racines, ni les branches courtes restantes, ni toutes les involutions.

## Produits minuscules sans hypothese de minimum sur une extension

Pour un generateur u de norme3 et une racine alpha de norme2 d'une extension integrale, (u,alpha) vaut0,+/-1. La preuve utilise la borne duale acquise8/7 : un produit+/-2 ferait une norme1 orthogonale a N, donc une projection de alpha sur N egale a+/-u, de norme3>2. Le minimum2 de l'extension n'est pas necessaire.

## D_n>=13 dans toute extension integrale de rang<=24

La projection x d'un u sur D_n a des coordonnees toutes entieres ou toutes demi-entieres, avec |x_i|+|x_j|<=1. Elle est donc0,+/-e_i ou un demi-spinor de norme n/4. Pour n>=13, le demi-spinor coute plus que3 et est impossible.

Les42 projections u contribuent alors au plus42 a la somme des normes projetees, et les sept h au plus28. Le frame est7I_N, pas7I_L. Pour E=span D_n,

    7 tr(P_E P_N)<=70,
    tr(P_E P_N)>=n-(dim L-22)>=n-2.

Pour n>=13, le membre gauche est au moins77. Cette preuve n'a pas suppose E subset N.

## D11/D12 dans N ou Nmax de rang22

Sans demi-spinor, la meme somme serait<=70, contraire a7n=77 ou84. Un u porte donc un demi-spinor.

D12 : la projection du u a deja norme3, donc u est entierement dans D12span. Adjoindre ce spinor a D12 donne un reseau integral de rang12, d'index2 et determinant1. Un sous-reseau unimodulaire se detache orthogonalement d'un reseau integral. L'indecomposabilite acquise du reseau22 interdit ce facteur.

D11 : ecrire u=p+b avec p^2=11/4 et b^2=1/4. Comme4p appartient a D11,4b=4u-4p appartient au reseau. D11 direct-sum Z(4b) a determinant16. La classe de u a ordre4, des produits entiers et norme3 ; son adjonction donne determinant1/rang12. Ce facteur est encore interdit. On n'a pas suppose que p lui-meme appartenait au reseau.

## D12 incline dans une extension de rang24

Sans demi-spinor, la trace de la premiere preuve atteint son unique valeur possible10. Chaque projection de u vaut+/-e_i, chaque h est dans E=span D12, et U=N^perp, de dimension2, est contenu dans E. Posons H0=span des sept h. Dans E, le frame s'ecrit

    Mdiag+4P_H0=7I-7P_U.

Mdiag est la matrice des nombres de projections u sur chaque axe. Les sous-espaces U,H0 et leur complement ont dimensions2,7,3 ; Mdiag a donc valeurs propres0,3,7. P_H0 est son projecteur spectral3 et est un sous-espace d'axes. Pour chaque projection u=+/-e_i, somme_c(h_c,u)^2 vaut alors0 ou4, alors que la colonne C impose exactement2. Contradiction.

Avec demi-spinor, le u est entierement dans E et engendre avec D12 un P=D12+ unimodulaire de rang12. Dans le decoupage L=P direct-sum Q, la projection de chaque u est dans P et est minuscule pour D12. Les+/-e_i n'appartiennent pas a P ; elle vaut donc0 ou un spinor de norme3. Les u sont purs dans P/Q. T et T^2 deviennent bloc-diagonaux, puis la connexite du graphe D7 non orthogonal met tous les u, et les h, dans un facteur de rang12. Leur span22 rend cela impossible. Il n'est pas necessaire de supposer min Q>=2.

Le resultat ferme D12 dans toute extension integrale de rang<=24. D11 incline dans une extension24 n'est pas ferme par cette note.

## Grandes composantes A_n

Une projection minuscule sur A_n est0 ou un poids de norme k(n+1-k)/(n+1). A norme<=3 et n>=20, k<=3 ou est le complement d'une de ces valeurs : k=4 coute deja4(n-3)/(n+1)>3. Le maximum autorise est3(n-2)/(n+1).

La trace du frame est donc au plus42*3(n-2)/(n+1)+28. Elle est strictement inferieure a7n pour n20..22 dans un reseau de rang22 contenant le frame, et a7(n-2) pour n22..24 dans une extension de rang24. Ces composantes sont exclues. A20/A21 dans une extension24 ne sont pas fermes par cette inegalite.

## Carrier lourd : les trois regimes et P0

L'unique coefficient double interieur d'une norme2 laisse six racines positives incidentes I et quatre externes E. Les capacites physiques donnent AII/BII matchings, AIE/BIE colonnes de degre<=2 et

    X-Y=12+2(eAII-eBII),
    2(eBEE-eAEE)+X-Y=16.

Il reste(eAII,eBII)=(0,2),(1,3),(0,3). Dans les deux premieres, X=8,Y=0 et BEE=C4,AEE=0. Dans la derniere, BEE=K4-e,AEE=0 et X=6+Y,Y<=2. Toute arete AIE de cette derniere branche est un double BIE dans un matching. Ces reductions n'utilisent pas P0 et ne ferment pas le cas lourd.

Sous P0 seulement, les quatre supports de blocs externes sont distincts : une paire soeur simplement adjacente donne un prisme ; une paire soeur non adjacente dans BEE a deux communs negatifs plus un commun interieur. Aucun bloc ne porte les quatre supports : les budgets de communs forcent deux labels+ et deux labels-, puis un prisme induit.

Le second controle dense `verifier_carrier_lourd_indep.mjs/.json` reconstruit les ARETES CONNUES des144 contextes. Il rejette108 contextes par un troisieme commun ; pour chacun des36 restants, il examine les210 sous-ensembles de six sommets et trouve deux triangles disjoints relies par un matching, exactement9 aretes. Cette voie ne reprend pas les masques ou le choix de temoins du producteur. Les autres carriers et les deux branches de normes2 restent ouverts.


---

Pièce originale : AUDIT_GOLAY_ENVELOPPE.md

# Audit Golay de l'enveloppe : le frame demeure essentiel

Le contre-modele `CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md` passe la relecture mathematique et une seconde implementation exacte de tous ses ingredients finis. Il satisfait une ENVELOPPE de contraintes de reseaux, mais aucun frame49 physique ni graphe SRG99 n'est realise.

## Construction et indices

Les douze translates du polynome de degre11 engendrent un code de dimension12 sur F2, et l'extension de parite le rend auto-dual en dimension24. La seconde voie utilise des tableaux de24 coordonnees et double recursivement leur span ; elle ne reprend ni les masques de bits ni la boucle sur les messages du producteur. Elle retrouve4096 mots de poids0,8,12,16,24 avec effectifs1,759,2576,759,1. Le mot constant est present, et les produits des douze generateurs sont tous pairs.

Le reseau L est forme par x/sqrt8, avec x=m*ones+2c+4t, c dans le code, et somme x divisible par8. Le poids de c etant multiple de4, cette derniere condition equivaut a somme t paire. L'addition de deux parites impaires remplace c+c' par son complement ; le mot constant du code assure la fermeture. Les poids multiples de4 et l'auto-orthogonalite rendent x.x' divisible par8.

L'index dans Z24 est2^23 pour la parite commune, puis2^12 pour le code, puis2 pour la derniere condition. Au facteur d'echelle sqrt8 en dimension24, det L=1. Pour une parite impaire, la norme est>=24/8=3. Pour une parite paire, une norme<3 requerrait soit un support modulo4 plus petit que le poids minimal8 du code, soit une unique coordonnee+/-4, qui ne satisfait pas la somme modulo8. Le minimum est donc3, et ses4096 normes3 sont exactement les vecteurs de signes du code.

Les deux y de la sortie sont dans L, orthogonaux et de normes7. Leur reseau P=7I2 est primitif : une saturation non triviale aurait index7 et determinant1 en rang2. Un reseau integral positif unimodulaire de rang2 possede une norme1, contraire au minimum3 de L. Ce dernier fait peut se voir par une base reduite : a<=c et |b|<=a/2 donnent1=ac-b^2>=3a^2/4, donc a=1.

Le complement M=P^perp intersect L a donc rang22, determinant49 et discriminant anti-isometrique a celui de P, soit(Z/7)^2. Son minimum est au moins3.

## Certificat de generation exacte

La deuxieme voie retrouve704 signes du code orthogonaux aux deux y. Elle rejoue les22 vecteurs LIVRES dans le JSON du producteur comme un certificat : membership dans le code et dans M, Gram integral et diagonale3, puis determinant49 exact.

Le determinant est calcule par elimination SYMETRIQUE rationnelle, avec fractions BigInt reduites et tous les pivots positifs. Aucun Bareiss ou choix de base modulo101 du producteur n'est repris. Le determinant49 montre que ces22 vecteurs engendrent M integralement. Le graphe de leurs produits non nuls possede131 aretes et est connexe. Sous min M=3, une norme3 doit etre pure dans une decomposition integrale ; cette connexite prouve l'indecomposabilite de M.

## Minimum dual et caracteristiques

Tout v dans M* se colle a une classe b=(k y1+l y2)/7 de P*, avec k,l entre-3 et3 ; b^2<=18/7. Si0<v^2<10/7, le vecteur v+b dans L aurait une norme entiere strictement inferieure a4, donc egale a3. Or les projections sur M des4096 signes ont toutes norme>=11/7. Les huit numerateurs et leurs effectifs, controles independamment, sont

| Numerateur sur7 |11|12|13|16|17|19|20|21|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Effectif |8|12|32|336|336|1032|1636|704|

Cela donne min M*>=10/7. On n'affirme pas que le minimum dual soit exactement10/7.

Dans L, sqrt8*e_i est caracteristique : son produit avec x/sqrt8 vaut x_i, et x^2/8 a la meme parite m que chaque x_i. Sa norme est8 ; toutes les caracteristiques de L sont donc0 modulo8. Une caracteristique chi de M se prolonge en chi+y1+y2 dans M direct-sum P, puis dans L par l'index49 impair. Elle a donc chi^2=2 modulo8. M contient des normes3, donc une caracteristique ne peut etre nulle ; min M=3 exclut le carre2 et force le carre>=10.

## Bilan adverse

Le controle est acquis : rang22, determinant49, discriminant elementaire2, minimum3, dual>=10/7, generation integrale par normes3, indecomposabilite et minimum caracteristique>=10 sont compatibles. Le reseau est sans racines de norme2.

Cette construction ne viole pas les nouvelles coupes sur les systemes de racines de grand rang : son rang des racines est0. Elle ne teste ni CT=0, ni les42 supports D7, ni les sept blocs orthogonaux, ni le tight frame7. Ces conditions portent un seul ensemble de49 vecteurs et restent le chainon manquant. Aucune involution ni SRG99 n'est construite.

`verifier_golay_enveloppe_indep.mjs/.json` a ete execute exit0 en environ0,20seconde. Un premier arret de test etait seulement la distinction JS entre+0 et-0 dans les restes ; les restes ont ete normalises avant le rejeu exact. Aucun resultat mathematique n'a ete ajuste pour faire passer le controle.


---

Pièce originale : AUDIT_INDECOMPOSABILITE.md

# Deux contre-audits de l'indecomposabilite uniforme

Hypotheses : N est le MEME reseau integral de rang22 de Gram H=3I-S, S=[-I7,C;C^t,T], avec H^2=7H et min N>=2. Les42 colonnes de C sont les42 racines D7. Les generateurs u_o de norme3 et h_c de norme4 satisfont

    (h_c,u_o)=-C_co,
    3h_c+somme_o C_co u_o=0,
    T^2+T=12I-C^t C.

Le minimum est la consequence deja acquise de min N*>=8/7. Aucune hypothese P0, catalogue local, solveur ou congruence de rang ne figure ici.

## Premiere preuve : connexite des42 lignes D7

Supposons N decompose en facteurs orthogonaux integraux. Tout u de norme3 appartient entierement a un facteur : deux projections non nulles auraient chacune une norme entiere>=2.

La matrice3I-T des produits entre les42 u est donc bloc-diagonale selon leurs facteurs. T et T^2 le sont aussi. Pour deux u_p,u_q appartenant a des facteurs distincts, l'identite T^2+T=12I-C^tC impose

    C_p^t C_q=0.

Or le graphe des42 lignes D7, avec une arete quand leur produit est non nul, est connexe. Deux supports de deux indices partageant exactement un indice ont produit+/-1. Deux soeurs de meme support, de produit0, sont reliees par une ligne utilisant un troisieme indice. Toutes les42 lignes sont ainsi connectees.

Il est impossible de partitionner les u en facteurs distincts sans qu'une arete non orthogonale traverse la partition. Tous les u appartiennent au meme facteur. Les sept relations3h_c+somme C_co u_o=0 mettent chaque h_c dans le meme sous-espace. Puisque tous les49 generateurs engendrent N, la decomposition est triviale.

## Deuxieme preuve : aucun bloc ne peut etre partage

Pour un facteur L_j, noter alpha_c la projection de h_c et C_j la sous-matrice des u appartenant a ce facteur. Les alpha appartiennent au facteur integral. Les produits des relations avec alpha donnent exactement

    3G=C_j C_j^t, G_cd=(alpha_c,alpha_d).

Pour c!=d, seules les deux lignes D7 de support{c,d} contribuent. Leurs contributions sont opposees. Toute sous-selection en donne0,+1 ou-1. Comme G est entier, 3G_cd ne peut prendre ces valeurs que si G_cd=0.

Le frame total est7I. L'operateur des generateurs u de ce facteur envoie alpha_c sur3alpha_c par la meme relation. L'operateur des projections h l'envoie donc sur4alpha_c. En prenant les produits avec les autres alpha,

    G^2=4G.

G etant diagonale, chaque projection h a norme0 ou4. Il n'y a pas de bloc partage en deux normes2. Une ligne D7 incidente a deux blocs a des produits non nuls avec eux ; leur facteur doit donc etre celui de u. Les21 paires de blocs forment K7 connexe, et tous les generateurs sont dans un unique facteur.

Cette seconde preuve valide aussi la preuve plus longue initiale par les familles F_c de taille<=2 et le reseau A3, mais elle n'a pas besoin de cette classification.

## Portee

N est indecomposable. Toute surlattice integrale L de minimum>=2, de MEME rang22 et contenant N, l'est egalement : le raisonnement met N dans un facteur unique, dont le sous-espace contient deja tout l'espace reel de L. Pour une extension de rang superieur, il prouve seulement que N est dans un facteur unique ; il ne ferme pas un complement orthogonal.

Ce resultat ne prouve ni min N>=3, ni g>=21, ni l'absence d'involutions. Les branches courtes de norme2 restent ouvertes.

`verifier_indecomposabilite_courte.mjs` controle les42 lignes,420 aretes, connexite et chemins explicites entre les soeurs ; les quatre sous-selections par paire donnant0,+/-1 ; et les seuls nombres d'incidences compatibles avec le Gram diagonal0/4. Ces verifications finies sont des certificats des etapes discretes, pas une recherche de graphes SRG.


---

Pièce originale : AUDIT_NORME1_ET_METRIQUES.md

# Audit uniforme : norme1 et trois metriques

La borne acquise est : min N* >= 8/7 pour le reseau integral N de Gram H=3I-S d'une involution du cadre SRG(99,14,1,2). Elle est DEJA prouvee dans `outputs/dossier6_involution/NOTE_RESEAU_MINIMUM.md`, sections2-3, et citee dans les anciens dossiers. La presente note en redonne un double compte exact et audite ses nouveaux raccords ; elle ne la revendique pas comme nouvelle. P0 et le choix d'un type local ne sont pas utilises. Cette conclusion n'exclut pas encore norme2, ni g18/g20, ni toutes les involutions.

## Les objets a ne pas confondre

Sur les entiers, H^2=7H et rang H=22. Le reseau N est engendre par les u_i de Gram H ; on peut concretement prendre u_i=H e_i/sqrt(7), dans l'espace propre reel de H. Les sept u_c interieurs ont Gram4I7, les42 autres generateurs ont norme3.

Avec S=[-I7,C;C^t,T], les colonnes de C sont les42 lignes de racines D7, et CC^t=12I7. Les coefficient-vecteurs n_c=(3e_c;C_c^t) satisfont Hn_c=0 et ont Gram21I7 pour le produit standard entier. Les vecteurs w_c=-He_c=(-4e_c;C_c^t) ont Gram28I7 standard. Ils ne sont pas les memes vecteurs entiers ni les memes espaces propres, meme s'ils coincident modulo7.

Modulo7, la forme sur im H est beta(Hx,Hy)=x^tHy. Elle est non degeneree. Le produit standard RESTRICTED a im H est identiquement nul, car H^2=0. Les h_c=He_c ont bien Gram4I7 pour beta. Si la forme globale de dimension g18/g20 est hyperbolique, leur orthogonal a dimension11/13, et est un espace hyperbolique de rang5/6 plus une droite carree. Aucun argument d'autodualite ne peut substituer le produit standard a beta.

## Du vecteur court a un eigenvecteur integral

Supposons v non nul dans N*, v.v <= 1, et posons a_i=(v,u_i). Les a_i sont entiers, et leur vecteur n'est pas nul puisque les49 generateurs engendrent l'espace reel de N. L'identite de frame donne

    S a = -4 a, 0 < somme_i a_i^2 = 7 v.v <= 7.

La norme restante apres un coefficient absolu2 est au plus3, donc la somme des valeurs absolues des autres coefficients est au plus3. La ligne S demanderait un total de valeur absolue8 pour une racine (diagonale0), ou6 pour un interieur (diagonale-1). Les coefficients hors diagonale sont0,+1,-1 ; c'est impossible. Une valeur absolue3 est deja exclue par la norme. Ainsi tous les a_i sont0,+1,-1, et leur support a une taille m entre1 et7.

Dans le graphe99 entier, relever a en un vecteur impair f : f vaut a_i sur le representant choisi de l'orbite, -a_i sur son mate, et0 au sommet fixe x. On a Af=-4f. Changer le representant de chaque orbite active permet de definir P de sept sommets de valeur+1 et Q=sigma(P) de sept sommets de valeur-1. Ce choix de jauge ne change pas le graphe.

## Double compte exact des communs

Posons m=|P|, A0=A[P,P], B=A[P,Q], d_i=deg_P(i) et e=e(P). B est symetrique, car sigma est un automorphisme. L'equation Af=-4f donne deg_Q(i)=d_i+4.

La somme des nombres de communs sur les paires non ordonnees de P est exactement m(m-1)-e, puisque lambda=1 et mu=2. Les contributions des sommets de P puis Q sont

    somme_i [binom(d_i,2)+binom(d_i+4,2)]
    = somme_i d_i^2 + 6e + 6m.

La contribution de tous les autres sommets est donc l'EGALITE

    D = somme_{z hors P union Q} binom(|N(z) intersect P|,2)
      = m(m-7) - 7e - somme_i d_i^2.

D est nonnegative. A m<7, le membre droit est strictement negatif. Il reste m=7 : l'egalite force e=0, tous les d_i=0 et D=0. P et Q sont independants, et B est une matrice0/1 symetrique de taille7, de somme de ligne4.

Toutes les paires de P ont exactement deux communs ; ceux-ci sont uniquement dans Q puisque D=0. On obtient B^2=2I+2J. Sur la droite constante, B a valeur propre4 ; sur son orthogonal de dimension6, ses valeurs propres sont +sqrt(2) et -sqrt(2). Leur multiplicite est la meme, parce que le polynome caracteristique est integral. Ainsi

    det(tI-B)=(t-4)(t^2-2)^3, trace B=4.

Une entree diagonale B_ii vaut1 exactement lorsque le sommet choisi dans P est adjacent a son mate. L'unique commun d'une telle paire est invariant sous sigma, donc c'est le seul sommet fixe x. Ces quatre choix sont donc interieurs. Le sommet x est hors P union Q, et sa contribution a D est binom(4,2)=6, en contradiction avec D=0.

Cela exclut tout eigenvecteur integral non nul de norme carree <=7. Comme sa norme carree est entiere, le frame donne min N* >= 8/7. Toute surlattice integrale de N dans le meme espace a donc minimum au moins2. L'argument alternatif du parent, quatre interieurs necessitant12 incidences vers les trois racines selectionnees mais chacune n'ayant que deux voisins interieurs, est egalement correct. La contribution du sommet fixe est plus courte.

## Norme2 : consequences acquises, branches ouvertes

Pour v.v=2, somme a_i^2=14. Une valeur absolue3 demanderait9 ou12 dans sa ligne, avec une norme restante5 et donc une somme absolue restante au plus5 : impossible. Il reste0,+1,-1,+2,-2. Si k coefficients ont valeur absolue2, il y a14-3k sommets dans P et autant dans Q. Un sommet positif de poids2 a au moins8-k voisins distincts dans Q. Deux tels sommets auraient au moins2+k communs dans Q. Pour k=2/3, c'est contraire a mu<=2. Donc k<=1.

Min N>=2 donne plus : a_i=+-2 sur une racine de norme3 ferait v-+u_i de norme1. Le seul coefficient double possible est interieur. Si a_c=2epsilon, v'=v-epsilon u_c est encore de norme2. Les douze racines incidentes a c ont donc a_i dans {0,-epsilon C_ci}. L'equation C a_root=-3 a_interieur impose exactement six incidences actives.

Si r autres interieurs ont coefficient absolu1, il reste4-r racines actives externes au bloc c. Chaque interieur actif requiert au moins deux de leurs incidences, car ses deux racines vers c apportent au plus1 en valeur absolue. Donc2r<=2(4-r), et r<=2. Pour r=2, les deux racines externes seraient les deux lignes D7 + et - sur la meme paire d'interieurs ; leurs charges seraient(+-2,0) ou(0,+-2), ne chargeant pas les deux interieurs requis. Ainsi r<=1.

Enfin, chaque colonne de C a une somme paire, donc C a_root=-3 a_interieur rend somme a_interieur paire. Le coefficient double est pair ; les r autres interieurs unitaires donnent r pair. Comme r<=1, il reste r=0.

Les cas k=0, et k=1/r=0, restent ouverts dans cet audit. Le rejet k>=2 et la localisation interieure du coefficient double figurent deja dans l'ancien dossier6 ; le raccord par reflexion puis parite precise la branche lourde restante. Ces bornes ne doivent pas etre annoncees comme une exclusion de norme2.

## Caracteristiques et limites

Le vecteur chi0=somme_des_42_racines u_i est caracteristique dans N. Les incidences C ont douze termes par ligne et T a dix termes non nuls par ligne ; modulo2, les produits de chi0 sont donc pairs sur les sept generateurs pairs et impairs sur les42 generateurs impairs.

Si M compte les aretes negatives du seul bloc T, chi0^2=4M-294. La preuve GLOBAL de parite donne M pair : les sept sommes de lignes de S sont impaires ; les42 autres sont paires et somment a462-4M. L'identite S^2+S=12I implique3+(497-4M)=588 modulo8, donc4M=0 modulo8.

Puisque det N est impair, les caracteristiques de N different de2N ; la meme affirmation vaut dans toute surlattice integrale d'indice impair. chi0 reste caracteristique dans une telle surlattice. Leurs normes sont donc2 modulo8. Le frame donne7chi^2>=42, car les42 produits impairs ont valeur absolue au moins1. Donc toute caracteristique a norme au moins10. Cette borne seule ne ferme pas le genre g20.

A norme10, ecrire les produits roots impairs1/3/5 et les produits blocs2a_c. L'equation est2n3+6n5+somme a_c^2=7. Le cas n5=1 est exclu par la ligne de la racine5, qui demanderait20 avec une borne12. Pour n3=n5=0, il faut distinguer SEPT demi-coefficients blocs absolus1, ou UN absolu2 et TROIS absolus1. Une reduction a un tournoi regulier K7 traite seulement le premier. Aucun argument de cette note ne ferme les six profils restants apres rejet du5.

## Controle reel et portee

`verifier_identites_courtes.mjs` controle les polynomes de double compte, les deux Grams21/28, la parite globale, les petits minorants et les sept profils arithmetiques de norme10. Ces tests ne remplacent pas la preuve humaine.

Le source reconstruit aussi directement le vrai H(2,3) a neuf sommets. Son reseau H=I-S, H^2=3H, possede un generateur de norme1 : le script le conserve et verifie son double compte avec eigenvaleur-2, sans lui imposer m=7 ni le facteur7. Le controle vrai BvLS(r4,d9,p3) acquis en0636 est lie par son SHA sans etre rerun ou traite comme SRG99. Aucun repo, Web, solveur ou Python local n'est utilise.


---

Pièce originale : AUDIT_RACINES_CORANG_UN.md

# Seconde preuve du rejet du rang21 des racines

La proposition auditee est conditionnelle et uniforme. Soit L un reseau integral positif de rang22, de minimum>=2, de determinant49 et discriminant7 elementaire de dimension2. Il contient le frame physique h_1,...,h_7,u_1,...,u_42 de rang REEL22, avec h_c^2=4, u_o^2=3 et3h_c+somme C_co u_o=0. On n'exige pas que le frame engendre L integralement. Sous ces hypotheses, les racines de norme2 de L ne peuvent avoir rang21.

Le determinant49 et la longueur2 du discriminant sont des hypotheses essentielles. Le relèvement maximal du regimeg18 doit etre fourni par la preuve ancienne ; cette note ne le cree pas. Elle ne ferme pas les reseaux sans racines ni les genres de determinant49.

## Reduction primitive et tableau entier

Supposons R, engendre par toutes les racines, de rang21. La classification ADE donne comme seuls facteurs7 A6,A13,A20, de valuations1. Il y en a a<=3. Soit M=L intersect span(R) la cloture primitive et J=M^perp intersect L=<r>, r^2=m. Les parties7 de R et M sont elementaires. La saturation interne a dimension d et laisse a'=a-2d.

Le groupe de collage M direct-sum J subset L s'injecte dans les deux discriminants, car les facteurs sont primitifs. Celui de J est cyclique, celui de M7 elementaire : sa7-partie a ordre7^j avec j<=1. Avec b=v7(m),

    a'+b-2j=2.

Les plans7 de A6^2 et A13+A6 sont anisotropes, de coefficients(6,6) ou(6,5) sur F7. Donc aucune saturation interne n'est possible dans ces plans. Une droite7 n'a pas non plus de classe isotrope non nulle. Les seules saturations possibles sont celles de A6^3, par une ligne.

Si a'=0, j=0 et b=2, le discriminant7 de L serait cyclique d'ordre49, et non elementaire de longueur2. Si a'=1,j=1, alors b=3 ; si a'=2,j=1, b=2. Dans ces deux cas, le sous-groupe d'ordre7 de J* a une norme entiere, puisque m/49 est entier. La classe de M devrait alors etre isotrope non nulle, impossible pour la droite ou les deux plans anisotropes. Il reste exactement

| a' | b | j |
|---:|---:|---:|
|1|1|0|
|2|0|0|
|3|1|1|

## Un ou deux facteurs7

Pour a=1/2 sans saturation interne, j=0 : les projections7 du collage L sont nulles. Une composante A6, dont le discriminant est exclusivement7, se detache orthogonalement dans L. Tout u de norme3 est orthogonal a cette composante paire de minimum2 : une projection non nulle coute>=2, et le reste, s'il est non nul, est un vecteur de L de norme>=2.

Sans A6, il reste A13 ouA20. La classe7 est nulle ; les seules classes non7 ont minima7/2 ou14/3, trop grands pour u^2=3. La projection de chaque u appartient donc a A13 ouA20 lui-meme. Soustraire cette projection laisse un vecteur de L. Le meme minimum2 et la parite du facteur rendent la projection nulle. Les sept relations rendent les h orthogonaux eux aussi, ce qui contredit le span reel22.

## A6^3 avec saturation interne

Dans A6, le minimum de la classe k est k(7-k)/7. Toute classe isotrope non nulle dans A6^3 est non nulle sur les trois facteurs, car les sous-plans sont anisotropes. Ses trois numerateurs de minimum sont6,10,12, dans un ordre quelconque : la somme vaut28, donc le minimum de cette projection est4.

La saturation interne par une ligne ne peut donc fournir aucune classe de projection a un u de norme3. Dans la strate a'=1,b=1,j=0, L ne rajoute aucune autre classe7. Les u ont toutes leurs projections integrales dans A6^3 ; elles sont nulles par le minimum2 et la parite, puis les h le sont aussi. Contradiction de span.

## A6^3 avec collage au complement de rang1

Il reste a'=3,b=1,j=1, sans saturation interne7. Si la ligne de collage s'annule sur un A6, ce facteur se detache et donne la contradiction precedente. Sinon ses trois composantes sont non nulles.

Les trois rangs de racines restants forment R3=A3, A2+A1 ouA1^3. Leur saturation non7 est triviale : les classes integrales non nulles d'A3 et d'A1^3 ont un representant de norme1, interdit dans L ; A2+A1 n'a aucune classe integrale non nulle. Les A6 n'ont pas d'autre premier discriminant, donc M=R.

L est unimodulaire hors7. Le collage primitif impose l'anti-isometrie COMPLETE des discriminants non7 de M et J. Celui de J est cyclique. A1^3, de discriminant(Z/2)^3, est impossible. Il reste R3=A3 de determinant d0=4 ouA2+A1 de determinant d0=6, et

    m=7d0.

Si un u utilise la classe7 de collage, ses trois projections A6 coutent au moins18/7. Si sa classe R3 est non nulle, elle coute au moins1/2, donnant43/14>3. Si elle est nulle, sa classe J non7 est aussi nulle par l'injection du collage. Sa projection J est alors un multiple non entier de r/7, de norme>=m/49=d0/7. Le cout total est>=22/7>3.

Ainsi aucun u ne peut utiliser la classe7 non nulle. Ses projections A6 sont integrales ; soustraire une projection non nulle laisserait soit un vecteur de L de norme<=1, soit un u exclusivement dans un facteur pair. Dans les deux cas c'est impossible. Les u, puis les h, sont orthogonaux a A6^3. Contradiction finale de span.

## Statut et controle

La preuve candidate `RACINES_CORANG_UN_CANDIDAT.md` passe ce contre-audit complet. Les hypotheses primitives, les classes fractionnaires et tous les collages non7 ont ete traites. La conclusion acquise est le rejet du rang21 dans L sous les hypotheses de tete. Avec le rejet separe du plein rang22, les racines de L ont donc rang<=20.

`verifier_corang_un_indep.mjs` est une seconde implementation arithmetique :216 triples de classes A6,48 isotropes de minimum4, deux plans anisotropes, toutes les strates de valuation, les discriminants de rang3, et les couts strictement>3. Les operations sont des entiers ou fractions explicites ; aucun catalogue local ni solveur n'est utilise. Ce controle accompagne la preuve humaine et ne la remplace pas.


---

Pièce originale : G18_G20_A20_FRAME.md

# Trace uniforme : grands sous-systemes A dans le meme frame

## Hypotheses

N est le reseau integral de rang22 du frame global SRG, avec sept h_c de norme4 et42 u_p de norme3. Dans toute extension INTEGRALE L contenant N, leur operateur commun est

    somme_c h_c tensor h_c + somme_p u_p tensor u_p = 7 P_N.

La borne duale acquise min(N*)>=8/7 implique que chaque u_p a produit0,+1 ou-1 avec toute racine de norme2 de L. Le raccord, valable meme si L a des normes1, est donne dans [G18_G20_E8_MINUSCULE.md](G18_G20_E8_MINUSCULE.md). On n'utilise ni P0, ni type d'etoile, ni une completion locale.

Supposons que L porte un sous-systeme A_n, dans le sous-espace E de dimension n realise par somme x_i=0 dans R^(n+1), avec les racines e_i-e_j.

## Les projections minuscules sont explicites

Pour x=proj_E(u_p), les differences x_i-x_j sont entieres et de valeur absolue au plus1. Il y a donc soit un seul niveau, auquel cas x=0, soit deux niveaux distants de1. Si k des n+1 coordonnees sont au niveau haut, la condition somme x_i=0 donne

    x_i=(n+1-k)/(n+1) sur k coordonnees,
    x_i=-k/(n+1) sur les n+1-k autres,
    ||x||^2=k(n+1-k)/(n+1).

Comme ||u_p||^2=3, seules les valeurs k telles que k(n+1-k)<=3(n+1) sont possibles. Pour n>=20, k=4 est deja exclu : 4(n-3)>3(n+1). Par symetrie k et n+1-k, et par croissance jusqu'au milieu, il reste k<=3 ou k>=n-2. Le maximum de norme projetee est donc

    q_n = 3(n-2)/(n+1).

## La trace utilise le meme espace N

Si dim L=22+d, la trace du frame sur E est

    7 trace(P_E P_N) >= 7(n-d).

En effet trace(P_E P_Nperp)<=d. En majorant chaque projection h_c par sa norme4 et chaque projection u_p par q_n, on obtient la condition necessaire

    7(n-d) <= 42 q_n + 28.

Pour une surlattice integrale de meme rang22, d=0. Cette condition echoue pour n=20,21,22. Pour une extension de dimension au plus24, d<=2 : elle echoue pour n=22,23,24. Les comparaisons entieres sont :

| Cas | n | 7(n-d)(n+1) | 42*3(n-2)+28(n+1) | Ecart strict |
|---|---:|---:|---:|---:|
| Meme rang22 | 20 | 2940 | 2856 | 84 |
| Meme rang22 | 21 | 3234 | 3010 | 224 |
| Meme rang22 | 22 | 3542 | 3164 | 378 |
| Dimension au plus24 | 22 | 3220 | 3164 | 56 |
| Dimension au plus24 | 23 | 3528 | 3318 | 210 |
| Dimension au plus24 | 24 | 3850 | 3472 | 378 |

Ainsi aucun A_n de rang n>=20 ne peut etre contenu dans N ou dans une surlattice integrale de meme rang. Aucun A_n de rang n>=22 ne peut etre contenu dans une extension integrale de dimension au plus24.

## Portee et controles

Ce sont des exclusions de familles de SYSTEMES DE RACINES dans un espace commun. Elles ne prouvent pas g>=21. A19 dans N et A21 dans une extension de dimension24 ne sont pas fermes par cette trace ; les bornes correspondantes ne sont pas strictes. La preuve n'impose jamais un frame7I sur tout L.

[G18_G20_A20_FRAME.mjs](G18_G20_A20_FRAME.mjs) controle par fractions entieres les valeurs k admissibles, le maximum q_n et les six ecarts stricts. Il inclut les deux cas-frontieres non conclus. Ce controle court ne reconstruit aucun graphe et ne fait aucune recherche locale.


---

Pièce originale : G18_G20_CARRIER_LOURD_P0.md

# Carrier externe lourd : simplicite et degre au plus3 sous P0

Cette annexe utilise les trois regimes necessaires de [G18_G20_LOURD_REGIMES.md](G18_G20_LOURD_REGIMES.md). Elle ne ferme pas la norme2 ni g18/g20.

Les quatre sommets racines positifs externes p_1,...,p_4 ont pour mates q_i=sigma(p_i). Sur ces huit sommets, les adjacences positives/positives et negatives/negatives sont nulles ; les adjacences p_i--q_j sont donnees par B=C4 ou B=K4 moins une arete. Leurs supports interieurs ont chacun deux blocs, hors du bloc lourd.

## Aucun support de blocs repete

Si deux racines externes avaient le meme support de deux blocs, ce seraient les deux orbites soeurs e_j+e_k et e_j-e_k. Elles ne peuvent etre simplement adjacentes sous P0. Pour l'expliquer sans type local : une telle arete reelle(p_i,q_j) partage un interieur L_a et fournit le triangle(p_i,q_j,L_a). Les deux autres incidences sont aux deux labels mates L_b,L_pi(b) d'un autre bloc. Le triangle(x,L_b,L_pi(b)) lui est disjoint ; les trois barreaux sont L_a--x,p_i--L_b,q_j--L_pi(b). C'est un prisme. Une paire soeurs est donc impossible si B_ij=1.

Si B_ij=0, les paires opposees du C4, ou l'unique paire manquante du K4 moins une arete, ont deja deux communs dans {q_1,...,q_4}. Deux racines soeurs positives partagent en outre un label interieur. Ce troisieme commun viole mu=2.

Les quatre supports de blocs externes sont donc distincts : leur graphe sur les six blocs exterieurs est SIMPLE.

## Un bloc ne peut porter les quatre racines

Supposons que les quatre racines touchent le meme bloc de labels L+,L-. Donner a p_i le signe s_i=+ ou- selon son label dans ce bloc ; q_i a le label oppose.

Pour B=C4, chacune des deux paires d'indices opposees a deja deux communs negatifs. Ses deux p_i ne peuvent toucher le meme label interieur, donc leurs signes sont opposes. Pour B=K4 moins l'arete(a,b), les paires(a,b) et(c,d) ont de meme deux communs negatifs et portent des signes opposes. Dans les deux cas, on a deux signes+ et deux signes-.

Il existe alors quatre indices distincts i,j,k,l tels que

    s_i=s_l=+, s_j=s_k=-,
    B_ij=B_kl=B_il=B_kj=1.

Pour C4, prendre les deux aretes disjointes reliant des signes opposes : les contraintes sur les deux paires opposees imposent que les deux autres aretes du cycle soient les barreaux requis. Pour K4 moins(a,b), utiliser les quatre aretes entre {a,b} et {c,d}; chaque paire comporte un signe+ et un signe-.

Les deux triangles

    (p_i,q_j,L+) et (p_k,q_l,L-)

sont disjoints, et leurs trois barreaux sont p_i--q_l,q_j--p_k,L+--L-. Le prisme est induit : les autres aretes entre les deux triangles seraient contraires a lambda=1, puisqu'une telle arete apporterait un second commun a une arete d'un triangle. On peut aussi constater directement que les aretes positives/positives et negatives/negatives sont absentes et que chaque racine ne touche qu'un label de ce bloc.

Cela contredit P0. Chaque bloc exterieur porte donc au plus trois des quatre racines actives.

## Portee concrete

La famille des carriers externes de degre4 est fermee UNIFORMEMENT dans les trois regimes lourds. Le graphe de leurs quatre supports a quatre aretes distinctes et degre maximum3. Les autres carriers (cycles, chemins ou triangles avec attache) ne sont pas exclus par cette annexe. Aucun placement W ni aucun type local n'a ete enumere ou suppose equivalent a un autre.

Le controle exact joint traite les3 cycles C4 et les6 K4 moins une arete etiquetes, toutes les16 affectations de labels, et retrouve36 contextes admissibles par les budgets satures. Chacun contient un prisme induit explicite de six sommets. Ce petit graphe de dix sommets est une extraction des ARETES CONNUES du carrier, jamais une pretendue completion SRG99.


---

Pièce originale : G18_G20_D11_D12_DANS_N.md

# Aucun D_n de rang au moins11 dans le reseau commun de rang22

## Hypotheses et provenance

M est une surlattice INTEGRALE de meme rang22 contenant le frame physique N. On garde les sept h_c de norme4, les42 u_p de norme3, les incidences D7 et l'operateur commun7I sur cet espace reel22. La borne duale de N donne min(M)>=2. Le meme frame rend M indecomposable ; les preuves independantes sont [INDECOMPOSABILITE_GLOBALE.md](INDECOMPOSABILITE_GLOBALE.md) et [AUDIT_INDECOMPOSABILITE.md](AUDIT_INDECOMPOSABILITE.md).

Chaque u_p a produit0,+1 ou-1 avec les racines de M. Pour un D_n dans un espace E, sa projection est donc0,+/-e_i, ou un demi-vecteur dont toutes les valeurs absolues sont1/2. La derniere norme est n/4. Ces reductions sont detaillees dans [G18_G20_D13_FRAME.md](G18_G20_D13_FRAME.md).

On traite ici D11 et D12. Le cas n>=13 est deja ferme par la trace, puisque les demi-vecteurs auraient norme>3. Aucun determinant49, type W ou P0 n'est necessaire.

## La trace force une projection spinorielle

Sans demi-vecteur parmi les projections des42 u, leur contribution totale est au plus42, celle des sept h au plus28. Mais E est dans le meme espace reel22 : le frame sur E a trace7n. Pour n=11 ou12, 7n est77 ou84, strictement superieur a70.

Il existe donc un generateur u=p+b, avec p dans E un demi-vecteur et b dans E^perp.

## D12

On a p^2=3=u^2, donc b=0. Le reseau P=D12+Z u est integral, de rang12. La classe de u a ordre2 modulo D12, et det(D12)=4 ; ainsi det(P)=4/2^2=1.

Un sous-reseau integral unimodulaire P se detache de M : les projections de chaque vecteur de M appartiennent a P*=P, donc M=P orthogonalement somme Q. Comme P a rang12<22, c'est une decomposition non triviale, contraire a l'indecomposabilite acquise.

## D11

Ici p^2=11/4 et b^2=1/4. Dans le modele D11={z dans Z11 : somme z_i paire}, 4p appartient a D11, tandis que2p n'y appartient pas. Puisque u et4p appartiennent a M, 4b=4u-4p appartient a M et a norme4.

Le reseau de base

    R=D11 orthogonalement somme Z(4b)

a rang12 et determinant4*4=16. Le vecteur u=p+b a ordre exactement4 modulo R : 4u appartient a R, tandis que les multiples1,2,3 ont une composante orthogonale b,2b,3b qui n'est pas un multiple entier de4b.

Ainsi P=R+Z u est integral, d'indice4 sur R, et det(P)=16/4^2=1. Il se detache de M comme dans le cas precedent, donnant encore une decomposition non triviale. Contradiction.

## Conclusion et limite de transport

Il n'existe aucun sous-systeme D_n de rang n>=11 dans M. Cela s'applique a N et a Nmax, puisque le raisonnement ne requiert que l'integralite et le meme espace de rang22 contenant le frame. La preuve des deux petites branches a ete relue independamment par g18_audit_neuf, qui a confirme les ordres2/4, les determinants et le raccord par indecomposabilite.

On ne transporte PAS cette indecomposabilite a un collage de rang24. La preuve specifique [G18_G20_D12_COLLAGE.md](G18_G20_D12_COLLAGE.md) y exclut D12, meme si le collage a des normes1 ; D11 en rang24 reste ouvert par les arguments presents. Aucun genre g18/g20 entier n'est exclu par cette note.


---

Pièce originale : G18_G20_D12_COLLAGE.md

# Aucun sous-systeme D12 dans un collage integral de dimension24

## Hypotheses uniformes

L est une extension INTEGRALE, de dimension au plus24, contenant le reseau/espace N22 du meme frame SRG. Les sept h_c sont orthogonaux de norme4 ; les42 u_p ont norme3 et verifient

    (h_c,u_p)=-C_cp, somme_c C_cp^2=2,
    3h_c+sum_p C_cp u_p=0,
    sum_c h_c tensor h_c+sum_p u_p tensor u_p=7P_N.

Les42 u_p engendrent deja N reel. La borne duale min(N*)>=8/7 implique qu'ils sont minuscules pour TOUTE racine de norme2 de L, meme si L contient des normes1 ; voir [G18_G20_E8_MINUSCULE.md](G18_G20_E8_MINUSCULE.md). Aucun type d'etoile ou P0 n'est impose.

Supposons un D12 de racines dans un espace E de dimension12. Les projections de chaque u_p sur E sont0,+/-e_i ou demi-vecteurs(+/-1/2)^12, ces derniers de norme3. Il faut distinguer les deux branches ; on ne peut pas transporter l'indécomposabilite de N a L sans les arguments ci-dessous.

## Aucun generateur u_p n'a une projection spinorielle

Chaque projection u_p a alors norme au plus1. La trace du frame est majoree par42+28=70, tandis que

    7trace(P_E P_N)>=7(12-(dim L-22))>=70.

Si dim L<24, la derniere borne est strictement plus grande que70. En dimension24, toutes les inegalites doivent etre des egalites :

* U=N^perp, de dimension2, est contenu dans E ;
* tous les h_c sont contenus dans E ;
* chaque projection de u_p est +/-e_i, de norme1.

Poser H0=span(h_1,...,h_7), de dimension7, orthogonal a U. En prenant le frame sur E et en notant m_i le nombre de projections u_p sur l'axe i, on obtient

    M=diag(m_i)=7I_E-7P_U-4P_H0.

Les trois espaces U,H0,(U+H0)^perp ont respectivement dimensions2,7,3, et M y vaut0,3,7. Comme M est diagonale, son espace propre3 est un ensemble de sept axes de coordonnees. C'est H0.

Pour tout u_p dont la projection vaut +/-e_i,

    somme_c (h_c,u_p)^2=4||P_H0 e_i||^2 dans {0,4}.

Mais le MEME C global donne cette somme egale a2 pour chaque racine. Contradiction. La branche sans spinor est impossible.

## Un generateur u_p a une projection spinorielle

Cette projection a deja norme3 : le generateur u_p entier est dans E. Le reseau

    P=D12+Z u_p

est integral, de rang12 et determinant1. En effet D12={z dans Z12 : somme z_i paire} a determinant4 ; le demi-vecteur u_p a ordre2 modulo D12 et norme3. L'indice est2 et le determinant est4/2^2=1.

Un sous-reseau integral unimodulaire P se detache de toute extension integrale L : la projection de tout x dans L est dans P*=P, donc L=P orthogonalement somme Q, avec dim Q<=12.

Les projections des autres u sur P sont dans P et restent minuscules pour D12. Les vecteurs +/-e_i n'appartiennent pas a P (ils ont une somme entiere impaire). Il reste0 ou des demi-vecteurs de norme3. Un u est donc ENTIEREMENT dans P ou ENTIEREMENT dans Q.

Voici le raccord de facteur qui interdit cette partition, sans supposer min(Q)>=2. Les u engendrant N reel et etant purs, cet espace est stable par les projections P/Q. Pour un facteur F parmi P,Q, poser h_cF=proj_F h_c. Ces vecteurs sont dans le facteur integral. La relation commune donne

    3(h_cF,h_dF)=sum_{u_p dans F} C_cp C_dp.

Pour c!=d, les seules colonnes concernees sont les deux racines D7 de support {c,d}, avec produits opposes+1 et-1. Le membre droit est0,+1 ou-1. L'integralite du membre gauche force (h_cF,h_dF)=0. Pour c=d, t=||h_cF||^2 donne3t=n_cF, le nombre de racines incidentes porteuses dans F.

Le frame sur h_cF, qui appartient a N reel, donne alors

    7t=t^2+n_cF=t^2+3t.

Ainsi t=0 ou4. Chaque h_c est entierement dans un facteur. Chaque paire de blocs c,d porte deux colonnes D7 non nulles sur c et d ; une telle racine u a produit non nul avec ces deux h. Ils sont donc dans le meme facteur. Le graphe des sept blocs est complet : tous les h_c et tous les u_p sont dans un seul facteur.

Ce facteur a dimension au plus12, mais ils engendrent N22. Contradiction. La branche spinorielle est elle aussi impossible.

## Portee exacte

Aucun D12 de racines n'existe dans une extension integrale de dimension au plus24 contenant ce frame commun N22. Avec [G18_G20_D13_FRAME.md](G18_G20_D13_FRAME.md), cela exclut uniformement tous les sous-systemes D_n de rang n>=12 de ces collages. La preuve ne suppose pas que D12 appartient a N, ni que L a minimum2, ni un frame7I24.

Les petits D, les A et E6/E7 restent ouverts ; cette fermeture de familles ne prouve pas encore g>=21 et n'exclut pas tous les genres g18/g20. Le source court joint verifie les chiffres de trace et les alternatives entieres de facteur, pas une completion locale ou un graphe.


---

Pièce originale : G18_G20_D13_FRAME.md

# Trace du frame : aucun D_n de rang au moins13 dans un collage24

## Hypotheses communes

N est l'espace/reseau global de dimension22 du Gram H=3I-S. Ses sept generateurs h_i ont norme4 et ses42 generateurs u_p ont norme3. Dans une extension euclidienne integrale L contenant N, le meme frame a pour operateur

    sum_i h_i tensor h_i + sum_p u_p tensor u_p =7 P_N,

ou P_N est la projection orthogonale sur l'espace de N. Ce n'est PAS 7I sur tout L si sa dimension est24.

La borne duale min(N*)>=8/7, deja raccordee dans [G18_G20_E8_MINUSCULE.md](G18_G20_E8_MINUSCULE.md), implique que toute norme1 de L est orthogonale a N. Pour toute racine alpha de norme2 de L, on a donc (u_p,alpha) dans {0,+1,-1}. Une valeur absolue2 ferait u_p-sign((u_p,alpha))alpha de norme1, mais sa projection forcerait proj_N(alpha)=+/-u_p de norme3>2. Aucun minimum>=2 de L n'est suppose.

## Projections sur un D_n

Supposons un sous-systeme D_n de racines de L, normalise par les vecteurs +/-e_i+/-e_j dans un espace E de dimension n. Pour x=proj_E(u_p), les produits avec ces racines sont entiers et de valeur absolue au plus1.

L'integralite impose x_i-x_j et x_i+x_j entiers, donc toutes les coordonnees sont entieres ou toutes demi-entieres. La borne impose |x_i|+|x_j|<=1 pour i!=j.

Ainsi x est soit0 ou+/-e_i, de norme au plus1, soit un demi-vecteur dont toutes les valeurs absolues valent1/2, de norme n/4. Pour n>=13, la seconde possibilite a norme strictement superieure a3 et est impossible pour une projection d'un u_p de norme3. Les42 projections u_p ont donc chacune norme au plus1.

La somme des normes projetees est majoree par

    sum_p ||proj_E u_p||^2 + sum_i ||proj_E h_i||^2 <=42+7*4=70.

## Le defaut commun est au plus deux dimensions

En prenant la trace du MEME frame sur E, le membre gauche vaut

    7 trace(P_E P_N).

Si dim L=22+d, alors

    trace(P_E P_N)
      =n-trace(P_E P_Nperp) >=n-d,

car P_Nperp a rang d et ses d vecteurs orthonormaux ont chacun projection sur E de norme au plus1. Cette inegalite ne suppose pas que E et N s'alignent, ni que L se decompose orthogonalement comme reseau.

Pour dim L<=24, on a d<=2. Si n>=13, la trace est donc au moins7(n-2)>=77, en contradiction avec70.

Il n'existe donc AUCUN sous-systeme D_n de rang n>=13 dans une extension INTEGRALE L de dimension au plus24 contenant N. Cela inclut les surlattices de meme espace reel N22 ; dans ce cas, la trace vaut exactement7n et le conflit est encore plus fort.

Plus generalement, lorsque n>=13, la meme preuve necessite n<=10+d dans toute extension integrale de dimension22+d. La borne n>=13 est indispensable dans le passage excluant les poids demi-entiers : elle ne permet pas d'exclure D11 ou D12, dont les poids spinoriels ont norme au plus3.

## Portee

Cette fermeture porte sur une famille de SYSTEMES DE RACINES du meme reseau/collage global, pas sur des types d'etoiles independants. Elle n'utilise pas P0. Les autres composantes A/D de petit rang/E6/E7 demeurent ouvertes ; aucune borne g>=21 ni exclusion entiere g18/g20 n'est annoncee.

La table JS jointe donne les douze ecarts stricts pour13<=n<=24. Les preuves des classes de coordonnees et du defaut de projection sont humaines ; cette table n'est pas une recherche ni une certification de graphe.


---

Pièce originale : G18_G20_E8_MINUSCULE.md

# Exclusion uniforme d'un E8 par les42 generateurs minuscules

## Hypotheses globales

N est le reseau integral reel de dimension22 engendre par les49 vecteurs du Gram H=3I49-S : sept h_i de norme4 et42 u_p de norme3. Il n'a pas de vecteur de norme1. Ses relations communes sont

    3h_i + sum_p C_ip u_p =0.

Elles impliquent que les42 u_p engendrent deja l'espace reel de N. On n'utilise ni un type W, ni P0, ni une completion separee des sept etoiles.

Un vecteur alpha de norme2 dans N, ou dans une extension INTEGRALE N' de minimum au moins2, satisfait

    (u_p,alpha) dans {0,+1,-1}.

En effet, Cauchy donne une valeur absolue au plus2, et une valeur +/-2 rendrait u_p-sign((u_p,alpha))alpha de norme3+2-4=1 dans N'. Ces projections sont donc des poids minuscules pour tout systeme de racines de N'.

## Lemme elementaire E8

Dans un espace orthonormal de dimension8, prendre les240 racines E8 : les112 vecteurs +/-e_i+/-e_j et les128 demi-vecteurs (+/-1/2,...,+/-1/2) comportant un nombre pair de signes moins.

Si x a des produits ENTIERS de valeur absolue au plus1 avec ces240 racines, alors x=0.

Les produits avec e_i-e_j et e_i+e_j imposent x_i-x_j et x_i+x_j entiers. Toutes les coordonnees sont donc entieres ou toutes demi-entieres. La borne sur ces memes racines donne |x_i|+|x_j|<=1 pour i!=j.

Dans le cas entier, au plus une coordonnee est non nulle, et elle vaut +/-1. Ce vecteur non nul aurait produit +/-1/2 avec la demi-racine (1/2,...,1/2), ce qui contredit l'INTEGRALITE.

Dans le cas demi-entier, les huit valeurs absolues sont exactement1/2. Le produit avec (1/2,...,1/2) est entier seulement si le nombre de signes moins est pair. Alors x est lui-meme une racine E8. Son produit avec cette racine vaut2 et contredit la borne1.

## Consequence pour le meme reseau global

Supposons un sous-systeme E8 de racines de norme2, dans N ou dans N'. Pour chaque u_p, sa projection x_p sur l'espace de cet E8 satisfait le lemme ; elle est donc nulle. Les relations3h_i+sum C_ip u_p=0 rendent aussi tous les h_i orthogonaux a cet E8.

Si E8 est dans N, tous ses huit axes sont orthogonaux a l'espace entier de N alors qu'ils lui appartiennent : contradiction. Une autre verification consiste a restreindre le tight frame7I a E8 : les42 u_p n'y contribuent pas et les sept h_i seuls ne peuvent fournir un operateur de rang8. La premiere preuve utilise plus fortement les relations communes et n'a pas besoin de compter ces sept rangs separement.

## Extension integrale, meme de minimum1

La borne duale uniforme acquise dans [AUDIT_NORME1_ET_METRIQUES.md](AUDIT_NORME1_ET_METRIQUES.md) donne min(N*)>=8/7. Pour expliciter le raccord, si y appartient a N* et ||y||^2<=1, ses coefficients a_i=(y,u_i) sont entiers, Sa=-4a et somme a_i^2<=7. Un coefficient absolu2 est impossible par sa ligne : il reste au plus3 en somme absolue, contre6 ou8 demandes. Si a est non nul, il est donc ternaire de support m<=7. Le double compte D=m(m-7)-7e-somme d_i^2>=0 force m>=7 ; et le cas m=7 est exclu par le lemme physique uniforme deja audite. Ainsi y=0. Comme somme a_i^2 est un entier, le premier y non nul a norme au moins8/7.

Soit L une extension INTEGRALE contenant N. Tout w dans L de norme1 a projection sur N dans N* de norme au plus1 ; cette projection est donc nulle. Toutes les normes1 de L sont orthogonales a N.

Si (u_p,alpha)=+/-2 pour une racine alpha de L, w=u_p-sign((u_p,alpha))alpha aurait norme1 et serait orthogonal a N. Sa projection nulle imposerait proj_N(alpha)=+/-u_p, de norme3, alors que ||alpha||^2=2. Contradiction. Les42 u_p restent donc minuscules pour les racines de L, MEME si L possede des vecteurs de norme1.

Un E8 de L serait par consequent contenu dans N^perp. Il est impossible lorsque dim(L)-22<8, c'est-a-dire dim(L)<=29. Cela couvre en particulier tout collage integral en dimension24. Il ne faut pas supposer un tight frame7I24 : il vaut seulement sur N22. L'integralite de L et la borne duale commune sont indispensables ; son minimum>=2 ne l'est plus.

## Portee

Cette preuve ferme uniformement une famille de SYSTEMES DE RACINES globaux : aucun sous-systeme E8 de N ni de toute extension integrale de dimension au plus29. Elle ne classe pas les composantes A/D/E6/E7, ne prouve pas l'absence de toute racine de norme2 et ne donne pas encore g>=21. Elle ne suppose pas que le choix initial des49 generateurs est invariant sous les reflexions du systeme de racines.

Le JS joint regenere les240 racines et controle exactement les273 candidats restant apres les bornes +/-e_i+/-e_j, avec des produits rationnels represented par des entiers multiples de4. Il constitue un contre-controle fini du lemme, pas une recherche de graphe.


---

Pièce originale : G18_G20_LOURD_REGIMES.md

# Trois regimes du support global lourd de norme14

## Meme vecteur, memes sommets

On utilise la reduction de [G18_G20_NORME14_LOURDS.md](G18_G20_NORME14_LOURDS.md) : une racine v de norme2 du reseau global a un unique coefficient interieur2, aucun autre interieur actif, six orbites racines actives incidentes a ce bloc, et quatre orbites racines actives externes. On oriente son eigenvecteur physique phi pour avoir phi(c+)=2 et phi(c-)=-2.

I est l'ensemble de ses six sommets racines positifs incidents : ils sont voisins de c-, pas de c+. Leurs mates sigma(I) sont voisins de c+. E est l'ensemble de ses quatre sommets racines positifs externes ; ils ne sont voisins d'aucun des deux interieurs c+,c-. Toutes ces dix racines ont poids1. On travaille sur CES sommets reels du meme graphe, pas sur des possibilites locales independantes.

Poser A=adj[I union E,I union E] et B=adj[I union E,sigma(I union E)]. A et B sont symetriques0/1, avec diagonale nulle. La diagonale de B est nulle parce que les mates racines sont non adjacents. A et B peuvent avoir simultanement une entree1 : c'est alors une paire double D reelle.

## Capacites fournies par les interieurs lourds

Le graphe induit par N(c-) est un matching. A_II est donc un matching. Pour p dans I, la paire non adjacente(c+,p) a deja le commun c- ; elle peut avoir au plus un autre commun dans sigma(I). Ainsi B_II est aussi un matching.

Pour e dans E, les paires(e,c+) et(e,c-) sont non adjacentes. Elles montrent que chacune des colonnes B_IE et A_IE comporte au plus deux1. En particulier

    X = nombre de1 de B_IE <=8,
    Y = nombre de1 de A_IE <=8.

L'equation propre Agraph phi=-4phi impose, sur les dix racines positives,

    B1-A1 = 2 sur I,
    B1-A1 = 4 sur E.

Les deux unites deja recues par I proviennent du voisin c- de poids-2. La sommation sur I donne

    X-Y = 12+2(a-b),

ou a=e(A_II) et b=e(B_II). Les deux matchings donnent a,b<=3 ; X<=8 et Y>=0 imposent b-a>=2. Il reste seulement

    (a,b) = (0,2), (1,3), (0,3).

Chaque p dans I a au moins un voisin dans sigma(E) : sa ligne propre donne t_p=2+deg_AII(p)+deg_AIE(p)-deg_BII(p)>=1. Les quatre racines externes ne sont donc pas un decor libre : elles recoivent entre6 et8 incidences opposees depuis I.

## Matrices externes forcees

La sommation sur E donne

    e(B_EE)-e(A_EE)=(16-(X-Y))/2.

Si X-Y=8, alors X=8,Y=0 et cette difference vaut4. Si X-Y=6, elle vaut5.

Un B_EE complet K4 rend chaque paire de sommets positifs externes deja commune a deux sommets negatifs externes. A_EE ne pourrait donc contenir aucune arete. Cela contredit la difference4 ou5 ; B_EE n'est jamais complet.

Pour une difference4, l'autre possibilite a examiner est e(B_EE)=5 et e(A_EE)=1. Comme Y=0, chaque sommet externe satisfait

    colonne(B_IE)=4-deg_BEE+deg_AEE <=2.

Les deux sommets de degre2 de B_EE ne peuvent toucher l'arete A_EE. Celle-ci serait donc entre les deux sommets de degre3, qui ont deja deux communs dans sigma(E). C'est impossible pour une paire adjacente (lambda=1). Il reste e(B_EE)=4,A_EE=0. La meme formule impose deg_BEE>=2 partout, donc B_EE est un C4.

Pour une difference5, la seule possibilite restante est B_EE=K4 moins une arete,A_EE=0.

## Tableau exact des regimes necessaires

| Regime | a=e(A_II) | b=e(B_II) | B_EE | A_EE | X | Y |
| --- | ---: | ---: | --- | --- | ---: | ---: |
|R1|0|2|C4|0|8|0|
|R2|1|3|C4|0|8|0|
|R3|0|3|K4 moins une arete|0|6+Y|0,1 ou2|

R1/R2 : toutes les colonnes de B_IE ont degre2. Ses lignes ont degres(2,2,1,1,1,1). En R1, les deux lignes de degre2 sont les deux sommets non couverts par B_II. En R2, ce sont les deux sommets couverts par A_II. Dans R2, ces deux lignes n'ont aucun voisin commun dans sigma(E), car leur paire est adjacente et a deja c- comme commun.

R3 : les deux sommets de l'arete manquante de B_EE ont chacun degre2 dans B_IE et degre0 dans A_IE. Les deux autres ont degre1 ou2 dans B_IE, et respectivement0 ou1 dans A_IE. Cela impose X=6+Y et Y<=2.

Toute arete A_IE en R3 est AUSSI une arete B_IE. En effet, soit p dans I adjacent a e dans E. Une telle colonne e ne peut etre qu'un sommet de degre3 dans B_EE. Si p a d voisins dans E, sa ligne propre donne1+d voisins dans sigma(E). Parmi eux, au moins1+d-[e dans B_IE(p)] sont aussi voisins de e, puisque e est adjacent aux trois autres sommets de sigma(E). Le plafond lambda=1 force d=1 et e dans B_IE(p). C'est une paire double D. Ces aretes A_IE forment un matching : deux doubles incidents a une meme orbite fourniraient quatre communs a ses deux mates, contre mu=2.

## Portee et circularite

La preuve utilise des capacites physiques(lambda,mu), le meme eigenvecteur et les deux interieurs fixes de son support. Elle n'impose pas CT=0 une seconde fois en l'appelant nouveau filtre. Elle ne requiert pas P0 ; P0 pourra ajouter la disjonction des supports de bloc pour D et l'absence d'aretes entre soeurs.

Ce tableau ne prouve pas que ces trois regimes ont des completions. Il ne les exclut pas non plus : les racines de coefficient0, les contraintes T/W globales et les budgets restants sont toujours necessaires. Aucune conclusion g>=21, aucune exclusion entiere g18/g20, ni aucun graphe ne sont revendiques.

Le petit JS joint teste les4096 paires de graphes externes etiquetes pour chaque difference et la consequence locale de lambda en R3. Il ne cherche ni les matrices globales42, ni une completion SRG.


---

Pièce originale : G18_G20_NORME14_LOURDS.md

# Coupe uniforme sur les coefficients lourds d'une norme2

## Cadre commun

On suppose un SRG(99,14,1,2) avec l'involution du cadre : un sommet fixe x, sept orbites interieures et42 orbites de racines. Le secteur impair est

    S = [[-I7,C],[C^t,T]],
    CC^t = 12I7, CT = 0, T^2+T = 12I42-C^t C.

Les42 colonnes de C sont les racines e_i+e_j et e_i-e_j, une paire par support {i,j}. Le changement simultane de signe d'une colonne et de sa coordonnee est seulement une convention pour representer son orbite.

Pour le raccord au reseau, H=3I49-S est le Gram de sept generateurs h_i de norme4, orthogonaux, et42 generateurs u_p de norme3. On suppose un reseau integral contenant ces generateurs et un vecteur v de norme2. Le tight frame donne

    a=( (v,h_i), (v,u_p) ),
    sum a_i^2=7||v||^2=14, Sa=-4a,
    C a_roots=-3 a_interieurs.

Le vecteur impair physique phi prend a_i et -a_i sur les deux sommets de chaque orbite, et0 sur x. Ses valeurs satisfont A phi=-4phi. Cauchy donne |a_i|<=2, puisque les normes des generateurs sont4 et3. Aucune hypothese P0 n'est utilisee dans les coupes qui suivent.

## Deux coefficients lourds sont impossibles

Ce lemme s'applique aussi directement a tout eigenvecteur impair entier de norme14 sur les49 orbites, avec coefficients dans {0,+1,-1,+2,-2}.

Soit k le nombre d'orbites dont le coefficient a une valeur absolue2, et l le nombre de coefficients de valeur absolue1. Alors4k+l=14, donc k<=3. Chacun des ensembles P={phi>0} et N={phi<0} contient m=k+l=14-3k sommets, avec k sommets de poids2.

Pour un sommet p de P de poids2, l'equation propre impose

    somme des poids des voisins de p dans N
      =8+somme des poids des voisins de p dans P >=8.

Il a donc au moins8-k voisins DISTINCTS dans N : les k poids2 peuvent apporter seulement k unites au-dela du nombre de voisins. Si k>=2, deux sommets lourds p,q de P ont au moins

    (8-k)+(8-k)-(14-3k)=2+k

voisins communs dans N. C'est au moins4, alors que toute paire distincte d'un SRG(99,14,1,2) a au plus2 voisins communs. Contradiction. Ainsi k<=1.

Cette coupe ne postule ni un type W, ni des prolongements locaux independants, ni un residu propre a une etoile.

## Raccord au minimum du reseau

Pour la suite seulement, on utilise le lemme uniforme excluant les vecteurs de norme1 : le reseau integral considere a minimum au moins2. Cette propriete est une hypothese explicite de cette section ; les booles d'un moteur ne la prouvent pas.

Si (v,u_p)=+/-2, alors v-sign((v,u_p))u_p est un vecteur du meme reseau de norme

    2+3-2*2=1.

Il est non nul et contredit ce minimum. Tous les coefficients racines appartiennent donc a {0,+1,-1}. Par le lemme precedent, il reste soit aucun coefficient lourd, soit un unique coefficient interieur a_i=2 epsilon, epsilon dans {+1,-1}.

## Un lourd interieur laisse au plus un autre interieur actif

Supposons a_i=2 epsilon. Le vecteur v'=v-epsilon h_i appartient au meme reseau et conserve la norme2. Sur une racine p incidente a i, sa coordonnee devient

    a'_p=a_p+epsilon C_ip,

car (h_i,u_p)=-C_ip. Les coefficients racines de v et de v' ont tous valeur absolue au plus1. Ainsi

    a_p dans {0,-epsilon C_ip}

sur les12 colonnes incidentes a i. La relation C a_roots=-3 a_interieurs impose que exactement6 de ces colonnes aient un coefficient non nul.

Soit r le nombre des autres interieurs actifs. Le lourd consomme4 unites de norme ; les10 restantes sont des coefficients +/-1. Il reste donc10-r racines actives, dont6 incidentes a i et4-r hors i.

Pour chaque autre interieur actif j, la charge demandee est +/-3. Les deux racines sur le support {i,j}, si toutes deux sont actives, donnent des contributions opposees a j ; si une seule est active, sa contribution vaut +/-1. Leur contribution totale a une valeur absolue au plus1. Les racines hors i doivent donc apporter une valeur absolue au moins2 a j, et comportent au moins deux incidences a j.

Il y a au total2(4-r) incidences de racines hors i. Donc2r<=2(4-r), soit r<=2. Si r=2, chaque incidence des deux racines hors i doit appartenir aux deux interieurs actifs j,k. Ces racines ont necessairement le meme support {j,k} et sont les deux racines distinctes e_j+e_k et e_j-e_k. Avec coefficients +/-1, leurs deux charges sont

    (alpha+beta,alpha-beta), alpha,beta dans {+1,-1}.

L'une est nulle, l'autre vaut +/-2. Elles ne peuvent donc apporter une valeur absolue2 aux DEUX interieurs actifs. Contradiction. Ainsi r<=1.

Il reste a imposer la parite du MEME C global. Chaque colonne D7 a une somme paire, donc C a_roots=-3 a_interieurs implique somme(a_interieurs)=0 modulo2. Le lourd est pair ; le nombre r d'autres interieurs actifs est donc pair. Comme r<=1, on obtient r=0. Le cas lourd restant a exactement la forme suivante :

| Autres interieurs actifs | Racines actives incidentes au lourd | Racines actives hors de son bloc |
| ---: | ---: | ---: |
|0|6|4|

La reflexion v -> v-epsilon h_i remplace les six racines incidentes actives par les six complementaires et change le signe du lourd. Elle ne justifie aucune equivalence entre placements physiques W/ombres.

## Portee et reste ouvert

La contradiction k>=2 est prouvee par les budgets SRG reels. Le raccord au minimum et la reduction r<=1 sont des contraintes uniformes du MEME reseau et du MEME vecteur global. Elles ne sont pas issues d'assemblages de Schur locaux.

Dans le cas sans lourd, la meme parite impose un nombre pair d'interieurs actifs. La capacite3r<=2(14-r) donne r<=5, donc r dans {0,2,4}.

Restent ouverts le cas sans lourd (14 coefficients +/-1) et l'unique forme lourde du tableau. Aucun minimum>=3 n'est acquis ici ; aucune borne g>=21 ni exclusion entiere g18/g20 n'en decoule encore. Le petit source JS joint verifie seulement les capacites finies et les identites de signes utilisees, pas l'existence ou l'inexistence d'un graphe.


---

Pièce originale : G18_G20_STATUTS_ET_PARAMETRES.md

# Statuts des coupes uniformes et parametres des controles positifs

Toutes les nouvelles pieces ci-dessous utilisent les memes49 generateurs dans le meme espace N de rang22. Elles ne recollent pas des etoiles independantes. Dans une extension de rang superieur, l'operateur du frame vaut7P_N, jamais7I sur l'extension entiere.

## Familles fermees et branches restantes

| Objet | Resultat acquis | Hypotheses supplementaires / portee |
|---|---|---|
| Borne duale | min(N*)>=8/7 ; toute norme1 d'une extension integrale est orthogonale a N | Borne ancienne, raccord physique audite ; aucune nouveaute revendiquee |
| Indecomposabilite | N et toute surlattice integrale de meme rang22 sont indecomposables | Meme frame D7 ; min>=2 vient de la borne duale |
| E8 | Aucun E8 dans une extension integrale de dimension<=29 | Minuscule + les42 u engendrent N reel ; pas de minimum2 suppose pour l'extension |
| D_n dans rang22 | Aucun D_n pour n>=11 | Trace + facteur unimodulaire + indecomposabilite |
| D_n dans rang<=24 | Aucun D_n pour n>=12 | D12 traite separement les branches spinorielle et non spinorielle ; D11 reste ouvert |
| A_n dans rang22 | Aucun A_n pour n>=20 | Trace rationnelle, produits minuscules |
| A_n dans rang<=24 | Aucun A_n pour n>=22 | Meme trace avec defaut commun au plus2 ; A20/A21 restent ouverts |
| Racines, rang total | Rang<=20 dans Nmax et N | Det(Nmax)=49 et discriminant7 elementaire de dimension2, plus les preuves independantes du plein rang et du corang1 |
| Coefficient lourd d'une norme2 | Si un coefficient double est present : il est unique et interieur ; six racines incidentes et quatre externes ; tous les autres interieurs nuls | Reflexion et parite, sans P0 ; le cas plat reste ouvert |
| Carrier lourd | Les quatre supports externes sont distincts et leur graphe simple a degre maximal3 | P0 seulement pour cette annexe ; les regimes restants ne sont pas fermes |

La borne de rang des racines a ses propres hypotheses de determinant/discriminant, exposees dans [AUDIT_RACINES_CORANG_UN.md](AUDIT_RACINES_CORANG_UN.md). La table ne remplace aucune de ces hypotheses par une consequence implicite du genre.

Sources des nouvelles familles : [E8](G18_G20_E8_MINUSCULE.md), [D>=13 par trace](G18_G20_D13_FRAME.md), [D11/D12 de meme rang](G18_G20_D11_D12_DANS_N.md), [D12 en rang24](G18_G20_D12_COLLAGE.md), [A>=20 par trace](G18_G20_A20_FRAME.md), [regimes lourds](G18_G20_LOURD_REGIMES.md) et [carrier P0](G18_G20_CARRIER_LOURD_P0.md). Chaque source JS joint ne controle que les etapes finies annoncees ; aucune sortie ne pretend reconstruire un SRG.

## Parametres anonymes du cadre signe

Pour les positifs, on garde leurs propres parametres. Dans le cadre signe general, ecrire S=[-I_m,C;C^t,T], avec valeurs propres r et-(r+1). Poser

    H=rI-S, H^2=(2r+1)H,
    ||h_c||^2=r+1, ||u_p||^2=r,
    r h_c + somme_p C_cp u_p=0,
    CC^t=2(m-1)I=r(r+1)I.

La relation entre m et r vaut pour les exemples physiques ici controles, pas pour une matrice arbitraire. Le nombre de colonnes racines est m(m-1), et le rang reel du frame est

    rank(H)=m(1+mr)/(2r+1).

| Controle | Sommets | m | r | Constante du frame | Normes h/u | Rang H |
|---|---:|---:|---:|---:|---|---:|
| H(2,3) | 9 | 2 | 1 | 3 | 2 / 1 | 2 |
| Hypothese SRG99 | 99 | 7 | 3 | 7 | 4 / 3 | 22 |
| BvLS | 243 | 11 | 4 | 9 | 5 / 4 | 55 |

[controles_positifs_cadre_global.mjs](controles_positifs_cadre_global.mjs) reconstruit les deux graphes positifs et controle leurs vrais comptes communs, le polynome de S, le frame et les incidences. Son resultat existant est exact=true :36 paires du petit graphe et29403 paires BvLS. Aucun nouveau calcul positif n'est necessaire pour cette cloture documentaire.

Ces positifs valident la normalisation du cadre. Ils ne satisfont pas les hypotheses norm3/norm4/constante7 des exclusions ci-dessus : H(2,3) possede des normes1, et BvLS a des generateurs racines de norme4. On ne leur impose donc ni min(N*)>=8/7, ni determinant49, ni premier7, ni P0, ni les bornes E8/D/A specifiques au frame SRG99.

## Ce qui n'est pas prouve

Aucune borne g>=21, aucune exclusion uniforme des genres g18/g20, aucun graphe certifie, aucune fermeture des classes de racines plus petites n'est produite. Le contre-modele d'enveloppe Golay de rang22 et determinant49 reste coherent avec les contraintes de genre citees : il ne porte pas de frame physique49 construit. Le verrou restant est donc l'existence simultanee du frame, de ses incidences D7 et des produits entiers des42 colonnes ; il ne suffit pas de repeter les seules contraintes de genre.


---

Pièce originale : SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.md

# Sept blocs, caractéristiques et collage : contraintes globales acquises

Cette note conserve un objet intégral portant simultanément les sept blocs. Elle ne donne aucune exclusion globale de g18 ou g20. Le minimum dual 8/7 était déjà présent dans les rapports antérieurs ; il n'est pas présenté comme une nouveauté. La borne10 pour les caractéristiques et les trois profils du collage de rang24 sont des contraintes arithmétiques supplémentaires.

## 1. Hypothèses et métriques

On suppose le cadre signé entier provenant d'une involution de SRG(99,14,1,2), avec un sommet fixe :

    S = [−I7  C ; Cᵀ  T],   S²+S=12I49,
    CCᵀ=12I7, CT=0, T²+T=12I42−CᵀC.

Les42 colonnes de C sont, à un changement de signe de chacune près, les42 racines e_i+e_j et e_i−e_j, i<j, de D7. T est symétrique, de diagonale nulle, avec10 coefficients ±1 par ligne. P0 n'est utilisé nulle part dans cette note.

Poser H=3I49−S. Sur les réels, H²=7H et rang H=22. Le réseau N est l'image de Z49, de Gram H. Dans le modèle euclidien on prend les générateurs H e_i/√7. Les sept générateurs blocs v_c ont Gram4I7 ; les42 autres générateurs u_o ont norme3.

Il faut distinguer trois produits :

- les coefficients w_c=−H e_c ont Gram standard28I7 ;
- les coefficients n_c=(3e_c;C_cᵀ) appartiennent à ker H et ont Gram standard21I7 ;
- les v_c ont Gram4I7 dans N.

Dans la forme modulo7 sur im H, β(Hx,Hy)=xᵀHy, les h_c=He_c ont également Gram4I7 ; le produit standard sur im H est nul. On ne substitue pas cette forme modulo7 à la métrique réelle de N.

Pour un vecteur x dans l'espace réel de N, l'identité de frame est

    Σ_c (x,v_c)² + Σ_o (x,u_o)² = 7(x,x).

Si x appartient à N#, ses49 produits sont entiers et forment un coefficient-vecteur propre de S, de valeur propre−4.

## 2. Clôture primitive exacte des sept blocs

Soit L une surlattice intégrale de N de déterminant impair, avec indice [L:N] impair. N lui-même est autorisé. Dans le cas g20, L=N et det L=49 ; dans le cas g18, le relèvement maximal isotrope du discriminant donne une telle L avec [L:N]=7 et det L=49.

La clôture primitive P dans L de V=Σ Z v_c est universelle :

    P = V + Z z,   z=½Σ_c v_c,   [P:V]=2.

En coordonnées orthonormées v_c=2e_c, cela signifie

    P=2Z7+Z·1,    z²=7,    det P=2^12.

En effet, si x appartient à L et au span réel des v_c, ses produits entiers avec les v_c donnent x=¼Σ a_c v_c avec a_c entier. Ses produits avec toutes les u_o imposent a_i+a_j et a_i−a_j divisibles par4. Les sept a_c sont donc tous0, ou tous2, modulo4. Ces conditions montrent aussi que z appartient à N#. Or 2z appartient à N et N#/N est d'ordre impair, donc z appartient déjà à N. Il n'existe aucun autre élément de la clôture.

On a P#=½D7. Par conséquent

    A_P=P#/P ≅ D7/(4Z7+2Z·1) ≅ (Z/4)^6.

Le groupe a4096 éléments et son sous-groupe de2-torsion64 éléments. Cette vérification est également effectuée directement dans le source propre.

Poser K=P⊥∩L. Alors rang K=15. Puisque P est primitif et L est unimodulaire sur Z2, le collage2-primaire est complet et anti-isométrique :

    [L:P⊕K]=2^12,  A_K,2 ≅ −A_P,
    det K=2^12 det L.

Aucun indice impair supplémentaire n'est caché ici : A_P est2-primaire, donc L/(P⊕K) est2-primaire. Pour det L=49, K a déterminant2^12·49=200704.

K est un réseau réel de rang15. Ce n'est ni ker C de dimension35, ni l'orthogonal modulo7 de dimension11/13, ni l'ancien L_T dans la métrique standard des coefficients. Les anciens indices calculés dans le réseau propre des coefficients donnent un objet dual ; cette note ne renomme pas cet ancien résultat en exclusion nouvelle.

## 3. Les42 classes de norme5/2 prescrites

La projection de u_o sur P a les coordonnées

    p_o=−½(e_i±e_j),   p_o²=½.

Elle représente une classe d'ordre4 de A_P. Les42 classes correspondant aux42 colonnes orientées de C sont distinctes : la différence de deux racines D7 ne peut être uniformément2 modulo4, puisqu'elle a au moins trois coordonnées nulles ; si elle est nulle modulo4, les deux racines sont égales.

La projection q_o=u_o−p_o sur K appartient à K# et satisfait

    q_o²=5/2.

Sa classe dans A_K,2 est celle prescrite par l'anti-isométrie de collage. On obtient donc un problème intégral uniforme : un réseau K de rang15 et de déterminant200704 doit porter42 vecteurs du dual de norme5/2, dans42 classes d'ordre4 prescrites par le code des sept blocs.

Les relations Σ_o C_co q_o=0 et le frame Σ_o q_o⊗q_o=7I15 sont nécessaires. Elles sont des projections de relations déjà présentes dans H ; seules, elles ne constituent pas une obstruction nouvelle. Le contenu intégral est le collage simultané des42 classes.

## 4. Toute caractéristique de N ou L a norme au moins10

Un vecteur χ de L est caractéristique lorsque (χ,x)≡x² modulo2 pour tout x dans L. Ses produits avec les42 u_o sont impairs, et ceux avec les sept v_c sont pairs. Le frame donne χ²≥42/7=6.

Le vecteur χ0=Σ_o u_o est caractéristique dans N : chaque ligne de C a12 coefficients non nuls, et chaque ligne de T en a10. Modulo2, χ0 a les produits pairs voulus sur v_c et impairs voulus sur u_o. Il reste caractéristique dans une surlattice d'indice impair : si mx appartient à N, m impair, l'identité sur mx donne celle sur x.

Écrire M pour le nombre d'arêtes négatives dans T. Alors

    χ0² =126−1ᵀT1=4M−294.

Pour vérifier M pair sans P0, choisir C sous sa forme canonique. Les sept sommes de lignes de S sont impaires, les42 autres sont paires et leur somme vaut462−4M. Puisque b²≡2b modulo8 pour b pair,

    ||S1||²≡7+2(462−4M)≡3 modulo8,
    1ᵀS1=497−4M.

L'identité S²+S=12I impose3+(497−4M)≡588 modulo8, donc M est pair. Ainsi χ0²≡2 modulo8.

Det L étant impair, les caractéristiques diffèrent de2L. L'identité χ'=χ+2x donne χ'²−χ²=4[(χ,x)+x²], multiple de8. Toutes les caractéristiques ont donc carré2 modulo8. Avec la borne6 du frame, on obtient

    min{χ² : χ caractéristique de L} ≥10.

Cette conclusion est plus précise qu'une contrainte sur les valeurs propres de S. Elle ne suppose pas min N≥3. Le lemme uniforme min N≥2 et la borne min N#≥8/7 sont démontrés séparément dans l'audit des vecteurs courts.

## 5. Profils exacts à norme10, et un tournoi portant les sept blocs

Écrire (χ,v_c)=2a_c. Les produits racines sont impairs. La norme10 donne

    2n3+6n5+Σ a_c²=7,

où n3 et n5 comptent les produits de valeur absolue3 et5. Il ne peut y avoir de valeur absolue supérieure à5, par le frame. Le cas n5=1 impose n3=0 et un seul |a_c|=1. La ligne de la racine5 demanderait20, mais les10 contributions T et les deux contributions blocs donnent au plus12 : contradiction. Donc n5=0.

Les six profils restants sont :

| n3 | Demi-coefficients blocs non nuls |
|---:|---|
| 0 | sept valeurs absolues1 |
| 0 | une valeur absolue2 et trois valeurs absolues1 |
| 1 | cinq valeurs absolues1 |
| 1 | une valeur absolue2 et une valeur absolue1 |
| 2 | trois valeurs absolues1 |
| 3 | une valeur absolue1 |

Dans le premier profil seulement, orienter les sept blocs pour avoir a_c=1. Les produits racines ε_o valent±1, et l'équation des blocs devient Cε=−6·1. Pour une paire {i,j}, les deux racines donnent

    ½[(e_i+e_j)ε_+ +(e_i−e_j)ε_-] ∈ {±e_i,±e_j}.

La somme des21 contributions vaut−3·1. Leur somme totale est−21, donc chacune est négative. Chaque paire choisit un de ses deux endpoints, et chaque endpoint reçoit trois paires. C'est exactement un tournoi régulier sur K7.

En particulier ε_+=−1 sur les21 racines plus. L'équation entière des racines impose encore Tε=0 sur ces21 racines plus et Tε=−4ε sur les21 racines moins. Ce second système n'est pas construit par l'existence du tournoi.

La projection blocs de χ est z=½Σ v_c. Le complément χ−z appartient à K et a norme3. Ses produits avec les u_o sont0 sur les21 racines plus et ε_- sur les21 racines moins. Ceci donne une cible entière supplémentaire pour K dans ce seul profil.

Un tournoi cyclique sur sept sommets existe, et le source en donne un : chaque sommet reçoit les trois différences1,2,4 modulo7. Ainsi l'équation des blocs Cε=−6·1 est cohérente. Ce contrôle interdit de présenter la seule réduction au tournoi comme une contradiction.

## 6. La borne caractéristique10 seule est réalisable

Voici un contre-témoin de genre, sans prétendre qu'il porte le frame SRG.

Soit D12+ = D12 + Z·h, h=(½,...,½). Ce réseau intégral impair unimodulaire de rang12 a minimum2. Prendre

    a=(3/2,3/2,1/2,...,1/2),  a²=7,
    K11=a⊥∩D12+.

a est primitif et de divisibilité1, car (a,e1−e3)=1. Donc det K11=7, et K11 a minimum2, atteint par e3−e4.

Le vecteur c=(1,1,−1,1,...,1) a norme12 et est caractéristique sur D12+ : il a tous ses coefficients impairs, et (c,h)=5≡h² modulo2. On a (c,a)=7 ; k=c−a appartient à K11, est caractéristique et a norme5.

Réciproquement, si k' est caractéristique de K11, k'+a est caractéristique sur K11⊕Za, donc sur D12+ puisque l'indice est7. Les caractéristiques de D12+ ont carré4 modulo8, comme le témoin2e1. Donc k'²+7≡4 modulo8, et k'²≥5. Ainsi min caractéristique K11=5.

Le réseau K11⊕K11 a rang22, déterminant49, minimum2 et minimum caractéristique10. Son discriminant7 est anisotrope en dimension2. La borne10 et le minimum2 ne ferment donc pas ce genre.

Ce contre-témoin est cependant déjà éliminé par le minimum dual : la projection de b=e1+e2 sur a⊥ a norme2−9/7=5/7. Il viole min N#≥8/7. On ne réannonce pas cette vieille exclusion comme un gain nouveau, et on ne prétend pas que ce réseau possède P ou les42 classes prescrites.

## 7. Collage unimodulaire24 : une conséquence nouvelle finie

Dans le cas det L=49 et discriminant7 anisotrope2, on peut coller L⊕J, J=7I2, par une anti-isométrie de ses discriminants7. L'indice est49, et la surlattice U a rang24, déterminant1 et est impaire. L et J y sont primitifs. Ce raccord est audité séparément ; il ne prouve pas que U soit sans racines.

Noter r1,r2 les générateurs orthogonaux de J, de norme7. Le vecteur χ0+r1+r2 est caractéristique sur L⊕J, donc sur U par l'indice49 impair. Son carré est0 modulo8. Les caractéristiques de U diffèrent de2U, donc ont toutes carré0 modulo8.

Pour une caractéristique χ de U, ses projections sont x dans L# et y dans J#. Les42 produits (x,u_o) sont impairs. Écrire (x,v_c)=2a_c et (y,r_i)=b_i, b_i impair. Alors

    χ²=x²+(b1²+b2²)/7,
    7x²=42+8n3+24n5+4Σa_c².

On a χ²≥44/7, donc χ²≥8. À norme8, l'équation exacte est

    b1²+b2²+4Σa_c²+8n3+24n5=14.

Elle impose n5=0, |b_i|≤3, |a_c|≤1, et exactement trois profils, à permutation et signe près :

| Produits J en valeur absolue | n3 | Σa_c² |
|---|---:|---:|
| (1,1) | 0 | 3 |
| (1,1) | 1 | 1 |
| (1,3) | 0 | 1 |

La borne10 sur les caractéristiques de L ne s'applique pas à x, car x appartient à L# et n'est pas nécessairement dans L. Confondre ces deux appartenances donnerait une fausse exclusion.

Dans le second profil, il existe une unique racine r avec produit3s et un unique bloc actif i avec a_i=±1. La ligne de r exige

    C_ir a_i=−s,    (x,u_t)=−s T_rt pour chacun des10 voisins simples t de r.

En effet, 2Cᵀa peut fournir au plus2 et T peut fournir au plus10, alors que la ligne exige12. Toutes les contributions saturent ; r doit toucher i. La caractéristique χ−2s u_r reste de norme8 ; son bloc actif migre vers l'autre endpoint de r. Ces conditions sont uniformes, mais aucune contradiction n'est obtenue ici.

Pour une racine mixte de U, écrire sa projection sur J# sous la forme b/7. Min L#≥8/7 implique b1²+b2²∈{0,1,2,4,5}. Même si min L≥3, les quatre valeurs non nulles peuvent encore donner une racine mixte. Le collage ne rend donc pas U sans racines automatiquement.

## 8. Vérification et portée

Le source propre verifier_sept_blocs_caracteristiques.mjs effectue seulement :

- les16384 résidus du code des sept blocs, donnant4096 classes et64 éléments de2-torsion ;
- les42 classes d'ordre4 et le tournoi cyclique, sans construire T ;
- les égalités rationnelles exactes du témoin K11 et son vecteur dual5/7 ;
- les trois profils de caractéristique8.

Le résultat est verifier_sept_blocs_caracteristiques.json. Ce contrôle ne remplace pas les preuves de réseaux. Les indices, classes, caractéristiques et profils ont été communiqués au contre-auditeur indépendant avant livraison.

Résultat utilisable : le problème uniforme porte un réseau de rang15, un code4-aire de dimension6,42 classes courtes prescrites, et des profils caractéristiques extrêmement restreints. Aucun réseau SRG99, aucune reconstruction de T et aucune exclusion globale g18/g20 ne sont produits. Les profils restants et les racines du collage24 demeurent des obstacles effectifs.


---

Pièce originale : TEMPLATE_CONDITIONNEL_SHADOW24.md

# Template conditionnel : sept blocs et deux lignes pondérées dans le shadowframe24

## Hypothèse supplémentaire

Cette note ne démontre pas que le collage unimodulaire U de rang24 soit sans racines. On suppose explicitement l'existence de24 vecteurs s_j orthogonaux, de norme2, tels que2s_j soient caractéristiques de U. La présence de ce shadowframe est une hypothèse supplémentaire ; aucune classification de réseaux n'est invoquée ici.

U contient le réseau physique N de rang22 et deux vecteurs r1,r2 orthogonaux à N et entre eux, de norme7. Les sept v_c de norme4 et les42 u_o de norme3 sont ceux de la note SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.

## Matrices exactes

Poser

    E_oj=2(u_o,s_j),    M_cj=(v_c,s_j),
    B_ij=2(r_i,s_j).

Les42 lignes de E sont des mots de signes de longueur24. En effet, E_oj est impair et Parseval SUR LES24 vecteurs donne Σ_j E_oj²=8u_o²=24. Chaque carré est au moins1, donc chaque coefficient vaut±1. La norme3 seule ne suffirait pas à obtenir cette conclusion pour une caractéristique isolée.

M est entier ; B a tous ses coefficients impairs. Les trois profils de caractéristique8, appliqués à2s_j, imposent M_cj∈{0,1,−1} et B_ij∈{±1,±3}.

On a BBᵀ=56I2. Chaque ligne B possède donc quatre coefficients de valeur absolue3 et vingt de valeur absolue1. Les deux ensembles de quatre sont disjoints, car un profil de caractéristique8 n'autorise pas les deux produits absolus3 dans la même colonne.

Ainsi :

- les huit colonnes appartenant à un des deux ensembles de quatre ont un seul coefficient non nul dans M ;
- les seize autres colonnes ont trois coefficients non nuls dans M.

La totalité des sept blocs est donc codée par une matrice M de7 lignes orthogonales, chacune de poids8, avec seize colonnes de poids3 et huit de poids1.

Les relations de Gram et d'orthogonalité donnent

    EEᵀ=8(3I42−T),   MMᵀ=8I7,
    MEᵀ=−4C,        BBᵀ=56I2,
    EBᵀ=0,          MBᵀ=0.

La relation physique fournit aussi CE=−6M. Enfin, le frame7I sur N et le projecteur sur l'orthogonal de rang2 donnent

    EᵀE+4MᵀM+BᵀB=56I24.

Ces constantes se vérifient directement par Parseval : les coordonnées de u_o sont E_o/(2√2), celles de v_c sont M_c/√2, et celles de r_i sont B_i/(2√2).

Pour deux u_o distincts, leur produit est0,1 ou−1. Les distances entre les42 mots de E sont donc12,8 ou16, respectivement. Mais les distances seules ne conservent pas le modèle : il faut aussi les deux lignes pondérées B, la matrice des sept blocs M, CE=−6M et toutes les relations précédentes.

## Un petit invariant binaire

Réduire M modulo2. Les sept lignes ont poids8 et deux lignes se recouvrent en un nombre pair de coordonnées, parce que leur produit signé est nul. Elles engendrent donc un code binaire doublement pair. Chaque colonne de M a poids impair, donc la somme des sept lignes est le mot constant de poids24.

Il y a huit colonnes de poids1 et seulement sept supports possibles pour celles-ci : deux colonnes au moins ont le même support binaire. Ce fait ne contredit pas l'existence d'un code plus grand ; il donne seulement une relation de poids2 dans le dual du sous-code engendré par M. On ne remplace pas ce sous-code par un code autodual sans preuve.

## Portée

Ce template est un objet fini global, portant simultanément les42 mots, les sept blocs et les deux charges du collage. L'hypothèse du shadowframe, et a fortiori l'absence de racines dans U, ne sont pas acquises par cette note. Aucun choix de E,M,B satisfaisant toutes les équations n'est produit, et aucune exclusion globale de g20 n'est affirmée.

L'audit indépendant confirme les constantes, les profils et la nécessité de Parseval sur les24 vecteurs pour rendre E plat.



---

Pièce originale : ETAT_REPRISE.md

# État de reprise — 27 septembre 2026, attaque globale de 08:03 UTC

Reprise à la demande : « le cas par cas marche clairement pas, il faut tout balayer d’un coup ». La campagne locale de 07:36 UTC est figée et conservée ci-dessous. Cette reprise travaille avec les sept blocs simultanément, sans relancer le catalogue d’étoiles.

## État des objectifs

**L’involution n’est pas exclue.** Ni g⁻=18 ni g⁻=20 n’est éliminé intégralement ; aucune preuve générale involution ⇒ prisme. L’automation reste active. Les normes 9/10 demeurent ouvertes globalement. Le registre propre P=0 demeure 278 types g18 fermés, 163 ouverts, et aucun type g20 entièrement fermé : ces chiffres ne sont pas extrapolés hors P=0.

## Nouveaux résultats uniformes — démontrés et contre-audités

Les réductions transmises g⁻∈{18,20}, déterminant 7^(22−g⁻) et discriminant 7 non scindé sont des ENTRÉES attribuées à C1/structures, pas une lecture nouvelle de leurs dépôts.

1. **Unification des deux genres.** À g20, Nmax=N ; à g18, un sur-réseau intégral d’indice 7 donne Nmax de rang 22, déterminant 49 et discriminant anisotrope élémentaire de dimension 2. Il conserve le repère physique réel. Collage avec 7I₂ d’indice 49 : réseau unimodulaire impair de rang 24, sans norme 1. Cela ne convertit pas une matrice g18 en une réalisation g20.
2. **Indécomposabilité globale.** Le minimum ≥2 rend chaque générateur de norme 3 pur dans toute décomposition orthogonale. L’identité T²+T=12I−CᵀC et la connexité des 42 colonnes D7 de C obligent tous les générateurs à être dans un seul facteur. Vaut pour N et Nmax, sans P=0 ; deux preuves indépendantes.
3. **Rang des racines ≤20.** Les strates de racines de rang 22 et 21 sont exclues par les valuations 7, les collages ADE et les coûts des classes minimales. En corang 1, conserver les classes fractionnaires : les seules strates 7 possibles conduisent à un facteur inaccessible aux normes 3, ou à un coût >3. Deux implémentations finies et audit adverse.
4. **Composantes entières exclues.** Dans Nmax : pas de E8, de D_n pour n≥11, ni de A_n pour n≥20. Dans le collage de rang 24 : pas de E8, de D_n pour n≥12, ni de A_n pour n≥22. Les frontières de transport sont distinctes ; toutes les preuves sans P=0.
5. **Sept blocs et parité.** Saturation P=2ℤ⁷+ℤ·1, det P=2¹², discriminant (ℤ/4)⁶. Les 42 projections complémentaires portent 42 classes de norme 5/2. Les caractéristiques de N ont carré ≥10 ; à carré 10, le profil régulier de tournoi K7 survit : aucune contradiction annoncée.

## Contrôle positif de l’enveloppe : le genre seul ne ferme pas

Construction autonome par code binaire explicite de dimension 12 et réseau unimodulaire impair 24 : deux vecteurs orthogonaux de norme 7 ont un complément M de rang 22, det 49, discriminant (ℤ/7)², minimum 3, minimum dual ≥10/7, minimum caractéristique ≥10. Vingt-deux des 704 vecteurs de norme 3 donnent un Gram exact de déterminant 49 : ils engendrent M intégralement et son Gram connexe démontre l’indécomposabilité. M est sans racines.

La seconde implémentation utilise une autre génération du code et un déterminant rationnel exact indépendant. Toutes les 4096 projections concordent. **Ce contrôle n’est pas un graphe** : ni les 42 supports D7, ni les 7 blocs, ni le repère serré 7, ni degrés/couplage/relèvement SRG n’y sont construits. Il interdit une fausse exclusion fondée uniquement sur les minima, le déterminant et l’indécomposabilité.

## Annexes conditionnelles

Norme 2 dans N ⇒ vecteur propre entier impair de carré 14. Il comporte au plus un coefficient |2|, uniquement intérieur ; alors six racines incidentes et quatre externes sont forcées. Le cas plat reste ouvert.

Sous P=0 seulement, le carrier lourd à quatre supports externes ne peut être une étoile sur un même bloc ni comporter de support répété : les trois régimes saturés donnent un prisme. Deux contrôles exacts indépendants. Cela ne ferme pas les normes 9/10 ni tout g.

## Prochain problème concret global

Contrôler le **repère physique commun 42+7** dans Nmax (déterminant 49) ou son collage unimodulaire 24. Ses 49 vecteurs doivent satisfaire simultanément les supports C, CT=0, le Gram signé, dix produits racines non nuls par ligne et la relation de repère serré.

Une formulation entière conditionnelle existe si le collage a un repère de 24 ombres orthogonales : matrices E (42 mots de signes), M (7 octades signées), B (2 mots à coefficients ±1/±3), avec EEᵀ=8(3I−T), MMᵀ=8I, MEᵀ=−4C, BBᵀ=56I₂, EBᵀ=MBᵀ=0 et EᵀE+4MᵀM+BᵀB=56I₂₄. Les quatre grandes coordonnées des deux lignes B sont disjointes ; les colonnes de M ont poids 1 (huit) ou 3 (seize). L’existence du repère d’ombres pour tout collage est NON DÉMONTRÉE : conserver cette hypothèse.

Ne pas reprendre automatiquement un sweep local. Un nouveau sweep ne constituerait pas l’argument uniforme demandé.

## Pièces, validations, limites

Dossier : outputs/attaque_globale_27_0803.
Bilan lisible : BILAN_ATTAQUE_GLOBALE.md.
Preuves et audits rassemblés : PREUVES_COMPLETES_ATTAQUE_GLOBALE.md.
Programmes, sorties, SHA : MANIFESTE_ATTAQUE_GLOBALE.json et archive livrée.

Vrais graphes reconstruits ici : H(2,3), r=1,d=3 et BvLS, r=4,d=9. λ=1,μ=2, S²+S=r(r+1)I, H²=dH et relations de repère vérifiées ; aucun F7/P0/g18/g20 imposé à ces contrôles. Leurs générateurs ont normes 1/4, pas 3.

Uniquement fichiers produits dans ce fil, mathématiques et courts calculs exacts JavaScript. Aucun document extérieur, dépôt, Web mathématique, Python local, SAT/CP/PLNE ou solveur externe dans cette reprise. Aucun calcul lourd ou fenêtre visible lancé sur le PC.

---

# Historique figé — campagne locale précédente

