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
