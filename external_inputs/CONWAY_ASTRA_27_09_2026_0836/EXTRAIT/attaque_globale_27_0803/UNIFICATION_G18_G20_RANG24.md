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
