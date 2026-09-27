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
