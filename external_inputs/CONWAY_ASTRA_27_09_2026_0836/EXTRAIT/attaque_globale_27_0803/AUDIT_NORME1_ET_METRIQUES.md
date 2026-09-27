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
