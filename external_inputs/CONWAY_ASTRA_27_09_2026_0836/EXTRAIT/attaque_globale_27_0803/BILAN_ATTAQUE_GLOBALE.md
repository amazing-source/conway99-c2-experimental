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
