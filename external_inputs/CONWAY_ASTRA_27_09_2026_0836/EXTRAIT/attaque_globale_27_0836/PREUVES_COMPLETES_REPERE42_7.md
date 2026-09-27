# Preuves complètes — attaque directe du repère 42+7

# Attaque directe du repère physique : avancées communes à g⁻=18 et20

27 septembre2026 — reprise commencée à08h36 UTC. Ce dossier traite les42 racines, les7 blocs et les2 normales dans UNE MÊME enveloppe. Il n’utilise aucun balayage des types d’étoile, ni SAT/CP/PLNE, ni document extérieur à ce fil.

## Résultat et statut exact

**DÉMONTRÉ, avec contre-audit indépendant :**

1. Les42 racines engendrent le réseau physique N sur les ENTIERS, sans avoir à ajouter les7 blocs.
2. Une enveloppe dont la coque complète de norme3 est entière dans un repère orthonormé ne peut porter ce repère. TOUTE enveloppe contenant trois D8 orthogonaux de rang total24 est exclue pour le repère, pour g18 ET g20, sans P=0. Une deuxième preuve utilise le rang20 modulo2 du Gram de sa coque, face au rang22 imposé.
3. La présence de D11 dans l’enveloppe est également exclue : une racine physique spinorielle y créerait D12, déjà exclu. Cela renforce la limite antérieure D≥12.
4. Dans la famille D6⁴, SIX blocs fractionnaires dans une même paire de composantes opposées sont impossibles. La preuve impose simultanément les deux normales : elles auraient quatre unités communes, puis une racine aurait une projection duale de norme6/7, sous le minimum8/7. Cette strate entière est fermée, sans P=0 et pour les deux valeurs de g.
5. Si l’enveloppe est sans racines de norme2, les24 ombres orthogonales sont FORCÉES. Le template des42 mots de signes et7 octades devient uniforme sur cette famille, et son code binaire est autodual doublement pair [24,12,8]. Aucun résultat d’unicité du code n’est supposé.
6. Dans l’enveloppe D4⁶ construite à partir du cycle6, la sélection physique doit utiliser au moins6 des8 classes de norme3. La preuve ferme231 des256 familles de classes en une seule coupe globale ;25 restent nécessaires, sans réalisation annoncée.
7. Pour sept octades dont les colonnes ont poids1 ou3, un rang binaire≤4 force que le support A des8 colonnes de poids1 soit dans leur code. Dans notre paire de normales0803, A n’appartient pas au code : toute cette famille de sept appuis est exclue, quels que soient leurs signes et les42 racines ensuite choisies.

**Les deux valeurs g⁻=18 et20 restent ouvertes globalement.** Les réseaux rootless, les autres systèmes de racines et les régimes D6⁴ restants ne sont pas fermés. Aucun nombre de types locaux n’est artificiellement ajouté au registre historique. L’involution n’est pas exclue et involution⇒prisme n’est pas démontré ; la poursuite programmée n’est donc pas mise en pause.

## 1. Cadre physique commun et dépendances

On accepte la réduction transmise par C1/structures : g⁻∈{18,20}. Le secteur impair a

    S=[-I7,C ; Cᵀ,T],  S²+S=12I,
    CCᵀ=12I7, CT=0, T²+T=12I42−CᵀC.

Les colonnes de C sont les42 directions e_i±e_j de D7. Le Gram H=3I−S a rang22 et vérifie H²=7H. Le réseau N est engendré par les7 h_c de norme4 et les42 u_o de norme3, avec

    (h_c,h_d)=4δ_cd, (h_c,u_o)=−C_co,
    Gram(u)=3I−T, 3h_c+Σ_o C_co u_o=0,
    Σ_o u_o⊗u_o+Σ_c h_c⊗h_c=7I22.

Les réductions propres de la campagne0803 donnent

    detN=7^(22−g), minN*≥8/7.

La borne duale est un acquis, pas une nouvelle invention. À g18, une sur-lattice intégrale d’indice7 fournit Nmax de déterminant49 ; à g20, Nmax=N. Le collage de Nmax avec J=7I2 donne une enveloppe entière unimodulaire IMPAIRE U de rang24, minimum≥2. Ses deux normales y1,y2 de norme7 sont orthogonales et perpendiculaires à N. Le même repère satisfait

    Σ42 u_o⊗u_o +Σ7 h_c⊗h_c +y1⊗y1+y2⊗y2=7I24.       (F)

Il s’agit de49 générateurs physiques, complétés par2 normales, donc51 vecteurs dans(F). L’indice [U:N⊥J] vaut49 ou343, toujours impair. Cette enveloppe n’est pas un graphe.

Les preuves complètes antérieures sont conservées intactes dans ../attaque_globale_27_0803, notamment UNIFICATION_G18_G20_RANG24.md, AUDIT_NORME1_ET_METRIQUES.md et G18_G20_D12_COLLAGE.md. Le dossier précédent contient aussi l’indécomposabilité de Nmax et l’exclusion de ses systèmes de racines de rang21 ou22.

## 2. Les42 racines engendrent N intégralement

Noter U(z)=Σ_o z_o u_o et h(a)=Σ_c a_c h_c. Les identités physiques donnent

    (3I−T)(T+4I)=CᵀC,
    U((T+4I)z)=−h(Cz).                                  (G)

Pour prouver(G), prendre les produits avec tous les h et tous les u : ils s’annulent grâce à CT=0, Gram(h)=4I et l’identité affichée. Ces vecteurs engendrent le span réel22, donc le vecteur de différence est nul.

Pour un bloc i, choisir les deux colonnes sœurs de support{i,j}. Prendre leurs coefficients dans z avec les signes qui donnent Cz=2e_i : dans les orientations e_i+e_j,e_i−e_j, z=e_++e_−. Si i est le second indice de la convention canonique, le coefficient de la colonne moins est inversé. Alors2h_i∈Γ42:=ΣZu_o. La relation physique donne également3h_i∈Γ42. Plus précisément

    h_i=U((T+4I)z−C_iᵀ).

Ainsi tous les h_i sont dans Γ42, donc **Γ42=N**. Cela utilise les colonnes sœurs de D7 et les49 vecteurs ensemble ; ce n’est pas seulement une génération rationnelle.

Preuves indépendantes : G18_G20_QUARANTE_DEUX_GENERATEURS.md et AUDIT_GENERATION42_ET_COQUE_ENTIERE.md. Le raccord général produit2h et r·h dans le span entier des racines ; il donne la génération totale quand r est impair. À H(2,3), r=1 ; à BvLS r=4, on ne prétend donc pas obtenir le même résultat de génération totale.

## 3. Piège de coque et exclusion de tous les collages D8³

Si un vecteur réel w vérifie w²≤1 et (w,u_o)∈Z pour les42 u sélectionnés, sa projection p sur N appartient à N*, par Γ42=N. Comme p²≤1<8/7, p=0. Dans une enveloppe24, TROIS telles directions indépendantes sont déjà impossibles : elles seraient toutes dans N⊥, de dimension2.

Cette coupe porte sur les42 sélectionnés. Si elle vaut sur toute la coque3 d’une enveloppe, elle exclut TOUT repère physique dans cette enveloppe.

Pour D8={z∈Z8:Σz pair}, poser s=(1/2)^8,v=e1 et

    U=D8³+Z(s,s,0)+Z(0,s,s)+Z(v,v,v).

Les8 classes ont minima0,4,4,4,3,5,5,5. Cette U existe, est impaire unimodulaire, minimum2. Ses4096 vecteurs de norme3 sont exactement les triples (±e_i,±e_j,±e_k), tous entiers. Les24 axes courts ont donc des produits entiers avec toute sélection de42 racines. Le piège ferme la famille.

Seconde preuve : modulo2, les signes disparaissent. Le span W des512 triples e_i+e_j+e_k a dimension22 : les trois sommes de composantes sont égales. Son radical pour le produit standard a dimension2, engendré par 1_B1+1_B2 et1_B2+1_B3. Le Gram de la coque a donc rang20. Or Γ42=N et detN impair imposent rang_F2 Gram(42u)=22. Contradiction.

Une troisième preuve énergétique/index est dans EXCLUSION_FRAME_D8_TROIS.md : les caractéristiques8 interdisent les h demi-entiers, la diagonale rend les normales entières, et l’indice4 de l’enveloppe entière devrait diviser49 ou343.

### Raccord couvrant tous les collages D8³

Pour R=D8³, le discriminant est F2⁶ avec produit symplectique. Le collage H=U/R est un Lagrangien de dimension3. Dans chaque composante, les classes spinorielles s,c ont minimum2 et la classe vectorielle v=s+c minimum1. Les singletons v sont interdits par minU≥2 ; les singletons spinoriels ajoutent E8 ; les doubles vectoriels ajoutent D16. Ces deux dernières familles sont déjà exclues par les preuves du repère.

Une classe de minimum3 existe parce que les42 u physiques ont norme3 et R est pair. Elle est soit(v,v,v), soit(v,s,0) après jauge. Dans le premier cas, aucune classe v-spinor n’est orthogonale à vvv : toute la coque3 est vectorielle dans les trois composantes. Dans le second cas, une classe3 avec centre vectoriel différent est non orthogonale, ou sa somme avec(v,s,0) est un double vectoriel interdit, ou les deux mots forment un Lagrangien complet sur les deux premières composantes. Ce dernier cas oblige le troisième générateur de H, après soustraction, à être un singleton sur la troisième composante : norme1 ou E8, également interdits. Toutes les classes3 ont donc le même centre vectoriel.

Il existe ainsi toujours une composante D8 où la coque3 entière a des coordonnées entières. Ses huit axes sont courts et ont leurs produits avec les42 u dans Z. Le piège dual oblige huit directions indépendantes à être dans N⊥ de dimension2. Contradiction. **Toute la famille D8³ est fermée, et non seulement le collage explicite ci-dessus.**

Trois implémentations indépendantes retrouvent135 collages,30 pairs et105 impairs ;37 normes1,24 E8 et12 D16 sont rejetés. Les32 restantes ont toutes la composante entière :8 cas vvv,24 cas à deux classes v-spinor de même centre. Le raisonnement humain couvre ces32 sans dépendre du balayage. Audit complet : AUDIT_FAMILLE_COMPLETE_D8_TROIS.md ; second contrôle parent : verifier_tous_collages_D8_parent.mjs/.json.

Ce n’est pas une exclusion de toutes les enveloppes avec racines. Les contre-contrôles D4⁶ et D6⁴ montrent au contraire que leur coque3 peut engendrer U entier et avoir Gram modulo2 de rang24.

## 4. D11 exclu dans l’enveloppe

Sur une composante D11, les projections de norme≤3 des u physiques sont0, des unités vectorielles, ou des spinors de norme11/4. Sans spinor, les11 axes courts ont produits entiers avec les42 u, impossible par la coupe précédente.

Choisir donc u=p+b avec p spinor et b²=1/4 dans l’orthogonal. On a4b=4u−4p∈U. L’axe euclidien e12:=2b est de norme1, sans supposer qu’il appartient à U. Comme2p−e_i∈D11,

    2u−(2p−e_i)=e_i+e12∈U,
    (e_i+e12)−4b=e_i−e12∈U.

Ces racines et D11 engendrent D12 dans U, déjà exclu. Ainsi D≥11 est maintenant interdit dans l’enveloppe aussi. Les valeurs D10 et inférieures ne sont pas fermées par ce raccord.

Preuve et audit : G18_G20_DUAL_COORDONNEES.md, AUDIT_D11_ET_LIMITE_COQUE.md.

## 5. D6⁴ : une exclusion utilisant vraiment les deux normales communes

### Enveloppe uniforme
Le collage de D6⁴ se décrit par les huit symboles spinoriels s,c. Leur forme discriminante multipliée par2 est le produit binaire standard. Le code de glue H est autodual [8,4]. Pour un mot de poids w et t composantes doubles, sa norme minimale vaut3w/2−2t. L’enveloppe est impaire, donc H a poids2 ou6 ; par complément, il a poids2. Celui-ci scinde un I2. La moyenne exacte des poids force encore poids2 dans les codes résiduels de longueurs6 et4. Donc H=I2⁴.

Les paires dans une même composante donneraient minimum1. Les deux doubles arêtes entre composantes ajouteraient les racines vectorielles d’un D12, exclu. Il reste uniformément un cycle C4 de glues. Le contrôle des105 couplages trouve45 premières alternatives,12 secondes et48 présentations isométriques du cycle.

Dans le cycle, indexer les composantes A,B,C,D. La coque3 a4096 vecteurs : spinors minimaux dans deux composantes ADJACENTES. Les288 caractéristiques8 sont

    χ=2(±e_i±e_j), i,j dans A,C ou dans B,D.

Tous les42 u physiques sont plats sur chaque χ : |(χ,u)|=1.

L’énergie(F) impose |(χ,h)|≤2 et |(χ,y)|≤3. Les seuls h possibles sont : quatre unités dans une composante ; deux unités dans deux composantes adjacentes ; deux spinors minimaux dans une paire opposée, plus une unité dans une composante intermédiaire. Les comptes individuels960/14400/49152 ne sont pas des repères physiques ; leurs sélections communes restent à contrôler.

### Théorème : six spinors dans une même paire sont impossibles
Supposer que six h soient fractionnaires dans A,C. Leur projection carrée sur A⊕C vaut3 chacune. Chaque u y a carré3/2, et chaque normale y a au moins3/2, parce que sa classe impaire est spinorielle sur une arête du cycle. La trace de(F) sur ces12 dimensions donne

    84=42·(3/2)+6·3+||h7_AC||²+Σ_i ||yi_AC||².

Les trois premiers coûts minimaux valent déjà84. Donc h7_AC=0 et chaque yi_AC est un spinor minimal dans UNE des composantes A,C, sans unité ni excès ailleurs dans cette paire. Le septième h est de type quatre unités dans B ou D ; jauger B.

Dans B,D, une normale doit avoir carré11/2. La borne |(χ,y)|≤3 empêche de combiner une demi-coordonnée3/2 avec une unité dans la composante opposée. Deux demi-coordonnées3/2 dans une composante donneraient un produit3 avec une racine D6 ; la projection duale l’interdit. Donc chaque normale a exactement un spinor minimal dans B ou D, et QUATRE unités dans l’autre composante.

Noter m_B(i),m_D(j) les multiplicités des six centres unitaires des h fractionnaires, et

    t_B(i)=m_B(i)+1_{supp(h7)}(i), t_D(j)=m_D(j).

Pour χ=2(±e_i_B±e_j_D), le nombre k de blocs h actifs vaut t_B(i)+t_D(j). Les deux produits normaux sont impairs. L’énergie exacte devient

    (χ,y1)²+(χ,y2)²=14−4k.

Sous la borne absolue3, les carrés impairs ne peuvent donner que2 ou10 : **k vaut EXACTEMENT1 ou3**.

L’orthogonalité des sept blocs interdit tout centre B sur les quatre positions de h7. Sur ces positions, t_B=1, donc tout t_D vaut0 ou2. Sur les deux positions restantes de B, t_B vaut1 ou3. Le total des six centres laisse deux cas :

- deux centres B simples, et quatre centres D répartis en deux doubles ; t_B vaut1 partout ;
- six centres B répartis en deux triples, aucun centre D ; t_B vaut3 hors h7,1 sur h7.

Une normale ayant quatre unités dans D peut avoir |(χ,y)|=3 pour CHAQUE i_B et chaque j dans ce support, en choisissant les deux signes de χ. Il faut alors k=1. Dans le premier cas, cela force son support D à être exactement les quatre positions sans centre. Une normale ayant ses unités dans B est impossible, car un centre D donnerait k≥3. Les DEUX normales ont donc le même quatre-support D.

Dans le second cas, une normale ayant ses unités dans D serait lourde sur les deux positions B à t_B=3 : impossible. Les deux normales ont leurs unités dans B, exactement sur les quatre positions de h7. Leur quatre-support est encore commun.

Sur ces quatre positions communes, les ratios des signes y2/y1 ont seulement deux valeurs. Deux positions ont donc le même ratio. Une racine α=±e_i±e_j de D6 vérifie alors

    |(α,y1)|=|(α,y2)|=2.

Sa projection sur N a carré

    2−(4+4)/7=6/7.

Elle est non nulle et appartient à N*, contradiction avec minN*≥8/7. **Toute la strate(f_A,f_B)=(6,0), ainsi que sa symétrique(0,6), est fermée.** Cette preuve ne suppose pas P=0 et ne choisit pas des normales différentes selon les blocs.

La seconde preuve et le contrôle exact sont G18_G20_D6_SIX_SPINORS.md/.mjs/.json. Le contrôle des1716 distributions trouve16 possibilités énergétiques, et les élimine toutes avec un témoin de racine commune. La preuve ci-dessus couvre ces possibilités sans s’appuyer sur leur enumeration.

### Coupe collective du régime mixte 4+2

Sous quatre blocs fractionnaires AC, deux BD et un septième bloc entier de type quatre unités dans AC, les quatre centres AC dans B,D doivent être distincts. La trace sur AC vaut63+12+2+4=81 ; les deux normales ont donc leur projection minimale totale3. Les diagonales BD donnent des couvertures entières constantes t_B+t_D=2. Un centre double force t_B=2,t_D=0 (ou l’inverse), puis au moins trois unités communes aux deux normales. La même racine duale de norme6/7 contredit8/7. Toutes les répétitions sont donc exclues dans ce sous-régime.

Le second rejeu indépendant parcourt1365 distributions,870 répétées,150 compatibles avec les diagonales et270 paires de supports unitaires ; aucune ne passe la borne duale. Le corollaire signé impose en plus une répartition EXACTEMENT2+2 des quatre centres distincts dans B,D. En notant σ_i etτ_j les ratios de signes des deux blocs spinoriels BD, l’énergie des deux orientations de χ donne σ_iτ_j=−(−1)^(m_B(i)+m_D(j)). Donc σ_i=ε(−1)^m_B(i) etτ_j=−ε(−1)^m_D(j). Si b centres sont dans B, leur produit spinoriel vautε(2−b) ; les centres AC étant distincts, leur orthogonalité impose b=2. Les profils4+0 et3+1 sont donc exclus aussi. Le régime mixte entier et les autres types du septième bloc restent ouverts. Voir G18_G20_D6_MIXTE_CENTRES_REPETES.md et AUDIT_D6_MIXTE_CENTRES_REPETES.md.

Les répartitions fractionnaires(4,2),(2,4), les répartitions de total inférieur et les autres familles d’enveloppes restent ouvertes. Les premiers calculs P/Q sur les six spinors ont été remplacés par cette preuve plus forte ; ils ne sont pas comptés comme une deuxième fermeture.

## 6. Les enveloppes sans racines ont obligatoirement un code24

Les théorèmes theta autonomes de cette reprise donnent, pour r=#racines2 de U et Z=Σ_{α²=2}α⊗α,

    #χ8=48+r,
    Σχ8 χ⊗χ=(16+r)I24−8Z,
    #coque3=4096,
    Σ_{u²=3}u⊗u=(512+2r)I24−24Z.

La preuve utilise Poisson et des séries de poids12/14, avec un argument de valence détaillé, sans classification des réseaux. Le vrai contre-contrôle E8⊕U16 distingue le signe correct du moment ; la formule naïve4I+Z est fausse et n’est pas utilisée.

Si r=0, il y a24 paires de caractéristiques8 et leur moment vaut16I. Les24 représentantes constituent une matrice CARRÉE K : KKᵀ=8I implique KᵀK=8I. Les24 ombresχ/2 sont donc orthogonales de norme2.

Dans leurs axes, x∈U a coordonnées a/√8, les24 a entiers de même parité. Le sous-réseau pair fournit un code binaire autodual doublement pair [24,12,8]. Son énumérateur des poids est

    1 +759 X8+2576 X12+759 X16+X24.

Il suit des indices, de l’absence de racines, du deuxième moment et de la borne de Hamming ; aucune unicité Golay n’est invoquée. Après jauge d’un u de norme3 en tout-un/√8, la forme complète est

    U={a/√8 : a_i≡m(mod2), {i:a_i≡m+2(mod4)}∈Code,
       Σa_i≡0(mod8)}.

Les42 u sont des signwords E/√8 ; les sept h sont des octades signées2M/√8 ; les deux normales sont B/√8, avec quatre coefficients±3 chacune, disjoints. Le même repère doit satisfaire

    EEᵀ=8(3I−T), MMᵀ=8I7, MEᵀ=−4C, CE=−6M,
    BBᵀ=56I2, EBᵀ=MBᵀ=0,
    EᵀE+4MᵀM+BᵀB=56I24.

Huit colonnes de M ont poids1, seize ont poids3. Cette nécessité est maintenant UNIFORME sur toutes les enveloppes rootless. L’enveloppe positive0803 ne devient pas un graphe ; elle doit encore fournir ce repère complet.

Chaque octade porte également un multigraphe cubique à huit sommets : ses12 racines incidentes ont chacune deux positions minoritaires parmi huit ; le centroïde impose degré3. Une même arête ne peut se répéter trois fois, par le code et T_star=P_μ−P_η. Les sept graphes doivent se coupler aux MÊMES42 mots ; classifier un seul graph ne suffirait pas.

Preuves complètes : THEOREME_CARACTERISTIQUE8_THETA.md, THEOREME_MOMENTS_CARACTERISTIQUES8.md, ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md.

## 7. Deux coupes globales supplémentaires sur les sélections

### D4⁶/cycle6
Le glue a8 classes de norme3 : six classes(v au centre,s aux voisins du cycle), et deux triades v sur les bipartitions. Toute composante D4 doit employer au moins DEUX classes non nulles parmi les42 u sélectionnés : une classe unique fournit, par trialité, quatre axes courts duaux, interdits par la coupe de coque.

Il faut au moins deux classes-centres dans chaque bipartition pour couvrir s partout. Avec quatre classes-centres, les deux triades sont obligatoires ; avec cinq, une triade ; avec six, aucune. Au total, au moins SIX des8 classes doivent figurer. Les25 familles de classes encore nécessaires se répartissent16 de taille6,8 de taille7,1 de taille8 ; les231 autres familles sont exclues. Cette coupe ne ferme pas toute l’enveloppe D4⁶ et ne construit pas de42-sélection dans les25 restantes.

Preuve et certificat de chaque famille rejetée : D4_SIX_CYCLE_SELECTION_COMMUNE.md et controle_D4_cycle6_classes.mjs/.json.

### Sept octades de petit rang
Pour sept appuis de poids8 avec multiplicité de colonne1/3, un rang binaire≤4 force que A, les8 positions de multiplicité1, soit dans leur span. Le quotient par le tout-un a dimension≤3. Trois supports de multiplicité impaire forment un trio disjoint ; sept supports se traitent par les huit caractères de F2³. Les profils couvrants donnent A comme octade ou complément de deux octades disjointes.

Dans l’enveloppe positive0803, A={0,1,2,3,4,9,13,15}, masque41503, n’appartient pas au code : son produit avec le générateur8391395 est impair. Donc toutes les sept sélections d’appuis de rang≤4 sont impossibles dans CETTE paire de normales. Les rangs5/6/7 et les autres paires de normales restent ouverts.

Preuve : SEPT_OCTADES_RANG_BINAIRE_PETIT.md ; contrôle indépendant des128 polarités : controle_sept_octades_rang4.mjs/.json.

## 8. Vérifications, positifs et limites

Les preuves d’impossibilité ci-dessus ont été relues indépendamment ; les ingrédients finis possèdent des sources séparés. Les positifs H(2,3) et BvLS sont reconstruits depuis les données écrites dans ce fil. Le nouveau contrôle vérifie exactement toutes les λ/μ, S²+S=r(r+1)I, H²=(2r+1)H, CCᵀ=2(m−1)I, et la génération entière de2h. Il distingue r=1 etr=4, n’impose ni les normes3 de99 ni son premier7 aux vrais graphes positifs.

Les assertions du rapport Deep Research transmis ne sont pas reprises comme preuves. Aucun graphe SRG99, aucune bijection locale complète (i)–(iii) et aucune sélection physique49 entière n’est produite ici. Les normes9/10 et les registres historiques ne sont pas déclarés fermés par ces nouvelles enveloppes.

Les contrôles sont de petits programmes JavaScript exacts, sans Python local ni solveur. Les sources, sorties et SHA256 sont livrés. Le fichier de reprise conserve les cibles encore ouvertes ; les campagnes0803 et0736 restent intactes.


---

# Dépendances intégrales : campagne immédiatement précédente, 0803

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

# Pièce : AUDIT_D11_ET_LIMITE_COQUE.md

SHA256 : 185fb4ae8216e0cab721a533bf5d8e3ee6db00c81df398b4abbef2ec44f4cfb5

# D11 dans le collage24, et limite de toute borne de coque

## 1. Fermeture D11 dans U24

**Statut : preuve uniforme acquise, conditionnee au repere physique49.** Supposons qu'une composante de racines D11 soit contenue dans U24. La borne minuscule acquise donne, pour chaque u_o de norme3, une projection sur D11 soit nulle, soit +/-e_i, soit un spinor p=(+/-1/2)^11. Elle vient des produits entiers |(u_o,alpha)|<=1 avec toutes les racines, et non d'une classification du collage.

Si aucun des42 u n'a de projection spinor, les onze axes e_i ont des produits entiers avec les42 u. Par Gamma42=N, leurs projections sur span N sont dans N* et ont norme<=1. Le gap8/7 les annule. Les onze axes seraient dans Nperp de dimension2, impossible.

Il existe donc u=p+b, avec p spinor, p^2=11/4 et b^2=1/4, b orthogonal a D11. On a 4p dans D11, donc 4b=4u-4p dans U. Poser e_12=2b ; c'est une DIRECTION de norme1, pas un vecteur suppose appartenir a U.

Pour tout i<=11, le vecteur 2p-e_i a des coordonnees entieres et une somme paire, donc appartient a D11. Par consequent

    e_i+e_12 =2u-(2p-e_i) appartient a U,
    e_i-e_12 =(e_i+e_12)-4b appartient a U.

Ces vecteurs ont norme2. Avec les racines +/-e_i+/-e_j de D11, ils engendrent exactement un reseau de racines D12 dans U. La fermeture D12 dans le collage24, deja prouvee et auditee en0803, exclut ce cas. Ainsi D11 est lui aussi exclu dans U24.

Cette preuve ne suppose ni2b dans U, ni indécomposabilite de U. Le resultat anterieur D11 dans N etait plus etroit ; ici le transport a U passe par de VRAIES racines D12.

## 2. Contre-modele a toute borne universelle Gram(coque3)<=20

Dans R^6, D6 a les classes s=(1/2)^6, c=(-1/2,1/2,...,1/2), v=s+c. Leurs normes minimales sont3/2,3/2,1. Leur forme bilineaire modulo1 donne b(s,s)=b(c,c)=1/2 et b(s,c)=0.

Dans D6^4, ajouter les quatre glues g_i=c_i+s_(i+1 modulo4). Ils sont independants dans le discriminant, ont norme3, et leur Gram est integral. Le glue d'ordre16 fait passer det(D6^4)=256 a det U=1. Le reseau U est impair, integral, de minimum2, et ses racines sont D6^4.

Les minima de ses16 classes sont

    0 une fois ; 3 quatre fois ; 4 cinq fois ; 5 quatre fois ; 6 deux fois.

La coque3 est formee des quatre spinor-pairs,32^2 vecteurs par classe, donc4096 au total. Dans une composante s, changer deux signes dans un vecteur minimal conserve sa classe ; la difference donne e_i+e_j. Ces differences engendrent D6, puisque e_i-e_j=(e_i+e_k)-(e_j+e_k). Chaque composante apparait comme s dans une des quatre familles. Les baselines g_i sont elles aussi dans la coque3. Celle-ci engendre donc U integralement.

Le Gram de toute la coque3 a rang24 modulo2, puisque U est unimodulaire. Un controle direct utilise les24 generateurs simples D6 et les quatre baselines, tous engendres par des normes3, et retrouve le rang24 de leur Gram modulo2. Cela falsifie une borne de rang20 pour toutes les coques3 de collages24. Aucun de ces4096 vecteurs n'est affirme constituer les42 u physiques, ni satisfaire C/T.

## 3. Controle et limites

Le source verifier_D11_et_coque_D6.mjs teste2048 choix de spinor D11, les22 nouvelles racines positives et negatives par choix, les16 classes de glue D6^4, puis le Gram modulo2 des28 generateurs. Il ne produit aucun graphe, ne lance aucun solveur, et ne modifie aucune preuve0803.


---

# Pièce : AUDIT_D6_MIXTE_CENTRES_REPETES.md

SHA256 : 4fd9283e9436c52a42d3fab0664facea4e7ceed788ce3a250a5c69b13cd8b9c1

# D6^4 : coupe conditionnelle des centres repetes dans le regime mixte

**Statut : derivation adverse et petit rejeu independants acquis.** Hypotheses exactes : quatre h spinoriels sur A,C, deux sur B,D, et le septieme h ENTIER dans A,C. Les trois groupes utilisent les memes42 u et les memes deux normales du frame7I24. Aucune fermeture du regime mixte entier n'est annoncee.

## 1. Les diagonales forcent les profils normaux

Sur A+C, les42 u contribuent63 a la trace, les quatre h spinoriels12, les deux centres des h sur B,D contribuent2, et h7 contribue4. Cela donne81. Chaque normale impaire a au moins un spinor dans A ou C, donc au moins3/2 sur cet espace. La trace totale84 force les deux minima3/2 exactement. Chaque normale a un spinor minimal dans une seule des A,C et aucune coordonnee dans l'autre.

Le reste de sa norme sur B+D est11/2. La borne caracteristique max|y_B|+max|y_D|<=3/2 et la borne commune aux deux normales sur toute racine D6 eliminent les spinors lourds. Chaque normale a donc un spinor minimal dans B ou D et quatre unites dans l'autre. Ce sont les profils H1 deja controles dans le cas six spinors ; leur usage ici depend de la trace precedente.

Pour chaque paire d'axes a dans A et c dans C, la base des demi-coordonnees contribue13 a la diagonale paire14. Les deux centres des h sur B,D et les quatre unites de h7 contribuent donc exactement1 par paire. Ils couvrent les six axes d'une seule composante sans repetition. Cela est coherent avec h7 entier de typeI, et ne presume pas que les quatre centres restants soient distincts.

