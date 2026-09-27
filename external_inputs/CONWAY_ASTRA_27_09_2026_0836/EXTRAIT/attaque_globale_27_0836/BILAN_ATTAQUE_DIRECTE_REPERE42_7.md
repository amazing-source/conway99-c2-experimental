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
