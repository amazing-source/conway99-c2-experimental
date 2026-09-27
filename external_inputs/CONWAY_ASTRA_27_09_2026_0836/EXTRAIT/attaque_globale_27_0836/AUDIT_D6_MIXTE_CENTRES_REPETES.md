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