## 2. Une repetition force trois axes unitaires communs

Noter m_B,m_D les multiplicites des quatre centres des h spinoriels A,C. Sur chaque paire b dans B et d dans D, les demi-coordonnees des42 u, des deux h spinoriels B,D et des deux normales contribuent12. La diagonale paire14 impose donc exactement

    m_B(b)+coverage_B(b)+m_D(d)+coverage_D(d)=2.

Ici coverage compte les quatre unites de chacune des deux normales. Les deux sommes separees sont constantes sur leur composante.

Si un centre de B est repete, la premiere constante est au moins2. L'autre vaut donc0. Tous les quatre centres sont dans B, les deux normales ont leurs quatre unites dans B et leur spinor dans D. La constante B vaut2 : une multiplicite3 est impossible. Les seuls motifs repetes sont2+2 et2+1+1.

Dans le motif2+2, les quatre axes B sans centre appartiennent aux deux normales. Dans2+1+1, les trois axes sans centre appartiennent aux deux normales. La symetrie echange B et D. Dans les deux cas, au moins trois axes unitaires sont communs. Deux des ratios de signes sont egaux ; une racine D6 a alors produit absolu2 avec chacune des deux normales. La somme des carres8 contredit la borne commune6, ou equivalemment produit une projection duale non nulle de norme6/7<8/7.

Les quatre centres des blocs spinoriels A,C doivent donc etre distincts, sous les hypotheses annoncees. Cette coupe de repetition seule ne ferme pas les distributions distinctes. Le corollaire du paragraphe4 les restreint encore ; aucun argument ne ferme le regime entier, ni le cas ou h7 est sur B,D, ni d'autres types entiers de h7.

## 3. Verification finie

verifier_D6_mixte_centres_independant.mjs enumere les1365 compositions de quatre centres sur les douze axes B,D. Il regenere les15 supports de quatre unites et verifie les36 equations entieres de diagonale pour les deux normales communes. Il n'utilise aucun masque du producteur.

Il retrouve150 distributions repetees compatibles avec ces diagonales avant la coupe de racine : les15 motifs2+2 et les60 motifs2+1+1 dans chacune des deux composantes. Leurs270 paires de supports normales partagent toutes au moins trois axes. Les autres distributions ne sont pas declarees refutees par ce test. Les signes relatifs sur trois axes sont controles separement.

Le JSON conserve les comptes, deux exemples et le SHA256 du source. C'est une verification de la derniere etape finie, distincte des hypotheses de frame, de caracteristiques et de dual deja demontrees.

## 4. Corollaire : les centres distincts se partagent deux et deux

Pour les deux blocs spinoriels B,D, noter sigma_i et tau_j les rapports de leurs signes sur ces composantes. Fixer deux axes et les deux orientations de la caracteristique : chacun des deux h est actif dans exactement une orientation. Leurs nombres d'activations r(+) et r(-) somment donc2. Avec m=m_B(i)+m_D(j), la condition exacte m+r dans{1,3} force r=1,1 si m est pair et r=0,2 si m est impair. Ainsi

    sigma_i*tau_j = -(-1)^m.

On en deduit sigma_i=epsilon*(-1)^m_B(i), tau_j=-epsilon*(-1)^m_D(j). Si b des quatre centres sont dans B et d=4-b dans D, le produit des parties spinorielles des deux h vaut epsilon*(2-b). Leurs centres A,C sont distincts par les diagonales du paragraphe1 et ont produit0. L'orthogonalite des deux h impose donc b=d=2.

Le source verifie separement les64 cas locaux de signes et les dix cas(b,epsilon). Ce corollaire est une necessite dans le meme sous-regime ; aucune existence ni fermeture de celui-ci n'est annoncee.


---

# Pièce : AUDIT_D6_SIX_FRACTIONNAIRES_MEME_PAIRE.md

SHA256 : efca00c61ec1647e597715f360528ef8de56123e1bac8faa4304f55073d836ca

# D6^4 : six blocs fractionnaires sur une meme paire sont impossibles

**Statut : seconde preuve mathematique et rejeu exact independants.** La famille fermee a f_A=6 et f_B=0 : six des sept h sont des spinor-pairs sur la MEME paire opposee A,C. Le resultat vaut sans P0, pour g18 et g20 dans le modele D6^4/C4. Il ne ferme ni D6^4 entierement, ni les regimes mixtes f_A=2,f_B=4 et f_A=4,f_B=2.

## 1. La trace commune force le septieme bloc et les normales

Les42 u sont des spinor-pairs sur des composantes adjacentes. Chacun projette avec norme3/2 sur A+C, donc leur contribution a la trace du frame sur cet espace12 est63.

Les six h fractionnaires sur A,C contribuent18. Le septieme h est entier : la parite deja acquise impose un nombre pair de h fractionnaires sur chaque paire opposee, donc il ne peut etre le seul fractionnaire B,D. Chaque normale y de norme7 est dans une classe impaire, a un spinor dans l'une des A,C, et y_A+C^2>=3/2.

La trace commune vaut7*12=84. Ses minimums63+18+3 atteignent deja84. Il s'ensuit h7_A+C=0 et, pour chaque normale, y_A+C^2=3/2. Le septieme h, de norme4 et entier horsA,C, est donc quatre unites dans B (ou D, cas symetrique) ; le type deux-plus-deux sur les composantes opposees est interdit par les caracteristiques.

Chaque normale a un spinor minimal sur une des A,C, l'autre A/C nulle. Sa classe est necessairement une seule arete de glue : une classe de trois aretes aurait une classe v entiere non nulle dans l'autre A/C. Elle a donc un spinor dans B ou D et une composante entiere dans l'autre B/D.

## 2. Pourquoi chaque normale a quatre unites et des spinors minimaux

Les288 caracteristiques chi=2(+/-e_B+/-e_D) voient tous les u avec produit+/-1. L'energie56 donne |(chi,y)|<=3 ; d'ou max|y_B|+max|y_D|<=3/2.

La norme residuelle sur B+D est11/2. Si la composante entiere est nonzero, son maximum est>=1. Le maximum du spinor est donc1/2, et celui de la composante entiere1. Il reste exactement quatre unites dans la composante entiere.

Si la composante entiere est nulle, le spinor de norme11/2 aurait deux coordonnees d'absolu3/2, les autres d'absolu1/2. Une racine D6 additionnant ces deux coordonnees a produit absolu3 avec y. Cela viole la borne commune aux deux normales, (alpha,y1)^2+(alpha,y2)^2<=6. Les normales ont donc toutes le profil H1 : deux spinors minimaux adjacents et quatre unites dans l'autre B/D.

## 3. L'energie exacte ne laisse que deux motifs de centres

Le h7 a un support O de quatre coordonnees de B. Les six h fractionnaires ont chacun un centre unitaire dans B ou D. L'orthogonalite avec h7 interdit les centres de B dans O, ne laissant que deux coordonnees de B disponibles.

Noter m_B(x),m_D(y) les nombres de centres et t_B(x)=m_B(x)+1_O(x). Pour chaque caracteristique chi=2(+/-e_Bx+/-e_Dy), la contribution des sept h vaut4k, avec k=t_B(x)+m_D(y). Les deux normales ont des produits+/-1 ou+/-3. L'energie EXACTE est

    56=42+4k+(chi,y1)^2+(chi,y2)^2.

Les seuls cas sont k=1 (carres1+9) ou k=3 (carres1+1). K=0 et k=2 sont impossibles, pas seulement non optimaux.

Sur les quatre positions O, t_B=1. Il s'ensuit que chaque m_D vaut0 ou2. Sur les deux positions horsO, m_B vaut1 ou3. La somme des six centres et l'interdiction de k=5 donnent exactement :

* deux centres simples dans B horsO et deux centres doubles dans D ;
* deux centres triples dans B horsO et aucun centre dans D.

Le petit rejeu explore les1716 compositions possibles de six centres dans les huit positions disponibles. Il retrouve15 placements du premier motif et1 du second, sans utiliser les masques du producteur.

## 4. Dans les deux motifs, les normales ont le meme quatre-support

Une normale H1 demi-entiere dans B et unitaire dans D peut avoir un produit d'absolu3 avec chi sur CHAQUE position de B et sur chacune de ses quatre positions unitaires de D (choisir les deux signes en accord). Ces positions doivent donc avoir k=1, car k=3 impose deux produits d'absolu1.

Dans le premier motif, t_B=1 partout et m_D=2 sur deux positions. Une normale avec spinorD/unitesB est impossible : une position unitaireB et un centreD donneraient k=3 avec produit3. Les deux normales ont donc spinorB et unitesD, avec les quatre unites exactement hors des deux centresD. Leurs quatre-supports sont identiques.

Dans le second motif, les deux positions horsO ont t_B=3. Une normale avec spinorB/unitesD est impossible. Les deux normales ont spinorD/unitesB, les quatre unites exactement dansO. Leurs quatre-supports sont encore identiques.

Sur ces quatre positions, les ratios des signes de y1 et y2 valent+/-1. Deux ratios sont egaux. La racine D6 qui additionne leurs signes a produit absolu2 avec chacune des normales. Sa projection sur N a alors norme

    2-(4+4)/7=6/7,

non nulle et inferieure au gap dual8/7. Contradiction. Aucune orthogonalite de U ou P0 supplementaire n'est utilisee.

## 5. Controle de la coupe matricielle plus faible

Les memes traces et profils rendent exactes les equations P^tQ=0 et PP^t+QQ^t=16I-4XX^t pour les deux matrices6x6 de signes des spinors et les centres unitaires X. Les contributions y_A y_C^t et h7_A h7_C^t sont nulles APRES les profils du paragraphe1, pas par la seule description du glue.

La preuve abstraite qu'aucune matrice6x6 de signes ne peut avoir rang3 et trois valeurs singulieres carrees12 est correcte : son rowspace3 ne contient que huit vertices du cube au plus, donc quatre lignes projectives au plus. Trois lignes imposeraient trois vecteurs orthogonaux de longueur6, impossibles. Quatre lignes donnent un Gram pondere12(I-zz^t) ; les multiplicités positives de somme6 doivent etre2,2,1,1, et les deux lignes de poids1 auraient produit absolu6, donc seraient la meme ligne projective. Cette sous-coupe ferme les centres tous distincts, et le profil3+1+1+1 par repartition spectrale. La preuve des paragraphes1-4 ferme la strate entiere et ne repose pas sur ces equations matricielles.

## 6. Portee

La conclusion s'applique seulement lorsque six h fractionnaires portent la meme paire opposee. Les nombres0,2,4, ainsi que les six fractionnaires repartis2+4 sur les deux paires, restent ouverts dans cet audit. Aucune selection physique42+7 dans D6^4 n'est construite, aucune exclusion globale g18/g20 n'est annoncee.


---

# Pièce : AUDIT_FAMILLE_COMPLETE_D8_TROIS.md

SHA256 : 8aa097f81c730af7f3003d34da18a3d44241f073400a646127c6b0ab077d4189

# Exclusion uniforme des enveloppes contenant D8^3

**Statut : preuve adverse et petit controle exact independants acquis.** Le resultat porte sur une enveloppe integrale unimodulaire impaire U de rang24 portant le repere physique42+7, pas sur tous les reseaux unimodulaires. Les reseaux D8^3 construits existent ; c'est leur repere physique qui est impossible.

## 1. Reduction par les classes de la coque de norme3

Le discriminant de R=D8^3 est F2^6. Dans chaque composante les classes s,c ont norme minimale2, v=s+c a norme minimale1, et le produit2b est symplectique avec b(s,s)=b(c,c)=0 et2b(s,c)=1. Le collage H=U/R est un Lagrangien de dimension3.

Les normes1 sont interdites. Une singleton spinorielle ajoute E8 et deux classes vectorielles ajoutent D16 ; ces deux familles sont deja exclues dans une enveloppe portant le repere physique. Il reste a examiner la coque3. Puisque le repere contient des u de norme3 et R est pair, une classe de minimum3 existe. Les seules classes possibles sont vvv ou un v et un spinor dans deux composantes.

Si vvv appartient a H, aucune classe v-spinor n'est orthogonale a elle : les classes de coque3 se reduisent donc a vvv. Toute composante D8 voit exclusivement v dans la coque3.

Sinon fixer a=(v,s,0), apres permutation et echange s/c. Une autre classe3 avec un centre vectoriel deplace est soit non orthogonale a a, soit donne par addition deux classes vectorielles (D16), soit est de la forme(s ou c,v,0). Ce dernier cas remplit un Lagrangien sur les deux premieres composantes. Tout prolongement de dimension3, apres soustraction des deux premiers generateurs, ajoute une singleton sur la troisieme composante, donc une norme1 ou E8. Ces alternatives sont exclues. Toutes les classes3 ont ainsi le meme centre vectoriel. La coque3 complete voit seulement0/v dans cette composante D8.

## 2. Le piege polaire ferme le repere physique

Les42 u engendrent N integralement, par la relation des soeurs D7 deja prouvee. Une composante D8 dont les projections de la coque3 sont0 ou+/-e_i fournit huit directions orthogonales de norme1 ayant produits entiers avec tous les42 u.

Leurs projections sur N appartiennent a N*. Le gap dual8/7 les force nulles. Elles devraient donc toutes appartenir a N_R perpendiculaire, de dimension2 dans U, contradiction. L'argument n'exige ni caracteristiques8 ni indice de sous-reseau de coordonnees ; il s'applique uniformement aux deux valeurs g18/g20 et sans P0.

## 3. Certificat fini independant

verifier_collages_D8_independant.mjs construit les sous-espaces par extension symplectique et les canonise par leurs listes completes de vecteurs. Il n'utilise ni le RREF de l'agent, ni les fichiers de collage du parent. Les135 Lagrangiens se repartissent en30 pairs et105 impairs. Dans les105 impairs, le filtre ordonne rejette37 normes1,24 singleton spinor/E8 et12 doubles vectoriels/D16. Les32 restants sont8 collages dont la coque3 a seulement vvv et24 dont les deux classes v-spinor ont le meme centre vectoriel. Chacun a4096 vecteurs de norme3 et au moins une composante entierement0/v.

Le meme source controle les13 minima de classes3 et toutes leurs paires orthogonales a centres deplaces. Ce dernier controle ne remplace pas le raisonnement de prolongement Lagrangien ; il en verifie les seules alternatives locales.

Les comptes concordent avec les deux autres voies. Aucun classement de tous les reseaux impairs de rang24, aucune borne universelle de rang du Gram de coque, ni aucune fermeture globale g18/g20 n'est invoque.


---

# Pièce : AUDIT_GENERATION42_ET_COQUE_ENTIERE.md

SHA256 : 0546400d993fcd659a531f5f99065d58b5806a245b067ee2f4b0dac5837e4954

# Generation integrale42 et obstruction de coque entiere

**Statut : preuves uniformes dans le cadre physique49.** La generation par42 est une consequence des identites du repere. Le piege de coque entiere combine cette generation avec la borne duale acquise8/7 ; il n'est pas une nouvelle preuve de cette borne. D8^3 en donne une application complete, et non une classification des collages24.

## 1. Les quarante-deux u engendrent N integralement

Poser U(z)=somme_o z_o u_o et Gamma=<u_o>. Les relations physiques sont

    Gram(u)=3I-T, (h_c,u_o)=-C_co,
    Gram(h)=4I, 3h_c=-U(C_c),
    CT=0, (3I-T)(T+4I)=C^tC.

Pour un vecteur entier z, poser w=U((T+4I)z)+h(Cz). Ses produits avec chaque h sont -C(T+4I)z+4Cz=0. Ses produits avec chaque u sont (3I-T)(T+4I)z-C^tCz=0. Les h et u engendrent le span reel de N, donc w=0.

Choisir deux colonnes soeurs de C avec C_+=e_i+e_j et C_-=e_i-e_j ; prendre z=e_++e_-. Alors Cz=2e_i et

    U((T+4I)z)=-2h_i, U(C_i)=-3h_i.

La difference donne la combinaison ENTIERE

    h_i=U((T+4I)z-C_i).

Cela vaut pour les sept i. Tous les h sont dans Gamma, donc Gamma=N. Aucun determinant local, aucun calcul modulo3, aucun P0 n'est necessaire. Une autre preuve modulo3 est possible, mais la voie entiere suffit.

## 2. Piege de coque entiere

Supposons N plonge dans R^d et que tous ses quarante-deux u aient des coordonnees entieres dans une base orthonormee e_j. La generation42 impose N contenu dans Z^d. Pour chaque j, la projection p_j de e_j sur span(N) satisfait

    (p_j,N) entier, donc p_j appartient a N*,
    p_j^2 <=1.

La borne physique acquise min N*>=8/7 force p_j=0. Les e_j engendrent R^d, donc span(N)=0, contradiction au rang22. Ainsi aucun modele de collage dont toute la coque3 est entiere dans un repere orthonorme ne peut porter le repere49.

Dans D8^3/glue de EXCLUSION_FRAME_D8_TROIS.md, tous les4096 vecteurs de norme3 sont des triples d'unites entieres. La famille est donc exclue egalement par cette voie, sans caracteristique8 ni normales7.

## 3. Deuxieme piege, par Gram modulo2

N a determinant7^(22-g), impair. Son Gram modulo2 est donc non degenere de rang22. Puisque les42 u engendrent N, leur Gram modulo2 doit avoir rang22.

Dans la coque3 du modele D8^3, les signes disparaissent modulo2. Les512 vecteurs sont e_i+e_j+e_k, un indice dans chaque bloc8. Leur span W dans F2^24 est

    W={x : les trois sommes de blocs sont egales}, dim W=22.

Le complement orthogonal standard est engendre par 1_B1+1_B2 et 1_B2+1_B3. Ces deux vecteurs sont dans W car8 est pair. Le radical W inter Wperp a donc dimension2, et le Gram de toute la coque3 a rang20. Toute selection de42 aurait rang<=20, impossible.

Ce calcul porte sur le Gram, pas sur le rang reel de la coque, qui est24. Il ne s'etend pas a toute coque3 unimodulaire24 : aucun tel theoreme general n'est affirme.

## 4. Positifs et provenance

La borne duale8/7 est anterieure : voir les propres notes0803 et leur provenance dans dossier6_involution/NOTE_RESEAU_MINIMUM.md. Elle n'est pas revendiquee comme nouvelle.

H(2,3) et BvLS ont leurs r/d et normes propres. La combinaison de generation generale utilise gcd(2,r)=1 ; la specialisation99 a r=3. On ne transporte pas Gamma42=N a BvLS r=4, ni la borne duale8/7 a son cadre p3.

Le petit source verifier_coque_D8_mod2.mjs verifie la reduction D7 Cz=2e_i, les512 mots de parite, dim W22 et rang Gram20. Il ne reconstruit aucun graphe SRG ni matrice T candidate.


---

# Pièce : AUDIT_HEPTADE_RANG4_ET_D6_BLOCS.md

SHA256 : bef6f38cee740d630da3b6a8e4716b1e851250a2e195f0d0e0a5ccfc58e9dce2

# Audit de deux contraintes collectives, sans fermeture generale

## 1. Sept octades de rang binaire<=4

La preuve de SEPT_OCTADES_RANG_BINAIRE_PETIT.md est correcte. Voici les points qui rendent sa couverture exhaustive.

Pour sept supports de poids8, colonnes de multiplicite1 ou3, leur somme binaire est le tout-un e. Dans V/<e>, dimension<=3, deux octades distinctes restent distinctes : une difference egale a e donnerait un poids16 a l'une d'elles. Les supports de multiplicite impaire sont donc des classes nonzero distinctes, en nombre impair, de somme0. Dans F2^3, un ou cinq sont impossibles ; il reste trois ou sept.

Avec trois, les trois octades impaires partitionnent les24 coordonnees, car leur poids total24 et leur somme tout-un interdisent tout recouvrement. La borne de colonne3 interdit une multiplicite>3. Les seuls profils possibles sont3,3,1 ;3,2,1,1 ;2,2,1,1,1. Dans les derniers profils, les deux supports repetes sont disjoints (sinon une colonne aurait multiplicite>=5). A est une octade ou le complement de deux octades disjointes, donc appartient a V.

Avec sept, chaque coordonnee est l'un des huit types de formes lineaires sur V prenant1 sur e. La transformee de Fourier des sept poids8 donne n_x=3+S_x. Un type present a S=5 ou1, un type absent S=-3. Les deux moments des caracteres donnent exactement une valeur5, quatre valeurs1, trois valeurs-3. Apres translation au type unique5, les polarites sont toutes positives sauf une. L'octade correspondante vaut1 exactement sur les huit coordonnees de multiplicite1 : c'est A.

Ainsi A est dans le span des sept octades. Pour les deux normales FIXES0803, A a masque41503 et son produit avec le generateur8391395 du code propre est impair. A n'est pas dans le code ; tout heptade de rang<=4 est donc exclu pour cette paire fixe. Cela impose rang>=5, pas rang exactement5. A peut appartenir au code pour une autre paire de normales ; aucune de ces paires n'est exclue par le lemme seul.

Le second controle joint construit directement les56 polarites admissibles depuis le type unique et l'indice exceptionnel, plutot que reutiliser la boucle productrice sur128 choix. Il verifie les poids et multiplicites, puis le coupon de syndrome.

## 2. Classification individuelle D6^4

Le modele D6^4/glue cycle4 de la note de combinatoire existe ; son Gram de coque3 est de rang24 modulo2, et aucune borne universelle20 n'est licite. Les16 classes et leurs minima ont ete controles independamment dans verifier_D11_et_coque_D6.mjs.

Ses288 caracteristiques8 sont exactement2(+/-e_i+/-e_j), avec les deux indices dans des composantes opposees. Une composante impaire d'une caracteristique coute6 ; aucun ajout ne peut completer a8, tandis que deux coordonnees paires doubles couvrent les quatre contraintes glues impaires exactement lorsqu'elles sont dans des composantes opposees.

Pour un h physique, la borne |(chi,h)|<=2 est donc equivalente aux deux inegalites max|h_A|+max|h_C|<=1 et max|h_B|+max|h_D|<=1. La classification complete des normes4 qui les passent est correcte :

* quatre unites dans une composante :4*binom(6,4)*16=960 ;
* deux unites dans chacune de deux composantes adjacentes :4*binom(6,2)^2*16=14400 ;
* spinors minimaux sur deux composantes opposees et une unite intermediaire :4*32^2*12=49152.

Une seule coordonnee2, deux-plus-deux dans des composantes opposees, ou quatre unites dans les quatre classes v, violent la borne. Les seules classes nonentieres de norme4 sont les quatre paths de deux glues adjacentes, de cout minimal3/2+1+3/2 ; elles donnent exactement le troisieme type. Les classes de parite impaire ou de minimum>4 n'ajoutent rien. Le total64512 est donc acquis pour des candidats INDIVIDUELS, pas pour sept blocs simultanes.

## 3. Deux contraintes sur les memes normales et les memes sept h

Dans D6^4, chaque u de coque3 et chaque normale de norme7 ont des demi-coordonnees dans deux composantes adjacentes. Les h fractionnaires du troisieme type ont leurs deux composantes spinor opposees. La diagonale du frame, sommee sur une paire de composantes opposees, impose44+2f=0 modulo4, donc le nombre f de tels h sur chaque paire opposee est pair. Cela autorise0,2,4 ou6 h fractionnaires, sans fermer la selection.

Pour toute racine alpha du collage U, sa projection sur span N est dans N*. Elle est nonzero : sinon alpha serait dans le primitif J=<y_1,y_2>=7I2, de minimum7. Le gap dual8/7 donne donc

    (alpha,y_1)^2+(alpha,y_2)^2 <=6.

Les deux produits sont entiers et doivent etre testes avec les MEMES normales. Le raccord utilise la primitivite de J acquise dans le collage, et ne suppose pas que les racines mixtes soient absentes.

## 4. Limites

Le heptade de rang>=5 de la paire fixe reste ouvert. Sept blocs de la classification D6^4 et leurs deux normales communes restent ouverts. Le template octades general reste uniforme seulement si le collage est sans racines, comme prouve dans ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md. Aucune famille restante n'est declaree fermee par ce seul audit.


---

# Pièce : AUDIT_Q42_ET_CLASSIFICATION_D6.md

SHA256 : 561b44d6c66377a816a2d663db4de52eb0d1df0ceffa428291ae68c5ea9aea12

# Audit adverse : congruences Q42 et classification du collage D6^4

**Statut : derivations independantes et controle exact acquis.** Les controles ne cherchent aucune nouvelle selection physique. Ils relisent deux selections deja imprimees et classent les sous-espaces binaires du discriminant D6^4.

## 1. Developpement de Q et mot unique

Avec E=1-2c, B_i=1-2d_i+4k_i, n=sum c, d=d_1+d_2 et K=k_1+k_2, on a hors diagonale

    4Q_jl = -44+2(n_j+d_j+n_l+d_l) (mod4).

Les diagonales sont divisibles par4 parce que les deux B sont impairs. Par consequent Q est entier exactement lorsque n+d=t1 modulo2. Ecrire alors a=(n+d-t1)/2. Le developpement integral, avant reduction modulo2, donne

    Q = (1+t)J + 1(a+K)^t+(a+K)1^t
          +sum c c^t+d_1d_1^t+d_2d_2^t (mod2).

Pour g dans le code autodual doublement pair, tous les termes quadratiques et les termes contenant le poids de g s'annulent. Ainsi Qg=((a+K).g)1. Les24 lignes de Q appartiennent au code exactement lorsque (a+K) modulo2 appartient au code. Il ne s'agit donc pas de24 conditions independantes.

Le rejeu controle les576 entrees de cette expansion et les288 syndromes sur le second temoin fixe. Il retrouve le mot7218972 hors code, alors que le checksum de caracteristique passe. Le premier temoin viole deja l'integralite de Q.

## 2. Caracteristique commune et checksum

Sur un vrai repere physique, sum42u a produit impair avec chaque u, puisque son produit est3 moins une somme de dix signes, et produit pair avec chaque h, par les douze incidences D7. Cette somme est donc caracteristique de N. Les deux normales de norme7 donnent une caracteristique de J. L'indice49 ou343 de N orthogonal J dans U est impair : multiplier tout vecteur de U par cet indice permet de diviser la congruence caracteristique modulo2. La somme chi=sum42u+r_1+r_2 est donc caracteristique de U.

Dans les coordonnees du code normalise, la classe de chi/2 demande le meme mot unique, puis sum du numerateur de chi egal8 modulo16. Pour les deux normales fixes0803, leurs sommes8 et0 reduisent cette derniere condition a un nombre pair de dodecads parmi les42 mots. Cela ne remplace ni les conditions de code, ni le degre dix, ni CT, ni les budgets de voisins communs. Les deux temoins controles ne passent pas ces axiomes physiques.

## 3. Tous les collages impairs D6^4 se reduisent a un couplage

Le discriminant de D6^4 est F2^8, avec les deux symboles spinoriels de chaque composante et le produit bilineaire2b egal au produit standard. Le collage unimodulaire est un sous-espace H autodual de dimension4. Tous ses mots sont pairs et le mot tout-un est dans H.

Un mot de poids w, dont t composantes contiennent leurs deux symboles, a minimum3w/2-2t. La parite de norme vaut w/2 modulo2. L'impair exige un poids2 ou6, et le complement donne un poids2. Ce mot scinde un code de repetition de longueur2. Les codes residuels autoduals de longueur6 puis4 contiennent encore un poids2 : leurs sommes exactes de poids sont24 puis8, tandis que sans poids2 elles seraient au moins28 puis12. Aucune coordonnee ne peut etre constamment nulle, sinon un poids1 serait dans le dual et donc dans le code. On obtient quatre paires disjointes.

Une paire situee dans la meme composante ajoute une classe vectorielle de norme1, interdite. Le graphe des composantes, de degre2 sans boucle, est un cycle4 ou deux doubles aretes. Chaque double arete ajoute la classe(v,v) de norme2 ; toutes les racines croisees sont presentes et avec les deux D6 forment D12, deja exclu dans un collage portant le repere physique. Le cycle4 est unique a permutation et reflexion d'un axe D6 pres.

## 4. Seconde enumeration et portee

Le source independant ne genere aucun couplage parfait. Il construit les sous-espaces orthogonaux contenant le mot tout-un et les deduplique par leurs listes completes de vecteurs. Il trouve135 codes autoduals :30 pairs et105 impairs. Les105 impairs ont chacun exactement quatre mots disjoints de poids2 ;45 ont une boucle,12 donnent deux doubles aretes et48 un cycle4. Cela concorde avec la preuve analytique et avec le controle du parent.

Cette classification rend les coupes physiques C4 uniformes pour les enveloppes de cette famille. La fermeture f_A=6 sur une meme paire opposee est acquise separement. Les regimes0/2/4 et les repartitions mixtes2+4/4+2 restent ouverts. Aucun rang modulo2 universel de la coque3, aucune fermeture g18/g20 globale, ni aucune selection42+7 n'est deduit ici.

Pieces : verifier_Q42_et_collage_D6_independant.mjs et son JSON. Le JSON lie le source et le seul input de selections par SHA256.


---

# Pièce : BILAN_AUDIT_INDEPENDANT_0836.md

SHA256 : d9842032a63c2a6aa77c4c465039a84875c3b602322cdc82a97fe7cd274b4455

# Bilan de l'audit independant 0836

Les preuves et controles de ce dossier concernent le meme repere physique de42 vecteurs u de norme3 et sept vecteurs h de norme4, dans une enveloppe unimodulaire impaire de rang24, avec deux normales de norme7. Le terme racine de reseau designe ici un vecteur de norme2. Aucun registre de types locaux, aucun resultat de foret et aucun fichier ancien n'a ete modifie.

