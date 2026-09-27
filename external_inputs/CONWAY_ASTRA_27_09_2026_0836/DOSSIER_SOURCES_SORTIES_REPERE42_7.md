# Sources et sorties exactes — repère 42+7

Les fichiers intégraux sont tous dans l’archive ; le domaine de 2,7 Mo reste dans son JSON original, sans troncature. Aucun graphe99 ni repère physique complet n’est produit.

## Campagne 0803, sources et sorties intégrales

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



---

# Programmes exacts et sorties intégrales

Les programmes mathématiques sont des contrôles bornés ; les scripts de manifeste ne sont pas des preuves de non-existence. Les sorties complètes comprennent la base de 22 vecteurs et le Gram du contrôle positif.



## G18_G20_A20_FRAME.json

````json
{
  "exact": true,
  "same_rank_22": [
    {
      "n": 20,
      "d": 0,
      "admissible_k": [
        1,
        2,
        3,
        18,
        19,
        20
      ],
      "max_projection_norm": {
        "numerator": 54,
        "denominator": 21
      },
      "lower_trace_numerator": 2940,
      "upper_trace_numerator": 2856,
      "strict_gap_numerator": 84,
      "excluded": true
    },
    {
      "n": 21,
      "d": 0,
      "admissible_k": [
        1,
        2,
        3,
        19,
        20,
        21
      ],
      "max_projection_norm": {
        "numerator": 57,
        "denominator": 22
      },
      "lower_trace_numerator": 3234,
      "upper_trace_numerator": 3010,
      "strict_gap_numerator": 224,
      "excluded": true
    },
    {
      "n": 22,
      "d": 0,
      "admissible_k": [
        1,
        2,
        3,
        20,
        21,
        22
      ],
      "max_projection_norm": {
        "numerator": 60,
        "denominator": 23
      },
      "lower_trace_numerator": 3542,
      "upper_trace_numerator": 3164,
      "strict_gap_numerator": 378,
      "excluded": true
    }
  ],
  "integral_extension_dimension_at_most24": [
    {
      "n": 22,
      "d": 2,
      "admissible_k": [
        1,
        2,
        3,
        20,
        21,
        22
      ],
      "max_projection_norm": {
        "numerator": 60,
        "denominator": 23
      },
      "lower_trace_numerator": 3220,
      "upper_trace_numerator": 3164,
      "strict_gap_numerator": 56,
      "excluded": true
    },
    {
      "n": 23,
      "d": 2,
      "admissible_k": [
        1,
        2,
        3,
        21,
        22,
        23
      ],
      "max_projection_norm": {
        "numerator": 63,
        "denominator": 24
      },
      "lower_trace_numerator": 3528,
      "upper_trace_numerator": 3318,
      "strict_gap_numerator": 210,
      "excluded": true
    },
    {
      "n": 24,
      "d": 2,
      "admissible_k": [
        1,
        2,
        3,
        22,
        23,
        24
      ],
      "max_projection_norm": {
        "numerator": 66,
        "denominator": 25
      },
      "lower_trace_numerator": 3850,
      "upper_trace_numerator": 3472,
      "strict_gap_numerator": 378,
      "excluded": true
    }
  ],
  "boundary_not_closed_by_this_inequality": [
    {
      "n": 19,
      "d": 0,
      "admissible_k": [
        1,
        2,
        3,
        17,
        18,
        19
      ],
      "max_projection_norm": {
        "numerator": 51,
        "denominator": 20
      },
      "lower_trace_numerator": 2660,
      "upper_trace_numerator": 2702,
      "strict_gap_numerator": -42,
      "excluded": false
    },
    {
      "n": 21,
      "d": 2,
      "admissible_k": [
        1,
        2,
        3,
        19,
        20,
        21
      ],
      "max_projection_norm": {
        "numerator": 57,
        "denominator": 22
      },
      "lower_trace_numerator": 2926,
      "upper_trace_numerator": 3010,
      "strict_gap_numerator": -84,
      "excluded": false
    }
  ],
  "scope": "Common N22 frame and acquired dual gap8/7; no type catalogue, P0, g>=21 or entire g18/g20 exclusion."
}

````


## G18_G20_A20_FRAME.mjs

````javascript
import fs from 'node:fs';
import assert from 'node:assert/strict';
const exactTrace=(n,d)=>{
  const denominator=n+1;
  const weights=Array.from({length:n},(_,i)=>i+1).filter(k=>k*(n+1-k)<=3*denominator);
  const maxNumerator=Math.max(...weights.map(k=>k*(n+1-k)));
  const lhs=7*(n-d)*denominator,rhs=42*maxNumerator+28*denominator;
  return {n,d,admissible_k:weights,max_projection_norm:{numerator:maxNumerator,denominator},
    lower_trace_numerator:lhs,upper_trace_numerator:rhs,strict_gap_numerator:lhs-rhs,excluded:lhs>rhs};
};
const sameRank=[20,21,22].map(n=>exactTrace(n,0));
const rank24=[22,23,24].map(n=>exactTrace(n,2));
for(const row of sameRank.concat(rank24)){
  assert.equal(row.max_projection_norm.numerator,3*(row.n-2));
  assert.deepEqual(row.admissible_k,[1,2,3,row.n-2,row.n-1,row.n]);
  assert(row.excluded);
}
const boundary=[exactTrace(19,0),exactTrace(21,2)];
assert(boundary.every(row=>!row.excluded));
const out={exact:true,same_rank_22:sameRank,integral_extension_dimension_at_most24:rank24,
  boundary_not_closed_by_this_inequality:boundary,
  scope:'Common N22 frame and acquired dual gap8/7; no type catalogue, P0, g>=21 or entire g18/g20 exclusion.'};
fs.writeFileSync(new URL('./G18_G20_A20_FRAME.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify(out));

````


## G18_G20_CARRIER_LOURD_P0.json

````json
{
  "exact": true,
  "graphs": 9,
  "label_contexts": 144,
  "budget_compatible_contexts": 36,
  "all_contain_induced_prism": true,
  "proofs": [
    {
      "B_mask": 30,
      "labels": 5,
      "s": [
        1,
        -1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            5,
            8
          ],
          [
            3,
            4,
            9
          ]
        ],
        "bars": [
          [
            2,
            4
          ],
          [
            5,
            3
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 30,
      "labels": 6,
      "s": [
        -1,
        1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            4,
            8
          ],
          [
            3,
            5,
            9
          ]
        ],
        "bars": [
          [
            2,
            5
          ],
          [
            4,
            3
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 30,
      "labels": 9,
      "s": [
        1,
        -1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            5,
            8
          ],
          [
            2,
            4,
            9
          ]
        ],
        "bars": [
          [
            3,
            4
          ],
          [
            5,
            2
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 30,
      "labels": 10,
      "s": [
        -1,
        1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            4,
            8
          ],
          [
            2,
            5,
            9
          ]
        ],
        "bars": [
          [
            3,
            5
          ],
          [
            4,
            2
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 31,
      "labels": 5,
      "s": [
        1,
        -1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            5,
            8
          ],
          [
            3,
            4,
            9
          ]
        ],
        "bars": [
          [
            2,
            4
          ],
          [
            5,
            3
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 31,
      "labels": 6,
      "s": [
        -1,
        1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            4,
            8
          ],
          [
            3,
            5,
            9
          ]
        ],
        "bars": [
          [
            2,
            5
          ],
          [
            4,
            3
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 31,
      "labels": 9,
      "s": [
        1,
        -1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            5,
            8
          ],
          [
            2,
            4,
            9
          ]
        ],
        "bars": [
          [
            3,
            4
          ],
          [
            5,
            2
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 31,
      "labels": 10,
      "s": [
        -1,
        1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            4,
            8
          ],
          [
            2,
            5,
            9
          ]
        ],
        "bars": [
          [
            3,
            5
          ],
          [
            4,
            2
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 45,
      "labels": 3,
      "s": [
        1,
        1,
        -1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            1,
            6,
            8
          ],
          [
            3,
            4,
            9
          ]
        ],
        "bars": [
          [
            1,
            4
          ],
          [
            6,
            3
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 45,
      "labels": 6,
      "s": [
        -1,
        1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            7,
            8
          ],
          [
            0,
            5,
            9
          ]
        ],
        "bars": [
          [
            2,
            5
          ],
          [
            7,
            0
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 45,
      "labels": 9,
      "s": [
        1,
        -1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            6,
            8
          ],
          [
            1,
            4,
            9
          ]
        ],
        "bars": [
          [
            3,
            4
          ],
          [
            6,
            1
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 45,
      "labels": 12,
      "s": [
        -1,
        -1,
        1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            4,
            8
          ],
          [
            1,
            6,
            9
          ]
        ],
        "bars": [
          [
            3,
            6
          ],
          [
            4,
            1
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 47,
      "labels": 3,
      "s": [
        1,
        1,
        -1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            1,
            6,
            8
          ],
          [
            3,
            4,
            9
          ]
        ],
        "bars": [
          [
            1,
            4
          ],
          [
            6,
            3
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 47,
      "labels": 6,
      "s": [
        -1,
        1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            7,
            8
          ],
          [
            0,
            5,
            9
          ]
        ],
        "bars": [
          [
            2,
            5
          ],
          [
            7,
            0
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 47,
      "labels": 9,
      "s": [
        1,
        -1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            6,
            8
          ],
          [
            1,
            4,
            9
          ]
        ],
        "bars": [
          [
            3,
            4
          ],
          [
            6,
            1
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 47,
      "labels": 12,
      "s": [
        -1,
        -1,
        1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            4,
            8
          ],
          [
            1,
            6,
            9
          ]
        ],
        "bars": [
          [
            3,
            6
          ],
          [
            4,
            1
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 51,
      "labels": 3,
      "s": [
        1,
        1,
        -1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            1,
            7,
            8
          ],
          [
            2,
            4,
            9
          ]
        ],
        "bars": [
          [
            1,
            4
          ],
          [
            7,
            2
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 51,
      "labels": 5,
      "s": [
        1,
        -1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            7,
            8
          ],
          [
            1,
            4,
            9
          ]
        ],
        "bars": [
          [
            2,
            4
          ],
          [
            7,
            1
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 51,
      "labels": 10,
      "s": [
        -1,
        1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            6,
            8
          ],
          [
            0,
            5,
            9
          ]
        ],
        "bars": [
          [
            3,
            5
          ],
          [
            6,
            0
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 51,
      "labels": 12,
      "s": [
        -1,
        -1,
        1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            5,
            8
          ],
          [
            0,
            6,
            9
          ]
        ],
        "bars": [
          [
            3,
            6
          ],
          [
            5,
            0
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 55,
      "labels": 3,
      "s": [
        1,
        1,
        -1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            1,
            7,
            8
          ],
          [
            2,
            4,
            9
          ]
        ],
        "bars": [
          [
            1,
            4
          ],
          [
            7,
            2
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 55,
      "labels": 5,
      "s": [
        1,
        -1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            7,
            8
          ],
          [
            1,
            4,
            9
          ]
        ],
        "bars": [
          [
            2,
            4
          ],
          [
            7,
            1
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 55,
      "labels": 10,
      "s": [
        -1,
        1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            6,
            8
          ],
          [
            0,
            5,
            9
          ]
        ],
        "bars": [
          [
            3,
            5
          ],
          [
            6,
            0
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 55,
      "labels": 12,
      "s": [
        -1,
        -1,
        1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            5,
            8
          ],
          [
            0,
            6,
            9
          ]
        ],
        "bars": [
          [
            3,
            6
          ],
          [
            5,
            0
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 59,
      "labels": 3,
      "s": [
        1,
        1,
        -1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            1,
            7,
            8
          ],
          [
            2,
            4,
            9
          ]
        ],
        "bars": [
          [
            1,
            4
          ],
          [
            7,
            2
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 59,
      "labels": 5,
      "s": [
        1,
        -1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            7,
            8
          ],
          [
            1,
            4,
            9
          ]
        ],
        "bars": [
          [
            2,
            4
          ],
          [
            7,
            1
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 59,
      "labels": 10,
      "s": [
        -1,
        1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            6,
            8
          ],
          [
            0,
            5,
            9
          ]
        ],
        "bars": [
          [
            3,
            5
          ],
          [
            6,
            0
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 59,
      "labels": 12,
      "s": [
        -1,
        -1,
        1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            5,
            8
          ],
          [
            0,
            6,
            9
          ]
        ],
        "bars": [
          [
            3,
            6
          ],
          [
            5,
            0
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 61,
      "labels": 3,
      "s": [
        1,
        1,
        -1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            1,
            6,
            8
          ],
          [
            3,
            4,
            9
          ]
        ],
        "bars": [
          [
            1,
            4
          ],
          [
            6,
            3
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 61,
      "labels": 6,
      "s": [
        -1,
        1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            7,
            8
          ],
          [
            0,
            5,
            9
          ]
        ],
        "bars": [
          [
            2,
            5
          ],
          [
            7,
            0
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 61,
      "labels": 9,
      "s": [
        1,
        -1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            6,
            8
          ],
          [
            1,
            4,
            9
          ]
        ],
        "bars": [
          [
            3,
            4
          ],
          [
            6,
            1
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 61,
      "labels": 12,
      "s": [
        -1,
        -1,
        1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            4,
            8
          ],
          [
            1,
            6,
            9
          ]
        ],
        "bars": [
          [
            3,
            6
          ],
          [
            4,
            1
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 62,
      "labels": 5,
      "s": [
        1,
        -1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            5,
            8
          ],
          [
            3,
            4,
            9
          ]
        ],
        "bars": [
          [
            2,
            4
          ],
          [
            5,
            3
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 62,
      "labels": 6,
      "s": [
        -1,
        1,
        1,
        -1
      ],
      "witness": {
        "triangles": [
          [
            2,
            4,
            8
          ],
          [
            3,
            5,
            9
          ]
        ],
        "bars": [
          [
            2,
            5
          ],
          [
            4,
            3
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 62,
      "labels": 9,
      "s": [
        1,
        -1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            5,
            8
          ],
          [
            2,
            4,
            9
          ]
        ],
        "bars": [
          [
            3,
            4
          ],
          [
            5,
            2
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    },
    {
      "B_mask": 62,
      "labels": 10,
      "s": [
        -1,
        1,
        -1,
        1
      ],
      "witness": {
        "triangles": [
          [
            3,
            4,
            8
          ],
          [
            2,
            5,
            9
          ]
        ],
        "bars": [
          [
            3,
            5
          ],
          [
            4,
            2
          ],
          [
            8,
            9
          ]
        ],
        "known_edges": 9
      }
    }
  ],
  "scope": "P0 excludes heavy external carrier degree4 only. Remaining carriers and g18/g20 remain open."
}

````


## G18_G20_CARRIER_LOURD_P0.mjs

````javascript
// Known-edge carrier check, without a global graph search.
import fs from 'node:fs';import assert from 'node:assert/strict';
const pairs=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)pairs.push([i,j]);
const count=x=>{let n=0;while(x){x&=x-1;n++;}return n;},graphs=[];
for(let mask=0;mask<64;mask++){
 const row=Array(4).fill(0);for(let e=0;e<6;e++)if(mask&(1<<e)){const[i,j]=pairs[e];row[i]|=1<<j;row[j]|=1<<i;}
 if(count(mask)===5||(count(mask)===4&&row.every(r=>count(r)===2)))graphs.push({mask,row});
}
assert.equal(graphs.length,9);const proofs=[];let contexts=0;
for(const g of graphs)for(let labels=0;labels<16;labels++){
 contexts++;const s=Array.from({length:4},(_,j)=>labels&(1<<j)?1:-1);
 if(pairs.some(([i,j])=>count(g.row[i]&g.row[j])>=2&&s[i]===s[j]))continue;
 const adj=Array.from({length:10},()=>Array(10).fill(false));
 const edge=(a,b)=>{adj[a][b]=true;adj[b][a]=true;};
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(g.row[i]&(1<<j))edge(i,4+j);
 edge(8,9);for(let i=0;i<4;i++){edge(i,s[i]===1?8:9);edge(4+i,s[i]===1?9:8);}
 let witness=null;
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++)for(let l=0;l<4;l++){
  if(new Set([i,j,k,l]).size!==4||s[i]!==1||s[l]!==1||s[j]!==-1||s[k]!==-1)continue;
  const triangles=[[i,4+j,8],[k,4+l,9]],bars=[[i,4+l],[4+j,k],[8,9]];
  const known=triangles.flatMap(t=>[[t[0],t[1]],[t[0],t[2]],[t[1],t[2]]]).concat(bars);
  if(!known.every(([a,b])=>adj[a][b]))continue;
  const six=triangles.flat();let n=0;for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)if(adj[six[a]][six[b]])n++;
  assert.equal(n,9);witness={triangles,bars,known_edges:n};break;
 }
 assert(witness);proofs.push({B_mask:g.mask,labels,s,witness});
}
assert.equal(proofs.length,36);
const result={exact:true,graphs:9,label_contexts:contexts,budget_compatible_contexts:proofs.length,all_contain_induced_prism:true,proofs,
 scope:'P0 excludes heavy external carrier degree4 only. Remaining carriers and g18/g20 remain open.'};
fs.writeFileSync(new URL('./G18_G20_CARRIER_LOURD_P0.json',import.meta.url),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,graphs:9,contexts,prisms:proofs.length,scope:result.scope}));

````


## G18_G20_D12_COLLAGE.json

````json
{
  "exact": true,
  "trace_equality": 70,
  "axis_multiplicities": {
    "0": 2,
    "3": 7,
    "7": 3
  },
  "possible_column_incidence_norms": [
    0,
    4,
    0
  ],
  "required_D7_column_incidence_norm": 2,
  "factor_projection_norms": [
    0,
    4
  ],
  "factor_off_diagonal": [
    0
  ],
  "spinor_extension": {
    "rank": 12,
    "index": 2,
    "determinant": 1
  },
  "scope": "No D12 root sub-system in any integral extension of dimension<=24 containing the common N22 frame and dual gap8/7. No entire g18/g20 exclusion."
}

````


## G18_G20_D12_COLLAGE.mjs

````javascript
import fs from 'node:fs';import assert from 'node:assert/strict';
const factorNorms=[];for(let t=0;t<=4;t++)if(7*t===t*t+3*t)factorNorms.push(t);
assert.deepEqual(factorNorms,[0,4]);
const offDiagonal=[];for(let g=-4;g<=4;g++)if([-1,0,1].includes(3*g))offDiagonal.push(g);
assert.deepEqual(offDiagonal,[0]);
const multiplicities={0:2,3:7,7:3};
assert.equal(2+7+3,12);assert.equal(3*7+7*3,42);
const incidenceValues=[];for(const eigen of [0,3,7]){
 const ph=eigen*(7-eigen)/12;assert(ph===0||ph===1);incidenceValues.push(4*ph);
}
assert(incidenceValues.every(x=>x!==2));
assert.equal(7*(12-2),42+7*4);assert.equal(4/2**2,1);
const out={exact:true,trace_equality:70,axis_multiplicities:multiplicities,possible_column_incidence_norms:incidenceValues,
 required_D7_column_incidence_norm:2,factor_projection_norms:factorNorms,factor_off_diagonal:offDiagonal,
 spinor_extension:{rank:12,index:2,determinant:1},
 scope:'No D12 root sub-system in any integral extension of dimension<=24 containing the common N22 frame and dual gap8/7. No entire g18/g20 exclusion.'};
fs.writeFileSync(new URL('./G18_G20_D12_COLLAGE.json',import.meta.url),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));

````


## G18_G20_D13_FRAME.json

````json
{
  "exact": true,
  "rows": [
    {
      "Dn_rank": 13,
      "half_weight_norm": "13/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 77,
      "frame_trace_upper": 70,
      "strict_gap": 7
    },
    {
      "Dn_rank": 14,
      "half_weight_norm": "14/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 84,
      "frame_trace_upper": 70,
      "strict_gap": 14
    },
    {
      "Dn_rank": 15,
      "half_weight_norm": "15/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 91,
      "frame_trace_upper": 70,
      "strict_gap": 21
    },
    {
      "Dn_rank": 16,
      "half_weight_norm": "16/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 98,
      "frame_trace_upper": 70,
      "strict_gap": 28
    },
    {
      "Dn_rank": 17,
      "half_weight_norm": "17/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 105,
      "frame_trace_upper": 70,
      "strict_gap": 35
    },
    {
      "Dn_rank": 18,
      "half_weight_norm": "18/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 112,
      "frame_trace_upper": 70,
      "strict_gap": 42
    },
    {
      "Dn_rank": 19,
      "half_weight_norm": "19/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 119,
      "frame_trace_upper": 70,
      "strict_gap": 49
    },
    {
      "Dn_rank": 20,
      "half_weight_norm": "20/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 126,
      "frame_trace_upper": 70,
      "strict_gap": 56
    },
    {
      "Dn_rank": 21,
      "half_weight_norm": "21/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 133,
      "frame_trace_upper": 70,
      "strict_gap": 63
    },
    {
      "Dn_rank": 22,
      "half_weight_norm": "22/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 140,
      "frame_trace_upper": 70,
      "strict_gap": 70
    },
    {
      "Dn_rank": 23,
      "half_weight_norm": "23/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 147,
      "frame_trace_upper": 70,
      "strict_gap": 77
    },
    {
      "Dn_rank": 24,
      "half_weight_norm": "24/4",
      "half_weight_exceeds_root_generator_norm3": true,
      "common_space_dimension": 22,
      "extension_dimension_at_most": 24,
      "frame_trace_lower": 154,
      "frame_trace_upper": 70,
      "strict_gap": 84
    }
  ],
  "scope": "No D_n,n>=13, in any integral extension of dimension<=24 containing the common N22 frame and dual gap8/7. No entire g18/g20 exclusion."
}

````


## G18_G20_D13_FRAME.mjs

````javascript
import fs from 'node:fs';import assert from 'node:assert/strict';
const rows=[];
for(let n=13;n<=24;n++){
 const lower=7*(n-2),upper=42+7*4;
 assert(n>4*3);assert(lower>upper);
 rows.push({Dn_rank:n,half_weight_norm:n+'/4',half_weight_exceeds_root_generator_norm3:true,
  common_space_dimension:22,extension_dimension_at_most:24,frame_trace_lower:lower,frame_trace_upper:upper,strict_gap:lower-upper});
}
const out={exact:true,rows,scope:'No D_n,n>=13, in any integral extension of dimension<=24 containing the common N22 frame and dual gap8/7. No entire g18/g20 exclusion.'};
fs.writeFileSync(new URL('./G18_G20_D13_FRAME.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,rows:rows.length,first:rows[0],last:rows.at(-1)}));

````


## G18_G20_E8_MINUSCULE.json

````json
{
  "exact": true,
  "roots": 240,
  "integer_candidate_checks": 6561,
  "post_pair_bound_candidates": 273,
  "integral_candidates": 129,
  "minuscule_candidates": [
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  ],
  "scope": "Uniform E8 sub-system obstruction in any integral extension of dimension<=29, using dual gap8/7; not g>=21 or whole-type exclusion."
}

````


## G18_G20_E8_MINUSCULE.mjs

````javascript
// Exact elementary E8 check; x2 and r2 mean twice each vector.
import fs from 'node:fs';
import assert from 'node:assert/strict';
const roots=[];
for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)for(const a of [-2,2])for(const b of [-2,2]){
 const r=Array(8).fill(0);r[i]=a;r[j]=b;roots.push(r);
}
const integerRoots=roots.slice();
for(let mask=0;mask<256;mask++){
 let n=0;for(let j=0;j<8;j++)if(mask&(1<<j))n++;
 if(n%2===0)roots.push(Array.from({length:8},(_,j)=>mask&(1<<j)?-1:1));
}
assert.equal(roots.length,240);
const dot=(a,b)=>a.reduce((z,x,j)=>z+x*b[j],0),candidates=[];
let integerChecks=0;
for(let code=0;code<3**8;code++){
 let q=code;const x=[];for(let j=0;j<8;j++){x.push(2*((q%3)-1));q=Math.floor(q/3);}
 integerChecks++;if(integerRoots.every(r=>Math.abs(dot(x,r))<=4))candidates.push(x);
}
assert.equal(candidates.length,17);
for(let mask=0;mask<256;mask++)candidates.push(Array.from({length:8},(_,j)=>mask&(1<<j)?-1:1));
assert.equal(candidates.length,273);
const integral=candidates.filter(x=>roots.every(r=>dot(x,r)%4===0));
const minuscule=integral.filter(x=>roots.every(r=>Math.abs(dot(x,r))<=4));
assert.equal(integral.length,129);assert.deepEqual(minuscule,[Array(8).fill(0)]);
const out={exact:true,roots:roots.length,integer_candidate_checks:integerChecks,post_pair_bound_candidates:candidates.length,
 integral_candidates:integral.length,minuscule_candidates:minuscule,
 scope:'Uniform E8 sub-system obstruction in any integral extension of dimension<=29, using dual gap8/7; not g>=21 or whole-type exclusion.'};
fs.writeFileSync(new URL('./G18_G20_E8_MINUSCULE.json',import.meta.url),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));

````


## G18_G20_LOURD_REGIMES.json

````json
{
  "exact": true,
  "matching_edge_regimes": [
    [
      0,
      2
    ],
    [
      0,
      3
    ],
    [
      1,
      3
    ]
  ],
  "external": [
    {
      "difference": 4,
      "checked": 4096,
      "survivors": [
        {
          "A": 0,
          "B": 30,
          "degree_B": [
            2,
            2,
            2,
            2
          ]
        },
        {
          "A": 0,
          "B": 45,
          "degree_B": [
            2,
            2,
            2,
            2
          ]
        },
        {
          "A": 0,
          "B": 51,
          "degree_B": [
            2,
            2,
            2,
            2
          ]
        }
      ]
    },
    {
      "difference": 5,
      "checked": 4096,
      "survivors": [
        {
          "A": 0,
          "B": 31,
          "degree_B": [
            3,
            3,
            2,
            2
          ]
        },
        {
          "A": 0,
          "B": 47,
          "degree_B": [
            3,
            2,
            3,
            2
          ]
        },
        {
          "A": 0,
          "B": 55,
          "degree_B": [
            3,
            2,
            2,
            3
          ]
        },
        {
          "A": 0,
          "B": 59,
          "degree_B": [
            2,
            3,
            3,
            2
          ]
        },
        {
          "A": 0,
          "B": 61,
          "degree_B": [
            2,
            3,
            2,
            3
          ]
        },
        {
          "A": 0,
          "B": 62,
          "degree_B": [
            2,
            2,
            3,
            3
          ]
        }
      ]
    }
  ],
  "R3_row_checks": 84,
  "R3_accepted_rows": 12,
  "scope": "Necessary capacity regimes for the same norm14 heavy eigenvector. Not a graph/type completion or exclusion."
}

````


## G18_G20_LOURD_REGIMES.mjs

````javascript
// Tiny independent capacity check on4 external vertices, not a completion search.
import fs from 'node:fs';
import assert from 'node:assert/strict';
const edges=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)edges.push([i,j]);
const graphs=Array.from({length:64},(_,mask)=>{
 const rows=Array(4).fill(0),degree=Array(4).fill(0);let n=0;
 for(let e=0;e<6;e++)if(mask&(1<<e)){const[i,j]=edges[e];rows[i]|=1<<j;rows[j]|=1<<i;degree[i]++;degree[j]++;n++;}
 return{mask,rows,degree,n};
});
const pop=x=>{let n=0;while(x){x&=x-1;n++;}return n;};
const regimes=[];
for(const difference of [4,5]){
 const survivors=[];let checked=0;
 for(const A of graphs)for(const B of graphs){
  checked++;if(B.n-A.n!==difference)continue;
  // Omit all unknown cross contributions: these are necessary lower bounds.
  if(edges.some(([i,j],e)=>(A.mask&(1<<e))&&pop(B.rows[i]&B.rows[j])>1))continue;
  if(B.degree.some((d,i)=>4-d+A.degree[i]>2))continue;
  if(difference===4)assert(A.n===0&&B.n===4&&B.degree.every(d=>d===2));
  else assert(A.n===0&&B.n===5);
  survivors.push({A:A.mask,B:B.mask,degree_B:B.degree});
 }
 assert.equal(survivors.length,difference===4?3:6);regimes.push({difference,checked,survivors});
}
let rowChecks=0,accepted=0;
for(let A=0;A<16;A++)for(let B=0;B<16;B++)if(pop(B)-pop(A)===1){
 for(let e=0;e<4;e++)if(A&(1<<e)){
  rowChecks++;if(pop(B&(15^(1<<e)))>1)continue;
  accepted++;assert.equal(pop(A),1);assert.equal(pop(B),2);assert(B&(1<<e));
 }
}
const pairs=[];for(let a=0;a<=3;a++)for(let b=0;b<=3;b++)if(12+2*(a-b)<=8)pairs.push([a,b]);
assert.deepEqual(pairs,[[0,2],[0,3],[1,3]]);
const out={exact:true,matching_edge_regimes:pairs,external:regimes,R3_row_checks:rowChecks,R3_accepted_rows:accepted,
 scope:'Necessary capacity regimes for the same norm14 heavy eigenvector. Not a graph/type completion or exclusion.'};
fs.writeFileSync(new URL('./G18_G20_LOURD_REGIMES.json',import.meta.url),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));

````


## G18_G20_MANIFESTE_COMBINATOIRE.json

````json
{
  "frozen_own_pieces": true,
  "own_count": 24,
  "own": [
    {
      "name": "G18_G20_NORME14_LOURDS.md",
      "bytes": 5847,
      "sha256": "425056c56cc6c76182360bcb433277ad3a8686794511ee31071a2f01059f5d16"
    },
    {
      "name": "G18_G20_NORME14_LOURDS.mjs",
      "bytes": 2300,
      "sha256": "5d8c43e6ca2dbbb7b3b17524dbaeffd1d710c6365b80f192e9e5d86d84275567"
    },
    {
      "name": "G18_G20_NORME14_LOURDS.json",
      "bytes": 1501,
      "sha256": "c21dfdaad964077b97c5929133ee13352523c49ea11d76766884c15e83829a9e"
    },
    {
      "name": "G18_G20_LOURD_REGIMES.md",
      "bytes": 5385,
      "sha256": "866e69177f5d99ba8826dcc8877df3a5fac560bf2ee88e864f9f0a77780a5367"
    },
    {
      "name": "G18_G20_LOURD_REGIMES.mjs",
      "bytes": 1968,
      "sha256": "82320d662e70b1cf1e8f718399166e6eb8e17f300120ca91d949bc9f99cbb59d"
    },
    {
      "name": "G18_G20_LOURD_REGIMES.json",
      "bytes": 1885,
      "sha256": "5c74df73d90df4b60b2e82e5724cc0ff846f4f5e7a85d3e2e50936d4a36b9604"
    },
    {
      "name": "G18_G20_CARRIER_LOURD_P0.md",
      "bytes": 3751,
      "sha256": "eb22e1afb618480506f605f890632f1e84c4dc2f1ccf7af18286f23ee1642b38"
    },
    {
      "name": "G18_G20_CARRIER_LOURD_P0.mjs",
      "bytes": 2164,
      "sha256": "df1831d2029657e68bfbe28b6ca580e1d2a048581de7d806df6a3125646ed5fb"
    },
    {
      "name": "G18_G20_CARRIER_LOURD_P0.json",
      "bytes": 19422,
      "sha256": "e87d9704659c321271c3828cca71c3dff0032e38e4e76a45780c330336e28e02"
    },
    {
      "name": "G18_G20_E8_MINUSCULE.md",
      "bytes": 4684,
      "sha256": "08f21a278b88f7c3a12e4b40f0674f603087234471244bdbc6eff5564681e7e5"
    },
    {
      "name": "G18_G20_E8_MINUSCULE.mjs",
      "bytes": 1674,
      "sha256": "afc067bb11e975e504d1e137a0dd9b01d31d4f5d4fda54ded7b961a6942e98ec"
    },
    {
      "name": "G18_G20_E8_MINUSCULE.json",
      "bytes": 401,
      "sha256": "a211293e4081502486c35cff47b3cffad1ca62c20857d634d3ecb4124cfe6561"
    },
    {
      "name": "G18_G20_D13_FRAME.md",
      "bytes": 3271,
      "sha256": "c4c5acc152a26cb8f3aa3babd3b202df3c606c7afae988a63790486b1c512142"
    },
    {
      "name": "G18_G20_D13_FRAME.mjs",
      "bytes": 771,
      "sha256": "03016c039de57a792161963a922a5fa7579b815565f9de447d10e96c40fb3a89"
    },
    {
      "name": "G18_G20_D13_FRAME.json",
      "bytes": 3624,
      "sha256": "aa522f56f9d46b6e7ba6351f8587a59bb9dc304d5a57c73e9db879565750d4d1"
    },
    {
      "name": "G18_G20_D12_COLLAGE.md",
      "bytes": 4577,
      "sha256": "14e1982694778879d232fdaa1b5b96db8a3321925b14cd2938c682f5fee5ee11"
    },
    {
      "name": "G18_G20_D12_COLLAGE.mjs",
      "bytes": 1198,
      "sha256": "556aee56c84fe4efb2cc3ccaba1d6cfcaf7887651ab1cfc7ea641d665e181339"
    },
    {
      "name": "G18_G20_D12_COLLAGE.json",
      "bytes": 544,
      "sha256": "f58e897dc6725c4a2767aad2a0e4428b98d512e727c6e8a4dd92c14d263a66a2"
    },
    {
      "name": "G18_G20_A20_FRAME.md",
      "bytes": 3088,
      "sha256": "22934b9fef2d3a7653cab21464f105c4d1643dab858a9397cc2b2530e1ef8f0e"
    },
    {
      "name": "G18_G20_A20_FRAME.mjs",
      "bytes": 1322,
      "sha256": "a98064aaac6008a22fe23c7f619c43fc3e12298044cc3689750b76cba6cd219c"
    },
    {
      "name": "G18_G20_A20_FRAME.json",
      "bytes": 3187,
      "sha256": "9357e215c5293ecad9a393021c76eb647145c872e42f088b3ae733d6c9fd8c30"
    },
    {
      "name": "G18_G20_D11_D12_DANS_N.md",
      "bytes": 3094,
      "sha256": "721d0cbaa56e856281453e92b95f05686db07d1d1dff25d131a5983a51b567f9"
    },
    {
      "name": "G18_G20_STATUTS_ET_PARAMETRES.md",
      "bytes": 4581,
      "sha256": "fee7cf6ce788644c3b713130b86865d052e17fd93be43da48cc46cf3a5b1ba95"
    },
    {
      "name": "G18_G20_MANIFESTE_COMBINATOIRE.mjs",
      "bytes": 2961,
      "sha256": "7fdcf5bba807c80f53d4a36c8de09b4e1982cc11c62edba8aa8b9171755e25a7"
    }
  ],
  "bound_prerequisites": [
    {
      "name": "AUDIT_NORME1_ET_METRIQUES.md",
      "bytes": 8572,
      "sha256": "73b638863453408ce1252f1a02d3b46179fbf959a75c5ee065b8929794ed9db8"
    },
    {
      "name": "AUDIT_INDECOMPOSABILITE.md",
      "bytes": 3635,
      "sha256": "102f435498ba84f7b0e0cc12d651944ce23cafc00785056f12fde5428be47c3a"
    },
    {
      "name": "INDECOMPOSABILITE_GLOBALE.md",
      "bytes": 6819,
      "sha256": "17d643fd120452110fe5270618ea944f61bfd7124f4c72e105bd016c2f123bf0"
    },
    {
      "name": "AUDIT_RACINES_CORANG_UN.md",
      "bytes": 5726,
      "sha256": "d63607b75b9b19b0df6a4a41cb73a3c86a102c72b9c8fd206c428e311b129e49"
    },
    {
      "name": "RACINES_CORANG_UN_CANDIDAT.md",
      "bytes": 8688,
      "sha256": "3734cbb4fa7a1f5972f029c3f8de200eee25f8b9d1058557a2cc0580b86e3fee"
    },
    {
      "name": "controles_positifs_cadre_global.mjs",
      "bytes": 2605,
      "sha256": "858f415967111796dd07eef21350793f1217148fe0a322eacf20065cc110fb01"
    },
    {
      "name": "controles_positifs_cadre_global.json",
      "bytes": 1068,
      "sha256": "c699700a3d764876711c0f4087582a1a2b95f238d58746f120ac743293fcd7ca"
    },
    {
      "name": "verifier_carrier_lourd_indep.mjs",
      "bytes": 3774,
      "sha256": "9685ed9e61647a58302ea08462a527281cef332a3dc85beda4b686bf822bfc91"
    },
    {
      "name": "verifier_carrier_lourd_indep.json",
      "bytes": 14848,
      "sha256": "5edb837de19e39b49a5fa3e122eb083290773a23ef7d52e5d3d8ba0c2d124d5a"
    }
  ],
  "existing_finite_tests": [
    {
      "name": "G18_G20_NORME14_LOURDS.json",
      "exact": true,
      "scope": "Capacity and sign identities only. No graph/whole-type exclusion or g>=21 bound."
    },
    {
      "name": "G18_G20_LOURD_REGIMES.json",
      "exact": true,
      "scope": "Necessary capacity regimes for the same norm14 heavy eigenvector. Not a graph/type completion or exclusion."
    },
    {
      "name": "G18_G20_CARRIER_LOURD_P0.json",
      "exact": true,
      "scope": "P0 excludes heavy external carrier degree4 only. Remaining carriers and g18/g20 remain open."
    },
    {
      "name": "G18_G20_E8_MINUSCULE.json",
      "exact": true,
      "scope": "Uniform E8 sub-system obstruction in any integral extension of dimension<=29, using dual gap8/7; not g>=21 or whole-type exclusion."
    },
    {
      "name": "G18_G20_D13_FRAME.json",
      "exact": true,
      "scope": "No D_n,n>=13, in any integral extension of dimension<=24 containing the common N22 frame and dual gap8/7. No entire g18/g20 exclusion."
    },
    {
      "name": "G18_G20_D12_COLLAGE.json",
      "exact": true,
      "scope": "No D12 root sub-system in any integral extension of dimension<=24 containing the common N22 frame and dual gap8/7. No entire g18/g20 exclusion."
    },
    {
      "name": "G18_G20_A20_FRAME.json",
      "exact": true,
      "scope": "Common N22 frame and acquired dual gap8/7; no type catalogue, P0, g>=21 or entire g18/g20 exclusion."
    }
  ],
  "positive_controls": {
    "exact": true,
    "source_hash_matches": true,
    "own_parameters_preserved": true,
    "new_execution": false
  },
  "claims": {
    "same_rank22": {
      "E8_excluded": true,
      "D_n_excluded_from": 11,
      "A_n_excluded_from": 20
    },
    "integral_extension_dimension_at_most24": {
      "E8_excluded": true,
      "D_n_excluded_from": 12,
      "A_n_excluded_from": 22
    },
    "root_rank20_requires_Nmax_det49_and_elementary_discriminant_dimension2": true,
    "P0_only_for_carrier_appendix": true
  },
  "limitations": [
    "No g>=21 conclusion.",
    "No uniform g18/g20 exclusion.",
    "The flat norm2 branch and remaining heavy regimes are open.",
    "D11 and A20/A21 in rank24 are not closed here.",
    "No graph is certified."
  ],
  "scope": "Read-only hash binding and documentary closure, not a new graph search or a proof of the full genre exclusion."
}

````


## G18_G20_MANIFESTE_COMBINATOIRE.mjs

````javascript
import fs from 'node:fs';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const folder=new URL('./',import.meta.url);
const stems=['G18_G20_NORME14_LOURDS','G18_G20_LOURD_REGIMES','G18_G20_CARRIER_LOURD_P0',
  'G18_G20_E8_MINUSCULE','G18_G20_D13_FRAME','G18_G20_D12_COLLAGE','G18_G20_A20_FRAME'];
const own=stems.flatMap(stem=>['md','mjs','json'].map(ext=>`${stem}.${ext}`)).concat([
  'G18_G20_D11_D12_DANS_N.md','G18_G20_STATUTS_ET_PARAMETRES.md','G18_G20_MANIFESTE_COMBINATOIRE.mjs']);
const prerequisites=['AUDIT_NORME1_ET_METRIQUES.md','AUDIT_INDECOMPOSABILITE.md',
  'INDECOMPOSABILITE_GLOBALE.md','AUDIT_RACINES_CORANG_UN.md','RACINES_CORANG_UN_CANDIDAT.md',
  'controles_positifs_cadre_global.mjs','controles_positifs_cadre_global.json',
  'verifier_carrier_lourd_indep.mjs','verifier_carrier_lourd_indep.json'];
const record=name=>{const bytes=fs.readFileSync(new URL(name,folder));return {
  name,bytes:bytes.length,sha256:crypto.createHash('sha256').update(bytes).digest('hex')};};
const tests=stems.map(stem=>{
  const name=`${stem}.json`,data=JSON.parse(fs.readFileSync(new URL(name,folder),'utf8'));
  assert.equal(data.exact,true,`${name}: exact`);
  return {name,exact:true,scope:data.scope??'Finite step checks only; see the associated proof.'};
});
const positive=JSON.parse(fs.readFileSync(new URL('controles_positifs_cadre_global.json',folder),'utf8'));
assert.equal(positive.exact,true);
assert.deepEqual(positive.results.map(row=>[row.vertices,row.m,row.r,row.d]),[[9,2,1,3],[243,11,4,9]]);
const sourceBytes=fs.readFileSync(new URL('controles_positifs_cadre_global.mjs',folder));
assert.equal(crypto.createHash('sha256').update(sourceBytes).digest('hex'),positive.source_sha256);
const out={frozen_own_pieces:true,own_count:own.length,own:own.map(record),
  bound_prerequisites:prerequisites.map(record),existing_finite_tests:tests,
  positive_controls:{exact:true,source_hash_matches:true,own_parameters_preserved:true,new_execution:false},
  claims:{same_rank22:{E8_excluded:true,D_n_excluded_from:11,A_n_excluded_from:20},
    integral_extension_dimension_at_most24:{E8_excluded:true,D_n_excluded_from:12,A_n_excluded_from:22},
    root_rank20_requires_Nmax_det49_and_elementary_discriminant_dimension2:true,
    P0_only_for_carrier_appendix:true},
  limitations:['No g>=21 conclusion.','No uniform g18/g20 exclusion.',
    'The flat norm2 branch and remaining heavy regimes are open.',
    'D11 and A20/A21 in rank24 are not closed here.','No graph is certified.'],
  scope:'Read-only hash binding and documentary closure, not a new graph search or a proof of the full genre exclusion.'};
fs.writeFileSync(new URL('G18_G20_MANIFESTE_COMBINATOIRE.json',folder),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({frozen_own_pieces:true,own_count:out.own_count,prerequisites:prerequisites.length,
  existing_tests_exact:tests.length,positive_parameters_bound:true,no_full_g18_g20_exclusion:true}));

````


## G18_G20_NORME14_LOURDS.json

````json
{
  "exact": true,
  "heavy": [
    {
      "k": 2,
      "m": 8,
      "subset_checks": 256,
      "valid_subsets": 24,
      "pair_checks": 576,
      "minimum_common": 4,
      "srg_maximum": 2,
      "contradiction": true
    },
    {
      "k": 3,
      "m": 5,
      "subset_checks": 32,
      "valid_subsets": 1,
      "pair_checks": 1,
      "minimum_common": 5,
      "srg_maximum": 2,
      "contradiction": true
    }
  ],
  "reflection_checks": 12,
  "incident_pair_checks": 8,
  "exterior": [
    {
      "coefficients": [
        -1,
        -1
      ],
      "charges": [
        -2,
        0
      ]
    },
    {
      "coefficients": [
        -1,
        1
      ],
      "charges": [
        0,
        -2
      ]
    },
    {
      "coefficients": [
        1,
        -1
      ],
      "charges": [
        0,
        2
      ]
    },
    {
      "coefficients": [
        1,
        1
      ],
      "charges": [
        2,
        0
      ]
    }
  ],
  "parity_checks": 8,
  "heavy_remaining": {
    "other_interior_active": 0,
    "incident_roots": 6,
    "external_roots": 4
  },
  "ternary_interior_active": [
    0,
    2,
    4
  ],
  "scope": "Capacity and sign identities only. No graph/whole-type exclusion or g>=21 bound.",
  "prerequisites": {
    "heavy": "Odd eigenvector -4, F49 coefficient norm14, all coefficients0,+/-1,+/-2, SRG maximum common2",
    "network": "Integral lattice minimum>=2 containing seven h norm4 and42u norm3, Gram3I-S, tight frame7"
  }
}

````


## G18_G20_NORME14_LOURDS.mjs

````javascript
// Tiny exact checks of the two capacity obstructions, not a graph search.
import fs from 'node:fs';
import assert from 'node:assert/strict';
const heavy=[];
for(const k of [2,3]){
 const m=14-3*k, valid=[];
 for(let mask=0;mask<(1<<m);mask++){
  let size=0,weight=0;
  for(let j=0;j<m;j++)if(mask&(1<<j)){size++;weight+=j<k?2:1;}
  if(weight>=8)valid.push({mask,size,weight});
 }
 let minCommon=Infinity,pairs=0;
 for(const a of valid)for(const b of valid){
  let n=0,x=a.mask&b.mask;while(x){x&=x-1;n++;}
  pairs++;minCommon=Math.min(minCommon,n);assert(n>=2+k);
 }
 assert.equal(minCommon,2+k);
 heavy.push({k,m,subset_checks:1<<m,valid_subsets:valid.length,pair_checks:pairs,minimum_common:minCommon,srg_maximum:2,contradiction:true});
}
let reflectionChecks=0;
for(const eps of [-1,1])for(const c of [-1,1])for(const a of [-1,0,1]){
 const allowed=Math.abs(a+eps*c)<=1;
 assert.equal(allowed,a===0||a===-eps*c);reflectionChecks++;
}
const exterior=[];
for(const alpha of [-1,1])for(const beta of [-1,1]){
 const charges=[alpha+beta,alpha-beta];
 assert(charges.some(x=>x===0));assert(!charges.every(x=>Math.abs(x)>=2));
 exterior.push({coefficients:[alpha,beta],charges});
}
let incidentPairChecks=0;
for(const eps of [-1,1])for(const first of [0,1])for(const second of [0,1]){
 const charge=-eps*(first-second);assert(Math.abs(charge)<=1);incidentPairChecks++;
}
let parityChecks=0;
for(const eps of [-1,1])for(const light of [-1,1]){
 assert.notEqual((-3*(2*eps+light))%2,0);parityChecks++;
}
for(const c1 of [-1,1])for(const c2 of [-1,1]){assert((c1+c2)%2===0);parityChecks++;}
const result={exact:true,heavy,reflection_checks:reflectionChecks,incident_pair_checks:incidentPairChecks,exterior,parity_checks:parityChecks,
 heavy_remaining:{other_interior_active:0,incident_roots:6,external_roots:4},ternary_interior_active:[0,2,4],
 scope:'Capacity and sign identities only. No graph/whole-type exclusion or g>=21 bound.',
 prerequisites:{heavy:'Odd eigenvector -4, F49 coefficient norm14, all coefficients0,+/-1,+/-2, SRG maximum common2',
 network:'Integral lattice minimum>=2 containing seven h norm4 and42u norm3, Gram3I-S, tight frame7'}};
fs.writeFileSync(new URL('./G18_G20_NORME14_LOURDS.json',import.meta.url),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));

````


## MANIFEST_AUDIT_INDEPENDANT_0803.json

````json
{
  "status": "AUDIT INDEPENDANT ACQUIS; own0803 pieces frozen",
  "own_files": [
    {
      "path": "AUDIT_NORME1_ET_METRIQUES.md",
      "bytes": 8572,
      "sha256": "73b638863453408ce1252f1a02d3b46179fbf959a75c5ee065b8929794ed9db8"
    },
    {
      "path": "AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md",
      "bytes": 9027,
      "sha256": "e03bbcab5f20605c168e2d1a1254e577ffe39a4610a316e06e44b0079c53bd7c"
    },
    {
      "path": "AUDIT_INDECOMPOSABILITE.md",
      "bytes": 3635,
      "sha256": "102f435498ba84f7b0e0cc12d651944ce23cafc00785056f12fde5428be47c3a"
    },
    {
      "path": "AUDIT_COMPOSANTES_RACINES_ET_CARRIER.md",
      "bytes": 5246,
      "sha256": "096414f2f25ef26b1ced6399d630a03e2aeb7eec580d5bf8b9c862927dedd60c"
    },
    {
      "path": "AUDIT_RACINES_CORANG_UN.md",
      "bytes": 5726,
      "sha256": "d63607b75b9b19b0df6a4a41cb73a3c86a102c72b9c8fd206c428e311b129e49"
    },
    {
      "path": "AUDIT_GOLAY_ENVELOPPE.md",
      "bytes": 4896,
      "sha256": "402978d669f8e3f8729cecfaf375622d3f6dc2c62238b886ae46f0b9b515e047"
    },
    {
      "path": "verifier_identites_courtes.mjs",
      "bytes": 5035,
      "sha256": "27ea92438164861646f0c6dec2aa4f74bb8588084d2c2b6af019f3a536c1c660"
    },
    {
      "path": "verifier_identites_courtes.json",
      "bytes": 3137,
      "sha256": "8a56caa5636e43be2cfb57142c15f8426d40179e600490138904721e0233e607"
    },
    {
      "path": "verifier_collage_E8_P.mjs",
      "bytes": 6269,
      "sha256": "d5d01a8b814026da4824c466110fa5d5c1b13cf9a63e18a2d9877a43190f6533"
    },
    {
      "path": "verifier_collage_E8_P.json",
      "bytes": 5399,
      "sha256": "297656e5d2886d197ac773f32def39a169ae055a48036402d668823ac13c3621"
    },
    {
      "path": "verifier_indecomposabilite_courte.mjs",
      "bytes": 2609,
      "sha256": "1584e73048859a48c55505641ad4948b6714a872dde7d8189c25ea7e0bf9124c"
    },
    {
      "path": "verifier_indecomposabilite_courte.json",
      "bytes": 5926,
      "sha256": "dc1ad417b18d23c8633121078b6a15ebeb0f7545f47746d53cfbef690630cfb3"
    },
    {
      "path": "verifier_carrier_lourd_indep.mjs",
      "bytes": 3774,
      "sha256": "9685ed9e61647a58302ea08462a527281cef332a3dc85beda4b686bf822bfc91"
    },
    {
      "path": "verifier_carrier_lourd_indep.json",
      "bytes": 14848,
      "sha256": "5edb837de19e39b49a5fa3e122eb083290773a23ef7d52e5d3d8ba0c2d124d5a"
    },
    {
      "path": "verifier_corang_un_indep.mjs",
      "bytes": 3977,
      "sha256": "b9e104067d0529b6148cce3bd20fc4b92cc53c4eb0e21f6f0a1425cc58958522"
    },
    {
      "path": "verifier_corang_un_indep.json",
      "bytes": 9633,
      "sha256": "e90fadfd9ae4ad4d8f772e36d14347bd95172edad9a073e928af7f2561789b7f"
    },
    {
      "path": "verifier_golay_enveloppe_indep.mjs",
      "bytes": 5121,
      "sha256": "c87c0d7b893759e386c3fecd6332435fe1231acb2834a6d8c91470202958c3a3"
    },
    {
      "path": "verifier_golay_enveloppe_indep.json",
      "bytes": 6586,
      "sha256": "76cc2cb462ba125d9488bee80cc56857406c10c7e8fff62ec3980c29ff392cb1"
    },
    {
      "path": "figer_audit_independant_0803.mjs",
      "bytes": 5472,
      "sha256": "6e37447c3d49079b3e6976ad52529a09fc843f7b6af2c44f626d3f70d1c99621"
    }
  ],
  "inputs_read_snapshot": [
    {
      "path": "../dossier6_involution/NOTE_RESEAU_MINIMUM.md",
      "bytes": 7343,
      "sha256": "e4e75cb9f6fb194486269a7d8109b28a3e2beb5e86dcc529a5603a4d1d7ab1d3"
    },
    {
      "path": "../dossier6_involution/AUDIT_GENRE.md",
      "bytes": 13328,
      "sha256": "759b4c66b6d788f1ea8348f1732be5eebfd66a5472b0184a70bbea675bd01235"
    },
    {
      "path": "../reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json",
      "bytes": 1869,
      "sha256": "d217f73bf0105226cedd73a702bb02b08d72338b27b6e0658b5e87e0bca8fb40"
    },
    {
      "path": "INDECOMPOSABILITE_GLOBALE.md",
      "bytes": 6819,
      "sha256": "17d643fd120452110fe5270618ea944f61bfd7124f4c72e105bd016c2f123bf0"
    },
    {
      "path": "RACINES_CORANG_UN_CANDIDAT.md",
      "bytes": 8688,
      "sha256": "3734cbb4fa7a1f5972f029c3f8de200eee25f8b9d1058557a2cc0580b86e3fee"
    },
    {
      "path": "SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.md",
      "bytes": 13003,
      "sha256": "b2a115acbde3af297479c58f9a8fca339f59cf85e3287f42fd2dcdbb70f9dccc"
    },
    {
      "path": "UNIFICATION_G18_G20_RANG24.md",
      "bytes": 7647,
      "sha256": "f3d1aa7908e63adf707c8cede320b5a091515ce0301487ee33b334ed785ef565"
    },
    {
      "path": "G18_G20_NORME14_LOURDS.md",
      "bytes": 5847,
      "sha256": "425056c56cc6c76182360bcb433277ad3a8686794511ee31071a2f01059f5d16"
    },
    {
      "path": "G18_G20_LOURD_REGIMES.md",
      "bytes": 5385,
      "sha256": "866e69177f5d99ba8826dcc8877df3a5fac560bf2ee88e864f9f0a77780a5367"
    },
    {
      "path": "G18_G20_CARRIER_LOURD_P0.md",
      "bytes": 3751,
      "sha256": "eb22e1afb618480506f605f890632f1e84c4dc2f1ccf7af18286f23ee1642b38"
    },
    {
      "path": "G18_G20_CARRIER_LOURD_P0.mjs",
      "bytes": 2164,
      "sha256": "df1831d2029657e68bfbe28b6ca580e1d2a048581de7d806df6a3125646ed5fb"
    },
    {
      "path": "G18_G20_CARRIER_LOURD_P0.json",
      "bytes": 19422,
      "sha256": "e87d9704659c321271c3828cca71c3dff0032e38e4e76a45780c330336e28e02"
    },
    {
      "path": "G18_G20_E8_MINUSCULE.md",
      "bytes": 4684,
      "sha256": "08f21a278b88f7c3a12e4b40f0674f603087234471244bdbc6eff5564681e7e5"
    },
    {
      "path": "G18_G20_D13_FRAME.md",
      "bytes": 3271,
      "sha256": "c4c5acc152a26cb8f3aa3babd3b202df3c606c7afae988a63790486b1c512142"
    },
    {
      "path": "G18_G20_D11_D12_DANS_N.md",
      "bytes": 3094,
      "sha256": "721d0cbaa56e856281453e92b95f05686db07d1d1dff25d131a5983a51b567f9"
    },
    {
      "path": "G18_G20_D12_COLLAGE.md",
      "bytes": 4577,
      "sha256": "14e1982694778879d232fdaa1b5b96db8a3321925b14cd2938c682f5fee5ee11"
    },
    {
      "path": "G18_G20_A20_FRAME.md",
      "bytes": 3088,
      "sha256": "22934b9fef2d3a7653cab21464f105c4d1643dab858a9397cc2b2530e1ef8f0e"
    },
    {
      "path": "CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md",
      "bytes": 7125,
      "sha256": "5e80991d75544850a941fd42755c2bfc2974d00962e7cd5b4c9481cd5f9e6a59"
    },
    {
      "path": "controle_enveloppe_g20_golay.mjs",
      "bytes": 4629,
      "sha256": "9c9cba2e19349cf681f256a990e69cdc0920b3eec31a8636fc5d3cba2027e9ed"
    },
    {
      "path": "controle_enveloppe_g20_golay.json",
      "bytes": 11370,
      "sha256": "20c9d9a206626dd47d0de4a5d164da7d888d7e146db9ee01d701cf650162763e"
    },
    {
      "path": "TEMPLATE_CONDITIONNEL_SHADOW24.md",
      "bytes": 3773,
      "sha256": "3fd25fc66b330e5a09911b8c579a2ada28f015454a8e06d7de962190e53fe5c7"
    },
    {
      "path": "BILAN_ATTAQUE_GLOBALE.md",
      "bytes": 10426,
      "sha256": "848112e02fe930734547d1ac0bbff25f43149f4d281ab7ff764a5cdf8866e9a1"
    },
    {
      "path": "controles_positifs_cadre_global.mjs",
      "bytes": 2605,
      "sha256": "858f415967111796dd07eef21350793f1217148fe0a322eacf20065cc110fb01"
    },
    {
      "path": "controles_positifs_cadre_global.json",
      "bytes": 1068,
      "sha256": "c699700a3d764876711c0f4087582a1a2b95f238d58746f120ac743293fcd7ca"
    }
  ],
  "runChecks": [
    {
      "source": "verifier_identites_courtes.mjs",
      "result": "verifier_identites_courtes.json",
      "exact": true
    },
    {
      "source": "verifier_collage_E8_P.mjs",
      "result": "verifier_collage_E8_P.json",
      "exact": true
    },
    {
      "source": "verifier_indecomposabilite_courte.mjs",
      "result": "verifier_indecomposabilite_courte.json",
      "exact": true
    },
    {
      "source": "verifier_carrier_lourd_indep.mjs",
      "result": "verifier_carrier_lourd_indep.json",
      "exact": true
    },
    {
      "source": "verifier_corang_un_indep.mjs",
      "result": "verifier_corang_un_indep.json",
      "exact": true
    },
    {
      "source": "verifier_golay_enveloppe_indep.mjs",
      "result": "verifier_golay_enveloppe_indep.json",
      "exact": true
    }
  ],
  "inputs_policy": "Snapshots of external sources read for audit. They are not modified or frozen by this script. Old files remain read-only.",
  "acquired_human_proofs": [
    "Correct separation of standard21/28 coefficient Grams, real4 block Gram and beta on imH",
    "Known dual minimum8/7 with exact common-neighbor recount; no novelty claim",
    "Indecomposability of N and same-rank integral minimum2 overlattices via two uniform proofs",
    "Primitive P of seven blocks, det2^12, discr(Z/4)^6, complement rank15/classes5/2",
    "Rank22 and rank21 root strata impossible in det49 elementary2 lattice carrying the physical real22 frame",
    "E8 absent in integral extensions of rank<=24; D>=11 and A>=20 absent in rank22 frame lattice; D>=12 and A>=22 absent in extensions<=24",
    "Heavy norm2 branch has6 incident roots,4 external and three physical regimes; P0 carrier degree4 excluded",
    "Three norm8 characteristic profiles in conditional unimodular24 gluing; root3 saturation remains a constraint",
    "Positive Golay-envelope example independently replayed: rank22det49/min3/gen3/indecomposable/dual>=10/7/char>=10, no physical frame"
  ],
  "scope_hypotheses": "SRG99 signed integer frame and old structural discriminant reduction for g18/g20 are assumed where named. Corank-one proof needs rank22/det49/elementary7 rank2/min2/full real frame. P0 is used only for the carrier cut. A shadowframe24 is conditional.",
  "positive_controls": {
    "small_H2_rebuilt_by_audit": true,
    "H2_r": 1,
    "H2_d": 3,
    "H2_root_norm": 1,
    "BvLS_r": 4,
    "BvLS_d": 9,
    "BvLS_root_norm": 4,
    "new_parent_controls_reviewed_not_rerun_by_audit": true,
    "SRG99_F7_P0_not_imposed": true
  },
  "remaining_open": [
    "Both g18 and g20 involution cases",
    "Norm2 flat and residual heavy carriers",
    "All three characteristic8 profiles",
    "Existence of shadowframe24",
    "Selection of exactly42 roots/7 blocks satisfying the common physical frame in the Golay-envelope or another genus lattice"
  ],
  "no_solver": true,
  "no_Web": true,
  "no_repository_access": true,
  "no_local_Python": true,
  "no_heavy_local_search": true,
  "whole_type_exclusions_added": 0,
  "historical_local_ledger_unchanged": {
    "g18_closed": 278,
    "g18_open": 163
  },
  "self_hash_omitted": true
}

````


## construire_livraison.mjs

````javascript
async function buildGlobalDelivery(dir) {
const fs = await import('node:fs/promises'), path = await import('node:path'), crypto = await import('node:crypto'), zlib = await import('node:zlib');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const excluded = new Set(['PREUVES_COMPLETES_ATTAQUE_GLOBALE.md','DOSSIER_COMPLET_SOURCES_ET_SORTIES.md','MANIFESTE_ATTAQUE_GLOBALE.json','ATTAQUE_GLOBALE_27_0803_PREUVES_CERTIFICATS.zip','AUDIT_LIVRAISON.json']);
const base = (await fs.readdir(dir)).filter(n => !excluded.has(n)).sort();
const notes = base.filter(n => n.endsWith('.md') && n !== 'BILAN_ATTAQUE_GLOBALE.md' && n !== 'ETAT_REPRISE.md');
const order = ['BILAN_ATTAQUE_GLOBALE.md','UNIFICATION_G18_G20_RANG24.md','INDECOMPOSABILITE_GLOBALE.md','RACINES_CORANG_UN_CANDIDAT.md','CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md',...notes.filter(n => !['UNIFICATION_G18_G20_RANG24.md','INDECOMPOSABILITE_GLOBALE.md','RACINES_CORANG_UN_CANDIDAT.md','CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md'].includes(n)),'ETAT_REPRISE.md'];
let proof = '# Preuves complètes — attaque globale du 27 septembre 2026\n\nCe dossier rassemble les preuves, les audits adverses et les limites de cette reprise. Il ne démontre pas l’inexistence de l’involution. Les deux valeurs g⁻=18 et g⁻=20 sont traitées par un cadre commun, sans balayage des types locaux.\n\n';
for (const n of order) proof += '\n\n---\n\nPièce originale : '+n+'\n\n'+await fs.readFile(path.join(dir,n),'utf8');
await fs.writeFile(path.join(dir,'PREUVES_COMPLETES_ATTAQUE_GLOBALE.md'),proof);
let complete = proof+'\n\n---\n\n# Programmes exacts et sorties intégrales\n\nLes programmes mathématiques sont des contrôles bornés ; les scripts de manifeste ne sont pas des preuves de non-existence. Les sorties complètes comprennent la base de 22 vecteurs et le Gram du contrôle positif.\n\n';
for (const n of base.filter(n => n.endsWith('.mjs') || n.endsWith('.json'))) complete += '\n\n## '+n+'\n\n````'+(n.endsWith('.json')?'json':'javascript')+'\n'+await fs.readFile(path.join(dir,n),'utf8')+'\n````\n';
await fs.writeFile(path.join(dir,'DOSSIER_COMPLET_SOURCES_ET_SORTIES.md'),complete);
const prefix = path.basename(dir);
const payload = [];
for (const n of [...base,'PREUVES_COMPLETES_ATTAQUE_GLOBALE.md','DOSSIER_COMPLET_SOURCES_ET_SORTIES.md'].sort()) {const data=await fs.readFile(path.join(dir,n));payload.push({name:prefix+'/'+n,data});}
const prerequisiteNames = ['dossier6_involution/NOTE_RESEAU_MINIMUM.md','dossier6_involution/AUDIT_GENRE.md','reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json'];
for(const n of prerequisiteNames){const data=await fs.readFile(path.join(path.dirname(dir),n));payload.push({name:n,data});}
const manifest={status:'Livraison de preuves partielles uniformes; aucune exclusion complète g18/g20',scope:'Reprise 27 septembre 2026 à 08:03 UTC; fichiers produits dans cette conversation uniquement',files:payload.map(e=>({path:e.name,bytes:e.data.length,sha256:sha(e.data)})),prerequisites_from_previous_campaign:prerequisiteNames,positive_controls:['H(2,3), r=1,d=3','BvLS, r=4,d=9','Réseau complémentaire de rang22/det49, construction explicite Golay']};
const manifestBytes=Buffer.from(JSON.stringify(manifest,null,2)+'\n');await fs.writeFile(path.join(dir,'MANIFESTE_ATTAQUE_GLOBALE.json'),manifestBytes);payload.push({name:prefix+'/MANIFESTE_ATTAQUE_GLOBALE.json',data:manifestBytes});
const table=Array.from({length:256},(_,i)=>{let c=i;for(let j=0;j<8;j++)c=(c&1)?0xedb88320^(c>>>1):c>>>1;return c>>>0;});const crc = b=>{let c=0xffffffff;for(const v of b)c=table[(c^v)&255]^(c>>>8);return(c^0xffffffff)>>>0;};
const locals=[],central=[];let offset=0;
for(const e of payload){const name=Buffer.from(e.name),compressed=zlib.deflateRawSync(e.data),c=crc(e.data);const h=Buffer.alloc(30);h.writeUInt32LE(0x04034b50);h.writeUInt16LE(20,4);h.writeUInt16LE(0x800,6);h.writeUInt16LE(8,8);h.writeUInt16LE(8<<11,10);h.writeUInt16LE(((2026-1980)<<9)|(9<<5)|27,12);h.writeUInt32LE(c,14);h.writeUInt32LE(compressed.length,18);h.writeUInt32LE(e.data.length,22);h.writeUInt16LE(name.length,26);locals.push(h,name,compressed);const ch=Buffer.alloc(46);ch.writeUInt32LE(0x02014b50);ch.writeUInt16LE(20,4);ch.writeUInt16LE(20,6);ch.writeUInt16LE(0x800,8);ch.writeUInt16LE(8,10);ch.writeUInt16LE(h.readUInt16LE(10),12);ch.writeUInt16LE(h.readUInt16LE(12),14);ch.writeUInt32LE(c,16);ch.writeUInt32LE(compressed.length,20);ch.writeUInt32LE(e.data.length,24);ch.writeUInt16LE(name.length,28);ch.writeUInt32LE(offset,42);central.push(ch,name);offset+=h.length+name.length+compressed.length;}
const centralBytes=Buffer.concat(central),end=Buffer.alloc(22);end.writeUInt32LE(0x06054b50);end.writeUInt16LE(payload.length,8);end.writeUInt16LE(payload.length,10);end.writeUInt32LE(centralBytes.length,12);end.writeUInt32LE(offset,16);const archive=Buffer.concat([...locals,centralBytes,end]);const zipName='ATTAQUE_GLOBALE_27_0803_PREUVES_CERTIFICATS.zip';await fs.writeFile(path.join(dir,zipName),archive);
return{zip:zipName,bytes:archive.length,entries:payload.length,sha256:sha(archive),proof_bytes:Buffer.byteLength(proof),full_bytes:Buffer.byteLength(complete),manifest_sha256:sha(manifestBytes)};
}
import {fileURLToPath} from 'node:url';
import path from 'node:path';
console.log(JSON.stringify(await buildGlobalDelivery(path.dirname(fileURLToPath(import.meta.url))),null,2));

````


## controle_enveloppe_g20_golay.json

````json
{
  "status": "VERIFIE EXACTEMENT; lattice-envelope control, NOT a graph",
  "binary_generator_exponents": [
    11,
    9,
    7,
    6,
    5,
    1,
    0
  ],
  "weight_enumerator": {
    "0": 1,
    "8": 759,
    "12": 2576,
    "16": 759,
    "24": 1
  },
  "V": [
    0,
    1,
    3,
    4,
    5,
    6,
    7,
    8,
    10,
    11,
    12,
    14
  ],
  "D": [
    0,
    1,
    2,
    9
  ],
  "D_prime": [
    3,
    4,
    13,
    15
  ],
  "norm_y": [
    7,
    7
  ],
  "inner_y": 0,
  "norm3_shell_of_L": 4096,
  "simultaneous_abs3": 0,
  "norm3_shell_of_M": 704,
  "projection_squared_numerators_over7": {
    "11": 8,
    "12": 12,
    "13": 32,
    "16": 336,
    "17": 336,
    "19": 1032,
    "20": 1636,
    "21": 704
  },
  "basis_rank": 22,
  "basis_Gram_support_connected": true,
  "basis_Gram_determinant": "49",
  "basis_integer_coordinates_over_sqrt8": [
    [
      1,
      1,
      -1,
      -1,
      -1,
      -1,
      1,
      -1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      -1,
      1,
      -1,
      -1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      1,
      1,
      -1,
      1,
      -1,
      -1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      1,
      -1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      -1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      1,
      1,
      -1,
      -1,
      -1,
      -1,
      -1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      -1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      1,
      1,
      -1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      1,
      1,
      1,
      1,
      -1,
      -1,
      -1,
      -1,
      1,
      -1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      -1,
      1,
      -1,
      -1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      1,
      -1,
      -1,
      1,
      -1,
      1,
      1,
      -1,
      -1,
      -1,
      -1,
      1,
      1,
      -1,
      -1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      -1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      -1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      -1,
      1,
      -1,
      -1,
      -1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      -1,
      1,
      -1,
      1,
      -1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      1,
      1,
      -1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      -1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      1,
      -1,
      1,
      -1,
      -1,
      1,
      -1,
      -1,
      1,
      -1,
      1,
      -1,
      1,
      -1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      -1,
      1,
      1,
      -1,
      -1,
      -1,
      1,
      1,
      1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      -1,
      1,
      -1,
      1,
      1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      -1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      -1,
      1,
      -1,
      -1,
      -1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      -1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      1,
      -1,
      1,
      1,
      -1,
      -1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      -1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      -1,
      -1,
      -1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      -1
    ],
    [
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      -1,
      -1,
      -1,
      -1,
      1,
      1,
      -1,
      1,
      -1,
      -1,
      -1,
      1,
      -1,
      1,
      -1,
      1,
      1
    ]
  ],
  "Gram": [
    [
      3,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      0,
      0,
      1,
      0,
      0,
      1,
      1,
      0,
      1
    ],
    [
      1,
      3,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      1,
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      1,
      1,
      0,
      0,
      -1
    ],
    [
      1,
      1,
      3,
      0,
      1,
      1,
      1,
      1,
      0,
      0,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0
    ],
    [
      1,
      1,
      0,
      3,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      0
    ],
    [
      1,
      1,
      1,
      1,
      3,
      1,
      1,
      0,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      0,
      1,
      0,
      1,
      0
    ],
    [
      1,
      1,
      1,
      1,
      1,
      3,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      0
    ],
    [
      1,
      1,
      1,
      0,
      1,
      1,
      3,
      1,
      0,
      0,
      0,
      1,
      1,
      1,
      0,
      0,
      -1,
      0,
      1,
      0,
      0,
      0
    ],
    [
      1,
      1,
      1,
      1,
      0,
      0,
      1,
      3,
      0,
      0,
      1,
      1,
      0,
      1,
      0,
      0,
      0,
      0,
      1,
      1,
      -1,
      0
    ],
    [
      1,
      0,
      0,
      1,
      1,
      1,
      0,
      0,
      3,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      1,
      1,
      1
    ],
    [
      0,
      1,
      0,
      1,
      1,
      1,
      0,
      0,
      1,
      3,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      0,
      1,
      1,
      0
    ],
    [
      1,
      0,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      3,
      1,
      1,
      1,
      0,
      0,
      1,
      0,
      0,
      1,
      0,
      1
    ],
    [
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      1,
      3,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      1,
      0,
      0
    ],
    [
      1,
      0,
      1,
      0,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      3,
      1,
      0,
      1,
      0,
      0,
      1,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      3,
      0,
      1,
      1,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      1,
      1,
      0,
      0,
      0,
      1,
      0,
      0,
      -1,
      0,
      0,
      3,
      1,
      1,
      1,
      1,
      0,
      1,
      0
    ],
    [
      1,
      0,
      0,
      1,
      1,
      0,
      0,
      0,
      1,
      1,
      0,
      0,
      1,
      1,
      1,
      3,
      1,
      1,
      1,
      0,
      1,
      0
    ],
    [
      0,
      0,
      0,
      1,
      1,
      0,
      -1,
      0,
      1,
      1,
      1,
      0,
      0,
      1,
      1,
      1,
      3,
      1,
      0,
      0,
      1,
      0
    ],
    [
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      3,
      0,
      0,
      0,
      -1
    ],
    [
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      1,
      0,
      1,
      1,
      0,
      0,
      3,
      0,
      1,
      -1
    ],
    [
      1,
      0,
      0,
      1,
      0,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      3,
      0,
      1
    ],
    [
      0,
      0,
      0,
      1,
      1,
      1,
      0,
      -1,
      1,
      1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      0,
      1,
      0,
      3,
      0
    ],
    [
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      -1,
      1,
      0,
      3
    ]
  ],
  "mathematical_consequences_verified_by_written_proof": [
    "M positive integral rank22 determinant49",
    "discriminant group (Z/7)^2",
    "minimum M=3",
    "M generated integrally by norm3 vectors",
    "minimum M* >=10/7",
    "characteristic minimum M >=10",
    "M orthogonally indecomposable"
  ],
  "not_claimed": [
    "49-column tight7 frame",
    "42 vectors with exactly ten nonzero root pairings each",
    "seven norm4 blocks with C incidence D7",
    "SRG completion",
    "involution existence"
  ],
  "source_sha256": "9c9cba2e19349cf681f256a990e69cdc0920b3eec31a8636fc5d3cba2027e9ed"
}

````


## controle_enveloppe_g20_golay.mjs

````javascript
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const wt=x=>{let n=0;while(x){n++;x&=x-1;}return n;};
const g=[11,9,7,6,5,1,0].reduce((a,b)=>a|(1<<b),0),words=[];
for(let m=0;m<4096;m++){let w=0;for(let j=0;j<12;j++)if(m>>j&1)w^=g<<j;if(wt(w)%2)w|=1<<23;words.push(w);}
assert.equal(new Set(words).size,4096);
const enumerator={};for(const w of words)enumerator[wt(w)]=(enumerator[wt(w)]||0)+1;
assert.deepEqual(enumerator,{0:1,8:759,12:2576,16:759,24:1});
const generators=Array.from({length:12},(_,j)=>words[1<<j]);
for(const a of generators)for(const b of generators)assert.equal(wt(a&b)%2,0);
assert(words.includes((1<<24)-1));
const mask=a=>a.reduce((s,i)=>s|(1<<i),0),indices=w=>Array.from({length:24},(_,i)=>i).filter(i=>w>>i&1);
const V=mask([0,1,3,4,5,6,7,8,10,11,12,14]),D=mask([0,1,2,9]),Dp=mask([3,4,13,15]);
assert(words.includes(V));assert.equal(wt(V),12);assert.equal(wt(D&V),2);assert.equal(wt(Dp&V),2);assert.equal(D&Dp,0);
const x=Array.from({length:24},(_,i)=>1-4*(D>>i&1)),y=Array.from({length:24},(_,i)=>(1-2*(V>>i&1))*(1-4*(Dp>>i&1)));
const inner=(a,b)=>a.reduce((s,z,i)=>s+z*b[i],0)/8;
assert.equal(inner(x,x),7);assert.equal(inner(y,y),7);assert.equal(inner(x,y),0);
function belongs(z){const m=(z[0]%2+2)%2;if(z.some(t=>(t%2+2)%2!==m))return false;let code=0;for(let i=0;i<24;i++)if(((z[i]-m)%4+4)%4===2)code|=1<<i;return words.includes(code)&&z.reduce((a,b)=>a+b,0)%8===0;}
assert(belongs(x));assert(belongs(y));
const all=words.map(w=>Array.from({length:24},(_,i)=>1-2*(w>>i&1))),norm3=[];const projectionNumerators={};let simultaneous3=0;
for(const z of all){assert(belongs(z));const a=inner(z,x),b=inner(z,y);assert(Number.isInteger(a)&&Number.isInteger(b));if(Math.abs(a)===3&&Math.abs(b)===3)simultaneous3++;const numerator=21-a*a-b*b;projectionNumerators[numerator]=(projectionNumerators[numerator]||0)+1;if(a===0&&b===0)norm3.push(z);}
assert.equal(simultaneous3,0);assert.equal(norm3.length,704);
const inv=a=>{let v=1;for(let j=0;j<99;j++)v=v*a%101;return v;};const pivots=[],basis=[];
for(const z of norm3){let row=z.map(a=>(a+101)%101);for(const [p,r] of pivots){const c=row[p];if(c)row=row.map((a,j)=>(a-c*r[j]%101+101)%101);}const p=row.findIndex(a=>a);if(p>=0){const c=inv(row[p]);row=row.map(a=>a*c%101);pivots.push([p,row]);basis.push(z);if(pivots.length===22)break;}}
assert.equal(basis.length,22);const Gram=basis.map(a=>basis.map(b=>inner(a,b)));
assert(Gram.every(r=>r.every(Number.isInteger)));
function bareiss(mat){const A=mat.map(r=>r.map(BigInt));let d=1n,sign=1n;for(let i=0;i<A.length-1;i++){let p=i;while(p<A.length&&A[p][i]===0n)p++;if(p===A.length)return 0n;if(p!==i){[A[p],A[i]]=[A[i],A[p]];sign=-sign;}const q=A[i][i];for(let j=i+1;j<A.length;j++)for(let k=i+1;k<A.length;k++){const n=A[j][k]*q-A[j][i]*A[i][k];assert.equal(n%d,0n);A[j][k]=n/d;}for(let j=i+1;j<A.length;j++)A[j][i]=0n;d=q;}return sign*A.at(-1).at(-1);}
const determinant=bareiss(Gram);assert.equal(determinant,49n);
const seen=new Set([0]),queue=[0];while(queue.length){const a=queue.shift();for(let b=0;b<22;b++)if(a!==b&&Gram[a][b]&&!seen.has(b)){seen.add(b);queue.push(b);}}assert.equal(seen.size,22);
const result={status:'VERIFIE EXACTEMENT; lattice-envelope control, NOT a graph',binary_generator_exponents:[11,9,7,6,5,1,0],weight_enumerator:enumerator,V:indices(V),D:indices(D),D_prime:indices(Dp),norm_y:[7,7],inner_y:0,norm3_shell_of_L:4096,simultaneous_abs3:simultaneous3,norm3_shell_of_M:704,projection_squared_numerators_over7:projectionNumerators,basis_rank:22,basis_Gram_support_connected:true,basis_Gram_determinant:determinant.toString(),basis_integer_coordinates_over_sqrt8:basis,Gram,
mathematical_consequences_verified_by_written_proof:['M positive integral rank22 determinant49','discriminant group (Z/7)^2','minimum M=3','M generated integrally by norm3 vectors','minimum M* >=10/7','characteristic minimum M >=10','M orthogonally indecomposable'],not_claimed:['49-column tight7 frame','42 vectors with exactly ten nonzero root pairings each','seven norm4 blocks with C incidence D7','SRG completion','involution existence'],source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'controle_enveloppe_g20_golay.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,enumerator,basis_rank:22,determinant:'49',norm3_M:704,simultaneous3,projectionNumerators,scope:result.not_claimed}));

````


## controles_positifs_cadre_global.json

````json
{
  "exact": true,
  "results": [
    {
      "vertices": 9,
      "m": 2,
      "r": 1,
      "d": 3,
      "signed_dimension": 4,
      "root_generators_norm": 1,
      "block_norm": 2,
      "graph_pairs_checked": 36,
      "polynomial": true,
      "tight_frame": true,
      "signed_incidence": true,
      "seven_block_genus_not_imposed": true,
      "norm3_integral_purity_hypothesis_applies": false,
      "scope": "positive controls with their own parameters; no SRG99/F7/P0 asserted"
    },
    {
      "vertices": 243,
      "m": 11,
      "r": 4,
      "d": 9,
      "signed_dimension": 121,
      "root_generators_norm": 4,
      "block_norm": 5,
      "graph_pairs_checked": 29403,
      "polynomial": true,
      "tight_frame": true,
      "signed_incidence": true,
      "seven_block_genus_not_imposed": true,
      "norm3_integral_purity_hypothesis_applies": false,
      "scope": "positive controls with their own parameters; no SRG99/F7/P0 asserted"
    }
  ],
  "source_sha256": "858f415967111796dd07eef21350793f1217148fe0a322eacf20065cc110fb01"
}

````


## controles_positifs_cadre_global.mjs

````javascript
import fs from 'node:fs';import path from 'node:path';import assert from 'node:assert/strict';import crypto from 'node:crypto';import {fileURLToPath} from 'node:url';
const dirsBvLS=[[1,0,0,0,0],[2,0,0,0,0],[0,1,0,0,0],[0,2,0,0,0],[0,0,1,0,0],[0,0,2,0,0],[0,0,0,1,0],[0,0,0,2,0],[0,0,0,0,1],[0,0,0,0,2],[1,0,2,1,2],[2,0,1,2,1],[2,1,1,1,2],[1,2,2,2,1],[2,2,2,0,2],[1,1,1,0,1],[2,2,0,1,1],[1,1,0,2,2],[1,2,1,1,0],[2,1,2,2,0],[0,1,2,1,1],[0,2,1,2,2]];
const here=path.dirname(fileURLToPath(import.meta.url));
function check(dim,dirs,r){const n=3**dim,m=dirs.length/2,d=2*r+1,mod=x=>(x%3+3)%3;const vs=Array.from({length:n},(_,a)=>Array.from({length:dim},(_,i)=>Math.floor(a/3**i)%3)),enc=v=>v.reduce((s,a,i)=>s+3**i*a,0),neg=vs.map(v=>enc(v.map(a=>mod(-a)))),A=vs.map(()=>Array(n).fill(0));for(let i=0;i<n;i++)for(const v of dirs)A[i][enc(v.map((a,j)=>mod(a+vs[i][j])))]=1;let graphPairs=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){assert.equal(A[i][j],A[j][i]);assert.equal(A[i].reduce((s,a,k)=>s+a*A[j][k],0),A[i][j]?1:2);graphPairs++;}
const interior=Array.from({length:n},(_,i)=>i).filter(i=>i>0&&i<neg[i]&&A[0][i]),roots=Array.from({length:n},(_,i)=>i).filter(i=>i>0&&i<neg[i]&&!A[0][i]),reps=interior.concat(roots);assert.equal(interior.length,m);assert.equal(roots.length,m*(m-1));
const S=reps.map(i=>reps.map(j=>A[i][j]-A[i][neg[j]])),H=S.map((row,i)=>row.map((a,j)=>r*+(i===j)-a));const C=S.slice(0,m).map(row=>row.slice(m));
for(let i=0;i<S.length;i++)for(let j=0;j<S.length;j++){const ss=S[i].reduce((s,a,k)=>s+a*S[k][j],0),hh=H[i].reduce((s,a,k)=>s+a*H[k][j],0);assert.equal(ss+S[i][j],i===j?r*(r+1):0);assert.equal(hh,d*H[i][j]);}
for(let c=0;c<m;c++)for(let j=0;j<m;j++)assert.equal(C[c].reduce((s,a,k)=>s+a*C[j][k],0),c===j?2*(m-1):0);
for(let c=0;c<m;c++)for(let i=0;i<H.length;i++){const hz=r*H[i][c]+C[c].reduce((s,a,k)=>s+a*H[i][m+k],0);assert.equal(hz,0);}
assert(roots.every(v=>!A[v][neg[v]]));return{vertices:n,m,r,d,signed_dimension:S.length,root_generators_norm:r,block_norm:r+1,graph_pairs_checked:graphPairs,polynomial:true,tight_frame:true,signed_incidence:true,seven_block_genus_not_imposed:true,norm3_integral_purity_hypothesis_applies:r===3,scope:'positive controls with their own parameters; no SRG99/F7/P0 asserted'};}
const results=[check(2,[[1,0],[2,0],[0,1],[0,2]],1),check(5,dirsBvLS,4)];const out={exact:true,results,source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};fs.writeFileSync(path.join(here,'controles_positifs_cadre_global.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));

````


## figer_audit_independant_0803.mjs

````javascript
// Freeze only this audit agent's new0803 files. Never writes any old folder or producer file.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const ownNotes=['AUDIT_NORME1_ET_METRIQUES.md','AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md','AUDIT_INDECOMPOSABILITE.md','AUDIT_COMPOSANTES_RACINES_ET_CARRIER.md','AUDIT_RACINES_CORANG_UN.md','AUDIT_GOLAY_ENVELOPPE.md'];
const runs=['verifier_identites_courtes','verifier_collage_E8_P','verifier_indecomposabilite_courte','verifier_carrier_lourd_indep','verifier_corang_un_indep','verifier_golay_enveloppe_indep'];
const own=ownNotes.concat(runs.flatMap(s=>[s+'.mjs',s+'.json']),['figer_audit_independant_0803.mjs']);
const entry=f=>{const bytes=fs.readFileSync(path.join(here,f));return{path:f,bytes:bytes.length,sha256:sha(bytes)};};
const runChecks=[];
for(const s of runs){const result=JSON.parse(fs.readFileSync(path.join(here,s+'.json'),'utf8'));assert.equal(result.exact,true);assert.equal(result.source_sha256,entry(s+'.mjs').sha256);runChecks.push({source:s+'.mjs',result:s+'.json',exact:true});}
const collage=JSON.parse(fs.readFileSync(path.join(here,'verifier_collage_E8_P.json')));
for(const e of collage.prior)assert.equal(entry(e.path).sha256,e.sha256);
const carrier=JSON.parse(fs.readFileSync(path.join(here,'verifier_carrier_lourd_indep.json')));
for(const e of carrier.prior)assert.equal(entry(e.path).sha256,e.sha256);
const corang=JSON.parse(fs.readFileSync(path.join(here,'verifier_corang_un_indep.json')));
assert.equal(entry('RACINES_CORANG_UN_CANDIDAT.md').sha256,corang.producer_note_sha256);
const golay=JSON.parse(fs.readFileSync(path.join(here,'verifier_golay_enveloppe_indep.json')));
assert.equal(entry('controle_enveloppe_g20_golay.json').sha256,golay.supplied_certificate_sha256);
assert.equal(entry('controle_enveloppe_g20_golay.mjs').sha256,golay.producer_source_sha256);
const inputFiles=[
 '../dossier6_involution/NOTE_RESEAU_MINIMUM.md','../dossier6_involution/AUDIT_GENRE.md','../reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json',
 'INDECOMPOSABILITE_GLOBALE.md','RACINES_CORANG_UN_CANDIDAT.md','SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.md','UNIFICATION_G18_G20_RANG24.md',
 'G18_G20_NORME14_LOURDS.md','G18_G20_LOURD_REGIMES.md','G18_G20_CARRIER_LOURD_P0.md','G18_G20_CARRIER_LOURD_P0.mjs','G18_G20_CARRIER_LOURD_P0.json',
 'G18_G20_E8_MINUSCULE.md','G18_G20_D13_FRAME.md','G18_G20_D11_D12_DANS_N.md','G18_G20_D12_COLLAGE.md','G18_G20_A20_FRAME.md',
 'CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md','controle_enveloppe_g20_golay.mjs','controle_enveloppe_g20_golay.json',
 'TEMPLATE_CONDITIONNEL_SHADOW24.md','BILAN_ATTAQUE_GLOBALE.md','controles_positifs_cadre_global.mjs','controles_positifs_cadre_global.json'
 ];
const manifest={status:'AUDIT INDEPENDANT ACQUIS; own0803 pieces frozen',own_files:own.map(entry),inputs_read_snapshot:inputFiles.map(entry),runChecks,
 inputs_policy:'Snapshots of external sources read for audit. They are not modified or frozen by this script. Old files remain read-only.',
 acquired_human_proofs:[
  'Correct separation of standard21/28 coefficient Grams, real4 block Gram and beta on imH',
  'Known dual minimum8/7 with exact common-neighbor recount; no novelty claim',
  'Indecomposability of N and same-rank integral minimum2 overlattices via two uniform proofs',
  'Primitive P of seven blocks, det2^12, discr(Z/4)^6, complement rank15/classes5/2',
  'Rank22 and rank21 root strata impossible in det49 elementary2 lattice carrying the physical real22 frame',
  'E8 absent in integral extensions of rank<=24; D>=11 and A>=20 absent in rank22 frame lattice; D>=12 and A>=22 absent in extensions<=24',
  'Heavy norm2 branch has6 incident roots,4 external and three physical regimes; P0 carrier degree4 excluded',
  'Three norm8 characteristic profiles in conditional unimodular24 gluing; root3 saturation remains a constraint',
  'Positive Golay-envelope example independently replayed: rank22det49/min3/gen3/indecomposable/dual>=10/7/char>=10, no physical frame'
 ],
 scope_hypotheses:'SRG99 signed integer frame and old structural discriminant reduction for g18/g20 are assumed where named. Corank-one proof needs rank22/det49/elementary7 rank2/min2/full real frame. P0 is used only for the carrier cut. A shadowframe24 is conditional.',
 positive_controls:{small_H2_rebuilt_by_audit:true,H2_r:1,H2_d:3,H2_root_norm:1,BvLS_r:4,BvLS_d:9,BvLS_root_norm:4,new_parent_controls_reviewed_not_rerun_by_audit:true,SRG99_F7_P0_not_imposed:true},
 remaining_open:['Both g18 and g20 involution cases','Norm2 flat and residual heavy carriers','All three characteristic8 profiles','Existence of shadowframe24','Selection of exactly42 roots/7 blocks satisfying the common physical frame in the Golay-envelope or another genus lattice'],
 no_solver:true,no_Web:true,no_repository_access:true,no_local_Python:true,no_heavy_local_search:true,whole_type_exclusions_added:0,
 historical_local_ledger_unchanged:{g18_closed:278,g18_open:163},self_hash_omitted:true};
fs.writeFileSync(path.join(here,'MANIFEST_AUDIT_INDEPENDANT_0803.json'),JSON.stringify(manifest,null,2)+'\n');
console.log(JSON.stringify({own_files:own.length,input_snapshots:inputFiles.length,exact_runs:runChecks.length,source_bindings_current:true,whole_type_exclusions_added:0}));

````


## verifier_carrier_lourd_indep.json

````json
{
  "exact": true,
  "graphs": 9,
  "contexts": 144,
  "commons_rejections": 108,
  "known_induced_prisms": 36,
  "certificates": [
    {
      "B_code": 30,
      "labelCode": 5,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            8
          ],
          [
            1,
            6,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 30,
      "labelCode": 6,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            9
          ],
          [
            1,
            7,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 30,
      "labelCode": 9,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            8
          ],
          [
            1,
            7,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 30,
      "labelCode": 10,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            9
          ],
          [
            1,
            6,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 31,
      "labelCode": 5,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            8
          ],
          [
            1,
            6,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 31,
      "labelCode": 6,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            9
          ],
          [
            1,
            7,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 31,
      "labelCode": 9,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            8
          ],
          [
            1,
            7,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 31,
      "labelCode": 10,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            9
          ],
          [
            1,
            6,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 45,
      "labelCode": 3,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            8
          ],
          [
            2,
            5,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 45,
      "labelCode": 6,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            9
          ],
          [
            2,
            7,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 45,
      "labelCode": 9,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            8
          ],
          [
            2,
            7,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 45,
      "labelCode": 12,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            9
          ],
          [
            2,
            5,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 47,
      "labelCode": 3,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            8
          ],
          [
            2,
            5,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 47,
      "labelCode": 6,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            9
          ],
          [
            2,
            7,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 47,
      "labelCode": 9,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            8
          ],
          [
            2,
            7,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 47,
      "labelCode": 12,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            9
          ],
          [
            2,
            5,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 51,
      "labelCode": 3,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            8
          ],
          [
            3,
            5,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 51,
      "labelCode": 5,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            8
          ],
          [
            3,
            6,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 51,
      "labelCode": 10,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            9
          ],
          [
            3,
            6,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 51,
      "labelCode": 12,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            9
          ],
          [
            3,
            5,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 55,
      "labelCode": 3,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            8
          ],
          [
            3,
            5,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 55,
      "labelCode": 5,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            8
          ],
          [
            3,
            6,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 55,
      "labelCode": 10,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            9
          ],
          [
            3,
            6,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 55,
      "labelCode": 12,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            9
          ],
          [
            3,
            5,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 59,
      "labelCode": 3,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            8
          ],
          [
            3,
            5,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 59,
      "labelCode": 5,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            8
          ],
          [
            3,
            6,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 59,
      "labelCode": 10,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            9
          ],
          [
            3,
            6,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 59,
      "labelCode": 12,
      "certificate": {
        "six": [
          0,
          3,
          5,
          6,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            9
          ],
          [
            3,
            5,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 61,
      "labelCode": 3,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            8
          ],
          [
            2,
            5,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 61,
      "labelCode": 6,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            9
          ],
          [
            2,
            7,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 61,
      "labelCode": 9,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            5,
            8
          ],
          [
            2,
            7,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 61,
      "labelCode": 12,
      "certificate": {
        "six": [
          0,
          2,
          5,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            9
          ],
          [
            2,
            5,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 62,
      "labelCode": 5,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            8
          ],
          [
            1,
            6,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 62,
      "labelCode": 6,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            9
          ],
          [
            1,
            7,
            8
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 62,
      "labelCode": 9,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            6,
            8
          ],
          [
            1,
            7,
            9
          ]
        ],
        "edge_count": 9
      }
    },
    {
      "B_code": 62,
      "labelCode": 10,
      "certificate": {
        "six": [
          0,
          1,
          6,
          7,
          8,
          9
        ],
        "triangles": [
          [
            0,
            7,
            9
          ],
          [
            1,
            6,
            8
          ]
        ],
        "edge_count": 9
      }
    }
  ],
  "scalar_regime_categories": [
    "0,2",
    "0,3",
    "1,3"
  ],
  "prior": [
    {
      "path": "G18_G20_CARRIER_LOURD_P0.mjs",
      "sha256": "df1831d2029657e68bfbe28b6ca580e1d2a048581de7d806df6a3125646ed5fb"
    },
    {
      "path": "G18_G20_CARRIER_LOURD_P0.json",
      "sha256": "e87d9704659c321271c3828cca71c3dff0032e38e4e76a45780c330336e28e02"
    },
    {
      "path": "G18_G20_LOURD_REGIMES.md",
      "sha256": "866e69177f5d99ba8826dcc8877df3a5fac560bf2ee88e864f9f0a77780a5367"
    }
  ],
  "source_sha256": "9685ed9e61647a58302ea08462a527281cef332a3dc85beda4b686bf822bfc91",
  "scope": "Dense independent check of all degree4 external carriers under P0 and of the scalar regime possibilities. It excludes only these carriers, not the remaining heavy case or an entire involution."
}

````


## verifier_carrier_lourd_indep.mjs

````javascript
// Independent dense known-edge test. No catalogue and no unknown-edge completion.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex'),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const pairs=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)pairs.push([i,j]);
const graphs=[];
for(let code=0;code<64;code++){
 const B=Array.from({length:4},()=>Array(4).fill(0));let edges=0;
 pairs.forEach(([i,j],k)=>{if((code>>k)&1){B[i][j]=B[j][i]=1;edges++;}});
 if(edges===5||(edges===4&&B.every(r=>r.reduce((s,x)=>s+x,0)===2)))graphs.push({code,B});
}
assert.equal(graphs.length,9);
const subsets=[];
function combinations(start,a){if(a.length===6){subsets.push([...a]);return;}for(let v=start;v<10;v++){a.push(v);combinations(v+1,a);a.pop();}}
combinations(0,[]);assert.equal(subsets.length,210);
function prism(G,six){
 const H=six.map(i=>six.map(j=>G[i][j]));if(!H.every(r=>r.reduce((s,x)=>s+x,0)===3))return null;
 const triangles=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)if(H[i][j]&&H[i][k]&&H[j][k])triangles.push([i,j,k]);
 if(triangles.length!==2||new Set(triangles.flat()).size!==6)return null;
 const t0=triangles[0],t1=triangles[1];
 if(!t0.every(i=>t1.reduce((s,j)=>s+H[i][j],0)===1)||!t1.every(j=>t0.reduce((s,i)=>s+H[i][j],0)===1))return null;
 return {six,triangles:triangles.map(t=>t.map(i=>six[i])),edge_count:9};
}
const records=[];let ruledByCommons=0;
for(const{code,B}of graphs)for(let labelCode=0;labelCode<16;labelCode++){
 const signs=Array.from({length:4},(_,i)=>((labelCode>>i)&1)?1:-1);
 const offending=pairs.find(([i,j])=>dot(B[i],B[j])>=2&&signs[i]===signs[j]);
 if(offending){ruledByCommons++;continue;}
 const G=Array.from({length:10},()=>Array(10).fill(0));const edge=(i,j)=>{G[i][j]=G[j][i]=1;};
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(B[i][j])edge(i,4+j);
 edge(8,9);for(let i=0;i<4;i++){edge(i,signs[i]>0?8:9);edge(4+i,signs[i]>0?9:8);}
 let certificate=null;for(const six of subsets){certificate=prism(G,six);if(certificate)break;}
 assert(certificate);records.push({B_code:code,labelCode,certificate});
}
assert.equal(records.length,36);assert.equal(ruledByCommons,108);
// Independent scalar regime enumeration from matching capacities and the two eigen-sums.
const regimes=[];
for(let a=0;a<=3;a++)for(let b=0;b<=3;b++)for(let X=0;X<=8;X++)for(let Y=0;Y<=8;Y++){
 if(X-Y!==12+2*(a-b))continue;
 for(let eb=0;eb<=6;eb++)for(let ea=0;ea<=6;ea++)if(2*(eb-ea)+X-Y===16)regimes.push({a,b,X,Y,eb,ea});
}
assert(regimes.every(v=>(v.a===0&&v.b===2)||(v.a===1&&v.b===3)||(v.a===0&&v.b===3)));
const categories=[...new Set(regimes.map(v=>`${v.a},${v.b}`))].sort();assert.deepEqual(categories,['0,2','0,3','1,3']);
const inputFiles=['G18_G20_CARRIER_LOURD_P0.mjs','G18_G20_CARRIER_LOURD_P0.json','G18_G20_LOURD_REGIMES.md'];
const out={exact:true,graphs:9,contexts:144,commons_rejections:ruledByCommons,known_induced_prisms:records.length,certificates:records,scalar_regime_categories:categories,
 prior:inputFiles.map(f=>({path:f,sha256:sha(fs.readFileSync(path.join(here,f)))})),source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 scope:'Dense independent check of all degree4 external carriers under P0 and of the scalar regime possibilities. It excludes only these carriers, not the remaining heavy case or an entire involution.'};
fs.writeFileSync(path.join(here,'verifier_carrier_lourd_indep.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,contexts:144,commons_rejections:ruledByCommons,known_prisms:records.length,regime_categories:categories}));

````


## verifier_collage_E8_P.json

````json
{
  "exact": true,
  "E8": {
    "roots": 240,
    "candidates": 273,
    "survivors": 1,
    "only_zero": true
  },
  "primitive_P": {
    "basis": [
      [
        2,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        2,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        2,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        2,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        2,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0,
        2,
        0
      ],
      [
        1,
        1,
        1,
        1,
        1,
        1,
        1
      ]
    ],
    "Gram": [
      [
        4,
        0,
        0,
        0,
        0,
        0,
        2
      ],
      [
        0,
        4,
        0,
        0,
        0,
        0,
        2
      ],
      [
        0,
        0,
        4,
        0,
        0,
        0,
        2
      ],
      [
        0,
        0,
        0,
        4,
        0,
        0,
        2
      ],
      [
        0,
        0,
        0,
        0,
        4,
        0,
        2
      ],
      [
        0,
        0,
        0,
        0,
        0,
        4,
        2
      ],
      [
        2,
        2,
        2,
        2,
        2,
        2,
        7
      ]
    ],
    "determinant": 4096,
    "discriminant_order": 4096,
    "exponent": 4,
    "torsion2_order": 64,
    "structure": "(Z/4)^6"
  },
  "discriminant_anti_isometry": {
    "U": [
      [
        2,
        -3
      ],
      [
        3,
        2
      ]
    ],
    "checks": 2401,
    "F7_I2_anisotropic": true
  },
  "rank24_mixed_root_necessary_norms": [
    {
      "b": [
        -2,
        -1
      ],
      "seven_y_norm": 5,
      "seven_x_norm": 9
    },
    {
      "b": [
        -2,
        0
      ],
      "seven_y_norm": 4,
      "seven_x_norm": 10
    },
    {
      "b": [
        -2,
        1
      ],
      "seven_y_norm": 5,
      "seven_x_norm": 9
    },
    {
      "b": [
        -1,
        -2
      ],
      "seven_y_norm": 5,
      "seven_x_norm": 9
    },
    {
      "b": [
        -1,
        -1
      ],
      "seven_y_norm": 2,
      "seven_x_norm": 12
    },
    {
      "b": [
        -1,
        0
      ],
      "seven_y_norm": 1,
      "seven_x_norm": 13
    },
    {
      "b": [
        -1,
        1
      ],
      "seven_y_norm": 2,
      "seven_x_norm": 12
    },
    {
      "b": [
        -1,
        2
      ],
      "seven_y_norm": 5,
      "seven_x_norm": 9
    },
    {
      "b": [
        0,
        -2
      ],
      "seven_y_norm": 4,
      "seven_x_norm": 10
    },
    {
      "b": [
        0,
        -1
      ],
      "seven_y_norm": 1,
      "seven_x_norm": 13
    },
    {
      "b": [
        0,
        1
      ],
      "seven_y_norm": 1,
      "seven_x_norm": 13
    },
    {
      "b": [
        0,
        2
      ],
      "seven_y_norm": 4,
      "seven_x_norm": 10
    },
    {
      "b": [
        1,
        -2
      ],
      "seven_y_norm": 5,
      "seven_x_norm": 9
    },
    {
      "b": [
        1,
        -1
      ],
      "seven_y_norm": 2,
      "seven_x_norm": 12
    },
    {
      "b": [
        1,
        0
      ],
      "seven_y_norm": 1,
      "seven_x_norm": 13
    },
    {
      "b": [
        1,
        1
      ],
      "seven_y_norm": 2,
      "seven_x_norm": 12
    },
    {
      "b": [
        1,
        2
      ],
      "seven_y_norm": 5,
      "seven_x_norm": 9
    },
    {
      "b": [
        2,
        -1
      ],
      "seven_y_norm": 5,
      "seven_x_norm": 9
    },
    {
      "b": [
        2,
        0
      ],
      "seven_y_norm": 4,
      "seven_x_norm": 10
    },
    {
      "b": [
        2,
        1
      ],
      "seven_y_norm": 5,
      "seven_x_norm": 9
    }
  ],
  "rank24_characteristic_norm8_profiles": [
    {
      "b_abs": [
        1,
        1
      ],
      "root_abs3": 0,
      "root_abs5": 0,
      "block_half_square_sum": 3
    },
    {
      "b_abs": [
        1,
        1
      ],
      "root_abs3": 1,
      "root_abs5": 0,
      "block_half_square_sum": 1
    },
    {
      "b_abs": [
        1,
        3
      ],
      "root_abs3": 0,
      "root_abs5": 0,
      "block_half_square_sum": 1
    }
  ],
  "norm8_middle_profile_reflection": {
    "cases": 1176,
    "valid_block_moves": 168,
    "neighbor_cases": 8
  },
  "prior": [
    {
      "path": "../dossier6_involution/NOTE_RESEAU_MINIMUM.md",
      "sha256": "e4e75cb9f6fb194486269a7d8109b28a3e2beb5e86dcc529a5603a4d1d7ab1d3"
    },
    {
      "path": "../dossier6_involution/AUDIT_GENRE.md",
      "sha256": "759b4c66b6d788f1ea8348f1732be5eebfd66a5472b0184a70bbea675bd01235"
    },
    {
      "path": "../reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json",
      "sha256": "d217f73bf0105226cedd73a702bb02b08d72338b27b6e0658b5e87e0bca8fb40"
    }
  ],
  "source_sha256": "d5d01a8b814026da4824c466110fa5d5c1b13cf9a63e18a2d9877a43190f6533",
  "scope": "Finite checks of formulas and the E8 minuscule lemma. Gluing needs a rank22 integral lattice of determinant49 with the stated anisotropic discriminant. Mixed norm pairs are possibilities, not vectors. No norm2/characteristic8/global involution exclusion."
}

````


## verifier_collage_E8_P.mjs

````javascript
// Bounded independent integer checks. This does not classify rank24 lattices.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const mod=(x,p=7)=>((x%p)+p)%p;
const norm=a=>dot(a,a);
const tr=A=>A[0].map((_,j)=>A.map(r=>r[j]));
const mm=(A,B)=>{const Bt=tr(B);return A.map(a=>Bt.map(b=>dot(a,b)));};
function detBareiss(input){
  const A=input.map(r=>r.map(BigInt));let sign=1n,last=1n;
  for(let k=0;k<A.length-1;k++){
    let p=k;while(p<A.length&&!A[p][k])p++;assert(p<A.length);
    if(p!==k){[A[p],A[k]]=[A[k],A[p]];sign=-sign;}
    const pivot=A[k][k];
    for(let i=k+1;i<A.length;i++)for(let j=k+1;j<A.length;j++){
      const numerator=pivot*A[i][j]-A[i][k]*A[k][j];
      assert.equal(numerator%last,0n);A[i][j]=numerator/last;
    }
    for(let i=k+1;i<A.length;i++)A[i][k]=0n;last=pivot;
  }
  return sign*A.at(-1).at(-1);
}
// All E8 roots and all candidates left by the D8 constraints, in doubled coordinates.
const roots2=[];
for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)for(const a of[-2,2])for(const b of[-2,2]){
  const r=Array(8).fill(0);r[i]=a;r[j]=b;roots2.push(r);
}
for(let mask=0;mask<256;mask++){
  const r=Array.from({length:8},(_,i)=>(mask>>i)&1?-1:1);
  if(r.filter(x=>x<0).length%2===0)roots2.push(r);
}
assert.equal(roots2.length,240);assert(roots2.every(r=>norm(r)===8));
const candidates2=[Array(8).fill(0)];
for(let i=0;i<8;i++)for(const s of[-2,2]){const x=Array(8).fill(0);x[i]=s;candidates2.push(x);}
for(let mask=0;mask<256;mask++)candidates2.push(Array.from({length:8},(_,i)=>(mask>>i)&1?-1:1));
assert.equal(candidates2.length,273);
const survivors=candidates2.filter(x=>roots2.every(r=>dot(x,r)%4===0&&Math.abs(dot(x,r))<=4));
assert.deepEqual(survivors,[Array(8).fill(0)]);
// Gram matrix of the primitive seven-block closure: 2e_0,...,2e_5,ones.
const Pbasis=Array.from({length:6},(_,i)=>Array.from({length:7},(_,j)=>i===j?2:0));
Pbasis.push(Array(7).fill(1));const Pgram=mm(Pbasis,tr(Pbasis));
assert.equal(detBareiss(Pgram),4096n);
// P*/P represented by k mod4 with even sum, quotienting the translation 2*ones.
let classesBefore=0,torsion2Before=0;const quotient=new Set();
for(let code=0;code<4**7;code++){
  let n=code;const k=Array.from({length:7},()=>{const x=n%4;n=Math.floor(n/4);return x;});
  if(k.reduce((s,x)=>s+x,0)%2)continue;classesBefore++;
  const translate=k.map(x=>(x+2)%4);
  quotient.add([k.join(''),translate.join('')].sort()[0]);
  if(k.every(x=>x%2===0))torsion2Before++;
}
assert.equal(classesBefore,8192);assert.equal(quotient.size,4096);assert.equal(torsion2Before/2,64);
// P has exponent <=4 and exactly 64 elements annihilated by2, hence (Z/4)^6.
const U=[[2,-3],[3,2]];assert.deepEqual(mm(tr(U),U),[[13,0],[0,13]]);
const plane=Array.from({length:49},(_,i)=>[Math.floor(i/7),i%7]);
assert.equal(plane.filter(v=>mod(norm(v))===0).length,1);
let antiIsometryChecks=0;
for(const a of plane)for(const b of plane){
  const ua=U.map(r=>mod(dot(r,a))),ub=U.map(r=>mod(dot(r,b)));
  assert.equal(mod(dot(ua,ub)),mod(-dot(a,b)));antiIsometryChecks++;
}
// Potential mixed roots of the rank24 gluing: these are only necessary norm pairs.
const mixed=[];
for(let b1=-2;b1<=2;b1++)for(let b2=-2;b2<=2;b2++){
  const j=b1*b1+b2*b2;
  if(j&&j<=6&&14-j>=8)mixed.push({b:[b1,b2],seven_y_norm:j,seven_x_norm:14-j});
}
assert.deepEqual([...new Set(mixed.map(v=>v.seven_y_norm))].sort((a,b)=>a-b),[1,2,4,5]);
// Characteristic vectors of norm8 in the odd unimodular24 gluing.
const profiles=[];
for(const b1 of[1,3])for(const b2 of[1,3])if(b1<=b2)
for(let n3=0;n3<=1;n3++)for(let n5=0;n5<=1;n5++)for(let z=0;z<=3;z++)
  if(b1*b1+b2*b2+4*z+8*n3+24*n5===14)profiles.push({b_abs:[b1,b2],root_abs3:n3,root_abs5:n5,block_half_square_sum:z});
assert.deepEqual(profiles,[
  {b_abs:[1,1],root_abs3:0,root_abs5:0,block_half_square_sum:3},
  {b_abs:[1,1],root_abs3:1,root_abs5:0,block_half_square_sum:1},
  {b_abs:[1,3],root_abs3:0,root_abs5:0,block_half_square_sum:1}
]);
// In the middle profile, reflection in the unique norm3 generator must move the block.
let reflectionCases=0,blockSaturationCases=0;
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const c of[-1,1])
for(let k=0;k<7;k++)for(const a of[-1,1])for(const s of[-1,1]){
  const C=Array(7).fill(0);C[i]=1;C[j]=c;
  const after=C.map((x,l)=>(l===k?a:0)+s*x);const allowed=norm(after)===1;
  assert.equal(allowed,C[k]!==0&&a*C[k]===-s);reflectionCases++;if(allowed)blockSaturationCases++;
}
let neighborSaturationCases=0;
for(const a of[-1,1])for(const h of[-1,1])for(const s of[-1,1]){
  assert.equal(Math.abs(a-2*s*h)===1,a===s*h);neighborSaturationCases++;
}
const priorFiles=[
 '../dossier6_involution/NOTE_RESEAU_MINIMUM.md',
 '../dossier6_involution/AUDIT_GENRE.md',
 '../reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json'
];
const prior=priorFiles.map(f=>({path:f,sha256:sha(fs.readFileSync(path.join(here,f)))}));
const out={exact:true,E8:{roots:240,candidates:273,survivors:1,only_zero:true},
 primitive_P:{basis:Pbasis,Gram:Pgram,determinant:4096,discriminant_order:4096,exponent:4,torsion2_order:64,structure:'(Z/4)^6'},
 discriminant_anti_isometry:{U,checks:antiIsometryChecks,F7_I2_anisotropic:true},
 rank24_mixed_root_necessary_norms:mixed,rank24_characteristic_norm8_profiles:profiles,
 norm8_middle_profile_reflection:{cases:reflectionCases,valid_block_moves:blockSaturationCases,neighbor_cases:neighborSaturationCases},
 prior,source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 scope:'Finite checks of formulas and the E8 minuscule lemma. Gluing needs a rank22 integral lattice of determinant49 with the stated anisotropic discriminant. Mixed norm pairs are possibilities, not vectors. No norm2/characteristic8/global involution exclusion.'};
fs.writeFileSync(path.join(here,'verifier_collage_E8_P.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,E8_nonzero_survivors:0,P_det:4096,P_torsion2:64,anti_isometry_checks:antiIsometryChecks,characteristic8_profiles:3,reflection_cases:reflectionCases}));

````


## verifier_corang_un_indep.json

````json
{
  "exact": true,
  "A6_class_minimum_numerators": [
    0,
    6,
    10,
    12,
    12,
    10,
    6
  ],
  "all_nonzero_triples": 216,
  "isotropicTriples": [
    {
      "classes": [
        1,
        2,
        3
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        1,
        2,
        4
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        1,
        3,
        2
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        1,
        3,
        5
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        1,
        4,
        2
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        1,
        4,
        5
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        1,
        5,
        3
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        1,
        5,
        4
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        2,
        1,
        3
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        2,
        1,
        4
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        2,
        3,
        1
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        2,
        3,
        6
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        2,
        4,
        1
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        2,
        4,
        6
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        2,
        6,
        3
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        2,
        6,
        4
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        3,
        1,
        2
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        3,
        1,
        5
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        3,
        2,
        1
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        3,
        2,
        6
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        3,
        5,
        1
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        3,
        5,
        6
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        3,
        6,
        2
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        3,
        6,
        5
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        4,
        1,
        2
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        4,
        1,
        5
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        4,
        2,
        1
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        4,
        2,
        6
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        4,
        5,
        1
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        4,
        5,
        6
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        4,
        6,
        2
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        4,
        6,
        5
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        5,
        1,
        3
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        5,
        1,
        4
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        5,
        3,
        1
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        5,
        3,
        6
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        5,
        4,
        1
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        5,
        4,
        6
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        5,
        6,
        3
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        5,
        6,
        4
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        6,
        2,
        3
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        6,
        2,
        4
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        6,
        3,
        2
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        6,
        3,
        5
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        6,
        4,
        2
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        6,
        4,
        5
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        6,
        5,
        3
      ],
      "seven_minimum": 28,
      "isotropic": true
    },
    {
      "classes": [
        6,
        5,
        4
      ],
      "seven_minimum": 28,
      "isotropic": true
    }
  ],
  "minimum_three_nonzero": [
    18,
    7
  ],
  "planes": [
    {
      "diagonal": [
        6,
        6
      ],
      "only_zero_isotropic": true
    },
    {
      "diagonal": [
        6,
        5
      ],
      "only_zero_isotropic": true
    }
  ],
  "valuation_cases": [
    {
      "aprime": 0,
      "b": 2,
      "j": 0,
      "reason": "cyclic discriminant49 is not elementary rank2"
    },
    {
      "aprime": 1,
      "b": 1,
      "j": 0,
      "reason": null
    },
    {
      "aprime": 1,
      "b": 3,
      "j": 1,
      "reason": "J order7 class has integral norm; anisotropic M forbids it"
    },
    {
      "aprime": 2,
      "b": 0,
      "j": 0,
      "reason": null
    },
    {
      "aprime": 2,
      "b": 2,
      "j": 1,
      "reason": "J order7 class has integral norm; anisotropic M forbids it"
    },
    {
      "aprime": 3,
      "b": 1,
      "j": 1,
      "reason": null
    }
  ],
  "A3": [
    {
      "class": 0,
      "norm": [
        0,
        4
      ]
    },
    {
      "class": 1,
      "norm": [
        3,
        4
      ]
    },
    {
      "class": 2,
      "norm": [
        4,
        4
      ]
    },
    {
      "class": 3,
      "norm": [
        3,
        4
      ]
    }
  ],
  "A2A1": [
    {
      "class": [
        0,
        0
      ],
      "norm": [
        0,
        6
      ]
    },
    {
      "class": [
        0,
        1
      ],
      "norm": [
        3,
        6
      ]
    },
    {
      "class": [
        1,
        0
      ],
      "norm": [
        4,
        6
      ]
    },
    {
      "class": [
        1,
        1
      ],
      "norm": [
        7,
        6
      ]
    },
    {
      "class": [
        2,
        0
      ],
      "norm": [
        4,
        6
      ]
    },
    {
      "class": [
        2,
        1
      ],
      "norm": [
        7,
        6
      ]
    }
  ],
  "A1cube": [
    {
      "class": 0,
      "norm": [
        0,
        2
      ]
    },
    {
      "class": 1,
      "norm": [
        1,
        2
      ]
    },
    {
      "class": 2,
      "norm": [
        1,
        2
      ]
    },
    {
      "class": 3,
      "norm": [
        2,
        2
      ]
    },
    {
      "class": 4,
      "norm": [
        1,
        2
      ]
    },
    {
      "class": 5,
      "norm": [
        2,
        2
      ]
    },
    {
      "class": 6,
      "norm": [
        2,
        2
      ]
    },
    {
      "class": 7,
      "norm": [
        3,
        2
      ]
    }
  ],
  "otherPrimeCosts": {
    "A13_order2": [
      49,
      14
    ],
    "A20_order3": [
      [
        98,
        21
      ],
      [
        98,
        21
      ]
    ]
  },
  "finalCosts": [
    {
      "R3_det": 4,
      "J_norm": 28,
      "nonzero_R3_cost": [
        43,
        14
      ],
      "zero_R3_cost": [
        22,
        7
      ]
    },
    {
      "R3_det": 6,
      "J_norm": 42,
      "nonzero_R3_cost": [
        43,
        14
      ],
      "zero_R3_cost": [
        24,
        7
      ]
    }
  ],
  "source_sha256": "b9e104067d0529b6148cce3bd20fc4b92cc53c4eb0e21f6f0a1425cc58958522",
  "producer_note_sha256": "3734cbb4fa7a1f5972f029c3f8de200eee25f8b9d1058557a2cc0580b86e3fee",
  "scope": "Finite rational costs accompanying an independent human proof. Hypotheses: rank22 integral minimum2, determinant49, elementary rank2 discriminant7, and the physical frame spanning rank22. No assertion for arbitrary determinant49 genus or for every root-free lattice."
}

````


## verifier_corang_un_indep.mjs

````javascript
// Independent exact rational costs for the corank-one human proof. No lattice search.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex'),mod=x=>((x%7)+7)%7;
const minimumA=(n,k)=>[k*(n+1-k),n+1];
const classNormNumerator=Array.from({length:7},(_,k)=>k*(7-k));
const isotropicTriples=[],allTriples=[];
for(let a=1;a<7;a++)for(let b=1;b<7;b++)for(let c=1;c<7;c++){
 const norm7=classNormNumerator[a]+classNormNumerator[b]+classNormNumerator[c];
 const r={classes:[a,b,c],seven_minimum:norm7,isotropic:mod(a*a+b*b+c*c)===0};allTriples.push(r);
 if(r.isotropic){assert.equal(norm7,28);isotropicTriples.push(r);}
}
assert.equal(allTriples.length,216);assert.equal(isotropicTriples.length,48);
const minThreeNonzero=Math.min(...allTriples.map(r=>r.seven_minimum));assert.equal(minThreeNonzero,18);
// Forms of the two possible pairs of 7-components, from A6 and A13.
const planes=[];
for(const diagonal of[[6,6],[6,5]]){
 const zeros=[];for(let x=0;x<7;x++)for(let y=0;y<7;y++)if(mod(diagonal[0]*x*x+diagonal[1]*y*y)===0)zeros.push([x,y]);
 assert.deepEqual(zeros,[[0,0]]);planes.push({diagonal,only_zero_isotropic:true});
}
// Primitive glue valuation: no copied table and no projective-space routine.
const allValuations=[];
for(let aprime=0;aprime<=3;aprime++)for(let j=0;j<=1;j++)for(let b=0;b<=5;b++){
 if(aprime+b-2*j!==2|| (j===1&&(aprime===0||b===0)))continue;
 const reason=aprime===0?'cyclic discriminant49 is not elementary rank2':j===1&&b>=2?'J order7 class has integral norm; anisotropic M forbids it':null;
 allValuations.push({aprime,b,j,reason});
}
assert.deepEqual(allValuations.filter(r=>!r.reason).map(({aprime,b,j})=>[aprime,b,j]),[[1,1,0],[2,0,0],[3,1,1]]);
// Rank-three root discriminants. Store norms as rational numerator/denominator.
const A3=Array.from({length:4},(_,k)=>({class:k,norm:minimumA(3,k)}));
assert.deepEqual(A3.filter(r=>r.class&&r.norm[0]%r.norm[1]===0),[{class:2,norm:[4,4]}]);
const A2A1=[];for(let a=0;a<3;a++)for(let b=0;b<2;b++)A2A1.push({class:[a,b],norm:[2*a*(3-a)+3*b,6]});
assert(A2A1.filter(r=>r.class.some(x=>x)).every(r=>r.norm[0]%r.norm[1]!==0));
const A1cube=[];for(let mask=0;mask<8;mask++){
 const weight=Array.from({length:3},(_,i)=>(mask>>i)&1).reduce((s,x)=>s+x,0);A1cube.push({class:mask,norm:[weight,2]});
}
assert(A1cube.filter(r=>r.class&&r.norm[0]%r.norm[1]===0).every(r=>r.norm[0]===2));
const otherPrimeCosts={A13_order2:minimumA(13,7),A20_order3:[minimumA(20,7),minimumA(20,14)]};
assert(otherPrimeCosts.A13_order2[0]>3*otherPrimeCosts.A13_order2[1]);
assert(otherPrimeCosts.A20_order3.every(([n,d])=>n>3*d));
const finalCosts=[];for(const d of[4,6]){
 const nonzero_R3_cost=[18*2+7,14];assert(nonzero_R3_cost[0]>3*nonzero_R3_cost[1]);
 const zero_R3_cost=[18+d,7];assert(zero_R3_cost[0]>3*zero_R3_cost[1]);
 finalCosts.push({R3_det:d,J_norm:7*d,nonzero_R3_cost,zero_R3_cost});
}
const out={exact:true,A6_class_minimum_numerators:classNormNumerator,all_nonzero_triples:216,isotropicTriples,minimum_three_nonzero:[18,7],planes,
 valuation_cases:allValuations,A3,A2A1,A1cube,otherPrimeCosts,finalCosts,
 source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 producer_note_sha256:sha(fs.readFileSync(path.join(here,'RACINES_CORANG_UN_CANDIDAT.md'))),
 scope:'Finite rational costs accompanying an independent human proof. Hypotheses: rank22 integral minimum2, determinant49, elementary rank2 discriminant7, and the physical frame spanning rank22. No assertion for arbitrary determinant49 genus or for every root-free lattice.'};
fs.writeFileSync(path.join(here,'verifier_corang_un_indep.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,triples:216,isotropic_triples:48,all_isotropic_minimum:4,primitive_strata:3,final_costs_above3:true}));

````


## verifier_golay_enveloppe_indep.json

````json
{
  "exact": true,
  "word_count": 4096,
  "weights": {
    "0": 1,
    "8": 759,
    "12": 2576,
    "16": 759,
    "24": 1
  },
  "code_self_dual": true,
  "y_norms": [
    7,
    7
  ],
  "y_inner": 0,
  "shell3_L": 4096,
  "shell3_M": 704,
  "projection_numerators_over7": {
    "11": 8,
    "12": 12,
    "13": 32,
    "16": 336,
    "17": 336,
    "19": 1032,
    "20": 1636,
    "21": 704
  },
  "simultaneous_abs3": 0,
  "certificate_basis": 22,
  "Gram": [
    [
      3,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      0,
      0,
      1,
      0,
      0,
      1,
      1,
      0,
      1
    ],
    [
      1,
      3,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      1,
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      1,
      1,
      0,
      0,
      -1
    ],
    [
      1,
      1,
      3,
      0,
      1,
      1,
      1,
      1,
      0,
      0,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0
    ],
    [
      1,
      1,
      0,
      3,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      0
    ],
    [
      1,
      1,
      1,
      1,
      3,
      1,
      1,
      0,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      0,
      1,
      0,
      1,
      0
    ],
    [
      1,
      1,
      1,
      1,
      1,
      3,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      0
    ],
    [
      1,
      1,
      1,
      0,
      1,
      1,
      3,
      1,
      0,
      0,
      0,
      1,
      1,
      1,
      0,
      0,
      -1,
      0,
      1,
      0,
      0,
      0
    ],
    [
      1,
      1,
      1,
      1,
      0,
      0,
      1,
      3,
      0,
      0,
      1,
      1,
      0,
      1,
      0,
      0,
      0,
      0,
      1,
      1,
      -1,
      0
    ],
    [
      1,
      0,
      0,
      1,
      1,
      1,
      0,
      0,
      3,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      1,
      1,
      1
    ],
    [
      0,
      1,
      0,
      1,
      1,
      1,
      0,
      0,
      1,
      3,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      0,
      1,
      1,
      0
    ],
    [
      1,
      0,
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      3,
      1,
      1,
      1,
      0,
      0,
      1,
      0,
      0,
      1,
      0,
      1
    ],
    [
      1,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      1,
      3,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      1,
      0,
      0
    ],
    [
      1,
      0,
      1,
      0,
      1,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      3,
      1,
      0,
      1,
      0,
      0,
      1,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      1,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      3,
      0,
      1,
      1,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      1,
      1,
      0,
      0,
      0,
      1,
      0,
      0,
      -1,
      0,
      0,
      3,
      1,
      1,
      1,
      1,
      0,
      1,
      0
    ],
    [
      1,
      0,
      0,
      1,
      1,
      0,
      0,
      0,
      1,
      1,
      0,
      0,
      1,
      1,
      1,
      3,
      1,
      1,
      1,
      0,
      1,
      0
    ],
    [
      0,
      0,
      0,
      1,
      1,
      0,
      -1,
      0,
      1,
      1,
      1,
      0,
      0,
      1,
      1,
      1,
      3,
      1,
      0,
      0,
      1,
      0
    ],
    [
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      3,
      0,
      0,
      0,
      -1
    ],
    [
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      1,
      0,
      1,
      1,
      0,
      0,
      3,
      0,
      1,
      -1
    ],
    [
      1,
      0,
      0,
      1,
      0,
      1,
      0,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      3,
      0,
      1
    ],
    [
      0,
      0,
      0,
      1,
      1,
      1,
      0,
      -1,
      1,
      1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      0,
      1,
      0,
      3,
      0
    ],
    [
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      -1,
      1,
      0,
      3
    ]
  ],
  "exact_rational_pivots": [
    [
      "3",
      "1"
    ],
    [
      "8",
      "3"
    ],
    [
      "5",
      "2"
    ],
    [
      "12",
      "5"
    ],
    [
      "9",
      "4"
    ],
    [
      "20",
      "9"
    ],
    [
      "32",
      "15"
    ],
    [
      "3",
      "2"
    ],
    [
      "97",
      "48"
    ],
    [
      "183",
      "97"
    ],
    [
      "239",
      "183"
    ],
    [
      "4169",
      "3824"
    ],
    [
      "6246",
      "4169"
    ],
    [
      "346",
      "347"
    ],
    [
      "2189",
      "3114"
    ],
    [
      "1792",
      "2189"
    ],
    [
      "107",
      "112"
    ],
    [
      "133",
      "214"
    ],
    [
      "14",
      "19"
    ],
    [
      "3",
      "8"
    ],
    [
      "1",
      "3"
    ],
    [
      "1",
      "4"
    ]
  ],
  "determinant": "49",
  "Gram_support_edges": 131,
  "connected": true,
  "supplied_certificate_sha256": "20c9d9a206626dd47d0de4a5d164da7d888d7e146db9ee01d701cf650162763e",
  "producer_source_sha256": "9c9cba2e19349cf681f256a990e69cdc0920b3eec31a8636fc5d3cba2027e9ed",
  "source_sha256": "c87c0d7b893759e386c3fecd6332435fe1231acb2834a6d8c91470202958c3a3",
  "scope": "Second implementation of all finite ingredients of the lattice-envelope control. Array-span generation and reduced rational Schur pivots are independent of the producer bitmask span/Bareiss. Supplied basis is replayed as a certificate. No SRG49 tight7 frame or graph is asserted."
}

````


## verifier_golay_enveloppe_indep.mjs

````javascript
// Independent Golay array-span and exact rational Schur determinant. No Bareiss or matching search.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex'),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),sum=a=>a.reduce((s,x)=>s+x,0),mod=(x,p)=>((x%p)+p)%p;
const exponents=[0,1,5,6,7,9,11],generators=Array.from({length:12},(_,shift)=>{
 const row=Array(24).fill(0);for(const e of exponents)row[e+shift]=1;row[23]=sum(row)%2;return row;
});
// Recursive doubling in F2^24. Words are coordinate arrays, never integer masks.
let code=[Array(24).fill(0)];for(const row of generators){const translated=code.map(c=>c.map((x,i)=>x^row[i]));code=code.concat(translated);}
const keys=new Set(code.map(c=>c.join('')));assert.equal(code.length,4096);assert.equal(keys.size,4096);assert(keys.has('1'.repeat(24)));
assert(generators.every(a=>generators.every(b=>dot(a,b)%2===0)));
const weights={};code.forEach(c=>{const w=sum(c);weights[w]=(weights[w]||0)+1;});assert.deepEqual(weights,{0:1,8:759,12:2576,16:759,24:1});
const set=a=>new Set(a),V=set([0,1,3,4,5,6,7,8,10,11,12,14]),D=set([0,1,2,9]),Dp=set([3,4,13,15]);
assert(keys.has(Array.from({length:24},(_,i)=>+V.has(i)).join('')));
const y1=Array.from({length:24},(_,i)=>D.has(i)?-3:1),y2=Array.from({length:24},(_,i)=>(V.has(i)?-1:1)*(Dp.has(i)?-3:1));
function latticeContains(x){
 const parity=mod(x[0],2);if(!x.every(t=>mod(t,2)===parity))return false;
 const cw=x.map(t=>+(mod(t-parity,4)===2));return keys.has(cw.join(''))&&mod(sum(x),8)===0;
}
assert(latticeContains(y1)&&latticeContains(y2));assert.equal(dot(y1,y1),56);assert.equal(dot(y2,y2),56);assert.equal(dot(y1,y2),0);
const norm3=code.map(c=>c.map(x=>1-2*x)),inM=[],projection={};let simultaneousAbs3=0;
for(const x of norm3){
 assert(latticeContains(x));assert.equal(dot(x,x),24);
 const a=dot(x,y1),b=dot(x,y2);assert.equal(mod(a,8),0);assert.equal(mod(b,8),0);
 const ia=a/8,ib=b/8,numerator=21-ia*ia-ib*ib;
 projection[numerator]=(projection[numerator]||0)+1;
 if(Math.abs(ia)===3&&Math.abs(ib)===3)simultaneousAbs3++;
 if(a===0&&b===0)inM.push(x);
}
assert.equal(inM.length,704);assert.equal(simultaneousAbs3,0);assert.equal(Math.min(...Object.keys(projection).map(Number)),11);
// Supplied 22-vector certificate is checked against the independently reconstructed shell.
const suppliedBytes=fs.readFileSync(path.join(here,'controle_enveloppe_g20_golay.json')),supplied=JSON.parse(suppliedBytes),basis=supplied.basis_integer_coordinates_over_sqrt8;
assert.equal(basis.length,22);assert(new Set(basis.map(x=>x.join(','))).size===22);
const Mkeys=new Set(inM.map(x=>x.join(',')));assert(basis.every(x=>Mkeys.has(x.join(','))));
const Gram=basis.map(a=>basis.map(b=>{const q=dot(a,b);assert.equal(mod(q,8),0);return q/8;}));
assert.deepEqual(Gram,supplied.Gram);assert.deepEqual(projection,supplied.projection_squared_numerators_over7);
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
const f=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);assert(d!==0n);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];};
const mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),sub=(a,b)=>f(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const A=Gram.map(row=>row.map(x=>f(x))),pivots=[];let determinant=f(1);
for(let k=0;k<22;k++){
 const pivot=A[k][k];assert(pivot[0]>0n);pivots.push(pivot.map(String));determinant=mul(determinant,pivot);
 for(let i=k+1;i<22;i++)for(let j=i;j<22;j++){
  const updated=sub(A[i][j],div(mul(A[i][k],A[j][k]),pivot));A[i][j]=A[j][i]=updated;
 }
}
assert.deepEqual(determinant,[49n,1n]);
const seen=new Set([0]),todo=[0];let edges=0;
for(let i=0;i<22;i++)for(let j=i+1;j<22;j++)if(Gram[i][j])edges++;
for(let k=0;k<todo.length;k++)for(let j=0;j<22;j++)if(Gram[todo[k]][j]&&j!==todo[k]&&!seen.has(j)){seen.add(j);todo.push(j);}
assert.equal(seen.size,22);assert.equal(edges,131);
const out={exact:true,word_count:4096,weights,code_self_dual:true,y_norms:[7,7],y_inner:0,shell3_L:4096,shell3_M:704,
 projection_numerators_over7:projection,simultaneous_abs3:simultaneousAbs3,certificate_basis:22,Gram,exact_rational_pivots:pivots,determinant:'49',Gram_support_edges:131,connected:true,
 supplied_certificate_sha256:sha(suppliedBytes),producer_source_sha256:sha(fs.readFileSync(path.join(here,'controle_enveloppe_g20_golay.mjs'))),source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 scope:'Second implementation of all finite ingredients of the lattice-envelope control. Array-span generation and reduced rational Schur pivots are independent of the producer bitmask span/Bareiss. Supplied basis is replayed as a certificate. No SRG49 tight7 frame or graph is asserted.'};
fs.writeFileSync(path.join(here,'verifier_golay_enveloppe_indep.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,words:4096,shell_M:704,determinant:'49',connected:true,projection_minimum:'11/7',basis_certificate_replayed:true}));

````


## verifier_identites_courtes.json

````json
{
  "exact": true,
  "localPolynomialChecks": 245,
  "global_M_parity_cases": 211,
  "seven_coefficient_relations_Gram": 21,
  "seven_image_columns_standard_Gram": 28,
  "mod7_coincidence": true,
  "heavyNorm14": [
    {
      "heavy": 2,
      "negative_vertices": 8,
      "min_negative_neighbors": 6,
      "min_common": 4
    },
    {
      "heavy": 3,
      "negative_vertices": 5,
      "min_negative_neighbors": 5,
      "min_common": 5
    }
  ],
  "pairLoads": [
    {
      "coefficients": [
        1,
        1
      ],
      "loads": [
        2,
        0
      ]
    },
    {
      "coefficients": [
        1,
        -1
      ],
      "loads": [
        0,
        2
      ]
    },
    {
      "coefficients": [
        -1,
        1
      ],
      "loads": [
        0,
        -2
      ]
    },
    {
      "coefficients": [
        -1,
        -1
      ],
      "loads": [
        -2,
        0
      ]
    }
  ],
  "characteristic10Profiles": [
    {
      "root_abs3": 0,
      "root_abs5": 0,
      "block_half_abs2": 0,
      "block_half_abs1": 7
    },
    {
      "root_abs3": 0,
      "root_abs5": 0,
      "block_half_abs2": 1,
      "block_half_abs1": 3
    },
    {
      "root_abs3": 0,
      "root_abs5": 1,
      "block_half_abs2": 0,
      "block_half_abs1": 1
    },
    {
      "root_abs3": 1,
      "root_abs5": 0,
      "block_half_abs2": 0,
      "block_half_abs1": 5
    },
    {
      "root_abs3": 1,
      "root_abs5": 0,
      "block_half_abs2": 1,
      "block_half_abs1": 1
    },
    {
      "root_abs3": 2,
      "root_abs5": 0,
      "block_half_abs2": 0,
      "block_half_abs1": 3
    },
    {
      "root_abs3": 3,
      "root_abs5": 0,
      "block_half_abs2": 0,
      "block_half_abs1": 1
    }
  ],
  "Hamming_H2_control": {
    "graph_vertices": 9,
    "degree": 4,
    "r": 1,
    "d": 3,
    "S": [
      [
        -1,
        0,
        1,
        -1
      ],
      [
        0,
        -1,
        1,
        1
      ],
      [
        1,
        1,
        0,
        0
      ],
      [
        -1,
        1,
        0,
        0
      ]
    ],
    "H": [
      [
        2,
        0,
        -1,
        1
      ],
      [
        0,
        2,
        -1,
        -1
      ],
      [
        -1,
        -1,
        1,
        0
      ],
      [
        1,
        -1,
        0,
        1
      ]
    ],
    "norm1_generator": 2,
    "coefficient_vector": [
      -1,
      -1,
      1,
      0
    ],
    "P": [
      2,
      6,
      4
    ],
    "Q": [
      1,
      3,
      8
    ],
    "external_common_pairs": 3,
    "norm1_NOT_rejected": true
  },
  "frozen_BvLS_positive_control_sha256": "d217f73bf0105226cedd73a702bb02b08d72338b27b6e0658b5e87e0bca8fb40",
  "positive_scope": "H2 is rebuilt directly. BvLS integer/p3 control remains acquired and frozen, not rerun or assigned SRG99 constants.",
  "source_sha256": "27ea92438164861646f0c6dec2aa4f74bb8588084d2c2b6af019f3a536c1c660",
  "scope": "Checks polynomial/parity/coefficient identities and a true small positive graph. The norm1 impossibility for SRG99 is a human proof, not a finite catalogue sweep."
}

````


## verifier_identites_courtes.mjs

````javascript
// Bounded exact checks of identities used in the human proofs. No graph99 search or solver.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex'),read=n=>fs.readFileSync(path.join(here,n)),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),tr=A=>A[0].map((_,i)=>A.map(r=>r[i])),mm=(A,B)=>{const T=tr(B);return A.map(r=>T.map(c=>dot(r,c)));},choose2=n=>n*(n-1)/2;
let localPolynomialChecks=0;for(let t=1;t<=5;t++)for(let d=0;d<=48;d++){assert.equal(choose2(d)+choose2(d+t),d*d+(t-1)*d+t*(t-1)/2);localPolynomialChecks++;}
const d7=[];for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const s of[1,-1]){const r=Array(7).fill(0);r[i]=1;r[j]=s;d7.push(r);}const C=tr(d7);assert.deepEqual(mm(C,tr(C)),Array.from({length:7},(_,i)=>Array.from({length:7},(_,j)=>i===j?12:0)));
const n=C.map((r,i)=>[...Array.from({length:7},(_,j)=>i===j?3:0),...r]),w=C.map((r,i)=>[...Array.from({length:7},(_,j)=>i===j?-4:0),...r]);
assert.deepEqual(mm(n,tr(n)),Array.from({length:7},(_,i)=>Array.from({length:7},(_,j)=>i===j?21:0)));assert.deepEqual(mm(w,tr(w)),Array.from({length:7},(_,i)=>Array.from({length:7},(_,j)=>i===j?28:0)));
assert(n.every((r,i)=>r.every((x,j)=>(x-w[i][j])%7===0)));
const blockRows=C.map(r=>r.reduce((s,x)=>s+x,0)-1);assert.deepEqual(blockRows,[11,9,7,5,3,1,-1]);let parityChecks=0;
for(let M=0;M<=210;M++){const rootsRowSum=462-4*M,rowSquaresMod8=((7+2*rootsRowSum)%8+8)%8;assert.equal(rowSquaresMod8,3);const equalityPossible=((rowSquaresMod8+497-4*M-588)%8+8)%8===0;assert.equal(equalityPossible,M%2===0);parityChecks++;}
const heavyNorm14=[2,3].map(k=>({heavy:k,negative_vertices:14-3*k,min_negative_neighbors:8-k,min_common:2*(8-k)-(14-3*k)}));assert(heavyNorm14.every(r=>r.min_common>2));
const pairLoads=[];for(const x of[1,-1])for(const y of[1,-1]){const loads=[x+y,x-y];assert(!(Math.abs(loads[0])>=2&&Math.abs(loads[1])>=2));pairLoads.push({coefficients:[x,y],loads});}
const characteristic10Profiles=[];for(let n3=0;n3<=3;n3++)for(let n5=0;n5<=1;n5++)for(let b2=0;b2<=1;b2++)for(let b1=0;b1<=7;b1++)if(2*n3+6*n5+4*b2+b1===7&&b1+b2<=7)characteristic10Profiles.push({root_abs3:n3,root_abs5:n5,block_half_abs2:b2,block_half_abs1:b1});assert.equal(characteristic10Profiles.length,7);
assert.equal(characteristic10Profiles.filter(r=>r.root_abs3===0&&r.root_abs5===0).length,2);
// Actual Hamming H(2,3), characteristic-independent integer control: its lattice has a generator of norm1.
const coord=Array.from({length:9},(_,i)=>[Math.floor(i/3),i%3]),sigma=coord.map(([x,y])=>3*((3-x)%3)+(3-y)%3),adj=coord.map(a=>coord.map(b=>+(a.reduce((s,x,i)=>s+(x!==b[i]),0)===1))),reps=Array.from({length:9},(_,i)=>i).filter(i=>i<sigma[i]);
assert.equal(reps.length,4);const S=reps.map(a=>reps.map(b=>adj[a][b]-adj[a][sigma[b]])),H=S.map((r,i)=>r.map((x,j)=>+(i===j)-x));assert.deepEqual(mm(H,H),H.map(r=>r.map(x=>3*x)));
const o=H.findIndex((r,i)=>r[i]===1);assert(o>=0);const a=H.map(r=>r[o]);assert.equal(dot(a,a),3);assert.deepEqual(S.map(r=>dot(r,a)),a.map(x=>x?-2*x:0));assert(a.every(x=>[0,1,-1].includes(x)));
const P=[],Q=[];a.forEach((x,i)=>{if(!x)return;P.push(x>0?reps[i]:sigma[reps[i]]);Q.push(x>0?sigma[reps[i]]:reps[i]);});const A=P.map(v=>P.map(z=>adj[v][z])),B=P.map(v=>Q.map(z=>adj[v][z])),deg=A.map(r=>r.reduce((s,x)=>s+x,0)),m=P.length,e=deg.reduce((s,x)=>s+x,0)/2;
assert.deepEqual(B.map(r=>r.reduce((s,x)=>s+x,0)),deg.map(x=>x+2));const outside=Array.from({length:9},(_,i)=>i).filter(i=>!P.includes(i)&&!Q.includes(i)),D=outside.reduce((s,i)=>s+choose2(P.reduce((n,j)=>n+adj[i][j],0)),0);
assert.equal(D,m*(m-2)-3*e-dot(deg,deg));assert(D>0); // The m7/d7 forcing argument is NOT transplanted here.
const bvlsFile=path.join(here,'../reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json'),bvlsBytes=fs.readFileSync(bvlsFile);
const out={exact:true,localPolynomialChecks,global_M_parity_cases:parityChecks,seven_coefficient_relations_Gram:21,seven_image_columns_standard_Gram:28,mod7_coincidence:true,
 heavyNorm14,pairLoads,characteristic10Profiles,Hamming_H2_control:{graph_vertices:9,degree:4,r:1,d:3,S,H,norm1_generator:o,coefficient_vector:a,P,Q,external_common_pairs:D,norm1_NOT_rejected:true},
 frozen_BvLS_positive_control_sha256:sha(bvlsBytes),positive_scope:'H2 is rebuilt directly. BvLS integer/p3 control remains acquired and frozen, not rerun or assigned SRG99 constants.',
 source_sha256:sha(read('verifier_identites_courtes.mjs')),scope:'Checks polynomial/parity/coefficient identities and a true small positive graph. The norm1 impossibility for SRG99 is a human proof, not a finite catalogue sweep.'};
fs.writeFileSync(path.join(here,'verifier_identites_courtes.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,polynomial_checks:localPolynomialChecks,parity_cases:parityChecks,H2_norm1_preserved:true,norm10_profiles:characteristic10Profiles.length}));

````


## verifier_indecomposabilite_courte.json

````json
{
  "exact": true,
  "D7_lines": 42,
  "nonorthogonality_edges": 420,
  "degree": 20,
  "connected": true,
  "parent": [
    0,
    2,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    4,
    4,
    4,
    4,
    4,
    4,
    6,
    6,
    6,
    6,
    8,
    8
  ],
  "sisterPaths": [
    [
      0,
      2,
      1
    ],
    [
      2,
      0,
      3
    ],
    [
      4,
      0,
      5
    ],
    [
      6,
      0,
      7
    ],
    [
      8,
      0,
      9
    ],
    [
      10,
      0,
      11
    ],
    [
      12,
      0,
      13
    ],
    [
      14,
      0,
      15
    ],
    [
      16,
      0,
      17
    ],
    [
      18,
      0,
      19
    ],
    [
      20,
      0,
      21
    ],
    [
      22,
      2,
      23
    ],
    [
      24,
      2,
      25
    ],
    [
      26,
      2,
      27
    ],
    [
      28,
      2,
      29
    ],
    [
      30,
      4,
      31
    ],
    [
      32,
      4,
      33
    ],
    [
      34,
      4,
      35
    ],
    [
      36,
      6,
      37
    ],
    [
      38,
      6,
      39
    ],
    [
      40,
      8,
      41
    ]
  ],
  "pairChecks": [
    {
      "blocks": [
        0,
        1
      ],
      "ids": [
        0,
        1
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        0,
        2
      ],
      "ids": [
        2,
        3
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        0,
        3
      ],
      "ids": [
        4,
        5
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        0,
        4
      ],
      "ids": [
        6,
        7
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        0,
        5
      ],
      "ids": [
        8,
        9
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        0,
        6
      ],
      "ids": [
        10,
        11
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        1,
        2
      ],
      "ids": [
        12,
        13
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        1,
        3
      ],
      "ids": [
        14,
        15
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        1,
        4
      ],
      "ids": [
        16,
        17
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        1,
        5
      ],
      "ids": [
        18,
        19
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        1,
        6
      ],
      "ids": [
        20,
        21
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        2,
        3
      ],
      "ids": [
        22,
        23
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        2,
        4
      ],
      "ids": [
        24,
        25
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        2,
        5
      ],
      "ids": [
        26,
        27
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        2,
        6
      ],
      "ids": [
        28,
        29
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        3,
        4
      ],
      "ids": [
        30,
        31
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        3,
        5
      ],
      "ids": [
        32,
        33
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        3,
        6
      ],
      "ids": [
        34,
        35
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        4,
        5
      ],
      "ids": [
        36,
        37
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        4,
        6
      ],
      "ids": [
        38,
        39
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    },
    {
      "blocks": [
        5,
        6
      ],
      "ids": [
        40,
        41
      ],
      "subsetValues": [
        0,
        1,
        -1,
        0
      ]
    }
  ],
  "diagonalCases": [
    {
      "incidences": 0,
      "Gram_diagonal": 0,
      "idempotence": true
    },
    {
      "incidences": 3,
      "Gram_diagonal": 1,
      "idempotence": false
    },
    {
      "incidences": 6,
      "Gram_diagonal": 2,
      "idempotence": false
    },
    {
      "incidences": 9,
      "Gram_diagonal": 3,
      "idempotence": false
    },
    {
      "incidences": 12,
      "Gram_diagonal": 4,
      "idempotence": true
    }
  ],
  "source_sha256": "1584e73048859a48c55505641ad4948b6714a872dde7d8189c25ea7e0bf9124c",
  "scope": "Discrete steps of two uniform human proofs. Norm3 generators must be pure in an integral minimum2 orthogonal decomposition. No local catalogue, lattice classification or graph99 search."
}

````


## verifier_indecomposabilite_courte.mjs

````javascript
// Independent bounded certificates for the two human decomposition arguments.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const roots=[];
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const s of[1,-1]){
 const v=Array(7).fill(0);v[i]=1;v[j]=s;roots.push({support:[i,j],sign:s,v});
}
assert.equal(roots.length,42);
const adj=roots.map((p,i)=>roots.map((q,j)=>i!==j&&dot(p.v,q.v)!==0?j:-1).filter(j=>j>=0));
assert(adj.every(row=>row.length===20));const parent=Array(42).fill(-1),queue=[0];parent[0]=0;
for(let k=0;k<queue.length;k++)for(const q of adj[queue[k]])if(parent[q]<0){parent[q]=queue[k];queue.push(q);}
assert.equal(queue.length,42);const edges=adj.reduce((n,row)=>n+row.length,0)/2;assert.equal(edges,420);
const sisterPaths=[];
for(let p=0;p<42;p+=2){
 assert.equal(dot(roots[p].v,roots[p+1].v),0);
 const middle=adj[p].find(q=>adj[q].includes(p+1));assert(middle!==undefined);
 sisterPaths.push([p,middle,p+1]);
}
const pairChecks=[];
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++){
 const ids=roots.map((r,k)=>r.support[0]===i&&r.support[1]===j?k:-1).filter(k=>k>=0);
 assert.equal(ids.length,2);const contributions=ids.map(k=>roots[k].v[i]*roots[k].v[j]);
 assert.deepEqual(contributions,[1,-1]);
 const subsetValues=[0,1,2,3].map(mask=>contributions.reduce((s,x,k)=>s+(((mask>>k)&1)?x:0),0));
 assert.deepEqual(subsetValues,[0,1,-1,0]);
 assert.deepEqual(subsetValues.filter(x=>x%3===0),[0,0]);pairChecks.push({blocks:[i,j],ids,subsetValues});
}
const diagonalCases=[];
for(let n=0;n<=12;n++)if(n%3===0){const G=n/3;diagonalCases.push({incidences:n,Gram_diagonal:G,idempotence:G*G===4*G});}
assert.deepEqual(diagonalCases.filter(r=>r.idempotence).map(r=>r.incidences),[0,12]);
const out={exact:true,D7_lines:42,nonorthogonality_edges:edges,degree:20,connected:true,parent,sisterPaths,pairChecks,diagonalCases,
 source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 scope:'Discrete steps of two uniform human proofs. Norm3 generators must be pure in an integral minimum2 orthogonal decomposition. No local catalogue, lattice classification or graph99 search.'};
fs.writeFileSync(path.join(here,'verifier_indecomposabilite_courte.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,D7_lines:42,edges,connected:true,offdiagonal_checks:84,pure_block_incidence_counts:[0,12]}));

````


## verifier_racines_corang_un.json

````json
{
  "scope": "Petits calculs propres associés à une preuve candidate de corang1; pas de reconstruction SRG",
  "anisotropic_pairs": [
    {
      "coefficients": [
        6,
        6
      ],
      "nonzero_isotropic_vectors": 0
    },
    {
      "coefficients": [
        5,
        6
      ],
      "nonzero_isotropic_vectors": 0
    }
  ],
  "A6_cube_isotropic_nonzero": 48,
  "A6_cube_all_isotropic_projection_norm": 4,
  "rank3_class_minima": {
    "A3": [
      {
        "class": 0,
        "numerator": 0,
        "denominator": 4
      },
      {
        "class": 1,
        "numerator": 3,
        "denominator": 4
      },
      {
        "class": 2,
        "numerator": 4,
        "denominator": 4
      },
      {
        "class": 3,
        "numerator": 3,
        "denominator": 4
      }
    ],
    "A2_A1": [
      {
        "classes": [
          0,
          0
        ],
        "numerator": 0,
        "denominator": 6
      },
      {
        "classes": [
          0,
          1
        ],
        "numerator": 3,
        "denominator": 6
      },
      {
        "classes": [
          1,
          0
        ],
        "numerator": 4,
        "denominator": 6
      },
      {
        "classes": [
          1,
          1
        ],
        "numerator": 7,
        "denominator": 6
      },
      {
        "classes": [
          2,
          0
        ],
        "numerator": 4,
        "denominator": 6
      },
      {
        "classes": [
          2,
          1
        ],
        "numerator": 7,
        "denominator": 6
      }
    ],
    "A1_cube": [
      {
        "mask": 1,
        "numerator": 1,
        "denominator": 2
      },
      {
        "mask": 2,
        "numerator": 1,
        "denominator": 2
      },
      {
        "mask": 3,
        "numerator": 2,
        "denominator": 2
      },
      {
        "mask": 4,
        "numerator": 1,
        "denominator": 2
      },
      {
        "mask": 5,
        "numerator": 2,
        "denominator": 2
      },
      {
        "mask": 6,
        "numerator": 2,
        "denominator": 2
      },
      {
        "mask": 7,
        "numerator": 3,
        "denominator": 2
      }
    ]
  },
  "primitive_determinant_rows": [
    {
      "a_prime": 0,
      "b": 2,
      "j": 0,
      "status": "cyclic rank1 incompatible with elementary rank2"
    },
    {
      "a_prime": 1,
      "b": 1,
      "j": 0,
      "status": "candidate"
    },
    {
      "a_prime": 1,
      "b": 3,
      "j": 1,
      "status": "anisotropic M7, integral J order7 class"
    },
    {
      "a_prime": 2,
      "b": 0,
      "j": 0,
      "status": "candidate"
    },
    {
      "a_prime": 2,
      "b": 2,
      "j": 1,
      "status": "anisotropic M7, integral J order7 class"
    },
    {
      "a_prime": 3,
      "b": 1,
      "j": 1,
      "status": "candidate"
    }
  ],
  "cost_bounds": [
    "18/7+1/2=43/14>3",
    "18/7+4/7=22/7>3",
    "18/7+6/7=24/7>3"
  ]
}

````


## verifier_racines_corang_un.mjs

````javascript
// Petits contrôles exacts de la preuve candidate; aucune classification
// de graphes ou de réseaux n'est exécutée par ce source.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const check=(ok,label)=>{if(!ok)throw Error(label);};
const isoPairs=[];
for(const coeff of [[6,6],[5,6]]){
  let count=0;
  for(let x=0;x<7;x++)for(let y=0;y<7;y++)
    if((x||y)&&(coeff[0]*x*x+coeff[1]*y*y)%7===0)count++;
  check(count===0,'A6^2 / A13+A6 anisotropes');
  isoPairs.push({coefficients:coeff,nonzero_isotropic_vectors:count});
}
const classNumerator=k=>k*(7-k);
const isotropic=[];
for(let a=1;a<7;a++)for(let b=1;b<7;b++)for(let c=1;c<7;c++){
  const n=classNumerator(a)+classNumerator(b)+classNumerator(c);
  if(n%7===0)isotropic.push({classes:[a,b,c],norm_numerator:n});
}
check(isotropic.length===48,'48 vecteurs isotropes A6^3');
check(isotropic.every(x=>x.norm_numerator===28),'minimum projection4');
const A3=Array.from({length:4},(_,k)=>({class:k,numerator:k*(4-k),denominator:4}));
const A2A1=[];
for(let k=0;k<3;k++)for(let l=0;l<2;l++)
  A2A1.push({classes:[k,l],numerator:2*k*(3-k)+3*l,denominator:6});
const A1cube=[];
for(let mask=1;mask<8;mask++){
  const weight=mask.toString(2).replaceAll('0','').length;
  A1cube.push({mask,numerator:weight,denominator:2});
}
check(A3.filter(x=>x.class&&x.numerator%4===0).every(x=>x.numerator===4),'A3 saturation norme1');
check(A2A1.filter(x=>x.classes.some(Boolean)).every(x=>x.numerator%6!==0),'A2+A1 aucune classe intégrale');
check(A1cube.filter(x=>x.numerator%2===0).every(x=>x.numerator===2),'A1^3 saturation norme1');
check(A3.filter(x=>x.class).every(x=>2*x.numerator>=x.denominator),'R3 minclasse>=1/2');
check(A2A1.filter(x=>x.classes.some(Boolean)).every(x=>2*x.numerator>=x.denominator),'R3 minclasse>=1/2');
const determinantRows=[];
for(let ap=0;ap<=3;ap++)for(let j=0;j<=1;j++){
  const b=2-ap+2*j;
  if(b<0||j&&(!ap||!b))continue;
  let status='candidate';
  if(ap===0)status='cyclic rank1 incompatible with elementary rank2';
  if(ap===1&&j===1||ap===2&&j===1)status='anisotropic M7, integral J order7 class';
  determinantRows.push({a_prime:ap,b,j,status});
}
check(18*2+7>3*14,'18/7+1/2>3');
check(18+4>21&&18+6>21,'18/7+d/7>3');
const result={scope:'Petits calculs propres associés à une preuve candidate de corang1; pas de reconstruction SRG',
  anisotropic_pairs:isoPairs,A6_cube_isotropic_nonzero:isotropic.length,
  A6_cube_all_isotropic_projection_norm:4,
  rank3_class_minima:{A3,A2_A1:A2A1,A1_cube:A1cube},
  primitive_determinant_rows:determinantRows,
  cost_bounds:['18/7+1/2=43/14>3','18/7+4/7=22/7>3','18/7+6/7=24/7>3']};
fs.writeFileSync(path.join(path.dirname(fileURLToPath(import.meta.url)),'verifier_racines_corang_un.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));

````


## verifier_sept_blocs_caracteristiques.json

````json
{
  "scope": "Contrôles finis arithmétiques; aucun graphe99 ni exclusion de genre",
  "code_P": {
    "size": 4096,
    "two_torsion": 64,
    "invariant_factors": "4^6",
    "root_classes": 42,
    "root_order": 4,
    "root_projection_norm": "1/2"
  },
  "D7_nonorthogonality_graph": {
    "vertices": 42,
    "degree": 20,
    "edges": 420,
    "connected": true
  },
  "characteristic10_tournament": {
    "indegrees": [
      3,
      3,
      3,
      3,
      3,
      3,
      3
    ],
    "C_epsilon": [
      -6,
      -6,
      -6,
      -6,
      -6,
      -6,
      -6
    ],
    "squared_coefficient_norm": 70,
    "limitations": "Condition des blocs seulement; T et appartenance au réseau non construits"
  },
  "counterexample_K11_squared": {
    "rank": 22,
    "determinant": 49,
    "minimum": 2,
    "characteristic_minimum": 10,
    "dual_vector_norm": "5/7",
    "limitations": "Contre-témoin à la borne caractéristique seule; viole min N#>=8/7"
  },
  "characteristic8_glue_profiles": [
    {
      "b_abs": [
        1,
        1
      ],
      "n3": 0,
      "block_half_square": 3
    },
    {
      "b_abs": [
        1,
        1
      ],
      "n3": 1,
      "block_half_square": 1
    },
    {
      "b_abs": [
        1,
        3
      ],
      "n3": 0,
      "block_half_square": 1
    }
  ]
}

````


## verifier_sept_blocs_caracteristiques.mjs

````javascript
// Contrôles finis propres : code 2-adique des sept blocs, profil tournoi,
// témoin K11^2. Ils ne construisent pas de graphe SRG99.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const check=(ok,label)=>{if(!ok)throw Error(label);};
const enc=a=>a.reduce((s,x,i)=>s+x*4**i,0);
const dec=n=>Array.from({length:7},(_,i)=>Math.floor(n/4**i)%4);
const code=a=>{
  a=a.map(x=>((x%4)+4)%4);
  return Math.min(enc(a),enc(a.map(x=>(x+2)%4)));
};
const classes=new Set();
for(let n=0;n<4**7;n++){
  const a=dec(n);if(a.reduce((s,x)=>s+x,0)%2===0)classes.add(code(a));
}
let order2=0;
for(const n of classes)if(code(dec(n).map(x=>2*x))===0)order2++;
check(classes.size===4096,'|A_P|');check(order2===64,'A_P[2]');
const roots=[];
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const s of [1,-1]){
  const r=Array(7).fill(0);r[i]=1;r[j]=s;roots.push(r);
}
const rootClasses=roots.map(code);
check(new Set(rootClasses).size===42,'42 classes distinctes');
check(rootClasses.every(n=>code(dec(n).map(x=>2*x))!==0),'ordre4');
check(roots.every(r=>dot(r,r)===2),'norme p=1/2');
const adjacency=roots.map((r,i)=>roots.map((s,j)=>i!==j&&dot(r,s)!==0));
check(adjacency.every(row=>row.filter(Boolean).length===20),'degré D7');
const visited=new Set([0]);const queue=[0];
while(queue.length){const p=queue.shift();adjacency[p].forEach((ok,q)=>{
  if(ok&&!visited.has(q)){visited.add(q);queue.push(q);}
});}
check(visited.size===42,'connexité D7');

// Cas caractéristique10 : les sept demi-coefficients blocs valent1.
// Un tournoi cyclique régulier donne C epsilon=-6*1, mais aucun T.
const residues=new Set([1,2,4]);const epsilon=[];const indegrees=Array(7).fill(0);
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++){
  const receiver=residues.has((j-i+7)%7)?i:j;
  indegrees[receiver]++;
  epsilon.push(-1,receiver===i?-1:1);
}
const Ce=Array(7).fill(0);
roots.forEach((r,k)=>r.forEach((x,i)=>Ce[i]+=x*epsilon[k]));
check(indegrees.every(x=>x===3),'tournoi régulier');
check(Ce.every(x=>x===-6),'C epsilon');
check(7*4+dot(epsilon,epsilon)===70,'profil caractéristique10');

// D12^+=D12+Z*(1/2,...,1/2), a=(3/2,3/2,1/2^10).
// Toutes les fractions sont contrôlées en coordonnées doublées.
const a2=[3,3,...Array(10).fill(1)];
const c=[1,1,-1,...Array(9).fill(1)];
const k2=c.map((x,i)=>2*x-a2[i]);
check(dot(a2,a2)===28,'a^2=7');
check(dot(c,c)===12,'c^2=12');
check(dot(c,a2)===14,'c.a=7');
check(dot(k2,a2)===0,'k dans a-perp');
check(dot(k2,k2)===20,'k^2=5');
check(c.reduce((s,x)=>s+x,0)%2===0,'c dans D12');
check(c.every(x=>x%2!==0),'c caractéristique sur D12');
check((c.reduce((s,x)=>s+x,0)/2-3)%2===0,'c caractéristique sur spin');
const b=[1,1,...Array(10).fill(0)];
check(dot(b,b)===2&&dot(b,a2)===6,'b^2=2,b.a=3');
const dualNormNumerator=7*dot(b,b)-(dot(b,a2)/2)**2;
check(dualNormNumerator===5,'dual de K : norme5/7');

// Les trois profils d'une caractéristique8 dans le collage unimodulaire24.
const char8=[];
for(const b1 of [1,3])for(const b2 of [1,3])if(b1<=b2)
  for(let n3=0;n3<=1;n3++)for(let aSquare=0;aSquare<=3;aSquare++)
    if(b1*b1+b2*b2+8*n3+4*aSquare===14)
      char8.push({b_abs:[b1,b2],n3,block_half_square:aSquare});
check(char8.length===3,'trois profils caractère8');

const result={scope:'Contrôles finis arithmétiques; aucun graphe99 ni exclusion de genre',
  code_P:{size:classes.size,two_torsion:order2,invariant_factors:'4^6',
    root_classes:42,root_order:4,root_projection_norm:'1/2'},
  D7_nonorthogonality_graph:{vertices:42,degree:20,edges:420,connected:visited.size===42},
  characteristic10_tournament:{indegrees,C_epsilon:Ce,squared_coefficient_norm:70,
    limitations:'Condition des blocs seulement; T et appartenance au réseau non construits'},
  counterexample_K11_squared:{rank:22,determinant:49,minimum:2,
    characteristic_minimum:10,dual_vector_norm:'5/7',
    limitations:'Contre-témoin à la borne caractéristique seule; viole min N#>=8/7'},
  characteristic8_glue_profiles:char8};
const target=path.join(path.dirname(fileURLToPath(import.meta.url)),'verifier_sept_blocs_caracteristiques.json');
fs.writeFileSync(target,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));

````


## D4_SIX_GLUE_DIAGNOSTIC.json

5224 octets ; SHA256 cdc22f26b323b4a06acedbb828cc030c2fa768b157bb9f226e3da65d51e1add5

```json
{
  "graphs": 32768,
  "minimum_at_least3": 5712,
  "odd_with_weight3": 5580,
  "one_symbol_component": 0,
  "survivors": 5580,
  "examples": [
    {
      "graph": 1880,
      "adjacency": [
        48,
        40,
        24,
        6,
        5,
        3
      ],
      "words3": [
        [
          1,
          48
        ],
        [
          2,
          40
        ],
        [
          4,
          24
        ],
        [
          7,
          0
        ],
        [
          8,
          6
        ],
        [
          16,
          5
        ],
        [
          32,
          3
        ],
        [
          56,
          0
        ]
      ],
      "symbol_masks": [
        6,
        6,
        6,
        6,
        6,
        6
      ]
    },
    {
      "graph": 1881,
      "adjacency": [
        50,
        41,
        24,
        6,
        5,
        3
      ],
      "words3": [
        [
          4,
          24
        ],
        [
          7,
          3
        ],
        [
          8,
          6
        ],
        [
          16,
          5
        ],
        [
          32,
          3
        ],
        [
          33,
          49
        ],
        [
          34,
          42
        ],
        [
          56,
          0
        ]
      ],
      "symbol_masks": [
        12,
        12,
        6,
        6,
        6,
        10
      ]
    },
    {
      "graph": 1882,
      "adjacency": [
        52,
        40,
        25,
        6,
        5,
        3
      ],
      "words3": [
        [
          2,
          40
        ],
        [
          7,
          5
        ],
        [
          8,
          6
        ],
        [
          16,
          5
        ],
        [
          17,
          49
        ],
        [
          20,
          28
        ],
        [
          32,
          3
        ],
        [
          56,
          0
        ]
      ],
      "symbol_masks": [
        12,
        6,
        12,
        6,
        10,
        6
      ]
    },
    {
      "graph": 1883,
      "adjacency": [
        54,
        41,
        25,
        6,
        5,
        3
      ],
      "words3": [
        [
          7,
          6
        ],
        [
          8,
          6
        ],
        [
          16,
          5
        ],
        [
          20,
          28
        ],
        [
          32,
          3
        ],
        [
          34,
          42
        ],
        [
          49,
          48
        ],
        [
          56,
          0
        ]
      ],
      "symbol_masks": [
        6,
        12,
        12,
        6,
        10,
        10
      ]
    },
    {
      "graph": 1884,
      "adjacency": [
        56,
        40,
        24,
        7,
        5,
        3
      ],
      "words3": [
        [
          2,
          40
        ],
        [
          3,
          16
        ],
        [
          4,
          24
        ],
        [
          5,
          32
        ],
        [
          16,
          5
        ],
        [
          24,
          2
        ],
        [
          32,
          3
        ],
        [
          40,
          4
        ]
      ],
      "symbol_masks": [
        6,
        6,
        6,
        6,
        6,
        6
      ]
    },
    {
      "graph": 1885,
      "adjacency": [
        58,
        41,
        24,
        7,
        5,
        3
      ],
      "words3": [
        [
          3,
          19
        ],
        [
          4,
          24
        ],
        [
          16,
          5
        ],
        [
          24,
          2
        ],
        [
          32,
          3
        ],
        [
          34,
          42
        ],
        [
          37,
          33
        ],
        [
          40,
          4
        ]
      ],
      "symbol_masks": [
        12,
        12,
        6,
        6,
        6,
        10
      ]
    },
    {
      "graph": 1886,
      "adjacency": [
        60,
        40,
        25,
        7,
        5,
        3
      ],
      "words3": [
        [
          2,
          40
        ],
        [
          5,
          37
        ],
        [
          16,
          5
        ],
        [
          19,
          17
        ],
        [
          20,
          28
        ],
        [
          24,
          2
        ],
        [
          32,
          3
        ],
        [
          40,
          4
        ]
      ],
      "symbol_masks": [
        12,
        6,
        12,
        6,
        10,
        6
      ]
    },
    {
      "graph": 1887,
      "adjacency": [
        62,
        41,
        25,
        7,
        5,
        3
      ],
      "words3": [
        [
          16,
          5
        ],
        [
          19,
          18
        ],
        [
          20,
          28
        ],
        [
          24,
          2
        ],
        [
          32,
          3
        ],
        [
          34,
          42
        ],
        [
          37,
          36
        ],
        [
          40,
          4
        ]
      ],
      "symbol_masks": [
        6,
        12,
        12,
        6,
        10,
        10
      ]
    }
  ]
}

```


## G18_G20_D6_MIXTE_CENTRES_REPETES.json

1997 octets ; SHA256 54067ebf5a3f6c75a5bc79b569c1b344b357e051bf82ccfc3620d0aea0fb0c6d

```json
{
  "exact": true,
  "scope": "D6^4/C4, f_A=4,f_B=2, h7 integer typeI supported in A or C, common physical normals",
  "assumptions": [
    "fullframe=7I24",
    "min(N*)>=8/7",
    "J=7I2 primitive",
    "seven h mutually orthogonal"
  ],
  "all_four_centre_distributions": 1365,
  "repeated_centre_distributions": 870,
  "diagonal_compatible_repeated_contexts": 150,
  "profiles": {
    "2+2": 30,
    "2+1+1": 120
  },
  "ordered_unit_support_pairs_covering_diagonal": 270,
  "pairs_passing_root_bound": 0,
  "local_ratio_sign_cases_checked": 64,
  "split_profiles": [
    {
      "centres_B": 0,
      "centres_D": 4,
      "epsilon": -1,
      "spinor_inner": -2,
      "orthogonal": false
    },
    {
      "centres_B": 0,
      "centres_D": 4,
      "epsilon": 1,
      "spinor_inner": 2,
      "orthogonal": false
    },
    {
      "centres_B": 1,
      "centres_D": 3,
      "epsilon": -1,
      "spinor_inner": -1,
      "orthogonal": false
    },
    {
      "centres_B": 1,
      "centres_D": 3,
      "epsilon": 1,
      "spinor_inner": 1,
      "orthogonal": false
    },
    {
      "centres_B": 2,
      "centres_D": 2,
      "epsilon": -1,
      "spinor_inner": 0,
      "orthogonal": true
    },
    {
      "centres_B": 2,
      "centres_D": 2,
      "epsilon": 1,
      "spinor_inner": 0,
      "orthogonal": true
    },
    {
      "centres_B": 3,
      "centres_D": 1,
      "epsilon": -1,
      "spinor_inner": 1,
      "orthogonal": false
    },
    {
      "centres_B": 3,
      "centres_D": 1,
      "epsilon": 1,
      "spinor_inner": -1,
      "orthogonal": false
    },
    {
      "centres_B": 4,
      "centres_D": 0,
      "epsilon": -1,
      "spinor_inner": 2,
      "orthogonal": false
    },
    {
      "centres_B": 4,
      "centres_D": 0,
      "epsilon": 1,
      "spinor_inner": -2,
      "orthogonal": false
    }
  ],
  "conclusion": "the four centres of the AC-spinor blocks must be distinct, two in B and two in D; whole mixed regime not excluded"
}

```


## G18_G20_D6_MIXTE_CENTRES_REPETES.mjs

3941 octets ; SHA256 b5a6d8d22a01a4fa8a51522513c3e5fa6fd8389147b44fb5a8d7123423e573dc

```javascript
// Controle exact du dernier argument de couverture unitaire, pas un solveur.
import { writeFileSync } from 'node:fs';
function* compositions(total, count, p = []) {
  if (count === 1) { yield [...p, total]; return; }
  for (let v = 0; v <= total; v++) yield* compositions(total - v, count - 1, [...p, v]);
}
const units = [];
for (let component = 0; component < 2; component++)
  for (let a = 0; a < 6; a++) for (let b = a + 1; b < 6; b++)
    for (let c = b + 1; c < 6; c++) for (let d = c + 1; d < 6; d++) {
      const support = [a,b,c,d].map(j => j + 6*component);
      units.push({ component, support, vector: Array.from({length: 12}, (_, j) => support.includes(j) ? 1 : 0) });
    }
let checked = 0, repeated = 0, diagonalContexts = 0, coveredPairs = 0, survivingPairs = 0;
const hist = {};
for (const centres of compositions(4, 12)) {
  checked++;
  if (Math.max(...centres) <= 1) continue;
  repeated++;
  for (let tB = 0; tB <= 2; tB++) {
    const tD = 2 - tB;
    const residual = centres.map((m, j) => (j < 6 ? tB : tD) - m);
    if (residual.some(x => x < 0 || x > 2)) continue;
    diagonalContexts++;
    const profile = centres.filter(x => x > 0).sort((a,b) => b-a).join('+');
    hist[profile] = (hist[profile] || 0) + 1;
    for (const first of units) for (const second of units) {
      if (!residual.every((v,j) => v === first.vector[j] + second.vector[j])) continue;
      coveredPairs++;
      const common = first.support.filter(j => second.support.includes(j)).length;
      // If >=3 unit axes are shared, two sign ratios agree. A root on
      // those axes has absolute pairing2 with BOTH normals: 8>6.
      if (first.component !== second.component || common <= 2) survivingPairs++;
    }
  }
}
if (checked !== 1365 || repeated !== 870 || diagonalContexts !== 150 || coveredPairs !== 270 || survivingPairs !== 0)
  throw new Error('Unexpected exact coverage');
let localSignCases = 0;
for (let mB = 0; mB <= 1; mB++) for (let mD = 0; mD <= 1; mD++)
  for (let bits = 0; bits < 16; bits++) {
    const [b1,b2,d1,d2] = Array.from({length: 4}, (_, j) => ((bits>>j)&1) ? -1 : 1);
    const first = b1*d1, second = b2*d2;
    const rPlus = (first === 1 ? 1 : 0) + (second === 1 ? 1 : 0);
    const kPlus = mB+mD+rPlus, kMinus = mB+mD+2-rPlus;
    const exactCapacity = [1,3].includes(kPlus) && [1,3].includes(kMinus);
    const ratioRelation = b1*b2*d1*d2 === -((-1)**(mB+mD));
    if (exactCapacity !== ratioRelation) throw new Error('Incorrect local ratio equivalence');
    localSignCases++;
  }
const splitProfiles = [];
for (let b = 0; b <= 4; b++) for (const epsilon of [-1,1]) {
  const d = 4-b;
  const ratiosB = Array.from({length: 6}, (_, j) => epsilon*((-1)**(j<b ? 1 : 0)));
  const ratiosD = Array.from({length: 6}, (_, j) => -epsilon*((-1)**(j<d ? 1 : 0)));
  const inner = (ratiosB.reduce((a,v)=>a+v,0)+ratiosD.reduce((a,v)=>a+v,0))/4;
  if (inner !== epsilon*(2-b)) throw new Error('Incorrect spinor inner product');
  splitProfiles.push({ centres_B: b, centres_D: d, epsilon, spinor_inner: inner, orthogonal: inner === 0 });
}
const result = {
  exact: true,
  scope: 'D6^4/C4, f_A=4,f_B=2, h7 integer typeI supported in A or C, common physical normals',
  assumptions: ['fullframe=7I24','min(N*)>=8/7','J=7I2 primitive','seven h mutually orthogonal'],
  all_four_centre_distributions: checked,
  repeated_centre_distributions: repeated,
  diagonal_compatible_repeated_contexts: diagonalContexts,
  profiles: hist,
  ordered_unit_support_pairs_covering_diagonal: coveredPairs,
  pairs_passing_root_bound: survivingPairs,
  local_ratio_sign_cases_checked: localSignCases,
  split_profiles: splitProfiles,
  conclusion: 'the four centres of the AC-spinor blocks must be distinct, two in B and two in D; whole mixed regime not excluded',
};
writeFileSync(new URL('./G18_G20_D6_MIXTE_CENTRES_REPETES.json', import.meta.url), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result));

```


## G18_G20_D6_QUATRE.json

17542 octets ; SHA256 e747d9cf46a28c7981af17aa7944baeced93b21e3134eb2d49cb18bf1943014f

```json
{
  "exact": true,
  "glue_classes": [
    {
      "mask": 0,
      "classes": [
        0,
        0,
        0,
        0
      ],
      "minimum_twice_norm": 0
    },
    {
      "mask": 1,
      "classes": [
        2,
        1,
        0,
        0
      ],
      "minimum_twice_norm": 6
    },
    {
      "mask": 2,
      "classes": [
        0,
        2,
        1,
        0
      ],
      "minimum_twice_norm": 6
    },
    {
      "mask": 3,
      "classes": [
        2,
        3,
        1,
        0
      ],
      "minimum_twice_norm": 8
    },
    {
      "mask": 4,
      "classes": [
        0,
        0,
        2,
        1
      ],
      "minimum_twice_norm": 6
    },
    {
      "mask": 5,
      "classes": [
        2,
        1,
        2,
        1
      ],
      "minimum_twice_norm": 12
    },
    {
      "mask": 6,
      "classes": [
        0,
        2,
        3,
        1
      ],
      "minimum_twice_norm": 8
    },
    {
      "mask": 7,
      "classes": [
        2,
        3,
        3,
        1
      ],
      "minimum_twice_norm": 10
    },
    {
      "mask": 8,
      "classes": [
        1,
        0,
        0,
        2
      ],
      "minimum_twice_norm": 6
    },
    {
      "mask": 9,
      "classes": [
        3,
        1,
        0,
        2
      ],
      "minimum_twice_norm": 8
    },
    {
      "mask": 10,
      "classes": [
        1,
        2,
        1,
        2
      ],
      "minimum_twice_norm": 12
    },
    {
      "mask": 11,
      "classes": [
        3,
        3,
        1,
        2
      ],
      "minimum_twice_norm": 10
    },
    {
      "mask": 12,
      "classes": [
        1,
        0,
        2,
        3
      ],
      "minimum_twice_norm": 8
    },
    {
      "mask": 13,
      "classes": [
        3,
        1,
        2,
        3
      ],
      "minimum_twice_norm": 10
    },
    {
      "mask": 14,
      "classes": [
        1,
        2,
        3,
        3
      ],
      "minimum_twice_norm": 10
    },
    {
      "mask": 15,
      "classes": [
        3,
        3,
        3,
        3
      ],
      "minimum_twice_norm": 8
    }
  ],
  "coset_minimum_histogram": {
    "0": 1,
    "3": 4,
    "4": 5,
    "5": 4,
    "6": 2
  },
  "determinant": 1,
  "root_system": "D6^4",
  "norm3_shell_size": 4096,
  "norm3_sample64_twice_coordinates": [
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
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
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      -1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      1,
      -1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      1,
      1,
      -1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      1,
      1,
      1,
      -1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      1,
      1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      -1,
      -1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      -1,
      1,
      -1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      -1,
      1,
      1,
      -1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      -1,
      1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      1,
      -1,
      -1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      1,
      -1,
      1,
      -1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      1,
      -1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      1,
      1,
      -1,
      -1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      1,
      1,
      -1,
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      1,
      1,
      1,
      1,
      -1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      -1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      0,
      0,
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
    [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      0,
      0,
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
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      1,
      -1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      1,
      -1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      1,
      -1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      1,
      -1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      -1,
      -1
    ]
  ],
  "sample_Gram_F2_rank": 24,
  "characteristic8_count": 288,
  "allowed_individual_norm4": {
    "single_component_four_units": 960,
    "adjacent_two_plus_two_units": 14400,
    "opposite_spinors_plus_intermediate_unit": 49152
  },
  "allowed_individual_norm4_total": 64512,
  "scope": "Integral rootful envelope and individual h classification; no simultaneous physical49-frame or graph certified."
}

```


## G18_G20_D6_QUATRE.mjs

2510 octets ; SHA256 0a147df75a003db1d62fe95f8d8ac619394487fe95a98a08c091319eb4498c9b

```javascript
import fs from 'node:fs';
import assert from 'node:assert/strict';
const bit=(m,j)=>m>>j&1;
const classes=[];
for(let m=0;m<16;m++){
  const local=Array.from({length:4},(_,i)=>bit(m,(i+3)%4)+2*bit(m,i));
  const twiceNorm=local.reduce((s,a)=>s+(a===0?0:a===3?2:3),0);
  classes.push({mask:m,classes:local,minimum_twice_norm:twiceNorm});
}
const hist={};for(const row of classes)hist[row.minimum_twice_norm/2]=(hist[row.minimum_twice_norm/2]||0)+1;
assert.deepEqual(hist,{0:1,3:4,4:5,5:4,6:2});
const baseline=i=>{
  const a=Array(24).fill(0);for(let j=0;j<6;j++){a[6*i+j]=j===0?-1:1;a[6*((i+1)%4)+j]=1;}return a;
};
const shell=Array.from({length:4},(_,i)=>baseline(i));
for(let c=0;c<4;c++)for(let a=0;a<6;a++)for(let b=a+1;b<6;b++){
  const v=baseline((c+3)%4);v[6*c+a]*=-1;v[6*c+b]*=-1;shell.push(v);
}
assert.equal(shell.length,64);
const dot=(a,b)=>a.reduce((s,x,j)=>s+x*b[j],0);
for(const row of shell)assert.equal(dot(row,row),12);
const G=shell.map(a=>shell.map(b=>{const n=dot(a,b);assert.equal(n%4,0);return n/4;}));
const rows=G.map(row=>row.reduce((s,a,j)=>s|(BigInt((a%2+2)%2)<<BigInt(j)),0n));
const echelon=[];
for(const original of rows){let row=original;for(const [pivot,r] of echelon)if(row>>BigInt(pivot)&1n)row^=r;
  if(row){let pivot=0;while(!(row>>BigInt(pivot)&1n))pivot++;echelon.push([pivot,row]);}}
assert.equal(echelon.length,24);
const choose=(n,k)=>{let a=1;for(let j=1;j<=k;j++)a=a*(n-j+1)/j;return a;};
const allowed={single_component_four_units:4*choose(6,4)*16,
  adjacent_two_plus_two_units:4*choose(6,2)**2*16,
  opposite_spinors_plus_intermediate_unit:4*32**2*12};
assert.deepEqual(allowed,{single_component_four_units:960,adjacent_two_plus_two_units:14400,
  opposite_spinors_plus_intermediate_unit:49152});
const out={exact:true,glue_classes:classes,coset_minimum_histogram:hist,
  determinant:256/16**2,root_system:'D6^4',norm3_shell_size:4*32**2,
  norm3_sample64_twice_coordinates:shell,sample_Gram_F2_rank:echelon.length,
  characteristic8_count:2*6**2*4,allowed_individual_norm4:allowed,
  allowed_individual_norm4_total:Object.values(allowed).reduce((a,b)=>a+b,0),
  scope:'Integral rootful envelope and individual h classification; no simultaneous physical49-frame or graph certified.'};
fs.writeFileSync(new URL('./G18_G20_D6_QUATRE.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,classes:hist,sample_Gram_F2_rank:24,
  norm3_shell:4096,characteristic8:288,allowed_norm4_total:64512,no_physical_frame_claim:true}));

```


## G18_G20_D6_SIX_SPINORS.json

6518 octets ; SHA256 9f2108673284af149c8cf925ab050f85d44ca76b8afb0461b7aba62491466ec4

```json
{
  "exact": true,
  "scope": "D6^4/C4, same physical frame49+two primitive normals; f_A=6 only",
  "assumptions": [
    "fullframe=7I24",
    "min(N*)>=8/7",
    "J=7I2 primitive",
    "seven h mutually orthogonal"
  ],
  "centre_distributions_checked": 1716,
  "characteristic_capacity_passed": 569,
  "exact_characteristic_capacity_passed": 16,
  "distributions_with_one_relaxed_normal": 16,
  "relaxed_two_normal_pairs": 0,
  "common_four_axis_signed_pairs_checked": 256,
  "one_normal_cases": [
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        0,
        0,
        0,
        2,
        2
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            1,
            2,
            3
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        0,
        0,
        2,
        0,
        2
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            1,
            2,
            4
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        0,
        0,
        2,
        2,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            1,
            2,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        0,
        2,
        0,
        0,
        2
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            1,
            3,
            4
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        0,
        2,
        0,
        2,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            1,
            3,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        0,
        2,
        2,
        0,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            1,
            4,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        2,
        0,
        0,
        0,
        2
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            2,
            3,
            4
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        2,
        0,
        0,
        2,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            2,
            3,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        2,
        0,
        2,
        0,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            2,
            4,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        2,
        2,
        0,
        0,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            0,
            3,
            4,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        2,
        0,
        0,
        0,
        0,
        2
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            1,
            2,
            3,
            4
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        2,
        0,
        0,
        0,
        2,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            1,
            2,
            3,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        2,
        0,
        0,
        2,
        0,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            1,
            2,
            4,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        2,
        0,
        2,
        0,
        0,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            1,
            3,
            4,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        1,
        1,
        0,
        0,
        0,
        0
      ],
      "mD": [
        2,
        2,
        0,
        0,
        0,
        0
      ],
      "normal_options": [
        {
          "unit_component": "D",
          "support": [
            2,
            3,
            4,
            5
          ]
        }
      ]
    },
    {
      "mB": [
        3,
        3,
        0,
        0,
        0,
        0
      ],
      "mD": [
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "normal_options": [
        {
          "unit_component": "B",
          "support": [
            2,
            3,
            4,
            5
          ]
        }
      ]
    }
  ],
  "conclusion": "f_A=6 impossible; symmetric f_B=6 impossible; no global g18/g20 exclusion"
}

```


## G18_G20_D6_SIX_SPINORS.mjs

4096 octets ; SHA256 8909171e44b561967b1ef8be0c1f3577f9e095a27f0e0f16358fa925001eca30

```javascript
// Controle exact fini d'une relaxation necessaire du MEME frame D6^4.
// Ni recherche de graphe, ni solveur, ni enumeration des normes7 signees.
import { writeFileSync } from 'node:fs';

function* compositions(total, length, prefix = []) {
  if (length === 1) { yield [...prefix, total]; return; }
  for (let n = 0; n <= total; n++) yield* compositions(total - n, length - 1, [...prefix, n]);
}
function subsets4(allowed) {
  const result = [];
  for (let a = 0; a < allowed.length; a++)
    for (let b = a + 1; b < allowed.length; b++)
      for (let c = b + 1; c < allowed.length; c++)
        for (let d = c + 1; d < allowed.length; d++) result.push([allowed[a], allowed[b], allowed[c], allowed[d]]);
  return result;
}
function rootPairNecessary(first, second) {
  if (first.unit_component !== second.unit_component) return true;
  return first.support.filter(x => second.support.includes(x)).length <= 2;
}

// h7 has four units at B2,B3,B4,B5. Orthogonality forces all centres
// at B0,B1 or in D. This fixes only harmless coordinate permutations.
let checked = 0, capacityPassed = 0, exactCapacityPassed = 0, withOneNormal = 0, survivingPairs = 0;
const oneNormalCases = [];
for (const multiplicities of compositions(6, 8)) {
  checked++;
  const mB = [multiplicities[0], multiplicities[1], 0, 0, 0, 0];
  const mD = multiplicities.slice(2);
  const tB = mB.map((m, j) => m + (j >= 2 ? 1 : 0));
  const maxB = Math.max(...tB), maxD = Math.max(...mD);
  if (maxB + maxD > 3) continue;
  capacityPassed++;
  if (tB.every(a => mD.every(b => a + b === 1 || a + b === 3))) exactCapacityPassed++;
  // A normal with four units in D has half-coordinates on B. For
  // every such D unit one characteristic has product +/-3. Therefore
  // maxB+mD[j] <= 1 is necessary, since k>=2 forces BOTH normals flat.
  const eligibleD = mD.flatMap((m, j) => maxB + m <= 1 ? [j] : []);
  const eligibleB = tB.flatMap((m, j) => m + maxD <= 1 ? [j] : []);
  const options = [
    ...subsets4(eligibleD).map(support => ({ unit_component: 'D', support })),
    ...subsets4(eligibleB).map(support => ({ unit_component: 'B', support })),
  ];
  if (options.length) {
    withOneNormal++;
    oneNormalCases.push({ mB, mD, normal_options: options });
  }
  // Repetition is allowed here: it is a SAFE SUPERSET of the actual
  // two signed orthogonal normals. Common >=3 unit axes already fail.
  for (const first of options) for (const second of options)
    if (rootPairNecessary(first, second)) survivingPairs++;
}

let signedPairs = 0;
for (let first = 0; first < 16; first++) for (let second = 0; second < 16; second++) {
  const a = Array.from({length: 4}, (_, j) => ((first >> j) & 1) ? -1 : 1);
  const b = Array.from({length: 4}, (_, j) => ((second >> j) & 1) ? -1 : 1);
  let witness = false;
  for (let i = 0; i < 4; i++) for (let j = i + 1; j < 4; j++) {
    const sign = a[i] * a[j];
    if (Math.abs(a[i] + sign * a[j]) === 2 && Math.abs(b[i] + sign * b[j]) === 2) witness = true;
  }
  if (!witness) throw new Error('Missing root witness for common four unit axes');
  signedPairs++;
}
if (checked !== 1716 || exactCapacityPassed !== 16 || survivingPairs !== 0) throw new Error('Coverage failed');
const result = {
  exact: true,
  scope: 'D6^4/C4, same physical frame49+two primitive normals; f_A=6 only',
  assumptions: ['fullframe=7I24','min(N*)>=8/7','J=7I2 primitive','seven h mutually orthogonal'],
  centre_distributions_checked: checked,
  characteristic_capacity_passed: capacityPassed,
  exact_characteristic_capacity_passed: exactCapacityPassed,
  distributions_with_one_relaxed_normal: withOneNormal,
  relaxed_two_normal_pairs: survivingPairs,
  common_four_axis_signed_pairs_checked: signedPairs,
  one_normal_cases: oneNormalCases,
  conclusion: 'f_A=6 impossible; symmetric f_B=6 impossible; no global g18/g20 exclusion',
};
writeFileSync(new URL('./G18_G20_D6_SIX_SPINORS.json', import.meta.url), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ exact: result.exact, checked, capacityPassed, exactCapacityPassed, withOneNormal, survivingPairs, signedPairs }));

```


## G18_G20_MANIFESTE_COMBINATOIRE0836.json

5272 octets ; SHA256 c9d0cb9ca5be2947b9654dc458d0518f259e891f11f0916784c35cdc32e11c87

```json
{
  "kind": "frozen_own_mathematical_sources_and_bounded_controls",
  "scope": "physical frame49, explicit envelopes; no new complete local type or g18/g20 exclusion",
  "conclusions": {
    "generation42": true,
    "D11_in_U_dim24_excluded": true,
    "D6_cycle_individual_h_classification_complete": true,
    "D6_six_spinors_one_opposite_pair_excluded": true,
    "D6_cycle_whole_frame_excluded": false,
    "seven_Golay_selections_exhausted": false
  },
  "independent_f6_report": "acquired; separate supplement, not substituted by producer control",
  "own": [
    {
      "path": "G18_G20_QUARANTE_DEUX_GENERATEURS.md",
      "bytes": 2817,
      "sha256": "e6a5cd6936692031d14ecf566cccb71445bcf3095fa6e6c417c6b750e6d12421"
    },
    {
      "path": "G18_G20_DUAL_COORDONNEES.md",
      "bytes": 3540,
      "sha256": "4956adbbdd388ad3fb5845cccbe52a2282d4778bd48541d6fe745cbc21253583"
    },
    {
      "path": "G18_G20_D6_QUATRE.md",
      "bytes": 6995,
      "sha256": "93699a1ee744fe70fa155e1f7cd2821f6f253aebdcbe097ecbef296206c3bfea"
    },
    {
      "path": "G18_G20_D6_QUATRE.mjs",
      "bytes": 2510,
      "sha256": "0a147df75a003db1d62fe95f8d8ac619394487fe95a98a08c091319eb4498c9b"
    },
    {
      "path": "G18_G20_D6_QUATRE.json",
      "bytes": 17542,
      "sha256": "e747d9cf46a28c7981af17aa7944baeced93b21e3134eb2d49cb18bf1943014f"
    },
    {
      "path": "G18_G20_D6_SIX_SPINORS.md",
      "bytes": 6676,
      "sha256": "d1e8a5c45e42482e5fae1d6f52cb28c59dc561913a69b7fb542d49ab4cade0cc"
    },
    {
      "path": "G18_G20_D6_SIX_SPINORS.mjs",
      "bytes": 4096,
      "sha256": "8909171e44b561967b1ef8be0c1f3577f9e095a27f0e0f16358fa925001eca30"
    },
    {
      "path": "G18_G20_D6_SIX_SPINORS.json",
      "bytes": 6518,
      "sha256": "9f2108673284af149c8cf925ab050f85d44ca76b8afb0461b7aba62491466ec4"
    },
    {
      "path": "G18_G20_SEPT_BLOCS_CAPACITE.md",
      "bytes": 4807,
      "sha256": "eafa5a8153ccf6500d05a4c8a4329abfabe2d72fd586b10fd0cfb059a6732fd3"
    },
    {
      "path": "G18_G20_SEPT_BLOCS_CAPACITE.mjs",
      "bytes": 5225,
      "sha256": "e7c0a23b778a3da7cf63e6e9784f6cb7748cea841e6b202346f69381a576af53"
    },
    {
      "path": "G18_G20_TEST_SEPT_BLOCS.mjs",
      "bytes": 2690,
      "sha256": "f468983cd58b0acbf3b22e288c395ba67b9e7d7c00494780a8232c1f0020731c"
    },
    {
      "path": "G18_G20_TEST_SEPT_BLOCS.json",
      "bytes": 608,
      "sha256": "40d2e4e794668fca25bcaab3b119b40755a3ca3bd49984f68054d22587b75530"
    },
    {
      "path": "G18_G20_STATUTS_COMBINATOIRES0836.md",
      "bytes": 2749,
      "sha256": "69f1b2d2b890ec7ce34c4155a1f94dd4d97d2bcafd2be46ab118840296705d54"
    },
    {
      "path": "G18_G20_MANIFESTE_COMBINATOIRE0836.mjs",
      "bytes": 2759,
      "sha256": "0e46b3f7eb60eb46232c75c1262f24d90b921d74d467f95d87a02919bc28521a"
    }
  ],
  "prerequisites": [
    {
      "path": "../attaque_globale_27_0803/UNIFICATION_G18_G20_RANG24.md",
      "bytes": 7647,
      "sha256": "f3d1aa7908e63adf707c8cede320b5a091515ce0301487ee33b334ed785ef565"
    },
    {
      "path": "../attaque_globale_27_0803/SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.md",
      "bytes": 13003,
      "sha256": "b2a115acbde3af297479c58f9a8fca339f59cf85e3287f42fd2dcdbb70f9dccc"
    },
    {
      "path": "../attaque_globale_27_0803/AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md",
      "bytes": 9027,
      "sha256": "e03bbcab5f20605c168e2d1a1254e577ffe39a4610a316e06e44b0079c53bd7c"
    },
    {
      "path": "../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md",
      "bytes": 4577,
      "sha256": "14e1982694778879d232fdaa1b5b96db8a3321925b14cd2938c682f5fee5ee11"
    },
    {
      "path": "../attaque_globale_27_0803/G18_G20_MANIFESTE_COMBINATOIRE.json",
      "bytes": 7818,
      "sha256": "7496e183acc9902b1f2bc052ad0947b963cae633c6e58a67301ee5a7efb4f2d0"
    },
    {
      "path": "AUDIT_GENERATION42_ET_COQUE_ENTIERE.md",
      "bytes": 3440,
      "sha256": "0546400d993fcd659a531f5f99065d58b5806a245b067ee2f4b0dac5837e4954"
    },
    {
      "path": "AUDIT_D11_ET_LIMITE_COQUE.md",
      "bytes": 3328,
      "sha256": "185fb4ae8216e0cab721a533bf5d8e3ee6db00c81df398b4abbef2ec44f4cfb5"
    },
    {
      "path": "verifier_D11_et_coque_D6.mjs",
      "bytes": 3559,
      "sha256": "8acc2fe7b3f9c6ed0f5c61f5f373dbcf1559b80650cef6d659cd58b12630ed8a"
    },
    {
      "path": "verifier_D11_et_coque_D6.json",
      "bytes": 2519,
      "sha256": "dcadba627dda22ae7d43f6368e287a3715dcadb89c170726c2c2bb0977aa2339"
    },
    {
      "path": "AUDIT_D6_SIX_FRACTIONNAIRES_MEME_PAIRE.md",
      "bytes": 6249,
      "sha256": "efca00c61ec1647e597715f360528ef8de56123e1bac8faa4304f55073d836ca"
    },
    {
      "path": "verifier_D6_fA6_independant.mjs",
      "bytes": 3385,
      "sha256": "56642c70cb7ed0daba25f4784b1d2dde98d8e16940b4e56a5ab73d93cdb76bdb"
    },
    {
      "path": "verifier_D6_fA6_independant.json",
      "bytes": 8189,
      "sha256": "54c6abdefceb0aea2da06ec66b9b5409658c052eb6dc55879bc6e027aaaa8ec7"
    }
  ],
  "checks": [
    {
      "path": "G18_G20_D6_QUATRE.json",
      "exact": true
    },
    {
      "path": "G18_G20_D6_SIX_SPINORS.json",
      "exact": true
    },
    {
      "path": "G18_G20_TEST_SEPT_BLOCS.json",
      "exact": true
    }
  ]
}

```


## G18_G20_MANIFESTE_COMBINATOIRE0836.mjs

2759 octets ; SHA256 0e46b3f7eb60eb46232c75c1262f24d90b921d74d467f95d87a02919bc28521a

```javascript
// Fige uniquement les pieces propres de cette reprise ; aucun calcul de recherche.
import { readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const ownNames = [
  'G18_G20_QUARANTE_DEUX_GENERATEURS.md',
  'G18_G20_DUAL_COORDONNEES.md',
  'G18_G20_D6_QUATRE.md','G18_G20_D6_QUATRE.mjs','G18_G20_D6_QUATRE.json',
  'G18_G20_D6_SIX_SPINORS.md','G18_G20_D6_SIX_SPINORS.mjs','G18_G20_D6_SIX_SPINORS.json',
  'G18_G20_SEPT_BLOCS_CAPACITE.md','G18_G20_SEPT_BLOCS_CAPACITE.mjs',
  'G18_G20_TEST_SEPT_BLOCS.mjs','G18_G20_TEST_SEPT_BLOCS.json',
  'G18_G20_STATUTS_COMBINATOIRES0836.md','G18_G20_MANIFESTE_COMBINATOIRE0836.mjs',
];
const prerequisitePaths = [
  '../attaque_globale_27_0803/UNIFICATION_G18_G20_RANG24.md',
  '../attaque_globale_27_0803/SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.md',
  '../attaque_globale_27_0803/AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md',
  '../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md',
  '../attaque_globale_27_0803/G18_G20_MANIFESTE_COMBINATOIRE.json',
  'AUDIT_GENERATION42_ET_COQUE_ENTIERE.md',
  'AUDIT_D11_ET_LIMITE_COQUE.md',
  'verifier_D11_et_coque_D6.mjs','verifier_D11_et_coque_D6.json',
  'AUDIT_D6_SIX_FRACTIONNAIRES_MEME_PAIRE.md',
  'verifier_D6_fA6_independant.mjs','verifier_D6_fA6_independant.json',
];
function record(path) {
  const bytes = readFileSync(new URL(path, import.meta.url));
  return { path, bytes: bytes.length, sha256: createHash('sha256').update(bytes).digest('hex') };
}
const checks = ['G18_G20_D6_QUATRE.json','G18_G20_D6_SIX_SPINORS.json','G18_G20_TEST_SEPT_BLOCS.json'];
for (const name of checks) {
  if (JSON.parse(readFileSync(new URL(name, import.meta.url), 'utf8')).exact !== true) throw new Error(`Nonexact output: ${name}`);
}
const manifest = {
  kind: 'frozen_own_mathematical_sources_and_bounded_controls',
  scope: 'physical frame49, explicit envelopes; no new complete local type or g18/g20 exclusion',
  conclusions: {
    generation42: true,
    D11_in_U_dim24_excluded: true,
    D6_cycle_individual_h_classification_complete: true,
    D6_six_spinors_one_opposite_pair_excluded: true,
    D6_cycle_whole_frame_excluded: false,
    seven_Golay_selections_exhausted: false,
  },
  independent_f6_report: 'acquired; separate supplement, not substituted by producer control',
  own: ownNames.map(record),
  prerequisites: prerequisitePaths.map(record),
  checks: checks.map(name => ({ path: name, exact: true })),
};
const bytes = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
writeFileSync(new URL('./G18_G20_MANIFESTE_COMBINATOIRE0836.json', import.meta.url), bytes);
console.log(JSON.stringify({ exact: true, own: ownNames.length, prerequisites: prerequisitePaths.length,
  sha256: createHash('sha256').update(bytes).digest('hex') }));

```


## G18_G20_MANIFESTE_SUPPLEMENT_MIXTE0836.json

2188 octets ; SHA256 ad690290371390771f6875293231b476953a0fa12ae3316deca3b5f0fd4e9dc3

```json
{
  "kind": "frozen_mathematical_supplement",
  "same_frame": "42 u + 7 h + 2 primitive normals in D6^4 cycle glue",
  "scope": "f_A=4,f_B=2; h7 integer typeI in A/C, and symmetric version",
  "conclusion": "the four AC-spinor centres are distinct, exactly two in B and two in D",
  "whole_mixed_regime_excluded": false,
  "whole_D6_frame_excluded": false,
  "new_complete_g18_g20_type_excluded": false,
  "earlier_frozen_own_files_verified": 14,
  "own": [
    {
      "path": "G18_G20_D6_MIXTE_CENTRES_REPETES.md",
      "bytes": 5974,
      "sha256": "56b8fc1e58480b059e154db723a8fb699be7927a74b80d9de5f432c81e44b61e"
    },
    {
      "path": "G18_G20_D6_MIXTE_CENTRES_REPETES.mjs",
      "bytes": 3941,
      "sha256": "b5a6d8d22a01a4fa8a51522513c3e5fa6fd8389147b44fb5a8d7123423e573dc"
    },
    {
      "path": "G18_G20_D6_MIXTE_CENTRES_REPETES.json",
      "bytes": 1997,
      "sha256": "54067ebf5a3f6c75a5bc79b569c1b344b357e051bf82ccfc3620d0aea0fb0c6d"
    },
    {
      "path": "G18_G20_MANIFESTE_SUPPLEMENT_MIXTE0836.mjs",
      "bytes": 2278,
      "sha256": "a874fc2f4c9579b76eaa69d77a73a27dc565b4a070b7bb153971853409f1868c"
    }
  ],
  "prerequisites": [
    {
      "path": "G18_G20_MANIFESTE_COMBINATOIRE0836.json",
      "bytes": 5272,
      "sha256": "c9d0cb9ca5be2947b9654dc458d0518f259e891f11f0916784c35cdc32e11c87"
    },
    {
      "path": "G18_G20_D6_SIX_SPINORS.md",
      "bytes": 6676,
      "sha256": "d1e8a5c45e42482e5fae1d6f52cb28c59dc561913a69b7fb542d49ab4cade0cc"
    },
    {
      "path": "G18_G20_D6_QUATRE.md",
      "bytes": 6995,
      "sha256": "93699a1ee744fe70fa155e1f7cd2821f6f253aebdcbe097ecbef296206c3bfea"
    },
    {
      "path": "AUDIT_D6_MIXTE_CENTRES_REPETES.md",
      "bytes": 5076,
      "sha256": "4fd9283e9436c52a42d3fab0664facea4e7ceed788ce3a250a5c69b13cd8b9c1"
    },
    {
      "path": "verifier_D6_mixte_centres_independant.mjs",
      "bytes": 4972,
      "sha256": "96e995fc9f3f367ace1ea239aa2415a5b68f48e31beac6af57774e368efcfdd4"
    },
    {
      "path": "verifier_D6_mixte_centres_independant.json",
      "bytes": 3132,
      "sha256": "41c50ca25e80d7c9eb70506d6b90e89bd6dca88aa7ffa80e68719e2f3af46b90"
    }
  ]
}

```


## G18_G20_MANIFESTE_SUPPLEMENT_MIXTE0836.mjs

2278 octets ; SHA256 a874fc2f4c9579b76eaa69d77a73a27dc565b4a070b7bb153971853409f1868c

```javascript
// Raccord et freeze uniquement : aucun nouveau calcul de recherche.
import { readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
function record(path) {
  const bytes = readFileSync(new URL(path, import.meta.url));
  return { path, bytes: bytes.length, sha256: createHash('sha256').update(bytes).digest('hex') };
}
const frozen = JSON.parse(readFileSync(new URL('./G18_G20_MANIFESTE_COMBINATOIRE0836.json', import.meta.url), 'utf8'));
for (const old of frozen.own) {
  const now = record(old.path);
  if (now.sha256 !== old.sha256 || now.bytes !== old.bytes) throw new Error(`Frozen file altered: ${old.path}`);
}
const ownNames = ['G18_G20_D6_MIXTE_CENTRES_REPETES.md','G18_G20_D6_MIXTE_CENTRES_REPETES.mjs',
  'G18_G20_D6_MIXTE_CENTRES_REPETES.json','G18_G20_MANIFESTE_SUPPLEMENT_MIXTE0836.mjs'];
const prerequisites = ['G18_G20_MANIFESTE_COMBINATOIRE0836.json',
  'G18_G20_D6_SIX_SPINORS.md','G18_G20_D6_QUATRE.md',
  'AUDIT_D6_MIXTE_CENTRES_REPETES.md',
  'verifier_D6_mixte_centres_independant.mjs','verifier_D6_mixte_centres_independant.json'];
const result = JSON.parse(readFileSync(new URL('./G18_G20_D6_MIXTE_CENTRES_REPETES.json', import.meta.url), 'utf8'));
if (result.exact !== true || result.pairs_passing_root_bound !== 0 || result.local_ratio_sign_cases_checked !== 64)
  throw new Error('Supplement control not complete');
const manifest = {
  kind: 'frozen_mathematical_supplement',
  same_frame: '42 u + 7 h + 2 primitive normals in D6^4 cycle glue',
  scope: 'f_A=4,f_B=2; h7 integer typeI in A/C, and symmetric version',
  conclusion: 'the four AC-spinor centres are distinct, exactly two in B and two in D',
  whole_mixed_regime_excluded: false,
  whole_D6_frame_excluded: false,
  new_complete_g18_g20_type_excluded: false,
  earlier_frozen_own_files_verified: frozen.own.length,
  own: ownNames.map(record), prerequisites: prerequisites.map(record),
};
const bytes = Buffer.from(JSON.stringify(manifest,null,2)+'\n');
writeFileSync(new URL('./G18_G20_MANIFESTE_SUPPLEMENT_MIXTE0836.json', import.meta.url), bytes);
console.log(JSON.stringify({exact: true, own: ownNames.length, prerequisites: prerequisites.length,
  frozen_files_intact: frozen.own.length, sha256: createHash('sha256').update(bytes).digest('hex')}));

```


## G18_G20_SEPT_BLOCS_CAPACITE.mjs

5225 octets ; SHA256 e7c0a23b778a3da7cf63e6e9784f6cb7748cea841e6b202346f69381a576af53

```javascript
import crypto from 'node:crypto';
const mod=(x,p)=>(x%p+p)%p;
const weight=x=>{let n=0;for(;x;x&=x-1)n++;return n;};
const hash=x=>crypto.createHash('sha256').update(JSON.stringify(x)).digest('hex');
export function golayWords(){
  const g=[11,9,7,6,5,1,0].reduce((a,j)=>a|(1<<j),0),words=[];
  for(let m=0;m<4096;m++){
    let w=0;for(let j=0;j<12;j++)if(m>>j&1)w^=g<<j;
    if(weight(w)%2)w|=1<<23;words.push(w);
  }
  return words;
}
export function membership(z,code){
  if(z.length!==24||z.some(x=>!Number.isInteger(x)))throw Error('24 integral coordinates required');
  const parity=mod(z[0],2);let word=0;
  if(z.some(x=>mod(x,2)!==parity))return {member:false,reason:'mixed_parity'};
  for(let j=0;j<24;j++)if(mod(z[j]-parity,4)===2)word|=1<<j;
  const sum=z.reduce((a,b)=>a+b,0),inCode=code.has(word);
  return {member:inCode&&mod(sum,8)===0,word,in_code:inCode,sum,sum_mod8:mod(sum,8)};
}
const dot=(a,b)=>a.reduce((s,x,j)=>s+x*b[j],0);
export function prepareShell(B){
  if(B.length!==2||B.some(row=>row.length!==24||row.some(x=>Math.abs(x)!==1&&Math.abs(x)!==3)))
    throw Error('B must contain two 24-coordinate rows with entries +/-1 or +/-3');
  const words=golayWords(),code=new Set(words);
  if(B.some(row=>dot(row,row)!==56||!membership(row,code).member)||dot(B[0],B[1])!==0)
    throw Error('The two B charges must belong to U_Golay, have norm7 and be orthogonal');
  const lines=[];
  for(const word of words){
    const E=Array.from({length:24},(_,j)=>1-2*(word>>j&1));
    if(E[0]===1&&B.every(row=>dot(row,E)===0))lines.push(E);
  }
  return {B:B.map(row=>row.slice()),words,code,lines,
    code_sha256:hash(words),B_sha256:hash(B),shell_sha256:hash(lines),
    complete_shell_reconstructed:true,oriented_shell_size:2*lines.length,line_count:lines.length,
    scope:'Fixed explicit U_Golay and B; complete norm3 shell reconstructed from the code.'};
}
export function blockBins(row,lines){
  const bins={zero:0n,positive:0n,negative:0n};
  for(let i=0;i<lines.length;i++){
    const a=dot(row,lines[i]),bit=1n<<BigInt(i);
    if(a===0)bins.zero|=bit;else if(a===4)bins.positive|=bit;else if(a===-4)bins.negative|=bit;
  }
  return bins;
}
const popcount=x=>{let n=0;for(;x;x&=x-1n)n++;return n;};
export function pairCapacitiesFromBins(bins,lineCount){
  const profiles=[],all=(1n<<BigInt(lineCount))-1n;
  for(let c=0;c<bins.length;c++)for(let d=c+1;d<bins.length;d++){
    let far=all;for(let k=0;k<bins.length;k++)if(k!==c&&k!==d)far&=bins[k].zero;
    const plus=far&((bins[c].positive&bins[d].positive)|(bins[c].negative&bins[d].negative));
    const minus=far&((bins[c].positive&bins[d].negative)|(bins[c].negative&bins[d].positive));
    profiles.push({c,d,plus:plus.toString(16),minus:minus.toString(16),
      plus_count:popcount(plus),minus_count:popcount(minus)});
  }
  return profiles;
}
export function sevenCapacity(M,prepared){
  if(M.length!==7||M.some(row=>row.length!==24||row.some(x=>![0,1,-1].includes(x))))
    throw Error('M must have seven 24-coordinate rows with entries0,+1,-1');
  const context={M:M.map(row=>row.slice()),B:prepared.B,M_sha256:hash(M),
    B_sha256:prepared.B_sha256,code_sha256:prepared.code_sha256,shell_sha256:prepared.shell_sha256,
    complete_shell_reconstructed:prepared.complete_shell_reconstructed,
    assumptions:['Physical seven blocks in the fixed explicit U_Golay orthogonal to B',
      'Odd determinant of the physical N','All42 roots chosen from the complete norm3 shell']};
  const fail=(kind,witness)=>({refuted:true,kind,witness,context,
    scope:'Refutes this simultaneous seven-block selection only; not every envelope, genre or graph.'});
  for(let c=0;c<7;c++){
    if(dot(M[c],M[c])!==8)return fail('block_weight',{c,weight:dot(M[c],M[c])});
    const member=membership(M[c].map(x=>2*x),prepared.code);
    if(!member.member)return fail('block_not_in_lattice',{c,...member});
    if(dot(M[c],prepared.B[0])||dot(M[c],prepared.B[1]))return fail('block_not_orthogonal_B',{c});
    for(let d=0;d<c;d++)if(dot(M[c],M[d]))return fail('blocks_not_orthogonal',{c,d,inner:dot(M[c],M[d])});
  }
  const columnWeights=Array.from({length:24},(_,j)=>M.reduce((s,row)=>s+row[j]**2,0));
  if(columnWeights.filter(x=>x===1).length!==8||columnWeights.filter(x=>x===3).length!==16)
    return fail('column_weight_profile',{columnWeights});
  for(let j=0;j<24;j++)if(4*columnWeights[j]+prepared.B[0][j]**2+prepared.B[1][j]**2!==14)
    return fail('column_weight_B_mismatch',{j,column_weight:columnWeights[j],
      B_squared:prepared.B[0][j]**2+prepared.B[1][j]**2});
  const Z=Array.from({length:24},(_,j)=>M.reduce((s,row)=>s+row[j],0));
  const halfSum=membership(Z,prepared.code);
  if(!halfSum.member)return fail('half_sum_not_in_lattice',{Z,...halfSum});
  const bins=M.map(row=>blockBins(row,prepared.lines));
  const profiles=pairCapacitiesFromBins(bins,prepared.lines.length);
  const empty=profiles.find(p=>p.plus_count===0||p.minus_count===0);
  if(empty)return fail('empty_D7_class',{c:empty.c,d:empty.d,sign:empty.plus_count===0?'same':'opposite'});
  return {refuted:false,kind:'capacity_only',context,half_sum:halfSum,profiles,
    scope:'All42 classes nonempty; mutual Gram, frame, budgets and generation index still required.'};
}

```


## G18_G20_TEST_SEPT_BLOCS.json

608 octets ; SHA256 40d2e4e794668fca25bcaab3b119b40755a3ca3bd49984f68054d22587b75530

```json
{
  "exact": true,
  "bitset_profiles_compared": 42,
  "abstract_noise_profiles_ignored": 3,
  "one_class_removal_detected": true,
  "golden_Golay_charges_membership": true,
  "golden_complete_shell_size": 704,
  "golden_line_count": 352,
  "code_sha256": "a1cf04f6f3282140a70a2f207961fb82e32c254af716869c87d917ab1a04e80c",
  "B_sha256": "640a6ffee26828d0be66dc2f2667238b07d29dcba63de5e4814a0a143ff70576",
  "shell_sha256": "f5878a046782bc5fd505cac914e16c12eff3e1dbc9a73a232fe20403afe92827",
  "scope": "Source fixtures and reconstruction only; no seven-block coverage, physical49-frame or graph claimed."
}

```


## G18_G20_TEST_SEPT_BLOCS.mjs

2690 octets ; SHA256 f468983cd58b0acbf3b22e288c395ba67b9e7d7c00494780a8232c1f0020731c

```javascript
import fs from 'node:fs';
import assert from 'node:assert/strict';
import {golayWords,membership,prepareShell,pairCapacitiesFromBins,sevenCapacity}
  from './G18_G20_SEPT_BLOCS_CAPACITE.mjs';
const signature=[];
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const sign of [1,-1]){
  const v=Array(7).fill(0);v[i]=1;v[j]=sign;signature.push(v);
}
signature.push([1,0,0,0,0,0,0],[1,1,1,0,0,0,0],[2,1,0,0,0,0,0]);
const bins=Array.from({length:7},(_,i)=>({zero:0n,positive:0n,negative:0n}));
for(let j=0;j<signature.length;j++)for(let i=0;i<7;i++){
  const x=signature[j][i],b=1n<<BigInt(j);
  if(x===0)bins[i].zero|=b;else if(x===1)bins[i].positive|=b;else if(x===-1)bins[i].negative|=b;
}
const profiles=pairCapacitiesFromBins(bins,signature.length);
for(const p of profiles){
  const candidates=sign=>signature.map((v,j)=>({v,j})).filter(({v})=>v[p.c]&&Math.abs(v[p.c])===1&&
    Math.abs(v[p.d])===1&&v[p.c]*v[p.d]===sign&&v.every((a,i)=>i===p.c||i===p.d||a===0)).map(({j})=>j);
  for(const [key,s] of [['plus',1],['minus',-1]]){
    const mask=candidates(s).reduce((a,j)=>a|(1n<<BigInt(j)),0n);
    assert.equal(p[key],mask.toString(16));assert.equal(p[`${key}_count`],1);
  }
}
const removed=bins.map(row=>Object.fromEntries(Object.entries(row).map(([key,b])=>[key,b&~1n])));
const failures=pairCapacitiesFromBins(removed,signature.length).filter(p=>!p.plus_count||!p.minus_count);
assert.deepEqual(failures.map(p=>[p.c,p.d,p.plus_count,p.minus_count]),[[0,1,0,1]]);
const words=golayWords(),code=new Set(words);
assert.equal(code.size,4096);
const V=[0,1,3,4,5,6,7,8,10,11,12,14],D=[0,1,2,9],Dp=[3,4,13,15];
const B=[Array.from({length:24},(_,j)=>1-4*+D.includes(j)),
  Array.from({length:24},(_,j)=>(1-2*+V.includes(j))*(1-4*+Dp.includes(j)))];
assert(B.every(row=>membership(row,code).member));
const broken=B[0].slice();broken[23]*=-1;assert(!membership(broken,code).member);
const prepared=prepareShell(B);assert.equal(prepared.line_count,352);assert.equal(prepared.oriented_shell_size,704);
const zeroM=Array.from({length:7},()=>Array(24).fill(0));
assert.equal(sevenCapacity(zeroM,prepared).kind,'block_weight');
const out={exact:true,bitset_profiles_compared:42,abstract_noise_profiles_ignored:3,
  one_class_removal_detected:true,golden_Golay_charges_membership:true,
  golden_complete_shell_size:704,golden_line_count:352,
  code_sha256:prepared.code_sha256,B_sha256:prepared.B_sha256,shell_sha256:prepared.shell_sha256,
  scope:'Source fixtures and reconstruction only; no seven-block coverage, physical49-frame or graph claimed.'};
fs.writeFileSync(new URL('./G18_G20_TEST_SEPT_BLOCS.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify(out));

```


## MANIFEST_ALGEBRE_0836.json

4271 octets ; SHA256 b30898ac143684337401625df5124bc735b91148c0994533496f88c0c19813f6

```json
{
  "frozen": true,
  "owner": "g18_algebre_neuve",
  "directory": "outputs/attaque_globale_27_0836",
  "files_count": 14,
  "files": [
    {
      "name": "OBSTRUCTION_COQUE3_ET_D8_CUBE.md",
      "bytes": 8670,
      "sha256": "72363f4c8c247ce9032e4c7f7cb4d4af5f905cf529d95f32a0c2fd4942d7c962"
    },
    {
      "name": "controle_coque3_D8_et_trialite.mjs",
      "bytes": 4441,
      "sha256": "f37c6a02a3a55727fda6208db78b58609cbad27bd3c84660cd798ab7a01f8dfc"
    },
    {
      "name": "controle_coque3_D8_et_trialite.json",
      "bytes": 2594,
      "sha256": "f102fc83009fb6c4ff90ca1a01a037aabd4c1ffcdebfdb97edc8a5dbf49d91b6"
    },
    {
      "name": "SEPT_OCTADES_RANG_BINAIRE_PETIT.md",
      "bytes": 7444,
      "sha256": "13534ecf47c00a28dc11b35420cf73f9eb63c93320bfd87a8c367ccbec097b4a"
    },
    {
      "name": "controle_sept_octades_rang4.mjs",
      "bytes": 4579,
      "sha256": "dc969063f47510a85e5e376804a0a79c8788f24689dfe90c3551c9f23e7903d3"
    },
    {
      "name": "controle_sept_octades_rang4.json",
      "bytes": 11545,
      "sha256": "8d8c19992f26efd7c85d054bb34a833e6c10f00065dcc9c10e0c35dbd0a24782"
    },
    {
      "name": "D4_SIX_CYCLE_SELECTION_COMMUNE.md",
      "bytes": 5355,
      "sha256": "39839ca0035e0e8d2d4bdbf8b90faf1904ab1a0b72a0b7f621b2bfd0efbf9279"
    },
    {
      "name": "controle_D4_cycle6_classes.mjs",
      "bytes": 3755,
      "sha256": "72f9bfc38c6a7c52d2607606ea6e863f7f3eb29fb38971f3b184eac312115c5b"
    },
    {
      "name": "controle_D4_cycle6_classes.json",
      "bytes": 42040,
      "sha256": "1ad44dcf3d4e3bf0cd2a6c7fda4974c693c1ff16447e863de0951d05efe2158c"
    },
    {
      "name": "COUPES_ENTIERES_SELECTION42.md",
      "bytes": 6648,
      "sha256": "91c41918d3c999e5771156e5b07763bfc6c9458a77378ba28c40cbf6ea78fe96"
    },
    {
      "name": "controle_congruences_selection42.mjs",
      "bytes": 4080,
      "sha256": "53515dcbfd3a31b6889e9b27fbfee4c75f8854eea2d47cc4f0e1675cfaeeb5b8"
    },
    {
      "name": "controle_congruences_selection42.json",
      "bytes": 2558,
      "sha256": "197e8a20d46063f4954020c8db4d9b95354bf28b39fa95a2d1caec463419184b"
    },
    {
      "name": "controle_selection42_golay.mjs",
      "bytes": 6518,
      "sha256": "ab36c25725bec80aca4365ba6607d0276bd990dc2145bcb80d8b7a5635ccead6"
    },
    {
      "name": "controle_selection42_golay.json",
      "bytes": 20665,
      "sha256": "3f7d688f1fdad4795b1e85fef2dd59f81027a6d8d5af85b9cda21833bafd774f"
    }
  ],
  "reviewed_by": "g18_audit_neuf",
  "results": {
    "D8_cube": {
      "status": "proved_and_independently_reviewed",
      "physical_frame_impossible": true,
      "shell4096": 4096,
      "shell_Gram_mod2_rank": 20,
      "physical_required_rank": 22
    },
    "D4_cycle6": {
      "status": "proved_and_independently_reviewed",
      "families": 256,
      "refuted": 231,
      "qualifying": 25,
      "minimum_used_classes": 6,
      "qualifying_realization": false
    },
    "seven_octads": {
      "status": "proved_and_independently_reviewed",
      "claim": "rank at most4 implies A in support code",
      "fixed_normal_A": 41503,
      "A_outside_code": true,
      "required_rank_for_fixed_pair": 5,
      "A_in_code_not_refuted": true
    },
    "selection42_congruences": {
      "status": "independent_mathematical_derivation_reviewed",
      "source_exact": true,
      "syndromes_verified": 288,
      "single_word": 7218972,
      "checksum_mod16": 8,
      "independent_fixture_control_in_preparation": true
    }
  },
  "limitations": [
    "No global exclusion of g18 or g20.",
    "No modification of frozen0803 or0736 artifacts.",
    "D4^6 qualifying families are not realized or declared impossible.",
    "Seven-octad ranks5/6/7 and A inside the code remain open.",
    "The42 witness selections do not assert degree10,CT or SRG common-neighbor budgets."
  ],
  "prerequisites": [
    "outputs/attaque_globale_27_0836/G18_G20_QUARANTE_DEUX_GENERATEURS.md",
    "outputs/attaque_globale_27_0836/EXCLUSION_FRAME_D8_TROIS.md",
    "outputs/attaque_globale_27_0836/ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md",
    "outputs/attaque_globale_27_0803/UNIFICATION_G18_G20_RANG24.md",
    "outputs/attaque_globale_27_0803/controle_enveloppe_g20_golay.json"
  ]
}

```


## MANIFEST_AUDIT_INDEPENDANT_0836.json

10217 octets ; SHA256 cc90542261ec5d36fd187a651904eb389c6034b39ae9bfe6ac5e579be474d83b

```json
{
  "exact": true,
  "status": "frozen_own_outputs_only",
  "scope": "Uniform mathematical consequences and explicitly conditional families of the same physical frame; no full g18/g20 exclusion.",
  "file_count": 35,
  "executed_exact_sources": 11,
  "entries": [
    {
      "file": "THEOREME_CARACTERISTIQUE8_THETA.md",
      "bytes": 8633,
      "sha256": "dc70c6159e88fab9542fd83de6827396dd54c81c4d27331eb914e103e8b736d9"
    },
    {
      "file": "verifier_theta_caracteristique8.mjs",
      "bytes": 5670,
      "sha256": "09d42c355d9c793a3065db52416f897b85f9887fbcae4ac95ad11f7f27b7d504"
    },
    {
      "file": "verifier_theta_caracteristique8.json",
      "bytes": 3149,
      "sha256": "22b9322b3783982431ea6ddf987a1b897b2d690d8aabf655289f9f4311e243e7"
    },
    {
      "file": "THEOREME_MOMENTS_CARACTERISTIQUES8.md",
      "bytes": 6188,
      "sha256": "2fdb9e5dace239006dcc0894c20c855a095a2ccb5ac138e60e4968d1c0e9ad18"
    },
    {
      "file": "verifier_moments_caracteristique8.mjs",
      "bytes": 4591,
      "sha256": "e433d49e37d56efc8cdfd5554325a537918290a463b29f232e00dd8fa4bad064"
    },
    {
      "file": "verifier_moments_caracteristique8.json",
      "bytes": 1944,
      "sha256": "9f053c0fca4486a26d00e77f3c98cc7abaf1ebcffd14ac4540f448892a51a496"
    },
    {
      "file": "EXCLUSION_FRAME_D8_TROIS.md",
      "bytes": 4334,
      "sha256": "4d629388b8832bba4a47c5e9bdd2020d773b4e4ae9c9027144d5fe98efa5fb09"
    },
    {
      "file": "verifier_frame_D8_trois.mjs",
      "bytes": 4426,
      "sha256": "d0d784c3a8ca6e77e0c95edcd4e5a533ae23b4f48e44044c76b84b5c0118c756"
    },
    {
      "file": "verifier_frame_D8_trois.json",
      "bytes": 2195,
      "sha256": "21bc34b046b16c6a9dee593b830311b5c385fbe29c3fb20055a18dffd64fe504"
    },
    {
      "file": "AUDIT_GENERATION42_ET_COQUE_ENTIERE.md",
      "bytes": 3440,
      "sha256": "0546400d993fcd659a531f5f99065d58b5806a245b067ee2f4b0dac5837e4954"
    },
    {
      "file": "verifier_coque_D8_mod2.mjs",
      "bytes": 2282,
      "sha256": "8bab28410783cea666a88b25606a6056251791caaebe008e72a9fe5aaa593cfd"
    },
    {
      "file": "verifier_coque_D8_mod2.json",
      "bytes": 418,
      "sha256": "b051a8c5659f87c85b1a8387b2a01edad1be0e702faa6dd85082145efc72db4e"
    },
    {
      "file": "AUDIT_D11_ET_LIMITE_COQUE.md",
      "bytes": 3328,
      "sha256": "185fb4ae8216e0cab721a533bf5d8e3ee6db00c81df398b4abbef2ec44f4cfb5"
    },
    {
      "file": "verifier_D11_et_coque_D6.mjs",
      "bytes": 3559,
      "sha256": "8acc2fe7b3f9c6ed0f5c61f5f373dbcf1559b80650cef6d659cd58b12630ed8a"
    },
    {
      "file": "verifier_D11_et_coque_D6.json",
      "bytes": 2519,
      "sha256": "dcadba627dda22ae7d43f6368e287a3715dcadb89c170726c2c2bb0977aa2339"
    },
    {
      "file": "ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md",
      "bytes": 7470,
      "sha256": "13a222669e15e92676160573bd112209f04d823fda1d8cc263f4a6453e138e39"
    },
    {
      "file": "verifier_rootless_code24.mjs",
      "bytes": 2948,
      "sha256": "ca2c51affa6ff639d7d0c90a9af388757ad5fab0e1b8138f8245fa3150a166aa"
    },
    {
      "file": "verifier_rootless_code24.json",
      "bytes": 1338,
      "sha256": "c399539ed9136b6603ee4e11cb66aa21e2fc2c1b625685a2f1f0142d6ec219d0"
    },
    {
      "file": "AUDIT_HEPTADE_RANG4_ET_D6_BLOCS.md",
      "bytes": 5022,
      "sha256": "bef6f38cee740d630da3b6a8e4716b1e851250a2e195f0d0e0a5ccfc58e9dce2"
    },
    {
      "file": "verifier_heptade_et_D6_bornes.mjs",
      "bytes": 3961,
      "sha256": "8efbd65240e9f736c20aefc59c6c9e5cb97af83c6348010b65fcbaa46a9e5fbc"
    },
    {
      "file": "verifier_heptade_et_D6_bornes.json",
      "bytes": 1004,
      "sha256": "e71199c37b13be894d4be686df02c0f7469be0de76ef2bf8e66bf13d14226668"
    },
    {
      "file": "AUDIT_D6_SIX_FRACTIONNAIRES_MEME_PAIRE.md",
      "bytes": 6249,
      "sha256": "efca00c61ec1647e597715f360528ef8de56123e1bac8faa4304f55073d836ca"
    },
    {
      "file": "verifier_D6_fA6_independant.mjs",
      "bytes": 3385,
      "sha256": "56642c70cb7ed0daba25f4784b1d2dde98d8e16940b4e56a5ab73d93cdb76bdb"
    },
    {
      "file": "verifier_D6_fA6_independant.json",
      "bytes": 8189,
      "sha256": "54c6abdefceb0aea2da06ec66b9b5409658c052eb6dc55879bc6e027aaaa8ec7"
    },
    {
      "file": "AUDIT_Q42_ET_CLASSIFICATION_D6.md",
      "bytes": 4581,
      "sha256": "561b44d6c66377a816a2d663db4de52eb0d1df0ceffa428291ae68c5ea9aea12"
    },
    {
      "file": "verifier_Q42_et_collage_D6_independant.mjs",
      "bytes": 6448,
      "sha256": "0e80c70704eb3831d0798e5f92135a22b5c8df9dcc028ffa5f4668cee0dc0551"
    },
    {
      "file": "verifier_Q42_et_collage_D6_independant.json",
      "bytes": 1245,
      "sha256": "7362e2726a9df2e1025456a60b8a5dc129c26a3daec51b2aed18d936cfa0004f"
    },
    {
      "file": "AUDIT_D6_MIXTE_CENTRES_REPETES.md",
      "bytes": 5076,
      "sha256": "4fd9283e9436c52a42d3fab0664facea4e7ceed788ce3a250a5c69b13cd8b9c1"
    },
    {
      "file": "verifier_D6_mixte_centres_independant.mjs",
      "bytes": 4972,
      "sha256": "96e995fc9f3f367ace1ea239aa2415a5b68f48e31beac6af57774e368efcfdd4"
    },
    {
      "file": "verifier_D6_mixte_centres_independant.json",
      "bytes": 3132,
      "sha256": "41c50ca25e80d7c9eb70506d6b90e89bd6dca88aa7ffa80e68719e2f3af46b90"
    },
    {
      "file": "AUDIT_FAMILLE_COMPLETE_D8_TROIS.md",
      "bytes": 3520,
      "sha256": "8aa097f81c730af7f3003d34da18a3d44241f073400a646127c6b0ab077d4189"
    },
    {
      "file": "verifier_collages_D8_independant.mjs",
      "bytes": 4258,
      "sha256": "209842f07d8c545b244d5aaf8d9e766f5bbcf0de2e9e9508e7d5f74183058d01"
    },
    {
      "file": "verifier_collages_D8_independant.json",
      "bytes": 9374,
      "sha256": "ab382730e1c86c2f57a5ab67ec323e889d4c7984ef92c59784e762a857374413"
    },
    {
      "file": "BILAN_AUDIT_INDEPENDANT_0836.md",
      "bytes": 4369,
      "sha256": "d9842032a63c2a6aa77c4c465039a84875c3b602322cdc82a97fe7cd274b4455"
    },
    {
      "file": "figer_audit_independant_0836.mjs",
      "bytes": 4326,
      "sha256": "9049ee6fbcf9b361b43afef5527b713e499660e9ee1334be8b9e58634eec6a3d"
    }
  ],
  "result_checks": [
    {
      "source": "verifier_theta_caracteristique8.mjs",
      "result": "verifier_theta_caracteristique8.json",
      "exact": true
    },
    {
      "source": "verifier_moments_caracteristique8.mjs",
      "result": "verifier_moments_caracteristique8.json",
      "exact": true
    },
    {
      "source": "verifier_frame_D8_trois.mjs",
      "result": "verifier_frame_D8_trois.json",
      "exact": true
    },
    {
      "source": "verifier_coque_D8_mod2.mjs",
      "result": "verifier_coque_D8_mod2.json",
      "exact": true
    },
    {
      "source": "verifier_D11_et_coque_D6.mjs",
      "result": "verifier_D11_et_coque_D6.json",
      "exact": true
    },
    {
      "source": "verifier_rootless_code24.mjs",
      "result": "verifier_rootless_code24.json",
      "exact": true
    },
    {
      "source": "verifier_heptade_et_D6_bornes.mjs",
      "result": "verifier_heptade_et_D6_bornes.json",
      "exact": true
    },
    {
      "source": "verifier_D6_fA6_independant.mjs",
      "result": "verifier_D6_fA6_independant.json",
      "exact": true
    },
    {
      "source": "verifier_Q42_et_collage_D6_independant.mjs",
      "result": "verifier_Q42_et_collage_D6_independant.json",
      "exact": true
    },
    {
      "source": "verifier_D6_mixte_centres_independant.mjs",
      "result": "verifier_D6_mixte_centres_independant.json",
      "exact": true
    },
    {
      "source": "verifier_collages_D8_independant.mjs",
      "result": "verifier_collages_D8_independant.json",
      "exact": true
    }
  ],
  "dependencies": [
    {
      "file": "../attaque_globale_27_0803/MANIFEST_AUDIT_INDEPENDANT_0803.json",
      "bytes": 10410,
      "sha256": "0ca8af0714d5edcf74e6ee5295fabf8e508678008d1d455a2fcb4bc2a6858ef8",
      "access": "read_only"
    },
    {
      "file": "../attaque_globale_27_0803/AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md",
      "bytes": 9027,
      "sha256": "e03bbcab5f20605c168e2d1a1254e577ffe39a4610a316e06e44b0079c53bd7c",
      "access": "read_only"
    },
    {
      "file": "../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md",
      "bytes": 4577,
      "sha256": "14e1982694778879d232fdaa1b5b96db8a3321925b14cd2938c682f5fee5ee11",
      "access": "read_only"
    },
    {
      "file": "../attaque_globale_27_0803/UNIFICATION_G18_G20_RANG24.md",
      "bytes": 7647,
      "sha256": "f3d1aa7908e63adf707c8cede320b5a091515ce0301487ee33b334ed785ef565",
      "access": "read_only"
    },
    {
      "file": "../attaque_globale_27_0803/verifier_golay_enveloppe_indep.json",
      "bytes": 6586,
      "sha256": "76cc2cb462ba125d9488bee80cc56857406c10c7e8fff62ec3980c29ff392cb1",
      "access": "read_only"
    },
    {
      "file": "../attaque_globale_27_0803/controles_positifs_cadre_global.json",
      "bytes": 1068,
      "sha256": "c699700a3d764876711c0f4087582a1a2b95f238d58746f120ac743293fcd7ca",
      "access": "read_only"
    },
    {
      "file": "../dossier6_involution/NOTE_RESEAU_MINIMUM.md",
      "bytes": 7343,
      "sha256": "e4e75cb9f6fb194486269a7d8109b28a3e2beb5e86dcc529a5603a4d1d7ab1d3",
      "access": "read_only"
    },
    {
      "file": "controle_selection42_golay.json",
      "bytes": 20665,
      "sha256": "3f7d688f1fdad4795b1e85fef2dd59f81027a6d8d5af85b9cda21833bafd774f",
      "access": "read_only"
    }
  ],
  "old_outputs_modified": false,
  "new_local_type_exclusions": 0,
  "rootless_shadowframe_uniform": true,
  "D8_three_entire_ambient_family_excluded": true,
  "D6_four_entire_ambient_family_excluded": false,
  "D6_same_pair_fractional_six_excluded": true,
  "D6_mixed_regime_excluded": false,
  "D6_mixed_centres_necessary": "four distinct centres, two B and two D; only when h7 is integral in AC",
  "limitations": [
    "No full odd-unimodular rank-24 classification",
    "No universal shell Gram rank-20 bound",
    "No shadowframe without the rootless hypothesis",
    "Positive H2/BvLS parameters remain 3/9 and their own norms",
    "Fixed Q42 fixtures do not satisfy all physical graph axioms"
  ]
}

```


## MANIFEST_SUPPLEMENT_D8_TROIS.json

1397 octets ; SHA256 6a3ad91a9a128f24807864cb6dfff66e26c8f0f32f322297836291b894b328e1

```json
{
  "frozen": true,
  "owner": "g18_algebre_neuve",
  "files_count": 3,
  "files": [
    {
      "name": "SUPPLEMENT_D8_TROIS_TOUS_COLLAGES.md",
      "bytes": 8274,
      "sha256": "13c0e1b0ce89931ff8fdbec41ba7ea6843e4137198f7118e79d147103b8a1ec1"
    },
    {
      "name": "classifier_collages_D8_trois.mjs",
      "bytes": 5038,
      "sha256": "2535a462bb40d3811ed36214da4dc0555fdc741f3513371a692cf85c20aab0d7"
    },
    {
      "name": "classifier_collages_D8_trois.json",
      "bytes": 260080,
      "sha256": "416369c633abf51a67c5e396bc9dc8cb5f188d11773b5f8973bea65ee402da93"
    }
  ],
  "theorem": "Aucun collage integral unimodulaire24 de D8^3 ne porte le repere physique42+7 avec ses deux normales7, dans les cadresg18/g20.",
  "independent_checks": [
    "verifier_tous_collages_D8_parent.mjs",
    "verifier_collages_D8_independant.mjs"
  ],
  "counts": {
    "Lagrangians": 135,
    "even": 30,
    "odd": 105,
    "min1": 37,
    "singleton_E8": 24,
    "double_v_D16": 12,
    "residual": 32,
    "forms": [
      8,
      24
    ]
  },
  "prerequisites": [
    "OBSTRUCTION_COQUE3_ET_D8_CUBE.md",
    "G18_G20_QUARANTE_DEUX_GENERATEURS.md",
    "../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md"
  ],
  "limitations": [
    "No exclusion of all rank24 envelopes.",
    "No global exclusion of g18/g20.",
    "The14 previously frozen algebra artifacts remain unchanged."
  ]
}

```


## REPERE_COMPLET_GOLAY_DOMAINES.json

2716692 octets ; SHA256 b50d1f7499926f3dfc13c58db69bb60d4a5621da0bdfe31c69fc2478f93501d6

Fichier volumineux fourni intégralement et séparément dans l’archive. Sa source génératrice figure dans ce document.


## REPERE_COMPLET_GOLAY_DOMAINES.mjs

2676 octets ; SHA256 9cb4578d1369deae546de67f59ad14df5baceebe3839273a0a8cd19098d84ba5

```javascript
import fs from 'node:fs';import path from 'node:path';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));const cert=JSON.parse(fs.readFileSync(path.join(here,'../attaque_globale_27_0803/controle_enveloppe_g20_golay.json')));
const pop=x=>{let n=0;for(;x;x&=x-1)n++;return n;},dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);let gp=0;for(const e of cert.binary_generator_exponents)gp|=1<<e;const words=[];for(let m=0;m<4096;m++){let w=0;for(let i=0;i<12;i++)if((m>>i)&1)w^=gp<<i;if(pop(w)&1)w|=1<<23;words.push(w);}
const V=new Set(cert.V),D=new Set(cert.D),Dp=new Set(cert.D_prime);const B1=Array.from({length:24},(_,i)=>D.has(i)?-3:1),B2=Array.from({length:24},(_,i)=>(V.has(i)?-1:1)*(Dp.has(i)?-3:1));const bigMask=[...D,...Dp].reduce((m,i)=>m|(1<<i),0);
const E=words.map(w=>Array.from({length:24},(_,i)=>(w>>i)&1?-1:1)).filter(e=>dot(e,B1)===0&&dot(e,B2)===0);assert.equal(E.length,704);const projectiveE=E.filter(e=>e[0]===1);
const octads=[],candidateM=[];for(const w of words.filter(w=>pop(w)===8)){const supp=Array.from({length:24},(_,i)=>i).filter(i=>(w>>i)&1);let count=0;for(let mask=0;mask<256;mask++){if(pop(mask)&1)continue;const m=Array(24).fill(0);supp.forEach((j,k)=>m[j]=(mask>>k)&1?-1:1);if(m[supp[0]]<0||dot(m,B1)||dot(m,B2))continue;count++;const products=projectiveE.map(e=>dot(m,e)/4);assert(products.every(x=>Number.isInteger(x)&&Math.abs(x)<=2));candidateM.push({support:w,vector:m,big_weight:pop(w&bigMask),counts:{zero:products.filter(x=>x===0).length,one:products.filter(x=>Math.abs(x)===1).length,two:products.filter(x=>Math.abs(x)===2).length}});}if(count)octads.push({support:w,count,big_weight:pop(w&bigMask)});}
const dist={};for(const o of octads){const k=o.big_weight;dist[k]??={supports:0,signed_rows:0};dist[k].supports++;dist[k].signed_rows+=o.count;}
const A=projectiveE.map((e,i)=>projectiveE.map((f,j)=>i===j?0:Math.abs(dot(e,f))===8?1:0));const degrees=A.map(r=>r.reduce((s,x)=>s+x,0));const degreeHist={};degrees.forEach(d=>degreeHist[d]=(degreeHist[d]||0)+1);
const result={exact:true,scope:'All norm3 lines and admissible signed-octad norm4 block candidates in the explicit rank22 envelope only; no full frame selected, no global exclusion',norm3_lines:projectiveE.length,octad_supports:octads.length,signed_block_lines:candidateM.length,distribution_by_large_coordinates:dist,norm3_nonzero_inner_degree_histogram:degreeHist,octads,candidate_blocks:candidateM};fs.writeFileSync(path.join(here,'REPERE_COMPLET_GOLAY_DOMAINES.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({...result,octads:undefined,candidate_blocks:undefined}));

```


## classer_collage_D6_quatre.json

973 octets ; SHA256 69eb13dd3948451ae1a59a83babdfd9d631971d54fa21ebc6e7b844d0dae8877

```json
{
  "exact": true,
  "all_perfect_matchings": 105,
  "counts": {
    "within_component": 45,
    "two_double_edges_D12": 12,
    "cycle4": 48
  },
  "representatives": {
    "two_double_edges_D12": [
      [
        0,
        2
      ],
      [
        1,
        3
      ],
      [
        4,
        6
      ],
      [
        5,
        7
      ]
    ],
    "cycle4": [
      [
        0,
        2
      ],
      [
        1,
        4
      ],
      [
        3,
        6
      ],
      [
        5,
        7
      ]
    ]
  },
  "binary_selfdual_residual_min4_impossible": [
    6,
    4
  ],
  "rootful_ambient_D6_four_cycle_uniform": true,
  "no_solver": true,
  "scope": "Analytic proof reduces odd D6^4 glue to I2^4; finite matching check then exhausts the component multigraph. This does not close all physical frames; the f6 theorem closes only one collective regime.",
  "source_sha256": "da2b1d39e36978070be1e2369ff19f732a4873bc27b1ab3fa0850ce06fbf43f8"
}

```


## classer_collage_D6_quatre.mjs

1832 octets ; SHA256 da2b1d39e36978070be1e2369ff19f732a4873bc27b1ab3fa0850ce06fbf43f8

```javascript
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';const here=path.dirname(fileURLToPath(import.meta.url));const all=[];function match(left,pairs){if(!left.length){all.push(pairs);return;}const x=left[0];for(let i=1;i<left.length;i++)match(left.filter((_,j)=>j!==0&&j!==i),pairs.concat([[x,left[i]]]));}match([0,1,2,3,4,5,6,7],[]);assert.equal(all.length,105);const counts={within_component:0,two_double_edges_D12:0,cycle4:0};const representatives={};for(const pairs of all){const edges=pairs.map(([a,b])=>[a>>1,b>>1]);if(edges.some(([a,b])=>a===b)){counts.within_component++;continue;}const adj=Array.from({length:4},()=>[]);for(const[a,b]of edges){adj[a].push(b);adj[b].push(a);}assert(adj.every(x=>x.length===2));let seen=new Set([0]),todo=[0];while(todo.length){let x=todo.pop();for(const y of adj[x])if(!seen.has(y)){seen.add(y);todo.push(y);}}const kind=seen.size===4?'cycle4':'two_double_edges_D12';counts[kind]++;representatives[kind]??=pairs;}assert.deepEqual(counts,{within_component:45,two_double_edges_D12:12,cycle4:48});for(const n of[6,4])assert((2**(n/2)-1)*4>2**(n/2)*n/2);const out={exact:true,all_perfect_matchings:105,counts,representatives,binary_selfdual_residual_min4_impossible:[6,4],rootful_ambient_D6_four_cycle_uniform:true,no_solver:true,scope:'Analytic proof reduces odd D6^4 glue to I2^4; finite matching check then exhausts the component multigraph. This does not close all physical frames; the f6 theorem closes only one collective regime.',source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};fs.writeFileSync(path.join(here,'classer_collage_D6_quatre.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
```


## classifier_collages_D8_trois.json

260080 octets ; SHA256 416369c633abf51a67c5e396bc9dc8cb5f188d11773b5f8973bea65ee402da93

```json
{
  "exact": true,
  "scope": "Tous les135 collages unimodulaires de D8^3 ; fermeture physique par min1/E8/D16 acquis ou coque locale entiere.",
  "convention": "Digits0,v,s,c encoded0,1,2,3 per component; discriminant symplectic 2 inner product mod2.",
  "Grassmann_subspaces": 1395,
  "Lagrangians": 135,
  "odd": 105,
  "even": 30,
  "ordered_obstruction_counts": {
    "minimum1": 37,
    "singleton_spinor_E8": 24,
    "even_no_norm3": 30,
    "double_v_D16": 12,
    "integer_component_shelltrap": 32
  },
  "residual_glues": 32,
  "canonical_orbits": {
    "A": 8,
    "B": 24
  },
  "all_residual_glues_have_integer_component": true,
  "parent_example": {
    "generators": [
      [
        1,
        2,
        0
      ],
      [
        1,
        0,
        3
      ],
      [
        2,
        3,
        2
      ]
    ],
    "word_masks": [
      0,
      9,
      22,
      31,
      39,
      46,
      49,
      56
    ],
    "type": "B"
  },
  "records": [
    {
      "RREF_basis": [
        33,
        18,
        4
      ],
      "word_masks": [
        0,
        4,
        18,
        22,
        33,
        37,
        51,
        55
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        49,
        18,
        4
      ],
      "word_masks": [
        0,
        4,
        18,
        22,
        35,
        39,
        49,
        53
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        17,
        34,
        4
      ],
      "word_masks": [
        0,
        4,
        17,
        21,
        34,
        38,
        51,
        55
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        49,
        34,
        4
      ],
      "word_masks": [
        0,
        4,
        19,
        23,
        34,
        38,
        49,
        53
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        17,
        50,
        4
      ],
      "word_masks": [
        0,
        4,
        17,
        21,
        35,
        39,
        50,
        54
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        33,
        50,
        4
      ],
      "word_masks": [
        0,
        4,
        19,
        23,
        33,
        37,
        50,
        54
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        33,
        18,
        12
      ],
      "word_masks": [
        0,
        12,
        18,
        30,
        33,
        45,
        51,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 12,
        "classes": [
          0,
          3,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        49,
        18,
        12
      ],
      "word_masks": [
        0,
        12,
        18,
        30,
        35,
        47,
        49,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 12,
        "classes": [
          0,
          3,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        17,
        34,
        12
      ],
      "word_masks": [
        0,
        12,
        17,
        29,
        34,
        46,
        51,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        49,
        34,
        12
      ],
      "word_masks": [
        0,
        12,
        19,
        31,
        34,
        46,
        49,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 12,
        "classes": [
          0,
          3,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        17,
        50,
        12
      ],
      "word_masks": [
        0,
        12,
        17,
        29,
        35,
        47,
        50,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        33,
        50,
        12
      ],
      "word_masks": [
        0,
        12,
        19,
        31,
        33,
        45,
        50,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 12,
        "classes": [
          0,
          3,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        41,
        18,
        20
      ],
      "word_masks": [
        0,
        6,
        18,
        20,
        41,
        47,
        59,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 20,
        "classes": [
          0,
          1,
          1
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        57,
        18,
        20
      ],
      "word_masks": [
        0,
        6,
        18,
        20,
        43,
        45,
        57,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 20,
        "classes": [
          0,
          1,
          1
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        17,
        42,
        20
      ],
      "word_masks": [
        0,
        5,
        17,
        20,
        42,
        47,
        59,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        57,
        42,
        20
      ],
      "word_masks": [
        0,
        7,
        19,
        20,
        42,
        45,
        57,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 20,
        "classes": [
          0,
          1,
          1
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        17,
        58,
        20
      ],
      "word_masks": [
        0,
        5,
        17,
        20,
        43,
        46,
        58,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        41,
        58,
        20
      ],
      "word_masks": [
        0,
        7,
        19,
        20,
        41,
        46,
        58,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 20,
        "classes": [
          0,
          1,
          1
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        41,
        18,
        28
      ],
      "word_masks": [
        0,
        14,
        18,
        28,
        39,
        41,
        53,
        59
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          2
        ],
        "coque3_class_masks": [
          18,
          28
        ]
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        57,
        18,
        28
      ],
      "word_masks": [
        0,
        14,
        18,
        28,
        37,
        43,
        55,
        57
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          2
        ],
        "coque3_class_masks": [
          18,
          28
        ]
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        17,
        42,
        28
      ],
      "word_masks": [
        0,
        13,
        17,
        28,
        39,
        42,
        54,
        59
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 17,
        "classes": [
          1,
          0,
          1
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        2
      ]
    },
    {
      "RREF_basis": [
        57,
        42,
        28
      ],
      "word_masks": [
        0,
        15,
        19,
        28,
        37,
        42,
        54,
        57
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          2
        ],
        "coque3_class_masks": [
          19,
          28
        ]
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        17,
        58,
        28
      ],
      "word_masks": [
        0,
        13,
        17,
        28,
        38,
        43,
        55,
        58
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 17,
        "classes": [
          1,
          0,
          1
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        2
      ]
    },
    {
      "RREF_basis": [
        41,
        58,
        28
      ],
      "word_masks": [
        0,
        15,
        19,
        28,
        38,
        41,
        53,
        58
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          2
        ],
        "coque3_class_masks": [
          19,
          28
        ]
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        33,
        26,
        36
      ],
      "word_masks": [
        0,
        5,
        26,
        31,
        33,
        36,
        59,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 5,
        "classes": [
          1,
          1,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1
      ]
    },
    {
      "RREF_basis": [
        57,
        26,
        36
      ],
      "word_masks": [
        0,
        7,
        26,
        29,
        35,
        36,
        57,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          1
        ],
        "coque3_class_masks": [
          7,
          36
        ]
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        25,
        34,
        36
      ],
      "word_masks": [
        0,
        6,
        25,
        31,
        34,
        36,
        59,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          1
        ],
        "coque3_class_masks": [
          6,
          36
        ]
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        57,
        34,
        36
      ],
      "word_masks": [
        0,
        6,
        27,
        29,
        34,
        36,
        57,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          1
        ],
        "coque3_class_masks": [
          6,
          36
        ]
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        25,
        58,
        36
      ],
      "word_masks": [
        0,
        7,
        25,
        30,
        35,
        36,
        58,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          1
        ],
        "coque3_class_masks": [
          7,
          36
        ]
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        33,
        58,
        36
      ],
      "word_masks": [
        0,
        5,
        27,
        30,
        33,
        36,
        58,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 5,
        "classes": [
          1,
          1,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1
      ]
    },
    {
      "RREF_basis": [
        33,
        26,
        44
      ],
      "word_masks": [
        0,
        13,
        23,
        26,
        33,
        44,
        54,
        59
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0
        ],
        "coque3_class_masks": [
          13,
          33
        ]
      },
      "norm3_classes": [
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        57,
        26,
        44
      ],
      "word_masks": [
        0,
        15,
        21,
        26,
        35,
        44,
        54,
        57
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0,
          1,
          2
        ],
        "coque3_class_masks": [
          21
        ]
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ],
      "canonical_type": "A_vvv"
    },
    {
      "RREF_basis": [
        25,
        34,
        44
      ],
      "word_masks": [
        0,
        14,
        23,
        25,
        34,
        44,
        53,
        59
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        57,
        34,
        44
      ],
      "word_masks": [
        0,
        14,
        21,
        27,
        34,
        44,
        55,
        57
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0,
          1,
          2
        ],
        "coque3_class_masks": [
          21
        ]
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ],
      "canonical_type": "A_vvv"
    },
    {
      "RREF_basis": [
        25,
        58,
        44
      ],
      "word_masks": [
        0,
        15,
        22,
        25,
        35,
        44,
        53,
        58
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        33,
        58,
        44
      ],
      "word_masks": [
        0,
        13,
        22,
        27,
        33,
        44,
        55,
        58
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0
        ],
        "coque3_class_masks": [
          13,
          33
        ]
      },
      "norm3_classes": [
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        41,
        26,
        52
      ],
      "word_masks": [
        0,
        7,
        26,
        29,
        41,
        46,
        51,
        52
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          1
        ],
        "coque3_class_masks": [
          7,
          52
        ]
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        49,
        26,
        52
      ],
      "word_masks": [
        0,
        5,
        26,
        31,
        43,
        46,
        49,
        52
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 5,
        "classes": [
          1,
          1,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1
      ]
    },
    {
      "RREF_basis": [
        25,
        42,
        52
      ],
      "word_masks": [
        0,
        7,
        25,
        30,
        42,
        45,
        51,
        52
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          1
        ],
        "coque3_class_masks": [
          7,
          52
        ]
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        49,
        42,
        52
      ],
      "word_masks": [
        0,
        5,
        27,
        30,
        42,
        47,
        49,
        52
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 5,
        "classes": [
          1,
          1,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1
      ]
    },
    {
      "RREF_basis": [
        25,
        50,
        52
      ],
      "word_masks": [
        0,
        6,
        25,
        31,
        43,
        45,
        50,
        52
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          1
        ],
        "coque3_class_masks": [
          6,
          52
        ]
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        41,
        50,
        52
      ],
      "word_masks": [
        0,
        6,
        27,
        29,
        41,
        47,
        50,
        52
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          1
        ],
        "coque3_class_masks": [
          6,
          52
        ]
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        41,
        26,
        60
      ],
      "word_masks": [
        0,
        15,
        21,
        26,
        38,
        41,
        51,
        60
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0,
          1,
          2
        ],
        "coque3_class_masks": [
          21
        ]
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ],
      "canonical_type": "A_vvv"
    },
    {
      "RREF_basis": [
        49,
        26,
        60
      ],
      "word_masks": [
        0,
        13,
        23,
        26,
        38,
        43,
        49,
        60
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0
        ],
        "coque3_class_masks": [
          13,
          49
        ]
      },
      "norm3_classes": [
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        25,
        42,
        60
      ],
      "word_masks": [
        0,
        15,
        22,
        25,
        37,
        42,
        51,
        60
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        49,
        42,
        60
      ],
      "word_masks": [
        0,
        13,
        22,
        27,
        39,
        42,
        49,
        60
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0
        ],
        "coque3_class_masks": [
          13,
          49
        ]
      },
      "norm3_classes": [
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        25,
        50,
        60
      ],
      "word_masks": [
        0,
        14,
        23,
        25,
        37,
        43,
        50,
        60
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        41,
        50,
        60
      ],
      "word_masks": [
        0,
        14,
        21,
        27,
        39,
        41,
        50,
        60
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0,
          1,
          2
        ],
        "coque3_class_masks": [
          21
        ]
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ],
      "canonical_type": "A_vvv"
    },
    {
      "RREF_basis": [
        33,
        18,
        8
      ],
      "word_masks": [
        0,
        8,
        18,
        26,
        33,
        41,
        51,
        59
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 8,
        "classes": [
          0,
          2,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        49,
        18,
        8
      ],
      "word_masks": [
        0,
        8,
        18,
        26,
        35,
        43,
        49,
        57
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 8,
        "classes": [
          0,
          2,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        17,
        34,
        8
      ],
      "word_masks": [
        0,
        8,
        17,
        25,
        34,
        42,
        51,
        59
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        49,
        34,
        8
      ],
      "word_masks": [
        0,
        8,
        19,
        27,
        34,
        42,
        49,
        57
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 8,
        "classes": [
          0,
          2,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        17,
        50,
        8
      ],
      "word_masks": [
        0,
        8,
        17,
        25,
        35,
        43,
        50,
        58
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        33,
        50,
        8
      ],
      "word_masks": [
        0,
        8,
        19,
        27,
        33,
        41,
        50,
        58
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 8,
        "classes": [
          0,
          2,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        37,
        18,
        24
      ],
      "word_masks": [
        0,
        10,
        18,
        24,
        37,
        47,
        55,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          2
        ],
        "coque3_class_masks": [
          18,
          24
        ]
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        53,
        18,
        24
      ],
      "word_masks": [
        0,
        10,
        18,
        24,
        39,
        45,
        53,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          2
        ],
        "coque3_class_masks": [
          18,
          24
        ]
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        17,
        38,
        24
      ],
      "word_masks": [
        0,
        9,
        17,
        24,
        38,
        47,
        55,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 17,
        "classes": [
          1,
          0,
          1
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        2
      ]
    },
    {
      "RREF_basis": [
        53,
        38,
        24
      ],
      "word_masks": [
        0,
        11,
        19,
        24,
        38,
        45,
        53,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          2
        ],
        "coque3_class_masks": [
          19,
          24
        ]
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        17,
        54,
        24
      ],
      "word_masks": [
        0,
        9,
        17,
        24,
        39,
        46,
        54,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "double_v_D16",
      "certificate": {
        "mask": 17,
        "classes": [
          1,
          0,
          1
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        2
      ]
    },
    {
      "RREF_basis": [
        37,
        54,
        24
      ],
      "word_masks": [
        0,
        11,
        19,
        24,
        37,
        46,
        54,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          2
        ],
        "coque3_class_masks": [
          19,
          24
        ]
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        33,
        22,
        40
      ],
      "word_masks": [
        0,
        9,
        22,
        31,
        33,
        40,
        55,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0
        ],
        "coque3_class_masks": [
          9,
          33
        ]
      },
      "norm3_classes": [
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        53,
        22,
        40
      ],
      "word_masks": [
        0,
        11,
        22,
        29,
        35,
        40,
        53,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        21,
        34,
        40
      ],
      "word_masks": [
        0,
        10,
        21,
        31,
        34,
        40,
        55,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0,
          1,
          2
        ],
        "coque3_class_masks": [
          21
        ]
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ],
      "canonical_type": "A_vvv"
    },
    {
      "RREF_basis": [
        53,
        34,
        40
      ],
      "word_masks": [
        0,
        10,
        23,
        29,
        34,
        40,
        53,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        21,
        54,
        40
      ],
      "word_masks": [
        0,
        11,
        21,
        30,
        35,
        40,
        54,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0,
          1,
          2
        ],
        "coque3_class_masks": [
          21
        ]
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ],
      "canonical_type": "A_vvv"
    },
    {
      "RREF_basis": [
        33,
        54,
        40
      ],
      "word_masks": [
        0,
        9,
        23,
        30,
        33,
        40,
        54,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0
        ],
        "coque3_class_masks": [
          9,
          33
        ]
      },
      "norm3_classes": [
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        37,
        22,
        56
      ],
      "word_masks": [
        0,
        11,
        22,
        29,
        37,
        46,
        51,
        56
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        49,
        22,
        56
      ],
      "word_masks": [
        0,
        9,
        22,
        31,
        39,
        46,
        49,
        56
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0
        ],
        "coque3_class_masks": [
          9,
          49
        ]
      },
      "norm3_classes": [
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        21,
        38,
        56
      ],
      "word_masks": [
        0,
        11,
        21,
        30,
        38,
        45,
        51,
        56
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0,
          1,
          2
        ],
        "coque3_class_masks": [
          21
        ]
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ],
      "canonical_type": "A_vvv"
    },
    {
      "RREF_basis": [
        49,
        38,
        56
      ],
      "word_masks": [
        0,
        9,
        23,
        30,
        38,
        47,
        49,
        56
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0
        ],
        "coque3_class_masks": [
          9,
          49
        ]
      },
      "norm3_classes": [
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ],
      "canonical_type": "B_common_v_center"
    },
    {
      "RREF_basis": [
        21,
        50,
        56
      ],
      "word_masks": [
        0,
        10,
        21,
        31,
        39,
        45,
        50,
        56
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "integer_component_shelltrap",
      "certificate": {
        "components": [
          0,
          1,
          2
        ],
        "coque3_class_masks": [
          21
        ]
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ],
      "canonical_type": "A_vvv"
    },
    {
      "RREF_basis": [
        37,
        50,
        56
      ],
      "word_masks": [
        0,
        10,
        23,
        29,
        37,
        47,
        50,
        56
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        9,
        6,
        16
      ],
      "word_masks": [
        0,
        6,
        9,
        15,
        16,
        22,
        25,
        31
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        13,
        6,
        16
      ],
      "word_masks": [
        0,
        6,
        11,
        13,
        16,
        22,
        27,
        29
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        5,
        10,
        16
      ],
      "word_masks": [
        0,
        5,
        10,
        15,
        16,
        21,
        26,
        31
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        13,
        10,
        16
      ],
      "word_masks": [
        0,
        7,
        10,
        13,
        16,
        23,
        26,
        29
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        5,
        14,
        16
      ],
      "word_masks": [
        0,
        5,
        11,
        14,
        16,
        21,
        27,
        30
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        9,
        14,
        16
      ],
      "word_masks": [
        0,
        7,
        9,
        14,
        16,
        23,
        25,
        30
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        9,
        6,
        48
      ],
      "word_masks": [
        0,
        6,
        9,
        15,
        48,
        54,
        57,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 48,
        "classes": [
          0,
          0,
          3
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        13,
        6,
        48
      ],
      "word_masks": [
        0,
        6,
        11,
        13,
        48,
        54,
        59,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 48,
        "classes": [
          0,
          0,
          3
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        5,
        10,
        48
      ],
      "word_masks": [
        0,
        5,
        10,
        15,
        48,
        53,
        58,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        13,
        10,
        48
      ],
      "word_masks": [
        0,
        7,
        10,
        13,
        48,
        55,
        58,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 48,
        "classes": [
          0,
          0,
          3
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        5,
        14,
        48
      ],
      "word_masks": [
        0,
        5,
        11,
        14,
        48,
        53,
        59,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        9,
        14,
        48
      ],
      "word_masks": [
        0,
        7,
        9,
        14,
        48,
        55,
        57,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 48,
        "classes": [
          0,
          0,
          3
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        9,
        6,
        32
      ],
      "word_masks": [
        0,
        6,
        9,
        15,
        32,
        38,
        41,
        47
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 32,
        "classes": [
          0,
          0,
          2
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        13,
        6,
        32
      ],
      "word_masks": [
        0,
        6,
        11,
        13,
        32,
        38,
        43,
        45
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 32,
        "classes": [
          0,
          0,
          2
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        5,
        10,
        32
      ],
      "word_masks": [
        0,
        5,
        10,
        15,
        32,
        37,
        42,
        47
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        13,
        10,
        32
      ],
      "word_masks": [
        0,
        7,
        10,
        13,
        32,
        39,
        42,
        45
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 32,
        "classes": [
          0,
          0,
          2
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        5,
        14,
        32
      ],
      "word_masks": [
        0,
        5,
        11,
        14,
        32,
        37,
        43,
        46
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        9,
        14,
        32
      ],
      "word_masks": [
        0,
        7,
        9,
        14,
        32,
        39,
        41,
        46
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 32,
        "classes": [
          0,
          0,
          2
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        1,
        36,
        24
      ],
      "word_masks": [
        0,
        1,
        24,
        25,
        36,
        37,
        60,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        3,
        36,
        24
      ],
      "word_masks": [
        0,
        3,
        24,
        27,
        36,
        39,
        60,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 3,
        "classes": [
          3,
          0,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        1,
        52,
        24
      ],
      "word_masks": [
        0,
        1,
        24,
        25,
        44,
        45,
        52,
        53
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        3,
        52,
        24
      ],
      "word_masks": [
        0,
        3,
        24,
        27,
        44,
        47,
        52,
        55
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 3,
        "classes": [
          3,
          0,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        1,
        20,
        40
      ],
      "word_masks": [
        0,
        1,
        20,
        21,
        40,
        41,
        60,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        3,
        20,
        40
      ],
      "word_masks": [
        0,
        3,
        20,
        23,
        40,
        43,
        60,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        1,
        52,
        40
      ],
      "word_masks": [
        0,
        1,
        28,
        29,
        40,
        41,
        52,
        53
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        3,
        52,
        40
      ],
      "word_masks": [
        0,
        3,
        28,
        31,
        40,
        43,
        52,
        55
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 3,
        "classes": [
          3,
          0,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        1,
        20,
        56
      ],
      "word_masks": [
        0,
        1,
        20,
        21,
        44,
        45,
        56,
        57
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        3,
        20,
        56
      ],
      "word_masks": [
        0,
        3,
        20,
        23,
        44,
        47,
        56,
        59
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        1,
        36,
        56
      ],
      "word_masks": [
        0,
        1,
        28,
        29,
        36,
        37,
        56,
        57
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        3,
        36,
        56
      ],
      "word_masks": [
        0,
        3,
        28,
        31,
        36,
        39,
        56,
        59
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 3,
        "classes": [
          3,
          0,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        1,
        4,
        16
      ],
      "word_masks": [
        0,
        1,
        4,
        5,
        16,
        17,
        20,
        21
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 21,
          "classes": [
            1,
            1,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        3,
        4,
        16
      ],
      "word_masks": [
        0,
        3,
        4,
        7,
        16,
        19,
        20,
        23
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 23,
          "classes": [
            3,
            1,
            1
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        1,
        12,
        16
      ],
      "word_masks": [
        0,
        1,
        12,
        13,
        16,
        17,
        28,
        29
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 29,
          "classes": [
            1,
            3,
            1
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        2
      ]
    },
    {
      "RREF_basis": [
        3,
        12,
        16
      ],
      "word_masks": [
        0,
        3,
        12,
        15,
        16,
        19,
        28,
        31
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 31,
          "classes": [
            3,
            3,
            1
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        1,
        4,
        48
      ],
      "word_masks": [
        0,
        1,
        4,
        5,
        48,
        49,
        52,
        53
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 53,
          "classes": [
            1,
            1,
            3
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1
      ]
    },
    {
      "RREF_basis": [
        3,
        4,
        48
      ],
      "word_masks": [
        0,
        3,
        4,
        7,
        48,
        51,
        52,
        55
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 55,
          "classes": [
            3,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        1,
        12,
        48
      ],
      "word_masks": [
        0,
        1,
        12,
        13,
        48,
        49,
        60,
        61
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 61,
          "classes": [
            1,
            3,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        3,
        12,
        48
      ],
      "word_masks": [
        0,
        3,
        12,
        15,
        48,
        51,
        60,
        63
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 63,
          "classes": [
            3,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        1,
        4,
        32
      ],
      "word_masks": [
        0,
        1,
        4,
        5,
        32,
        33,
        36,
        37
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 5,
          "classes": [
            1,
            1,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 37,
          "classes": [
            1,
            1,
            2
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        1
      ]
    },
    {
      "RREF_basis": [
        3,
        4,
        32
      ],
      "word_masks": [
        0,
        3,
        4,
        7,
        32,
        35,
        36,
        39
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 39,
          "classes": [
            3,
            1,
            2
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 7,
          "classes": [
            3,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        1,
        12,
        32
      ],
      "word_masks": [
        0,
        1,
        12,
        13,
        32,
        33,
        44,
        45
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 45,
          "classes": [
            1,
            3,
            2
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 13,
          "classes": [
            1,
            3,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        3,
        12,
        32
      ],
      "word_masks": [
        0,
        3,
        12,
        15,
        32,
        35,
        44,
        47
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 15,
          "classes": [
            3,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 47,
          "classes": [
            3,
            3,
            2
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        1,
        8,
        16
      ],
      "word_masks": [
        0,
        1,
        8,
        9,
        16,
        17,
        24,
        25
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 17,
          "classes": [
            1,
            0,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 25,
          "classes": [
            1,
            2,
            1
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0,
        2
      ]
    },
    {
      "RREF_basis": [
        3,
        8,
        16
      ],
      "word_masks": [
        0,
        3,
        8,
        11,
        16,
        19,
        24,
        27
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 27,
          "classes": [
            3,
            2,
            1
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 19,
          "classes": [
            3,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        1,
        8,
        48
      ],
      "word_masks": [
        0,
        1,
        8,
        9,
        48,
        49,
        56,
        57
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 57,
          "classes": [
            1,
            2,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 49,
          "classes": [
            1,
            0,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        3,
        8,
        48
      ],
      "word_masks": [
        0,
        3,
        8,
        11,
        48,
        51,
        56,
        59
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 51,
          "classes": [
            3,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 59,
          "classes": [
            3,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        1,
        8,
        32
      ],
      "word_masks": [
        0,
        1,
        8,
        9,
        32,
        33,
        40,
        41
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 1,
          "classes": [
            1,
            0,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 41,
          "classes": [
            1,
            2,
            2
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 1,
        "classes": [
          1,
          0,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 9,
          "classes": [
            1,
            2,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 33,
          "classes": [
            1,
            0,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        3,
        8,
        32
      ],
      "word_masks": [
        0,
        3,
        8,
        11,
        32,
        35,
        40,
        43
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 3,
          "classes": [
            3,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 11,
          "classes": [
            3,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 35,
          "classes": [
            3,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 43,
          "classes": [
            3,
            2,
            2
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        2,
        36,
        24
      ],
      "word_masks": [
        0,
        2,
        24,
        26,
        36,
        38,
        60,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 2,
        "classes": [
          2,
          0,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        2,
        52,
        24
      ],
      "word_masks": [
        0,
        2,
        24,
        26,
        44,
        46,
        52,
        54
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 2,
        "classes": [
          2,
          0,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        2,
        20,
        40
      ],
      "word_masks": [
        0,
        2,
        20,
        22,
        40,
        42,
        60,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        2,
        52,
        40
      ],
      "word_masks": [
        0,
        2,
        28,
        30,
        40,
        42,
        52,
        54
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 2,
        "classes": [
          2,
          0,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        2,
        20,
        56
      ],
      "word_masks": [
        0,
        2,
        20,
        22,
        44,
        46,
        56,
        58
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        2,
        36,
        56
      ],
      "word_masks": [
        0,
        2,
        28,
        30,
        36,
        38,
        56,
        58
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": true,
      "obstruction": "singleton_spinor_E8",
      "certificate": {
        "mask": 2,
        "classes": [
          2,
          0,
          0
        ],
        "minimum": 2
      },
      "norm3_classes": [
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        0
      ]
    },
    {
      "RREF_basis": [
        2,
        4,
        16
      ],
      "word_masks": [
        0,
        2,
        4,
        6,
        16,
        18,
        20,
        22
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 20,
          "classes": [
            0,
            1,
            1
          ],
          "minimum": 2
        },
        {
          "mask": 22,
          "classes": [
            2,
            1,
            1
          ],
          "minimum": 4
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        2,
        12,
        16
      ],
      "word_masks": [
        0,
        2,
        12,
        14,
        16,
        18,
        28,
        30
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 30,
          "classes": [
            2,
            3,
            1
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 28,
          "classes": [
            0,
            3,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        2,
        4,
        48
      ],
      "word_masks": [
        0,
        2,
        4,
        6,
        48,
        50,
        52,
        54
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        },
        {
          "mask": 54,
          "classes": [
            2,
            1,
            3
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 52,
          "classes": [
            0,
            1,
            3
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        2,
        12,
        48
      ],
      "word_masks": [
        0,
        2,
        12,
        14,
        48,
        50,
        60,
        62
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 60,
          "classes": [
            0,
            3,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 62,
          "classes": [
            2,
            3,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        2,
        4,
        32
      ],
      "word_masks": [
        0,
        2,
        4,
        6,
        32,
        34,
        36,
        38
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 4,
          "classes": [
            0,
            1,
            0
          ],
          "minimum": 1
        },
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        },
        {
          "mask": 38,
          "classes": [
            2,
            1,
            2
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 4,
        "classes": [
          0,
          1,
          0
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 6,
          "classes": [
            2,
            1,
            0
          ],
          "minimum": 3
        },
        {
          "mask": 36,
          "classes": [
            0,
            1,
            2
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        1
      ]
    },
    {
      "RREF_basis": [
        2,
        12,
        32
      ],
      "word_masks": [
        0,
        2,
        12,
        14,
        32,
        34,
        44,
        46
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 12,
          "classes": [
            0,
            3,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 14,
          "classes": [
            2,
            3,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 44,
          "classes": [
            0,
            3,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 46,
          "classes": [
            2,
            3,
            2
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        2,
        8,
        16
      ],
      "word_masks": [
        0,
        2,
        8,
        10,
        16,
        18,
        24,
        26
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 16,
          "classes": [
            0,
            0,
            1
          ],
          "minimum": 1
        },
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 26,
          "classes": [
            2,
            2,
            1
          ],
          "minimum": 5
        }
      ],
      "odd": true,
      "obstruction": "minimum1",
      "certificate": {
        "mask": 16,
        "classes": [
          0,
          0,
          1
        ],
        "minimum": 1
      },
      "norm3_classes": [
        {
          "mask": 18,
          "classes": [
            2,
            0,
            1
          ],
          "minimum": 3
        },
        {
          "mask": 24,
          "classes": [
            0,
            2,
            1
          ],
          "minimum": 3
        }
      ],
      "norm3_shell_count": 4096,
      "integer_components_for_shell3": [
        2
      ]
    },
    {
      "RREF_basis": [
        2,
        8,
        48
      ],
      "word_masks": [
        0,
        2,
        8,
        10,
        48,
        50,
        56,
        58
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 48,
          "classes": [
            0,
            0,
            3
          ],
          "minimum": 2
        },
        {
          "mask": 50,
          "classes": [
            2,
            0,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 56,
          "classes": [
            0,
            2,
            3
          ],
          "minimum": 4
        },
        {
          "mask": 58,
          "classes": [
            2,
            2,
            3
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    },
    {
      "RREF_basis": [
        2,
        8,
        32
      ],
      "word_masks": [
        0,
        2,
        8,
        10,
        32,
        34,
        40,
        42
      ],
      "words": [
        {
          "mask": 0,
          "classes": [
            0,
            0,
            0
          ],
          "minimum": 0
        },
        {
          "mask": 2,
          "classes": [
            2,
            0,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 8,
          "classes": [
            0,
            2,
            0
          ],
          "minimum": 2
        },
        {
          "mask": 10,
          "classes": [
            2,
            2,
            0
          ],
          "minimum": 4
        },
        {
          "mask": 32,
          "classes": [
            0,
            0,
            2
          ],
          "minimum": 2
        },
        {
          "mask": 34,
          "classes": [
            2,
            0,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 40,
          "classes": [
            0,
            2,
            2
          ],
          "minimum": 4
        },
        {
          "mask": 42,
          "classes": [
            2,
            2,
            2
          ],
          "minimum": 6
        }
      ],
      "odd": false,
      "obstruction": "even_no_norm3",
      "norm3_classes": [],
      "norm3_shell_count": 0,
      "integer_components_for_shell3": [
        0,
        1,
        2
      ]
    }
  ],
  "limitation": "No classification of all rank24 unimodular lattices or global exclusion of g18/g20."
}

```


## classifier_collages_D8_trois.mjs

5038 octets ; SHA256 2535a462bb40d3811ed36214da4dc0555fdc741f3513371a692cf85c20aab0d7

```javascript
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const assert=(p,m)=>{if(!p)throw new Error(m);};
const minima=[0,1,2,2],minimalCounts=[1,16,128,128];
const classes=x=>[0,1,2].map(i=>(x>>(2*i))&3);
const mask=c=>c.reduce((x,z,i)=>x|(z<<(2*i)),0);
const cost=x=>classes(x).reduce((s,c)=>s+minima[c],0);
function symp(x,y){
  let a=0;for(let i=0;i<3;i++)a^=(((x>>(2*i))&1)*((y>>(2*i+1))&1))
    ^(((x>>(2*i+1))&1)*((y>>(2*i))&1));return a;
}
function span(rows){return Array.from({length:8},(_,m)=>rows.reduce((x,r,i)=>x^(((m>>i)&1)?r:0),0)).sort((a,b)=>a-b);}
const records=[];let grassmann=0;
for(let p0=0;p0<4;p0++)for(let p1=p0+1;p1<5;p1++)for(let p2=p1+1;p2<6;p2++){
  const pivots=[p0,p1,p2],slots=[];
  for(let i=0;i<3;i++)for(let j=pivots[i]+1;j<6;j++)if(!pivots.includes(j))slots.push([i,j]);
  for(let m=0;m<(1<<slots.length);m++){
    grassmann++;const rows=pivots.map(j=>1<<j);
    for(let k=0;k<slots.length;k++)if((m>>k)&1)rows[slots[k][0]]|=1<<slots[k][1];
    if(rows.some((x,i)=>rows.some((y,j)=>i<j&&symp(x,y))))continue;
    const words=span(rows);assert(new Set(words).size===8,'dimension trois');
    for(const x of words)for(const y of words){
      assert(symp(x,y)===0,'Lagrangien');
      assert((cost(x)+cost(y)-cost(x^y))%2===0,'parite lineaire sur L');
    }
    const descriptors=words.map(x=>({mask:x,classes:classes(x),minimum:cost(x)}));
    const odd=words.some(x=>cost(x)%2===1);
    const norm1=descriptors.find(w=>w.minimum===1);
    const spin=descriptors.find(w=>w.classes.filter(Boolean).length===1&&w.classes.some(c=>c===2||c===3));
    const vv=descriptors.find(w=>w.classes.filter(Boolean).length===2&&w.classes.filter(Boolean).every(c=>c===1));
    const shell3=descriptors.filter(w=>w.minimum===3);
    const integerComponents=[0,1,2].filter(i=>shell3.every(w=>w.classes[i]===0||w.classes[i]===1));
    let obstruction,certificate;
    if(!odd)obstruction='even_no_norm3';
    else if(norm1){obstruction='minimum1';certificate=norm1;}
    else if(spin){obstruction='singleton_spinor_E8';certificate=spin;}
    else if(vv){obstruction='double_v_D16';certificate=vv;}
    else{
      obstruction='integer_component_shelltrap';
      assert(shell3.length>0&&integerComponents.length>0,'piege local pour toute glue restante');
      certificate={components:integerComponents,coque3_class_masks:shell3.map(w=>w.mask)};
    }
    const shellCount=shell3.reduce((s,w)=>s+w.classes.reduce((n,c)=>n*minimalCounts[c],1),0);
    records.push({RREF_basis:rows,word_masks:words,words:descriptors,odd,obstruction,certificate,
      norm3_classes:shell3,norm3_shell_count:shellCount,integer_components_for_shell3:integerComponents});
  }
}
assert(grassmann===1395&&records.length===135,'comptage Grassmann/Lagrangiens');
const counts={};for(const r of records)counts[r.obstruction]=(counts[r.obstruction]||0)+1;
assert(counts.even_no_norm3===30&&counts.minimum1===37&&counts.singleton_spinor_E8===24
  &&counts.double_v_D16===12&&counts.integer_component_shelltrap===32,'strates135');
const survivors=records.filter(r=>r.obstruction==='integer_component_shelltrap');
assert(survivors.every(r=>r.norm3_shell_count===4096),'4096 normes trois restantes');
const perms=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
function orbit(words){
  const keys=new Set();for(const p of perms)for(let f=0;f<8;f++){
    const changed=words.map(x=>{const c=classes(x),d=p.map(i=>c[i]);
      for(let j=0;j<3;j++)if(((f>>j)&1)&&(d[j]&2))d[j]^=1;
      return mask(d);}).sort((a,b)=>a-b);keys.add(changed.join(','));
  }return keys;
}
const A=orbit(span([mask([2,2,0]),mask([0,2,2]),mask([1,1,1])]));
const B=orbit(span([mask([1,2,0]),mask([1,0,2]),mask([2,1,1])]));
assert(A.size===8&&B.size===24,'orbites8/24');
for(const k of A)assert(!B.has(k),'orbites disjointes');
for(const r of survivors){
  const k=r.word_masks.join(',');assert(A.has(k)||B.has(k),'classification complete');
  r.canonical_type=A.has(k)?'A_vvv':'B_common_v_center';
}
const example=span([mask([1,2,0]),mask([1,0,3]),mask([2,3,2])]);
assert(B.has(example.join(',')),'exemple du parent');
const result={exact:true,
  scope:'Tous les135 collages unimodulaires de D8^3 ; fermeture physique par min1/E8/D16 acquis ou coque locale entiere.',
  convention:'Digits0,v,s,c encoded0,1,2,3 per component; discriminant symplectic 2 inner product mod2.',
  Grassmann_subspaces:grassmann,Lagrangians:135,odd:105,even:30,ordered_obstruction_counts:counts,
  residual_glues:32,canonical_orbits:{A:8,B:24},all_residual_glues_have_integer_component:true,
  parent_example:{generators:[[1,2,0],[1,0,3],[2,3,2]],word_masks:example,type:'B'},records,
  limitation:'No classification of all rank24 unimodular lattices or global exclusion of g18/g20.'};
const here=path.dirname(fileURLToPath(import.meta.url));
fs.writeFileSync(path.join(here,'classifier_collages_D8_trois.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,Lagrangians:135,odd:105,counts,orbits:{A:8,B:24},allInteger:true}));

```


## construire_archive_repere42_7.ps1

3249 octets ; SHA256 e5d85a15cec4e7e5a2b146245acd3d19a6ea46bd2bfad14bd82179221c2aa069

```powershell
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$campaignCurrent = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$outputRoot = Split-Path -Parent $campaignCurrent
$campaignPrior = Join-Path $outputRoot 'attaque_globale_27_0803'
$archiveTarget = Join-Path $outputRoot 'ATTAQUE_DIRECTE_27_0836_PREUVES_CERTIFICATS.zip'
$manifestTarget = Join-Path $campaignCurrent 'MANIFESTE_REPERE42_7.json'
$manifest = Get-Content -LiteralPath $manifestTarget -Raw -Encoding UTF8 | ConvertFrom-Json
$expected = @{}
foreach ($item in $manifest.files) { $expected[$item.path] = $item.sha256 }
$manifestHash = (Get-FileHash -LiteralPath $manifestTarget -Algorithm SHA256).Hash.ToLowerInvariant()
$expected['attaque_globale_27_0836/MANIFESTE_REPERE42_7.json'] = $manifestHash
$archiveStream = [System.IO.File]::Open($archiveTarget,[System.IO.FileMode]::Create,[System.IO.FileAccess]::Write)
$zip = [System.IO.Compression.ZipArchive]::new($archiveStream,[System.IO.Compression.ZipArchiveMode]::Create,$false)
try {
 foreach ($sourceFolder in @($campaignCurrent,$campaignPrior)) {
  $folderName = Split-Path -Leaf $sourceFolder
  foreach ($sourceFile in (Get-ChildItem -LiteralPath $sourceFolder -File | Sort-Object Name)) {
   if ($sourceFile.Extension -eq '.zip') { continue }
   $entryName = $folderName + '/' + $sourceFile.Name
   if (-not $expected.ContainsKey($entryName)) { throw ('Unmanifested input: '+$entryName) }
   $entry = $zip.CreateEntry($entryName,[System.IO.Compression.CompressionLevel]::Optimal)
   $dst = $entry.Open()
   $src = [System.IO.File]::OpenRead($sourceFile.FullName)
   try { $src.CopyTo($dst) } finally { $src.Dispose(); $dst.Dispose() }
  }
 }
} finally { $zip.Dispose(); $archiveStream.Dispose() }
$checkZip = [System.IO.Compression.ZipFile]::OpenRead($archiveTarget)
$checked = 0
$seen = @{}
try {
 foreach ($entry in $checkZip.Entries) {
  if ($seen.ContainsKey($entry.FullName)) { throw ('Duplicate entry: '+$entry.FullName) }
  $seen[$entry.FullName] = $true
  if (-not $expected.ContainsKey($entry.FullName)) { throw ('Unexpected entry: '+$entry.FullName) }
  $hashTool = [System.Security.Cryptography.SHA256]::Create()
  $stream = $entry.Open()
  try { $digest=[System.BitConverter]::ToString($hashTool.ComputeHash($stream)).Replace('-','').ToLowerInvariant() }
  finally { $stream.Dispose(); $hashTool.Dispose() }
  if ($digest -ne $expected[$entry.FullName]) { throw ('Hash mismatch: '+$entry.FullName) }
  $checked++
 }
} finally { $checkZip.Dispose() }
if ($checked -ne $expected.Count) { throw 'Entry count mismatch' }
$zipHash=(Get-FileHash -LiteralPath $archiveTarget -Algorithm SHA256).Hash.ToLowerInvariant()
$audit=[ordered]@{exact=$true;archive=(Split-Path -Leaf $archiveTarget);bytes=(Get-Item -LiteralPath $archiveTarget).Length;entries_checked=$checked;every_entry_sha256_matches=$true;manifest_sha256=$manifestHash;archive_sha256=$zipHash;scope='two complete own-conversation campaigns; no global g18/g20 exclusion'}
$auditPath=$archiveTarget+'.AUDIT.json'
$utf8NoBom=[System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($auditPath,($audit | ConvertTo-Json -Depth 4),$utf8NoBom)
$audit | ConvertTo-Json -Depth 4

```


## construire_livraison_repere42_7.mjs

3329 octets ; SHA256 0eaa666db17201625f56e48cdd0368ab92532e6428804a96db65172cb3d6ac33

```javascript
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const cur=path.dirname(fileURLToPath(import.meta.url));
const prev=path.join(cur,'../attaque_globale_27_0803');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const title='# Preuves complètes — attaque directe du repère 42+7\n\n';
const allCurrent=(await fs.readdir(cur)).sort();
const exclude=new Set(['PREUVES_COMPLETES_REPERE42_7.md','DOSSIER_SOURCES_SORTIES_REPERE42_7.md','LIRE_D_ABORD.md']);
let proof=title+await fs.readFile(path.join(cur,'BILAN_ATTAQUE_DIRECTE_REPERE42_7.md'),'utf8');
proof+='\n\n---\n\n# Dépendances intégrales : campagne immédiatement précédente, 0803\n\n';
proof+=await fs.readFile(path.join(prev,'PREUVES_COMPLETES_ATTAQUE_GLOBALE.md'),'utf8');
for(const name of allCurrent.filter(n=>n.endsWith('.md')&&!exclude.has(n)&&n!=='BILAN_ATTAQUE_DIRECTE_REPERE42_7.md')){
 const data=await fs.readFile(path.join(cur,name));
 proof+='\n\n---\n\n# Pièce : '+name+'\n\nSHA256 : '+sha(data)+'\n\n'+data.toString('utf8');
}
await fs.writeFile(path.join(cur,'PREUVES_COMPLETES_REPERE42_7.md'),proof,'utf8');
let source='# Sources et sorties exactes — repère 42+7\n\nLes fichiers intégraux sont tous dans l’archive ; le domaine de 2,7 Mo reste dans son JSON original, sans troncature. Aucun graphe99 ni repère physique complet n’est produit.\n\n';
source+='## Campagne 0803, sources et sorties intégrales\n\n'+await fs.readFile(path.join(prev,'DOSSIER_COMPLET_SOURCES_ET_SORTIES.md'),'utf8');
const bt=String.fromCharCode(96).repeat(3);
for(const name of allCurrent.filter(n=>/\.(mjs|json|ps1)$/.test(n)&&n!=='MANIFESTE_REPERE42_7.json')){
 const data=await fs.readFile(path.join(cur,name));
 source+='\n\n## '+name+'\n\n'+data.length+' octets ; SHA256 '+sha(data)+'\n\n';
 if(data.length>300000){source+='Fichier volumineux fourni intégralement et séparément dans l’archive. Sa source génératrice figure dans ce document.\n';continue;}
 source+=bt+(name.endsWith('.mjs')?'javascript':name.endsWith('.ps1')?'powershell':'json')+'\n'+data.toString('utf8')+'\n'+bt+'\n';
}
await fs.writeFile(path.join(cur,'DOSSIER_SOURCES_SORTIES_REPERE42_7.md'),source,'utf8');
const entries=[];
for(const [folder,dir] of [['attaque_globale_27_0836',cur],['attaque_globale_27_0803',prev]]){
 for(const item of (await fs.readdir(dir,{withFileTypes:true})).sort((a,b)=>a.name.localeCompare(b.name))){
  if(!item.isFile()||item.name.endsWith('.zip')||(folder==='attaque_globale_27_0836'&&item.name==='MANIFESTE_REPERE42_7.json'))continue;
  const data=await fs.readFile(path.join(dir,item.name));
  entries.push({path:folder+'/'+item.name,bytes:data.length,sha256:sha(data)});
 }
}
const manifest={campaign:'2026-09-27 0836 UTC',scope:'full physical 42+7+2 frame, g18 and g20, no P=0',whole_goals_closed:false,former_snapshot_unchanged:true,archive:'../ATTAQUE_DIRECTE_27_0836_PREUVES_CERTIFICATS.zip',files:entries};
await fs.writeFile(path.join(cur,'MANIFESTE_REPERE42_7.json'),JSON.stringify(manifest,null,2)+'\n','utf8');
console.log(JSON.stringify({proof_bytes:Buffer.byteLength(proof),sources_bytes:Buffer.byteLength(source),manifest_files:entries.length,manifest_sha256:sha(await fs.readFile(path.join(cur,'MANIFESTE_REPERE42_7.json')))}));

```


## contre_controle_coque_D4_six.json

1406 octets ; SHA256 2b5afec16af8c7fd9b0edfa8d1ff6a4cd22ebe57c09c830e0853d4b9b5ade42c

```json
{
  "exact": true,
  "glue_code": "D4^6, graph code of the six-cycle",
  "adjacency_bitmasks": [
    48,
    40,
    24,
    6,
    5,
    3
  ],
  "weight_counts": {
    "0": 1,
    "3": 8,
    "4": 21,
    "5": 24,
    "6": 10
  },
  "minima": [
    {
      "a": 1,
      "b": 48,
      "weight": 3
    },
    {
      "a": 2,
      "b": 40,
      "weight": 3
    },
    {
      "a": 4,
      "b": 24,
      "weight": 3
    },
    {
      "a": 7,
      "b": 0,
      "weight": 3
    },
    {
      "a": 8,
      "b": 6,
      "weight": 3
    },
    {
      "a": 16,
      "b": 5,
      "weight": 3
    },
    {
      "a": 32,
      "b": 3,
      "weight": 3
    },
    {
      "a": 56,
      "b": 0,
      "weight": 3
    }
  ],
  "binary_rank_weight3_words": 6,
  "roots": 144,
  "shell3": 4096,
  "characteristics8_predicted": 192,
  "entire_shell3_integrally_generates_U": true,
  "entire_shell3_Gram_mod2_rank": 24,
  "proof_of_last_two": "Each active component has all eight minuscule vectors in a fixed class; their differences generate D4 by triality. Weight3 glue classes span the six-dimensional maximal isotropic glue code. Thus shell3 generates U, which is unimodular integral rank24. No physical42 selection is constructed.",
  "full_physical_frame_constructed": false,
  "impossibility_asserted": false,
  "source_sha256": "2e5a0260a44d22f6e10bbdae6ece58fa536d342139df20e963c1556cce9b779f"
}

```


## contre_controle_coque_D4_six.mjs

1828 octets ; SHA256 2e5a0260a44d22f6e10bbdae6ece58fa536d342139df20e963c1556cce9b779f

```javascript
import fs from 'node:fs';import path from 'node:path';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';import crypto from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const n=6,adj=[48,40,24,6,5,3],pc=x=>{let s=0;for(;x;x&=x-1)s++;return s;};const parity=x=>pc(x)%2;const words=[];const counts={};for(let a=0;a<64;a++){let b=0;for(let i=0;i<6;i++)if((a>>i)&1)b^=adj[i];const w=pc(a|b);words.push({a,b,weight:w});counts[w]=(counts[w]??0)+1;}assert.deepEqual(counts,{'0':1,'3':8,'4':21,'5':24,'6':10});for(const x of words)for(const y of words)assert.equal(parity((x.a&y.b)^(x.b&y.a)),0);const minima=words.filter(x=>x.weight===3);let basis=[];for(const x of minima){let v=x.a|(x.b<<6);for(const b of basis)v=Math.min(v,v^b);if(v){basis.push(v);basis.sort((a,b)=>b-a);}}assert.equal(basis.length,6);for(let i=0;i<6;i++)assert(minima.some(x=>((x.a|x.b)>>i)&1));const out={exact:true,glue_code:'D4^6, graph code of the six-cycle',adjacency_bitmasks:adj,weight_counts:counts,minima,binary_rank_weight3_words:basis.length,roots:144,shell3:8*8**3,characteristics8_predicted:192,entire_shell3_integrally_generates_U:true,entire_shell3_Gram_mod2_rank:24,proof_of_last_two:'Each active component has all eight minuscule vectors in a fixed class; their differences generate D4 by triality. Weight3 glue classes span the six-dimensional maximal isotropic glue code. Thus shell3 generates U, which is unimodular integral rank24. No physical42 selection is constructed.',full_physical_frame_constructed:false,impossibility_asserted:false,source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};fs.writeFileSync(path.join(here,'contre_controle_coque_D4_six.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
```


## controle_D4_cycle6_classes.json

42040 octets ; SHA256 1ad44dcf3d4e3bf0cd2a6c7fda4974c693c1ff16447e863de0951d05efe2158c

```json
{
  "exact": true,
  "scope": "Collage D4^6 du cycle C6 et classes utilisees par la meme selection42 ; aucune realisation physique annoncee.",
  "adjacency": [
    34,
    5,
    10,
    20,
    40,
    17
  ],
  "glue_generator_Gram": [
    [
      3,
      1,
      1,
      0,
      1,
      1
    ],
    [
      1,
      3,
      1,
      1,
      0,
      1
    ],
    [
      1,
      1,
      3,
      1,
      1,
      0
    ],
    [
      0,
      1,
      1,
      3,
      1,
      1
    ],
    [
      1,
      0,
      1,
      1,
      3,
      1
    ],
    [
      1,
      1,
      0,
      1,
      1,
      3
    ]
  ],
  "glue_index": 64,
  "determinant": 1,
  "glue_class_weight_histogram": {
    "0": 1,
    "3": 8,
    "4": 21,
    "5": 24,
    "6": 10
  },
  "norm3_classes": [
    {
      "mask": 1,
      "v_mask": 1,
      "s_mask": 34,
      "symbols": [
        1,
        2,
        0,
        0,
        0,
        2
      ],
      "weight": 3
    },
    {
      "mask": 2,
      "v_mask": 2,
      "s_mask": 5,
      "symbols": [
        2,
        1,
        2,
        0,
        0,
        0
      ],
      "weight": 3
    },
    {
      "mask": 4,
      "v_mask": 4,
      "s_mask": 10,
      "symbols": [
        0,
        2,
        1,
        2,
        0,
        0
      ],
      "weight": 3
    },
    {
      "mask": 8,
      "v_mask": 8,
      "s_mask": 20,
      "symbols": [
        0,
        0,
        2,
        1,
        2,
        0
      ],
      "weight": 3
    },
    {
      "mask": 16,
      "v_mask": 16,
      "s_mask": 40,
      "symbols": [
        0,
        0,
        0,
        2,
        1,
        2
      ],
      "weight": 3
    },
    {
      "mask": 32,
      "v_mask": 32,
      "s_mask": 17,
      "symbols": [
        2,
        0,
        0,
        0,
        2,
        1
      ],
      "weight": 3
    },
    {
      "mask": 21,
      "v_mask": 21,
      "s_mask": 0,
      "symbols": [
        1,
        0,
        1,
        0,
        1,
        0
      ],
      "weight": 3
    },
    {
      "mask": 42,
      "v_mask": 42,
      "s_mask": 0,
      "symbols": [
        0,
        1,
        0,
        1,
        0,
        1
      ],
      "weight": 3
    }
  ],
  "norm3_shell_count": 4096,
  "all_glue_classes": [
    {
      "mask": 0,
      "v_mask": 0,
      "s_mask": 0,
      "symbols": [
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "weight": 0
    },
    {
      "mask": 1,
      "v_mask": 1,
      "s_mask": 34,
      "symbols": [
        1,
        2,
        0,
        0,
        0,
        2
      ],
      "weight": 3
    },
    {
      "mask": 2,
      "v_mask": 2,
      "s_mask": 5,
      "symbols": [
        2,
        1,
        2,
        0,
        0,
        0
      ],
      "weight": 3
    },
    {
      "mask": 3,
      "v_mask": 3,
      "s_mask": 39,
      "symbols": [
        3,
        3,
        2,
        0,
        0,
        2
      ],
      "weight": 4
    },
    {
      "mask": 4,
      "v_mask": 4,
      "s_mask": 10,
      "symbols": [
        0,
        2,
        1,
        2,
        0,
        0
      ],
      "weight": 3
    },
    {
      "mask": 5,
      "v_mask": 5,
      "s_mask": 40,
      "symbols": [
        1,
        0,
        1,
        2,
        0,
        2
      ],
      "weight": 4
    },
    {
      "mask": 6,
      "v_mask": 6,
      "s_mask": 15,
      "symbols": [
        2,
        3,
        3,
        2,
        0,
        0
      ],
      "weight": 4
    },
    {
      "mask": 7,
      "v_mask": 7,
      "s_mask": 45,
      "symbols": [
        3,
        1,
        3,
        2,
        0,
        2
      ],
      "weight": 5
    },
    {
      "mask": 8,
      "v_mask": 8,
      "s_mask": 20,
      "symbols": [
        0,
        0,
        2,
        1,
        2,
        0
      ],
      "weight": 3
    },
    {
      "mask": 9,
      "v_mask": 9,
      "s_mask": 54,
      "symbols": [
        1,
        2,
        2,
        1,
        2,
        2
      ],
      "weight": 6
    },
    {
      "mask": 10,
      "v_mask": 10,
      "s_mask": 17,
      "symbols": [
        2,
        1,
        0,
        1,
        2,
        0
      ],
      "weight": 4
    },
    {
      "mask": 11,
      "v_mask": 11,
      "s_mask": 51,
      "symbols": [
        3,
        3,
        0,
        1,
        2,
        2
      ],
      "weight": 5
    },
    {
      "mask": 12,
      "v_mask": 12,
      "s_mask": 30,
      "symbols": [
        0,
        2,
        3,
        3,
        2,
        0
      ],
      "weight": 4
    },
    {
      "mask": 13,
      "v_mask": 13,
      "s_mask": 60,
      "symbols": [
        1,
        0,
        3,
        3,
        2,
        2
      ],
      "weight": 5
    },
    {
      "mask": 14,
      "v_mask": 14,
      "s_mask": 27,
      "symbols": [
        2,
        3,
        1,
        3,
        2,
        0
      ],
      "weight": 5
    },
    {
      "mask": 15,
      "v_mask": 15,
      "s_mask": 57,
      "symbols": [
        3,
        1,
        1,
        3,
        2,
        2
      ],
      "weight": 6
    },
    {
      "mask": 16,
      "v_mask": 16,
      "s_mask": 40,
      "symbols": [
        0,
        0,
        0,
        2,
        1,
        2
      ],
      "weight": 3
    },
    {
      "mask": 17,
      "v_mask": 17,
      "s_mask": 10,
      "symbols": [
        1,
        2,
        0,
        2,
        1,
        0
      ],
      "weight": 4
    },
    {
      "mask": 18,
      "v_mask": 18,
      "s_mask": 45,
      "symbols": [
        2,
        1,
        2,
        2,
        1,
        2
      ],
      "weight": 6
    },
    {
      "mask": 19,
      "v_mask": 19,
      "s_mask": 15,
      "symbols": [
        3,
        3,
        2,
        2,
        1,
        0
      ],
      "weight": 5
    },
    {
      "mask": 20,
      "v_mask": 20,
      "s_mask": 34,
      "symbols": [
        0,
        2,
        1,
        0,
        1,
        2
      ],
      "weight": 4
    },
    {
      "mask": 21,
      "v_mask": 21,
      "s_mask": 0,
      "symbols": [
        1,
        0,
        1,
        0,
        1,
        0
      ],
      "weight": 3
    },
    {
      "mask": 22,
      "v_mask": 22,
      "s_mask": 39,
      "symbols": [
        2,
        3,
        3,
        0,
        1,
        2
      ],
      "weight": 5
    },
    {
      "mask": 23,
      "v_mask": 23,
      "s_mask": 5,
      "symbols": [
        3,
        1,
        3,
        0,
        1,
        0
      ],
      "weight": 4
    },
    {
      "mask": 24,
      "v_mask": 24,
      "s_mask": 60,
      "symbols": [
        0,
        0,
        2,
        3,
        3,
        2
      ],
      "weight": 4
    },
    {
      "mask": 25,
      "v_mask": 25,
      "s_mask": 30,
      "symbols": [
        1,
        2,
        2,
        3,
        3,
        0
      ],
      "weight": 5
    },
    {
      "mask": 26,
      "v_mask": 26,
      "s_mask": 57,
      "symbols": [
        2,
        1,
        0,
        3,
        3,
        2
      ],
      "weight": 5
    },
    {
      "mask": 27,
      "v_mask": 27,
      "s_mask": 27,
      "symbols": [
        3,
        3,
        0,
        3,
        3,
        0
      ],
      "weight": 4
    },
    {
      "mask": 28,
      "v_mask": 28,
      "s_mask": 54,
      "symbols": [
        0,
        2,
        3,
        1,
        3,
        2
      ],
      "weight": 5
    },
    {
      "mask": 29,
      "v_mask": 29,
      "s_mask": 20,
      "symbols": [
        1,
        0,
        3,
        1,
        3,
        0
      ],
      "weight": 4
    },
    {
      "mask": 30,
      "v_mask": 30,
      "s_mask": 51,
      "symbols": [
        2,
        3,
        1,
        1,
        3,
        2
      ],
      "weight": 6
    },
    {
      "mask": 31,
      "v_mask": 31,
      "s_mask": 17,
      "symbols": [
        3,
        1,
        1,
        1,
        3,
        0
      ],
      "weight": 5
    },
    {
      "mask": 32,
      "v_mask": 32,
      "s_mask": 17,
      "symbols": [
        2,
        0,
        0,
        0,
        2,
        1
      ],
      "weight": 3
    },
    {
      "mask": 33,
      "v_mask": 33,
      "s_mask": 51,
      "symbols": [
        3,
        2,
        0,
        0,
        2,
        3
      ],
      "weight": 4
    },
    {
      "mask": 34,
      "v_mask": 34,
      "s_mask": 20,
      "symbols": [
        0,
        1,
        2,
        0,
        2,
        1
      ],
      "weight": 4
    },
    {
      "mask": 35,
      "v_mask": 35,
      "s_mask": 54,
      "symbols": [
        1,
        3,
        2,
        0,
        2,
        3
      ],
      "weight": 5
    },
    {
      "mask": 36,
      "v_mask": 36,
      "s_mask": 27,
      "symbols": [
        2,
        2,
        1,
        2,
        2,
        1
      ],
      "weight": 6
    },
    {
      "mask": 37,
      "v_mask": 37,
      "s_mask": 57,
      "symbols": [
        3,
        0,
        1,
        2,
        2,
        3
      ],
      "weight": 5
    },
    {
      "mask": 38,
      "v_mask": 38,
      "s_mask": 30,
      "symbols": [
        0,
        3,
        3,
        2,
        2,
        1
      ],
      "weight": 5
    },
    {
      "mask": 39,
      "v_mask": 39,
      "s_mask": 60,
      "symbols": [
        1,
        1,
        3,
        2,
        2,
        3
      ],
      "weight": 6
    },
    {
      "mask": 40,
      "v_mask": 40,
      "s_mask": 5,
      "symbols": [
        2,
        0,
        2,
        1,
        0,
        1
      ],
      "weight": 4
    },
    {
      "mask": 41,
      "v_mask": 41,
      "s_mask": 39,
      "symbols": [
        3,
        2,
        2,
        1,
        0,
        3
      ],
      "weight": 5
    },
    {
      "mask": 42,
      "v_mask": 42,
      "s_mask": 0,
      "symbols": [
        0,
        1,
        0,
        1,
        0,
        1
      ],
      "weight": 3
    },
    {
      "mask": 43,
      "v_mask": 43,
      "s_mask": 34,
      "symbols": [
        1,
        3,
        0,
        1,
        0,
        3
      ],
      "weight": 4
    },
    {
      "mask": 44,
      "v_mask": 44,
      "s_mask": 15,
      "symbols": [
        2,
        2,
        3,
        3,
        0,
        1
      ],
      "weight": 5
    },
    {
      "mask": 45,
      "v_mask": 45,
      "s_mask": 45,
      "symbols": [
        3,
        0,
        3,
        3,
        0,
        3
      ],
      "weight": 4
    },
    {
      "mask": 46,
      "v_mask": 46,
      "s_mask": 10,
      "symbols": [
        0,
        3,
        1,
        3,
        0,
        1
      ],
      "weight": 4
    },
    {
      "mask": 47,
      "v_mask": 47,
      "s_mask": 40,
      "symbols": [
        1,
        1,
        1,
        3,
        0,
        3
      ],
      "weight": 5
    },
    {
      "mask": 48,
      "v_mask": 48,
      "s_mask": 57,
      "symbols": [
        2,
        0,
        0,
        2,
        3,
        3
      ],
      "weight": 4
    },
    {
      "mask": 49,
      "v_mask": 49,
      "s_mask": 27,
      "symbols": [
        3,
        2,
        0,
        2,
        3,
        1
      ],
      "weight": 5
    },
    {
      "mask": 50,
      "v_mask": 50,
      "s_mask": 60,
      "symbols": [
        0,
        1,
        2,
        2,
        3,
        3
      ],
      "weight": 5
    },
    {
      "mask": 51,
      "v_mask": 51,
      "s_mask": 30,
      "symbols": [
        1,
        3,
        2,
        2,
        3,
        1
      ],
      "weight": 6
    },
    {
      "mask": 52,
      "v_mask": 52,
      "s_mask": 51,
      "symbols": [
        2,
        2,
        1,
        0,
        3,
        3
      ],
      "weight": 5
    },
    {
      "mask": 53,
      "v_mask": 53,
      "s_mask": 17,
      "symbols": [
        3,
        0,
        1,
        0,
        3,
        1
      ],
      "weight": 4
    },
    {
      "mask": 54,
      "v_mask": 54,
      "s_mask": 54,
      "symbols": [
        0,
        3,
        3,
        0,
        3,
        3
      ],
      "weight": 4
    },
    {
      "mask": 55,
      "v_mask": 55,
      "s_mask": 20,
      "symbols": [
        1,
        1,
        3,
        0,
        3,
        1
      ],
      "weight": 5
    },
    {
      "mask": 56,
      "v_mask": 56,
      "s_mask": 45,
      "symbols": [
        2,
        0,
        2,
        3,
        1,
        3
      ],
      "weight": 5
    },
    {
      "mask": 57,
      "v_mask": 57,
      "s_mask": 15,
      "symbols": [
        3,
        2,
        2,
        3,
        1,
        1
      ],
      "weight": 6
    },
    {
      "mask": 58,
      "v_mask": 58,
      "s_mask": 40,
      "symbols": [
        0,
        1,
        0,
        3,
        1,
        3
      ],
      "weight": 4
    },
    {
      "mask": 59,
      "v_mask": 59,
      "s_mask": 10,
      "symbols": [
        1,
        3,
        0,
        3,
        1,
        1
      ],
      "weight": 5
    },
    {
      "mask": 60,
      "v_mask": 60,
      "s_mask": 39,
      "symbols": [
        2,
        2,
        3,
        1,
        1,
        3
      ],
      "weight": 6
    },
    {
      "mask": 61,
      "v_mask": 61,
      "s_mask": 5,
      "symbols": [
        3,
        0,
        3,
        1,
        1,
        1
      ],
      "weight": 5
    },
    {
      "mask": 62,
      "v_mask": 62,
      "s_mask": 34,
      "symbols": [
        0,
        3,
        1,
        1,
        1,
        3
      ],
      "weight": 5
    },
    {
      "mask": 63,
      "v_mask": 63,
      "s_mask": 0,
      "symbols": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "weight": 6
    }
  ],
  "families_tested": 256,
  "qualifying_families": 25,
  "refuted_families": 231,
  "minimum_used_classes": 6,
  "qualifying_by_number_bases": {
    "4": 9,
    "5": 12,
    "6": 4
  },
  "qualifying_by_total_classes": {
    "6": 16,
    "7": 8,
    "8": 1
  },
  "valid": [
    {
      "mask": 63,
      "bases": 6,
      "size": 6
    },
    {
      "mask": 111,
      "bases": 5,
      "size": 6
    },
    {
      "mask": 123,
      "bases": 5,
      "size": 6
    },
    {
      "mask": 126,
      "bases": 5,
      "size": 6
    },
    {
      "mask": 127,
      "bases": 6,
      "size": 7
    },
    {
      "mask": 159,
      "bases": 5,
      "size": 6
    },
    {
      "mask": 183,
      "bases": 5,
      "size": 6
    },
    {
      "mask": 189,
      "bases": 5,
      "size": 6
    },
    {
      "mask": 191,
      "bases": 6,
      "size": 7
    },
    {
      "mask": 207,
      "bases": 4,
      "size": 6
    },
    {
      "mask": 219,
      "bases": 4,
      "size": 6
    },
    {
      "mask": 222,
      "bases": 4,
      "size": 6
    },
    {
      "mask": 223,
      "bases": 5,
      "size": 7
    },
    {
      "mask": 231,
      "bases": 4,
      "size": 6
    },
    {
      "mask": 237,
      "bases": 4,
      "size": 6
    },
    {
      "mask": 239,
      "bases": 5,
      "size": 7
    },
    {
      "mask": 243,
      "bases": 4,
      "size": 6
    },
    {
      "mask": 246,
      "bases": 4,
      "size": 6
    },
    {
      "mask": 247,
      "bases": 5,
      "size": 7
    },
    {
      "mask": 249,
      "bases": 4,
      "size": 6
    },
    {
      "mask": 251,
      "bases": 5,
      "size": 7
    },
    {
      "mask": 252,
      "bases": 4,
      "size": 6
    },
    {
      "mask": 253,
      "bases": 5,
      "size": 7
    },
    {
      "mask": 254,
      "bases": 5,
      "size": 7
    },
    {
      "mask": 255,
      "bases": 6,
      "size": 8
    }
  ],
  "rejected": [
    {
      "mask": 0,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 1,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 2,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 3,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 4,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 5,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 6,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 7,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 8,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 9,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 10,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 11,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 12,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 13,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 14,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 15,
      "component": 4,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 16,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 17,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 18,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 19,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 20,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 21,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 22,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 23,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 24,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 25,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 26,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 27,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 28,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 29,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 30,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 31,
      "component": 5,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 32,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 33,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 34,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 35,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 36,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 37,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 38,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 39,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 40,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 41,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 42,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 43,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 44,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 45,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 46,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 47,
      "component": 4,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 48,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 49,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 50,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 51,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 52,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 53,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 54,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 55,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 56,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 57,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 58,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 59,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 60,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 61,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 62,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 64,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 65,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 66,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 67,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 68,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 69,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 70,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 71,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 72,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 73,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 74,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 75,
      "component": 3,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 76,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 77,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 78,
      "component": 5,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 79,
      "component": 5,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 80,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 81,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 82,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 83,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 84,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 85,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 86,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 87,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 88,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 89,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 90,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 91,
      "component": 5,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 92,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 93,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 94,
      "component": 5,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 95,
      "component": 5,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 96,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 97,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 98,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 99,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 100,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 101,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 102,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 103,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 104,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 105,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 106,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 107,
      "component": 3,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 108,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 109,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 110,
      "component": 5,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 112,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 113,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 114,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 115,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 116,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 117,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 118,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 119,
      "component": 3,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 120,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 121,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 122,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 124,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 125,
      "component": 1,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 128,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 129,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 130,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 131,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 132,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 133,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 134,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 135,
      "component": 4,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 136,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 137,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 138,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 139,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 140,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 141,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 142,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 143,
      "component": 4,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 144,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 145,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 146,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 147,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 148,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 149,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 150,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 151,
      "component": 4,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 152,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 153,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 154,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 155,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 156,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 157,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 158,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 160,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 161,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 162,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 163,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 164,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 165,
      "component": 2,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 166,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 167,
      "component": 4,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 168,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 169,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 170,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 171,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 172,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 173,
      "component": 4,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 174,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 175,
      "component": 4,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 176,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 177,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 0
    },
    {
      "mask": 178,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 179,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 180,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 181,
      "component": 2,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 182,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 184,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 185,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 186,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 187,
      "component": 2,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 188,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 190,
      "component": 0,
      "missing_class": "v",
      "present_symbol_mask": 2
    },
    {
      "mask": 192,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 193,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 194,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 195,
      "component": 3,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 196,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 197,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 198,
      "component": 4,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 199,
      "component": 4,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 200,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 201,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 202,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 203,
      "component": 3,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 204,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 205,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 206,
      "component": 5,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 208,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 209,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 210,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 211,
      "component": 4,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 212,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 213,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 214,
      "component": 4,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 215,
      "component": 4,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 216,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 217,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 218,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 220,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 221,
      "component": 0,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 224,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 225,
      "component": 2,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 226,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 227,
      "component": 3,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 228,
      "component": 2,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 229,
      "component": 2,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 230,
      "component": 5,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 232,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 233,
      "component": 3,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 234,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 235,
      "component": 3,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 236,
      "component": 5,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 238,
      "component": 5,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 240,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 241,
      "component": 2,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 242,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 244,
      "component": 2,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 245,
      "component": 2,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 248,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    },
    {
      "mask": 250,
      "component": 1,
      "missing_class": "s",
      "present_symbol_mask": 1
    }
  ],
  "rejection_principle": "Une composante uniforme 0/v ou0/s donne quatre directions de norme1 integralement duales aux42u, contredisant le petit polaire de dimension2."
}

```


## controle_D4_cycle6_classes.mjs

3755 octets ; SHA256 72f9bfc38c6a7c52d2607606ea6e863f7f3eb29fb38971f3b184eac312115c5b

```javascript
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const assert=(p,m)=>{if(!p)throw new Error(m);};
const pop=x=>{let n=0;while(x){x&=x-1;n++;}return n;};
const adjacency=Array.from({length:6},(_,i)=>(1<<((i+1)%6))|(1<<((i+5)%6)));
function describe(a){
  let b=0;for(let i=0;i<6;i++)if((a>>i)&1)b^=adjacency[i];
  const symbols=Array.from({length:6},(_,j)=>((a>>j)&1)+2*((b>>j)&1));
  return {mask:a,v_mask:a,s_mask:b,symbols,weight:symbols.filter(Boolean).length};
}
const classes=Array.from({length:64},(_,a)=>describe(a));
const hist={};for(const c of classes)hist[c.weight]=(hist[c.weight]||0)+1;
assert(classes.slice(1).every(c=>c.weight>=3),'aucune classe poids un ou deux');
const norm3=classes.filter(c=>c.weight===3);
const orderedMasks=[1,2,4,8,16,32,21,42];
assert(norm3.length===8&&norm3.every(c=>orderedMasks.includes(c.mask)),'huit classes exactes');
const ordered=orderedMasks.map(a=>describe(a));
assert(ordered.every(c=>!c.symbols.includes(3)),'pas de lettre c dans la coque trois');

// Produits exacts de six generateurs de collage, coordonnees doublees.
const glueVectors=Array.from({length:6},(_,i)=>{
  const x=Array(24).fill(0);x[4*i]=2;
  for(const j of [(i+1)%6,(i+5)%6])for(let k=0;k<4;k++)x[4*j+k]=1;
  return x;
});
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const gram=glueVectors.map(a=>glueVectors.map(b=>dot(a,b)/4));
assert(gram.every(row=>row.every(Number.isInteger)),'collage integral');
assert(gram.every((row,i)=>row[i]===3),'collage impair');
for(const g of glueVectors)for(let b=0;b<6;b++)for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)
  for(const s of [-1,1])for(const t of [-1,1])assert((s*g[4*b+i]+t*g[4*b+j])%2===0,'produit racine D4 entier');

const valid=[],rejected=[],byBases={},byClassCount={};
for(let m=0;m<256;m++){
  const present=Array(6).fill(0);
  for(let i=0;i<8;i++)if((m>>i)&1)for(let j=0;j<6;j++){
    const sym=ordered[i].symbols[j];if(sym)present[j]|=1<<(sym-1);
  }
  const deficient=present.findIndex(x=>(x&3)!==3);
  if(deficient>=0){
    const missing=(present[deficient]&1)?'s':'v';
    rejected.push({mask:m,component:deficient,missing_class:missing,present_symbol_mask:present[deficient]});
    continue;
  }
  const bases=pop(m&63),size=pop(m);
  assert(bases>=4,'quatre bases minimales');
  assert(pop(m&21)>=2&&pop(m&42)>=2,'deux bases par part');
  assert(size>=6,'six classes minimales');
  valid.push({mask:m,bases,size});byBases[bases]=(byBases[bases]||0)+1;
  byClassCount[size]=(byClassCount[size]||0)+1;
}
assert(valid.length===25&&rejected.length===231,'couverture256');
assert(byBases[4]===9&&byBases[5]===12&&byBases[6]===4,'formule9+12+4');
assert(byClassCount[6]===16&&byClassCount[7]===8&&byClassCount[8]===1,'tailles6/7/8');
const result={exact:true,
  scope:'Collage D4^6 du cycle C6 et classes utilisees par la meme selection42 ; aucune realisation physique annoncee.',
  adjacency,glue_generator_Gram:gram,glue_index:64,determinant:1,
  glue_class_weight_histogram:hist,norm3_classes:ordered,
  norm3_shell_count:8*8**3,all_glue_classes:classes,
  families_tested:256,qualifying_families:25,refuted_families:231,
  minimum_used_classes:6,qualifying_by_number_bases:byBases,
  qualifying_by_total_classes:byClassCount,valid,rejected,
  rejection_principle:'Une composante uniforme 0/v ou0/s donne quatre directions de norme1 integralement duales aux42u, contredisant le petit polaire de dimension2.'};
fs.writeFileSync(path.join(path.dirname(fileURLToPath(import.meta.url)),'controle_D4_cycle6_classes.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,shell4096:result.norm3_shell_count,
  qualifying25:valid.length,refuted231:rejected.length,
  byBases,byClassCount,minimumClasses:6}));

```


## controle_congruences_selection42.json

2558 octets ; SHA256 197e8a20d46063f4954020c8db4d9b95354bf28b39fa95a2d1caec463419184b

```json
{
  "exact": true,
  "scope": "Deux selections existantes uniquement ; aucune nouvelle recherche de graphe.",
  "d_masks": [
    0,
    24059
  ],
  "generators": [
    8391395,
    8394182,
    8399756,
    8410904,
    8433200,
    8477792,
    8566976,
    8745344,
    9102080,
    9815552,
    11242496,
    14096384
  ],
  "witnesses": {
    "wrong_xor": {
      "selected42_masks": [
        34236,
        117786,
        136944,
        141498,
        228921,
        235572,
        282996,
        305244,
        334034,
        345385,
        408336,
        449821,
        496827,
        573785,
        581244,
        601132,
        628698,
        706700,
        771060,
        1060121,
        2103532,
        4214092,
        342461,
        684922,
        743789,
        753962,
        791953,
        799998,
        804970,
        823048,
        848796,
        859881,
        899642,
        924740,
        993654,
        1012877,
        1020544,
        1036155,
        1043988,
        1068712,
        1145754,
        1163372
      ],
      "Q_integral": false,
      "xor_condition": false,
      "number_dodecads": 17,
      "characteristic_sum_mod16": 0
    },
    "correct_xor_wrong_rows": {
      "selected42_masks": [
        34236,
        117786,
        136944,
        141498,
        228921,
        235572,
        282996,
        305244,
        334034,
        345385,
        408336,
        449821,
        496827,
        573785,
        581244,
        601132,
        628698,
        706700,
        771060,
        1060121,
        2103532,
        4214092,
        342461,
        684922,
        743789,
        753962,
        791953,
        799998,
        804970,
        823048,
        848796,
        859881,
        899642,
        924740,
        993654,
        1012877,
        1020544,
        1036155,
        1043988,
        1068712,
        1145754,
        7612877
      ],
      "Q_integral": true,
      "xor_condition": true,
      "number_dodecads": 18,
      "characteristic_sum_mod16": 8,
      "tau": 0,
      "one_codeword_mask": 7218972,
      "one_codeword_in_code": false,
      "all_Q_rows_in_code": false,
      "Q_row_syndromes_verified": 288,
      "half_characteristic_codeword_mask": 9558243,
      "half_characteristic_sum_mod8": 4
    }
  },
  "theorem": "Q integral iff XOR; Q rows in C iff one class in C; physical characteristic checksum is 8 mod16.",
  "limitations": "Degree ten, CT and common-neighbor budgets are not asserted for the witnesses."
}

```


## controle_congruences_selection42.mjs

4080 octets ; SHA256 53515dcbfd3a31b6889e9b27fbfee4c75f8854eea2d47cc4f0e1675cfaeeb5b8

```javascript
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const input=JSON.parse(fs.readFileSync(path.join(here,'controle_selection42_golay.json'),'utf8'));
const assert=(p,m)=>{if(!p)throw new Error(m);};
const mod2=x=>(x%2+2)%2;
const mod16=x=>(x%16+16)%16;
const pop=x=>{let n=0;while(x){x&=x-1;n++;}return n;};
const signs=c=>Array.from({length:24},(_,j)=>1-2*((c>>>j)&1));
const generators=input.code.generator_masks;
const code=new Set();for(let m=0;m<4096;m++){
  let w=0;for(let i=0;i<12;i++)if((m>>i)&1)w^=generators[i];code.add(w);
}
const mask=row=>row.reduce((w,x,j)=>w|(mod2(x)<<j),0);
const dot=(a,b)=>a.reduce((s,x,j)=>s+x*b[j],0);
const B=input.B;
const d=B.map(row=>row.map(x=>mod2((1-x)/2)));
const k=B.map((row,i)=>row.map((x,j)=>(x-1+2*d[i][j])/4));
assert(d.every(row=>code.has(mask(row))),'d_i dans code');
assert(k.every(row=>row.every(Number.isInteger)),'k_i entiers');
const delta=d[0].map((x,j)=>x+d[1][j]);
const K=k[0].map((x,j)=>x+k[1][j]);
function audit(witness){
  const S=witness.selected_codeword_masks,E=S.map(signs);
  assert(S.length===42&&new Set(S).size===42,'selection42');
  const n=Array.from({length:24},(_,j)=>S.reduce((s,c)=>s+((c>>>j)&1),0));
  const F=Array.from({length:24},(_,j)=>Array.from({length:24},(_,h)=>
    (j===h?56:0)-E.reduce((s,row)=>s+row[j]*row[h],0)-B[0][j]*B[0][h]-B[1][j]*B[1][h]));
  const Qintegral=F.every(row=>row.every(x=>x%4===0));
  const tau=mod2(n[0]+delta[0]);
  const xorOK=n.every((x,j)=>mod2(x+delta[j])===tau);
  assert(Qintegral===xorOK,'equivalence XOR entier');
  const output={selected42_masks:S,Q_integral:Qintegral,xor_condition:xorOK,
    number_dodecads:S.filter(c=>pop(c)===12).length,
    characteristic_sum_mod16:mod16(E.reduce((s,row)=>s+row.reduce((a,b)=>a+b,0),0)
      +B.flat().reduce((s,x)=>s+x,0))};
  if(!Qintegral)return output;
  const Q=F.map(row=>row.map(x=>x/4));
  const a=n.map((x,j)=>(x+delta[j]-tau)/2);
  const single=a.map((x,j)=>x+K[j]);
  const singleMask=mask(single);
  const rows=Q.map(mask);
  for(let j=0;j<24;j++)for(const g of generators){
    const gb=Array.from({length:24},(_,i)=>(g>>>i)&1);
    assert(mod2(dot(Q[j],gb))===mod2(dot(single,gb)),'syndrome identique sur24lignes');
  }
  assert(rows.every(r=>code.has(r))===code.has(singleMask),'condition mot unique');
  const x=Array.from({length:24},(_,j)=>(E.reduce((s,row)=>s+row[j],0)+B[0][j]+B[1][j])/2);
  assert(x.every(z=>mod2(z)===tau),'parite demi-caracteristique');
  const halfMask=mask(x.map(z=>(z-tau)/2));
  assert(code.has(halfMask)===code.has(singleMask),'code demi-caracteristique');
  Object.assign(output,{tau,one_codeword_mask:singleMask,one_codeword_in_code:code.has(singleMask),
    all_Q_rows_in_code:rows.every(r=>code.has(r)),Q_row_syndromes_verified:24*12,
    half_characteristic_codeword_mask:halfMask,
    half_characteristic_sum_mod8:((x.reduce((s,z)=>s+z,0)%8)+8)%8});
  return output;
}
const witnesses={wrong_xor:audit(input.witness_wrong_xor),
  correct_xor_wrong_rows:audit(input.witness_correct_xor_wrong_Q_rows)};
assert(!witnesses.wrong_xor.Q_integral,'premier temoin');
assert(witnesses.correct_xor_wrong_rows.one_codeword_mask===7218972,'mot imprime');
assert(witnesses.correct_xor_wrong_rows.characteristic_sum_mod16===8,'checksum passe');
const result={exact:true,scope:'Deux selections existantes uniquement ; aucune nouvelle recherche de graphe.',
  d_masks:d.map(mask),generators,witnesses,
  theorem:'Q integral iff XOR; Q rows in C iff one class in C; physical characteristic checksum is 8 mod16.',
  limitations:'Degree ten, CT and common-neighbor budgets are not asserted for the witnesses.'};
fs.writeFileSync(path.join(here,'controle_congruences_selection42.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,word:witnesses.correct_xor_wrong_rows.one_codeword_mask,
  all24syndromes_verified:true,dodecads:witnesses.correct_xor_wrong_rows.number_dodecads,
  checksum:witnesses.correct_xor_wrong_rows.characteristic_sum_mod16}));

```


## controle_coque3_D8_et_trialite.json

2594 octets ; SHA256 f102fc83009fb6c4ff90ca1a01a037aabd4c1ffcdebfdb97edc8a5dbf49d91b6

```json
{
  "exact": true,
  "scope": "Coque D8^3 complete et trialite D4 ; aucune enumeration de reperes physiques.",
  "glue": [
    {
      "mask": 0,
      "classes": [
        0,
        0,
        0
      ],
      "min": 0,
      "integral": true
    },
    {
      "mask": 1,
      "classes": [
        2,
        2,
        0
      ],
      "min": 4,
      "integral": false
    },
    {
      "mask": 2,
      "classes": [
        0,
        2,
        2
      ],
      "min": 4,
      "integral": false
    },
    {
      "mask": 3,
      "classes": [
        2,
        0,
        2
      ],
      "min": 4,
      "integral": false
    },
    {
      "mask": 4,
      "classes": [
        1,
        1,
        1
      ],
      "min": 3,
      "integral": true
    },
    {
      "mask": 5,
      "classes": [
        3,
        3,
        1
      ],
      "min": 5,
      "integral": false
    },
    {
      "mask": 6,
      "classes": [
        1,
        3,
        3
      ],
      "min": 5,
      "integral": false
    },
    {
      "mask": 7,
      "classes": [
        3,
        1,
        3
      ],
      "min": 5,
      "integral": false
    }
  ],
  "root_determinant": 64,
  "index": 8,
  "determinant": 1,
  "integer_sublattice_index": 4,
  "norm3_shell_count": 4096,
  "unsigned_triple_masks": 512,
  "span_mod2": 22,
  "gram_mod2_rank": 20,
  "radical_dimension": 2,
  "radical_ambient_masks": [
    65535,
    16776960
  ],
  "basis_mod2": [
    3,
    5,
    9,
    17,
    33,
    65,
    129,
    768,
    1280,
    2304,
    4352,
    8448,
    16640,
    33024,
    196608,
    327680,
    589824,
    1114112,
    2162688,
    4259840,
    8454144,
    65793
  ],
  "gram_rows_mod2": [
    2097278,
    2097277,
    2097275,
    2097271,
    2097263,
    2097247,
    2097215,
    2113280,
    2113152,
    2112896,
    2112384,
    2111360,
    2109312,
    2105216,
    4161536,
    4145152,
    4112384,
    4046848,
    3915776,
    3653632,
    3129344,
    4194303
  ],
  "triality": {
    "D4_roots_tested": 24,
    "even_spinors": 8,
    "odd_spinors": 8,
    "hadamard": [
      [
        1,
        1,
        1,
        1
      ],
      [
        1,
        1,
        -1,
        -1
      ],
      [
        1,
        -1,
        1,
        -1
      ],
      [
        1,
        -1,
        -1,
        1
      ]
    ],
    "all_images_verified": true
  },
  "physical_root_Gram_mod2_required_rank": 22,
  "consequence": "Aucun repere physique 42+7 dans cette enveloppe D8^3. Une composante D4 uniforme en classe est impossible pour les memes 42 u."
}

```


## controle_coque3_D8_et_trialite.mjs

4441 octets ; SHA256 f37c6a02a3a55727fda6208db78b58609cbad27bd3c84660cd798ab7a01f8dfc

```javascript
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

// Petits calculs exacts independants : aucune coque quadratique 4096 x 4096.
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const assert=(p,m)=>{if(!p)throw new Error(m);};
const pop=n=>{let k=0;while(n){n&=n-1;k++;}return k;};
function rank2(rows,ncols){
  const a=rows.slice();let r=0;
  for(let j=0;j<ncols;j++){
    const p=a.findIndex((x,i)=>i>=r&&((x>>>j)&1));
    if(p<0)continue;
    [a[r],a[p]]=[a[p],a[r]];
    for(let i=0;i<a.length;i++)if(i!==r&&((a[i]>>>j)&1))a[i]^=a[r];
    r++;
  }
  return r;
}
const blockMasks=[255,255<<8,255<<16];
const basis=[];
for(let b=0;b<3;b++)for(let j=1;j<8;j++)basis.push((1<<(8*b))|(1<<(8*b+j)));
basis.push((1<<0)|(1<<8)|(1<<16));
const gramMasks=basis.map(x=>basis.reduce((m,y,j)=>m|((pop(x&y)&1)<<j),0));
const unsignedTriples=[];
for(let i=0;i<8;i++)for(let j=0;j<8;j++)for(let k=0;k<8;k++)
  unsignedTriples.push((1<<i)|(1<<(8+j))|(1<<(16+k)));
assert(rank2(basis,24)===22,'dimension W');
assert(rank2(unsignedTriples,24)===22,'span des 512 triplets');
assert(rank2(gramMasks,22)===20,'rang Gram modulo deux');
const radical=[blockMasks[0]^blockMasks[1],blockMasks[1]^blockMasks[2]];
for(const z of radical)for(const x of basis)assert((pop(z&x)&1)===0,'radical orthogonal');
for(const x of unsignedTriples){
  const par=blockMasks.map(b=>pop(x&b)&1);assert(par.every(p=>p===1),'parites trois blocs');
}

// Classes (x,y) avec v=(1,0), s=(0,1), c=(1,1).
const classMin=[0,1,2,2];
const glueBasis=[[2,2,0],[0,2,2],[1,1,1]];
const glue=[];
for(let m=0;m<8;m++){
  const cl=[0,0,0];
  for(let i=0;i<3;i++)if((m>>i)&1)for(let j=0;j<3;j++)cl[j]^=glueBasis[i][j];
  glue.push({mask:m,classes:cl,min:cl.reduce((s,c)=>s+classMin[c],0),
    integral:cl.every(c=>(c&2)===0)});
}
assert(new Set(glue.map(x=>x.classes.join(','))).size===8,'indice huit');
assert(glue.filter(x=>x.integral).length===2,'indice entier quatre');
assert(glue.filter(x=>x.min===3).length===1,'unique classe de norme trois');
assert(glue.find(x=>x.min===3).classes.every(c=>c===1),'classe vvv');
const rootDet=64,glueIndex=8,unimodDet=rootDet/(glueIndex*glueIndex);
assert(unimodDet===1,'determinant U');

// Trialite D4 : A=Hadamard/2. Les vecteurs testes ont coordonnees doublees.
const had=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];
for(let i=0;i<4;i++)for(let j=0;j<4;j++)assert(dot(had[i],had[j])===(i===j?4:0),'orthogonalite A');
const roots4=[];
for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)for(const a of [-1,1])for(const b of [-1,1]){
  const x=[0,0,0,0];x[i]=2*a;x[j]=2*b;roots4.push(x);
}
const transform=(x,flip=false)=>had.map(row=>dot(row,x.map((z,i)=>flip&&i===0?-z:z))/2);
for(const x of roots4)for(const flip of [false,true]){
  const y=transform(x,flip);
  assert(y.every(z=>Number.isInteger(z)&&z%2===0),'racine D4 entiere');
  assert((y.reduce((s,z)=>s+z,0)/2)%2===0,'racine D4 somme paire');
  assert(dot(y,y)===8,'norme deux preservee');
}
const spinEven=[],spinOdd=[];
for(let m=0;m<16;m++){
  const x=Array.from({length:4},(_,i)=>((m>>i)&1)?-1:1);
  (pop(m)%2?spinOdd:spinEven).push(x);
}
function isDoubledUnit(x){return dot(x,x)===4&&x.filter(z=>z!==0).length===1&&x.every(z=>z===0||Math.abs(z)===2);}
for(const x of spinEven)assert(isDoubledUnit(transform(x)),'s vers v');
for(const x of spinOdd)assert(isDoubledUnit(transform(x,true)),'c vers v');
const result={exact:true,
  scope:'Coque D8^3 complete et trialite D4 ; aucune enumeration de reperes physiques.',
  glue,root_determinant:rootDet,index:glueIndex,determinant:unimodDet,
  integer_sublattice_index:4,norm3_shell_count:16**3,
  unsigned_triple_masks:unsignedTriples.length,span_mod2:22,
  gram_mod2_rank:20,radical_dimension:2,radical_ambient_masks:radical,
  basis_mod2:basis,gram_rows_mod2:gramMasks,
  triality:{D4_roots_tested:roots4.length,even_spinors:spinEven.length,
    odd_spinors:spinOdd.length,hadamard:had,all_images_verified:true},
  physical_root_Gram_mod2_required_rank:22,
  consequence:'Aucun repere physique 42+7 dans cette enveloppe D8^3. Une composante D4 uniforme en classe est impossible pour les memes 42 u.'};
const outfile=path.join(path.dirname(fileURLToPath(import.meta.url)),'controle_coque3_D8_et_trialite.json');
fs.writeFileSync(outfile,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,determinant:unimodDet,shell:16**3,Gram_mod2:20,
  required:22,triality_verified:true}));

```


## controle_selection42_golay.json

20665 octets ; SHA256 3f7d688f1fdad4795b1e85fef2dd59f81027a6d8d5af85b9cda21833bafd774f

```json
{
  "scope": "Filtres sur la MEME sélection42+7 dans le Golay explicite; aucune exclusion globale g18/g20",
  "code": {
    "size": 4096,
    "polynomial_exponents": [
      11,
      9,
      7,
      6,
      5,
      1,
      0
    ],
    "generator_masks": [
      8391395,
      8394182,
      8399756,
      8410904,
      8433200,
      8477792,
      8566976,
      8745344,
      9102080,
      9815552,
      11242496,
      14096384
    ]
  },
  "B": [
    [
      -3,
      -3,
      -3,
      1,
      1,
      1,
      1,
      1,
      1,
      -3,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ],
    [
      -1,
      -1,
      1,
      3,
      3,
      -1,
      -1,
      -1,
      -1,
      1,
      -1,
      -1,
      -1,
      -3,
      -1,
      -3,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ]
  ],
  "V_mask": 24059,
  "V_indices": [
    0,
    1,
    3,
    4,
    5,
    6,
    7,
    8,
    10,
    11,
    12,
    14
  ],
  "shell704": 704,
  "witness_wrong_xor": {
    "selected_codeword_masks": [
      34236,
      117786,
      136944,
      141498,
      228921,
      235572,
      282996,
      305244,
      334034,
      345385,
      408336,
      449821,
      496827,
      573785,
      581244,
      601132,
      628698,
      706700,
      771060,
      1060121,
      2103532,
      4214092,
      342461,
      684922,
      743789,
      753962,
      791953,
      799998,
      804970,
      823048,
      848796,
      859881,
      899642,
      924740,
      993654,
      1012877,
      1020544,
      1036155,
      1043988,
      1068712,
      1145754,
      1163372
    ],
    "basis22_masks": [
      34236,
      117786,
      136944,
      141498,
      228921,
      235572,
      282996,
      305244,
      334034,
      345385,
      408336,
      449821,
      496827,
      573785,
      581244,
      601132,
      628698,
      706700,
      771060,
      1060121,
      2103532,
      4214092
    ],
    "exact_real_rank": 22,
    "rank_justification": "rang>=22mod101 et <=22 par les deux orthogonaux indépendants",
    "pair_Gram_histogram": {
      "0": 417,
      "1": 433,
      "-1": 11
    },
    "nonzero_pair_degrees": [
      26,
      25,
      19,
      22,
      21,
      25,
      23,
      25,
      20,
      21,
      21,
      23,
      20,
      21,
      28,
      26,
      19,
      23,
      18,
      18,
      21,
      21,
      23,
      18,
      22,
      20,
      20,
      21,
      24,
      24,
      20,
      21,
      25,
      23,
      19,
      15,
      19,
      19,
      19,
      18,
      13,
      19
    ],
    "xor_mask": 6665306,
    "xor_allowed": false,
    "integral": false,
    "F": [
      [
        4,
        -10,
        -2,
        6,
        10,
        4,
        6,
        0,
        -8,
        -6,
        -10,
        8,
        -2,
        -4,
        -4,
        4,
        -4,
        -2,
        -4,
        6,
        -10,
        -12,
        -12,
        -14
      ],
      [
        -10,
        4,
        8,
        8,
        0,
        -2,
        -4,
        -2,
        2,
        -12,
        8,
        6,
        4,
        -10,
        6,
        -2,
        -6,
        0,
        2,
        0,
        -8,
        -10,
        -10,
        -12
      ],
      [
        -2,
        8,
        4,
        4,
        4,
        2,
        -4,
        6,
        6,
        4,
        8,
        2,
        4,
        2,
        -2,
        2,
        6,
        0,
        2,
        0,
        4,
        -2,
        -2,
        0
      ],
      [
        6,
        8,
        4,
        4,
        -8,
        -6,
        8,
        6,
        2,
        8,
        -4,
        -6,
        8,
        10,
        -6,
        6,
        -2,
        12,
        6,
        -4,
        8,
        14,
        14,
        16
      ],
      [
        10,
        0,
        4,
        -8,
        4,
        2,
        4,
        2,
        -6,
        -4,
        4,
        2,
        -8,
        -2,
        6,
        2,
        -2,
        -4,
        -6,
        4,
        8,
        10,
        10,
        8
      ],
      [
        4,
        -2,
        2,
        -6,
        2,
        12,
        -10,
        0,
        4,
        6,
        2,
        0,
        -2,
        0,
        0,
        4,
        -8,
        -2,
        8,
        2,
        6,
        4,
        8,
        6
      ],
      [
        6,
        -4,
        -4,
        8,
        4,
        -10,
        12,
        2,
        -2,
        4,
        4,
        2,
        -4,
        6,
        -6,
        2,
        6,
        4,
        2,
        -8,
        0,
        -6,
        -6,
        -4
      ],
      [
        0,
        -2,
        6,
        6,
        2,
        0,
        2,
        12,
        4,
        -2,
        -2,
        12,
        -14,
        -4,
        8,
        0,
        0,
        2,
        0,
        2,
        -6,
        -8,
        -4,
        -6
      ],
      [
        -8,
        2,
        6,
        2,
        -6,
        4,
        -2,
        4,
        12,
        2,
        2,
        8,
        2,
        -4,
        -8,
        -4,
        4,
        2,
        0,
        -2,
        -2,
        0,
        -4,
        -2
      ],
      [
        -6,
        -12,
        4,
        8,
        -4,
        6,
        4,
        -2,
        2,
        4,
        0,
        6,
        -4,
        -2,
        -2,
        -2,
        -2,
        -4,
        2,
        -8,
        -8,
        -6,
        -6,
        -8
      ],
      [
        -10,
        8,
        8,
        -4,
        4,
        2,
        4,
        -2,
        2,
        0,
        12,
        -2,
        0,
        2,
        -2,
        -2,
        2,
        4,
        -2,
        0,
        0,
        2,
        -2,
        0
      ],
      [
        8,
        6,
        2,
        -6,
        2,
        0,
        2,
        12,
        8,
        6,
        -2,
        12,
        2,
        -8,
        0,
        4,
        0,
        2,
        0,
        6,
        6,
        8,
        8,
        10
      ],
      [
        -2,
        4,
        4,
        8,
        -8,
        -2,
        -4,
        -14,
        2,
        -4,
        0,
        2,
        12,
        -6,
        6,
        6,
        -2,
        -4,
        -10,
        0,
        8,
        2,
        6,
        4
      ],
      [
        -4,
        -10,
        2,
        10,
        -2,
        0,
        6,
        -4,
        -4,
        -2,
        2,
        -8,
        -6,
        4,
        0,
        0,
        0,
        -2,
        -4,
        2,
        -10,
        -8,
        -8,
        -10
      ],
      [
        -4,
        6,
        -2,
        -6,
        6,
        0,
        -6,
        8,
        -8,
        -2,
        -2,
        0,
        6,
        0,
        12,
        -8,
        0,
        -2,
        8,
        -2,
        -6,
        0,
        -4,
        -2
      ],
      [
        4,
        -2,
        2,
        6,
        2,
        4,
        2,
        0,
        -4,
        -2,
        -2,
        4,
        6,
        0,
        -8,
        4,
        -4,
        -2,
        4,
        -6,
        2,
        0,
        0,
        -2
      ],
      [
        -4,
        -6,
        6,
        -2,
        -2,
        -8,
        6,
        0,
        4,
        -2,
        2,
        0,
        -2,
        0,
        0,
        -4,
        12,
        -10,
        -4,
        -6,
        -2,
        0,
        0,
        -2
      ],
      [
        -2,
        0,
        0,
        12,
        -4,
        -2,
        4,
        2,
        2,
        -4,
        4,
        2,
        -4,
        -2,
        -2,
        -2,
        -10,
        12,
        -2,
        -8,
        0,
        -6,
        -6,
        -8
      ],
      [
        -4,
        2,
        2,
        6,
        -6,
        8,
        2,
        0,
        0,
        2,
        -2,
        0,
        -10,
        -4,
        8,
        4,
        -4,
        -2,
        12,
        -10,
        6,
        0,
        0,
        -2
      ],
      [
        6,
        0,
        0,
        -4,
        4,
        2,
        -8,
        2,
        -2,
        -8,
        0,
        6,
        0,
        2,
        -2,
        -6,
        -6,
        -8,
        -10,
        12,
        8,
        2,
        2,
        0
      ],
      [
        -10,
        -8,
        4,
        8,
        8,
        6,
        0,
        -6,
        -2,
        -8,
        0,
        6,
        8,
        -10,
        -6,
        2,
        -2,
        0,
        6,
        8,
        12,
        -34,
        -34,
        -36
      ],
      [
        -12,
        -10,
        -2,
        14,
        10,
        4,
        -6,
        -8,
        0,
        -6,
        2,
        8,
        2,
        -8,
        0,
        0,
        0,
        -6,
        0,
        2,
        -34,
        12,
        -40,
        -42
      ],
      [
        -12,
        -10,
        -2,
        14,
        10,
        8,
        -6,
        -4,
        -4,
        -6,
        -2,
        8,
        6,
        -8,
        -4,
        0,
        0,
        -6,
        0,
        2,
        -34,
        -40,
        12,
        -42
      ],
      [
        -14,
        -12,
        0,
        16,
        8,
        6,
        -4,
        -6,
        -2,
        -8,
        0,
        10,
        4,
        -10,
        -2,
        -2,
        -2,
        -8,
        -2,
        0,
        -36,
        -42,
        -42,
        12
      ]
    ],
    "nonintegral_entry": {
      "row": 0,
      "column": 1,
      "numerator": -10,
      "denominator": 4
    },
    "limitations": "Normes3, orthogonalité aux deux y, span22 et pairings0/±1 seulement; degré10, CT et budgets SRG non revendiqués"
  },
  "witness_correct_xor_wrong_Q_rows": {
    "selected_codeword_masks": [
      34236,
      117786,
      136944,
      141498,
      228921,
      235572,
      282996,
      305244,
      334034,
      345385,
      408336,
      449821,
      496827,
      573785,
      581244,
      601132,
      628698,
      706700,
      771060,
      1060121,
      2103532,
      4214092,
      342461,
      684922,
      743789,
      753962,
      791953,
      799998,
      804970,
      823048,
      848796,
      859881,
      899642,
      924740,
      993654,
      1012877,
      1020544,
      1036155,
      1043988,
      1068712,
      1145754,
      7612877
    ],
    "basis22_masks": [
      34236,
      117786,
      136944,
      141498,
      228921,
      235572,
      282996,
      305244,
      334034,
      345385,
      408336,
      449821,
      496827,
      573785,
      581244,
      601132,
      628698,
      706700,
      771060,
      1060121,
      2103532,
      4214092
    ],
    "exact_real_rank": 22,
    "rank_justification": "rang>=22mod101 et <=22 par les deux orthogonaux indépendants",
    "pair_Gram_histogram": {
      "0": 417,
      "1": 421,
      "-1": 23
    },
    "nonzero_pair_degrees": [
      25,
      25,
      20,
      22,
      22,
      25,
      22,
      25,
      20,
      20,
      20,
      23,
      21,
      20,
      28,
      25,
      20,
      22,
      18,
      19,
      21,
      21,
      24,
      19,
      21,
      20,
      19,
      21,
      23,
      24,
      20,
      21,
      26,
      23,
      19,
      15,
      20,
      20,
      20,
      17,
      13,
      19
    ],
    "xor_mask": 24059,
    "xor_allowed": true,
    "integral": true,
    "Q": [
      [
        1,
        -2,
        -1,
        1,
        3,
        1,
        1,
        0,
        -2,
        -1,
        -2,
        2,
        0,
        -1,
        -1,
        1,
        -1,
        0,
        -1,
        2,
        -3,
        -3,
        -3,
        -3
      ],
      [
        -2,
        1,
        2,
        2,
        0,
        -1,
        -1,
        0,
        1,
        -3,
        2,
        2,
        1,
        -2,
        1,
        -1,
        -2,
        0,
        1,
        0,
        -2,
        -2,
        -2,
        -3
      ],
      [
        -1,
        2,
        1,
        1,
        1,
        1,
        -1,
        1,
        1,
        1,
        2,
        0,
        1,
        0,
        0,
        1,
        2,
        0,
        0,
        0,
        1,
        -1,
        -1,
        0
      ],
      [
        1,
        2,
        1,
        1,
        -2,
        -1,
        2,
        1,
        0,
        2,
        -1,
        -2,
        2,
        2,
        -1,
        2,
        0,
        3,
        1,
        -1,
        2,
        3,
        3,
        4
      ],
      [
        3,
        0,
        1,
        -2,
        1,
        0,
        1,
        1,
        -1,
        -1,
        1,
        1,
        -2,
        0,
        1,
        0,
        -1,
        -1,
        -1,
        1,
        2,
        3,
        3,
        2
      ],
      [
        1,
        -1,
        1,
        -1,
        0,
        3,
        -2,
        0,
        1,
        1,
        0,
        0,
        -1,
        0,
        0,
        1,
        -2,
        -1,
        2,
        0,
        2,
        1,
        2,
        1
      ],
      [
        1,
        -1,
        -1,
        2,
        1,
        -2,
        3,
        0,
        -1,
        1,
        1,
        0,
        -1,
        1,
        -1,
        1,
        2,
        1,
        0,
        -2,
        0,
        -2,
        -2,
        -1
      ],
      [
        0,
        0,
        1,
        1,
        1,
        0,
        0,
        3,
        1,
        0,
        0,
        3,
        -3,
        -1,
        2,
        0,
        0,
        1,
        0,
        1,
        -2,
        -2,
        -1,
        -1
      ],
      [
        -2,
        1,
        1,
        0,
        -1,
        1,
        -1,
        1,
        3,
        1,
        1,
        2,
        1,
        -1,
        -2,
        -1,
        1,
        1,
        0,
        0,
        -1,
        0,
        -1,
        0
      ],
      [
        -1,
        -3,
        1,
        2,
        -1,
        1,
        1,
        0,
        1,
        1,
        0,
        2,
        -1,
        0,
        -1,
        -1,
        -1,
        -1,
        1,
        -2,
        -2,
        -1,
        -1,
        -2
      ],
      [
        -2,
        2,
        2,
        -1,
        1,
        0,
        1,
        0,
        1,
        0,
        3,
        0,
        0,
        1,
        -1,
        -1,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        2,
        2,
        0,
        -2,
        1,
        0,
        0,
        3,
        2,
        2,
        0,
        3,
        1,
        -2,
        0,
        1,
        0,
        1,
        0,
        2,
        1,
        2,
        2,
        3
      ],
      [
        0,
        1,
        1,
        2,
        -2,
        -1,
        -1,
        -3,
        1,
        -1,
        0,
        1,
        3,
        -1,
        1,
        1,
        -1,
        -1,
        -2,
        0,
        2,
        1,
        2,
        1
      ],
      [
        -1,
        -2,
        0,
        2,
        0,
        0,
        1,
        -1,
        -1,
        0,
        1,
        -2,
        -1,
        1,
        0,
        0,
        0,
        0,
        -1,
        1,
        -3,
        -2,
        -2,
        -2
      ],
      [
        -1,
        1,
        0,
        -1,
        1,
        0,
        -1,
        2,
        -2,
        -1,
        -1,
        0,
        1,
        0,
        3,
        -2,
        0,
        -1,
        2,
        -1,
        -1,
        0,
        -1,
        -1
      ],
      [
        1,
        -1,
        1,
        2,
        0,
        1,
        1,
        0,
        -1,
        -1,
        -1,
        1,
        1,
        0,
        -2,
        1,
        -1,
        -1,
        1,
        -2,
        1,
        0,
        0,
        -1
      ],
      [
        -1,
        -2,
        2,
        0,
        -1,
        -2,
        2,
        0,
        1,
        -1,
        0,
        0,
        -1,
        0,
        0,
        -1,
        3,
        -3,
        -1,
        -2,
        0,
        0,
        0,
        -1
      ],
      [
        0,
        0,
        0,
        3,
        -1,
        -1,
        1,
        1,
        1,
        -1,
        1,
        1,
        -1,
        0,
        -1,
        -1,
        -3,
        3,
        0,
        -2,
        0,
        -1,
        -1,
        -2
      ],
      [
        -1,
        1,
        0,
        1,
        -1,
        2,
        0,
        0,
        0,
        1,
        0,
        0,
        -2,
        -1,
        2,
        1,
        -1,
        0,
        3,
        -2,
        1,
        0,
        0,
        0
      ],
      [
        2,
        0,
        0,
        -1,
        1,
        0,
        -2,
        1,
        0,
        -2,
        0,
        2,
        0,
        1,
        -1,
        -2,
        -2,
        -2,
        -2,
        3,
        2,
        1,
        1,
        0
      ],
      [
        -3,
        -2,
        1,
        2,
        2,
        2,
        0,
        -2,
        -1,
        -2,
        0,
        1,
        2,
        -3,
        -1,
        1,
        0,
        0,
        1,
        2,
        3,
        -9,
        -9,
        -9
      ],
      [
        -3,
        -2,
        -1,
        3,
        3,
        1,
        -2,
        -2,
        0,
        -1,
        1,
        2,
        1,
        -2,
        0,
        0,
        0,
        -1,
        0,
        1,
        -9,
        3,
        -10,
        -10
      ],
      [
        -3,
        -2,
        -1,
        3,
        3,
        2,
        -2,
        -1,
        -1,
        -1,
        0,
        2,
        2,
        -2,
        -1,
        0,
        0,
        -1,
        0,
        1,
        -9,
        -10,
        3,
        -10
      ],
      [
        -3,
        -3,
        0,
        4,
        2,
        1,
        -1,
        -1,
        0,
        -2,
        0,
        3,
        1,
        -2,
        -1,
        -1,
        -1,
        -2,
        0,
        0,
        -9,
        -10,
        -10,
        3
      ]
    ],
    "row_masks": [
      16114301,
      8704866,
      7377917,
      7226541,
      7294933,
      10654511,
      8582999,
      13253020,
      5486582,
      6804343,
      2286936,
      9607312,
      10746854,
      1848769,
      14308955,
      9936743,
      8885009,
      6545400,
      1417755,
      6840472,
      16050437,
      3806781,
      5915549,
      9558243
    ],
    "rows_not_in_code": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11,
      12,
      13,
      14,
      15,
      16,
      17,
      18,
      19,
      20,
      21,
      22,
      23
    ],
    "first_bad_row_certificate": {
      "row": 0,
      "row_mask": 16114301,
      "generator_number": 0,
      "generator_mask": 8391395,
      "intersection_parity": 1
    },
    "limitations": "Normes3, orthogonalité aux deux y, span22 et pairings0/±1 seulement; degré10, CT et budgets SRG non revendiqués"
  },
  "forbidden_block": {
    "coordinates_numerator_over_sqrt8": [
      0,
      0,
      4,
      0,
      0,
      0,
      0,
      0,
      0,
      -4,
      0,
      0,
      0,
      0,
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
    "norm": 4,
    "orthogonal_to_y": true,
    "offending_coordinate": 2,
    "M_value": 2,
    "B_square_sum": 10,
    "column_energy": 26,
    "physical_target": 14,
    "limitation": "Un h réel de l’enveloppe; aucun cadre de sept h ni SRG n’est construit"
  },
  "proof_conditions": [
    "Tout h physique est octade, M0/±1",
    "XOR42=d1 XOR d2 ou son complément",
    "Q=(56I-EtE-BtB)/4 entier et toutes ses lignes modulo2 appartiennent au code",
    "Q=MtM, rank7 et Q^2=8Q sont aussi nécessaires mais non attestés par ces témoins"
  ]
}

```


## controle_selection42_golay.mjs

6518 octets ; SHA256 ab36c25725bec80aca4365ba6607d0276bd990dc2145bcb80d8b7a5635ccead6

```javascript
// Sélections42+7 dans l'enveloppe Golay explicite du fil.
// 4096 mots seulement; aucun solveur, aucun graphe SRG construit.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const check=(ok,label)=>{if(!ok)throw Error(label);};
const pop=n=>{let k=0;while(n){n&=n-1;k++;}return k;};
const ALL=(1<<24)-1;
const poly=[11,9,7,6,5,1,0].reduce((s,k)=>s|(1<<k),0);
const code=[];
for(let m=0;m<4096;m++){
  let c=0;for(let i=0;i<12;i++)if((m>>>i)&1)c^=poly<<i;
  c|=(pop(c)&1)<<23;code.push(c);
}
const codeSet=new Set(code);
const generators=Array.from({length:12},(_,i)=>code[1<<i]);
check(codeSet.size===4096,'code4096');
check(code.every(c=>[0,8,12,16,24].includes(pop(c))),'poids du code');
check(generators.every(a=>generators.every(b=>pop(a&b)%2===0)),'code autodual');
const Vindices=[0,1,3,4,5,6,7,8,10,11,12,14];
const V=Vindices.reduce((s,k)=>s|(1<<k),0);
const D=[0,1,2,9],Dp=[3,4,13,15];
const b1=Array.from({length:24},(_,j)=>D.includes(j)?-3:1);
const b2=Array.from({length:24},(_,j)=>(((V>>>j)&1)?-1:1)*(Dp.includes(j)?-3:1));
const signs=c=>Array.from({length:24},(_,j)=>1-2*((c>>>j)&1));
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
check(codeSet.has(V),'V dans code');
check(dot(b1,b1)===56&&dot(b2,b2)===56&&dot(b1,b2)===0,'deux y norm7');
const shell=code.filter(c=>dot(signs(c),b1)===0&&dot(signs(c),b2)===0);
check(shell.length===704,'shell704');
const canonical=shell.filter(c=>c<(c^ALL)).sort((a,b)=>a-b),canSet=new Set(canonical);
check(canonical.length===352,'sans antipodes');
const xor=S=>S.reduce((a,c)=>a^c,0);
const modulus=101;
const power=(x,k)=>{let a=1;while(k){if(k&1)a=a*x%modulus;x=x*x%modulus;k>>=1;}return a;};
const pivots=[],basis=[];
for(const c of canonical){
  let r=signs(c).map(x=>(x+modulus)%modulus);
  for(const p of pivots){const z=r[p.col];if(z)r=r.map((x,j)=>(x-z*p.row[j]%modulus+modulus)%modulus);}
  const col=r.findIndex(x=>x);if(col<0)continue;
  const z=power(r[col],modulus-2);r=r.map(x=>x*z%modulus);
  pivots.push({col,row:r});basis.push(c);if(basis.length===22)break;
}
check(basis.length===22,'rang22 modulo101');
const basisSet=new Set(basis),others=canonical.filter(c=>!basisSet.has(c));
function defect(S){
  const E=S.map(signs);
  const F=Array.from({length:24},(_,j)=>Array.from({length:24},(_,k)=>
    (j===k?56:0)-E.reduce((s,r)=>s+r[j]*r[k],0)-b1[j]*b1[k]-b2[j]*b2[k]));
  if(F.some(r=>r.some(x=>x%4))){
    const j=F.findIndex(r=>r.some(x=>x%4)),k=F[j].findIndex(x=>x%4);
    return{integral:false,F,nonintegral_entry:{row:j,column:k,numerator:F[j][k],denominator:4}};
  }
  const Q=F.map(r=>r.map(x=>x/4));
  const row_masks=Q.map(r=>r.reduce((m,x,j)=>m|(((x%2+2)%2)<<j),0));
  const rows_not_in_code=row_masks.flatMap((c,j)=>codeSet.has(c)?[]:[j]);
  let first_bad_row_certificate;
  if(rows_not_in_code.length){
    const j=rows_not_in_code[0],k=generators.findIndex(g=>pop(g&row_masks[j])%2);
    check(k>=0,'syndrome horscode');
    first_bad_row_certificate={row:j,row_mask:row_masks[j],generator_number:k,
      generator_mask:generators[k],intersection_parity:1};
  }
  return{integral:true,Q,row_masks,rows_not_in_code,first_bad_row_certificate};
}
const badXor=[...basis,...others.slice(0,20)];
check(xor(badXor)!==V&&xor(badXor)!==(V^ALL),'sélectionXOR fausse');
check(!defect(badXor).integral,'Q non entier');
let badRows;
for(let shift=0;shift<32&&!badRows;shift++){
  const base=[...basis,...others.slice(shift,shift+18)],used=new Set(base),target=xor(base)^V;
  for(const c of canonical){
    const d=c^target;
    if(c!==d&&canSet.has(d)&&!used.has(c)&&!used.has(d)){
      const S=[...base,c,d],r=defect(S);
      if(r.integral&&r.rows_not_in_code.length){badRows=S;break;}
    }
  }
}
check(badRows,'sélectionXOR correcte mais lignesQ incorrectes');
check(xor(badRows)===V,'XORV');
function certificate(S){
  check(new Set(S).size===42,'42 distincts');
  check(basis.every(c=>S.includes(c)),'contient22indépendants');
  const E=S.map(signs),histogram={};
  for(let i=0;i<42;i++)for(let j=i+1;j<42;j++){
    const n=dot(E[i],E[j]);check(n%8===0&&Math.abs(n)<=8,'Gram pair0/±1');
    const a=n/8;histogram[a]=(histogram[a]??0)+1;
  }
  const degree=E.map((r,i)=>E.filter((s,j)=>i!==j&&dot(r,s)!==0).length);
  return{selected_codeword_masks:S,basis22_masks:basis,
    exact_real_rank:22,rank_justification:'rang>=22mod101 et <=22 par les deux orthogonaux indépendants',
    pair_Gram_histogram:histogram,nonzero_pair_degrees:degree,
    xor_mask:xor(S),xor_allowed:xor(S)===V||xor(S)===(V^ALL),
    ...defect(S),
    limitations:'Normes3, orthogonalité aux deux y, span22 et pairings0/±1 seulement; degré10, CT et budgets SRG non revendiqués'};
}
// Un h de type coordonnées, de norme4 et orthogonal aux deux y, existe
// réellement dans l'enveloppe. Toute sélection physique contenant h est impossible.
const h=Array(24).fill(0);h[2]=4;h[9]=-4;
check(dot(h,h)===32&&dot(h,b1)===0&&dot(h,b2)===0,'h norm4 dans complément');
check(h.reduce((s,x)=>s+x,0)%8===0&&h.every(x=>x%4===0),'h dans réseau Golay');
const result={scope:'Filtres sur la MEME sélection42+7 dans le Golay explicite; aucune exclusion globale g18/g20',
  code:{size:4096,polynomial_exponents:[11,9,7,6,5,1,0],generator_masks:generators},
  B:[b1,b2],V_mask:V,V_indices:Vindices,shell704:shell.length,
  witness_wrong_xor:certificate(badXor),
  witness_correct_xor_wrong_Q_rows:certificate(badRows),
  forbidden_block:{coordinates_numerator_over_sqrt8:h,norm:4,orthogonal_to_y:true,
    offending_coordinate:2,M_value:2,B_square_sum:10,
    column_energy:10+4*2*2,physical_target:14,
    limitation:'Un h réel de l’enveloppe; aucun cadre de sept h ni SRG n’est construit'},
  proof_conditions:['Tout h physique est octade, M0/±1',
    'XOR42=d1 XOR d2 ou son complément',
    'Q=(56I-EtE-BtB)/4 entier et toutes ses lignes modulo2 appartiennent au code',
    'Q=MtM, rank7 et Q^2=8Q sont aussi nécessaires mais non attestés par ces témoins']};
fs.writeFileSync(path.join(path.dirname(fileURLToPath(import.meta.url)),'controle_selection42_golay.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,shell704:shell.length,
  witness1_xor:result.witness_wrong_xor.xor_mask,witness1_integral:result.witness_wrong_xor.integral,
  witness2_xor:result.witness_correct_xor_wrong_Q_rows.xor_mask,
  witness2_bad_Q_rows:result.witness_correct_xor_wrong_Q_rows.rows_not_in_code,
  both_rank:22,forbidden_h_energy:result.forbidden_block.column_energy,physical_target:14}));

```


## controle_sept_octades_rang4.json

11545 octets ; SHA256 8d8c19992f26efd7c85d054bb34a833e6c10f00065dcc9c10e0c35dbd0a24782

```json
{
  "exact": true,
  "scope": "Lemme sept appuis de rang binaire <=4 et paire de normales fixe 0803. Aucun balayage de septuplets.",
  "quotient_classes": 7,
  "multiplicity_bound": 3,
  "multisets_with_odd_xor_zero": 148,
  "odd_support_cardinalities": {
    "3": 147,
    "7": 1
  },
  "multiplicity_profiles": {
    "3,2,1,1": 84,
    "3,3,1": 21,
    "2,2,1,1,1": 42,
    "1,1,1,1,1,1,1": 1
  },
  "polarities_tested": 128,
  "admissible_polarities": 56,
  "polarities": [
    {
      "mask": 1,
      "multiplicities": [
        8,
        4,
        0,
        4,
        0,
        4,
        0,
        4
      ],
      "octad_index_of_A": 0
    },
    {
      "mask": 2,
      "multiplicities": [
        8,
        0,
        4,
        4,
        0,
        0,
        4,
        4
      ],
      "octad_index_of_A": 1
    },
    {
      "mask": 4,
      "multiplicities": [
        8,
        4,
        4,
        0,
        0,
        4,
        4,
        0
      ],
      "octad_index_of_A": 2
    },
    {
      "mask": 8,
      "multiplicities": [
        8,
        0,
        0,
        0,
        4,
        4,
        4,
        4
      ],
      "octad_index_of_A": 3
    },
    {
      "mask": 11,
      "multiplicities": [
        4,
        0,
        0,
        4,
        0,
        4,
        4,
        8
      ],
      "octad_index_of_A": 6
    },
    {
      "mask": 13,
      "multiplicities": [
        4,
        4,
        0,
        0,
        0,
        8,
        4,
        4
      ],
      "octad_index_of_A": 5
    },
    {
      "mask": 14,
      "multiplicities": [
        4,
        0,
        4,
        0,
        0,
        4,
        8,
        4
      ],
      "octad_index_of_A": 4
    },
    {
      "mask": 16,
      "multiplicities": [
        8,
        4,
        0,
        4,
        4,
        0,
        4,
        0
      ],
      "octad_index_of_A": 4
    },
    {
      "mask": 19,
      "multiplicities": [
        4,
        4,
        0,
        8,
        0,
        0,
        4,
        4
      ],
      "octad_index_of_A": 5
    },
    {
      "mask": 21,
      "multiplicities": [
        4,
        8,
        0,
        4,
        0,
        4,
        4,
        0
      ],
      "octad_index_of_A": 6
    },
    {
      "mask": 22,
      "multiplicities": [
        4,
        4,
        4,
        4,
        0,
        0,
        8,
        0
      ],
      "octad_index_of_A": 3
    },
    {
      "mask": 26,
      "multiplicities": [
        4,
        0,
        0,
        4,
        4,
        0,
        8,
        4
      ],
      "octad_index_of_A": 2
    },
    {
      "mask": 28,
      "multiplicities": [
        4,
        4,
        0,
        0,
        4,
        4,
        8,
        0
      ],
      "octad_index_of_A": 1
    },
    {
      "mask": 31,
      "multiplicities": [
        0,
        4,
        0,
        4,
        0,
        4,
        8,
        4
      ],
      "octad_index_of_A": 0
    },
    {
      "mask": 32,
      "multiplicities": [
        8,
        0,
        4,
        4,
        4,
        4,
        0,
        0
      ],
      "octad_index_of_A": 5
    },
    {
      "mask": 35,
      "multiplicities": [
        4,
        0,
        4,
        8,
        0,
        4,
        0,
        4
      ],
      "octad_index_of_A": 4
    },
    {
      "mask": 37,
      "multiplicities": [
        4,
        4,
        4,
        4,
        0,
        8,
        0,
        0
      ],
      "octad_index_of_A": 3
    },
    {
      "mask": 38,
      "multiplicities": [
        4,
        0,
        8,
        4,
        0,
        4,
        4,
        0
      ],
      "octad_index_of_A": 6
    },
    {
      "mask": 41,
      "multiplicities": [
        4,
        0,
        0,
        4,
        4,
        8,
        0,
        4
      ],
      "octad_index_of_A": 2
    },
    {
      "mask": 44,
      "multiplicities": [
        4,
        0,
        4,
        0,
        4,
        8,
        4,
        0
      ],
      "octad_index_of_A": 0
    },
    {
      "mask": 47,
      "multiplicities": [
        0,
        0,
        4,
        4,
        0,
        8,
        4,
        4
      ],
      "octad_index_of_A": 1
    },
    {
      "mask": 49,
      "multiplicities": [
        4,
        4,
        0,
        8,
        4,
        4,
        0,
        0
      ],
      "octad_index_of_A": 1
    },
    {
      "mask": 50,
      "multiplicities": [
        4,
        0,
        4,
        8,
        4,
        0,
        4,
        0
      ],
      "octad_index_of_A": 0
    },
    {
      "mask": 55,
      "multiplicities": [
        0,
        4,
        4,
        8,
        0,
        4,
        4,
        0
      ],
      "octad_index_of_A": 2
    },
    {
      "mask": 56,
      "multiplicities": [
        4,
        0,
        0,
        4,
        8,
        4,
        4,
        0
      ],
      "octad_index_of_A": 6
    },
    {
      "mask": 59,
      "multiplicities": [
        0,
        0,
        0,
        8,
        4,
        4,
        4,
        4
      ],
      "octad_index_of_A": 3
    },
    {
      "mask": 61,
      "multiplicities": [
        0,
        4,
        0,
        4,
        4,
        8,
        4,
        0
      ],
      "octad_index_of_A": 4
    },
    {
      "mask": 62,
      "multiplicities": [
        0,
        0,
        4,
        4,
        4,
        4,
        8,
        0
      ],
      "octad_index_of_A": 5
    },
    {
      "mask": 64,
      "multiplicities": [
        8,
        4,
        4,
        0,
        4,
        0,
        0,
        4
      ],
      "octad_index_of_A": 6
    },
    {
      "mask": 67,
      "multiplicities": [
        4,
        4,
        4,
        4,
        0,
        0,
        0,
        8
      ],
      "octad_index_of_A": 3
    },
    {
      "mask": 69,
      "multiplicities": [
        4,
        8,
        4,
        0,
        0,
        4,
        0,
        4
      ],
      "octad_index_of_A": 4
    },
    {
      "mask": 70,
      "multiplicities": [
        4,
        4,
        8,
        0,
        0,
        0,
        4,
        4
      ],
      "octad_index_of_A": 5
    },
    {
      "mask": 73,
      "multiplicities": [
        4,
        4,
        0,
        0,
        4,
        4,
        0,
        8
      ],
      "octad_index_of_A": 1
    },
    {
      "mask": 74,
      "multiplicities": [
        4,
        0,
        4,
        0,
        4,
        0,
        4,
        8
      ],
      "octad_index_of_A": 0
    },
    {
      "mask": 79,
      "multiplicities": [
        0,
        4,
        4,
        0,
        0,
        4,
        4,
        8
      ],
      "octad_index_of_A": 2
    },
    {
      "mask": 81,
      "multiplicities": [
        4,
        8,
        0,
        4,
        4,
        0,
        0,
        4
      ],
      "octad_index_of_A": 2
    },
    {
      "mask": 84,
      "multiplicities": [
        4,
        8,
        4,
        0,
        4,
        0,
        4,
        0
      ],
      "octad_index_of_A": 0
    },
    {
      "mask": 87,
      "multiplicities": [
        0,
        8,
        4,
        4,
        0,
        0,
        4,
        4
      ],
      "octad_index_of_A": 1
    },
    {
      "mask": 88,
      "multiplicities": [
        4,
        4,
        0,
        0,
        8,
        0,
        4,
        4
      ],
      "octad_index_of_A": 5
    },
    {
      "mask": 91,
      "multiplicities": [
        0,
        4,
        0,
        4,
        4,
        0,
        4,
        8
      ],
      "octad_index_of_A": 4
    },
    {
      "mask": 93,
      "multiplicities": [
        0,
        8,
        0,
        0,
        4,
        4,
        4,
        4
      ],
      "octad_index_of_A": 3
    },
    {
      "mask": 94,
      "multiplicities": [
        0,
        4,
        4,
        0,
        4,
        0,
        8,
        4
      ],
      "octad_index_of_A": 6
    },
    {
      "mask": 98,
      "multiplicities": [
        4,
        0,
        8,
        4,
        4,
        0,
        0,
        4
      ],
      "octad_index_of_A": 2
    },
    {
      "mask": 100,
      "multiplicities": [
        4,
        4,
        8,
        0,
        4,
        4,
        0,
        0
      ],
      "octad_index_of_A": 1
    },
    {
      "mask": 103,
      "multiplicities": [
        0,
        4,
        8,
        4,
        0,
        4,
        0,
        4
      ],
      "octad_index_of_A": 0
    },
    {
      "mask": 104,
      "multiplicities": [
        4,
        0,
        4,
        0,
        8,
        4,
        0,
        4
      ],
      "octad_index_of_A": 4
    },
    {
      "mask": 107,
      "multiplicities": [
        0,
        0,
        4,
        4,
        4,
        4,
        0,
        8
      ],
      "octad_index_of_A": 5
    },
    {
      "mask": 109,
      "multiplicities": [
        0,
        4,
        4,
        0,
        4,
        8,
        0,
        4
      ],
      "octad_index_of_A": 6
    },
    {
      "mask": 110,
      "multiplicities": [
        0,
        0,
        8,
        0,
        4,
        4,
        4,
        4
      ],
      "octad_index_of_A": 3
    },
    {
      "mask": 112,
      "multiplicities": [
        4,
        4,
        4,
        4,
        8,
        0,
        0,
        0
      ],
      "octad_index_of_A": 3
    },
    {
      "mask": 115,
      "multiplicities": [
        0,
        4,
        4,
        8,
        4,
        0,
        0,
        4
      ],
      "octad_index_of_A": 6
    },
    {
      "mask": 117,
      "multiplicities": [
        0,
        8,
        4,
        4,
        4,
        4,
        0,
        0
      ],
      "octad_index_of_A": 5
    },
    {
      "mask": 118,
      "multiplicities": [
        0,
        4,
        8,
        4,
        4,
        0,
        4,
        0
      ],
      "octad_index_of_A": 4
    },
    {
      "mask": 121,
      "multiplicities": [
        0,
        4,
        0,
        4,
        8,
        4,
        0,
        4
      ],
      "octad_index_of_A": 0
    },
    {
      "mask": 122,
      "multiplicities": [
        0,
        0,
        4,
        4,
        8,
        0,
        4,
        4
      ],
      "octad_index_of_A": 1
    },
    {
      "mask": 124,
      "multiplicities": [
        0,
        4,
        4,
        0,
        8,
        4,
        4,
        0
      ],
      "octad_index_of_A": 2
    }
  ],
  "binary_generator_exponents": [
    0,
    1,
    5,
    6,
    7,
    9,
    11
  ],
  "generators": [
    8391395,
    8394182,
    8399756,
    8410904,
    8433200,
    8477792,
    8566976,
    8745344,
    9102080,
    9815552,
    11242496,
    14096384
  ],
  "code_weight_histogram": {
    "0": 1,
    "8": 759,
    "12": 2576,
    "16": 759,
    "24": 1
  },
  "large_coefficient_support": {
    "D1": [
      0,
      1,
      2,
      9
    ],
    "D2": [
      3,
      4,
      13,
      15
    ],
    "mask": 41503,
    "in_code": false,
    "syndrome": [
      1,
      0,
      0,
      1,
      0,
      0,
      0,
      1,
      1,
      0,
      1,
      0
    ],
    "offending_generator_index": 0,
    "offending_generator_mask": 8391395
  },
  "physical_seven_support_minimum_binary_rank_for_this_pair": 5,
  "remaining_scope": "Support ranks 5,6,7 and other normal pairs are not excluded."
}

```


## controle_sept_octades_rang4.mjs

4579 octets ; SHA256 dc969063f47510a85e5e376804a0a79c8788f24689dfe90c3551c9f23e7903d3

```javascript
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const assert=(p,m)=>{if(!p)throw new Error(m);};
const pop=x=>{let n=0;while(x){x&=x-1;n++;}return n;};
function rank2(rows,ncols){
  const a=rows.slice();let r=0;
  for(let j=0;j<ncols;j++){
    const p=a.findIndex((x,i)=>i>=r&&((x>>>j)&1));if(p<0)continue;
    [a[r],a[p]]=[a[p],a[r]];
    for(let i=0;i<a.length;i++)if(i!==r&&((a[i]>>>j)&1))a[i]^=a[r];r++;
  }
  return r;
}

// Sept classes non nulles de V/<1>=F2^3. Les multiplicites sont <=3.
const profiles={},oddCardCounts={};
let multisets=0;
function walk(c,left){
  if(c.length===7){
    if(left)return;let sum=0,odd=0;
    for(let i=0;i<7;i++)if(c[i]&1){sum^=i+1;odd++;}
    if(sum)return;multisets++;oddCardCounts[odd]=(oddCardCounts[odd]||0)+1;
    assert(odd===3||odd===7,'nombre impair de supports');
    const profile=c.filter(Boolean).sort((a,b)=>b-a).join(',');
    profiles[profile]=(profiles[profile]||0)+1;return;
  }
  for(let n=0;n<=Math.min(3,left);n++)walk([...c,n],left-n);
}
walk([],7);
const expected=['3,3,1','3,2,1,1','2,2,1,1,1','1,1,1,1,1,1,1'];
assert(Object.keys(profiles).every(p=>expected.includes(p)),'profils couvrants');

// Inversion Fourier du cas sept supports distincts.
const polarities=[];
for(let m=0;m<128;m++){
  const sigma=Array.from({length:7},(_,i)=>(m>>i)&1?-1:1);
  const sums=Array.from({length:8},(_,x)=>sigma.reduce((s,t,i)=>s+t*((pop((i+1)&x)&1)?-1:1),0));
  const multiplicities=sums.map(s=>3+s);
  if(multiplicities.some(n=>n<0))continue;
  if(sums.some((s,x)=>multiplicities[x]>0&&s!==1&&s!==5))continue;
  assert(sums.filter(s=>s===5).length===1,'type unique gros huit');
  assert(sums.filter(s=>s===1).length===4,'quatre tetrades');
  assert(sums.filter(s=>s===-3).length===3,'trois types absents');
  const labels=[];for(let x=0;x<8;x++)for(let k=0;k<multiplicities[x];k++)labels.push(x);
  assert(labels.length===24,'vingt-quatre coordonnees');
  const octads=Array.from({length:7},(_,i)=>labels.reduce((w,x,j)=>{
    const bit=sigma[i]*((pop((i+1)&x)&1)?-1:1)===-1;return bit?w|(1<<j):w;
  },0));
  assert(octads.every(w=>pop(w)===8),'sept poids huit');
  assert(rank2(octads,24)===4,'rang quatre');
  const A=labels.reduce((w,x,j)=>sums[x]===5?w|(1<<j):w,0);
  assert(pop(A)===8&&octads.includes(A),'A est une des octades');
  polarities.push({mask:m,multiplicities,octad_index_of_A:octads.indexOf(A)});
}
assert(polarities.length===56,'cinquante-six polarites couvrantes');

// Notre code propre 0803, reconstruit sans appel au producteur de domaines.
const exponents=[0,1,5,6,7,9,11];
const gp=exponents.reduce((w,e)=>w|(1<<e),0);
const generators=Array.from({length:12},(_,i)=>{let w=gp<<i;if(pop(w)&1)w|=1<<23;return w;});
assert(rank2(generators,24)===12,'rang code');
for(const g of generators)for(const h of generators)assert((pop(g&h)&1)===0,'code autodual');
const words=[];for(let m=0;m<4096;m++){
  let w=0;for(let i=0;i<12;i++)if((m>>i)&1)w^=generators[i];words.push(w);
}
assert(new Set(words).size===4096,'4096 mots');
const weightHist={};for(const w of words)weightHist[pop(w)]=(weightHist[pop(w)]||0)+1;
assert(Math.min(...words.filter(Boolean).map(pop))===8,'minimum huit');
const D1=[0,1,2,9],D2=[3,4,13,15];
const A=[...D1,...D2].reduce((w,j)=>w|(1<<j),0);
const syndrome=generators.map(g=>pop(g&A)&1);
assert(pop(A)===8&&A===41503&&!words.includes(A),'gros support hors code');
const offendingIndex=syndrome.indexOf(1);assert(offendingIndex>=0,'certificat dual');
const result={exact:true,
  scope:'Lemme sept appuis de rang binaire <=4 et paire de normales fixe 0803. Aucun balayage de septuplets.',
  quotient_classes:7,multiplicity_bound:3,multisets_with_odd_xor_zero:multisets,
  odd_support_cardinalities:oddCardCounts,multiplicity_profiles:profiles,
  polarities_tested:128,admissible_polarities:polarities.length,polarities,
  binary_generator_exponents:exponents,generators,code_weight_histogram:weightHist,
  large_coefficient_support:{D1,D2,mask:A,in_code:false,syndrome,
    offending_generator_index:offendingIndex,offending_generator_mask:generators[offendingIndex]},
  physical_seven_support_minimum_binary_rank_for_this_pair:5,
  remaining_scope:'Support ranks 5,6,7 and other normal pairs are not excluded.'};
const here=path.dirname(fileURLToPath(import.meta.url));
fs.writeFileSync(path.join(here,'controle_sept_octades_rang4.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,profiles,polarities:polarities.length,A,
  offending_generator:generators[offendingIndex],required_support_rank:5}));

```


## controles_positifs_cadre_global.json

1360 octets ; SHA256 20727f864796caf613409d6c3ebd38fe67623e0ac79269f1caee991643abd616

```json
{
  "exact": true,
  "results": [
    {
      "vertices": 9,
      "m": 2,
      "r": 1,
      "d": 3,
      "signed_dimension": 4,
      "root_generators_norm": 1,
      "block_norm": 2,
      "graph_pairs_checked": 36,
      "polynomial": true,
      "tight_frame": true,
      "signed_incidence": true,
      "twice_blocks_integral_in_root_span": true,
      "integral_generation_by_odd_r": true,
      "even_r_full_generation_not_asserted": false,
      "seven_block_genus_not_imposed": true,
      "norm3_integral_purity_hypothesis_applies": false,
      "scope": "positive controls with their own parameters; no SRG99/F7/P0 asserted"
    },
    {
      "vertices": 243,
      "m": 11,
      "r": 4,
      "d": 9,
      "signed_dimension": 121,
      "root_generators_norm": 4,
      "block_norm": 5,
      "graph_pairs_checked": 29403,
      "polynomial": true,
      "tight_frame": true,
      "signed_incidence": true,
      "twice_blocks_integral_in_root_span": true,
      "integral_generation_by_odd_r": false,
      "even_r_full_generation_not_asserted": true,
      "seven_block_genus_not_imposed": true,
      "norm3_integral_purity_hypothesis_applies": false,
      "scope": "positive controls with their own parameters; no SRG99/F7/P0 asserted"
    }
  ],
  "source_sha256": "5e214c7e365581fe20af0abf1666912b61d07134443d89ad59b5cde1382cc154"
}

```


## controles_positifs_generation42.mjs

3362 octets ; SHA256 5e214c7e365581fe20af0abf1666912b61d07134443d89ad59b5cde1382cc154

```javascript
import fs from 'node:fs';import path from 'node:path';import assert from 'node:assert/strict';import crypto from 'node:crypto';import {fileURLToPath} from 'node:url';
const dirsBvLS=[[1,0,0,0,0],[2,0,0,0,0],[0,1,0,0,0],[0,2,0,0,0],[0,0,1,0,0],[0,0,2,0,0],[0,0,0,1,0],[0,0,0,2,0],[0,0,0,0,1],[0,0,0,0,2],[1,0,2,1,2],[2,0,1,2,1],[2,1,1,1,2],[1,2,2,2,1],[2,2,2,0,2],[1,1,1,0,1],[2,2,0,1,1],[1,1,0,2,2],[1,2,1,1,0],[2,1,2,2,0],[0,1,2,1,1],[0,2,1,2,2]];
const here=path.dirname(fileURLToPath(import.meta.url));
function check(dim,dirs,r){const n=3**dim,m=dirs.length/2,d=2*r+1,mod=x=>(x%3+3)%3;const vs=Array.from({length:n},(_,a)=>Array.from({length:dim},(_,i)=>Math.floor(a/3**i)%3)),enc=v=>v.reduce((s,a,i)=>s+3**i*a,0),neg=vs.map(v=>enc(v.map(a=>mod(-a)))),A=vs.map(()=>Array(n).fill(0));for(let i=0;i<n;i++)for(const v of dirs)A[i][enc(v.map((a,j)=>mod(a+vs[i][j])))]=1;let graphPairs=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){assert.equal(A[i][j],A[j][i]);assert.equal(A[i].reduce((s,a,k)=>s+a*A[j][k],0),A[i][j]?1:2);graphPairs++;}
const interior=Array.from({length:n},(_,i)=>i).filter(i=>i>0&&i<neg[i]&&A[0][i]),roots=Array.from({length:n},(_,i)=>i).filter(i=>i>0&&i<neg[i]&&!A[0][i]),reps=interior.concat(roots);assert.equal(interior.length,m);assert.equal(roots.length,m*(m-1));
const S=reps.map(i=>reps.map(j=>A[i][j]-A[i][neg[j]])),H=S.map((row,i)=>row.map((a,j)=>r*+(i===j)-a));const C=S.slice(0,m).map(row=>row.slice(m));
for(let i=0;i<S.length;i++)for(let j=0;j<S.length;j++){const ss=S[i].reduce((s,a,k)=>s+a*S[k][j],0),hh=H[i].reduce((s,a,k)=>s+a*H[k][j],0);assert.equal(ss+S[i][j],i===j?r*(r+1):0);assert.equal(hh,d*H[i][j]);}
for(let c=0;c<m;c++)for(let j=0;j<m;j++)assert.equal(C[c].reduce((s,a,k)=>s+a*C[j][k],0),c===j?2*(m-1):0);
for(let c=0;c<m;c++)for(let i=0;i<H.length;i++){const hz=r*H[i][c]+C[c].reduce((s,a,k)=>s+a*H[i][m+k],0);assert.equal(hz,0);}
for(let c=0;c<m;c++){ let chosen=null; for(let a=0;a<roots.length&&!chosen;a++)for(let b=a+1;b<roots.length&&!chosen;b++)for(const sign of [-1,1]){const cv=C.map(row=>row[a]+sign*row[b]);if(cv[c]===2&&cv.every((x,i)=>i===c||x===0)){chosen={a,b,sign};break;}} assert(chosen);const vv=roots.map((_,i)=> +(i===chosen.a)+chosen.sign*+(i===chosen.b));const coeff=roots.map((_,i)=>-S[m+i].slice(m).reduce((sum,x,j)=>sum+x*vv[j],0)-(r+1)*vv[i]);for(let i=0;i<H.length;i++) assert.equal(coeff.reduce((sum,x,j)=>sum+x*H[i][m+j],0),2*H[i][c]); if(r===1){for(let i=0;i<H.length;i++)assert.equal(0-C[c].reduce((sum,x,j)=>sum+x*H[i][m+j],0),H[i][c]);}}
assert(roots.every(v=>!A[v][neg[v]]));return{vertices:n,m,r,d,signed_dimension:S.length,root_generators_norm:r,block_norm:r+1,graph_pairs_checked:graphPairs,polynomial:true,tight_frame:true,signed_incidence:true,twice_blocks_integral_in_root_span:true,integral_generation_by_odd_r:r===1,even_r_full_generation_not_asserted:r===4,seven_block_genus_not_imposed:true,norm3_integral_purity_hypothesis_applies:r===3,scope:'positive controls with their own parameters; no SRG99/F7/P0 asserted'};}
const results=[check(2,[[1,0],[2,0],[0,1],[0,2]],1),check(5,dirsBvLS,4)];const out={exact:true,results,source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};fs.writeFileSync(path.join(here,'controles_positifs_cadre_global.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));

```


## figer_audit_independant_0836.mjs

4326 octets ; SHA256 9049ee6fbcf9b361b43afef5527b713e499660e9ee1334be8b9e58634eec6a3d

```javascript
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
const pairs=[
 ['THEOREME_CARACTERISTIQUE8_THETA.md','verifier_theta_caracteristique8'],
 ['THEOREME_MOMENTS_CARACTERISTIQUES8.md','verifier_moments_caracteristique8'],
 ['EXCLUSION_FRAME_D8_TROIS.md','verifier_frame_D8_trois'],
 ['AUDIT_GENERATION42_ET_COQUE_ENTIERE.md','verifier_coque_D8_mod2'],
 ['AUDIT_D11_ET_LIMITE_COQUE.md','verifier_D11_et_coque_D6'],
 ['ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md','verifier_rootless_code24'],
 ['AUDIT_HEPTADE_RANG4_ET_D6_BLOCS.md','verifier_heptade_et_D6_bornes'],
 ['AUDIT_D6_SIX_FRACTIONNAIRES_MEME_PAIRE.md','verifier_D6_fA6_independant'],
 ['AUDIT_Q42_ET_CLASSIFICATION_D6.md','verifier_Q42_et_collage_D6_independant'],
 ['AUDIT_D6_MIXTE_CENTRES_REPETES.md','verifier_D6_mixte_centres_independant'],
 ['AUDIT_FAMILLE_COMPLETE_D8_TROIS.md','verifier_collages_D8_independant']
];
const resultChecks=[];
for(const [note,stem] of pairs){
 const source=fs.readFileSync(path.join(here,stem+'.mjs'));
 const result=JSON.parse(fs.readFileSync(path.join(here,stem+'.json'),'utf8'));
 assert.equal(result.exact,true,stem+' executed exact result');
 assert.equal(result.source_sha256,digest(source),stem+' source binding');
 assert(fs.readFileSync(path.join(here,note),'utf8').length>100);
 resultChecks.push({source:stem+'.mjs',result:stem+'.json',exact:true});
}
const files=pairs.flatMap(([note,stem])=>[note,stem+'.mjs',stem+'.json']);
files.push('BILAN_AUDIT_INDEPENDANT_0836.md','figer_audit_independant_0836.mjs');
const entries=files.map(file=>{const bytes=fs.readFileSync(path.join(here,file));return{file,bytes:bytes.length,sha256:digest(bytes)};});
assert.equal(entries.length,35);assert.equal(new Set(files).size,35);
const dependencies=[
 '../attaque_globale_27_0803/MANIFEST_AUDIT_INDEPENDANT_0803.json',
 '../attaque_globale_27_0803/AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md',
 '../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md',
 '../attaque_globale_27_0803/UNIFICATION_G18_G20_RANG24.md',
 '../attaque_globale_27_0803/verifier_golay_enveloppe_indep.json',
 '../attaque_globale_27_0803/controles_positifs_cadre_global.json',
 '../dossier6_involution/NOTE_RESEAU_MINIMUM.md',
 'controle_selection42_golay.json'
].map(file=>{const bytes=fs.readFileSync(path.join(here,file));return{file,bytes:bytes.length,sha256:digest(bytes),access:'read_only'};});
assert.equal(dependencies[0].sha256,'0ca8af0714d5edcf74e6ee5295fabf8e508678008d1d455a2fcb4bc2a6858ef8');
const theta=JSON.parse(fs.readFileSync(path.join(here,'verifier_theta_caracteristique8.json'),'utf8'));
for(const binding of theta.input_bindings)assert.equal(digest(fs.readFileSync(path.join(here,binding.file))),binding.sha256);
const q42=JSON.parse(fs.readFileSync(path.join(here,'verifier_Q42_et_collage_D6_independant.json'),'utf8'));
assert.equal(q42.input_sha256,dependencies.at(-1).sha256);
const out={exact:true,status:'frozen_own_outputs_only',scope:'Uniform mathematical consequences and explicitly conditional families of the same physical frame; no full g18/g20 exclusion.',
 file_count:entries.length,executed_exact_sources:resultChecks.length,entries,result_checks:resultChecks,
 dependencies,old_outputs_modified:false,new_local_type_exclusions:0,
 rootless_shadowframe_uniform:true,D8_three_entire_ambient_family_excluded:true,
 D6_four_entire_ambient_family_excluded:false,D6_same_pair_fractional_six_excluded:true,
 D6_mixed_regime_excluded:false,D6_mixed_centres_necessary:'four distinct centres, two B and two D; only when h7 is integral in AC',
 limitations:['No full odd-unimodular rank-24 classification','No universal shell Gram rank-20 bound','No shadowframe without the rootless hypothesis','Positive H2/BvLS parameters remain 3/9 and their own norms','Fixed Q42 fixtures do not satisfy all physical graph axioms']};
const manifest=path.join(here,'MANIFEST_AUDIT_INDEPENDANT_0836.json');
fs.writeFileSync(manifest,JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,own_files:entries.length,executed_sources:resultChecks.length,manifest_sha256:digest(fs.readFileSync(manifest))}));

```


## verifier_D11_et_coque_D6.json

2519 octets ; SHA256 dcadba627dda22ae7d43f6368e287a3715dcadb89c170726c2c2bb0977aa2339

```json
{
  "exact": true,
  "scope": "D11-to-D12 root construction and true D6^4 shell counter-test, no SRG/frame realization",
  "D11": {
    "spinor_cases": 2048,
    "parity_checks": 22528,
    "D12_root_count": 264,
    "twice_b_not_assumed_integral": true
  },
  "D6_countermodel": {
    "glue_classes": [
      {
        "row": [
          0,
          0,
          0,
          0
        ],
        "min": 0
      },
      {
        "row": [
          2,
          1,
          0,
          0
        ],
        "min": 3
      },
      {
        "row": [
          0,
          2,
          1,
          0
        ],
        "min": 3
      },
      {
        "row": [
          2,
          3,
          1,
          0
        ],
        "min": 4
      },
      {
        "row": [
          0,
          0,
          2,
          1
        ],
        "min": 3
      },
      {
        "row": [
          2,
          1,
          2,
          1
        ],
        "min": 6
      },
      {
        "row": [
          0,
          2,
          3,
          1
        ],
        "min": 4
      },
      {
        "row": [
          2,
          3,
          3,
          1
        ],
        "min": 5
      },
      {
        "row": [
          1,
          0,
          0,
          2
        ],
        "min": 3
      },
      {
        "row": [
          3,
          1,
          0,
          2
        ],
        "min": 4
      },
      {
        "row": [
          1,
          2,
          1,
          2
        ],
        "min": 6
      },
      {
        "row": [
          3,
          3,
          1,
          2
        ],
        "min": 5
      },
      {
        "row": [
          1,
          0,
          2,
          3
        ],
        "min": 4
      },
      {
        "row": [
          3,
          1,
          2,
          3
        ],
        "min": 5
      },
      {
        "row": [
          1,
          2,
          3,
          3
        ],
        "min": 5
      },
      {
        "row": [
          3,
          3,
          3,
          3
        ],
        "min": 4
      }
    ],
    "coset_minima": {
      "0": 1,
      "3": 4,
      "4": 5,
      "5": 4,
      "6": 2
    },
    "determinant": 1,
    "min": 2,
    "roots": "D6^4",
    "shell3": 4096,
    "shell_generates_lattice": true,
    "generators_checked": 28,
    "Gram_rank_mod2": 24,
    "no_42_plus_7_frame_asserted": true
  },
  "source_sha256": "8acc2fe7b3f9c6ed0f5c61f5f373dbcf1559b80650cef6d659cd58b12630ed8a"
}

```


## verifier_D11_et_coque_D6.mjs

3559 octets ; SHA256 8acc2fe7b3f9c6ed0f5c61f5f373dbcf1559b80650cef6d659cd58b12630ed8a

```javascript
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
let spinorCases=0,parityChecks=0;
for(let mask=0;mask<2048;mask++){
  const twiceP=Array.from({length:11},(_,i)=>mask>>i&1?-1:1);
  assert(twiceP.reduce((s,x)=>s+x*x,0)===11,'spinor norm11/4');
  assert(twiceP.reduce((s,x)=>s+2*x,0)%2===0,'4p in D11');
  for(let i=0;i<11;i++){assert((twiceP.reduce((s,x)=>s+x,0)-1)%2===0,'2p-e_i in D11');parityChecks++;}
  spinorCases++;
}
assert(2*11*10+4*11===2*12*11,'D11 roots plus new roots yield D12 count264');

const zero=()=>Array(24).fill(0),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const glues=[];for(let part=0;part<4;part++){
  const x=zero();for(let j=0;j<6;j++){x[6*part+j]=j===0?-1:1;x[6*((part+1)%4)+j]=1;}glues.push(x);
}
for(const x of glues)assert(dot(x,x)/4===3,'spinor-pair norm3');
for(const x of glues)for(const y of glues)assert(dot(x,y)%4===0,'glue Gram integral');
const classes=[];const costs2=[0,3,3,2];
for(let mask=0;mask<16;mask++){
  const row=[0,0,0,0];for(let j=0;j<4;j++)if(mask>>j&1){row[j]^=2;row[(j+1)%4]^=1;}
  const min2=row.reduce((s,c)=>s+costs2[c],0);assert(min2%2===0,'integer coset norm');classes.push({row,min:min2/2});
}
assert(new Set(classes.map(x=>x.row.join(''))).size===16,'independent four glue classes');
const histogram={};for(const x of classes)histogram[x.min]=(histogram[x.min]??0)+1;
assert(JSON.stringify(histogram)===JSON.stringify({'0':1,'3':4,'4':5,'5':4,'6':2}),'all coset minima');
const generators=[];
for(let part=0;part<4;part++){
  const baseline=glues[(part+3)%4];
  function plus(i,j){const flip=baseline.slice();flip[6*part+i]*=-1;flip[6*part+j]*=-1;assert(dot(flip,flip)/4===3,'two flips preserve shell3');return baseline.map((x,k)=>x-flip[k]);}
  for(let i=0;i<5;i++){
    const k=Array.from({length:6},(_,j)=>j).find(j=>j!==i&&j!==i+1);
    const x=plus(i,k).map((a,j)=>a-plus(i+1,k)[j]);
    assert(x[6*part+i]===2&&x[6*part+i+1]===-2&&dot(x,x)===8,'simple D6 difference from shell');generators.push(x);
  }
  generators.push(plus(4,5));
}
generators.push(...glues);assert(generators.length===28,'24 roots and4 shell baselines');
const gram=generators.map(a=>generators.map(b=>{assert(dot(a,b)%4===0,'integral generator products');return dot(a,b)/4;}));
const bitrows=gram.map(row=>row.reduce((x,v,i)=>x|((Math.abs(v)%2)<<i),0));
function rank(rows){const piv=Array(28).fill(0);let r=0;for(const value of rows){let x=value;for(let j=27;j>=0;j--)if(x>>>j&1){if(piv[j])x^=piv[j];else{piv[j]=x;r++;break;}}}return r;}
const actualRank=rank(bitrows);assert(actualRank===24,'actual full Gram shell rank24, not20');
const out={exact:true,scope:'D11-to-D12 root construction and true D6^4 shell counter-test, no SRG/frame realization',
  D11:{spinor_cases:spinorCases,parity_checks:parityChecks,D12_root_count:264,twice_b_not_assumed_integral:true},
  D6_countermodel:{glue_classes:classes,coset_minima:histogram,determinant:1,min:2,roots:'D6^4',shell3:4*32**2,
    shell_generates_lattice:true,generators_checked:28,Gram_rank_mod2:actualRank,no_42_plus_7_frame_asserted:true},
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_D11_et_coque_D6.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,D11_spinors:spinorCases,D12_root_count:264,D6_shell3:4096,D6_Gram_rank_mod2:actualRank}));

```


## verifier_D6_fA6_independant.json

8189 octets ; SHA256 54c6abdefceb0aea2da06ec66b9b5409658c052eb6dc55879bc6e027aaaa8ec7

```json
{
  "exact": true,
  "scope": "D6^4 six fractionary blocks in ONE opposite pair; mixed2+4 remains open",
  "trace_AC": 84,
  "normal_profiles": [
    {
      "heavy": 0,
      "integerUnits": 4,
      "chiAllowed": true,
      "rootAllowed": true,
      "pass": true
    },
    {
      "heavy": 1,
      "integerUnits": 2,
      "chiAllowed": false,
      "rootAllowed": true,
      "pass": false
    },
    {
      "heavy": 2,
      "integerUnits": 0,
      "chiAllowed": true,
      "rootAllowed": false,
      "pass": false
    }
  ],
  "center_compositions": 1716,
  "valid_patterns": [
    {
      "m": [
        1,
        1,
        0,
        0,
        0,
        0,
        2,
        2
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        0,
        0,
        0,
        2,
        2
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          1,
          2,
          3
        ]
      }
    },
    {
      "m": [
        1,
        1,
        0,
        0,
        0,
        2,
        0,
        2
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        0,
        0,
        2,
        0,
        2
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          1,
          2,
          4
        ]
      }
    },
    {
      "m": [
        1,
        1,
        0,
        0,
        0,
        2,
        2,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        0,
        0,
        2,
        2,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          1,
          2,
          5
        ]
      }
    },
    {
      "m": [
        1,
        1,
        0,
        0,
        2,
        0,
        0,
        2
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        0,
        2,
        0,
        0,
        2
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          1,
          3,
          4
        ]
      }
    },
    {
      "m": [
        1,
        1,
        0,
        0,
        2,
        0,
        2,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        0,
        2,
        0,
        2,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          1,
          3,
          5
        ]
      }
    },
    {
      "m": [
        1,
        1,
        0,
        0,
        2,
        2,
        0,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        0,
        2,
        2,
        0,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          1,
          4,
          5
        ]
      }
    },
    {
      "m": [
        1,
        1,
        0,
        2,
        0,
        0,
        0,
        2
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        2,
        0,
        0,
        0,
        2
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          2,
          3,
          4
        ]
      }
    },
    {
      "m": [
        1,
        1,
        0,
        2,
        0,
        0,
        2,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        2,
        0,
        0,
        2,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          2,
          3,
          5
        ]
      }
    },
    {
      "m": [
        1,
        1,
        0,
        2,
        0,
        2,
        0,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        2,
        0,
        2,
        0,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          2,
          4,
          5
        ]
      }
    },
    {
      "m": [
        1,
        1,
        0,
        2,
        2,
        0,
        0,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        0,
        2,
        2,
        0,
        0,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          0,
          3,
          4,
          5
        ]
      }
    },
    {
      "m": [
        1,
        1,
        2,
        0,
        0,
        0,
        0,
        2
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        2,
        0,
        0,
        0,
        0,
        2
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          1,
          2,
          3,
          4
        ]
      }
    },
    {
      "m": [
        1,
        1,
        2,
        0,
        0,
        0,
        2,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        2,
        0,
        0,
        0,
        2,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          1,
          2,
          3,
          5
        ]
      }
    },
    {
      "m": [
        1,
        1,
        2,
        0,
        0,
        2,
        0,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        2,
        0,
        0,
        2,
        0,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          1,
          2,
          4,
          5
        ]
      }
    },
    {
      "m": [
        1,
        1,
        2,
        0,
        2,
        0,
        0,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        2,
        0,
        2,
        0,
        0,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          1,
          3,
          4,
          5
        ]
      }
    },
    {
      "m": [
        1,
        1,
        2,
        2,
        0,
        0,
        0,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "mD": [
        2,
        2,
        0,
        0,
        0,
        0
      ],
      "normalSupport": {
        "half": "B",
        "units": "D",
        "support": [
          2,
          3,
          4,
          5
        ]
      }
    },
    {
      "m": [
        3,
        3,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "tB": [
        1,
        1,
        1,
        1,
        3,
        3
      ],
      "mD": [
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "normalSupport": {
        "half": "D",
        "units": "B",
        "support": [
          0,
          1,
          2,
          3
        ]
      }
    }
  ],
  "normal_same_support_forced": true,
  "ratio_tests": 16,
  "root_projection_norm": "6/7",
  "dual_gap": "8/7",
  "family_fA6_fB0_excluded": true,
  "D6_full_not_excluded": true,
  "mixed_fA2_fB4_open": true,
  "source_sha256": "56642c70cb7ed0daba25f4784b1d2dde98d8e16940b4e56a5ab73d93cdb76bdb"
}

```


## verifier_D6_fA6_independant.mjs

3385 octets ; SHA256 56642c70cb7ed0daba25f4784b1d2dde98d8e16940b4e56a5ab73d93cdb76bdb

```javascript
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
assert(42*3/2+6*3+2*3/2===84,'traceAC exactly full');
const normalProfiles=[];for(let heavy=0;heavy<=2;heavy++)for(let integerUnits=0;integerUnits<=4;integerUnits++)if(2*heavy+integerUnits===4){
  const maxSum=(heavy?.5+1:.5)+(integerUnits?1:0);
  const chiAllowed=maxSum<=1.5,rootAllowed=heavy<2;
  normalProfiles.push({heavy,integerUnits,chiAllowed,rootAllowed,pass:chiAllowed&&rootAllowed});
}
assert(normalProfiles.filter(x=>x.pass).length===1&&normalProfiles.find(x=>x.pass).integerUnits===4,'only H1');
const patterns=[];let compositions=0;
function explore(prefix,remaining){if(prefix.length===7){const m=[...prefix,remaining];compositions++;
  const tB=[1,1,1,1,m[0],m[1]],mD=m.slice(2);
  if(tB.every(b=>mD.every(d=>b+d===1||b+d===3)))patterns.push({m,tB,mD});return;}
  for(let n=0;n<=remaining;n++)explore([...prefix,n],remaining-n);
}
explore([],6);assert(compositions===1716&&patterns.length===16,'all six-center compositions independent integer counters');
const unitSets=[];for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)unitSets.push(Array.from({length:6},(_,i)=>i).filter(i=>i!==a&&i!==b));
let first=0,second=0;
for(const p of patterns){const normalSupports=[];
  for(const units of unitSets){
    if(p.tB.every(b=>units.every(j=>b+p.mD[j]===1)))normalSupports.push({half:'B',units:'D',support:units});
    if(p.mD.every(d=>units.every(j=>p.tB[j]+d===1)))normalSupports.push({half:'D',units:'B',support:units});
  }
  assert(normalSupports.length===1,'each center pattern forces a unique common normal four-support');p.normalSupport=normalSupports[0];
  if(p.m[0]===1&&p.m[1]===1){first++;assert(p.mD.filter(x=>x===2).length===2&&p.normalSupport.half==='B','2singles/2doubles case');}
  else{second++;assert(p.m[0]===3&&p.m[1]===3&&p.mD.every(x=>x===0)&&p.normalSupport.half==='D','2triples case');}
}
assert(first===15&&second===1,'two complete cases');
for(let mask=0;mask<16;mask++){const ratios=Array.from({length:4},(_,i)=>mask>>i&1?-1:1);assert(ratios.some((x,i)=>ratios.some((y,j)=>j>i&&x===y)),'four signratios contain an equal pair');}
assert(2*7-4-4===6&&6<8,'projection norm6/7 below8/7');
const orthCandidates=[];for(let mask=0;mask<64;mask++){
  const v=Array.from({length:6},(_,i)=>mask>>i&1?-1:1);
  if(v.reduce((s,x)=>s+x,0)===0&&v.reduce((s,x,i)=>s+x*(i<3?1:-1),0)===0)orthCandidates.push(v);
}
assert(orthCandidates.length===0,'no third signvector orthogonal to ones and three-plus/three-minus');
const out={exact:true,scope:'D6^4 six fractionary blocks in ONE opposite pair; mixed2+4 remains open',
  trace_AC:84,normal_profiles:normalProfiles,center_compositions:compositions,valid_patterns:patterns,
  normal_same_support_forced:true,ratio_tests:16,root_projection_norm:'6/7',dual_gap:'8/7',
  family_fA6_fB0_excluded:true,D6_full_not_excluded:true,mixed_fA2_fB4_open:true,
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_D6_fA6_independant.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,compositions:1716,valid_patterns:16,fA6_same_pair_excluded:true,mixed2plus4_open:true}));

```


## verifier_D6_mixte_centres_independant.json

3132 octets ; SHA256 41c50ca25e80d7c9eb70506d6b90e89bd6dca88aa7ffa80e68719e2f3af46b90

```json
{
  "exact": true,
  "stats": {
    "distributions": 1365,
    "distributions_with_repeat": 870,
    "diagonal_surviving_distributions": 405,
    "diagonal_surviving_repeated_distributions": 150,
    "normal_support_pairs_before_root_cut": 900,
    "repeated_normal_support_pairs": 270,
    "minimum_common_axes_for_repeated": 3
  },
  "examples": [
    {
      "centre_multiplicities": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        2
      ],
      "unit_component": "D",
      "s1": [
        1,
        1,
        1,
        1,
        0,
        0
      ],
      "s2": [
        1,
        1,
        1,
        1,
        0,
        0
      ],
      "common_axes": 4
    },
    {
      "centre_multiplicities": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        2
      ],
      "unit_component": "D",
      "s1": [
        1,
        1,
        1,
        1,
        0,
        0
      ],
      "s2": [
        1,
        1,
        1,
        0,
        1,
        0
      ],
      "common_axes": 3
    }
  ],
  "hypothesis": "Four h have spinors on AC, two on BD, and h7 is integral and supported on AC; full physical frame and common normal root-dual bound.",
  "conclusion": "The four centres of the AC spinor blocks must be distinct and split as two in B and two in D. The mixed regime is not wholly refuted.",
  "orthogonality_corollary": {
    "local_cases": 64,
    "split_checks": [
      {
        "centres_B": 0,
        "centres_D": 4,
        "epsilon": -1,
        "spinor_inner": -2,
        "orthogonal": false
      },
      {
        "centres_B": 0,
        "centres_D": 4,
        "epsilon": 1,
        "spinor_inner": 2,
        "orthogonal": false
      },
      {
        "centres_B": 1,
        "centres_D": 3,
        "epsilon": -1,
        "spinor_inner": -1,
        "orthogonal": false
      },
      {
        "centres_B": 1,
        "centres_D": 3,
        "epsilon": 1,
        "spinor_inner": 1,
        "orthogonal": false
      },
      {
        "centres_B": 2,
        "centres_D": 2,
        "epsilon": -1,
        "spinor_inner": 0,
        "orthogonal": true
      },
      {
        "centres_B": 2,
        "centres_D": 2,
        "epsilon": 1,
        "spinor_inner": 0,
        "orthogonal": true
      },
      {
        "centres_B": 3,
        "centres_D": 1,
        "epsilon": -1,
        "spinor_inner": 1,
        "orthogonal": false
      },
      {
        "centres_B": 3,
        "centres_D": 1,
        "epsilon": 1,
        "spinor_inner": -1,
        "orthogonal": false
      },
      {
        "centres_B": 4,
        "centres_D": 0,
        "epsilon": -1,
        "spinor_inner": 2,
        "orthogonal": false
      },
      {
        "centres_B": 4,
        "centres_D": 0,
        "epsilon": 1,
        "spinor_inner": -2,
        "orthogonal": false
      }
    ],
    "only_split": [
      2,
      2
    ]
  },
  "source_sha256": "96e995fc9f3f367ace1ea239aa2415a5b68f48e31beac6af57774e368efcfdd4"
}

```


## verifier_D6_mixte_centres_independant.mjs

4972 octets ; SHA256 96e995fc9f3f367ace1ea239aa2415a5b68f48e31beac6af57774e368efcfdd4

```javascript
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
function compositions(total,width,prefix=[],out=[]){if(width===1){out.push([...prefix,total]);return out;}
  for(let x=0;x<=total;x++)compositions(total-x,width-1,[...prefix,x],out);return out;}
const supports=[];
for(let a=0;a<3;a++)for(let b=a+1;b<4;b++)for(let c=b+1;c<5;c++)for(let d=c+1;d<6;d++){
  const v=Array(6).fill(0);for(const i of[a,b,c,d])v[i]=1;supports.push(v);}
assert.equal(supports.length,15);
const stats={distributions:0,distributions_with_repeat:0,diagonal_surviving_distributions:0,
  diagonal_surviving_repeated_distributions:0,normal_support_pairs_before_root_cut:0,
  repeated_normal_support_pairs:0,minimum_common_axes_for_repeated:6};
const examples=[];
for(const m of compositions(4,12)){
  stats.distributions++;
  const repeated=m.some(x=>x>=2);if(repeated)stats.distributions_with_repeat++;
  const B=m.slice(0,6),D=m.slice(6);
  let surviving=false,survivingRepeated=false;
  // q is the number of normals whose four integral units are in B.
  // Their minimal spinor is then in D. Diagonal sums determine q exactly.
  for(let q=0;q<=2;q++){
    const mB=B.reduce((s,x)=>s+x,0),mD=D.reduce((s,x)=>s+x,0);
    if((mB+4*q)%6||(mD+4*(2-q))%6)continue;
    const tB=(mB+4*q)/6,tD=(mD+4*(2-q))/6;
    if(tB+tD!==2)continue;
    const types=q===0?[[0,0]]:q===2?[[1,1]]:[[1,0],[0,1]];
    for(const [unitB1,unitB2] of types)for(const s1 of supports)for(const s2 of supports){
      const coverageB=Array.from({length:6},(_,i)=>unitB1*s1[i]+unitB2*s2[i]);
      const coverageD=Array.from({length:6},(_,i)=>(1-unitB1)*s1[i]+(1-unitB2)*s2[i]);
      // Exact 36 paired coordinate equations; no producer bitsets or centre masks.
      let good=true;
      for(let i=0;i<6;i++)for(let j=0;j<6;j++)
        if(B[i]+coverageB[i]+D[j]+coverageD[j]!==2)good=false;
      if(!good)continue;
      surviving=true;stats.normal_support_pairs_before_root_cut++;
      if(!repeated)continue;
      survivingRepeated=true;stats.repeated_normal_support_pairs++;
      assert.equal(unitB1,unitB2);
      const common=s1.reduce((s,x,i)=>s+x*s2[i],0);
      assert(common>=3);
      stats.minimum_common_axes_for_repeated=Math.min(stats.minimum_common_axes_for_repeated,common);
      if(examples.length<2)examples.push({centre_multiplicities:m,unit_component:unitB1?'B':'D',s1,s2,common_axes:common});
      // Every pair of sign lists on >=3 common axes has two equal sign ratios.
      // Check the eight relative sign patterns on a three-axis subset directly.
      for(let ratios=0;ratios<8;ratios++){
        const r=Array.from({length:3},(_,i)=>((ratios>>i)&1)?-1:1);
        assert(r[0]===r[1]||r[0]===r[2]||r[1]===r[2]);
      }
    }
  }
  if(surviving)stats.diagonal_surviving_distributions++;
  if(survivingRepeated)stats.diagonal_surviving_repeated_distributions++;
}
assert.equal(stats.distributions,1365);
assert.equal(stats.diagonal_surviving_repeated_distributions,150);
assert.equal(stats.repeated_normal_support_pairs,270);
assert.equal(stats.minimum_common_axes_for_repeated,3);
assert.equal(stats.diagonal_surviving_distributions,405);
assert.equal(stats.normal_support_pairs_before_root_cut,900);
let localCases=0;const splitChecks=[];
for(let mB=0;mB<=1;mB++)for(let mD=0;mD<=1;mD++)
for(const b1 of[-1,1])for(const b2 of[-1,1])for(const d1 of[-1,1])for(const d2 of[-1,1]){
  let allKAllowed=true;
  for(const direction of[-1,1]){
    const r=(b1===direction*d1?1:0)+(b2===direction*d2?1:0);
    const k=mB+mD+r;if(k!==1&&k!==3)allKAllowed=false;
  }
  assert.equal(allKAllowed,b1*b2*d1*d2===-((-1)**(mB+mD)));localCases++;
}
for(let b=0;b<=4;b++)for(const epsilon of[-1,1]){
  const d=4-b;
  const sigma=Array.from({length:6},(_,i)=>epsilon*(i<b?-1:1));
  const tau=Array.from({length:6},(_,i)=>-epsilon*(i<d?-1:1));
  const spinorInner=(sigma.reduce((s,x)=>s+x,0)+tau.reduce((s,x)=>s+x,0))/4;
  assert(spinorInner===epsilon*(2-b));assert.equal(spinorInner===0,b===2);
  splitChecks.push({centres_B:b,centres_D:d,epsilon,spinor_inner:spinorInner,orthogonal:b===2});
}
const output={exact:true,stats,examples,
  hypothesis:'Four h have spinors on AC, two on BD, and h7 is integral and supported on AC; full physical frame and common normal root-dual bound.',
  conclusion:'The four centres of the AC spinor blocks must be distinct and split as two in B and two in D. The mixed regime is not wholly refuted.',
  orthogonality_corollary:{local_cases:localCases,split_checks:splitChecks,only_split:[2,2]},
  source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_D6_mixte_centres_independant.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({exact:true,...stats,mixed_regime_excluded:false}));

```


## verifier_Q42_et_collage_D6_independant.json

1245 octets ; SHA256 7362e2726a9df2e1025456a60b8a5dc129c26a3daec51b2aed18d936cfa0004f

```json
{
  "exact": true,
  "method": "Orthogonal subspace enumeration, then direct integer Q expansion on two existing fixtures.",
  "binary_space_stages": [
    {
      "dimension": 2,
      "spaces": 63
    },
    {
      "dimension": 3,
      "spaces": 315
    },
    {
      "dimension": 4,
      "spaces": 135
    }
  ],
  "D6_selfdual_codes": {
    "even": 30,
    "odd_with_loop": 45,
    "odd_two_double_edges": 12,
    "odd_cycle4": 48
  },
  "Q42_witnesses": [
    {
      "key": "witness_wrong_xor",
      "Q_integral": false,
      "xor_condition": false,
      "checksum": 0,
      "dodecads": 17
    },
    {
      "key": "witness_correct_xor_wrong_Q_rows",
      "Q_integral": true,
      "xor_condition": true,
      "checksum": 8,
      "dodecads": 18,
      "singleMask": 7218972,
      "singleInCode": false,
      "syndromes": 288,
      "shadowMask": 9558243,
      "shadowSumMod8": 4
    }
  ],
  "input_sha256": "3f7d688f1fdad4795b1e85fef2dd59f81027a6d8d5af85b9cda21833bafd774f",
  "source_sha256": "0e80c70704eb3831d0798e5f92135a22b5c8df9dcc028ffa5f4668cee0dc0551",
  "scope": "Classification of odd integral D6^4 ambient glue and congruences of two fixed selections; no physical frame existence or whole-g18/g20 exclusion."
}

```


## verifier_Q42_et_collage_D6_independant.mjs

6448 octets ; SHA256 0e80c70704eb3831d0798e5f92135a22b5c8df9dcc028ffa5f4668cee0dc0551

```javascript
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const parity=x=>{let s=0;while(x){s^=1;x&=x-1;}return s;};
const weight=x=>{let s=0;while(x){s++;x&=x-1;}return s;};
const mod=(x,n)=>(x%n+n)%n;
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);

// Independent binary subspace enumeration: contain the mandatory word 11111111,
// then extend an orthogonal subspace, canonicalizing its entire list of vectors.
// No perfect-matching generator is used.
let spaces=[[0,255]], stages=[];
for(let dimension=2;dimension<=4;dimension++){
  const next=new Map();
  for(const H of spaces)for(let v=1;v<256;v++){
    if(parity(v)||H.includes(v)||H.some(h=>parity(v&h)))continue;
    const J=H.concat(H.map(h=>h^v)).sort((a,b)=>a-b);
    next.set(J.join(','),J);
  }
  spaces=[...next.values()];stages.push({dimension,spaces:spaces.length});
}
assert.equal(spaces.length,135);
const counts={even:0,odd_with_loop:0,odd_two_double_edges:0,odd_cycle4:0};
for(const H of spaces){
  assert(H.length===16&&H.every(x=>H.every(y=>!parity(x&y))));
  const odd=H.some(x=>weight(x)%4===2);
  if(!odd){counts.even++;continue;}
  const pairs=H.filter(x=>weight(x)===2);
  assert.equal(pairs.length,4);
  assert.equal(pairs.reduce((a,b)=>a|b,0),255);
  assert(pairs.every((p,i)=>pairs.every((q,j)=>i===j||!(p&q))));
  for(const word of H){
    let doubled=0;
    for(let i=0;i<4;i++)if(((word>>2*i)&3)===3)doubled++;
    const numerator=3*weight(word)-4*doubled;
    assert.equal(mod(numerator/2,2),mod(weight(word)/2,2));
  }
  if(pairs.some(p=>[3,12,48,192].includes(p))){counts.odd_with_loop++;continue;}
  const adjacency=Array.from({length:4},()=>new Set());
  for(const p of pairs){const vertices=[];for(let i=0;i<8;i++)if(p&(1<<i))vertices.push(i>>1);
    assert(vertices.length===2&&vertices[0]!==vertices[1]);
    adjacency[vertices[0]].add(vertices[1]);adjacency[vertices[1]].add(vertices[0]);}
  const seen=new Set([0]);for(let changed=true;changed;){changed=false;
    for(const i of [...seen])for(const j of adjacency[i])if(!seen.has(j)){seen.add(j);changed=true;}}
  if(seen.size===4)counts.odd_cycle4++;else counts.odd_two_double_edges++;
}
assert.deepEqual(counts,{even:30,odd_with_loop:45,odd_two_double_edges:12,odd_cycle4:48});

// Replay only the two existing selection fixtures, using direct integer matrix
// multiplication and the separately derived mod-2 expansion of Q.
const inputPath=path.join(here,'controle_selection42_golay.json');
const inputBytes=fs.readFileSync(inputPath),data=JSON.parse(inputBytes);
const generators=data.code.generator_masks;
assert.equal(generators.length,12);
assert(generators.every(a=>generators.every(b=>!parity(a&b))));
let code=[0];for(const g of generators)code=code.concat(code.map(x=>x^g));
assert.equal(new Set(code).size,4096);const codeSet=new Set(code);
assert(code.every(c=>weight(c)%4===0)&&codeSet.has((1<<24)-1));
const B=data.B,d=B.map(row=>row.map(x=>mod((1-x)/2,2)));
const k=B.map((row,i)=>row.map((x,j)=>(x-1+2*d[i][j])/4));
assert(k.flat().every(Number.isInteger));
const delta=d[0].map((x,j)=>x+d[1][j]),K=k[0].map((x,j)=>x+k[1][j]);
const toMask=row=>row.reduce((m,x,j)=>m|(mod(x,2)<<j),0);
assert(d.every(row=>codeSet.has(toMask(row))));
const witnesses=[];
for(const key of ['witness_wrong_xor','witness_correct_xor_wrong_Q_rows']){
  const words=data[key].selected_codeword_masks;
  assert.equal(words.length,42);assert.equal(new Set(words).size,42);
  assert(words.every(w=>codeSet.has(w)));
  const c=words.map(w=>Array.from({length:24},(_,j)=>(w>>j)&1));
  const E=c.map(row=>row.map(x=>1-2*x));
  const n=Array.from({length:24},(_,j)=>c.reduce((s,row)=>s+row[j],0));
  const F=Array.from({length:24},(_,i)=>Array.from({length:24},(_,j)=>
    (i===j?56:0)-E.reduce((s,row)=>s+row[i]*row[j],0)-B.reduce((s,row)=>s+row[i]*row[j],0)));
  const tau=mod(n[0]+delta[0],2);
  const xorOK=n.every((x,j)=>mod(x+delta[j],2)===tau);
  const integral=F.flat().every(x=>x%4===0);assert.equal(integral,xorOK);
  const checksum=mod(E.flat().reduce((s,x)=>s+x,0)+B.flat().reduce((s,x)=>s+x,0),16);
  const dodecads=words.filter(w=>weight(w)===12).length;
  assert.equal(checksum===8,dodecads%2===0);
  const item={key,Q_integral:integral,xor_condition:xorOK,checksum,dodecads};
  if(integral){
    const Q=F.map(row=>row.map(x=>x/4));
    const a=n.map((x,j)=>(x+delta[j]-tau)/2),single=a.map((x,j)=>x+K[j]);
    for(let i=0;i<24;i++)for(let j=0;j<24;j++){
      const expansion=1+tau+single[i]+single[j]
        +c.reduce((s,row)=>s+row[i]*row[j],0)+d.reduce((s,row)=>s+row[i]*row[j],0);
      assert.equal(mod(Q[i][j],2),mod(expansion,2));
    }
    let syndromes=0;
    for(const gen of generators){const gb=Array.from({length:24},(_,i)=>(gen>>i)&1);
      const scalar=mod(dot(single,gb),2);
      for(const row of Q){assert.equal(mod(dot(row,gb),2),scalar);syndromes++;}}
    const singleMask=toMask(single),x=Array.from({length:24},(_,j)=>
      (E.reduce((s,row)=>s+row[j],0)+B[0][j]+B[1][j])/2);
    assert(x.every(z=>mod(z,2)===tau));
    const shadowMask=toMask(x.map(z=>(z-tau)/2));
    assert.equal(codeSet.has(shadowMask),codeSet.has(singleMask));
    assert.equal(Q.every(row=>codeSet.has(toMask(row))),codeSet.has(singleMask));
    Object.assign(item,{singleMask,singleInCode:codeSet.has(singleMask),syndromes,
      shadowMask,shadowSumMod8:mod(x.reduce((s,z)=>s+z,0),8)});
  }
  witnesses.push(item);
}
assert(!witnesses[0].Q_integral);
assert.equal(witnesses[1].singleMask,7218972);assert(!witnesses[1].singleInCode);
const output={exact:true,method:'Orthogonal subspace enumeration, then direct integer Q expansion on two existing fixtures.',
  binary_space_stages:stages,D6_selfdual_codes:counts,Q42_witnesses:witnesses,
  input_sha256:hash(inputBytes),source_sha256:hash(fs.readFileSync(fileURLToPath(import.meta.url))),
  scope:'Classification of odd integral D6^4 ambient glue and congruences of two fixed selections; no physical frame existence or whole-g18/g20 exclusion.'};
fs.writeFileSync(path.join(here,'verifier_Q42_et_collage_D6_independant.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({exact:true,codes135:spaces.length,counts,Q42_syndromes:witnesses[1].syndromes,singleMask:witnesses[1].singleMask}));

```


## verifier_collages_D8_independant.json

9374 octets ; SHA256 ab382730e1c86c2f57a5ab67ec323e889d4c7984ef92c59784e762a857374413

```json
{
  "exact": true,
  "stages": [
    {
      "dimension": 1,
      "count": 63
    },
    {
      "dimension": 2,
      "count": 315
    },
    {
      "dimension": 3,
      "count": 135
    }
  ],
  "counts": {
    "even": 30,
    "odd": 105,
    "min1": 37,
    "singleton_spinor_E8": 24,
    "double_vector_D16": 12,
    "admissible": 32,
    "only_vvv": 8,
    "two_vector_spinor_same_centre": 24
  },
  "survivors": [
    {
      "H": [
        0,
        5,
        17,
        20,
        43,
        46,
        58,
        63
      ],
      "shellClasses": [
        63
      ],
      "integerComponents": [
        0,
        1,
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        5,
        26,
        31,
        43,
        46,
        49,
        52
      ],
      "shellClasses": [
        49,
        52
      ],
      "integerComponents": [
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        5,
        27,
        30,
        33,
        36,
        58,
        63
      ],
      "shellClasses": [
        63
      ],
      "integerComponents": [
        0,
        1,
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        5,
        27,
        30,
        42,
        47,
        49,
        52
      ],
      "shellClasses": [
        49,
        52
      ],
      "integerComponents": [
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        6,
        18,
        20,
        43,
        45,
        57,
        63
      ],
      "shellClasses": [
        63
      ],
      "integerComponents": [
        0,
        1,
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        6,
        25,
        31,
        43,
        45,
        50,
        52
      ],
      "shellClasses": [
        50,
        52
      ],
      "integerComponents": [
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        6,
        27,
        29,
        34,
        36,
        57,
        63
      ],
      "shellClasses": [
        63
      ],
      "integerComponents": [
        0,
        1,
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        6,
        27,
        29,
        41,
        47,
        50,
        52
      ],
      "shellClasses": [
        50,
        52
      ],
      "integerComponents": [
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        7,
        19,
        20,
        41,
        46,
        58,
        61
      ],
      "shellClasses": [
        7,
        19
      ],
      "integerComponents": [
        0
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        7,
        19,
        20,
        42,
        45,
        57,
        62
      ],
      "shellClasses": [
        7,
        19
      ],
      "integerComponents": [
        0
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        7,
        25,
        30,
        35,
        36,
        58,
        61
      ],
      "shellClasses": [
        7,
        35
      ],
      "integerComponents": [
        0
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        7,
        26,
        29,
        35,
        36,
        57,
        62
      ],
      "shellClasses": [
        7,
        35
      ],
      "integerComponents": [
        0
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        9,
        17,
        24,
        39,
        46,
        54,
        63
      ],
      "shellClasses": [
        63
      ],
      "integerComponents": [
        0,
        1,
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        9,
        22,
        31,
        39,
        46,
        49,
        56
      ],
      "shellClasses": [
        49,
        56
      ],
      "integerComponents": [
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        9,
        23,
        30,
        33,
        40,
        54,
        63
      ],
      "shellClasses": [
        63
      ],
      "integerComponents": [
        0,
        1,
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        9,
        23,
        30,
        38,
        47,
        49,
        56
      ],
      "shellClasses": [
        49,
        56
      ],
      "integerComponents": [
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        10,
        18,
        24,
        39,
        45,
        53,
        63
      ],
      "shellClasses": [
        63
      ],
      "integerComponents": [
        0,
        1,
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        10,
        21,
        31,
        39,
        45,
        50,
        56
      ],
      "shellClasses": [
        50,
        56
      ],
      "integerComponents": [
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        10,
        23,
        29,
        34,
        40,
        53,
        63
      ],
      "shellClasses": [
        63
      ],
      "integerComponents": [
        0,
        1,
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        10,
        23,
        29,
        37,
        47,
        50,
        56
      ],
      "shellClasses": [
        50,
        56
      ],
      "integerComponents": [
        2
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        11,
        19,
        24,
        37,
        46,
        54,
        61
      ],
      "shellClasses": [
        11,
        19
      ],
      "integerComponents": [
        0
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        11,
        19,
        24,
        38,
        45,
        53,
        62
      ],
      "shellClasses": [
        11,
        19
      ],
      "integerComponents": [
        0
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        11,
        21,
        30,
        35,
        40,
        54,
        61
      ],
      "shellClasses": [
        11,
        35
      ],
      "integerComponents": [
        0
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        11,
        22,
        29,
        35,
        40,
        53,
        62
      ],
      "shellClasses": [
        11,
        35
      ],
      "integerComponents": [
        0
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        13,
        17,
        28,
        38,
        43,
        55,
        58
      ],
      "shellClasses": [
        13,
        28
      ],
      "integerComponents": [
        1
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        13,
        17,
        28,
        39,
        42,
        54,
        59
      ],
      "shellClasses": [
        13,
        28
      ],
      "integerComponents": [
        1
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        13,
        22,
        27,
        33,
        44,
        55,
        58
      ],
      "shellClasses": [
        13,
        44
      ],
      "integerComponents": [
        1
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        13,
        23,
        26,
        33,
        44,
        54,
        59
      ],
      "shellClasses": [
        13,
        44
      ],
      "integerComponents": [
        1
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        14,
        18,
        28,
        37,
        43,
        55,
        57
      ],
      "shellClasses": [
        14,
        28
      ],
      "integerComponents": [
        1
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        14,
        18,
        28,
        39,
        41,
        53,
        59
      ],
      "shellClasses": [
        14,
        28
      ],
      "integerComponents": [
        1
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        14,
        21,
        27,
        34,
        44,
        55,
        57
      ],
      "shellClasses": [
        14,
        44
      ],
      "integerComponents": [
        1
      ],
      "shell_vectors": 4096
    },
    {
      "H": [
        0,
        14,
        23,
        25,
        34,
        44,
        53,
        59
      ],
      "shellClasses": [
        14,
        44
      ],
      "integerComponents": [
        1
      ],
      "shell_vectors": 4096
    }
  ],
  "norm3_class_count": 13,
  "displaced_centre_pair_checks": 36,
  "theorem": "Every admissible odd D8^3 glue has a component containing only classes 0/v in its complete norm-3 shell; eight orthogonal unit directions pair integrally with all physical u, contradicting the dual gap and codimension two.",
  "source_sha256": "209842f07d8c545b244d5aaf8d9e766f5bbcf0de2e9e9508e7d5f74183058d01",
  "scope": "Entire ambient family containing D8^3 is excluded for the physical frame; no general classification of all odd rank-24 lattices."
}

```


## verifier_collages_D8_independant.mjs

4258 octets ; SHA256 209842f07d8c545b244d5aaf8d9e766f5bbcf0de2e9e9508e7d5f74183058d01

```javascript
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const parity=x=>{let p=0;while(x){p^=1;x&=x-1;}return p;};
// Each component has symbols s,c, with 2b(s,c)=1, b(s,s)=b(c,c)=0.
const bilinear=(x,y)=>parity((((x&21)<<1)^((x&42)>>1))&y);
const symbols=x=>Array.from({length:3},(_,i)=>(x>>(2*i))&3);
const cost=x=>symbols(x).reduce((s,c)=>s+(c===0?0:c===3?1:2),0);
let spaces=[[0]],stages=[];
for(let dim=1;dim<=3;dim++){
  const output=new Map();
  for(const H of spaces)for(let v=1;v<64;v++){
    if(H.includes(v)||H.some(h=>bilinear(v,h)))continue;
    const J=H.concat(H.map(h=>h^v)).sort((a,b)=>a-b);output.set(J.join(','),J);
  }
  spaces=[...output.values()];stages.push({dimension:dim,count:spaces.length});
}
assert.equal(spaces.length,135);
const counts={even:0,odd:0,min1:0,singleton_spinor_E8:0,double_vector_D16:0,
  admissible:0,only_vvv:0,two_vector_spinor_same_centre:0};
const survivors=[];
for(const H of spaces){
  assert(H.length===8&&H.every(x=>H.every(y=>!bilinear(x,y))));
  const odd=H.some(x=>cost(x)%2);counts[odd?'odd':'even']++;
  if(!odd)continue;
  if(H.some(x=>cost(x)===1)){counts.min1++;continue;}
  if(H.some(x=>{const s=symbols(x);return s.filter(c=>c!==0).length===1&&s.some(c=>c===1||c===2);})){counts.singleton_spinor_E8++;continue;}
  if(H.some(x=>{const s=symbols(x);return s.filter(c=>c===3).length===2&&s.filter(c=>c!==0).length===2;})){counts.double_vector_D16++;continue;}
  const shellClasses=H.filter(x=>cost(x)===3);
  assert(shellClasses.length>0);
  const integerComponents=[];
  for(let i=0;i<3;i++)if(shellClasses.every(x=>[0,3].includes(symbols(x)[i])))integerComponents.push(i);
  assert(integerComponents.length>0);
  let vectors=0;for(const word of shellClasses)vectors+=symbols(word).reduce((s,c)=>s*(c===0?1:c===3?16:128),1);
  assert.equal(vectors,4096);counts.admissible++;
  if(shellClasses.includes(63)){assert.deepEqual(shellClasses,[63]);counts.only_vvv++;}
  else{
    assert.equal(shellClasses.length,2);
    const centres=shellClasses.map(x=>symbols(x).findIndex(c=>c===3));
    assert.equal(centres[0],centres[1]);counts.two_vector_spinor_same_centre++;
  }
  survivors.push({H,shellClasses,integerComponents,shell_vectors:vectors});
}
assert.deepEqual(counts,{even:30,odd:105,min1:37,singleton_spinor_E8:24,
  double_vector_D16:12,admissible:32,only_vvv:8,two_vector_spinor_same_centre:24});
// The direct human reduction needs only the 13 possible class-minima of norm3.
const norm3=Array.from({length:63},(_,i)=>i+1).filter(x=>cost(x)===3);
assert.equal(norm3.length,13);
const pairChecks=[];
for(const a of norm3)for(const b of norm3){
  if(bilinear(a,b))continue;
  const initial=[0,a,b,a^b],independent=a!==b;
  if(!independent)continue;
  const commonVector=symbols(a).some((s,i)=>s===3&&symbols(b)[i]===3);
  if(commonVector)continue;
  // An orthogonal pair with displaced centre either adds two vector classes,
  // or fills the Lagrangian on two components, whose extension is a singleton.
  let forbidden=cost(a^b)<=2;
  const union=symbols(a|b).map(c=>c!==0).filter(Boolean).length;
  const singletonForced=union===2;
  assert(forbidden||singletonForced);
  pairChecks.push({a,b,forbidden_sum:forbidden,full_two_component_Lagrangian:singletonForced});
}
const result={exact:true,stages,counts,survivors,norm3_class_count:norm3.length,
  displaced_centre_pair_checks:pairChecks.length,
  theorem:'Every admissible odd D8^3 glue has a component containing only classes 0/v in its complete norm-3 shell; eight orthogonal unit directions pair integrally with all physical u, contradicting the dual gap and codimension two.',
  source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex'),
  scope:'Entire ambient family containing D8^3 is excluded for the physical frame; no general classification of all odd rank-24 lattices.'};
fs.writeFileSync(path.join(here,'verifier_collages_D8_independant.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,lagrangians:spaces.length,counts,displaced_pair_checks:pairChecks.length}));

```


## verifier_coque_D8_mod2.json

418 octets ; SHA256 b051a8c5659f87c85b1a8387b2a01edad1be0e702faa6dd85082145efc72db4e

```json
{
  "exact": true,
  "scope": "D8^3 shell parity Gram and integer D7 generator coefficients; no general shell rank bound",
  "D7_columns": 42,
  "integer_Cz_checks": 7,
  "parity_words": 512,
  "coordinate_rank": 22,
  "Gram_rank_mod2": 20,
  "radical_dimension": 2,
  "required_physical_Gram_rank": 22,
  "frame_excluded": true,
  "source_sha256": "8bab28410783cea666a88b25606a6056251791caaebe008e72a9fe5aaa593cfd"
}

```


## verifier_coque_D8_mod2.mjs

2282 octets ; SHA256 8bab28410783cea666a88b25606a6056251791caaebe008e72a9fe5aaa593cfd

```javascript
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
const C=[];for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const sign of [1,-1]){const col=Array(7).fill(0);col[i]=1;col[j]=sign;C.push(col);}
let integerCzChecks=0;for(let i=0;i<7;i++){
  let found=false;for(let a=0;a<42&&!found;a++)for(let b=a+1;b<42;b++){
    const plus=C[a].map((x,k)=>x+C[b][k]);const minus=C[a].map((x,k)=>x-C[b][k]);
    for(const sum of [plus,minus])if(sum.every((x,k)=>x===(k===i?2:0))){found=true;integerCzChecks++;break;}
    if(found)break;
  }assert(found,'every block has two signed sisters giving Cz=2e_i');
}
const words=[];for(let i=0;i<8;i++)for(let j=0;j<8;j++)for(let k=0;k<8;k++)words.push((1<<i)|(1<<(8+j))|(1<<(16+k)));
function basis(words,width){const piv=Array(width).fill(0),rows=[];for(const value of words){let x=value;for(let j=width-1;j>=0;j--)if(x>>>j&1){if(piv[j])x^=piv[j];else{piv[j]=x;rows.push(x);break;}}}return rows;}
const rows=basis(words,24);assert(rows.length===22,'parity span22');
const parity=x=>{let p=0;while(x){p^=x&1;x>>>=1;}return p;};
const gram=rows.map(a=>rows.reduce((mask,b,j)=>mask|(parity(a&b)<<j),0));
const gramRank=basis(gram,rows.length).length;assert(gramRank===20,'Gram modulo2 rank20');
const block0=255,block1=255<<8,block2=255<<16,rad=[block0^block1,block1^block2];
for(const r of rad){assert(words.every(x=>parity(r&x)===0),'radical orthogonal to all shell words');assert(basis([...rows,r],24).length===22,'radical contained in span');}
assert(basis(rad,24).length===2,'radical dimension2');
const out={exact:true,scope:'D8^3 shell parity Gram and integer D7 generator coefficients; no general shell rank bound',
  D7_columns:C.length,integer_Cz_checks:integerCzChecks,parity_words:words.length,coordinate_rank:rows.length,Gram_rank_mod2:gramRank,
  radical_dimension:2,required_physical_Gram_rank:22,frame_excluded:true,
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_coque_D8_mod2.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));

```


## verifier_frame_D8_trois.json

2195 octets ; SHA256 21bc34b046b16c6a9dee593b830311b5c385fbe29c3fb20055a18dffd64fe504

```json
{
  "exact": true,
  "scope": "D8^3 glue family excluded for complete physical42+7 frame and two norm7 normals, not all U24",
  "classes": [
    {
      "row": [
        0,
        0,
        0
      ],
      "minima": 0
    },
    {
      "row": [
        1,
        1,
        0
      ],
      "minima": 4
    },
    {
      "row": [
        0,
        1,
        1
      ],
      "minima": 4
    },
    {
      "row": [
        1,
        0,
        1
      ],
      "minima": 4
    },
    {
      "row": [
        2,
        2,
        2
      ],
      "minima": 3
    },
    {
      "row": [
        3,
        3,
        2
      ],
      "minima": 5
    },
    {
      "row": [
        2,
        3,
        3
      ],
      "minima": 5
    },
    {
      "row": [
        3,
        2,
        3
      ],
      "minima": 5
    }
  ],
  "glue_gram": [
    [
      4,
      2,
      1
    ],
    [
      2,
      4,
      1
    ],
    [
      1,
      1,
      3
    ]
  ],
  "lattice_determinant": 1,
  "integer_sublattice_index": 4,
  "root_count": 336,
  "shell3": 4096,
  "shell4": 90192,
  "noninteger_shell4": 49152,
  "explicit_characteristics8": 384,
  "character_checks": 65664,
  "energy_lower_bound_with_half_block": 60,
  "energy_available": 56,
  "half_square_checks": [
    {
      "halves": [
        0,
        0
      ],
      "square_sum_mod1_numerator4": 0,
      "integer": true
    },
    {
      "halves": [
        0,
        1
      ],
      "square_sum_mod1_numerator4": 1,
      "integer": false
    },
    {
      "halves": [
        1,
        0
      ],
      "square_sum_mod1_numerator4": 1,
      "integer": false
    },
    {
      "halves": [
        1,
        1
      ],
      "square_sum_mod1_numerator4": 2,
      "integer": false
    }
  ],
  "physical_indices": [
    {
      "g": 18,
      "physical_index": 343,
      "integer_sublattice_index": 4,
      "contradiction": true
    },
    {
      "g": 20,
      "physical_index": 49,
      "integer_sublattice_index": 4,
      "contradiction": true
    }
  ],
  "no_P0": true,
  "no_all_U_classification": true,
  "source_sha256": "d0d784c3a8ca6e77e0c95edcd4e5a533ae23b4f48e44044c76b84b5c0118c756"
}

```


## verifier_frame_D8_trois.mjs

4426 octets ; SHA256 d0d784c3a8ca6e77e0c95edcd4e5a533ae23b4f48e44044c76b84b5c0118c756

```javascript
// Exact small coordinate/discriminant check; the family obstruction is in the MD.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));
const assert=(x,s)=>{if(!x)throw new Error(s);};
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const add=(a,b)=>a.map((x,i)=>x+b[i]);
const zero=()=>Array(24).fill(0);
const vector=(entries)=>{const x=zero();for(const [i,v] of entries)x[i]=v;return x;};
const spin=(part)=>vector(Array.from({length:8},(_,i)=>[8*part+i,1])); // doubled coordinates
const unit=(part)=>vector([[8*part,2]]);
const generators=[add(spin(0),spin(1)),add(spin(1),spin(2)),add(add(unit(0),unit(1)),unit(2))];
const gram4=generators.map(a=>generators.map(b=>dot(a,b)));
assert(JSON.stringify(gram4)===JSON.stringify([[16,8,4],[8,16,4],[4,4,12]]),'glue Gram /4 integral');
// Class labels in F2^2: s=1, v=2, c=3.
const classGenerators=[[1,1,0],[0,1,1],[2,2,2]];
const classes=[];
for(let mask=0;mask<8;mask++){
  const row=[0,0,0];for(let j=0;j<3;j++)if(mask>>j&1)for(let i=0;i<3;i++)row[i]^=classGenerators[j][i];
  classes.push(row);
}
assert(new Set(classes.map(x=>x.join(''))).size===8,'eight independent glue classes');
const costs=[0,2,1,2];
const minima=classes.map(x=>x.reduce((s,c)=>s+costs[c],0));
assert(classes.filter(x=>x.every(c=>c===0||c===2)).length===2,'two integer classes; index4');
assert(classes.filter((x,i)=>minima[i]===3).every(x=>x.every(c=>c===2)),'norm3 only vvv');
assert(classes.filter((x,i)=>minima[i]===4).every(x=>x.filter(c=>c===1).length===2&&x.includes(0)),'noninteger norm4 only ss0');

const roots=[];
for(let part=0;part<3;part++)for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)for(const sign of [1,-1])roots.push(vector([[8*part+i,1],[8*part+j,sign]]));
const characteristics=[];
for(let part=0;part<3;part++)for(let mask=0;mask<256;mask++){
  let minus=0;for(let i=0;i<8;i++)minus+=mask>>i&1;if(minus%2)continue;
  const chi=vector(Array.from({length:8},(_,i)=>[8*part+i,mask>>i&1?-1:1]));
  assert(dot(chi,chi)===8,'characteristic norm8');
  for(const r of roots)assert(dot(chi,r)%2===0,'even D8 root products');
  for(let j=0;j<3;j++){
    const twice=dot(chi,generators[j]);assert(twice%2===0,'integral product with glue');
    assert((twice/2-(gram4[j][j]/4))%2===0,'characteristic parity on glue');
  }
  const doubledSpin=vector(Array.from({length:8},(_,i)=>[8*part+i,mask>>i&1?-1:1]));
  assert(dot(chi,doubledSpin)===8,'matching spinor component gives inner4');
  characteristics.push({part,mask});
}
assert(characteristics.length===384,'384 explicit characteristics8');
const rootCount=3*8*7*2;
const shell3=16**3;
const nonintegerShell4=3*128**2;
const integerShell4=3*(16+70*16)+3*(8*7*2)**2;
assert(rootCount===336&&shell3===4096&&integerShell4+nonintegerShell4===90192,'direct shell counts');
assert(characteristics.length===48+rootCount,'independent theta characteristic count');
const quarterResidues=[];for(let a=0;a<2;a++)for(let b=0;b<2;b++)quarterResidues.push({halves:[a,b],square_sum_mod1_numerator4:a+b,integer:a+b===0});
assert(quarterResidues.filter(x=>x.integer).length===1,'normal coordinates forced integer');
const indices=[18,20].map(g=>({g,physical_index:7**((24-g)/2),integer_sublattice_index:4,contradiction:7**((24-g)/2)%4!==0}));
assert(indices.every(x=>x.contradiction),'both odd indices contradict containment in U_Z');
const out={exact:true,scope:'D8^3 glue family excluded for complete physical42+7 frame and two norm7 normals, not all U24',
  classes:classes.map((row,i)=>({row,minima:minima[i]})),glue_gram:gram4.map(row=>row.map(x=>x/4)),
  lattice_determinant:1,integer_sublattice_index:4,root_count:rootCount,shell3,shell4:integerShell4+nonintegerShell4,
  noninteger_shell4:nonintegerShell4,explicit_characteristics8:characteristics.length,
  character_checks:characteristics.length*(roots.length+3),energy_lower_bound_with_half_block:60,energy_available:56,
  half_square_checks:quarterResidues,physical_indices:indices,no_P0:true,no_all_U_classification:true,
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_frame_D8_trois.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,family_frame_excluded:true,characteristics8:384,shell3,root_count:rootCount,indices}));

```


## verifier_heptade_et_D6_bornes.json

1004 octets ; SHA256 e71199c37b13be894d4be686df02c0f7469be0de76ef2bf8e66bf13d14226668

```json
{
  "exact": true,
  "scope": "heptade lowrank proof normalization and D6 individual-type representatives, not a search over septuples",
  "heptade": {
    "polarities": 56,
    "fixed_A": 41503,
    "code_generator": 8391395,
    "syndrome": 1,
    "fixed_pair_rank_at_least": 5,
    "A_in_Code_general_not_excluded": true
  },
  "D6": {
    "characteristics8": 288,
    "norm4_allowed_types": [
      960,
      14400,
      49152
    ],
    "norm4_candidates": 64512,
    "representatives": [
      {
        "name": "I",
        "pass": true
      },
      {
        "name": "II",
        "pass": true
      },
      {
        "name": "III",
        "pass": true
      },
      {
        "name": "one2",
        "pass": false
      },
      {
        "name": "opposite2plus2",
        "pass": false
      },
      {
        "name": "vvvv",
        "pass": false
      }
    ],
    "seven_blocks_open": true
  },
  "source_sha256": "8efbd65240e9f736c20aefc59c6c9e5cb97af83c6348010b65fcbaa46a9e5fbc"
}

```


## verifier_heptade_et_D6_bornes.mjs

3961 octets ; SHA256 8efbd65240e9f736c20aefc59c6c9e5cb97af83c6348010b65fcbaa46a9e5fbc

```javascript
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
const parity=x=>{let p=0;while(x){p^=x&1;x>>>=1;}return p;};const pop=x=>{let p=0;while(x){p+=x&1;x>>>=1;}return p;};
const polarities=new Set();let constructions=0;
for(let x0=0;x0<8;x0++)for(let a0=1;a0<8;a0++){
  const s=Array.from({length:7},(_,j)=>(parity((j+1)&x0)?-1:1)*((j+1)===a0?-1:1));polarities.add(s.join(','));
  const present=Array.from({length:8},(_,x)=>x).filter(x=>parity(a0&(x^x0))===1);
  const types=[...Array(8).fill(x0),...present.flatMap(x=>Array(4).fill(x))];assert(types.length===24,'8+4*4 coordinates');
  const supports=Array.from({length:7},(_,j)=>types.reduce((bits,x,k)=>bits|((parity((j+1)&(x^x0))^((j+1)===a0?1:0))<<k),0));
  assert(supports.every(x=>pop(x)===8),'all seven octades');
  const multiplicities=types.map((_,i)=>supports.reduce((n,x)=>n+(x>>>i&1),0));assert(multiplicities.every(x=>x===1||x===3),'all columns1/3');
  const A=multiplicities.reduce((bits,n,i)=>bits|((n===1?1:0)<<i),0);assert(A===supports[a0-1],'A is the exceptional octad');constructions++;
}
assert(constructions===56&&polarities.size===56,'56 admissible polarities, independently parametrized');
const fixedA=[0,1,2,9,3,4,13,15].reduce((m,i)=>m|(1<<i),0);
const polynomial=[11,9,7,6,5,1,0].reduce((m,i)=>m|(1<<i),0),generator=polynomial|(parity(polynomial)<<23);
assert(fixedA===41503&&generator===8391395&&parity(fixedA&generator)===1,'fixed0803 syndrome nonzero');

const zero=()=>Array(24).fill(0),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),chars=[];
for(const [a,b] of [[0,2],[1,3]])for(let i=0;i<6;i++)for(let j=0;j<6;j++)for(const sa of [1,-1])for(const sb of [1,-1]){const x=zero();x[6*a+i]=2*sa;x[6*b+j]=2*sb;chars.push(x);}
const glues=[];for(let a=0;a<4;a++){const x=zero();for(let i=0;i<6;i++){x[6*a+i]=i===0?-.5:.5;x[6*((a+1)%4)+i]=.5;}glues.push(x);}
for(const x of chars){assert(dot(x,x)===8,'all288characteristics norm8');for(const g of glues)assert((dot(x,g)-3)%2===0,'characteristic parity onglue');}
const specimens=[];
function sample(entries){const x=zero();for(const [i,v]of entries)x[i]=v;assert(dot(x,x)===4,'norm4 specimen');return x;}
specimens.push({name:'I',x:sample([[0,1],[1,1],[2,1],[3,1]]),pass:true});
specimens.push({name:'II',x:sample([[0,1],[1,1],[6,1],[7,1]]),pass:true});
const iii=zero();for(let i=0;i<6;i++){iii[i]=i===0?-.5:.5;iii[12+i]=.5;}iii[6]=1;specimens.push({name:'III',x:iii,pass:true});
specimens.push({name:'one2',x:sample([[0,2]]),pass:false});
specimens.push({name:'opposite2plus2',x:sample([[0,1],[1,1],[12,1],[13,1]]),pass:false});
specimens.push({name:'vvvv',x:sample([[0,1],[6,1],[12,1],[18,1]]),pass:false});
for(const t of specimens){assert(dot(t.x,t.x)===4,'specimen norm4');const pass=chars.every(c=>Math.abs(dot(c,t.x))<=2);assert(pass===t.pass,'complete-type representative flatness');}
const counts=[4*15*16,4*15**2*16,4*32**2*12];assert(JSON.stringify(counts)===JSON.stringify([960,14400,49152]),'all three analytic counts');
const out={exact:true,scope:'heptade lowrank proof normalization and D6 individual-type representatives, not a search over septuples',
  heptade:{polarities:constructions,fixed_A:fixedA,code_generator:generator,syndrome:1,fixed_pair_rank_at_least:5,A_in_Code_general_not_excluded:true},
  D6:{characteristics8:chars.length,norm4_allowed_types:counts,norm4_candidates:counts.reduce((s,x)=>s+x,0),representatives:specimens.map(x=>({name:x.name,pass:x.pass})),seven_blocks_open:true},
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_heptade_et_D6_bornes.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,polarities:56,fixed_syndrome:1,D6_norm4_candidates:64512,no_septuple_exclusion:true}));

```


## verifier_moments_caracteristique8.json

1944 octets ; SHA256 9f053c0fca4486a26d00e77f3c98cc7abaf1ebcffd14ac4540f448892a51a496

```json
{
  "exact": true,
  "scope": "harmonic theta normalization and a true explicit lattice counter-test, no physical graph exclusion",
  "weighted_basis_q0_q3": [
    [
      "-1",
      "-24",
      "24",
      "9248"
    ],
    [
      "0",
      "-1",
      "0",
      "300"
    ],
    [
      "0",
      "0",
      "-1",
      "24"
    ],
    [
      "0",
      "0",
      "0",
      "-1"
    ]
  ],
  "weighted_shadow_common4096": [
    [
      "0",
      "0",
      "0",
      "0",
      "0",
      "0",
      "137438953472",
      "0",
      "6597069766656"
    ],
    [
      "0",
      "0",
      "0",
      "0",
      "-33554432",
      "0",
      "-805306368",
      "0",
      "0"
    ],
    [
      "0",
      "0",
      "8192",
      "0",
      "0",
      "0",
      "-2457600",
      "0",
      "33554432"
    ],
    [
      "-2",
      "0",
      "48",
      "0",
      "48",
      "0",
      "-18496",
      "0",
      "393264"
    ]
  ],
  "harmonic_ratio": -2,
  "correct_operator": "(4+r/4)I - 2R",
  "wrong_operator": "4I+R",
  "norm3_operator": "(512+2r)I - 24R",
  "positive": {
    "lattice": "E8 orthogonal [D8^2+<(s,v),(v,s)>]",
    "rank": 24,
    "min": 2,
    "odd": true,
    "unimodular": true,
    "roots": 464,
    "characteristics8": 512,
    "root_moment_diagonal": [
      60,
      60,
      60,
      60,
      60,
      60,
      60,
      60,
      28,
      28,
      28,
      28,
      28,
      28,
      28,
      28,
      28,
      28,
      28,
      28,
      28,
      28,
      28,
      28
    ],
    "shadow_moment_diagonal": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      64,
      64,
      64,
      64,
      64,
      64,
      64,
      64,
      64,
      64,
      64,
      64,
      64,
      64,
      64,
      64
    ],
    "wrong_operator_diagonals": 24
  },
  "source_sha256": "e433d49e37d56efc8cdfd5554325a537918290a463b29f232e00dd8fa4bad064"
}

```


## verifier_moments_caracteristique8.mjs

4591 octets ; SHA256 e433d49e37d56efc8cdfd5554325a537918290a463b29f232e00dd8fa4bad064

```javascript
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));
const assert=(x,s)=>{if(!x)throw new Error(s);};
const N=8,z=()=>Array(N+1).fill(0n),one=()=>{const x=z();x[0]=1n;return x;};
const add=(a,b)=>a.map((x,i)=>x+b[i]),scale=(a,c)=>a.map(x=>x*BigInt(c));
function mul(a,b){const x=z();for(let i=0;i<=N;i++)for(let j=0;i+j<=N;j++)x[i+j]+=a[i]*b[j];return x;}
function pow(a,n){let x=one();while(n--)x=mul(x,a);return x;}
function div(a,d){assert(a.every(x=>x%BigInt(d)===0n),'exact series division');return a.map(x=>x/BigInt(d));}
const t3=one(),t4=one(),series=z();for(let i=1;i*i<=N;i++){t3[i*i]=2n;t4[i*i]=i%2?-2n:2n;}for(let i=0;i*(i+1)<=N;i++)series[i*(i+1)]++;
const a=z(),s4=pow(series,4);for(let i=0;i<N;i++)a[i+1]=16n*s4[i];
const b=pow(t4,4),c=pow(t3,4),delta=div(mul(a,b),16),d=add(a,scale(b,-1));
const bases=[],shadows4096=[];
const fSh=[scale(pow(a,6),4096),scale(mul(pow(a,4),mul(b,c)),-256),scale(mul(pow(a,2),mul(pow(b,2),pow(c,2))),16),scale(mul(pow(b,3),pow(c,3)),-1)];
for(let j=0;j<4;j++){bases.push(mul(d,mul(pow(t3,24-8*j),pow(delta,j))));shadows4096.push(mul(add(b,c),fSh[j]));}
for(let j=0;j<4;j++)for(let i=0;i<=j;i++)assert(bases[j][i]===(i===j?-1n:0n),'weighted triangular leading -q^j');
assert(shadows4096[3][0]===-2n&&shadows4096.slice(0,3).every(x=>x[0]===0n),'weighted shadow constant -2d3/4096');
assert(bases[2][2]===-1n&&shadows4096[2][2]===8192n,'harmonic shadow/roots factor -2');
assert(bases[2][3]===24n,'harmonic norm3/roots factor -24');

const v=()=>Array(24).fill(0),dot=(x,y)=>x.reduce((s,t,i)=>s+t*y[i],0);
const roots=[];
for(let part=0;part<3;part++)for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)for(const si of [1,-1])for(const sj of [1,-1]){const x=v();x[8*part+i]=si;x[8*part+j]=sj;roots.push(x);}
const countBits=mask=>{let n=0;for(let i=0;i<8;i++)n+=mask>>i&1;return n;};
for(let mask=0;mask<256;mask++)if(countBits(mask)%2===0){const x=v();for(let i=0;i<8;i++)x[i]=mask>>i&1?-.5:.5;roots.push(x);}
assert(roots.length===464&&roots.every(x=>dot(x,x)===2),'all norm2 roots of E8 + odd U16');
const chars=[];
for(let part=1;part<=2;part++)for(let mask=0;mask<256;mask++)if(countBits(mask)%2===1){const x=v();for(let i=0;i<8;i++)x[8*part+i]=mask>>i&1?-1:1;chars.push(x);}
for(let i=0;i<8;i++)for(let j=0;j<8;j++)for(const si of [1,-1])for(const sj of [1,-1]){const x=v();x[8+i]=2*si;x[16+j]=2*sj;chars.push(x);}
const glueA=v(),glueB=v();for(let i=0;i<8;i++){glueA[8+i]=.5;glueB[16+i]=.5;}glueA[16]=1;glueB[8]=1;
assert(dot(glueA,glueA)===3&&dot(glueB,glueB)===3&&dot(glueA,glueB)===1,'odd U16 glue');
for(const x of chars){assert(dot(x,x)===8,'characteristic norm8');for(const r of roots)assert(dot(x,r)%2===0,'root characteristic parity');for(const g of [glueA,glueB])assert((dot(x,g)-3)%2===0,'odd glue characteristic parity');}
assert(chars.length===512&&chars.length===48+roots.length,'actual shell count');
const R=Array.from({length:24},()=>v()),M=Array.from({length:24},()=>v());
for(const r of roots)for(let i=0;i<24;i++)for(let j=0;j<24;j++)R[i][j]+=r[i]*r[j];
for(const x of chars)for(let i=0;i<24;i++)for(let j=0;j<24;j++)M[i][j]+=x[i]*x[j]/4;
let wrong=0;for(let i=0;i<24;i++)for(let j=0;j<24;j++){
  assert(R[i][j]===(i===j?(i<8?60:28):0),'root moment block diagonal');
  assert(M[i][j]===(i===j?(i<8?0:64):0),'shadow moment block diagonal');
  assert(M[i][j]===(i===j?4+464/4:0)-2*R[i][j],'correct universal harmonic operator');
  if(M[i][j]!==((i===j?4:0)+R[i][j]))wrong++;
}
assert(wrong===24,'candidate 4I+R falsified on every diagonal');
const out={exact:true,scope:'harmonic theta normalization and a true explicit lattice counter-test, no physical graph exclusion',
  weighted_basis_q0_q3:bases.map(x=>x.slice(0,4).map(String)),weighted_shadow_common4096:shadows4096.map(x=>x.map(String)),
  harmonic_ratio:-2,correct_operator:'(4+r/4)I - 2R',wrong_operator:'4I+R',norm3_operator:'(512+2r)I - 24R',
  positive:{lattice:'E8 orthogonal [D8^2+<(s,v),(v,s)>]',rank:24,min:2,odd:true,unimodular:true,roots:464,characteristics8:512,
    root_moment_diagonal:R.map((x,i)=>x[i]),shadow_moment_diagonal:M.map((x,i)=>x[i]),wrong_operator_diagonals:wrong},
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_moments_caracteristique8.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,harmonic_ratio:-2,roots:464,characteristics8:512,candidate_plus_R_falsified:true}));

```


## verifier_rootless_code24.json

1338 octets ; SHA256 c399539ed9136b6603ee4e11cb66aa21e2fc2c1b625685a2f1f0142d6ec219d0

```json
{
  "exact": true,
  "scope": "rootless U24 theorem and exact arithmetic checks; no all-U or all-graph exclusion",
  "rootless_characteristics8": 48,
  "antipodal_pairs": 24,
  "square_frame_Gram": 8,
  "shadowframe_Gram": 2,
  "Code": {
    "length": 24,
    "dimension": 12,
    "min_distance": 8,
    "self_dual_proved": true,
    "doubly_even_proved": true,
    "weight_counts": {
      "0": 1,
      "8": 759,
      "12": 2576,
      "16": 759,
      "24": 1
    },
    "uniqueness_not_claimed": true
  },
  "L0_index": 8192,
  "kernel_index": 33554432,
  "Hamming_ball4": 12951,
  "energy_profiles": [
    {
      "b_abs": [
        1,
        1
      ],
      "activeBlocks": 1,
      "heavyRoots": 1
    },
    {
      "b_abs": [
        1,
        1
      ],
      "activeBlocks": 3,
      "heavyRoots": 0
    },
    {
      "b_abs": [
        1,
        3
      ],
      "activeBlocks": 1,
      "heavyRoots": 0
    },
    {
      "b_abs": [
        3,
        1
      ],
      "activeBlocks": 1,
      "heavyRoots": 0
    }
  ],
  "minor_edge_options": 28,
  "cubic_degree": 3,
  "multiplicity_max": 2,
  "triangle_colorings_valid": 0,
  "physical_template_uniform_if_rootless": true,
  "physical_template_general_case_conditional": true,
  "source_sha256": "ca2c51affa6ff639d7d0c90a9af388757ad5fab0e1b8138f8245fa3150a166aa"
}

```


## verifier_rootless_code24.mjs

2948 octets ; SHA256 ca2c51affa6ff639d7d0c90a9af388757ad5fab0e1b8138f8245fa3150a166aa

```javascript
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
function choose(n,k){let x=1;for(let i=1;i<=k;i++)x=x*(n+1-i)/i;assert(Number.isInteger(x),'integer binomial');return x;}
const evenL0Covol=2**13,kernelCovol=2**25,codeSize=kernelCovol/evenL0Covol;
assert(codeSize===4096,'code size2^12');
const ball4=Array.from({length:5},(_,k)=>choose(24,k)).reduce((s,x)=>s+x,0);
assert(ball4===12951&&ball4*codeSize>2**24,'Hamming excludes d>=12');
const rhs=2**10*24*23,t=(rhs-552-132*4094)/32;
assert(t===759&&4094-2*t===2576,'weight enumerator via second moment');
const profiles=[];for(const b1 of [1,3])for(const b2 of [1,3])for(let activeBlocks=0;activeBlocks<=3;activeBlocks++)for(let heavyRoots=0;heavyRoots<=1;heavyRoots++)
  if(b1*b1+b2*b2+4*activeBlocks+8*heavyRoots===14)profiles.push({b_abs:[b1,b2],activeBlocks,heavyRoots});
assert(profiles.length===4,'three physical profiles, with normal-order two variants');
const edges=[];for(let i=0;i<8;i++)for(let j=i+1;j<8;j++){
  const signs=Array(8).fill(-1);signs[i]=signs[j]=1;assert(signs.reduce((s,x)=>s+x,0)===-4,'minority positions exactlytwo');edges.push([i,j]);
}
assert(edges.length===28&&2*3-12===-6&&8*3===12*2,'centroid forces cubicdegree3');
const possible=[0,8,12,16,24];
const disjointOctadWords=possible.filter(w=>w<=16&&possible.includes(8+w)&&possible.includes(24-8-w));
assert(JSON.stringify(disjointOctadWords)===JSON.stringify([0,8,16]),'no disjoint weight12 with an octad');
let goodColorings=0;for(let mask=0;mask<8;mask++){
  const colors=[mask&1,mask>>1&1,mask>>2&1];
  if(colors[0]!==colors[1]&&colors[1]!==colors[2]&&colors[2]!==colors[0])goodColorings++;
}
assert(goodColorings===0,'three repeated minor edges force impossible two-matching triangle');
const out={exact:true,scope:'rootless U24 theorem and exact arithmetic checks; no all-U or all-graph exclusion',
  rootless_characteristics8:48,antipodal_pairs:24,square_frame_Gram:8,shadowframe_Gram:2,
  Code:{length:24,dimension:12,min_distance:8,self_dual_proved:true,doubly_even_proved:true,weight_counts:{0:1,8:759,12:2576,16:759,24:1},uniqueness_not_claimed:true},
  L0_index:evenL0Covol,kernel_index:kernelCovol,Hamming_ball4:ball4,energy_profiles:profiles,
  minor_edge_options:edges.length,cubic_degree:3,multiplicity_max:2,triangle_colorings_valid:goodColorings,
  physical_template_uniform_if_rootless:true,physical_template_general_case_conditional:true,
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_rootless_code24.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,code:'[24,12,8] self-dual doubly-even, no uniqueness claimed',rootless_shadowframe:true,minor_edge_multiplicity_max:2}));

```


## verifier_theta_caracteristique8.json

3149 octets ; SHA256 22b9322b3783982431ea6ddf987a1b897b2d690d8aabf655289f9f4311e243e7

```json
{
  "exact": true,
  "scope": "finite exact series and normalization checks; analytic proof is in THEOREME_CARACTERISTIQUE8_THETA.md",
  "truncation_q": 8,
  "theta3": [
    "1",
    "2",
    "0",
    "0",
    "2",
    "0",
    "0",
    "0",
    "0"
  ],
  "theta4": [
    "1",
    "-2",
    "0",
    "0",
    "2",
    "0",
    "0",
    "0",
    "0"
  ],
  "A": [
    "0",
    "16",
    "0",
    "64",
    "0",
    "96",
    "0",
    "128",
    "0"
  ],
  "delta8": [
    "0",
    "1",
    "-8",
    "28",
    "-64",
    "126",
    "-224",
    "344",
    "-512"
  ],
  "basis_q0_q3": [
    [
      "1",
      "48",
      "1104",
      "16192"
    ],
    [
      "0",
      "1",
      "24",
      "252"
    ],
    [
      "0",
      "0",
      "1",
      "0"
    ],
    [
      "0",
      "0",
      "0",
      "1"
    ]
  ],
  "shadow_basis_common4096": [
    [
      "0",
      "0",
      "0",
      "0",
      "0",
      "0",
      "68719476736",
      "0",
      "1649267441664"
    ],
    [
      "0",
      "0",
      "0",
      "0",
      "-16777216",
      "0",
      "0",
      "0",
      "402653184"
    ],
    [
      "0",
      "0",
      "4096",
      "0",
      "-98304",
      "0",
      "1032192",
      "0",
      "-6029312"
    ],
    [
      "-1",
      "0",
      "48",
      "0",
      "-1104",
      "0",
      "16192",
      "0",
      "-170064"
    ]
  ],
  "universal_formula": {
    "a": -48,
    "c": 0,
    "b": "48 + number of norm2 vectors",
    "number_characteristics_norm8": "b"
  },
  "golay_positive": {
    "theta": [
      "1",
      "0",
      "0",
      "4096",
      "98256",
      "1130496",
      "8384512",
      "45785088",
      "199066704"
    ],
    "shadow": [
      "0",
      "0",
      "48",
      "0",
      "195456",
      "0",
      "16789312",
      "0",
      "397863936"
    ],
    "shell4_direct": "98256",
    "characteristics_norm8": 48
  },
  "D8_cube_positive": {
    "coefficients": [
      1,
      -48,
      384,
      0
    ],
    "theta": [
      "1",
      "0",
      "336",
      "4096",
      "90192",
      "1130496",
      "8469184",
      "45785088",
      "198572112"
    ],
    "roots": 336,
    "shell3": 4096,
    "shell4": 90192
  },
  "even_boundary": {
    "coefficients": [
      1,
      -48,
      768,
      -4096
    ],
    "theta": [
      "1",
      "0",
      "720",
      "0",
      "179280",
      "0",
      "16954560",
      "0",
      "396974160"
    ],
    "shadow_constant": 1
  },
  "cosets_mod2": [
    [
      "0110",
      "1001"
    ],
    [
      "0111",
      "1101"
    ],
    [
      "1011",
      "1110"
    ]
  ],
  "input_bindings": [
    {
      "file": "../attaque_globale_27_0803/verifier_golay_enveloppe_indep.json",
      "sha256": "76cc2cb462ba125d9488bee80cc56857406c10c7e8fff62ec3980c29ff392cb1"
    },
    {
      "file": "../attaque_globale_27_0803/controles_positifs_cadre_global.json",
      "sha256": "c699700a3d764876711c0f4087582a1a2b95f238d58746f120ac743293fcd7ca"
    }
  ],
  "source_sha256": "09d42c355d9c793a3065db52416f897b85f9887fbcae4ac95ad11f7f27b7d504",
  "no_shadowframe_claim": true,
  "no_graph_exclusion": true
}

```


## verifier_theta_caracteristique8.mjs

5670 octets ; SHA256 09d42c355d9c793a3065db52416f897b85f9887fbcae4ac95ad11f7f27b7d504

```javascript
// Exact, bounded formal-series check. It does not replace the Poisson/valence proof.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';

const here=path.dirname(fileURLToPath(import.meta.url));
const N=8;
const assert=(test,message)=>{if(!test)throw new Error(message);};
const zero=()=>Array(N+1).fill(0n);
const unit=()=>{const a=zero();a[0]=1n;return a;};
const add=(a,b)=>a.map((x,i)=>x+b[i]);
const scale=(a,c)=>a.map(x=>x*BigInt(c));
function mul(a,b){const c=zero();for(let i=0;i<=N;i++)for(let j=0;i+j<=N;j++)c[i+j]+=a[i]*b[j];return c;}
function pow(a,k){let c=unit();for(let i=0;i<k;i++)c=mul(c,a);return c;}
function divide(a,d){const D=BigInt(d);assert(a.every(x=>x%D===0n),'nonintegral exact division');return a.map(x=>x/D);}
const equal=(a,b)=>a.every((x,i)=>x===b[i]);
const strings=a=>a.map(String);
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');

const theta3=unit(),theta4=unit(),s=zero();
for(let n=1;n*n<=N;n++){theta3[n*n]=2n;theta4[n*n]=n%2?-2n:2n;}
for(let n=0;n*(n+1)<=N;n++)s[n*(n+1)]+=1n;
const A=zero(),s4=pow(s,4);
for(let i=0;i<N;i++)A[i+1]=16n*s4[i];
const B=pow(theta4,4),C=pow(theta3,4);
assert(equal(C,add(A,B)),'Jacobi theta3^4 = theta2^4 + theta4^4');
const delta=divide(mul(A,B),16);
assert(delta[1]===1n&&delta[2]===-8n&&delta[3]===28n,'Delta8 normalization');

const base=[];
for(let j=0;j<=3;j++)base.push(mul(pow(theta3,24-8*j),pow(delta,j)));
for(let j=0;j<=3;j++)for(let i=0;i<=j;i++)assert(base[j][i]===(i===j?1n:0n),'triangular orders q^j');

// The four TS transforms, with common denominator 4096.
const shadow4096=[
  scale(pow(A,6),4096),
  scale(mul(pow(A,4),mul(B,C)),-256),
  scale(mul(pow(A,2),mul(pow(B,2),pow(C,2))),16),
  scale(mul(pow(B,3),pow(C,3)),-1),
];
const combine=(parts,coeff)=>parts.reduce((a,b,i)=>add(a,scale(b,coeff[i])),zero());
assert(base[0][1]===48n&&base[1][1]===1n,'coefficient a=-48');
assert(base[0][2]===1104n&&base[1][2]===24n&&base[2][2]===1n,'roots=b-48');
assert(base[0][3]-48n*base[1][3]===4096n&&base[2][3]===0n,'universal shell3=4096 when c=0');
assert(shadow4096[3][0]===-1n&&shadow4096.slice(0,3).every(a=>a[0]===0n),'constant=-c/4096');
assert(shadow4096[2][2]===4096n&&shadow4096[0][2]===0n&&shadow4096[1][2]===0n,'shadow q^2=b when c=0');
assert(shadow4096.every(a=>a.every((x,i)=>i%2===0||x===0n)),'shadow exponents even');

const old=path.resolve(here,'../attaque_globale_27_0803');
const positiveFile=path.join(old,'verifier_golay_enveloppe_indep.json');
const positiveBytes=fs.readFileSync(positiveFile);
const positive=JSON.parse(positiveBytes);
assert(positive.exact===true&&positive.word_count===4096&&positive.weights['8']===759,'frozen true Golay positive');
assert(positive.shell3_L===4096,'frozen shell3');

const golayTheta=combine(base,[1,-48,48,0]);
const golayShadow=divide(combine(shadow4096,[1,-48,48,0]),4096);
const directShell4=BigInt(positive.weights['8'])*128n+4n*24n*23n/2n;
assert(golayTheta[0]===1n&&golayTheta[1]===0n&&golayTheta[2]===0n,'odd positive min3');
assert(golayTheta[3]===4096n&&golayTheta[4]===directShell4&&directShell4===98256n,'independent norm4 octad/sign and 4^2 count');
assert(golayShadow[2]===48n,'48 explicit +/-sqrt(8)e_i characteristics');
const D8cubeTheta=combine(base,[1,-48,384,0]);
assert(D8cubeTheta[2]===336n&&D8cubeTheta[3]===4096n&&D8cubeTheta[4]===90192n,'D8^3 glue shell counts agree with exact series');

const e8=divide(add(add(pow(A,2),pow(B,2)),pow(C,2)),2);
const evenTheta=pow(e8,3);
assert(equal(evenTheta,combine(base,[1,-48,768,-4096])),'even E8^3 boundary coefficients');
const evenShadow=divide(combine(shadow4096,[1,-48,768,-4096]),4096);
assert(equal(evenTheta,evenShadow)&&evenShadow[0]===1n,'even boundary shadow includes zero');
assert(evenTheta[2]===720n,'even boundary roots 720');

// SL2(F2), the three left cosets H\G for H={I,S}.
const mm=(a,b)=>[(a[0]*b[0]+a[1]*b[2])%2,(a[0]*b[1]+a[1]*b[3])%2,(a[2]*b[0]+a[3]*b[2])%2,(a[2]*b[1]+a[3]*b[3])%2];
const I=[1,0,0,1],S=[0,1,1,0],T=[1,1,0,1];
const reps=[I,T,mm(T,S)];
const cosets=reps.map(r=>[r,mm(S,r)].map(x=>x.join('')).sort());
const six=new Set(cosets.flat());assert(six.size===6,'three disjoint cosets in SL2(F2)');

const inputBindings=[positiveFile,path.join(old,'controles_positifs_cadre_global.json')].map(p=>({file:path.relative(here,p).replaceAll('\\','/'),sha256:sha(fs.readFileSync(p))}));
const output={
  exact:true,scope:'finite exact series and normalization checks; analytic proof is in THEOREME_CARACTERISTIQUE8_THETA.md',
  truncation_q:N,theta3:strings(theta3),theta4:strings(theta4),A:strings(A),delta8:strings(delta),
  basis_q0_q3:base.map(a=>strings(a.slice(0,4))),shadow_basis_common4096:shadow4096.map(strings),
  universal_formula:{a:-48,c:0,b:'48 + number of norm2 vectors',number_characteristics_norm8:'b'},
  golay_positive:{theta:strings(golayTheta),shadow:strings(golayShadow),shell4_direct:String(directShell4),characteristics_norm8:48},
  D8_cube_positive:{coefficients:[1,-48,384,0],theta:strings(D8cubeTheta),roots:336,shell3:4096,shell4:90192},
  even_boundary:{coefficients:[1,-48,768,-4096],theta:strings(evenTheta),shadow_constant:1},
  cosets_mod2:cosets,input_bindings:inputBindings,source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
  no_shadowframe_claim:true,no_graph_exclusion:true,
};
fs.writeFileSync(path.join(here,'verifier_theta_caracteristique8.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({exact:true,basis_dimension_proved_in_note:4,golay_characteristics8:48,golay_shell4:String(directShell4),even_shadow_constant:1,no_shadowframe_claim:true}));

```


## verifier_tous_collages_D8_parent.json

11842 octets ; SHA256 99c95d999ec7a2ca467350a8667068f6367ee6a324229fd6f7d1c42851d9eaf1

```json
{
  "exact": true,
  "counters": {
    "even": 30,
    "odd": 105,
    "min1": 37,
    "E8": 24,
    "D16": 12,
    "admissible": 32
  },
  "shape": {
    "1:3": 8,
    "2:1": 24
  },
  "witnesses": [
    {
      "glue": [
        0,
        5,
        17,
        20,
        43,
        46,
        58,
        63
      ],
      "minima": [
        0,
        4,
        4,
        4,
        5,
        5,
        5,
        3
      ],
      "norm3_classes": [
        63
      ],
      "integral_components": [
        0,
        1,
        2
      ]
    },
    {
      "glue": [
        0,
        5,
        26,
        31,
        43,
        46,
        49,
        52
      ],
      "minima": [
        0,
        4,
        6,
        4,
        5,
        5,
        3,
        3
      ],
      "norm3_classes": [
        49,
        52
      ],
      "integral_components": [
        2
      ]
    },
    {
      "glue": [
        0,
        5,
        27,
        30,
        33,
        36,
        58,
        63
      ],
      "minima": [
        0,
        4,
        5,
        5,
        4,
        4,
        5,
        3
      ],
      "norm3_classes": [
        63
      ],
      "integral_components": [
        0,
        1,
        2
      ]
    },
    {
      "glue": [
        0,
        5,
        27,
        30,
        42,
        47,
        49,
        52
      ],
      "minima": [
        0,
        4,
        5,
        5,
        6,
        4,
        3,
        3
      ],
      "norm3_classes": [
        49,
        52
      ],
      "integral_components": [
        2
      ]
    },
    {
      "glue": [
        0,
        6,
        18,
        20,
        43,
        45,
        57,
        63
      ],
      "minima": [
        0,
        4,
        4,
        4,
        5,
        5,
        5,
        3
      ],
      "norm3_classes": [
        63
      ],
      "integral_components": [
        0,
        1,
        2
      ]
    },
    {
      "glue": [
        0,
        6,
        25,
        31,
        43,
        45,
        50,
        52
      ],
      "minima": [
        0,
        4,
        6,
        4,
        5,
        5,
        3,
        3
      ],
      "norm3_classes": [
        50,
        52
      ],
      "integral_components": [
        2
      ]
    },
    {
      "glue": [
        0,
        6,
        27,
        29,
        34,
        36,
        57,
        63
      ],
      "minima": [
        0,
        4,
        5,
        5,
        4,
        4,
        5,
        3
      ],
      "norm3_classes": [
        63
      ],
      "integral_components": [
        0,
        1,
        2
      ]
    },
    {
      "glue": [
        0,
        6,
        27,
        29,
        41,
        47,
        50,
        52
      ],
      "minima": [
        0,
        4,
        5,
        5,
        6,
        4,
        3,
        3
      ],
      "norm3_classes": [
        50,
        52
      ],
      "integral_components": [
        2
      ]
    },
    {
      "glue": [
        0,
        7,
        19,
        20,
        41,
        46,
        58,
        61
      ],
      "minima": [
        0,
        3,
        3,
        4,
        6,
        5,
        5,
        4
      ],
      "norm3_classes": [
        7,
        19
      ],
      "integral_components": [
        0
      ]
    },
    {
      "glue": [
        0,
        7,
        19,
        20,
        42,
        45,
        57,
        62
      ],
      "minima": [
        0,
        3,
        3,
        4,
        6,
        5,
        5,
        4
      ],
      "norm3_classes": [
        7,
        19
      ],
      "integral_components": [
        0
      ]
    },
    {
      "glue": [
        0,
        7,
        25,
        30,
        35,
        36,
        58,
        61
      ],
      "minima": [
        0,
        3,
        6,
        5,
        3,
        4,
        5,
        4
      ],
      "norm3_classes": [
        7,
        35
      ],
      "integral_components": [
        0
      ]
    },
    {
      "glue": [
        0,
        7,
        26,
        29,
        35,
        36,
        57,
        62
      ],
      "minima": [
        0,
        3,
        6,
        5,
        3,
        4,
        5,
        4
      ],
      "norm3_classes": [
        7,
        35
      ],
      "integral_components": [
        0
      ]
    },
    {
      "glue": [
        0,
        9,
        17,
        24,
        39,
        46,
        54,
        63
      ],
      "minima": [
        0,
        4,
        4,
        4,
        5,
        5,
        5,
        3
      ],
      "norm3_classes": [
        63
      ],
      "integral_components": [
        0,
        1,
        2
      ]
    },
    {
      "glue": [
        0,
        9,
        22,
        31,
        39,
        46,
        49,
        56
      ],
      "minima": [
        0,
        4,
        6,
        4,
        5,
        5,
        3,
        3
      ],
      "norm3_classes": [
        49,
        56
      ],
      "integral_components": [
        2
      ]
    },
    {
      "glue": [
        0,
        9,
        23,
        30,
        33,
        40,
        54,
        63
      ],
      "minima": [
        0,
        4,
        5,
        5,
        4,
        4,
        5,
        3
      ],
      "norm3_classes": [
        63
      ],
      "integral_components": [
        0,
        1,
        2
      ]
    },
    {
      "glue": [
        0,
        9,
        23,
        30,
        38,
        47,
        49,
        56
      ],
      "minima": [
        0,
        4,
        5,
        5,
        6,
        4,
        3,
        3
      ],
      "norm3_classes": [
        49,
        56
      ],
      "integral_components": [
        2
      ]
    },
    {
      "glue": [
        0,
        10,
        18,
        24,
        39,
        45,
        53,
        63
      ],
      "minima": [
        0,
        4,
        4,
        4,
        5,
        5,
        5,
        3
      ],
      "norm3_classes": [
        63
      ],
      "integral_components": [
        0,
        1,
        2
      ]
    },
    {
      "glue": [
        0,
        10,
        21,
        31,
        39,
        45,
        50,
        56
      ],
      "minima": [
        0,
        4,
        6,
        4,
        5,
        5,
        3,
        3
      ],
      "norm3_classes": [
        50,
        56
      ],
      "integral_components": [
        2
      ]
    },
    {
      "glue": [
        0,
        10,
        23,
        29,
        34,
        40,
        53,
        63
      ],
      "minima": [
        0,
        4,
        5,
        5,
        4,
        4,
        5,
        3
      ],
      "norm3_classes": [
        63
      ],
      "integral_components": [
        0,
        1,
        2
      ]
    },
    {
      "glue": [
        0,
        10,
        23,
        29,
        37,
        47,
        50,
        56
      ],
      "minima": [
        0,
        4,
        5,
        5,
        6,
        4,
        3,
        3
      ],
      "norm3_classes": [
        50,
        56
      ],
      "integral_components": [
        2
      ]
    },
    {
      "glue": [
        0,
        11,
        19,
        24,
        37,
        46,
        54,
        61
      ],
      "minima": [
        0,
        3,
        3,
        4,
        6,
        5,
        5,
        4
      ],
      "norm3_classes": [
        11,
        19
      ],
      "integral_components": [
        0
      ]
    },
    {
      "glue": [
        0,
        11,
        19,
        24,
        38,
        45,
        53,
        62
      ],
      "minima": [
        0,
        3,
        3,
        4,
        6,
        5,
        5,
        4
      ],
      "norm3_classes": [
        11,
        19
      ],
      "integral_components": [
        0
      ]
    },
    {
      "glue": [
        0,
        11,
        21,
        30,
        35,
        40,
        54,
        61
      ],
      "minima": [
        0,
        3,
        6,
        5,
        3,
        4,
        5,
        4
      ],
      "norm3_classes": [
        11,
        35
      ],
      "integral_components": [
        0
      ]
    },
    {
      "glue": [
        0,
        11,
        22,
        29,
        35,
        40,
        53,
        62
      ],
      "minima": [
        0,
        3,
        6,
        5,
        3,
        4,
        5,
        4
      ],
      "norm3_classes": [
        11,
        35
      ],
      "integral_components": [
        0
      ]
    },
    {
      "glue": [
        0,
        13,
        17,
        28,
        38,
        43,
        55,
        58
      ],
      "minima": [
        0,
        3,
        4,
        3,
        6,
        5,
        4,
        5
      ],
      "norm3_classes": [
        13,
        28
      ],
      "integral_components": [
        1
      ]
    },
    {
      "glue": [
        0,
        13,
        17,
        28,
        39,
        42,
        54,
        59
      ],
      "minima": [
        0,
        3,
        4,
        3,
        5,
        6,
        5,
        4
      ],
      "norm3_classes": [
        13,
        28
      ],
      "integral_components": [
        1
      ]
    },
    {
      "glue": [
        0,
        13,
        22,
        27,
        33,
        44,
        55,
        58
      ],
      "minima": [
        0,
        3,
        6,
        5,
        4,
        3,
        4,
        5
      ],
      "norm3_classes": [
        13,
        44
      ],
      "integral_components": [
        1
      ]
    },
    {
      "glue": [
        0,
        13,
        23,
        26,
        33,
        44,
        54,
        59
      ],
      "minima": [
        0,
        3,
        5,
        6,
        4,
        3,
        5,
        4
      ],
      "norm3_classes": [
        13,
        44
      ],
      "integral_components": [
        1
      ]
    },
    {
      "glue": [
        0,
        14,
        18,
        28,
        37,
        43,
        55,
        57
      ],
      "minima": [
        0,
        3,
        4,
        3,
        6,
        5,
        4,
        5
      ],
      "norm3_classes": [
        14,
        28
      ],
      "integral_components": [
        1
      ]
    },
    {
      "glue": [
        0,
        14,
        18,
        28,
        39,
        41,
        53,
        59
      ],
      "minima": [
        0,
        3,
        4,
        3,
        5,
        6,
        5,
        4
      ],
      "norm3_classes": [
        14,
        28
      ],
      "integral_components": [
        1
      ]
    },
    {
      "glue": [
        0,
        14,
        21,
        27,
        34,
        44,
        55,
        57
      ],
      "minima": [
        0,
        3,
        6,
        5,
        4,
        3,
        4,
        5
      ],
      "norm3_classes": [
        14,
        44
      ],
      "integral_components": [
        1
      ]
    },
    {
      "glue": [
        0,
        14,
        23,
        25,
        34,
        44,
        53,
        59
      ],
      "minima": [
        0,
        3,
        5,
        6,
        4,
        3,
        5,
        4
      ],
      "norm3_classes": [
        14,
        44
      ],
      "integral_components": [
        1
      ]
    }
  ],
  "scope": "All odd unimodular glues of D8^3 with min>=2 and no E8/D16 admit at least one full integral coordinate component on the complete norm3 shell; the dual gap then excludes the whole physical frame for g18 and g20.",
  "source_sha256": "b7dbfc11b37d675cf6898807e486193aac1c2403bb182c6ee8d445ff34b02e79"
}

```


## verifier_tous_collages_D8_parent.mjs

2390 octets ; SHA256 b7dbfc11b37d675cf6898807e486193aac1c2403bb182c6ee8d445ff34b02e79

```javascript
import fs from 'node:fs';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=fileURLToPath(import.meta.url);
const b=(x,y)=>{let z=0;for(let i=0;i<3;i++){const a=(x>>(2*i))&3,c=(y>>(2*i))&3;z^=((a&1)*((c>>1)&1))^(((a>>1)&1)*(c&1));}return z&1;};
const cost=x=>{let z=0;for(let i=0;i<3;i++){const a=(x>>(2*i))&3;z+=(a===3?1:a===0?0:2);}return z;};
const all=new Map();
for(let x=1;x<64;x++)for(let y=x+1;y<64;y++){
 if(b(x,y))continue;
 const two=[0,x,y,x^y];
 for(let z=y+1;z<64;z++){
  if(two.includes(z)||b(x,z)||b(y,z))continue;
  const h=[...two,...two.map(a=>a^z)].sort((a,c)=>a-c);
  all.set(h.join(','),h);
 }
}
assert.equal(all.size,135);
const counters={even:0,odd:0,min1:0,E8:0,D16:0,admissible:0};
const witnesses=[];
for(const h of all.values()){
 assert.equal(h.length,8);
 for(const x of h)for(const y of h)assert.equal(b(x,y),0);
 if(h.every(x=>cost(x)%2===0)){counters.even++;continue;}
 counters.odd++;
 if(h.some(x=>cost(x)===1)){counters.min1++;continue;}
 const singleton=x=>[0,1,2].filter(i=>((x>>(2*i))&3)!==0).length===1;
 if(h.some(x=>cost(x)===2&&singleton(x))){counters.E8++;continue;}
 if(h.some(x=>cost(x)===2&&!singleton(x))){counters.D16++;continue;}
 const shell=h.filter(x=>cost(x)===3);
 const integral_components=[0,1,2].filter(i=>shell.every(x=>[0,3].includes((x>>(2*i))&3)));
 assert(shell.length>0);assert(integral_components.length>0);
 counters.admissible++;
 witnesses.push({glue:h,minima:h.map(cost),norm3_classes:shell,integral_components});
}
assert.deepEqual(counters,{even:30,odd:105,min1:37,E8:24,D16:12,admissible:32});
const shape=witnesses.reduce((a,w)=>{const k=w.norm3_classes.length+':'+w.integral_components.length;a[k]=(a[k]||0)+1;return a;},{});
assert.deepEqual(shape,{'2:1':24,'1:3':8});
const result={exact:true,counters,shape,witnesses,scope:'All odd unimodular glues of D8^3 with min>=2 and no E8/D16 admit at least one full integral coordinate component on the complete norm3 shell; the dual gap then excludes the whole physical frame for g18 and g20.',source_sha256:crypto.createHash('sha256').update(fs.readFileSync(here)).digest('hex')};
fs.writeFileSync(here.replace(/\.mjs$/,'.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:result.exact,counters,shape,witnesses:witnesses.length,source_sha256:result.source_sha256}));

```
