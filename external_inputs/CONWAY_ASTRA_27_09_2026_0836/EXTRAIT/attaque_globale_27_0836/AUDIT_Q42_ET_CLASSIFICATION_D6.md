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