| Resultat acquis | Portee exacte |
| --- | --- |
| Toute enveloppe impaire unimodulaire24 de minimum>=2 a48+r caracteristiques de norme8 | r est le nombre total de racines de norme2 de l'enveloppe ; preuve theta/Poisson et dimension par norme modulaire |
| Moments des caracteristiques8 et de la coque3 | M_chi=(16+r)I-8R et M_coque3=(512+2r)I-24R, R somme des operateurs de TOUTES les racines de l'enveloppe |
| Si l'enveloppe est sans racines, les48 caracteristiques8 donnent24 ombres orthogonales | Le template commun devient necessaire ; code autodual doublement pair[24,12,8], sans unicite de Golay invoquee |
| Les42 u engendrent N integralement | Relation entiere utilisant deux soeurs D7 et les coefficients2 et3 ; aucun transport aux constantes p3 des controles positifs |
| D11 est impossible dans l'enveloppe portant le repere | Un spinor physique fournit de vraies racines D12 ; la direction2b n'est pas supposee dans le reseau |
| Toute enveloppe contenant D8^3 est impossible pour le repere | Classification135 Lagrangiens ; les32 collages restants ont une composante0/v dans toute la coque3, contredisant le petit polaire de dimension2 |
| Tout collage impair D6^4 admissible pour le repere se reduit au cycle4 | Classification135 codes binaires ; les boucles donnent norme1 et les doubles aretes D12 |
| Six blocs spinoriels sur une meme paire opposee D6 sont impossibles | Le cas mixte2+4/4+2 n'est pas ferme par cette preuve |
| Dans le regime4AC+2BD avec h7 entier dans AC, les quatre centres AC sont distincts et se partagent2B+2D | Coupe de repetitions puis orthogonalite ; regime entier non ferme |
| Sept octades de rang binaire<=4 forcent leur octade de multiplicite1 dans leur span | La paire de normales0803 viole cette condition ; aucune exclusion si l'octade est dans le code, ni pour les rangs5..7 |
| Congruences de selection Q42 | Les24 conditions de lignes se reduisent a un mot ; XOR, code et checksum sont controles sur deux temoins fixes non physiques |

## Limites et contre-controles

Le moment candidat M_shadow=4I+R a ete falsifie par le vrai reseau E8 orthogonal U16. La formule correcte est M_shadow=(4+r/4)I-2R. Avec des racines, une coque de caracteristiques8 ne fournit pas automatiquement un repere d'ombres orthogonales.

Les collages D6^4/C4 et D4^6/C6 ont4096 vecteurs de norme3 dont le Gram complet a rang24 modulo2. Ils sont des contre-controles a une borne universelle20 de coque ; ils ne fournissent pas de selection physique42+7. Le minimum du reseau est2, distinct du minimum3 des classes ajoutees.

Le code de rang24 rootless et ses octades sont necessaires sous l'hypothese sans racines. Les congruences Q, checksum, code et budgets ne sont pas presentees comme une contradiction globale. La classification des autres enveloppes et le verrou de la meme selection physique restent ouverts. Aucune cloture g18 ou g20 globale n'est annoncee.

## Verification et provenance

Onze sources Node propres ont ete executes avec sortie exacte. Les series sont tronquees seulement pour les controles de normalisation ; les preuves analytiques de dimension et de Poisson sont dans les notes, et ne sont pas deduites d'une troncature. Les petites enumerations finales ont ete completes :135 codes D6,135 Lagrangiens D8,1716 distributions de six centres,1365 distributions de quatre centres. Aucun solveur, Python local, depot ou Web n'a ete utilise.

Les vrais controles H(2,3) et BvLS du dossier0803 sont conserves et lies en lecture seule. Leurs parametres r=1,d=3 et r=4,d=9, normes u=1 et4, h=2 et5, restent distincts des constantes99. Ils ne sont soumis ni a F7, ni a P0, ni aux regles de purete de norme3.

MANIFEST_AUDIT_INDEPENDANT_0836.json lie les onze notes, onze sources, onze resultats, ce bilan et son constructeur. Chaque resultat porte exact=true et le SHA de son source. Les dependances anciennes et le seul fichier de temoins de selection sont lies separement ; leurs contenus n'ont pas ete modifies.


---

# Pièce : CLASSIFICATION_UNIFORME_D6_QUATRE.md

SHA256 : 8ba147c080fd977db5645784d813cc94f254284c21a71993b3f8746d85c0c3a4

# Classification uniforme de l’enveloppe contenant D6^4

## Théorème
Soit U un réseau entier unimodulaire positif de rang24, minimum au moins2, portant le repère physique42+7 et les deux normales7. Si U contient quatre D6 orthogonaux de rang total24, alors, à permutation et échange des deux classes spinorielles près, son collage est le cycle C4 décrit dans G18_G20_D6_QUATRE.md. L’alternative à deux doubles arêtes contient D12, déjà exclu par la preuve indépendante0803. Aucune classification publiée de réseaux n’est utilisée.

## Preuve par le groupe discriminant
Poser R=D6^4. Son discriminant est F2^8, en prenant pour chaque D6 les deux classes spinorielles s,c de minimum3/2. Leurs produits discriminants multipliés par2 sont diag(1,1) ; s+c est la classe vectorielle v de minimum1. Puisque detR=4^4, le collage H=U/R a cardinal16 et est un code binaire autodual de dimension4. Il est orthogonal à lui-même pour le produit standard, donc tous ses mots ont poids pair. Le mot tout-un appartient à H, puisqu’il est orthogonal à tous ces mots pairs.

Pour un mot de poids binaire w, avec t composantes ayant les deux bits s,c, le minimum de sa classe vaut

    (3/2)(w-2t)+t =3w/2-2t.

La parité de norme vaut donc w/2 modulo2. Si tous les poids de H étaient divisibles par4, U serait pair. Or les42 vecteurs physiques ont norme3. H contient donc un mot de poids2 ou6 ; son complément donne un mot de poids2.

Un mot de poids2 force les deux coordonnées correspondantes à être égales sur tous les mots de H. Ce bloc I2 se scinde dans le code. Le code résiduel autodual de longueur6 possède lui aussi un mot de poids2 : sans cela ses sept mots non nuls auraient poids au moins4, pour une somme au moins28, tandis que la somme exacte des poids est8·6/2=24. Chaque coordonnée prend bien les deux valeurs, sinon un mot de poids1 serait dans le dual et dans le code. Le même argument à longueur4 donne12>8. À longueur2, le dernier code est I2.

Ainsi H est constitué de quatre paires disjointes des huit symboles spinoriels. Une paire située dans le même D6 ajouterait v, de minimum1, impossible. Le multigraphe sur les quatre composantes D6 a donc degré2, sans boucle. Il est soit un cycle C4, soit deux cycles à deux arêtes parallèles.

Dans une double arête entre deux D6, la somme des glues ajoute (v,v), de minimum2. Toutes ses racines ±e_i±e_j reliant les deux composantes sont présentes ; avec leurs D6 elles engendrent D12. Cette possibilité est exclue par G18_G20_D12_COLLAGE.md de la campagne0803.

Le cycle C4 est donc la seule enveloppe possible dans cette famille. Les échanges s↔c sont des changements de signe d’un axe dans D6 ; toutes les orientations du cycle sont isométriques.

## Contrôle fini indépendant de la preuve du code
Le source classer_collage_D6_quatre.mjs parcourt seulement les105 couplages parfaits de huit symboles. Il trouve45 couplages comportant une boucle (minimum1),12 avec deux doubles arêtes (D12),48 réalisations du même cycle C4. Il vérifie également les deux inégalités de somme des poids. Ce contrôle n’énumère aucun type local ni graphe SRG.

## Portée
Cette classification rend les coupes physiques dans le cycle C4 uniformes pour toute cette famille d’enveloppes. Elle ne ferme pas D6^4 à elle seule. L’exclusion collective de six blocs fractionnaires dans une paire opposée est une preuve distincte ; les répartitions0/2/4 et les répartitions mixtes restent ouvertes. Les autres systèmes de racines de U ne sont pas couverts ici.


---

# Pièce : COUPES_ENTIERES_SELECTION42.md

SHA256 : 91c41918d3c999e5771156e5b07763bfc6c9458a77378ba28c40cbf6ea78fe96

# Congruences communes à une même sélection des 42 racines et sept blocs

**Statut : dérivation indépendante relue par g18_audit_neuf et contrôle exact propre acquis.** Les congruences sont des conséquences du repère commun ; aucun nouveau filtre autonome de graphe ni aucune fermeture globale n'est revendiqué.

**Portée.** On utilise un repère d'ombres orthogonales de rang 24 et le code binaire auto-dual doublement pair C qu'il fournit. Ce repère est explicite dans l'enveloppe du dossier 0803. Le théorème indépendant de l'auditeur le rend également obligatoire pour une enveloppe unimodulaire impaire de rang 24 sans racines ; aucune hypothèse analogue n'est imposée à une enveloppe avec racines.

Les calculs ci-dessous ne supposent pas l'unicité de C. Les témoins imprimés utilisent exclusivement notre code explicite, la paire de normales 0803 et sa coque de 704 racines. Ils ne satisfont pas tous les axiomes physiques et ne sont pas présentés comme des graphes.

## 1. Le système entier commun

Dans les coordonnées normalisées, écrire u_o=E_o/√8, h_c=2M_c/√8 et r_i=B_i/√8. Les 42 lignes E sont des mots de signes ±1. Les sept lignes M sont 0,±1, d'appuis des octades de C. Les deux lignes B sont impaires. Le même repère impose

    EᵀE + 4MᵀM + BᵀB = 56I24,
    MMᵀ=8I7, MEᵀ=−4C_physique,
    Q := (56I24−EᵀE−BᵀB)/4 = MᵀM.                       (1)

L'apparition du code C et celle de C_physique, matrice des directions D7, sont deux objets distincts.

En particulier, Q est entier, ses lignes modulo deux sont dans C, et Q est positif de rang sept avec Q²=8Q. Les deux premières conditions peuvent se vérifier avant de chercher M.

## 2. Une congruence XOR sur les 42 mots

Écrire E_o=1−2c_o, où c_o∈C. Pour les normales, écrire

    B_i=1−2d_i+4k_i,

où d_i∈C, k_i est entier. Noter n=Σ_o c_o (somme entière), δ=d_1+d_2 et K=k_1+k_2.

Les entrées hors diagonale de 4Q modulo quatre sont 2(n_j+δ_j+n_k+δ_k). Les diagonales sont divisibles par quatre car chaque B_ij est impair. Donc

    Q entier  ⇔  n+δ ≡ τ1 (mod2), pour τ=0 ou1,
             ⇔  XOR_o c_o = d_1 XOR d_2, ou son complément. (2)

C'est une contrainte sur les 42 mots choisis ensemble. Elle ne se déduit pas de la norme trois, de l'orthogonalité aux deux normales ni des seuls produits 0,±1 de chaque paire.

## 3. Les 24 tests de lignes de Q se réduisent à un seul mot

Supposer (2), et poser a=(n+δ−τ1)/2, qui est entier. Le développement de (1) modulo deux donne

    Q ≡ (1+τ)J + 1(a+K)ᵀ + (a+K)1ᵀ
          + Σ_o c_o c_oᵀ + d_1 d_1ᵀ + d_2 d_2ᵀ  (mod2).

Pour tout g∈C, les termes quadratiques s'annulent après multiplication par g, car C est auto-dual ; le terme J et l'autre terme de rang un s'annulent car g a poids pair. Ainsi

    Qg ≡ ((a+K)·g)1 (mod2).

On obtient la condition exacte

    toutes les lignes Q mod2 appartiennent à C
       ⇔  (a+K) mod2 appartient à C.                       (3)

Si (3) échoue, les vingt-quatre lignes échouent simultanément contre un même générateur dual. On n'a donc besoin que d'un certificat binaire unique. Cette simplification évite de traiter les lignes comme vingt-quatre tests indépendants.

## 4. Raccord à la caractéristique physique et checksum modulo seize

Pour un vrai repère physique, χ_N=Σ_o u_o est caractéristique de N. En effet, son produit avec u_o est 3 moins une somme de dix signes, donc impair ; son produit avec chaque h_c est une somme paire des colonnes D7, donc pair. Ces parités coïncident avec les carrés des générateurs. Les deux normales de carré sept donnent une caractéristique r_1+r_2 du réseau J qu'elles engendrent.

L'indice de N⊕J dans l'enveloppe est impair, 49 ou343. Il s'ensuit que

    χ = Σ_o u_o + r_1+r_2

est caractéristique de l'enveloppe entière. L'argument ne suppose pas que N soit primitif en g18 : si un multiple impair d'un vecteur de l'enveloppe appartient à N⊕J, la congruence caractéristique se divise modulo deux.

Dans l'enveloppe explicite, une caractéristique canonique est √8 e_j ; toutes les caractéristiques s'en déduisent en ajoutant 2U. Si x=(Σ_o E_o+B_1+B_2)/2 est le numérateur de χ/2, son appartenance à la classe d'ombres demande

    x_j tous de même parité,
    support de (x−parité(x)1)/2 modulo2 dans C,
    Σ_j x_j ≡4 (mod8).                                   (4)

Les deux premières conditions sont exactement (2) et (3), à l'addition éventuelle du mot 1 près. La dernière apporte le checksum commun

    Σ_j (Σ_o E_oj+B_1j+B_2j) ≡8 (mod16).                  (5)

Pour les normales fixes 0803, ΣB_1=8 et ΣB_2=0. Les mots de C ont poids0,8,12,16,24. La congruence (5) impose donc un **nombre pair de mots de poids 12** parmi les 42 c_o. Ce filtre ne remplace pas le degré dix ou les identités physiques ; il découle de leur caractéristique commune.

## 5. Contrôles bornés et limites des témoins

[controle_selection42_golay.mjs](controle_selection42_golay.mjs) régénère les 4096 mots propres, les deux normales et leurs 704 racines orthogonales. Ses deux sélections déterministes de 42 lignes contiennent une même base de 22 lignes indépendante modulo101 ; leur rang réel est donc exactement22, et tous leurs produits par paire sont0,±1.

La première viole (2). La deuxième satisfait (2) mais viole (3) sur les vingt-quatre lignes ; le mot unique de (3) est 7218972, hors C. Elle contient dix-huit dodecads et satisfait donc (5). Elle démontre que le checksum de caractéristique ne remplace pas la congruence de code. Les deux témoins ne satisfont pas le degré dix, CT, les budgets λ/μ ou le repère complet ; aucune assertion inverse n'est formulée.

[controle_congruences_selection42.mjs](controle_congruences_selection42.mjs) contrôle séparément le développement de (3) sur les douze générateurs binaires, les vingt-quatre lignes Q, et le checksum (5). Le résultat est [controle_congruences_selection42.json](controle_congruences_selection42.json).

Le même premier source contient un bloc h réel de carré quatre, orthogonal aux deux normales, de numérateur4e_2−4e_9. Il appartient à l'enveloppe et est pourtant impossible dans le repère physique : une colonne de M vaudrait2, et son énergie diagonale serait26 au lieu de14. Cela justifie de filtrer les h par le repère commun, et non par leur seule existence dans le réseau.

Les congruences (2)–(5), le lemme des sept appuis de rang binaire petit et les tests de capacité sont complémentaires. Aucun résultat de cette note ne ferme g18 ou g20 globalement.


---

# Pièce : D4_SIX_CYCLE_SELECTION_COMMUNE.md

SHA256 : 39839ca0035e0e8d2d4bdbf8b90faf1904ab1a0b72a0b7f621b2bfd0efbf9279

# D4⁶ avec collage du cycle six : au moins six classes doivent être choisies

**Statut : démontré par preuve couvrante, après contre-audit humain indépendant ; contrôle exact de 64 classes puis 256 familles.** Ce résultat porte sur les classes des mêmes 42 vecteurs physiques. Il ne ferme pas tout le collage D4⁶, ni g18 ou g20.

## 1. Une enveloppe intégrale explicite

Dans chaque composante D4, noter v=e_1 et s=(1/2)^4 modulo D4. Les trois classes non nulles v,s,c=v+s ont minimum 1. Soit A la matrice d'adjacence du cycle C6 sur les indices0,...,5. Au réseau D4⁶, adjoindre six classes a_i : v dans la composante i, s dans ses deux voisines, et zéro ailleurs.

Pour un masque binaire a de six sommets, la classe résultante a pour composante v a_j+s( Aa )_j. Les six générateurs sont indépendants, car leurs coefficients v sont les six vecteurs unitaires. Les produits sont entiers : chaque produit v·s=1/2 dû à une arête du cycle apparaît deux fois, et un chevauchement s·s vaut1. Le carré d'un générateur est3. Ainsi le collage est intégral impair, d'indice2⁶ dans D4⁶ ; det(D4⁶)=2¹² donne det U=1.

Le poids d'une classe est le nombre de composantes non nulles. Les accroissements de carré au sein d'une classe sont pairs, et chaque composante non nulle a minimum1. Le contrôle propre des64 masques établit que le poids minimal non nul est3 et que les seules classes de poids3 sont :

* six classes a_i, avec v en i et s aux deux voisines ;
* deux classes t_0,t_1, avec v sur l'une des deux parts {0,2,4} ou {1,3,5} et zéro ailleurs.

Il existe aussi une réduction humaine courte : |a|≥4 donne immédiatement poids≥4 ; |a|=1 donne les six bases ; |a|=2 donne poids4 ou6 selon la distance. Pour |a|=3, les gaps cycliques sont, à ordre près, (1,1,4), (1,2,3) ou (2,2,2). Seul le dernier masque ne crée aucun voisin de parité impaire hors de a, et donne les deux triades alternées.

La coque3 complète comprend donc huit classes, chacune avec8³=512 vecteurs minimaux. Les racines D4 du collage ont carré2 ; on ne confond pas le minimum3 des classes ajoutées avec le minimum2 du réseau entier.

## 2. Le petit polaire contraint chaque composante

Les quarante-deux u du repère physique engendrent N intégralement. Le gap dual de N impose que toute tranche de dimension au moins trois ne puisse porter leurs projections dans 0 et une seule classe minuscule : une trialité D4 rendrait les quatre axes intégraux contre N, et leurs projections duales de carré≤1 seraient nulles. Ils ne pourraient tenir dans N⊥ de dimension deux.

Ici les classes de coque3 utilisent seulement 0,v,s, jamais c. **Dans chacune des six composantes, les mêmes42 u doivent donc employer v et s.** Cette assertion concerne les classes effectivement utilisées, pas la simple disponibilité des huit classes de la coque complète.

Le lemme et la trialité explicite sont donnés dans [OBSTRUCTION_COQUE3_ET_D8_CUBE.md](OBSTRUCTION_COQUE3_ET_D8_CUBE.md).

## 3. Couverture simultanée du cycle : au moins six classes

Noter B l'ensemble des indices des bases a_i effectivement utilisées. Pour obtenir la lettre s en chaque composante, chaque sommet du cycle doit avoir un voisin dans B. Les deux triades n'apportent aucune lettre s.

Le cycle est biparti, avec trois sommets par part. Les voisins de chaque sommet sont deux des trois sommets de la part opposée. Une seule base dans une part manque l'un des trois sommets opposés. Il faut donc au moins deux bases dans chaque part, soit |B|≥4.

Pour couvrir v, une composante absente de B ne peut recevoir v que de la triade de sa part. On obtient exactement les familles suivantes.

| Nombre de bases utilisées | Condition sur les triades | Nombre de familles qualifiantes |
|---|---|---:|
| 4 : deux bases dans chaque part | Les deux triades sont obligatoires pour les deux sommets absents. | 9 |
| 5 | La triade de la part du sommet absent est obligatoire ; l'autre est facultative. | 6·2=12 |
| 6 | Les deux triades sont facultatives. | 4 |

Parmi les2⁸=256 familles de classes, exactement25 passent cette condition nécessaire. Le nombre de classes utilisées est au moins6 ; la distribution des familles survivantes est16 de taille6,8 de taille7 et1 de taille8.

Les231 autres familles sont impossibles pour le repère physique entier, même avant de choisir les signes ou de vérifier les produits T. Un certificat d'une famille rejetée est une composante où v ou s manque : la trialité et le petit polaire donnent la contradiction. Les25 familles restantes ne sont pas déclarées réalisables.

## 4. Certificat et limites

[controle_D4_cycle6_classes.mjs](controle_D4_cycle6_classes.mjs) construit le collage depuis C6, recalcule ses64 classes, vérifie les produits des six générateurs et les huit classes exactes de coque3, puis traite les256 sous-ensembles directement par composante. Il compare à la formule9+12+4 et imprime, pour chaque rejet, une composante et une lettre manquante. Son [résultat](controle_D4_cycle6_classes.json) est autonome.

La coupe est commune à g18 et g20, sans P0. Elle n'invoque aucune classification de lattices, aucun rang20 universel modulo2 pour D4⁶, aucun shadowframe, ni l'existence d'un graphe. Elle combine la même sélection des42 u avec les six composantes de cette enveloppe déterminée.


---

# Pièce : ETAT_REPRISE_SNAPSHOT.md

SHA256 : b6efdf6ca439965052173d3f97c5447786d69900c53d1fb7093889f440460ae7

# État de reprise — 27 septembre2026, attaque directe commencée à08:36 UTC

Demande active : attaquer directement le repère complet ; abandonner les balayages indépendants par étoile. Cette reprise travaille avec les42 racines, les7 blocs et les2 normales dans UNE MÊME enveloppe intégrale unimodulaire24.

## Objectifs et limites

**L’involution n’est toujours pas exclue. Aucun rang g⁻=18 ou20 n’est fermé globalement ; involution ⇒ prisme n’est pas démontré.** La poursuite programmée reste active. Les normes9/10 demeurent ouvertes globalement ; le registre historique P=0 (278 types g18 fermés,163 ouverts ; aucun type g20 entièrement fermé) n’est pas modifié par les nouvelles coupes d’enveloppes.

## Avancées globales acquises, sans P=0

1. Les42 u engendrent N sur les ENTIERS : U((T+4I)z)=−h(Cz), les colonnes sœurs donnent2h dans leur span, les relations donnent3h, donc h y est aussi. Cette étape rend les coupes du dual applicables à toute sélection42.
2. Piège d’axes courts : si un w de norme≤1 a tous ses produits avec42u entiers, sa projection sur N est nulle par minN*=8/7. Trois directions indépendantes suffisent à exclure un repère dans U24. TOUTE enveloppe contenant D8³ est fermée : une classe3 physique impose vvv ou un centre vectoriel commun aux classes v-spinor ; le prolongement Lagrangien interdit les autres centres. Trois contrôles concordent135/32 et8+24. Le collage explicite possède en plus les preuves Gram modulo2=20<22 et indice.
3. Aucun D11 dans U : une projection spinorielle physique forcerait D12 ; sans spinor les11 axes seraient dans le dual court. Toutes les composantes D_n,n≥11 sont donc interdites dans l’enveloppe.
4. Classification couvrante D6⁴ : tout collage impair admissible se réduit au cycleC4, par code autodual[8,4], puis poids2 et couplage des huit symboles. Deux doubles arêtes donnent D12. Seconde implémentation :135 codes,30 pairs/105impairs,45boucles/12doubles/48cycles.
5. Dans D6⁴, six blocs fractionnaires sur UNE même paire opposée sont impossibles. Trace commune ⇒ deux normales H1 ; énergie exacte k=1 ou3 ⇒ mêmes quatre unités pour les deux normales ⇒ racine projetée de norme6/7<8/7. Seconde vérification indépendante :1716 compositions,16 profils exacts,0 paire normale admissible. Ferme(f_A,f_B)=(6,0)/(0,6), pas toutes les répartitions de six.
6. Régime mixte4+2 avec septième bloc entier de typeI dans la paire à quatre : les centres des quatre blocs doivent être distincts. Toute répétition impose au moins trois unités normales communes. Deuxième rejeu1365/870/150/270, aucun passe le gap dual. Le corollaire signé, également audité, impose EXACT2+2 pour les quatre centres distincts (énergie deux orientations, puis orthogonalité des deux spinorsBD). Les autres types de septième bloc et le régime entier restent ouverts.
7. Théorèmes theta autonomes : #χ8=48+r ; sommeχχᵀ=(16+r)I−8Z ; coque3=4096 et son moment(512+2r)I−24Z. Lorsque r=0, la matrice carrée24 des caractéristiques force24ombres orthogonales. Donc le template E/M/B par un code autodual doublement pair[24,12,8] est désormais OBLIGATOIRE pour toute enveloppe sans racines. Les sept octades portent sept multigraphes cubiques8 sans triple arête, couplés aux MÊMES42 mots. Aucune unicité de Golay supposée.
8. Enveloppe D4⁶/C6 : toute sélection physique emploie au moins6 des8classes3 ;231/256 familles d’appuis exclues,25nécessaires restantes. Pour la paire de normales0803, toute sélection des sept octades de rang binaire≤4 est exclue parce que son support des huit colonnes1 n’est pas dans le code. Les autres paires et rangs restent ouverts.

## Prochain sous-problème concret

- Enveloppes sans racines : rechercher une contradiction sur le système COMPLET E42/M7/B2, avec IncE=−6M et EᵀE+4MᵀM+BᵀB=56I, puis les sept graphes cubiques couplés. Une simple sélection de sept octades ne constitue pas un repère.
- D6⁴ : les répartitions mixtes4+2/2+4 et les totaux0/2/4 ; imposer les mêmes normales et les off-diagonales du frame. Ne pas réintroduire un choix de normales par bloc.
- D4⁶/C6 : les25families de classes nécessaires, tous les autres systèmes de racines encore admissibles. Aucune coque positive seule n’est un graphe.
- C1 sans symétrie et normes9/10 : acquis antérieurs conservés, pas de fermeture uniforme nouvelle par extrapolation.

## Livraison et contrôles

Dossier propre : outputs/attaque_globale_27_0836. Bilan : BILAN_ATTAQUE_DIRECTE_REPERE42_7.md ; preuves compilées : PREUVES_COMPLETES_REPERE42_7.md ; sources/sorties : DOSSIER_SOURCES_SORTIES_REPERE42_7.md ; manifeste : MANIFESTE_REPERE42_7.json. L’archive réunit cette campagne et le dossier0803 intact.

Les positifs H(2,3) et BvLS sont reconstruits et vérifiés exactement : λ/μ, polynômes S/H, incidence et2h dans le span entier des racines. Génération totale affirmée seulement pour r impair(H2,r=1) ; non imposée à BvLS(r=4). Pas de F7/P0/genre99 imposé aux contrôles.

Seuls les fichiers écrits dans ce fil ont été lus. Aucun dépôt, Web mathématique, SAT/CP/PLNE, solveur externe ou Python local. Petits calculs exacts JavaScript, sans fenêtre visible. Les trois agents ont communiqué directement et écrit des preuves/implémentations séparées.

---

# Historique figé des reprises précédentes

<!-- Livraison globale 0803 figée et vérifiée : outputs/attaque_globale_27_0803/ATTAQUE_GLOBALE_27_0803_PREUVES_CERTIFICATS.zip ; 69 entrées, 68 fichiers comparés au manifeste et aux sources ; SHA256 e55e730bedc4ee008819647dc235873beae25aef83d908cba744af4990cfce98. Audit : AUDIT_LIVRAISON.json. Aucun g entier exclu. -->

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

<!-- Livraison0736 vérifiée : REPRISE_27_0736_PREUVES_ET_CERTIFICATS_COMPLETS.zip ; SHA256 9cdc6e3cbab743135a8ce1607179d0b3ffc54f6e06441e36cc37f7bfccd20fa2 ;914 entrées, CRC et SHA toutes vérifiées contre les sources. Rapport indépendant : REPRISE_27_0736_PREUVES_ET_CERTIFICATS_COMPLETS.zip.AUDIT.json. Les fichiers archivés0736 sont désormais figés ; seul cet état parent reçoit ce pointeur après livraison. -->

# État de reprise — 27 septembre 2026, reprise 07:36 UTC

Photographie vérifiée avant livraison. Seuls fichiers produits dans cette conversation ; aucun dépôt ni Web mathématique ; aucun solveur/SAT/CP/PLNE/Python local. Les arbres Python sont exécutés à distance sur SageMathCell ; diagnostics JS bornés et opérations de preuve/archives locales. Toutes les pièces des agents sont figées. L'automation reste active : involution exclue ou involution ⇒ prisme NON atteint.

## Résultats nouveaux acquis

1. **Type44 g18/P0 fermé** :267/267 racines,5 fragments16+70+72+71+38,15 tranches directes strictes,363268 nœuds=118323 internes+115826 vides+129119 CN,depth5 racineincluse. Domaines13773,seed9158,4615 retraits=1333L1+1221S1+1052S2+1009centre. H18det5,char−1,MRV8,z=(0,10),πz=(2,7). Second moteur H18direct ; rapprochement catalogue/domaines/journal/seed/arbre/sorties exact. Aucun budget et aucune relance d'éditeur non liée ne comptent.
2. **Registre ACTUEL propre441P0 :278 exclusions g18,163 ouverts=127 rang18 scindés+36 singuliers.** g20:0typeentierexclu/441ouverts. Snapshots REGISTRE_882_APRES_TYPE44.json et LISTES_RESTANTES_APRES_TYPE44.json dans reprise_27_0736. REGISTRE_882.json y reste le baseline277/164. Seule18:44 change. Raccordindépendant124SHAfreeze44+109SHAanciens41 inchangés.
3. **Classification complète q2/s5/C8 exact+EXACT3extras** :22racineshorsT,1540triplets parclasseD4=4620total. Garder le planCprescrit ;admis76/388/52supports dans503/1020/1526 ;profilsprojectifs76/624/52. Chacun des16 plansCde1020 a mêmesprofils. Conditions 503/1526:Eextw0,ΔFw0 ;1020:Eextw0,w²+2(Fw)²0. Deuximplémentations (projection/cocharge et affine+diagonalisation) concordenttousprofiles ;preuve couvrante EXTENSIONS_EXACTES_TROIS_RACINES_D4.md. Aucuneombre/SRGdanscontre-témoins.
4. **Deuxblocsextérieurs** :seuls128cheminsàunpont+16deuxponts peuventéquilibrer3nonzeros. 503/1526 :16cheminsfermési=j/signproduct−1,νégales.1020:96chemins+i≠j et16deuxponts ;deuxponts νattach=4νbridge. Audit144×3 et1824témoinsC,v. Ces passages empêchent une fermeture universelle de la strateexact3 par l'incidence seule.
5. **Nouvelles familles d'ombres1526 fermées** :sur52supports,32profilsνégales et20profils{2η,η,η},η∈{3,5,6},une ligneprojective chacun. Troisnormes distinctes ou2égales+troisièmeQUADRUPLE sontimpossibles. Témoinnontriangle(3,5,5)conservé. Empreinteℰ={a:D_ai≠0quelquei∈T},centresannulés exclus. Normdouble⇒Dcolumndouble horsℰnul (±3d0±d1±d2=0). Normégales⇒trianglerootéquilibré, chaqueétiquettehorsℰtoucheune paireavec mêmeorientationquecommunintérieur,μ2⇒≤1label/pair,≤3labeltotal. Deuxcoupescollectives démontrées+audit1404lignesternaires/192signcomparisons. OMBRES_TROIS_EXTRAS_1526.md.

