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
