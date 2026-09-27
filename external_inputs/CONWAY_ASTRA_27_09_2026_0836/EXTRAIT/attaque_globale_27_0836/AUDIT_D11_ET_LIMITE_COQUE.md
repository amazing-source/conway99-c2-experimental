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