## Prérequis conservés, portées et contrôles

- Le modèle commun Schur physique H49=3I−S,F7,H49²0 reste indispensable ; H48²0 faux. PourinverseQreflexifsymétrique:X0=(I−AQ)X,R=D−XᵀQX ;XR=−AX0,R²=−X0ᵀX0,X0R0,R³0. ρ estcompressionbilinéairesurkerX0, pasrestrictionendomorphisme.
- Saturation s=2q+ρ=5:R=CᵀL+LᵀC+VMVᵀ, M=I3(q1)ou3(q2), contraintescommunes CCᵀ=CLᵀ=CV=LV=VᵀV=0,LLᵀ=−𝒯ᵀ𝒯,XCᵀ=XV=0,XLᵀ=−A𝒯. Lesclasses1526nouveaufiltre exigentchargeEXACT8 etexactement3extras ;plus3extras/taillechargeautre horsportée.
- Anciennecoupe ≥3extras physiqueéquilibréesnonzero de0636 restevalide avec seshypothèses. Ne pasconvertir supportsmod7 ennormesentières.
- Type281/s≤4 :4directionsHallmortes,15géométriesfaiblesrestantes ;aucuntype281entierfermé. Stratesq2/s5 nouvelobjetci-dessus, pasétatscommunscompletsencore.
- Covariancemod4 XXᵀ=7A−A² :ancien64tests unaires0cuts/48all4096syndromes reste résultatnégatif ;nepasrépéter domainesinchangés.
- PositifsH2/BvLS de0636figés :constructionJS+Pythonindépendantes,λ1μ2,H=rI−S,H²=dH,XXᵀ=dA−A²entier+mod4 ;(r,d)=(1,3)/(4,9),local4/31,far0/90. AucunP0/F7/g18/g20imposé à cesgraphes. NouvellesclassificationsD6F7nonprétenduesapplicablesm2/11.
- HorsP0,3308classescitéesparstructures n'ontpasétésweepéesiciaujourd'hui.
- Normes9/10 encoreouvertesglobalement. Anciennorm10/cinqblocsexclu sousréductionflatstable seulement.
- CasAuttrivial :coupuresSchurC1 etétoilecomplète conservées,aucunplafonduniformenouveau.

## Prochain sous-problème concret

1. g18 :prochainindex45,puis50dansla liste actuelle127rang18scindés. Partirdepreuvesacquisesetfragmentcompletuniquement ;aucunpréfixebudgetnecompte.
2. g20 :fixerC8exact/3extras dansles étatsphysiquescommuns,type281q2s5, appliquercritères1540etcoupesℰ1526, puisombrescommunes etcochargesL/flux XLᵀ=−A𝒯 ;pasdechoixGramindépendants parpaire.
3. Étendre aux4extras ouchargessupportdifférent sansréutiliserlacoupe3 commeuniverselle. Comptercontraintesdes7blocsdansunmêmegraphe.
4. Relèvementmod4 àutilisersur DOMAINESconditionnés ;ancientriplesunaires tropfaibles.

## Livraison

RAPPORT_POUR_C1_C2_STRUCTURES.md lisible ; AVANCEES_COMPLETES_PREUVES.md et DOSSIER_COMPLET.md reproduisent preuves0736 puis dossierhistoriquecomplet0636. LIRE_D_ABORD.txt pourtéléphone. Archiveconsolidée prévue outputs/REPRISE_27_0736_PREUVES_ET_CERTIFICATS_COMPLETS.zip :reprend entréesancienarchive0636sansrecompressionet nouvellespreuves ;manifestSHA +relectureindépendanteCRC/SHAcontrechaquesource. Étatparentsera complété parSHA aprèscréation, snapshotci-présent restefigé.

## Pièces finales et hashes

Uniondirecte44 :6a47ffa85008e06ba805cfa525d56a6187292ed8472e35dfedaf742df4ff63a2.
Registreaprès44 :e826bbef620e0de8ceda69fdaf813c233f66a092b8ae826dbb5698ac5a803eae.
Manifestefreeze44 :3152b44d086664e3f8e3b724286ed6c5e958b27486f061ae05c1d8609db30722.
Preuvecomplète44 :c8235ddcfa541eef71e80748c3918bfbf3e34a3b7dfa4cb9f3cf82b6aca2cd17.
Auditmath :MANIFEST_AUDIT_MATH0736.json puis MANIFEST_AUDIT_INDEPENDANT_FINAL0736.json (20piècespropres/24prérequis), anciennes14pièces/17prérequis inchangés.

---

# Historique figé des états précédents

<!-- Livraison0636 vérifiée : REPRISE_27_0636_PREUVES_ET_CERTIFICATS_COMPLETS.zip ; SHA256 0a158baffe2b9b6787ee1ed4430588cfad8490481aebc7f44c318961262da2ce ;706entrées, CRC et SHA toutes vérifiées contre les sources. Audit séparé : REPRISE_27_0636_PREUVES_ET_CERTIFICATS_COMPLETS.zip.AUDIT.json. -->

# État de reprise — 27 septembre2026, reprise06:36UTC

Photographie vérifiée avant livraison de reprise_27_0636. Seuls fichiers créés dans ce fil ; aucun dépôt ni Web mathématique ; aucun solveur/SAT/CP/PLNE/Python local. Recherche Python pure distante SageMathCell ; petits contrôlesJS bornés et opérations d'archive locales. Automation active : involution exclue ou involution⇒prisme NON atteint.

## Nouveautés acquises

1. Type41 g18/P0 fermé :233/233 racines,5fragments71+28+32+76+26,13auditsstricts complets,244034nœuds=79766internes+78718vides+85550CN,depth5racineincluse. Domaines13285,seed8905,4380retraits(1259L1+1169S1+1042S2+910centre). Doublevoie petitsGram/H18direct et raccord physique indépendant. PREUVE_TYPE41_REGLES.md, CERTIFICAT_TYPE41.md, audit_type41_union_independant.json et audit_raccord_type41.json. Aucunbudget ne compte.
2. RegistreACTUEL propre441P0 :277g18exclus,164ouverts=128rang18scindés+36singuliers. g20:0typeentierexclu/441ouverts. Lire REGISTRE_882_APRES_TYPE41.json et LISTES_RESTANTES_APRES_TYPE41.json dans0636 ;REGISTRE_882.json y restehistorique276/165. Seuleligne18:41change.109SHAfreeze41 et91SHAfreeze40contrôlés.
3. Type281/g20 :115géométries,4directionscharge réfutéesHall(1,3,6)/(1,6,2)/(1,6,6)/(0,1,1),maxcentres10/10/6/8 <12. FULL/q0domainesvides déjàconnu.115tablesphysiquesindépendantes concordantes ;s≤4laisse15géométries(7iso+8plans tangents). Aucun type281 entierfermé.
4. ThéorèmeSchur saturé s=2q+rho=5 :R=CᵀL+LᵀC+VMVᵀ, M=I3(q1)ou3(q2), CCᵀ=CLᵀ=CV=LV=VᵀV=0,LLᵀ=-TᵀT ;XCᵀ=XV=0,XLᵀ=-AT. Applicable aussi chargeiso/plan tangent. Compressionrho bilinéaire, pas restrictionendomorphisme. Preuveadverse AUDIT_SATURATION_SCHUR5.md,42fixtures indépendantes,aucuntémoinSRG.
5. Nouveauobjet :troiscirculations TI danskerincidenceD6. q2/s5/supportchargesEXACT8⇒au moinsTROISbalancedνnonzero horscharge. ClassificationprérequisD4copiesdans0636/prerequis_appui8.220supports9+66supports10D4 sansTI3, puis84extensionsdeuxracinesextérieures sansTI3,2implémentations+preuvehumaineuniforme. Ne pas convertir en fermetureglobale normes9/10.
6. EXACT3extras surUNblocextérieur :168cas(56×3) audités. Classe1526tous56impossibles ;5038passagesseulement ;102056passages,contre-témoinTIexact sansombresniSRG. Familleconditionnelle1526 fermée,pasleg20global. TROIS_EXTRAS_MEME_BLOC.md.
7. Testcovarianceintmod4 XXᵀ=7A−A² :64tests sur16strates/faibles×4triples,0exclusion,48atteignent4096syndromes. Ne pas réessayercesdomainesunairesinchangés. Conservécomme résultatnégatifdansCOVARIANCE_MOD4_ET_CONTROLES.md.
8. ContrôlesréelsH2/BvLS reconstruitsJS puisPython distant,36/29403pairesλμ, H=rI−S,H²=dH etXXᵀ=dA−A² surentiers+mod4. (r,d)=(1,3)/(4,9),local4/31,far0/90. Anciencontrôlemod3α1 resteexactséparé ;aucunP0/F7/g18g20imposé.

## Prochain sous-problème concret

- Balayage g18 :prochainindexouvert rang18scindé44,puis45/50. Reprendre uniquement lesarbresintégralementfermés/audités ;unbudget interrompu nefermepasuneclasse.
- g20 :type281 etsonmodèleCOMMUN decharges/cocharges/résidu. Utilisercut≥3 seulement quandchargeEXACTsupport8fixé ;niunknownchargesnuls par défaut,nisquaredR0dansstrateschargées. Aprèscoupures,encoder étatscommuns etfluxinhomogèneXLᵀ=-AT, pasgramspairparpairindépendants.
- Fairejouerles7blocs simultanément parSchurconjoint,et contrôlesmod4surDOMAINESconditionnés ;lestriplesunairesactuels sonttropfaibles.
- HorsP0,3308classesrapportéesparstructures nefontpaspartiedubalaye441 ;nepasextrapoler.
- Normes9/10 encoreouvertesglobalement ;strates5bloc/norm10 antérieures sousflatstablegardentleurspropreshypothèses.
- CastrivialAut :travauxC1 généralcoupuresSchur/étoilecomplète conservés ;aucunplafonduniforme ni exclusionglobale. Pasdeweb/repo pourreprise.

## Livraison

RAPPORT_POUR_C1_C2_STRUCTURES.md estlisiblecourt ; AVANCEES_COMPLETES_PREUVES.md contient toutesnouvellespreuves,prérequis etannexehistorique. Archiveconsolidée attendue :outputs/REPRISE_27_0636_PREUVES_ET_CERTIFICATS_COMPLETS.zip ;manifestSHA etCRC/SHA indépendants disponiblesaprèscréation. Lesdossiersantérieursrestentfigés. Ne pasmettreautomation enpause :aucuneciblesubstantielle finaleatteinte.

---

# Historique figé des états précédents

<!-- Livraison0535 vérifiée : REPRISE_27_0535_TROIS_CAMPAGNES_PREUVES_ET_CERTIFICATS.zip ; SHA256 61f9af2f0aaf690d8c073202970907ef04d3d70f1cc45ed6792777c8220a9edb ;525entrées CRC/SHA toutes validées. -->

# État de reprise — 27 septembre2026, reprise05:35UTC

Photographie finale de cette reprise. Lire outputs/reprise_27_0535/RAPPORT_POUR_C1_C2_STRUCTURES.md et DOSSIER_COMPLET.md. Aucun dépôt/document préexistant/Webmath/SAT/CP/PLNE/solveur/Pythonlocal. Les recherches exactes Python ont été exécutées à distance sur SageCell en appels20/25s ; quelques contrôles JS courts, puis compression/CRC/SHA locale. Tout fichier consulté est produit dans ce fil.

## Résultats acquis

- Type39 sous P0/g18 :209/209 racines,113143nœuds, second H18 exact intégral et binding catalogue/domaines/seed ; exclu.
- Type40 sous P0/g18 :251/251 racines,5 fragments producteurs disjoints77+19+39+72+44 et11 rapports stricts indépendants,263504nœuds =87006internes+85322vides+91176CN ;depth6 racine incluse. Budget001indécis entièrement ignoré. Binding adverse direct rangH18=18/det3/root1/MRV251. Exclu.
- Registre propre441P0 :276typesg18exclus,165ouverts=129r18scindés+36singuliers. g20:0type entier exclu,441ouverts. Snapshots finaux REGISTRE_882_APRES_TYPE40.json et LISTES_RESTANTES_APRES_TYPE40.json ; fichiers canoniques REGISTRE_882.json de la freeze39 restent historiques275/166, ne pas les prendre comme snapshot actuel.
- c7 physique fixé :1254/1254μ couverts,350447locauxinversibles tous réfutés :350428normes+9rang/signe+10produits.4171482τbruts,601225postcoupons,25013couponsphysiques. Seconde voie H18 direct et union disjointe complète. Les80761singuliers restent hors balayage ; pas d'exclusion globale g20.

## Théorème uniforme nouveau : Schur chargé

H49=3I−S,F7,H²0,A19local,X19×30,D30,Qprincipal maximal,AQA=A,QAQ=Q. X0=(I−AQ)X,R=D−XᵀQX :XR=−AX0,R²=−X0ᵀX0,X0R0,X0X0ᵀ0,R³0. H48²0 faux ; R²0 ne doit pas être imposé en régime chargé.

r=18−t,t≤9. Les t coordonnées libres de X0 ont métrique Gt=I+4J, central=2somme. q=rankX0,a=rankR²,s=rankR,rho=rank FORME R sur kerX0. q−a≤w(Gt),rho≤s−2a par β_R(Ru,Rv)=uᵀRv et E=imR² isotrope. g=r+2q+rho≤r+2w+s. WittGt t1..9=[0,0,1,1,2,2,3,3,4],inclutradicalt5. Donc g20singulier s≥3odd/s≥4even ; aucune complétion conservant un Schur COMPLET de rang≤2. Cela ne ferme pas les singularités dont R a rang supérieur.

## Nouvelle classification du minimum et coupes X

g20,todd,w=(t−1)/2,s3: a0,qw,rho3,Jordan2+2+2 ; a1,qw+1,rho1,Jordan3+2. À t1,s3 automatique car s≤g−r=t+2=3.
X0R0 force E⊂F=RkerX0 ; en égalité F=E⊥β, imR∩imX0ᵀ=E et dim somme=w+3. Une ancienne possibilité Fdroite transversale a été corrigée avant livraison ; aucune coupe n'en dépend.
Charges t1/3/7/9: normes nonnulles de caractère−1/+1/−1/+1 si s≤4. Mauvaise norme ou Gram partielrank≥2 ⇒s≥5. t5: radicalconstant1_5 doit être dans imX0 COMPLET ; absence ⇒s≥5. Préfixe sans radical ne réfute qu'au plafond de rang. Preuve et audit EGALITE_SCHUR_RANG3_G20.md/AUDIT_EGALITE_SCHUR_RANG3.md, dix tableaux et18fixtures synthétiques exécutés. Pas de balayage de domaines par ces coupes. Type281 unique t3g20 propre, encore ouvert : application concrète suivante, avec s≤t+2=5.

## Contrôles positifs réels

Deux constructions indépendantes H(2,3)/BvLS et partitions signées, paramètres propres p3,H=I−S,sansP0. BvLS :g35,r20,q4,s15,a2,rho7 ;35=20+8+7,R³0,X0R0,X0X0ᵀ0,β et E, compressionρ7directe. H(2,3)far0vacu mais identitéSRG/secteur vérifiée. Ne pas annoncer les bornes7propres comme testées sur ces premiers3.

## Artifacts et reprise

Dossier courant PREUVES_COMPLETES_RECENTES.md contient les nouvelles preuves intégrales et toutes celles de0435. DOSSIER_COMPLET.md contient l'historique Markdown complet. LIRE_D_ABORD.txt pour téléphone. ZIP final outputs/REPRISE_27_0535_TROIS_CAMPAGNES_PREUVES_ET_CERTIFICATS.zip reprend0535,0435,suivi_structures avec manifestSHA et relectureCRC/SHA de touteslesentrées ; rapport de vérification séparé outputs/REPRISE_27_0535_VERIFICATION.json. Les anciennes grosses archives restent leurs certificats immuables. Ne modifier ni freezes39/40 ni fichiers0435/précédents.

Prochain travail : type41, premier des129r18scindés restants ; une nouvelle forêt bornée, fusion complète seulement et second audit intégral. Singuliersg18 : septPARTIALr16 ellcommun,29FULL ; conserver R³0pasR²0. g20 : appliquer les nouvelles coupes X au type281/s≤4 puis classifier chargés s5 ; traiter autresplacementsc7 etclasses503/1526 sansconfondre640framesabstraits et géométriesphysiques.

Le catalogue3308sansP0et gminus∈{18,20}sansP0 sont des inputs de structures/C1, pas une exécution personnelle ; les2867autresreprésentants n'ont pas été fournis. Les normes9/10 restent ouvertes globalement, cinqblocsnorme10 fermé uniquement plate/stable. Appui résiduel9 ne signifie pas norme9.

Aucune cible globale atteinte. Involution et involution⇒prisme restent ouvertes. Automatisation à laisser active. Ne pas déclarer les seules identités automatiques une résolution.


---

# Historique conservé

<!-- Dernière archive0435 vérifiée : REPRISE_27_0435_DEUX_CAMPAGNES_PREUVES_ET_CERTIFICATS.zip ; SHA256 f1f74e63916cecce47f2282bde9ed90fa6c8d873a6d7e35cf7e0b9c15d505376 ;296entrées,CRC/SHA tousvalidés. Dossier complet : outputs/reprise_27_0435/DOSSIER_COMPLET.md. -->

# État de reprise — 27 septembre2026, reprise04:35UTC

Cette photographie est la plus récente. Lire ensuite les preuves de outputs/reprise_27_0435. Tous les fichiers utilisés sont ceux produits dans ce fil ; aucun dépôt conway99-* ni document préexistant consulté. AucunSAT/CP/PLNE/solveur/Pythonlocal.

## Résultat acquis à cette reprise

Type35 entièrement exclu sous involution,P0,g⁻18. Six fragments32+41+46+47+47+6couvrent219/219racines. Tous ont un second audit physique exact ; union et version portable exact=true,excluded=true. Forêt141382nœuds,47954internes,46810vides,46618obstructions ; profondeur maximale cinq colonnes. Le producteur fusionné conserve ses flags historiques ; le verdict scientifique est celui de l’union auditée.

Bilan cataloguepropre441P0 : g18,274fermés et167ouverts=131r18scindés+36singuliers ; g20,0type entier fermé et441ouverts. Le catalogue3308sansP0et g∈{18,20}sansP0sont des inputs du brief, pas une exécution personnelle. La cible involution⇒prisme ou exclusion de touteinvolution reste ouverte. Ne pas mettre l’automationenpause.

## g20 : avancée couvrante sur un placement c7 fixé

La seconde classification couvre640frames signées de l’appui exact8/class1020/c7 ; cinqclasses de128, action abstraite uniquement. Les septcentres sont hors empreinteD4par la campagneprécédente. Les quatre ratios de normes et leur trace forment exactementkerCᵀ de dimension5 ; toutesles16planes canoniques vérifiées.

Le placement physique π,Z,E,F,V du baseline G20_C7_TOUT_MU_REMOTE.py est fixé. Parmi1254μcompatibles,678sont entièrement audités :0..412,555..654,790..869,1025..1109. Lacunes576 :413..554,655..789,870..1024,1110..1253. Les μinterrompus ne sont pas comptés. Secondaudit :308848τ restants,13875coupons physiques ;176586rejets de normes,7rang/caractère et3produits, soit176596locauxinversibles fermés. Les44182singuliers restent horsscope. Aucun autreplacement, typeg20entier, appui>8ou classe503/1526fermé.

Le wrapperfast a une preuve analytique du préfiltre K2/K3/S1/S2, exacte aprèscyclesC12/2C6. Repriseparrun_batch_fast(base,range(start,end),time_limit_s=20). La tranche132..319 n’a imprimé que188résultats individuels complets, sansrésumébatch ; ils ont été sauvegardés et audités chacun. Éviter lesappels60s ; reprendreavecplafonds20s et conserver lescomplets seulement.

Une borne négative réelle sur les987profilsgolden : rangaffine5des cinqviolations, mineurdet4 ; chacune des2801formes linéaires projectives s’annule surunprofilexistant. Aucuntesthomogèneunique ne ferme cetéchantillon. Deuxprofils nécessitent la cinquièmerelationtrace. Nonlinéaire/globalresteouvert.

## g18 chargé : progrès concret

PourA=H19physique,Qsym,AQA=A,X0=(I−AQ)X,R=D−XᵀQX : XR=−AX0,R²=−X0ᵀX0. PARTIALkcharge1,rho0 donneX0=u0cᵀ,R=c ellᵀ+ell cᵀ, Xell=−Au0,c·ell=0,ell²=−u0². Lesciblespeuventêtrenonnulles ; nepasréutiliserlesfluxFULL. H48ne satisfaitpaslecarrénulphysique.

Unvrai triplet202normal(1,0),orbites0/1/2, a charges4,3,0,ν1,1,0,ell1,6,libre ; p02=p12=2,h01=−1. La colonneéquilibrée exigeell2∈{3,5}contre0et{2,4,6}contre1. Chaque paire isolée passe,aucunellcommun. Témoinphysiqueet secondcode acquis ;aucunrégime/typeentierfermé.

Initial202huitnormales : septpassentflux/moments,normal(1,6)domainvide déjàancien. Forêtbornée202normal(1,0),8racines,200nœuds,depth4 :0racinefermée ; rienàextrapoler. LeQprincipal donneκ=−5n0²−n0n1−5n1²nonzero, Rrank2,R²rank1,R³0danscettejauge.

## Contrôles

Nouveauxflux validés par21fixtures physiques abstraites et vraisgraphes reconstruits. H(2,3),p3,secteur4/rang2,far0 ; BvLS,p3,secteur121,local31/rang20,far90,rankX0=4,rankR15. Lesidentités passent ; pasP0,F7,g18/20imposéauxcontrôles.

## Livrables et suite

LIRE_D_ABORD.md,RAPPORT_POUR_C1_C2_STRUCTURES.md,PREUVES_COMPLETES_RECENTES.md,DOSSIER_COMPLET.md,CERTIFICAT_TYPE35.md,CERTIFICAT_C7_678_FAMILLES.md,TRIPLET_PHYSIQUE_TYPE202.md,REPRODUCTION_ET_CERTIFICATS.md. Registre882etlistesactualisés ; preuves antérieures figées. ZIPdes deuxcampagnesetSHA256générésensuitedansoutputs.

Prochaineactionconcrète : achever les576μdu templatec7 enappels20s,avecsecondevoiephysique etuniondisjointe ; puistraiterseslocalsinguliers. Côtég18, type39estlepremier r18scindéouvertaprès35/36fermés. Continuerla forêtou appliquerellcommunaux7typesr16PARTIAL. Ne pascompterles678μcomme678types. Lesnormes9/10restentglobalementouvertes ; la réductionnorme10cinqblocs estconditionnelleplate/stable. C1appui résiduel9n’estpasnorme9.


---

# Historique antérieur conservé

Livraison vérifiée : REPRISE_27_SUIVI_STRUCTURES_PREUVES_ET_CERTIFICATS.zip, 7245342 octets, 140 entrées. SHA256 47a83bdd42c8fd898358bd32f33369352ef45f99bbe769faaede2856813db0b2. CRC/SHA256 de toutes les entrées relus ; anciens fichiers immuables.

# État de reprise — suivi de structures, 27 septembre 2026

## Cible et bilan

L'involution reste ouverte ; aucun théorème « involution implique prisme » n'est acquis. Aucune mise en pause de la poursuite n'est effectuée.

Notre catalogue P0 comprend 441 types, indices 0..440. A g18 : 273 types exclus, 168 ouverts (132 rangs18 scindés et 36 singuliers). A g20 : aucun type entier exclu, 441 ouverts. Les restrictions d'appuis ou de régimes restent distinctes des exclusions de types.

Le catalogue 3308 sans P0 et le théorème externe g⁻∈{18,20} sont reçus du brief de structures/C1. Les 2867 représentants supplémentaires ne sont pas disponibles ici ; nos 441 ne les couvrent pas.

## Résultats nouveaux

Type36 à g18 : forêt complète sur 177 racines, trois relectures 60+60+57 et union exact=true/excluded=true. Les règles L1/S1/S2 sont prouvées et vérifiées directement par les comptes λ/μ du graphe connu. Type35 : seulement 32/219 racines fermées et rejouées indépendamment, 187 ouvertes.

Classe1020, g20, appui résiduel réel exactement8 et rang2 : deux programmes couvrent 60912 cas. Seuls sept centres survivent, sur une empreinte de quatre labels D, avec poids (5,5,4,4). Une seconde coupe du centre fixé couvre 3200 cas et 49728 nœuds, sans feuille et sans limite : les sept centres sont hors empreinte, leur union utilise onze des douze labels. Le témoin c7 est vérifié uniquement dans cette relaxation : aucun W/K2/K3, aucune identité H=beta+R, aucune complétion des 22 autres colonnes.

Schur singulier : g=r+2(t−r0)+rho et formule de discriminant démontrés et audités. Une charge de rang1 avec rho=0 force R=c ellᵀ+ell cᵀ, donc les produits des colonnes chargées sont déterminés. Toute charge non nulle a support≥6. En régime FULL, C=0, l'identité du H49 physique donne XR=R²=0 et transfère BV=DV=VᵀV=0. H48 est seulement congruent : son carré n'est pas présumé nul. Ce transfert n'est pas utilisé en régime PARTIAL.

Les 36 singuliers ont une couverture unaire complète de 157 régimes. Les tests de sœurs sont complets pour 35 types, partiels pour281. Le producteur rejette 19 régimes ; huit FULL sont certifiés indépendamment par le graphe39 et 226956 motifs rejoués (240 tailles concordantes). Les onze autres rejets restent des diagnostics sans second certificat.

FULL202,277,281,300,303,309,360,389 sont impossibles avant toute restriction de rho, donc à g18 et g20. Pour les sept types de rang16 scindés (la liste sauf281), g18 impose r0=1/rho=0 ; g20 conserve (r0,rho)=(0,0) ou (1,2). Type281 : g18 impose (2,1), g20 conserve (1,1) ou (2,3). Aucun type entier n'est exclu par ces seuls FULL.

C1 antérieur : appui réel9 d'un résidu de rang2 sous droite générique impossible, sans symétrie ni P0. Cela ne ferme pas les normes9/10 de L_T. Norme10 sur cinq blocs est fermée uniquement sous la réduction plate stable ; les six/sept blocs restent ouverts.

## Fichiers

RAPPORT_POUR_C1_C2_STRUCTURES.md ; PREUVES_COMPLETES_RECENTES.md ; DOSSIER_COMPLET.md ; LIRE_D_ABORD.md ; LISTES_POUR_STRUCTURES.md ; BASELINE_133_PLUS_36_0249.json ; LISTES_RESTANTES.json ; TYPES_RESTANTS_G18.json ; REGISTRE_882.json ; les preuves/certificats de Type36, c7 et FULL ; diagnostic_singuliers_union_36.json ; REPRODUCTION_ET_CERTIFICATS.md.

Les archives anciennes sont immuables. Leur historique intégral est copié dans DOSSIER_COMPLET.md. Les anciens certificats volumineux restent dans l'archive0249 (581 entrées, 122757539 octets, SHA256 c9c10371fc177c51f3f7dbf2384551a3fb496c8bf94108a725d0b89a1ff1936d).

## Prochaine progression concrète

1. Type35 : reprendre la forêt partielle, sauter exactement ses 32 root_options_closed, commencer au choix49. Sauvegarder puis rejouer indépendamment chaque fragment. Une limite n'exclut jamais les choix restants.
2. Sept types rang16 scindés à FULL impossible : exploiter toute la strate g18 r0=1/rho=0 avec une seule charge c et un même ell global, support c≥6. Brancher sur une ancre chargée, fixer les produits des chargées et les trois états des non chargées ; appliquer ombres, points, sœurs et centres.
3. Type281 : 53 hyperplans PARTIAL passent les unaires. Grouper les sœurs dans une droite résiduelle commune gamma, sans choisir un espace indépendant pour chaque paire. Les sorties005+006 couvrent seulement les unaires ; la sortie002 garde ses tests de sœurs partiels.
4. g20 classe1020/appui8 : raccorder les onze labels au W local, aux normes de Schur et à K2/K3. Ne pas appliquer la coupe à une sélection dont l'appui peut encore grandir. Classes503/1526 et appuis>8 restent à traiter.
5. Catalogue3308 : ne pas inventer les représentants absents. Tant qu'ils ne sont pas fournis, nos statuts numériques restent P0 et les comptes sans P0 sont ceux reçus dans le brief.

## Méthode et ressources

Seulement les fichiers de cette conversation ; aucun dépôt, document préexistant ou recherche bibliographique consulté. Aucun SAT/CP/PLNE/solveur. Programmes propres bornés à20/25 secondes exécutés à distance via SageMathCell officiel ; pas de Python local ni de fenêtre Python. Contrôles JS exacts courts et assemblage des fichiers dans le workspace.

H(2,3) et BvLS passent les contrôles génériques, avec leurs paramètres adaptés en caractéristique3. P0/mod7/g18 ne leur sont pas imposés. Tous les onglets de calcul créés sont fermés après sauvegarde. Les agents algèbre, combinatoire et audit ont communiqué directement et fourni des fichiers stables. Aucun résultat indécis ou automatique n'est déclaré résolution globale.


---

# Historique conservé avant ce suivi

