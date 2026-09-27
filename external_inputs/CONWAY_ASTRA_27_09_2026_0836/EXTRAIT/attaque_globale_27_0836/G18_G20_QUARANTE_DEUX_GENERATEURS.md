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
