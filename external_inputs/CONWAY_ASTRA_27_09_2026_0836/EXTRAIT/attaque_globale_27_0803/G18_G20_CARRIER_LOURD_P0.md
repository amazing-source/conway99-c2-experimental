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