Livraison vérifiée : REPRISE_27_0249_PREUVES_ET_CERTIFICATS.zip, 122757539 octets, 581 entrées, SHA256 c9c10371fc177c51f3f7dbf2384551a3fb496c8bf94108a725d0b89a1ff1936d. Les494 entrées antérieures restent intactes ; CRC32/SHA256 de chaque entrée relus. DOSSIER_COMPLET.md : 2969416 octets, SHA256 8d4b5a35d148fae4e843b8c4feae1a2df60e848b78fd9d6188dd3b6ab243aa3e. Les deux derniers onglets cachés ont été fermés après sauvegarde.

# État de reprise — 27 septembre 2026, 02 h 49

## Acquis nouveaux

C1 : sous droite générique modulo7, rang R=2 et appui exact9 sont incompatibles. Preuve sans involution ni P0, avec classification finie indépendante des420 exceptions S6 et fermeture inter-couches.

g20 / résidu appui8 / classe1020 : c0/S8 fermé ; trois profils c0/S7 fermés (8,4^6), (7,5,4^5), (6,6,4^5), coûts40/26/32>24. Les deux autres profils restent ouverts, minima19 et15. Aucune répétition ±r non nulle possible, tous poids et centres. L’extension F≥w−λσδ est réfutée par les relations de poids5/coût3.

g18 sous involution et P0 : **272/441 types exclus,169 ouverts** (133 rang18 scindés,36 singuliers). Nouveau type34 :318 racines distinctes complètement rejouées, audit_type34_union_independant.json exact/excluded. g20 :0 type entier exclu,441 ouverts.

## Fichiers et vérifications

RAPPORT.md ; PREUVES_NOUVELLES.md ; DOSSIER_COMPLET.md ; certificat Type34 et forêts/audits ; REGISTRE_882.json. Sources et sorties indépendantes C1 et1020 figées dans ce dossier. H(2,3) et BvLS passent avec leurs propres paramètres en caractéristique3 ; P0 ne leur est pas imposé.

Aucun solveur, aucun Python local, aucun dépôt ou document préexistant consulté. Calculs exacts distants bornés, petits contrôles JS et assemblage locaux. Les deux derniers onglets cachés sont fermés. Les répétitions d’éditeur sont archivées, dédupliquées et sans effet sur la couverture certifiée318.

## Suite concrète

1. g18 :35,36,39,…, exclusion uniquement après couverture auditée ;36 singuliers à traiter par coupures conjointes/torsion.
2. g20 : coupler cp/cm et les vrais centres aux deux profils1020 c0/S7 encore ouverts, puis autres classes et appuis. Garder une seule forme résiduelle globale.
3. C1 : appuis exacts10 et plus ; le résultat9 ne ferme pas tout k24.
4. Normes9/10 des vecteurs propres à6/7 blocs restent ouvertes ; ne pas les confondre avec l’appui9 du résidu.

**Ni l’involution ni involution⇒prisme ne sont démontrées. Automatisation à laisser ACTIVE.**

Archive cumulative : REPRISE_27_0249_PREUVES_ET_CERTIFICATS.zip, préservant les494 entrées antérieures de SHA256 e2efedcdedf724a33dc19a0cb6cb42717ece2fefb87cfad0c9e46400fe076b53. Le parent ETAT_REPRISE.md reçoit l’état de livraison et garde son historique intact.


---

Historique antérieur conservé intégralement :

Livraison vérifiée : REPRISE_27_0148_PREUVES_ET_CERTIFICATS.zip, 93146199 octets, 494 entrées, SHA256 e2efedcdedf724a33dc19a0cb6cb42717ece2fefb87cfad0c9e46400fe076b53. Les 410 entrées précédentes sont intactes ; CRC32/SHA256 de chaque entrée relus. DOSSIER_COMPLET.md : 1 603 552 octets, SHA256 e8ffcc2e7f9738074cb3a5d015cb5e4e977bc6a8b1834c9b940427a343b7a415. Les deux onglets cachés ont été fermés après sauvegarde.

# État de reprise — 27 septembre 2026, campagne 01 h 48

## Bilan acquis

Sous srg99, involution et P = 0 : **271/441 types exclus à g⁻ = 18, 170 ouverts**. Les nouveaux types 31 et 33 ont chacun une forêt complète et un rejeu indépendant H18 direct. Les ouverts sont 134 types de rang local 18 scindés et 36 singuliers. À g⁻ = 20 : **aucun type entier fermé, 441 ouverts**. g16 et A33 restent des acquis antérieurs, à ne pas refaire.

Type 31 : 285 choix, en lots 54 + 57 + 43 + 64 + 66 + 1. Type 33 : 244 choix, en lots 69 + 75 + 76 + 24. Les unions audit_type31_union_independant.json et audit_type33_union_independant.json donnent exact=true, excluded=true. Tous les appels réellement exécutés, lots bruts et sorties indépendantes sont conservés. REGISTRE_882.json est actualisé seulement dans ce dossier ; les fichiers et archives précédents sont immuables.

## Nouveaux résultats démontrés et vérifiés

1. **g20, résidu de rang deux et support exact huit, classe 1020 : toute relation ternaire non nulle a poids au moins quatre.** Avec BBᵀ = 4I, π = I − BᵀB/4, un sélecteur de poids trois donne q(πa) = (3 − t)/2 ≠ 0, puisque −2 ≤ t ≤ 2. Une ligne active D_T a donc au moins quatre occurrences. L’empreinte S satisfait S ≤ floor((32 − 2c)/4) ≤ 8, après annulation des centres. Les seize plans et leurs relations ternaires sont vérifiés indépendamment. Les seules contraintes ternaires et de degrés admettent tous les nombres de centres c = 0,...,8 dans les trois classes : elles ne ferment aucun nombre de centres ni aucune classe.

2. **Reflet commun des ombres : au plus trois colonnes, ou six avec échanges indépendants.** Pour une bijection φ commune, e_p = φ(z_p), f_p = φ(s(z_p)). Les budgets cp ≥ 3|z∩w| et cm ≥ 3|z∩s(w)| imposent des supports de blocs disjoints dans chaque classe d’orientation. Un appui huit de cette forme est donc fermé, sans P0. Une paire de sœurs donne cp=cm=3 pour tous les échanges. Un relabeling propre à chaque colonne n’est pas couvert. Pour φ générale, y = P_φ a + 2a, et non 3a.

3. **C1, droite générique, résidu R de rang deux et support exact neuf : trois familles d’ombres sont fermées.** K₃,₃ et K₅ privé d’une arête imposent, par leurs quatorze relations 0/1, la répétition des mêmes étoiles dans toutes les couches : trois voisins communs, impossible. Le prisme comme graphe d’ombres a un noyau non dégénéré de dimension trois, incompatible avec un plan totalement isotrope de dimension deux. Les identités MR=R²=0 sont dérivées des équations de SRG et du Green, pas d’une congruence de Schur seule. Aucune hypothèse P0 ou de symétrie n’est requise. La spécialisation à k=24 utilise rang R=k−22.

4. **Corollaire uniforme C1 : chaque couche comporte une étiquette de degré deux parmi ces neuf ombres.** Un degré un est impossible par MV=0. Un degré minimal au moins trois laisserait au plus six labels et forcerait l’une des trois familles fermées. Chaque couche impose donc une paire v_i=−v_j, soit deux lignes opposées du résidu. La même paire ne peut apparaître dans les trois couches. Au moins deux paires distinctes sont forcées ; pas nécessairement trois.

Preuves humaines : THEOREME_C1_APPUI9_K33.md ; ADDENDUM_C1_APPUI9_DEGRE2.md ; RELATIONS_TERNAIRES_ET_CENTRES.md ; REFLET_COMMUN_ET_BUDGETS.md. Les sources, sorties exactes et audits indépendants sont figés dans ce dossier. Pour K33/K5−e, les deux implémentations concordent sur les 512 sélecteurs, les seize plans et les couvertures entières.

## Exécution et contrôles positifs

Aucun SAT, CP, PLNE, solveur externe ou Python local. Python standard exact distant sur SageMathCell par lots plafonnés ; petits JS exacts et opérations d’artefacts locaux. Aucun dépôt, document préexistant ou site de recherche n’a été ouvert. Deux onglets cachés de calcul fermés après sauvegarde.

H(2,3) et BvLS sont reconstruits dans cette campagne : secteurs signés, K2/K3, moments et signes passent ; les 4 005 couples de lointains de BvLS passent. Leurs paramètres propres utilisent la caractéristique 3. Les deux ont des prismes : aucun P0 ou Schur nul modulo 7 de SRG99 ne leur est imposé. H(2,3) n’a pas de lointains pour ce test, mais ses contrôles locaux ne sont pas vides.

## Sous-problèmes suivants

1. Continuer le balayage g18 de rang local 18 à partir des types 34,35,36,39,... Toute nouvelle exclusion exige une union complètement auditée avant le registre. Les 36 singuliers demandent les contraintes de torsion et les coupures conjointes.
2. À g20, intégrer le degré ternaire au moins quatre et les budgets entre colonnes aux ombres réelles et à une même forme résiduelle globale M. Les ombres sans reflet commun et les appuis neuf ou plus restent ouverts. Aucun moteur exhaustif g20 n’est acquis.
3. Dans C1/rang deux/appui neuf, exploiter les paires de lignes opposées. Pour une telle paire i,j : R_ii=R_jj=−R_ij, donc g(n_i,n_i)+g(n_i,n_j)=2−A_ij et g(n_j,n_j)=g(n_i,n_i). Chercher une obstruction de charges Green et de saturation μ, au lieu de répéter les moments automatiques.
4. Les normes 9/10 des vecteurs propres à six/sept blocs restent ouvertes. Un support neuf du résidu de Schur n’est pas un vecteur propre de norme neuf.

## Livraison et limites

RAPPORT.md donne les résultats nouveaux. DOSSIER_COMPLET.md réunit les nouvelles preuves, sources essentielles et le dossier de la campagne 00 h 47 intégralement. L’archive cumulative REPRISE_27_0148_PREUVES_ET_CERTIFICATS.zip préserve les 410 entrées du ZIP précédent, de SHA256 c4c50f292cad92609846e9df74a43bdb2f20b3c00d7295c2c30d87e7a51990b0. Le manifeste SHA256 et l’audit CRC/SHA lient les fichiers ; leur intégrité ne remplace pas les preuves mathématiques.

**Aucun objectif global atteint : ni l’exclusion de l’involution ni involution ⇒ prisme ne sont obtenues. La poursuite programmée reste à laisser ACTIVE.** Ne pas la mettre en pause pour ces seules familles fermées.


---

Historique antérieur conservé intégralement :

# Mise à jour acquise — reprise27_0047

# État de reprise — 27 septembre 2026, campagne 00 h 47

## Bilan acquis

Sous srg99, involution et P=0 : **269/441 types exclus à g⁻=18, 172 ouverts**. Les nouveaux types15,26,28 ont chacun une forêt complète et un rejeu indépendant H18 direct. Les survivants sont136 types r18 scindés et36 singuliers. Aucun type entier nouvellement exclu à g⁻=20 :441 ouverts. g16 etA33 demeurent acquis antérieurs, à ne pas refaire.

Les choix entièrement vérifiés sont236 (50+90+96),232 (90+90+52),249 (76+90+36+47). Les trois unions exact=true/excluded=true sont dans audit_type{15,26,28}_union_independant.json. Toutes les parties brutes et les appels réellement exécutés sont conservés. REGISTRE_882.json est actualisé uniquement dans ce nouveau dossier ; le registre et l'archive précédents sont immuables.

## Théorème g20/r18 : classification de l'égalité |T|=8

Pour V30×2 sur F7, rankV=2, BV=0, VᵀV=0 et T={p:v_p≠0} de taille8 : le graphe signé B_T est connexe sur exactement quatre blocs, rang4, dans les trois classes D4 503,1020,1526. Les masques se lisent dans l'ordre01+,01−,02+,02−,03+,03−,12+,12−,13+,13−,23+,23−. Quinze choix des quatre blocs donnent1125 supports et1800 plans isotropes complets au total. Ce ne sont pas des graphes ; ni les ombres ni le signe de la forme résiduelle globale M ne sont déterminés par ce comptage.

La réduction structurelle rank6/5/4 et les petits certificats exacts figurent dans CLASSIFICATION_SUPPORT8.md, avec l'audit adverse AUDIT_COMPLET_SUPPORT8.md. Deux JS écrits séparément couvrent495 supports D4,128 configurations signées de rang≤5,6435 graphes simples équilibrés à six blocs et huit arêtes. Ne pas prétendre avoir parcouru binom(30,8) supports ni confondre les625 petites lignes avec la classification complète.

Dans les18 plans représentatifs admissibles, aucune paire v_i=±v_j. Pour1020, BBᵀ=4I et la projection de e_i±e_j sur kerB a norme1,4 ou5, impossible dans un plan isotrope maximal. Pour503/1526, les huit directions sont distinctes.

Avec DV=0, D[a,p]=[a∈e_p]−[a∈f_p], toute ligne D_T active a degré≥3. Si c colonnes sont centrées, coefficient_total=32−2c et empreinte≤floor((32−2c)/3)≤10. Familles fermées : support réel exactement8 avec degré1/2, ou empreinte trop grande. L'empreinte est APRÈS annulation du centre. Cette coupure ne ferme aucun type global g20.

Une preuve autonome plus faible reste livrée : au moins deux colonnes échappent au graphe des relations d'ombres de degré2. Voir DEUX_COLONNES_LIBRES_APPUI8.md ; l'ancien helper est intact.

## Programmes et contrôles réellement exécutés

Recherche Python exacte distante sur SageMathCell : forêt15 en trois lots,26 en deux lots,28 en quatre lots ; audits directs15 en trois lots,26 en trois lots,28 en quatre lots. Aucun SAT/CP/PLNE/solveur, Python local ou calcul de recherche lourd local. Les petits JS exacts et opérations d'artefacts sont locaux.

H(2,3) etBvLS sont reconstruits à nouveau : secteurs signés, K2/K3, signes, moments, budgets sélectionnés. Les4005 couples lointains BvLS passent. H(2,3) n'a pas de partie lointaine pour ce test ; ses contrôles locaux/signés ne sont pas vides. Les deux graphes ont P0=False ; ne pas leur imposer P0 ou un Schur nul modulo7.

Le helper fort coupure_ombres_appui8_forte.py est livré en plus du faible. Six fixtures JS indépendantes sont exécutées ; le helper Python réel est ensuite exécuté À DISTANCE sur ces six fixtures, toutes concordantes, avec deux contextes incomplets rejetés. Source d'appel et sortie conservées. Les paramètres exact_nonzero_support et les noms d'équations ne vérifient pas eux-mêmes le contexte : le rejeu d'une branche doit établir huit vecteurs non nuls,22 zéros et le rang2. Une norme zéro dans le plan scindé peut être un vecteur non nul.

## Sous-problèmes suivants

1. Continuer les136 types g18 r18 scindés par sélection commune et certificats complets. Tout nouveau type : rejeu H18 direct puis union exacte avant registre. Les36 singuliers demandent les contraintes de torsion.
2. À g20/r18, intégrer la classification d'appui8 à la jauge canonique et au même plan M pour les30 colonnes ; sélectionner les ombres, puis appliquer les degrés/empreinte avec contexte complet. Couvrir aussi les appuis9 et plus. Aucun moteur exhaustif g20 n'est acquis.
3. Une compression des forêts en petits sous-ensembles interdits reste possible ; ne pas l'annoncer comme exécutée. Les normes9/10 à six/sept blocs et le cas sans symétrie sont ouverts.

## Livraison et limites

RAPPORT.md donne les résultats nouveaux ; DOSSIER_COMPLET.md inclut les preuves, programmes essentiels et le dossier précédent intégral. L'archive REPRISE_27_0047_PREUVES_ET_CERTIFICATS.zip est cumulative : les331 entrées de GRAM_GLOBAL_G18_G20_PREUVES_ET_CERTIFICATS.zip sont préservées byte pour byte, avec SHA256 précédent ec542c866766e1fdc8e4ab839f469d8996ba5b3bca48388cbc37090ab61bac55. Le nouveau manifeste SHA256 et l'audit CRC/SHA portent sur tous les fichiers. Une empreinte ne remplace pas l'audit mathématique.

Aucun dépôt ou document préexistant lu ; seuls les fichiers de cette conversation sont utilisés. Les deux onglets cachés de calcul sont fermés après sauvegarde. Aucun objectif global atteint : l'automation reste ACTIVE. Ne pas la mettre en pause pour ces seuls résultats partiels.


---

# Mise à jour prioritaire — 27 septembre : Gram commun et support résiduel

Les trois coupures sont désormais rejouées indépendamment sur leurs données réelles par verifier_certificats_bilans.mjs : domaines reconstruits, cibles (4,1), (3,3), (0,2) absentes de sommes atteignables de tailles 12, 33, 37. PREUVE_COUPURES_BILANS.md et audit_certificats_bilans_g20.json. Ce sont trois coupures conditionnelles, aucune fermeture de type.

**Trois types nouvellement exclus sous P=0/g⁻=18 : 2, 6, 14. Cumul266/441 ;175 ouverts. g⁻=20 :441types encore ouverts.** Forêts236/236,268/268,270/270 revérifiées directement par H18 et unions indépendantes.

**Nouveau lemme g20/r18 démontré et audité : au moins huit résidus non nuls.** Les bilans BV=0 et VᵀV=0 réduisent aux petites configurations D4 ; deux programmes concordent sur792supports/12classes. Le premier résidu non nul a indice≤22. Six bilans racines +douze bilans ombres +trois moments sont démontrés depuis H49 complet ; ne pas supposerH48²=0.

Le pilote renforcé coupe47branches par ces bilans, mais reste au budget sur3ancres : aucune fermetureg20. Contrôles H(2,3)/BvLS et fixtures Python réelles acquis. Lire ../gram_global_g18_g20/RAPPORT.md, ETAT_REPRISE.md et DOSSIER_COMPLET.md ; archive globale des deux campagnes avec preuves/certificats/sources. Aucun objectif global atteint : automation ACTIVE ; normes9/10six/septblocs etcasasymétrique ouverts.

---

Mise à jour prioritaire — 27 septembre : sweep g⁻=18 et20

**22 nouvelles exclusions locales vérifiées à P=0,g⁻=18** :20 par translations/recentrage des chargesD6,2 par prix entiers (types0/376). Cumul263/441 ;178types restent ouverts. g⁻=20 :aucune exclusion nouvelle,441types encore indécis. Les882couples type/rang sont examinés par des conditions nécessaires ; ce n'est pas une classification exhaustive de leurs extensions.

Lire ../sweep_g18_g20/PREUVE.md, DOSSIER_COMPLET.md et ETAT_REPRISE.md. Registre intégral REGISTRE_882.json ; tous les certificats, témoins, sources et sorties conservés. Deux voies indépendantes pour20translations (32 768graphes,6 279lifts) et pourles deuxprix entiers (408coefficients,0≥14/56). Les345témoins r18/g20 passent l'auditH18direct :10 350normes+5 175produits. Jonction des mêmes sous-espaces validée pour36singuliers survivantsg18 et96singuliersg20. Les64pilotes àdeuxcharges134/353 passent encore :aucune fermeture decesdeuxtypes.

Le nouvel objet utile est la famille des relèvements d'une torsion modulo la constante universelle :Yᵀ1=0entier, K1=−21·1. Recentrerλf+a1ajoute7w et modifie la charge. GarderJ et(Σf)² ; ne pas reprojeter sur somme nulle. Des types passant les premiers lifts échouent alors avec(E,μ)=(40,41),(28,30),(20,21).

Le verrou restant est la forme résiduelle commune :zéro àg18/r18 et un mêmeplan àg20/r18. Paires ettriplets séparés peuvent touspasser alorsque quatre colonnes demandent un rang4. Le prototype d'ancrages communs est audité mais non exécuté surcatalogue. Ne pasl'annoncer comme exclusion.

Aucun Python local ni solveur externe ; Python exact distant, petitsJS locaux. Aucun dépôt préexistantlu. ContrôlesH(2,3)/BvLS conservés. **Ni involution exclue ni involution⇒prisme auxrangs18/20 ; normes9/10six/septblocs etcasasymétrique ouverts. AutomationACTIVE.** Lescompteurs historiques ci-dessous sont dépassés par cette miseàjour.

---

# Mise à jour prioritaire — 26–27 septembre : charges entières D6 à g⁻=18

**Nouveau : trente-huit familles d'étoiles exclues à P=0,g⁻=18**, vérifiées par recatalogage indépendant et certificats entiers.29r17+9r16non scindés.23des38passaient le test préliminaire de domaines ; la contradiction d'arrondi ne requiert aucun domaine. Les38certificats passeraient la projection réelle seule.

Lemme humain nouveau :charge q=Yᵀf/7 entière, ||q||²=E=fᵀBf+f·k−||k||², A0q=r où les30colonnes deA0sontD6. Borne d'arrondi ; minimum exact par graphes de parité surK6, deux méthodes indépendantes. SousKf=0entier, différencesmates0/±1non nulles, ou0/±2surauplus4blocs, ne s'équilibrent jamais.

Les deux programmes concordent sur96tables. Contrôles réelsHamming/mod3 etBvLS/mod3 :1et364directions, moments/charges vérifiés. Audit Schur99705coefficients. Aucun solveur niPythonlocal ; calculsPythonàdistance, petitsJSlocaux. Aucun dépôt ou documentpréexistant lu dans cette reprise.

Lire ../couverture_g18/PREUVE.md, ETAT_REPRISE.md, DOSSIER_COMPLET.md, certificats_projection_38.json et verification_projection_independante.json. Le dossier comprend les deux campagnesg16/g18.

Après203Witt+38charges,**200types locaux restent non exclus**, dont142r18scindés sans torsion. Quatre r16non scindés exigentdeuxtorsionssimultanées :0,134,353,376. Nouveau lemmeD :pourune sélectionglobaleSchurfixée, supportDdéterminé,degrécandidat≤2etauplus16couplagesàtester ; aucune exclusion142revendiquée.

**Indécis :** involution⇒prisme àg18/g20, exclusioncomplèteinvolution, normes9/10six/septblocs,casasymétrique. La cible de l'automation n'est pas atteinte : elle demeureACTIVE. Dernière preuveg16conservée ci-dessous ;nepaslarefaire. Les essais incomplets229domaines/paires sœurs/énergie ne sont pas des certificats.

---

# Mise à jour du 26 septembre — couverture de g⁻=16

NOUVEAU, démontré avec couverture finie et vérification indépendante : **une involution avec g⁻=16 force un prisme ; P=0 ⇒ g⁻∈{18,20}** sous les acquis de genre. Les 441 types d'étoiles P=0 sont couverts ; après rang/signe restent neuf types, six à domaines vides, deux à budget d'apex insuffisant, et un certificat entier 0≥90 sur 1994 colonnes.

Lire ../couverture_g16/ETAT_REPRISE.md et ../couverture_g16/PREUVE.md. Sources, 408 coefficients, domaines, catalogue, sorties et contrôles H(2,3)/BvLS conservés ; dossier autonome ../couverture_g16/DOSSIER_COMPLET.md.

Ne pas refaire g16. Prochaine cible : g18, d'abord les 74 étoiles de rang17 et 13 de rang16 non scindées qui exigent r0=t ; restent surtout les 142 étoiles de rang18 scindées, sans torsion locale imposée. L'involution générale et les dernières normes 9/10 ne sont pas fermées. Aucune cible globale atteinte, aucune demande de pause de l'automation.

---

Historique conservé ci-dessous (les annonces anciennes de branches ouvertes ou de planchers doivent être lues avec cette mise à jour).

# Mise à jour prioritaire — A33 entièrement fermée

Lire ../fermeture_A33/PREUVE.md et ETAT_REPRISE.md. Le bloc impair A33 a rang14 et discriminant carré, donc est non scindé. Le lemme de Witt donne g⁻≥24−2r₀ ; les certificats précédents donnent r₀≤1, d’où g⁻≥22 contre g⁻≤20. Toute A111111 (3,3) est exclue, y compris la dernière classe à g⁻20. Deux implémentations du signe et contrôles H(2,3)/BvLS passent. La mention historique « A33 g⁻20 ouverte » ci-dessous est dépassée. Les autres étoiles, l’involution générale et les normes9/10 six/sept blocs restent ouvertes ; automation active.

## Actualisation prioritaire — nouveaux théorèmes du 26 septembre

Lire en premier ../coupures_et_torsion/RAPPORT.md et ETAT_REPRISE.md. Les recherches anciennes qui laissaient passer treize classes mixtes A33 sont dépassées : quinze certificats entiers nouveaux et un cas humain excluent 388/400 directions, dont363/375mixtes. La dernière classe12 n’a aucune coordonnée nulle, donc r₀≤1. La formule C1 impose r₀=1,ρ=0,g⁻=20 : toute A33 à g⁻16/18 est exclue. A33 àg⁻20 reste ouvert. Tous les coefficients et un vérificateur indépendant sont sauvegardés.

Autre preuve humaine nouvelle, sansP=0 sous réduction plate stable : une coupure de deux blocs inutilisés ferme tous les supports norme10 à cinq blocs (plus généralement m6..11 exige six blocs). Norme10/six : trois profils (1,24,5,2),(2,21,8,1),(3,18,11,0), aucun t≥4, au plus une orbite sélectionnée entre les petits blocs. Six/sept ouverts. Norme9 entière ouverte.

Contrôles H(2,3)/BvLS positifs, calculs exacts distants, dépôts read-only, aucun solveur externe ou calcul lourd local. Recherche seul. Involution générale et branche sans symétrie non résolues ; poursuite ACTIVE.

## Actualisation prioritaire — 26 septembre, lecture GitHub et étoile libre

L'utilisateur a autorisé explicitement les dépôts GitHub amazing-source C1, C2 et structures, STRICTEMENT en lecture seule. Cette autorisation remplace les interdictions de lecture historiques ci-dessous. Aucun dépôt n'a été modifié. Recherche conduite seul ; calculs exacts distants sur SageMathCell, aucun solveur ni calcul lourd local ou fenêtre Python dans cette reprise.

Lire en priorité ../etoile_sans_classe_fermee/RAPPORT.md et ETAT_REPRISE.md ; ../normes_9_10/PREUVE_TRIANGLE_SELECTIONNE.md.

Les dépôts C1/structures établissent désormais g⁻ ∈ {16,18,20}. La cible ancienne g⁻=12 est dépassée par leurs nouveaux résultats ; cela ne démontre pas l'absence des normes9/10. Leur classification exhaustive des rangs n'a pas été réexécutée dans cette reprise.

Nouveau lemme humain sous la réduction plate stable : norme9/six blocs impose exactement un triangle sélectionné sur les trois gros blocs et six racines gros–petit, sans racine petit–petit. Sous P=0, deux classifications indépendantes donnent des listes identiques de noyaux nécessaires : 682,642,82 classes. Total1406. Programmes, données, résultats et empreintes dans ../normes_9_10/norm9_six_*. Ce sont des noyaux à33sommets ; aucune fermeture à99sommets.

La carte de Claude est corroborée avec une distinction : absence de classe fermée n'est pas synonyme d'étoile totalement libre (μ∩τ=∅). A33 exige une torsion équilibrée. Notre relaxation d'affectation+énergie sur17orbites ne ferme aucune torsion mixte nouvelle ; les treize restantes passent. (i)-(iii) complets restent ouverts. Les étoiles t=0/discriminant carré forcentg⁻=20 mais n'ont pas ce filtre de torsion.

Nouveaux contrôles de la formulation compacte : H(2,3) et BvLS passent exactement bijection/K2/K3 avec leurs paramètres. Programmes dans ../etoile_sans_classe_fermee/.

Ni involution exclue, ni involution⇒prisme, ni normes9/10 fermées, ni nouvelle exclusion du cas asymétrique. La poursuite recherche-conway-automorphismes demeure ACTIVE.


## Actualisation prioritaire : normes 9 et 10, capacité des blocs

26 septembre 2026. Recherche conduite seul, calculs à distance uniquement.

**Nouveau lemme humain, sans P=0 :** dans la réduction plate stable des vecteurs courts de L_T, chaque bloc a h<=2 aux normes carrées 9 et 10. Un bloc ne touche donc pas six représentants positifs. La preuve combine n_0=9-somme C(t-1,2) et la somme locale 2m-6h sur 12-2h orbites racines. Elle est dans ../normes_9_10/PREUVE_CAPACITE.md ; une seconde énumération entière confirme l'exclusion.

**Corollaires démontrés, sans P=0 :** norme9 utilise six ou sept blocs ; norme8 utilise les sept blocs. Cette dernière conclusion renforce et remplace par une preuve humaine la fermeture antérieure des 25 classes Wagner à six blocs. Norme9 à six blocs : trois orbites racines nulles en triangle sur les gros blocs ; six orbites t=2 exactement sur les paires bloc inutilisé/petit bloc.

**Deux moteurs exacts :** trois matrices B possibles à norme9, six à norme10. Les ensembles complets des types de blocs sont retrouvés indépendamment. **Deux placements norm9 à six blocs fermés à P=0**, par certificats entiers régénérés indépendamment : 19 termes/758 colonnes/rhs -4 et 91 termes/831 colonnes/rhs -792. Les copies sauvegardées ont les mêmes empreintes que les données vérifiées à distance. Les contrôles positifs H(2,3) et BvLS passent à nouveau.

Lire ../normes_9_10/RAPPORT.md et ../normes_9_10/ETAT_REPRISE.md. **Limite :** ni toute la norme9, ni toute la norme10, ni Wagner à sept blocs, ni g^-=12 ne sont fermés. La classification des noyaux six blocs n'est complète que pour le premier B, par un seul moteur ; une tranche de 220 classes ne couvre pas les 1344 classes de ce B. Aucun calcul n'est à poursuivre localement. Prochaine attaque : combiner le triangle des zéros et les six orbites t=2, et extraire une inégalité commune aux certificats. La poursuite programmée reste ACTIVE ; aucune cible finale n'est atteinte.

# État de reprise - 26 septembre 2026

## Actualisation : autorisation distante et famille Wagner à six blocs fermée

Cette actualisation prévaut sur les consignes d'exécution plus anciennes ci-dessous. L'utilisateur autorise désormais les solveurs **à distance**, mais demande de préserver son PC saturé. Ne lancer aucun calcul lourd local, même sans fenêtre ; les anciennes commandes de calcul local sont donc suspendues. Les restrictions de lecture restent inchangées : uniquement les fichiers produits ici et les dossiers fournis dans la conversation, aucun dépôt conway99-* ni document préexistant. Recherche conduite seul dans cette reprise.

**Résultat nouveau, vérifié indépendamment : à P=0, tout support Wagner de norme carrée 8 utilise les sept blocs.** Un lemme humain réduit les supports à six ou sept blocs. Les 25 classes à six blocs sont toutes exclues par des certificats entiers de Farkas sur les voisinages extérieurs nécessaires. Une seconde implémentation retrouve exactement les 25 classes, régénère leurs colonnes et vérifie tous les coefficients et seconds membres. Les calculs ont été exécutés sur SageMathCell. Les contrôles positifs m=2 et m=11 passent.

Lire [le rapport complet](../wagner_fermeture/RAPPORT.md), [l'état détaillé](../wagner_fermeture/ETAT_REPRISE.md), [les certificats](../wagner_fermeture/certificats_six_blocs.json) et [le vérificateur indépendant](../wagner_fermeture/verifier_famille.py). Les données sauvegardées ont la même empreinte canonique que celles vérifiées à distance : b91eb6f9e16267042cfe18fb93a826b6201a204e41ee120df73c5d38fe20ed41.

**Limite et prochaine cible :** 120 classes à sept blocs restent ouvertes. Un premier signal de certificat sur sept blocs n'est pas encore sauvegardé/vérifié indépendamment et n'est pas un résultat acquis. Normes 9 et 10 également ouvertes : même exclure toute norme 8 ne tuerait pas g^-=12. Aucune exclusion de l'involution, aucune preuve involution implique prisme, aucune nouvelle fermeture du cas sans symétrie. La poursuite programmée reste ACTIVE.

Le texte qui suit conserve les résultats et règles historiques. Son interdiction générale des solveurs est remplacée par l'autorisation distante ci-dessus ; ses pistes et limites restent valables sauf actualisation explicite.

## Verdict et règles

**Indécis :** ni l'existence/non-existence de srg(99,14,1,2), ni l'exclusion de C2, ni C2 ⇒ présence d'un prisme ne sont démontrées. L'ordre 1 désigne ici un groupe d'automorphismes trivial ; l'identité seule n'impose rien. C3 reste aussi un cas bibliographique possible.

Lire uniquement les fichiers créés dans cette conversation, notamment ce dossier. Ne lire aucun document préexistant du projet ni dépôt conway99-*, y compris sur le Web. Pas de SAT, CP, PLNE ou solveur externe. Mathématiques et calculs exacts écrits ici. Une exclusion d'un objet auxiliaire ne vaut pas exclusion du graphe. Les contrôles positifs m=2 et m=11 sont dans `audit/verifier_quotients.py` et `audit/quotients_verifies.json`.

La poursuite horaire du même fil est ACTIVE : `recherche-conway-automorphismes`. Ne pas la dupliquer. Elle n'est à suspendre qu'après une cible substantielle et une vérification indépendante, ou sur instruction de l'utilisateur.

## Cadre exact du cas C2

Une involution fixe un unique sommet x et échange ses sept paires de voisins. Les 42 orbites extérieures portent les racines e_i+e_j et e_i−e_j ; Z est leur matrice 7×42, R=|Z|. Le quotient est équivalent à :

    ZW=0, W²+W=12I−ZᵀZ,
    RU=4J−2R, U²+U=12I+4J−RᵀR,
    (U_pq,W_pq) ∈ {(0,0),(1,1),(1,−1),(2,0)}.

On a U=T+2M, T=|W| simple 10-régulier, M couplage parfait disjoint de T. P désigne le nombre de prismes, ne pas le confondre avec M. Sous P=0, M joint seulement des supports de racines disjoints, T ne joint pas deux racines de même support, et chaque étoile T[I_i] est C12 ou 2C6.

## Travail achevé : Schur et signes

**Vérifié exactement.** `phase2_racine/star_local_filter.py` (révision 2) : 441 types d'étoiles (362 C12, 79 2C6), tous survivent aux filtres sur une seule orbite. 13 230 domaines, 22 724 738 choix, tailles 990 à 2038. Lire `star_filter_results.json`, pas l'ancien fichier v1. La correction v2 impose aussi les contraintes HN des anciens sommets après l'ajout.

**Démontré et certifié indépendamment.** Une paire de colonnes autorisées séparément est impossible simultanément : mineur de Schur entier −5 549 359 104. Le graphe partiel passe toutes les bornes combinatoires testées et ne contient pas de prisme. Voir `phase2_algebre/coupe_conjointe.md`, `verify_paired_certificate.py`, `paired_certificate_verified.json` et l'audit de géométrie.

**Vérifié exactement, sans exclusion de famille.** Les quinze paires canoniques du type 0 : 16 842 648 couples, 9 987 300 passent combinatoire et absence de prisme, 7 879 824 passent Schur. Aucun des 31 794 choix individuels n'est supprimé. `phase2_algebre/paired_domains_all15.json`.

**Démontré.** Le relèvement W=T−2N fournit un système linéaire modulo 2 nécessaire aux équations modulo 4 ; il peut exclure un quotient unsigned étiqueté. Voir `phase2_audit/NOTE_ARITHMETIQUE.md`. Les contrôles m=2 et m=11 passent. Pour m=11, les 2^55 torsions de racines sont classifiées par deux éliminations indépendantes : seules 2^10 torsions de coupure passent et se relèvent exactement. Ceci ne construit aucun nouveau graphe et n'exclut pas m=7.

## Travail courant : différences binaires de deux signatures

Portée : une différence D de deux solutions du filtre de signes, pour un quotient complet hypothétique sous P=0, satisfait sur F2 :

    D=Dᵀ, diag D=0, support D ⊆ T,
    RD=0, TD+DT+D=0.

**Démontré, relu indépendamment.** Rang 2 impossible. Chaque ligne non nulle de D apparaît au plus trois fois. Au rang 4, D est un soufflage d'un sous-graphe de la grille 3×3, multiplicités 0..3. Voir `phase2_audit/UNICITE_RANG2_RANG4.md`. Attention : même exclure tout rang 4 ne prouverait pas l'unicité, encore moins P≥1.

**Vérifié exactement, deux implémentations/certificats.** 4^9 profils couverts par 4480 orbites ; 4270 de rang 4 ; 478 après bornes degré/voisins communs ; 19 après contraintes d'incidence et équations binaires. Certificats XOR indépendants pour les exclusions linéaires.

**Vérifié exactement par deux moteurs indépendants.** Les lignes de R sur le support actif de D doivent être dans ker D et induire un ensemble indépendant ou un C6. Sept lignes couvrent chaque colonne deux fois, intersection de deux lignes de taille ≤2. Les 19 profils se réduisent à :

| Code | Incidences (sept lignes non étiquetées, zéros permis) |
|---|---:|
| 8684 | 240 |
| 25768 | 192 |
| 43176 | 3744 |

Fichiers : `phase2_audit/rank4_root_covers.json`, `phase2_geometrie/rank4_all_incidence_covers_independent.json`. Une incidence sur les sommets actifs se complète à R seul en ajoutant 2−c_ij colonnes de type D=0 pour chaque paire de classes. Cela ne complète ni T, ni U, ni W.

**Vérifié exactement, audit indépendant terminé.** `phase2_algebre/rank4_integer_extensions.py` énumère les 4 567 248 solutions binaires des 19 espaces affines (max nullité 22), puis impose les bornes entières. Sur les trois profils à incidence possible : 8684 (8192 solutions) et 25768 (1024) sont rejetés ; 43176 garde 16 matrices T_s sur 32768. Un autre code 26147 passe T_s seul mais est déjà exclu par R. `verify_rank4_integer_extensions.py` a revérifié les trois profils pertinents par Gauss-Jordan et parcours Gray indépendants.

**Vérifié exactement, audit indépendant terminé.** `phase3_racine/cross_rank4.py` croise les 16 T_s et les 3744 R pour 43176 : 59 904 couples, 53 376 rejets par voisins communs, 6016 par capacité RT≤4−2R, **512 survivants à cette étape seulement**. Sortie `phase3_racine/cross_rank4.json`.

**Démontré avec réduction finie vérifiée indépendamment : rang 4 entièrement exclu.** Le profil 43176 est un doublement de C6 sur 12 sommets. Ses 30 autres sommets ont type D nul, donc leurs voisinages v appartiennent à ker D. Les capacités de voisins communs interdisent à tout v de rejoindre les six sommets du noyau de degré 6, alors qu'ils doivent atteindre le degré 10. Les 512 couples sont tous rejetés. Deux moteurs indépendants et une preuve combinatoire courte concordent : `phase2_geometrie/exclusion_double_C6.md`, `phase2_algebre/verify_rank4_zero_capacity.py`, `rank4_zero_capacity_verified.json`. Selon la faiblesse du filtre, il reste 5 ou 9 vecteurs v ; tous évitent le côté de degré 6. Ne pas affirmer « toujours 5 ».

**Limite décisive, à respecter.** Une différence non nulle D a désormais rang au moins 6. Rien ne force un tel D à exister. Même une preuve d'unicité des signes ne fermerait pas P=0 ou C2. Le candidat universel TQ+QT est non nul mais possède au moins huit arêtes hors T ; il n'est donc pas une différence de signatures. Cette borne a été auditée et ne constitue pas un pont vers P≥1. Voir `phase2_audit/LIMITE_UNICITE_ET_COMMUTATEUR.md`. Ne pas lancer les rangs 6/8 par inertie.

Les trois agents ont terminé leurs tâches et audits. Aucun calcul n'est encore actif au dernier enregistrement. La reprise programmée reste active. Le bilan détaillé de cette reprise est `phase3_racine/BILAN_PHASE3.md`.

## Priorité à la prochaine reprise : recherche collective d'une étoile

`phase3_racine/collective_star_search.py` est un moteur de retour arrière personnalisé, sans solveur. Il choisit simultanément les 30 colonnes X=W[I,J], V=U[I,J] d'une étoile de 12 orbites, sous C2 et P=0. Les contraintes sont : XXᵀ et VVᵀ exacts, HN via VR_Jᵀ et XZ_Jᵀ exacts, puis bornes de voisins communs et mineurs de Schur d'ordre deux entre colonnes. Toutes les coupures sont entières ; le flottant sert uniquement à ordonner les branches. Les formules ont été auditées par algèbre.

**Vérifié exactement : calibration.** m=2 et m=11 passent les quotas, avec les colonnes des graphes témoins connus et des colonnes nulles comme leurres. Ce n'est pas une découverte à l'aveugle du graphe à 243 sommets. Deux petits problèmes contrôlent aussi la reprise : un témoin trouvé en deux tranches, une impossibilité élémentaire par parité en trois tranches.

**Indécis :** seul le type d'étoile 0 est actuellement exploré, parmi 441. 282 quotas non nuls ; 31 794 choix initiaux. Le parcours avec CN et Schur possède un point de reprise dans `phase3_racine/collective_star_search_joint.json`. Après deux tranches de 45 secondes : 67 042 appels cumulés, dont 12 revisites de préfixe ; profondeur maximale 15/30 avant une éventuelle coupure ; aucune solution, aucun arbre épuisé. Les statistiques du dernier segment sont 34 981 appels, 23 272 coupes maximum de quota, 6030 minimum, 1880 domaines vides, 1013 domaines rendus vides par les bornes de quota ; 176 branches supplémentaires coupées par compatibilité de paires.

Pour continuer sans répéter les branches terminées, depuis le répertoire de travail :

    & 'C:\Users\RESEARCHER\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'outputs/automorphismes_1_2/phase3_racine/collective_star_search.py' --seconds 45 --nodes 100000 --joint --resume 'outputs/automorphismes_1_2/phase3_racine/collective_star_search_joint.json'

Le JSON est remplacé par le nouveau point de reprise et conserve le nombre cumulé d'appels. La reprise vérifie l'empreinte des domaines et l'ordre des choix du préfixe. Si les règles de branchement changent, ne pas réutiliser aveuglément un ancien point de reprise. Avant toute conclusion d'impossibilité, il faudra un second moteur ou un certificat indépendant de cette recherche.

Progrès utile attendu : réduire une famille entière de choix, renforcer les contraintes simultanées (par exemple Schur d'ordre ≥3) ou trouver une réalisation complète des colonnes et tester son prolongement. Ne pas lancer des reprises identiques pendant des heures sans mesurer si une branche de premier niveau se ferme. Même un succès aux quotas laisse à choisir les adjacences entre les 30 orbites extérieures, et le type 0 n'est qu'un type parmi 441.

## Cas asymétrique : statut conservé

`phase2_geometrie/reflexions_globales.md` contient des identités démontrées sur les réflexions canoniques t_x, notamment 6P+4Σo_x+Σd_x=8316 et une borne spectrale sur le défaut de commutation. Elles admettent des valeurs scalaires formellement compatibles avec P≤1151 ; aucune exclusion. Ne pas présenter ces comptes comme forçant une involution.

## Exécution

Python : `C:/home/researcher/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`.
Répertoire de travail : `C:/home/researcher/Documents/Codex/2026-09-25/brief-astra-n-1-attaque-ind`.
Les sorties sont UTF-8 ; l'affichage PowerShell peut altérer visuellement les accents sans corruption du fichier.


---

# Pièce : EXCLUSION_FRAME_D8_TROIS.md

SHA256 : 4d629388b8832bba4a47c5e9bdd2020d773b4e4ae9c9027144d5fe98efa5fb09

# Une famille unimodulaire24 exclue par le repere physique49

**Statut : preuve directe et controle exact independant.** Le reseau U construit ci-dessous existe. Ce qui est impossible est d'y placer le repere physique complet 42+7, avec ses deux normales orthogonales de norme7. Le resultat vaut pour g18 et g20, sans P0. Il ne classe pas tous les reseaux unimodulaires24.

## 1. Reseau, glue et sous-reseau entier

Dans R^8 poser D8={x entier : somme x_i paire}, s=(1/2,...,1/2), v=e_1. Le discriminant D8*/D8 a quatre classes 0,s,v,c=s+v. Leurs minima sont respectivement 0,2,1,2. Les classes s et c sont demi-entieres, avec respectivement un nombre pair et impair de signes moins dans leurs vecteurs minimaux.

Dans D8^3 ajouter les trois classes

    a=(s,s,0), b=(0,s,s), t=(v,v,v).

Elles engendrent huit classes :

    000, ss0, 0ss, s0s, vvv, ccv, vcc, cvc.

Leurs couts minimaux sont 0,4,4,4,3,5,5,5. Les produits a^2=b^2=4, t^2=3, a.b=2 et a.t=b.t=1 sont entiers. Le reseau U ainsi obtenu est donc integral impair ; son indice8 dans D8^3 et det(D8^3)=64 donnent det U=1.

Le sous-reseau U_Z des vecteurs dont toutes les coordonnees sont entieres contient exactement les classes000 et vvv. Ainsi [U:U_Z]=4.

## 2. Coques et caracteristiques explicites

La coque de norme3 est exactement la classe vvv minimale : dans chaque composante, une unite +/-e_i. Elle comporte16^3=4096 vecteurs, tous entiers.

Un vecteur non entier de norme4 appartient necessairement a ss0, 0ss ou s0s et est minimal dans ses deux composantes spinor. Il a deux blocs de huit coordonnees +/-1/2, chacun avec un nombre pair de signes moins.

Pour chacune des trois composantes et chaque choix de huit signes +/-1 avec un nombre pair de signes moins, le vecteur chi forme de ces huit signes et nul ailleurs est caracteristique de U, et chi^2=8. En effet ses produits sur les racines de D8 sont pairs, ses produits sur a et b sont pairs puisque (s,chi)=4-n_minus est pair, et son produit sur t est impair. Cela verifie la parite sur tous les generateurs de U.

Si h est un vecteur non entier de norme4, choisir une composante spinor de h et prendre chi avec les memes signes sur cette composante. Le nombre de signes moins est pair, et (chi,h)=4.

## 3. Le repere interdit les sept blocs demi-entiers

Supposons que U contienne le repere physique de quarante-deux u_o de norme3, sept h_c de norme4 et deux y_i de norme7. Les deux y sont orthogonaux entre eux et au span22 du repere. L'identite tight-frame est

    somme_o u_o u_o^t + somme_c h_c h_c^t + y_1 y_1^t + y_2 y_2^t =7 I_24.

Pour toute caracteristique chi de norme8, elle donne

    56 = somme_o(chi,u_o)^2 + somme_c(chi,h_c)^2
           + (chi,y_1)^2 + (chi,y_2)^2.

Les quarante-deux premiers produits et les deux derniers sont impairs, donc coutent au moins42+2. Un h demi-entier fournit une caracteristique explicite avec produit4, et ajouterait16 : 60>56. Tous les sept h sont donc entiers. Cette etape ne suppose pas vingt-quatre caracteristiques orthogonales.

## 4. L'identite diagonale rend les normales entieres

Les u et h sont entiers. Dans chaque coordonnee j, l'identite diagonale impose y_1j^2+y_2j^2 entier. Or U est contenu dans (1/2 Z)^24. Un carre demi-entier vaut1/4 modulo1 ; avec une ou deux coordonnees demi-entieres, la somme des deux carres vaut1/4 ou1/2 modulo1. Aucun de ces cas n'est entier. Les deux y sont donc eux aussi entiers.

Le reseau N engendre par les u et h, plus J=<y_1,y_2>, est ainsi contenu dans U_Z. Mais

    [U:N orthogonal J] =sqrt(det N * det J)
                      =7^((24-g)/2),

soit49 en g20 ou343 en g18. Cet indice impair devrait etre divisible par [U:U_Z]=4, contradiction.

## 5. Portee et controle

La conclusion exclut uniformement cette famille D8^3/glue pour le repere physique49, et uniquement cette famille. Elle ne dit pas qu'U n'existe pas, que toutes les extensions sont de cette forme, ni que g18/g20 soit globalement ferme.

Le source verifier_frame_D8_trois.mjs regenere les huit classes, leurs produits,384 caracteristiques explicites et tous les signes spinor d'une composante. Il recalcule les coques3 et4, le residu des carres demi-entiers et les indices49/343. Aucun catalogue local ni solveur n'est utilise. H(2,3)/BvLS gardent leurs parametres propres ; ils ne sont pas places artificiellement dans ce collage24.


---

# Pièce : G18_G20_D6_MIXTE_CENTRES_REPETES.md

SHA256 : 56b8fc1e58480b059e154db723a8fb699be7927a74b80d9de5f432c81e44b61e

# D6^4 : centres distincts dans un regime mixte4+2

## Hypotheses exactes

On garde le repere physique de G18_G20_D6_SIX_SPINORS.md : U est le cycle-glue integral unimodulaire de racines D6^4, les42 u, les sept h et les deux normales y sont les MEMES vecteurs du frame7I24 ; J=7I2 est primitif et min(N*) >=8/7. Aucun P0 n'est utilise.

Cette piece suppose quatre h de typeIII spinoriels sur A,C, deux h de typeIII spinoriels sur B,D, et le septieme h de typeI ENTIER, quatre unites dans A ouC. La conclusion est : les QUATRE centres des premiers h doivent etre distincts, DEUX dans B et DEUX dans D. La strate mixte entiere n'est pas exclue. Le cas du septieme h de typeII n'est pas couvert. Une permutation cyclique donne la version symetrique.

## La trace puis les diagonales utilisent les deux normales communes

La contribution du frame sur A,C, en trace, est :63 pour les42 u, 12 pour les quatre h spinoriels A,C, 2 pour les deux centres des h spinoriels B,D, et4 pour le h entier. Le total est81, alors que7I sur ces douze dimensions a trace84. Les deux normales y contribuent donc EXACTEMENT3.

Chaque normale de norme7 a un spinor sur une composante A/C et un sur une composante B/D. Sa contribution minimale sur A,C est3/2. Les deux contributions sont ainsi toutes deux minimales : chaque normale a six coordonnees de valeur absolue1/2 dans une composante A/C, et aucune coordonnee dans l'autre. Il n'y a aucun exces normal sur A,C.

Les diagonales A,C ont ensuite une couverture entiere constante, de somme1 entre les deux composantes. Les quatre unites du h entier et les deux centres des h B,D couvrent ainsi exactement les SIX axes d'une seule composante A/C, une fois chacun. Ce fait est une consequence ; on ne choisit pas ces centres separement selon une normale.

Sur B,D, les contributions de base par coordonnees sont celles des42 incidences spinorielles des u, des quatre incidences des deux h spinoriels B,D, et des deux incidences normales. Leur somme est

    (42+4+2)/4 =12.

Il reste exactement2 dans la somme de deux diagonales opposees. Noter t_B,t_D les couvertures entieres constantes (centres des quatre h A,C et exces des normales). Alors

    t_B,t_D sont entiers >=0 ; t_B+t_D=2.            (1)

Pour chaque axe, m_B(x)<=t_B et m_D(z)<=t_D, ou m compte les quatre centres.

## Tout centre repete force trois axes normaux communs

Une multiplicite>=3 est directement incompatible avec(1). Si un centre double est dans B, il force t_B=2,t_D=0. Tous les quatre centres sont alors dans B, et aucun exces normal n'est possible dans D.

Les profils normaux deviennent tres simples. Leurs spinors sur A/C sont deja minimaux. Une demi-coordonnee3/2 dans B avec des unites D violerait la borne caracteristique max|y_B|+max|y_D|<=3/2. Deux demi-coordonnees3/2 dans B violeraient la borne root commune

    (alpha,y1)^2+(alpha,y2)^2 <=6

pour la root sur ces deux axes. Aucun exces D n'est permis. Chaque normale est donc minimale demi-entiere sur D, avec QUATRE unites dans B. Une coordonnee unique2 est aussi interdite par la borne caracteristique ; les glues de trois aretes exigeraient une unite A/C et sont exclues par la trace precedente.

La diagonale B donne exactement

    1_[x unite de y1] + 1_[x unite de y2] =2-m_B(x).   (2)

Les quatre centres ont les profils2+2 ou2+1+1. Il y a donc au moins TROIS axes B non centres. Sur chacun, le membre droit de(2) vaut2 ; les deux normales portent toutes deux une unite. Parmi trois ratios de signes +/-1, deux sont egaux. La root alpha sur ces deux axes a alors produit absolu2 avec chacune des normales. La somme de ses carres vaut8, contre la borne6. Le cas d'un centre double dans D est symetrique.

Toute repetition est exclue ; les quatre centres doivent etre distincts.

## Les quatre centres doivent se partager deux par composante

Ecrire b1,b2 les deux vecteurs spinoriels des h B,D sur B, et d1,d2 ceux sur D. Leurs coordonnees ont valeur absolue1/2. Noter

    sigma_i=b2_i/b1_i, tau_j=d2_j/d1_j, dans{+1,-1}.

Les centres deja prouves distincts donnent m_B(i),m_D(j) dans{0,1}. Pour chaque paire d'axes, les deux orientations des caracteristiques chi_BD recoivent r et2-r contributions actives des deux h spinoriels B,D. Avec les centres des quatre autres h, les nombres actifs sont m_B+m_D+r et m_B+m_D+2-r. Tous deux doivent etre1 ou3. Si m_B+m_D est0 ou2, les deux spinors doivent etre actifs dans des orientations opposees ; si cette somme est1, leurs orientations doivent coincider. Ceci equivaut exactement a

    sigma_i*tau_j = -(-1)^(m_B(i)+m_D(j)).

Il existe donc un signe epsilon commun tel que

    sigma_i=epsilon*(-1)^m_B(i),
    tau_j=-epsilon*(-1)^m_D(j).

Si b centres se trouvent dans B et d=4-b dans D, le produit des deux parties spinorielles vaut

    (b1,b2)+(d1,d2)
       =epsilon*((6-2b)-(6-2d))/4
       =epsilon*(2-b).

Leurs centres sur A/C sont distincts, comme prouve par la diagonale ; ils ont produit0. L'orthogonalite des deux h impose donc b=2 et d=2. Ce corollaire couple les memes deux h dans les36 paires d'axes ; il ne choisit pas leurs signes separement pour chaque caracteristique.

## Controle exact et limite

Le source joint regenere les1365 distributions de quatre centres sur douze axes ;870 ont une repetition. Les diagonales(1) en laissent150 contextes repetes, exactement les profils2+2 et2+1+1 sur une seule composante. Il enumere les270 paires ORDONNEES de supports unitaires normaux couvrant(2), autorisant toutes les parites et tous les signes. Chaque paire partage au moins trois axes, donc zero passe la borne root necessaire. Il controle aussi les64 cas de signes locaux du corollaire, puis les cinq profils b=0..4 avec les deux signes epsilon : seul le partage2+2 est orthogonal.

Ce controle est une relaxation : il n'affirme aucune completion SRG des centres distincts qui restent. Il confirme seulement la couverture de la sous-famille refutee, sans solveur, sans catalogue local et sans extension aux autres profils de h7.


---

# Pièce : G18_G20_D6_QUATRE.md

SHA256 : 93699a1ee744fe70fa155e1f7cd2821f6f253aebdcbe097ecbef296206c3bfea

# D6^4 : coque complete et classification des blocs de norme4

## Un modele global rootful, pas un graphe

Dans quatre espaces orthogonaux R^6 indices par i=0,1,2,3, prendre Q=D6^4. Chaque D6 a determinant4 et trois classes non nulles dans son discriminant : v de minimum1, et s,c de minimum3/2. Les classes s et c forment une base de F2^2, avec 2b(s,s)=2b(c,c)=1 et2b(s,c)=0.

Choisir s_i=(1/2,...,1/2) et c_i=(-1/2,1/2,...,1/2) dans la composante i. Definir

    g_i=c_i+s_(i+1 modulo4),
    U=Q+sum_i Z g_i.

Les quatre glues ont produits entiers et classes independantes. Leur groupe a ordre16 ; U est donc integral unimodulaire de rang24, det(U)=4^4/16^2=1. La norme minimale de chaque classe s'obtient par addition des minima des quatre composantes :

| Sous-ensemble des quatre glues | Nombre | Minimum |
|---|---:|---:|
| Vide | 1 | 0 |
| Une arete | 4 | 3 |
| Deux aretes adjacentes | 4 | 4 |
| Deux aretes opposees | 2 | 6 |
| Trois aretes | 4 | 5 |
| Quatre aretes | 1 | 4 |

Il n'y a pas de norme1, ni de racine supplementaire dans une classe non nulle. Le systeme de racines est exactement D6^4. Les normes3 sont les quatre cosets d'une seule arete : deux spinors de minimum3/2, chacun avec32 signes de la parite prescrite. Il y a4*32^2=4096 normes3.

## La coque3 engendre U

Fixer une de ces familles et changer deux signes dans son spinor d'une composante. La difference de deux normes3 donne un vecteur +/-e_a+/-e_b de D6. Ces differences engendrent le D6 de chaque composante. Les quatre baselines g_i sont elles-memes de norme3 et ajoutent les quatre classes independantes. Ainsi la coque3 engendre U integralement.

Son Gram modulo2 a donc rang24, puisque U est unimodulaire. Le source joint donne64 normes3 explicites qui suffisent deja, et controle le rang24 modulo2. Cela REFUTE la borne generale 'coque3 de rang modulo2 au plus20 dans les collages rootful restant apres E8/D12'. Ce modele ne porte pas de frame49 construit ; ni sept blocs physiques, ni dix voisins par racine, ni budgets SRG ne sont annonces.

Le glue, le minimum, la coque et sa generation ont ete relus independamment par g18_audit_neuf.

## Caracteristiques de norme8

L'integralite des produits caracteristiques avec toutes les roots D6 impose que, dans chaque composante, les six coordonnees soient entieres et de meme parite. Une composante impaire coute au moins6 ; une coordonnee non nulle dans les composantes paires coute au moins4. Une caracteristique de norme8 ne peut donc contenir de composante impaire.

Elle est de la forme2(+/-e_a +/-e_b). La condition caracteristique sur les glues g_i de norme impaire exige t_i+t_(i+1)=1 modulo2, ou t_i indique la composante de chaque coordonnee2. Ses deux coordonnees se trouvent donc dans deux composantes OPPOSEES du cycle. Il y a

    2 * 6^2 * 4 =288

caracteristiques de norme8, toutes explicites. Chaque norme3 de la coque est plate pour elles : son produit est toujours+1 ou-1, puisque une arete du cycle rencontre exactement une des deux composantes opposees.

## Les deux inegalites necessaires pour chaque h physique

Supposons maintenant un vrai frame49 dans U, avec les42 u de norme3, sept h de norme4, et deux normales y de norme7. Pour une caracteristique chi de norme8, le frame entier de constante7 donne

    sum_u (u,chi)^2 + sum_h (h,chi)^2 + sum_y (y,chi)^2 =56.

Les42 premiers termes valent42. Les deux normales ont norme impaire, donc leurs produits caracteristiques sont impairs et contribuent au moins2. Aucun h ne peut alors avoir produit absolu4 : son seul carre16 donnerait deja60>56. Les produits avec les h sont pairs, donc de valeur absolue au plus2.

Pour les composantes opposees A,C et B,D, ceci equivaut exactement a

    max_a |h_A,a| + max_c |h_C,c| <=1,
    max_b |h_B,b| + max_d |h_D,d| <=1.                  (1)

## Classification COMPLETE des normes4 passant(1)

Trois types restent. Les signes sont ceux du coset indique, et toutes les permutations permises dans les composantes sont admises.

| Type | Coordonnees non nulles | Classe de glue | Nombre de vecteurs |
|---|---|---|---:|
| I | Quatre unites +/-1 dans UNE composante D6 | 0 | 960 |
| II | Deux unites dans chacune de DEUX composantes ADJACENTES | 0 | 14400 |
| III | Spinors minimaux sur deux composantes opposees, une unite dans une composante intermediaire | Deux aretes adjacentes | 49152 |

Preuve d'exhaustivite : une classe non entiere de norme4 doit etre l'une des quatre classes de deux aretes adjacentes, car les autres ont minimum>4 ou parite impaire. Sa norme4 est deja son minimum3/2+1+3/2, donc elle est exactement du typeIII.

Une norme4 entiere est soit une seule coordonnee+/-2, soit quatre unites. La coordonnee2 viole(1). Dans la classe0, la parite paire des sommes D6 impose le profil4 dans une composante ou2+2. Deux composantes opposees violent(1), deux adjacentes donnent le typeII. La seule autre classe entiere est v dans les quatre composantes ; ses quatre unites, une par composante, violent(1). Le typeI passe(1).

Les comptes sont4*C(6,4)*2^4=960 ;4*C(6,2)^2*2^4=14400 ;4*32^2*12=49152. La coque de candidats h individuels a donc64512 vecteurs. Ce ne sont pas64512 blocs d'un frame valide ; ils doivent encore etre selectionnes SEPT ENSEMBLE, orthogonaux, dans le meme frame avec42 u et deux normales.

## Deux contraintes collectives encore necessaires

Les normales ont leurs demi-coordonnees dans deux composantes adjacentes : seules les classes d'une ou de trois aretes ont parite impaire et peuvent porter une norme7. Si f_A compte les h fractionnaires dont les spinors occupent A,C, et f_B ceux occupant B,D, alors f_A et f_B sont pairs. En effet, sur une coordonnee d'une composante i, la diagonale du frame modulo1 compte(1/4)(n_i+f_i+m_i), ou n_i est le nombre de u incident, et m_i le nombre des deux normales fractionnaires dans i. Pour deux composantes opposees, n_i+n_j=42, m_i+m_j=2 et f_i=f_j, donc44+2f_i est divisible par4. Ainsi il y a0,2,4 ou6 h fractionnaires parmi les sept.

Cette parite peut aussi se retrouver depuis la primitive des sept blocs ; elle n'est pas annoncee comme independante si cette primitive est deja imposee. Elle ne ferme pas la selection septuple.

Une autre borne utile pour les normales vient du minimum dual : pour toute root alpha de U, sa projection sur N est non nulle (sinon alpha serait dans le primitif7I2, de minimum7). Elle appartient a N*, donc

    (alpha,y_1)^2+(alpha,y_2)^2 <=6.

Le membre gauche est un entier, puisque y_i appartient a U ; la borne exacte avant arrondi est14-8=6. Aucun produit absolu3 avec une root n'est possible. Cette coupe concerne les deux normales COMMUNES ; elle ne les choisit pas separement selon les sept h.

## Statut

Le modele de coque et la classification des candidats h sont demontres. L'existence ou l'impossibilite de SEPT h de ces types, orthogonaux et completant le frame physique avec ses42 u et ses deux normales, reste OUVERTE dans cette note. Aucune exclusion globale g18/g20, ni aucun graphe, n'est revendiquee.


---

# Pièce : G18_G20_D6_SIX_SPINORS.md

SHA256 : d1e8a5c45e42482e5fae1d6f52cb28c59dc561913a69b7fb542d49ab4cade0cc

# Coupe uniforme des six blocs spinoriels dans D6^4

## Portee et hypotheses

On travaille dans le collage integral unimodulaire U de racines D6^4, avec glues c_i+s_(i+1) sur un cycle A-B-C-D. On suppose le MEME repere physique : 42 vecteurs u de norme3, sept h mutuellement orthogonaux de norme4, et deux normales y1,y2 orthogonales de norme7. Leur frame complet vaut7I24. Le sous-reseau N engendre par les49 vecteurs satisfait N_R=J_R^perp, ou J=7I2 est primitif dans U, et min(N*) >=8/7. N lui-meme n'est pas suppose primitif dans U. Aucun choix local independant de normale n'est admis.

La conclusion est seulement : parmi les sept h, SIX ne peuvent pas etre de typeIII avec spinors sur la meme paire opposee A,C. Le regime symetrique B,D est aussi ferme. Cela n'exclut pas D6^4, un type local, g18 ou g20.

Les ingredients acquis sont repris dans G18_G20_D6_QUATRE.md : les288 caracteristiques de norme8 sont2(+/-e_A +/-e_C) ou2(+/-e_B +/-e_D) ; chaque u est plat pour chacune ; les h sont plats aussi. Les h de norme4 sont donc les typesI,II,III de cette note. Les demi-coordonnees d'une normale de norme7 occupent deux composantes adjacentes.

## Borne commune des deux normales

Pour toute root alpha de U, proj_N(alpha) est non nulle : autrement alpha appartiendrait au J primitif, dont le minimum est7. Cette projection est dans N*. Comme alpha^2=2,

    (alpha,y1)^2+(alpha,y2)^2 <= 14-8 =6.          (R)

Les produits sont entiers. En particulier, une normale n'a pas de produit absolu3 avec une root.

Pour une caracteristique chi de norme8, les42 u contribuent42 au frame. Les produits des deux normales avec chi sont impairs, et chaque h actif contribue4. Si k h sont actifs,

    4k+(y1,chi)^2+(y2,chi)^2 =14.                (C)

Les deux produits normaux sont impairs, de valeur absolue1 ou3. La somme de leurs carres ne peut etre que2 ou10 (18 est trop grand). Il suit exactement

    k=1 ou k=3.

Pour k=3, les DEUX normales sont plates pour chi. Une normale lourde de produit absolu3 est possible seulement pour k=1. Cette conclusion vaut pour les144 paires de caracteristiques, simultanement pour le meme frame ; elle ne suppose pas24 ombres orthogonales.

## La diagonale force le septieme h et les profils normaux

Supposons six h de typeIII ayant leurs spinors sur A,C. Chacun a un centre unitaire dans B ouD. Les42 u ont au total42 incidences spinorielles sur A,C ; les six h en ont12 ; les deux normales en ont2. La somme des contributions de base, sur une coordonnee quelconque de A et une quelconque de C, est donc

    (42+12+2)/4 =14.

La diagonale totale est exactement7+7=14. Tous les exces, positifs, sont donc nuls sur A,C. Le septieme h ne peut avoir aucune coordonnee dans A,C. La classification des h plats impose qu'il soit de typeI : quatre unites dans B ouD. Echanger B etD permet de fixer ces quatre unites dans B. L'orthogonalite interdit a chacun des six centres d'occuper leur support.

Les normales n'ont aucune unite ni demi-coordonnee lourde sur A,C. Dans B,D, leur norme restante peut a priori etre faite de quatre unites, d'une demi-coordonnee3/2 et de deux unites, ou de deux demi-coordonnees3/2. Le second profil viole max|y_B|+max|y_D|<=3/2, qui suit de (C). Le troisieme donne un produit absolu3 avec une root D6, interdit par (R). Les classes de trois glues exigeraient une unite dans A ouC, deja exclue.

Ainsi chaque normale a deux spinors MINIMAUX sur une arete du cycle et exactement quatre unites dans l'autre composante B/D. Elle est soit demi-entiere sur B avec quatre unites dans D, soit demi-entiere sur D avec quatre unites dans B.

## Six centres contre les deux normales communes

Noter m_B(x),m_D(z) les multiplicites des centres sur les deux composantes. Poser

    t_B(x)=m_B(x)+1_[x dans supp(h7)],
    t_D(z)=m_D(z).

Pour chi=2(+/-e_B,x +/-e_D,z), le nombre de h actifs est k=t_B(x)+t_D(z), quelle que soit l'orientation des deux signes. Il est exactement1 ou3.

Les quatre coordonnees du support de h7 ont t_B=1. Il suit m_D(z) dans{0,2} pour les SIX coordonnees D. Les deux autres coordonnees B ont t_B=m_B dans{1,3}. Les six centres se partagent donc ainsi :

* deux centres simples B et deux centres doubles D ;
* deux centres triples B et aucun centre D.

Le partage intermediaire1+3 sur B laisserait un centre double D ; leur paire donnerait k=5. Les deux partages affiches sont ainsi exhaustifs, sans aucun calcul spectral.

Une normale demi-entiere sur B a des valeurs absolues1/2 sur SES SIX coordonnees B. Une unite de cette normale en D donne un produit absolu3 pour l'une des deux orientations de chi. Par (C), ses quatre unites D doivent donc toutes satisfaire k=1 pour CHAQUE coordonnee B, soit

    max(t_B)+m_D(z) <=1.                         (1)

Symetriquement, les quatre unites B d'une normale demi-entiere sur D doivent satisfaire

    t_B(x)+max(m_D) <=1.                         (2)

Dans le premier partage, max(m_D)=2 et (2) interdit toute normale demi-entiere sur D. Les deux normales sont donc demi-entieres sur B. Leurs quatre unites D sont necessairement le MEME complement des deux centres doubles.

Dans le second partage, max(t_B)=3 et (1) interdit toute normale demi-entiere sur B. Les deux normales sont demi-entieres sur D. Leurs quatre unites B sont necessairement le MEME support de h7 : sur les deux autres coordonnees, t_B=3 interdit (2).

Dans les deux cas, les quatre coordonnees unitaires communes portent deux listes de signes. Parmi quatre ratios +/-1, deux sont egaux. La root alpha=e_i+epsilon e_j correspondant a ces deux axes a produit absolu2 avec CHACUNE des normales. Ainsi

    (alpha,y1)^2+(alpha,y2)^2 =8,

en contradiction avec (R). Le regime six spinors sur A,C est impossible.

## Controle fini et statut

G18_G20_D6_SIX_SPINORS.mjs controle les1716 distributions des six centres sur les deux positions B autorisees et les six positions D. Il retrouve16 distributions satisfaisant exactement k dans{1,3} : quinze choix des deux centres doubles D et le choix3+3 dans B. Son test d'exclusion travaille meme sur une relaxation plus large : il conserve seulement k<=3, (1),(2), puis la necessite de ne pas partager trois unites entre les normales. Il relaxe les parites de glue et tous les signes, et autorise meme la repetition de leur support. Zero paire survit. Un controle separe des256 paires de signes sur quatre axes retrouve chaque fois une root-temoin de (R).

Cette verification ne remplace pas les lemmes physiques du frame ; elle controle le dernier argument combinatoire fini. La coupe concerne les six blocs simultanes et les deux normales du meme collage. Les regimes quatre-plus-deux ou moins de blocs spinoriels restent ouverts ici.


---

# Pièce : G18_G20_DUAL_COORDONNEES.md

SHA256 : 4956adbbdd388ad3fb5845cccbe52a2282d4778bd48541d6fe745cbc21253583

# Axes courts duaux : coupe de coque et fermeture D11 en rang24

## Lemme commun de trois directions

Les42 generateurs de norme3 engendrent integralement le reseau physique N ; voir [G18_G20_QUARANTE_DEUX_GENERATEURS.md](G18_G20_QUARANTE_DEUX_GENERATEURS.md). On garde la borne duale acquise min(N*)>=8/7. Si w est un vecteur reel de norme<=1 dont les produits avec ces42 vecteurs sont ENTIERS, alors proj_N(w) appartient a N* et a norme<=1. Cette projection est donc nulle.

Dans une extension de dimension<=24, trois tels w lineairement independants sont impossibles, car ils seraient contenus dans N^perp, de dimension<=2. Cela ne suppose pas que w appartient au reseau ambiant.

La forme globale du piege de coque est immediate : si toute la coque3 d'un reseau ambiant appartient aux coordonnees entieres d'un repere orthonormal, ses axes ont produits entiers avec toute selection des42 u. Les24 axes seraient orthogonaux a N. Cette enveloppe ne peut donc porter le frame physique. D8^3, dont la coque3 est composee de triples unites entieres, est une famille fermee par ce principe, sans les caracteristiques8 ni les normales.

## Une seule composante D4 uniforme en classe suffit

Pour D4, les trois classes minuscules v,s,c de norme1 sont chacune composees de quatre paires d'axes orthonormaux. Elles peuvent se realiser par les axes standards, ou par les lignes d'un Hadamard4 divise par2, avec la parite voulue.

Si les projections des42 u sur UNE composante D4 appartiennent a0 et une seule de ces classes, choisir ses quatre axes. Leurs produits avec tous les u sont entiers. Le lemme les rend orthogonaux a N, impossible en codimension<=2. Les projections de classe0, lorsqu'elles sont considerees, restent aussi entieres apres trialite.

Donc chaque composante D4 d'un collage candidat doit utiliser au moins DEUX classes parmi les42 vecteurs effectivement selectionnes. Un melange dans la coque ambiante complete ne suffit pas : il faut le garder dans la selection physique. Cette coupe ne ferme pas tous les D4^6 ; une enveloppe D4^6 avec plusieurs classes reste possible.

## Nouvelle fermeture D11 dans toute extension integrale de dimension<=24

Soit E l'espace d'un D11 de roots du collage L. Les projections des42 u sont0,+/-e_i ou des spinors de norme11/4 : le lemme minuscule acquis donne cette liste.

Si aucune projection n'est spinorielle, les onze axes e_i ont produits entiers avec les42 u. Ils seraient tous dans N^perp, contradiction. Il existe donc u=p+b, p dans E un spinor, b dans E^perp, avec

    p^2=11/4, b^2=1/4.

On a4p dans D11, donc4b=4u-4p appartient a L. Poser e12=2b comme AXE EUCLIDIEN de norme1 ; il n'est pas suppose appartenir a L. Les onze coordonnees de2p valent+/-1. Pour chaque i, le vecteur2p-e_i a somme entiere paire et appartient a D11. Alors

    2u-(2p-e_i)=e_i+e12

est une root de norme2 de L. Lui soustraire4b=2e12 donne aussi e_i-e12 dans L. Avec les roots D11, ces roots engendrent le D12 standard dans l'espace E plus Rb.

Mais D12 dans un collage de dimension<=24 portant le frame est DEJA exclu par la preuve0803, [G18_G20_D12_COLLAGE.md](../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md). Contradiction. Ainsi aucun D11 ne peut figurer non plus : tous les D_n de rang n>=11 sont fermes dans ces extensions de rang<=24.

Ce raccord a ete relu independamment par g18_audit_neuf. Il ne suppose ni que2b est un vecteur du reseau, ni que L est indecomposable, ni que D11 est contenu dans N. Il n'exclut pas D10 ni toutes les racines mixtes, et ne ferme pas les genres g18/g20.


---

# Pièce : G18_G20_QUARANTE_DEUX_GENERATEURS.md

SHA256 : e6a5cd6936692031d14ecf566cccb71445bcf3095fa6e6c417c6b750e6d12421

# Les42 generateurs de norme3 engendrent le reseau physique entier

## Hypotheses communes

N est le reseau physique engendre integralement par les sept h_c de norme4 et les42 u_p de norme3 du meme Gram

    H=[4I_7,-C ; -C^t,3I_42-T].

Les colonnes de C sont les42 directions D7, deux soeurs par support {c,d}. On garde

    CC^t=12I_7, CT=0, T^2+T=12I_42-C^tC,
    3h_c+sum_p C_cp u_p=0.

Poser Gamma=<u_1,...,u_42>_Z. Le resultat est Gamma=N, pas seulement span_R(Gamma)=span_R(N). Il n'utilise ni P0, ni choix local W, ni determinant49.

## Une formule entiere pour chaque bloc

Noter U(v)=sum_p v_p u_p et h(a)=sum_c a_c h_c. L'identite matricielle

    (3I-T)(T+4I)=C^tC

et CT=0 montrent que

    U((T+4I)v)=-h(Cv)                                      (1)

pour tout v reel : le vecteur de gauche plus h(Cv) a produit nul avec tous les h et tous les u. Ils engendrent l'espace reel entier, donc ce vecteur est nul.

Pour un bloc c, choisir un autre bloc d. Orienter les deux colonnes soeurs comme C_+=e_c+e_d et C_-=e_c-e_d. Si une colonne avait l'autre orientation, on change simplement le signe de son coefficient dans v. Prendre v=e_++e_-, de sorte que Cv=2e_c. La formule(1) donne U((T+4I)v)=-2h_c, tandis que U(C_c^t)=-3h_c. Par difference,

    h_c=U((T+4I)v-C_c^t).                                 (2)

Tous les coefficients de(2) sont ENTIERS. Ainsi chaque h_c appartient a Gamma, et Gamma=N.

## Consequence pour une selection commune dans une enveloppe

Dans le cadre g20, les42 u doivent engendrer exactement Nmax. Dans le cadre g18, ils doivent engendrer le reseau physique N d'indice7 dans Nmax. Les remplacer par42 vecteurs independants seulement au sens reel oublie une condition necessaire. Inversement, verifier le seul indice ne prouve pas les incidences, le carre de T, les budgets du graphe ou le frame.

La preuve entiere a ete relue par g18_algebre_neuve et g18_audit_neuf. Une seconde voie F3 confirme le raccord : le Gram des u a rang22 modulo3, tandis que N/Gamma est tue par3. Cette seconde voie est inutile pour la formule explicite(2).

## Parametres et risque de circularite

La meme identite existe avec des parametres propres r,m : si H=[(r+1)I,-C;-C^t,rI-T], CT=0 et T^2+T=r(r+1)I-C^tC, alors U((T+(r+1)I)v)=-h(Cv). Les soeurs donnent2h_c dans Gamma ; la relation rh_c=-U(C_c^t) donne r h_c dans Gamma. Si r est impair, Bezout implique h_c dans Gamma. On ne transporte pas cette conclusion a r pair, notamment BvLS(r=4), ou ces arguments ne donnent que2h_c.

Il s'agit d'une CONSEQUENCE du repere physique simultane. Ce n'est pas un nouveau filtre independant une fois toutes ses identites imposees, et ce lemme ne ferme aucun genre g18/g20. Il est utile pour lier une recherche de vecteurs a son indice exact et pour ne pas confondre generation integrale et generation reelle.


---

# Pièce : G18_G20_SEPT_BLOCS_CAPACITE.md

SHA256 : eafa5a8153ccf6500d05a4c8a4329abfabe2d72fd586b10fd0cfb059a6732fd3

# Test global de capacite des sept blocs dans une enveloppe Golay explicite

## Hypotheses supplementaires

Ce test est CONDITIONNEL. On utilise l'enveloppe explicite U_Golay de la campagne0803, avec les coordonnees entieres divisees par sqrt(8), les4096 mots du code binaire engendre par le polynome donne, et deux charges r_1,r_2 de norme7 orthogonales. Leurs coordonnees sont les deux lignes B. Toutes les normes3 de U_Golay sont les mots de signes E correspondants aux4096 mots du code. La coque complete de norme3 de leur orthogonal N0 se reconstruit en imposant EB^t=0.

Le helper n'affirme pas que tout collage uniforme de rang24 soit cette enveloppe, ni qu'un shadowframe existe en general. La coque704 du choix0803 est un cas fixe de cette reconstruction, pas une hypothese imposee a des charges arbitraires.

Une selection candidate de SEPT blocs se code par M : h_c=2M_c/sqrt(8), chaque ligne est une octade signee, MM^t=8I. Le template physique demande huit colonnes de poids1 et seize de poids3.

## Premiere coupe : la demi-somme doit etre un vecteur entier du reseau

Pour le vrai reseau physique N, poser z=(sum_c h_c)/2. Ses produits avec les h sont2 et ses produits avec les u sont-(sum_c C_cp)/2, des entiers. Donc z appartient a N*, tandis que2z appartient a N. Comme det(N) est impair, N*/N n'a aucune2-torsion et z appartient a N. Sa norme vaut7.

Dans les coordonnees du template, Z=sum_c M_c. Chaque coordonnee est impaire, et vaut+/-1 ou+/-3. L'orthogonalite des sept lignes donne sum_j Z_j^2=56, donc exactement QUATRE coordonnees ont valeur absolue3. Elles appartiennent aux seize colonnes de poids3, hors des huit gros coefficients des deux charges B.

Pour que Z/sqrt(8) appartienne a U_Golay, il faut simultanement

    support des (Z_j-1)/2 modulo2 dans le code Golay,
    sum_j Z_j divisible par8.

Une violation ferme la selection des sept blocs entiere, dans cette enveloppe. Tester une seule jauge suffit : changer les signes des h modifie z par des vecteurs h entiers. Les64 lignes de demi-sommes signees, modulo signe global, sont ainsi toutes presentes et de norme7. Ce n'est pas une assertion qu'une selection quelconque de sept octades orthogonales satisfait le test.

## Deuxieme coupe : les42 directions D7 doivent etre disponibles simultanement

Pour une ligne de norme3 candidate u=E/sqrt(8), les produits avec les sept blocs sont

    (h_c,u)=M_c E/4.

Une racine physique doit avoir exactement DEUX produits non nuls, chacun+1 ou-1. A signe global de u pres, chaque support {c,d} doit fournir les DEUX directions orthogonales : les signes egaux et les signes opposes. Cela fait42 classes, distinctes deux a deux.

Pour chaque bloc, preparer trois ensembles de lignes de la coque complete : Z_c pour le produit0, P_c pour+1 et N_c pour-1. Pour un support {c,d}, poser

    F_cd=intersection des Z_k pour k hors {c,d},
    classe+ =F_cd intersect ((P_c intersect P_d) union (N_c intersect N_d)),
    classe- =F_cd intersect ((P_c intersect N_d) union (N_c intersect P_d)).

Si l'une de ces42 classes est vide, AUCUNE selection des42 u de cette enveloppe ne peut prolonger les SEPT blocs fixes. Les intersections se font par bitsets, sans produit cartesien de completions d'etoiles. Les valeurs +/-2 ou superieures ne sont admises dans aucune classe.

Un PASS signifie uniquement que chaque classe possede au moins un candidat. Il n'impose pas les produits mutuels T, les dix voisins de chaque ligne, CT=0, les budgets lambda/mu, P0, le frame ou l'indice de generation. Les42 vecteurs devront ensuite appartenir a UNE MEME selection satisfaisant tout cela. [G18_G20_QUARANTE_DEUX_GENERATEURS.md](G18_G20_QUARANTE_DEUX_GENERATEURS.md) fixe l'indice physique necessaire.

## Source et certificat

[G18_G20_SEPT_BLOCS_CAPACITE.mjs](G18_G20_SEPT_BLOCS_CAPACITE.mjs) est un module sans execution a l'import. Il reconstruit le code et la coque sur appel, puis retourne les masques des42 classes. Il controle aussi l'alignement de chaque colonne de M avec B :4*poids(M_j)+B_1j^2+B_2j^2=14. Une refutation contient la selectionM complete, les chargesB, leurs hashes, le hash du code/de la coque et la classe vide ou le defaut de demi-somme. La completude est fournie par la reconstruction depuis les4096 mots, pas par une liste arbitraire de candidats. Un rejeu independant doit refaire cette reconstruction et comparer les hashes ; le champ booleen complete_shell_reconstructed n'est jamais une preuve a lui seul.

Les petits tests joints comparent les intersections de bitsets a des profils abstraits explicites. Ils verifient aussi l'appartenance exacte des deux charges0803 au reseau Golay. Ce sont des tests de source, pas des graphes positifs ni une couverture de toutes les sept selections. Aucun type ou genre g18/g20 n'est exclu par la livraison du helper seule.


---

# Pièce : G18_G20_STATUTS_COMBINATOIRES0836.md

SHA256 : 69f1b2d2b890ec7ce34c4155a1f94dd4d97d2bcafd2be46ab118840296705d54

# Etat des pieces combinatoires 0836

Les pieces concernent le meme repere physique de49 vecteurs et, quand precise, ses deux normales communes dans un collage de rang24. Aucun balayage de types locaux n'a ete effectue dans cette livraison. Aucun type entier g18/g20 n'est nouvellement exclu.

| Piece | Conclusion exacte | Limite |
|---|---|---|
| G18_G20_QUARANTE_DEUX_GENERATEURS | Les42 vecteurs de norme3 engendrent N integralement ; formule entiere explicite pour chaque h | Ne concerne pas automatiquement Nmax d'indice7 ; consequence du vrai frame |
| G18_G20_DUAL_COORDONNEES | Trois directions duales independantes de norme<=1 interdisent le frame ; une composante D4 uniforme et D11 dans U de dimension<=24 sont exclus | D4 mixte non exclu ; preuve D11 utilise D12 acquis0803 |
| G18_G20_D6_QUATRE | Le cycle-glue D6^4 a4096 normes3 engendrant U ; classification COMPLETE des64512 normes4 plates | Contre-modele a une borne generale de rang<=20 de la coque ; aucun frame49 realise dans ce modele |
| G18_G20_D6_SIX_SPINORS | Les strates(f_A,f_B)=(6,0),(0,6) sont impossibles avec les deux normales communes et la borne duale | Ni les strates4+2 ni D6^4 entier ne sont fermees par cette piece |
| G18_G20_SEPT_BLOCS_CAPACITE | Pour sept blocs DONNES dans une enveloppe Golay explicite : demi-somme dans le reseau et disponibilite des42 signatures D7 necessaires | Aucun septuplet complet n'est couvert ; le template shadow24 est conditionnel hors du cas rootless |
| G18_G20_TEST_SEPT_BLOCS | Tests du helper sur signatures abstraites et la coque704 de normales physiques fixees | Ce n'est pas une selection de sept blocs, ni un graphe |

Les controles JS sont finis et courts. Le controle D6 de la coque utilise64 vecteurs explicites suffisants pour le rang24 ; la formule4096 est demontree par les quatre familles32^2. Le controle f6 traite1716 distributions relaxees, retrouve16 distributions exactes de capacite et zero paire de normales, plus256 paires de signes. Les equations du vrai frame restent des prerequis mathematiques, jamais des booleens valant preuve.

Les preuves de generation42, du carrier dual, D11 et de la classification h D6 ont ete relues independamment par g18_audit_neuf. La fermeture f6 a aussi sa seconde voie acquise : AUDIT_D6_SIX_FRACTIONNAIRES_MEME_PAIRE.md et verifier_D6_fA6_independant.mjs/.json, qui regenerent les1716 compositions, les16 profils exacts et zero paire de normales. Ce supplement reste une piece distincte du controle producteur.

Les fichiers0803 et les reprises anterieures restent intacts. Le manifeste propre liste les SHA256 des sources et sorties de cette livraison et de leurs prerequis precis. Le manifeste ne transforme aucune relaxation satisfaisable en realisation du graphe.


---

# Pièce : OBSTRUCTION_COQUE3_ET_D8_CUBE.md

SHA256 : 72363f4c8c247ce9032e4c7f7cb4d4af5f905cf529d95f32a0c2fd4942d7c962

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


---

# Pièce : ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md

SHA256 : 13a222669e15e92676160573bd112209f04d823fda1d8cc263f4a6453e138e39

# Sans racines : shadowframe24, code autodual et cubicite des sept octades

**Theoreme uniforme de sous-famille.** Tout reseau integral unimodulaire IMPAIR U de rang24, minimum>=2 et sans racines de norme2 possede24 ombres orthogonales de norme2, dont les doubles sont caracteristiques. Il s'ecrit, apres isometrie, par un code binaire C autodual doublement pair [24,12,8]. Aucune unicite du code ni classification de reseaux n'est invoquee.

Le template E/M/B devient ainsi necessaire sur TOUS les collages sans racines. Il reste conditionnel pour un collage ayant des racines ; le positif E8+U16 de la note harmonique montre qu'un shadowframe ne suit pas dans ce cas.

## 1. Le passage carre du moment a l'orthogonalite

Les deux theoremes theta autonomes donnent, lorsque r=0,

    #caracteristiques(carre8)=48,
    somme_{chi^2=8} chi chi^t=16I24.

La coque se partitionne en24 paires +/-chi, sans point fixe. Choisir une representative par paire et former la matrice CARREE K de24 colonnes. Alors KK^t=8I. Cette matrice est inversible, et K^tK=8I. Les representatives sont donc orthogonales de norme8. Les ombres s_i=chi_i/2 ont Gram2I24 et appartiennent toutes au meme coset Sh.

Le caractere carre de K est essentiel : avec plus de48 caracteristiques, un tight-frame n'est pas automatiquement une base orthogonale.

## 2. Le code associe, sans classification

Utiliser les axes orthonormes e_i=s_i/sqrt2. Pour x dans U, poser a_i=(x,chi_i)=sqrt8*x_i. La caracteristicite donne a_i entier et a_i=x^2 modulo2 pour TOUS les i. Donc U est contenu dans (1/sqrt8)Z24, et les24 coordonnees a ont une meme parite.

Soit U0 le sous-reseau des normes paires, d'indice2 dans U, et L0=sqrt2 U0. Il est contenu dans Z24 et de covolume2^13. Comme s_i-s_j et s_i+s_j sont des differences de deux ombres du meme coset, ils appartiennent a U ; leurs normes4 sont paires. Ainsi L0 contient2D24.

On a exactement L0 inter 2Z24=2D24. Sinon un vecteur2z avec somme z impaire permettrait, modulo2D24, d'obtenir2e_i dans L0. Cela donnerait sqrt2*e_i dans U, de norme2, interdit.

Le code C=L0 modulo2 a donc cardinal

    |C|=[L0:2D24]=2^25/2^13=2^12.

Il a dimension12. Pour b,d dans L0, l'integralite de (b/sqrt2,d/sqrt2) impose b.d pair ; C est orthogonal a lui-meme, donc AUTODUAL par dimension. La norme paire b^2/2 impose b^2=0 modulo4, donc les poids de C sont divisibles par4 : C est DOUBLEMENT PAIR.

Un mot nonzero de poids4 permettrait de choisir un releve b avec quatre coordonnees +/-1 et toutes les autres nulles. En effet les differences de deux releves de meme parite valent2z ; changer un seul signe ajuste la parite de somme z, donc permet une difference dans2D24. Le vecteur b/sqrt2 aurait norme2. Ainsi le poids minimal est>=8.

Il est exactement8. S'il etait>=12, les boules de Hamming de rayon4 autour des2^12 mots seraient disjointes. Chacune contient

    1+24+276+2024+10626=12951 >4096=2^24/2^12

mots, contradiction. Le code a donc parametres [24,12,8].

Les poids pairs impliquent que le mot tout-un est dans Cperp=C. Les complements sont donc des mots de C. Les seuls poids sont0,8,12,16,24. La projection sur deux coordonnees est surjective, sinon Cperp aurait un mot de poids<=2. Le deuxieme moment des poids et la complementarite donnent, en notant t=A8=A16,

    552 +296t +132(4094-2t)=2^10*24*23,

donc A8=A16=759 et A12=2576. Ce compte ne prouve ni ne suppose l'unicite d'un code de ces parametres.

## 3. Forme explicite du reseau entier

La serie scalaire theta donne4096 vecteurs de norme3. Choisir l'un d'eux u0. Dans les axes precedents, ses24 coordonnees a sont impaires et leur somme de carres vaut24 ; elles sont toutes +/-1. Inverser les axes pour obtenir u0=1/sqrt8.

L'integralite avec u0 impose, pour b dans L0, somme b=0 modulo4. Le reseau

    {b dans Z24 : b modulo2 dans C, somme b=0 modulo4}

a le meme indice2^13 que L0, et le contient : ils sont egaux. La condition de somme fournit un bit supplementaire sur le reseau preimage du code, puisqu'ajouter2e_i change la somme de2. Enfin U=U0 union(u0+U0). On obtient

    U={a/sqrt8 : a_i=m modulo2 pour tous i,
       {i:a_i=m+2 modulo4} dans C,
       somme a_i=0 modulo8}.

Les4096 vecteurs de norme3 sont exactement les signwords a_i=+/-1 associes aux4096 mots de C. La preuve identifie une construction par C, sans appeler ce code unique ni invoquer une classification externe.

## 4. Le template physique E/M/B est maintenant uniforme ici

Les42 u physiques ont la forme E_o/sqrt8 avec E_o dans{+/-1}^24 et leurs mots de signes dans C. Les h ont la forme M_c/sqrt2 avec M_c entier. Pour les deux normales y_i de norme7, poser B_i=sqrt8*y_i ; leurs coordonnees sont impaires.

L'energie contre chaque caracteristique chi_j=sqrt8e_j vaut56. Les42 produits E coutent42 et les deux produits B coutent au moins2. Elle interdit |2M_cj|>=4 et |B_ij|>=5. Donc M a entrees0,+/-1, chaque ligne a poids8 et appartient a C : les sept h sont des OCTADES signees, avec un nombre pair de signes moins. Chaque ligne B a quatre entrees d'absolu3 et vingt d'absolu1 ; leurs quatre-supports sont disjoints.

Dans chacune des24 colonnes, l'energie impose poids(M_colonne)=1 si un B vaut3, et poids3 sinon. Il y a huit colonnes de poids1 et seize de poids3. Les identites exactes du meme repere sont

    EE^t=8(3I-T), MM^t=8I7, ME^t=-4Inc, Inc E=-6M,
    BB^t=56I2, EB^t=MB^t=0,
    E^tE+4M^tM+B^tB=56I24.

Ici Inc est la matrice d'incidence D7 ; le code binaire est C. Les deux objets ne sont pas identifies.

## 5. Chaque octade porte un multigraphe cubique sans triple arete

Fixer un h et orienter les12 u incidentes pour que (h,u)=-1. Sur les huit positions de son octade, les produits de signes M_j E_oj ont somme-4 : exactement DEUX positions valent+1, les six autres-1. Associer a chaque u l'arete de ses deux positions minoritaires.

La relation 3h=-somme_12u donne, sur chaque position de l'octade, somme_12 M_jE_oj=-6. La position figure donc exactement trois fois comme minoritaire. Les12 aretes forment un multigraphe cubique sur huit sommets.

Deux u ayant la MEME arete minoritaire ont les memes huit signes sur l'octade. Leur difference binaire d est un mot du code et est disjointe de l'octade O. Elle ne peut avoir poids12 : alors O+d aurait poids20, et son complement, egalement dans le code, aurait poids4. Les seules possibilites pour deux u distinctes sont donc poids8 ou16, donnant Gram(u,u')=+1 ou-1, jamais0.

Dans le secteur local physique, T_star est la difference de deux matrices de matchings, T_star=P_mu-P_eta (les coins annules, si les matchings coincident, ne changent pas l'argument). Trois occurrences de la meme arete obligeraient leurs trois Gram mutuels a etre nonzero, donc formeraient un triangle dans l'union des deux matchings. Un triangle n'admet pas de coloration propre de ses aretes en deux couleurs : impossible. Toute arete minoritaire a donc multiplicite<=2.

Cette derniere coupe utilise le code, la meme octade et les matchings physiques ; le centroid seul ne suffit pas. Elle ne ferme pas tous les multigraphes cubiques ni tous les repères49.

## 6. Verification et portee

verifier_rootless_code24.mjs controle les indices, la borne de Hamming, les moments de poids, les trois profils energetiques, les28 paires minoritaires, la difference code disjointe d'une octade et les huit colorations possibles d'un triangle. La preuve universelle est analytique et algebrique ; ce petit controle n'est pas une enumeration de tous les codes ou collages.


---

# Pièce : SEPT_OCTADES_RANG_BINAIRE_PETIT.md

SHA256 : 13534ecf47c00a28dc11b35420cf73f9eb63c93320bfd87a8c367ccbec097b4a

# Une famille entière de sept appuis est exclue dans l'enveloppe Golay fixe

**Statut : démontré par preuve couvrante, après contre-audit humain indépendant ; contrôle de 128 polarités exactes joint.** Ce résultat porte sur les SEPT h du même repère physique, avec les deux normales fixes du contre-modèle 0803. Il ne repose pas sur un essai de septuplet et ne ferme pas tous les repères de toutes les enveloppes.

## 1. Hypothèses et lien avec le repère physique

Utiliser les coordonnées de l'enveloppe explicite du dossier 0803 : u=E/√8, h=2M/√8, r_i=B_i/√8. Les E physiques sont des mots de signes ±1 ; les sept lignes M sont des octades signées 0,±1 du code binaire C. Le même repère donne

    EᵀE + 4MᵀM + BᵀB = 56I24,
    MMᵀ = 8I7.

Les deux B sont impairs, de carré 56, avec quatre coefficients absolus 3 chacun ; leurs deux supports de gros coefficients sont disjoints. Cette structure a été acquise par les profils caractéristiques dans le template de rang 24. On ne la transporte pas à une enveloppe avec racines sans repère d'ombres.

Noter A le support de leurs huit gros coefficients. L'équation diagonale, avec 42 signes dans chaque colonne E, impose

    Σ_c M_cj² = 1 si j∈A, et 3 si j∉A.                    (1)

Ainsi les sept appuis O_c de poids 8 sont des mots de C, et chaque coordonnée appartient à une ou trois octades. Leur somme binaire est 1_24.

Le lemme ci-dessous ne suppose ni les signes de M, ni leur orthogonalité, ni la disponibilité des 42 u. Il ferme donc une famille complète d'appuis avant ces choix supplémentaires.

## 2. Lemme binaire uniforme

Soient sept appuis de poids 8 dans 24 coordonnées, avec répétitions permises, tels que chaque coordonnée apparaît une ou trois fois. Si le rang binaire de ces sept appuis est au plus quatre, alors

    A = {coordonnées apparaissant une fois}

est dans leur espace binaire engendré. En fait A est soit l'une des octades, soit le complément de la réunion de deux octades disjointes. Son poids est huit, puisque 7·8=|A|+3(24−|A|).

### Réduction au nombre de supports de multiplicité impaire

Poser V=span_F2(O_1,...,O_7) et e=1_24. La somme des sept appuis vaut e, donc e∈V. Une octade est non nulle et distincte de e. Deux octades distinctes ont des classes distinctes dans V/<e> : si elles différaient de e, leurs poids seraient 8 et 16, et non deux fois 8.

Le quotient a dimension au plus trois. Les supports distincts de multiplicité impaire ont des classes distinctes non nulles et leur somme est zéro dans ce quotient. Leur nombre est impair, au plus sept. Un seul est impossible. Cinq sont impossibles aussi : dans F2³, la somme des sept vecteurs non nuls est zéro, tandis que la somme d'un ensemble de cinq serait celle des deux vecteurs distincts complémentaires, donc non nulle. Il reste trois ou sept supports impairs.

### Trois supports impairs

Leur somme vaut e dans V, pas seulement dans le quotient : leur somme est précisément la somme des sept lignes, les répétitions paires disparaissant. Trois octades de poids total 24 dont la somme binaire est e sont disjointes et partitionnent les 24 coordonnées.

Une multiplicité de support est au plus trois, par la borne de colonne. Les seuls profils sont les suivants, à permutation près.

| Multiplicités des supports distincts | Conclusion explicite pour A |
|---|---|
| 3,3,1 | A est l'octade de multiplicité 1. |
| 3,2,1,1 | L'octade de multiplicité 3 est disjointe de l'octade de multiplicité 2, sinon une colonne apparaîtrait au moins cinq fois. A est le complément de leur réunion. |
| 2,2,1,1,1 | Les trois octades impaires forment le trio disjoint. Les deux octades de multiplicité 2 sont disjointes, sinon une colonne apparaîtrait cinq fois. A est le complément de leur réunion. |

Dans les trois cas, A est une somme binaire de e et d'appuis présents, donc appartient à V.

### Sept supports impairs : une preuve par huit caractères

Les sept appuis sont distincts, chacun apparaît une fois, et le quotient V/<e> est F2³. Ce sont ses sept classes non nulles. Une coordonnée définit une forme linéaire sur V qui prend la valeur 1 sur e ; il existe huit types possibles, indexés par x∈F2³. Noter n_x leur multiplicité.

Écrire les sept caractères non triviaux du groupe F2³ comme χ_a(x)=(-1)^(a·x). Chaque octade a une polarité σ_a∈{−1,+1} et sa valeur binaire est (1−σ_a χ_a(x))/2. Son poids huit donne

    Σ_x n_x σ_a χ_a(x) = 8.

L'inversion de Fourier, avec Σn_x=24, donne

    n_x = 3 + S_x,  où S_x=Σ_{a≠0} σ_a χ_a(x).            (2)

Sur un type présent, la multiplicité de colonne est (7−S_x)/2, donc vaut 1 ou 3 : S_x vaut 5 ou 1. Sur un type absent, (2) donne S_x=−3. Orthogonalité des sept caractères : Σ_x S_x=0 et Σ_x S_x²=56.

Si p,q,r sont les nombres de types de valeurs 5,1,−3, on obtient

    p+q+r=8, 5p+q−3r=0, 25p+q+9r=56,
    donc (p,q,r)=(1,4,3).

Le type unique x_0 où S=5 a multiplicité huit ; ce sont exactement les coordonnées A. À x_0, six caractères polarisés valent +1 et un seul vaut −1, pour un indice a_0. Après translation par x_0, les polarités sont donc toutes +1 sauf celle d'a_0. Aux quatre autres types présents, χ_a0 vaut −1 ; l'octade d'indice a_0 vaut alors zéro. Cette octade vaut un sur x_0 et sur les trois types absents. Elle est exactement A. Le lemme est prouvé dans tous les cas.

## 3. Application aux deux normales réellement construites en 0803

Dans le cas fixe, les gros coefficients sont aux coordonnées

    D1={0,1,2,9}, D2={3,4,13,15},
    A=D1∪D2, masque binaire 41503.

Le code se régénère depuis son polynôme propre, sans classification externe. A n'appartient pas à C ; un générateur qui a un produit impair avec A est imprimé dans le certificat. Comme les sept appuis O_c appartiennent à C, le lemme impose

    rang_F2 span(O_1,...,O_7) ≥ 5.                         (3)

Toutes les familles d'appuis de rang binaire ≤4 sont donc exclues **en une fois**, quels que soient les signes des sept h et les 42 u que l'on proposerait ensuite. Les appuis de rang 5,6,7 restent ouverts par cette coupe. Une paire de normales différente dont A serait une octade n'est pas fermée par ce raisonnement.

## 4. Contrôle exact et portée rootless

[controle_sept_octades_rang4.mjs](controle_sept_octades_rang4.mjs) vérifie les 128 polarités du cas à sept supports impairs, les profils de multiplicités dans F2³, et le syndrome non nul d'A dans le code propre. La preuve du §2 couvre tous les cas sans dépendre de cette enumeration. Le résultat est [controle_sept_octades_rang4.json](controle_sept_octades_rang4.json).

Le template octades est explicite dans l'enveloppe construite en 0803. Le nouveau théorème de l'auditeur montre également qu'une enveloppe unimodulaire impaire de rang 24 sans racines possède un repère d'ombres orthogonales ; le lemme binaire s'applique alors dès que son template est identifié, sans supposer un repère d'ombres supplémentaire. L'application numérique A=41503 concerne toutefois notre enveloppe et notre paire de normales fixes : elle ne prétend ni à l'unicité du code ni à l'exclusion de toutes les paires de normales.

Ce résultat complète les sept tests de capacité et de demi-somme ; il ne constitue pas un graphe, un genre fermé, ou un remplacement des contraintes mutuelles T et λ/μ.


---

# Pièce : SUPPLEMENT_D8_TROIS_TOUS_COLLAGES.md

SHA256 : 13c0e1b0ce89931ff8fdbec41ba7ea6843e4137198f7118e79d147103b8a1ec1

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


---

# Pièce : THEOREME_CARACTERISTIQUE8_THETA.md

SHA256 : dc70c6159e88fab9542fd83de6827396dd54c81c4d27331eb914e103e8b736d9

# Entree uniforme : une caracteristique de carre8 sans shadowframe

**Theoreme.** Soit U un reseau integral positif unimodulaire IMPAIR de rang24 et de minimum au moins2. Le nombre de ses vecteurs caracteristiques de carre8 est exactement

    48 + nombre de vecteurs de U de carre2.

En particulier, il en existe au moins48. Aucun repere de24 ombres orthogonales ni classification des reseaux n'est suppose. Le theoreme s'applique aux collages24 acquis en0803, donc les trois profils physiques de caracteristique8 deviennent un point d'entree uniforme. Il ne prouve pas l'existence d'un shadowframe24.

## 1. Conventions et transformations par Poisson

Poser q=exp(pi*i*tau), Im tau>0, et

    Theta_U(tau)=somme_{x dans U} q^(x,x),
    theta3=somme_{n dans Z} q^(n^2),
    theta4=somme_{n dans Z} (-1)^n q^(n^2),
    theta2=somme_{n dans Z} q^((n+1/2)^2).

On utilise l'action f|_k gamma=(c*tau+d)^(-k) f((a*tau+b)/(c*tau+d)). Les transformations T:tau->tau+1 et S:tau->-1/tau se deduisent des sommes et de Poisson sur Z :

    theta3|T=theta4, theta4|T=theta3,
    theta2(tau+1)=exp(pi*i/4) theta2(tau),
    theta3(-1/tau)=(-i*tau)^(1/2) theta3(tau),
    theta2(-1/tau)=(-i*tau)^(1/2) theta4(tau),
    theta4(-1/tau)=(-i*tau)^(1/2) theta2(tau).

Poisson sur U, de covolume1, donne Theta_U(-1/tau)=(-i*tau)^12 Theta_U(tau). Comme(-i)^12=1 et les normes sont entieres, Theta_U est de poids12, avec caractere TRIVIAL, sur Gamma_theta=<S,T^2>.

Un vecteur caracteristique kappa existe : x->(x,x) modulo2 est une forme lineaire sur U/2U ; l'unimodularite rend le Gram modulo2 inversible et fournit kappa dans U tel que(kappa,x)=(x,x) modulo2.

Poisson avec le facteur(-1)^(kappa,x) donne exactement

    Theta_U|_12(TS) = Theta_Sh,
    Sh=kappa/2+U.

Le facteur de Poisson est encore(-i)^12=1. Ainsi aucune phase ni facteur2 n'est cache dans la serie du shadow. Elle est bornee a l'infini, puisque Sh est un coset d'un reseau positif. Les cusps de Gamma_theta sont representes par infini et1 ; cette formule prouve l'holomorphie de Theta_U a tous les cusps, sans supposer une congruence prealable sur kappa^2.

Le groupe Gamma_theta est l'image inverse du sous-groupe{I,S} dans SL2(F2), d'ordre2 dans le groupe d'ordre6. Pour justifier l'image inverse, le noyau Gamma(2) est engendre par -I, T^2 et ST^2S^{-1}. Une reduction euclidienne de la premiere colonne (a,c), avec a impair et c pair, le prouve : les operations a->a+2mc et c->c+2ma choisies avec quotient pair le plus proche reduisent strictement le plus grand module jusqu'a (1,0) ou (-1,0) ; le cas d'egalite des modules est exclu par les parites. La matrice restante est +/-T^{2m}. Ces generateurs sont dans <S,T^2>, et S represente l'autre element du sous-groupe modulo2. L'indice est donc3. Ses trois cosets a gauche sont representes par I,T,TS ; leurs six elements modulo2 sont egalement controles dans le petit source.

## 2. Pourquoi il n'y a que quatre coefficients : preuve de la base

Poser A=theta2^4, B=theta4^4, C=theta3^4 et

    Delta8=AB/16,
    f_j=theta3^(24-8j) Delta8^j, j=0,1,2,3.

Chaque f_j est une forme holomorphe de poids12 et de caractere trivial sur Gamma_theta. Sous S, A et B s'echangent avec signe moins, C prend signe moins ; dans les puissances presentes, ces signes s'annulent. Sous T^2, tout est invariant. Aux deux cusps, les series ont des exposants non negatifs. A l'infini, f_j commence par q^j avec coefficient1.

Voici une preuve autonome de la dimension necessaire. Supposons F de poids12, holomorphe sur Gamma_theta et aux cusps, avec F=O(q^4). Son produit norme

    P=F (F|_12 T) (F|_12 TS)

est une forme holomorphe de poids36 sur SL2(Z) : les trois facteurs se permutent sous toute matrice, par la decomposition en cosets. A l'infini, les deux premiers facteurs sont O(q^4), le troisieme est borne. P est donc O(q^8)=O(Q^4), avec Q=exp(2pi*i*tau).

La formule de valence sur SL2(Z) est

    ord_infini P + (1/2)ord_i P + (1/3)ord_rho P
      + somme_autres_points ord_z P = poids(P)/12 =3.

Tous les termes sont non negatifs pour une forme holomorphe. L'ordre>=4 est impossible si P n'est pas nul ; donc F=0. Pour rappeler la preuve de cette formule : appliquer le principe de l'argument au domaine |Re tau|<=1/2, |tau|>=1, tronque en hauteur. Les deux bords verticaux sont identifies par T. Les deux moities du cercle sont identifiees par S ; leur changement d'argument, issu du facteur tau^k, fournit k/12. Les petits arcs autour des points fixes ont respectivement les fractions1/2 et1/3, et le bord superieur fournit l'ordre en Q. Ceci est un calcul de contour, et non une classification de formes ou de reseaux.

On peut maintenant soustraire a n'importe quelle forme de poids12 les quatre f_j, successivement, pour annuler ses coefficients q^0,q^1,q^2,q^3. Le reste est O(q^4), donc nul. Les f_j sont independants par leurs quatre ordres initiaux. Il s'agit bien d'une base de dimension4, avec les bonnes normalisations.

Ainsi

    Theta_U = theta3^24 + a theta3^16 Delta8
                           + b theta3^8 Delta8^2 + c Delta8^3.

## 3. Coefficients physiques et absence de norme1

Les developpements commencent par

    theta3=1+2q+O(q^4),
    Delta8=q-8q^2+28q^3+O(q^4).

Le coefficient de q dans theta3^24 est48 et celui de theta3^16 Delta8 est1. Min U>=2 impose donc a=-48.

Le coefficient de q^2 est1104+24a+b=b-48. Il compte exactement les racines de norme2 de U ; par positivite,

    b=48+#roots(U)>=48.

Il reste a eliminer c, sans supposer que U soit sans racines.

## 4. Oddness elimine c, et Poisson compte les caracteristiques8

Les transformations au cusp1 donnent

    C|_2(TS)=-A,
    Delta8|_4(TS)=-BC/16.

Par consequent la serie du shadow est

    Theta_Sh=A^6 - (a/16) A^4 BC
                    + (b/256) A^2 B^2 C^2
                    - (c/4096) B^3 C^3.

Sa constante vaut-c/4096. Si0 appartenait a Sh, kappa appartiendrait a2U et toutes les normes de U seraient paires. L'IMPARITE de U exclut cette possibilite ; Theta_Sh n'a donc pas de constante, et c=0.

A=16q+O(q^3), B=C=1+O(q). Le premier terme contribue a partir de q^6, le second a partir de q^4, et le troisieme a partir de q^2 avec coefficientb. Il n'y a pas de terme de norme plus petite. Le coefficient q^2 de Theta_Sh est donc b.

Multiplier un vecteur de Sh par2 est une bijection de Sh sur l'ensemble kappa+2U des vecteurs caracteristiques de U. La norme2 dans Sh equivaut au carre8 pour la caracteristique. Donc

    #caracteristiques_U(carre8)=b=48+#roots(U).

La congruence caracteristique^2=0 modulo8 suit egalement de la forme de Theta_Sh, dont tous les exposants sont pairs. Il n'est pas necessaire de l'invoquer avant le calcul.

## 5. Portee sur le probleme physique49

Les collages U24 de0803 sont integraux, unimodulaires, impairs et de minimum>=2. Le theoreme leur fournit UNE caracteristique de carre8, et meme au moins48, sans postuler de24 vecteurs orthogonaux. Les trois profils de produits avec le frame physique49 et les deux directions de norme7 sont donc uniformement disponibles.

On ne deduit pas que ces caracteristiques puissent etre choisies orthogonales, ni qu'un shadowframe24 existe. Les matrices E/M/B de0803 restent conditionnelles tant que ce repere n'est pas demontre. Le compte b seul est modulaire : il ne fournit pas une contradiction avec le frame49, et aucune elimination complete de g18/g20 ne decoule de cette note.

Le theoreme harmonique ajoute ensuite un resultat precis : lorsque U est SANS RACINES, ses48 caracteristiques8 forment24 paires orthogonales. Dans cette sous-famille seulement, le shadowframe est acquis ; la preuve et le code associe figurent dans ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md. Ce corollaire ne s'applique pas aux collages ayant des racines.

## 6. Second controle de normalisations et positifs

Le source autonome `verifier_theta_caracteristique8.mjs` calcule les series exactes jusqu'a q^8, avec coefficients entiers verifies. Il controle la base triangulaire, les quatre transforms shadow, a=-48, roots=b-48, constante-c/4096 et coefficient shadowq^2=b lorsque c=0.

Le vrai reseau positif Golay de0803, unimodulaire impair24/min3, donne b=48. Le source retrouve4096 normes3 et98256 normes4 : ce dernier compte est aussi obtenu directement par759 octades fois128 signes, plus4*binom(24,2) vecteurs de type4^2. Les48 caracteristiques de carre8 y sont explicitement +/-sqrt8*e_i.

La limite paire est controlee avec la serie du reseau E8^3 : min2 mais non impair, c=-4096, constante shadow1. Le theoreme impair n'y est pas applique. Les positifs H(2,3)/BvLS de0803 gardent leurs propres rangs et parametres3/9 ; ils ne sont pas poses comme unimodulaires24.


---

# Pièce : THEOREME_MOMENTS_CARACTERISTIQUES8.md

SHA256 : 2fdb9e5dace239006dcc0894c20c855a095a2ccb5ac138e60e4968d1c0e9ad18

# Moment collectif exact des caracteristiques8

**Theoreme autonome.** Soit U integral positif unimodulaire impair de rang24, minimum>=2. Poser r=#racines de norme2, R=somme_{alpha^2=2} alpha alpha^t, et S2={chi/2 : chi caracteristique, chi^2=8}. Alors

    somme_{s dans S2} s s^t = (4+r/4) I_24 -2 R.

Equivalent : somme_{chi^2=8} chi chi^t = (16+r) I_24 -8R. La formule 4I+R n'est pas correcte en general ; elle lui est equivalente seulement lorsque R=(r/12)I, c'est-a-dire lorsque la coque des racines est un2-design.

## 1. Poisson pondere et base en poids14

Soit P(x)=x^t Qx avec Q symetrique reel de trace0. La derivee seconde de l'integrale gaussienne, et l'annulation du terme constant par trace Q=0, donnent

    Fourier[P(x) exp(pi*i*tau*x^2)](y)
      =(-i*tau)^(-12) tau^(-2) P(y) exp(-pi*i*y^2/tau).

Ainsi la serie Theta_{U,P}=somme P(x)q^(x^2) satisfait

    Theta_{U,P}|_14 S = Theta_{U,P},
    Theta_{U,P}|_14 T^2 = Theta_{U,P},
    Theta_{U,P}|_14(TS) = Theta_{Sh,P}.

Le caractere est bien TRIVIAL ; oublier le facteur tau^(-2) dans Fourier produirait un mauvais signe. L'holomorphie aux cusps suit de Poisson et de la convergence des series ponderees positives.

Reprendre A=theta2^4, B=theta4^4, C=theta3^4, Delta8=AB/16 et f_j=theta3^(24-8j)Delta8^j. Poser D=A-B. On a

    D|_2 S=D, D|_2 T^2=D, D|_2(TS)=B+C.

Les quatre Df_j sont donc holomorphes de poids14 sur Gamma_theta ; chacune commence par -q^j. Elles forment une base : si F=O(q^4), le produit norme F(F|T)(F|TS) est holomorphe de poids42 sur SL2(Z) et d'ordre>=4 en Q. La valence donne un total42/12=7/2, donc F=0. La preuve d'indice3 et de valence est detaillee dans THEOREME_CARACTERISTIQUE8_THETA.md, sans classification des formes ou des reseaux.

## 2. Un seul coefficient pondere subsiste

Le coefficient constant de Theta_{U,P} est0 car P(0)=0. Le coefficient q est0 par min U>=2. Dans l'expansion somme d_j Df_j, cela force d_0=d_1=0.

La constante de sa transformee shadow vaut -2d_3/4096, les autres termes commencant en q^2,q^4,q^6. Elle est nulle car le shadow ne contient pas0 ; meme si0 y appartenait, P(0)=0. Donc d_3=0.

Le coefficient q^2 dans Df_2 vaut-1. On obtient d_2=-somme_{alpha^2=2}P(alpha). Le coefficient q^2 dans (Df_2)|TS vaut2, puisque (B+C)(0)=2 et (f_2|TS) commence par q^2. Finalement

    somme_{s dans S2}P(s) = -2 somme_{alpha^2=2}P(alpha).

Cette identite vaut pour toute quadratique harmonique. L'operateur M_S+2R est donc scalaire. Son trace vaut2|S2|+4r=2(48+r)+4r=96+6r ; en divisant par24, on trouve le scalaire4+r/4 annonce.

## 3. Contre-test construit qui distingue les signes

Construire U16=D8^2+<(s,v),(v,s)> avec s=(1/2)^8, v=e_1. Le glue a quatre classes00,sv,vs,cc. Les deux generateurs ont norme3 et produit1, donc U16 est integral unimodulaire impair et min2.

Prendre U=E8 orthogonal U16, ou E8=D8+Zs. Il existe464 racines :240 dans E8,112 dans chacune des deux composantes D8. L'operateur R vaut60I sur E8 et28I sur les seize autres directions.

Les caracteristiques8 sont toutes nulles sur E8. Dans U16, elles sont exactement :

* les256 vecteurs (+/-1)^8 dans une composante et0 dans l'autre, avec un nombre IMPAIR de signes moins ;
* les256 vecteurs (+/-2e_i,+/-2e_j), une unite double dans chacune des deux composantes.

Ce sont bien des caracteristiques sur D8^2 et les deux glues. La description est exhaustive :2U16 est entier, les parites sont constantes dans chaque bloc8 ; un bloc impair coute au moins8, et dans le cas entier pair les parites des glues imposent une unite double dans chaque bloc. Une composante E8 nonzero d'une caracteristique coute au moins8, et U16 impair interdit une caracteristique nulle, donc elle ne peut intervenir au carre total8.

Il y a512 caracteristiques, comme48+464. L'operateur du shadow vaut0 sur E8 et64I sur les autres dimensions. C'est exactement120I-2R. La candidate4I+R donnerait64I sur E8 et32I ailleurs : elle est donc falsifiee par ce vrai reseau positif.

## 4. Coupe sur le meme repere physique49

Dans un collage portant le repere physique, toutes les caracteristiques8 satisfont |(chi,h_c)|<=2, et leurs produits sur u_o et y_i sont +/-1 ou +/-3. Cela suit de l'energie56 :42 produits roots impairs plus2 produits norm7 impairs coutent deja44. Un bloc avec produit4 couterait16 de plus. Les trois profils restent ceux du theoreme scalaire.

L'identite collective donne notamment, pour chaque u_o,

    nombre{chi^2=8 : |(chi,u_o)|=3}
       = r/4 - somme_{alpha^2=2}(alpha,u_o)^2.

Pour chaque h_c elle donne

    nombre{chi^2=8 : |(chi,h_c)|=2}
       =16+r-2 somme_{alpha^2=2}(alpha,h_c)^2.

Pour chaque normale y_i de norme7 elle donne

    nombre{chi^2=8 : |(chi,y_i)|=3}
       =8+3r/4-somme_{alpha^2=2}(alpha,y_i)^2.

Ces comptes sont entiers non negatifs. Ils concernent le MEME repere et toute la coque8, sans supposer24 caracteristiques orthogonales. Ils ne constituent pas, seuls, une contradiction globale. La matrice R est celle de toutes les racines du collage U, et non seulement de N ou Nmax.

Le meme coefficient pondere q^3 donne un controle de la coque3 complete. Le coefficient de q^3 dans Df_2 vaut24 ; celui de q^3 dans la serie scalaire vaut4096, independamment de r. Ainsi

    #vecteurs_U(carre3)=4096,
    somme_{u^2=3 dans U}u u^t=(512+2r)I_24-24R.

Son rang doit etre au moins22 si le collage porte le repere42, puisque ces42 generateurs doivent engendrer un span22. Il s'agit d'une coupe sur la coque COMPLETE d'un collage donne, pas d'une borne de rang universelle pour toutes les coques. Dans le contre-test E8+U16, cet operateur vaut0 sur E8 et768I ailleurs ; la coque3 n'a que16 directions, bien que le reseau ait rang24.

Lorsque r=0, les48 caracteristiques8 se groupent en24 paires. Le moment16I donne une matrice CARREE de24 representantes avec KK^t=8I, donc K^tK=8I. Le shadowframe24 est alors demontre. ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md developpe ce corollaire et sa construction binaire sans supposer l'unicite d'un code.

Le source verifier_moments_caracteristique8.mjs controle les quatre normalisations ponderees et les operateurs du contre-test explicite. Aucun catalogue SRG, aucun solveur, aucune classification de reseaux n'est utilise.
