# 14 — Mécanismes de preuve externes, en profondeur (salve « reset », 24/09/2026)

Sources : deux agents de recherche ciblés (Hall / Hamming local / Makhnev / Cameron ; Ishida / nombres d'intersection triples) et mes
propres calculs. Les textes extraits sont copiés dans `downloads/profondeur_2409/` : Makhnev 1988 = mzm4220, Hall 1960,
Makhnev–Minakova = dm144, Bondarenko–Radchenko = br, Brouwer–Van Maldeghem = srgw, Ishida.

Étiquettes de littérature :
- **[R]** : texte lu (par l'agent) ;
- **[S]** : connu seulement par une source secondaire ;
- **[M]** : déduction de l'agent, non publiée.

Pour ce qui vient de moi : étiquettes du labo.

## 0. Verdict

Le mécanisme qui « rendrait C2 facile » existe dans la littérature. C'est exactement celui du mouvement choisi (note 11) :

> **réflexions ponctuelles automorphes ⇒ translations ⇒ structure affine sur F₃ ⇒ 3^m sommets**
> (Hall 1960 ; Bondarenko–Radchenko 2013).

C2 est le cas où **une seule** réflexion est automorphe. Ce qui manque est un **lemme de propagation**. L'étape qui le fournit chez
Bondarenko–Radchenko échoue ici pour une raison de dimension, chiffrée au §3 : le 1-voisinage engendre 14 dimensions sur 44.

Les autres mécanismes sont vides ou non transférables, chacun pour une raison précise (§5 à §10) : Makhnev 1988, caractérisations
locales de Hamming, Cameron, Ishida, nombres d'intersection triples, Akiyama.

## 1. Objet central : la réflexion ponctuelle σ_v, définie en TOUT sommet (DÉRIVÉ)

**Définition.** Le graphe est de diamètre 2, avec λ = 1 et μ = 2.
- σ_v(v) = v.
- Sur N(v) : σ_v échange les deux autres points de chaque droite passant par v.
- Pour z ∈ N₂(v), de voisins communs p, q avec v : σ_v(z) est le second voisin commun de σ_v(p) et σ_v(q). Il est bien défini :
  σ_v(p) ≁ σ_v(q), et σ_v(z) ∈ N₂(v).
- C'est la « négation de carte » ι_v de la note 13.

**Propriétés.**
- σ_v est une involution de V, de point fixe unique v.
- Elle préserve toutes les arêtes, sauf peut-être les 504 arêtes internes à N₂(v). Donc σ_v ∈ Aut(Γ) ⟺ σ_v préserve le graphe des
  84 racines de la carte en v.
- Pour tout g ∈ Aut(Γ) : g σ_v g⁻¹ = σ_{g v}, car la construction est canonique.

**Place de C2 (ÉTABLI).**
- **C2 ⟺ σ_x ∈ Aut(Γ) pour un sommet x.** C'est le lemme « t = σ » de Makhnev, déjà dans la carte 00. Une trace le redonne :
  tr(tA) = 2f = 14 + 7·tr(t|V₃), avec f impair, force f = 7 droites fixes.
- Si σ_x ∈ Aut, alors σ_x σ_w σ_x = σ_{σ_x w} ≠ σ_w pour tout w ≠ x : deux réflexions distinctes ne commutent jamais.
- Comme |Aut Γ| ≤ 3 (carte 00), **au plus une réflexion est automorphe** : deux engendreraient un diédral d'ordre ≥ 6.

**C2 est un graphe « de Hall en exactement un point ».**

## 2. Hall 1960 — systèmes triples de Hall [R]

**Preuve d'origine.**
- Thm 3.1 : « tout point est le point fixe unique d'une involution automorphe » ⟺ tout triangle engendre un AG(2,3).
- Le sens direct est une chasse de clôture sur les 9 points du plan : s₁ envoie 246 sur 357 ; il faut une droite 258 ; puis 349,
  487, 596 ; on obtient les 12 droites.
- Lemme 4.1 : s_r s_s s_r = s_t sur une droite {r,s,t}, et (s_r s_s)³ = 1. Les produits de deux réflexions sont des translations.
- Pas global (Thm 4.2) : 4 points indépendants engendrent S(27) ou S(81). Sous transitivité, les translations commutent, d'où AG(r,3).
- En général on obtient une boucle de Moufang commutative d'exposant 3, donc 3^m points (Bruck).

**Mécanisme abstrait.** Des réflexions automorphes en suffisamment de points referment localement la géométrie en plans affines ;
leurs produits sont des translations ; on termine par la théorie des 3-groupes ou des boucles.

**Analogue C2.**
- Γ n'est pas un système triple de Steiner : deux points non adjacents ne sont pas colinéaires.
- Le substitut naturel est le triple {u, v, σ_u(v)}. Il ne « se ferme » que si σ_u(v) = σ_v(u), ce qui est vrai dans une grille
  (§4, H1).
- La chasse de Hall a besoin des réflexions aux 9 points d'un plan. C2 n'en fournit qu'une.

**Statut.** Transfert exact, bloqué dès la première étape. Il faudrait des réflexions automorphes en ≥ 2 points, d'où le lemme de
propagation (§3).

## 3. Bondarenko–Radchenko 2013 [R] — prolonger une réflexion locale par une base propre

**Preuve d'origine** (JCTB 103, famille srg((n²+3n−1)², n²(n+3), 1, n(n+1)), qui contient 9 et 81).
- La valeur propre négative θ a une multiplicité g égale à k. N(v) est donc une **base** de V_θ.
- σ_v permute N(v) en préservant leur Gram ; elle définit donc une isométrie O de V_θ.
- Tout u_z est déterminé par ses produits scalaires avec N(v), que σ_v transporte : l'adjacence de z à N(v) est σ_v-équivariante par
  construction. Donc O u_z = u_{σ_v z}, et σ_v ∈ Aut (Prop 1).
- Lemme 2 : σ_u(v) = σ_v(u) ; σ_uσ_vσ_u = σ_{σ_u(v)} ; σ_uσ_v est d'ordre 3 sans point fixe ; pour u ~ v, il déplace chaque sommet
  vers un voisin.
- Lemme 3 : (σ_vσ_wσ_u)² = e, prouvé avec λ = 1 ; c'est l'associativité.
- Prop 2 : espace vectoriel sur F₃, donc 3^m sommets.

**Mécanisme abstrait : rigidité spectrale du 1-voisinage.** Si la boule de rayon 1 engendre un espace propre, toute symétrie locale
compatible avec la carte est globale.

**Analogue C2 (DÉRIVÉ, calcul exact).**
- Dans V₋₄ (dim 44), le Gram de N(v) vaut (27I − 9P + J)/63, où P est le couplage des droites. Ses valeurs propres sont 32/63 ;
  18/63 (×6) ; 36/63 (×7). **Il est de rang 14.** Et u_v = −¼ Σ u_p est dans ce même sous-espace.
- Dans V₃ (dim 54) : (44I + 11P − 2J)/77, de valeurs propres 27/77, 55/77 (×6), 33/77 (×7). **Rang 14.**
- Le 1-voisinage fixe donc σ_v sur 14 dimensions, et **30 (resp. 40) lui échappent**. Elles portent exactement le Gram résiduel des
  racines :

  (27I − 9Q + J)/63 − G_{D₇} ⪰ 0, de rang ≤ 30,

  où Q est le graphe des racines (inconnu) et G_{D₇} un Gram fixé par la carte. C'est la matrice de l'étage S sous un autre angle.
- **Variante modulaire.** Seul p = 7 rend A − 3I de petit rang (3 ≡ −4 mod 7). Mais M = A − 3I y vérifie M² ≡ 2J : la forme de Gram
  est constante, donc la reconstruction de BR est impossible sans une forme nouvelle. Lien avec D₇(N₃) de type moins (note 10).

**Le lemme manquant, formulé.**

> **(P) Propagation.** Si σ_x ∈ Aut(Γ), il existe w ≠ x tel que σ_w ∈ Aut(Γ).

Avec le §1, **(P) ⟺ C2 est vide**. (P) n'est pas plus facile en soi, mais dit *ce qu'une preuve doit faire* : rigidifier le résidu de
dimension 30. Versions affaiblies testables :
- **(P_grille)** = R2 ;
- **(P_J)** : identités sur le défaut J du §4 ;
- **(P_rés)** : rigidité du Gram résiduel, par un SDP qui rejoint le théorème rêvé 21.

## 4. Le défaut de Hall de C2, mesuré en x (DÉRIVÉ, nouveau)

**(H1) Symétrie des milieux.** σ_v(x) = σ_x(v) ⟺ v est un coin d'un carré D de type sib ⟺ le quadrangle x–p–v–q est dans une grille.
Cela concerne **4 n_sib ≤ 28 racines sur 84**.

*Preuve.* Soit v = p + q.
- σ_v(p) = p + M_p(q) et σ_v(q) = q + M_q(p). Ces deux racines sont voisines de v.
- Si σ_v(x) = tv, elles sont aussi voisines de tv, donc dans D(v) = {w, tw}. Elles sont distinctes, donc t-conjuguées :
  {q, M_q(p)} = {−p, −M_p(q)}.
- Comme q ≠ −p, on obtient M_p(q) = −q et M_q(p) = −p : les deux arcs sœurs, donc {bloc p, bloc q} ∈ Σ.
- La réciproque se vérifie directement. ∎

La première identité du Lemme 2 de BR échoue donc en x pour **au moins 56 racines**.

**(H2) Translations locales.**
- ρᵢ = σ_x σ_{eᵢ} déplace R⁺ le long d'arêtes ⟺ les droites de M_{eᵢ} sont D-fermantes.
- Or #(t-orbites D-fermantes) = 2n_sib + n_one ≤ n_sib + 21 ≤ 28, sur 42.
- La propriété « déplace chaque sommet vers un voisin » du Lemme 2 échoue donc pour **au moins 14 orbites de droites**.

**(H3) Multiplicité des milieux.**
- Posons m(a,b) = #{v : σ_v(a) = b}. Alors Σ_{b≠a} m(a,b) = 98 pour tout a.
- Moyenne sur les paires adjacentes : **1 + J/1386**. Sur les paires non adjacentes : **1 − J/8316**.
- Ici J = #{(v,a) : a ∈ N₂(v), σ_v(a) ~ a}.
- Dans une structure de Hall : m ≡ 1 et J = 0 (Paley(9), BvLS).
- Si σ_v ∈ Aut, sa tranche J′_v = #{a ∈ N₂(v) : σ_v(a) ~ a} est nulle : l'arête {a, σ_v a} serait σ_v-stable, donc sa droite aussi,
  et le troisième point serait v. En C2, J′_x = 0.

**(H4) Tranche « a = x ».**
- J_x = #{racines v = p+q : M_p(q) = M_q(p)} : une même demi-étiquette b termine les deux droites de v en p et en q.
- Configuration à 7 points : x, p, q, b, p+q, p+b, q+b, avec les droites {p, p+q, p+b} et {q, p+q, q+b}. Elle est interdite dans
  toute structure de Hall.
- Elle ne dépend que des couplages locaux en x, mais **pas de l'étage Q seul** : Q = a + b efface la distinction A[u,v] / A[u,tv]
  qui fixe M_p(q). Il faut les étages Q et S ensemble.

**(H5) R2 et translations.** R2 ⟺ ρ_w déplace chaque point de Λ le long d'une arête : c'est le Lemme 2 de BR restreint aux grilles.

**Lecture.** La borne certifiée |Σ| ≤ 7 dit exactement que **C2 est loin de Hall autour de x**. Une preuve doit montrer l'incompatibilité
de « Hall en x » (σ_x ∈ Aut) et de « loin de Hall autour de x ».

## 5. Makhnev 1988 [R] (Mat. Zametki 44(5), réf. [7] de Reimbayev)

**Preuve d'origine.**
- Hypothèse (*) : deux triangles reliés par ≥ 2 arêtes le sont par 3. Autrement dit, tout quadrangle se ferme en grille, soit
  **n₃ = 0**.
- Thm 2 : pas de srg(99,14,1,2) vérifiant (*).
- On forme le graphe des 231 droites, deux droites étant adjacentes si elles sont parallèles dans une grille. Il est
  arête-régulier, de valence 12, avec λ = 1.
- On clôt autour d'une droite Δ : 60 points, 20 droites, puis Λ₀ de 33 droites. C'est un srg(33,12,1,6), exclu : une multiplicité
  vaudrait 44/7 [M].

**Mécanisme abstrait : DESCENTE (renormalisation) 99 → 33** par clôture sous un parallélisme de grilles. C'est la même famille d'idées
que R2 (auto-similarité des sous-structures parfaites), mais dans le régime « tous les coins se ferment ».

**Analogue C2.** C2 est à l'extrême opposé : au plus 7 grilles par x, et le cas « sans grille » est le cœur dur (note 08). La descente
a besoin d'une abondance de grilles.

**Statut.** Inapplicable tel quel. SPÉCULATION : chercher une descente pilotée par t plutôt que par les grilles, vers les 21 carrés D ou
vers l'orbifold à 50 points (O7).

Corollaire : n₃ > 0 dans tout graphe à 99 sommets. En C2, n₃/3 ≡ n_one (mod 2). (Corrigé le 24/09, note 20 : la note 08 affirmait
« n₃ ≡ 0 (mod 6) » à partir d'une analyse de cas incomplète.)

## 6. Caractérisations locales des graphes de Hamming [S/R]

**Preuves d'origine.**
- Egawa 1981 : un DRG avec le tableau de H(d,q) est H(d,q) ou un graphe de Doob.
- Nomura 1990 et Koolen 1995 : a₂ = 2a₁ entraîne un quotient de Hamming.
- Brouwer 1983 et Mulder : revêtement par le cube.
- Matsumoto 1991 : « localement Hamming » ⇒ H(r)/π.
- Mollard 1991 : |V| = ∏ h^{N_h}.

**Mécanisme abstrait.** On étend un isomorphisme de boules de rayon 1, poids par poids, par complétion de quadrangles (μ = 2). On
obtient un revêtement depuis l'objet universel.

**Analogue C2.**
- La carte en x a pour ensemble de sommets la boule de rayon 2 de H(7,3) (1 + 14 + 84), et X_Γ est localement H(7,3) (O2).
- Mais un revêtement H(7,3) → Γ aurait des fibres de 2187/99 ∉ Z.
- Γ est de diamètre 2, alors qu'Egawa et Nomura demandent ≥ 3.
- 140 des 231 droites évitent N(x) : Γ n'est pas faiblement modulaire, donc Chalopin–Chepoi–Hirai–Osajda ne s'applique pas [M].
- L'hypothèse de Mollard (pas de K₂□K₃∖e induit) équivaut à n₃ = 0, qui est exclu.

**Statut.** Inapplicable. Lecture utile : Γ est « la 2-boule de H(7,3), avec les droites des sommets intérieurs recouplées (M_{eᵢ} non
sœur) et la 3-couronne repliée sur les racines ». La complétion de quadrangles casse dès la première droite non sœur (|Σ| ≤ 7).

## 7. Cameron 1975 — quadrangles partiels [S]

**Preuve d'origine.**
- Γ est le graphe de colinéarité d'un PQ(2,6,2).
- Thm 2 (variance des nombres de voisins communs des triades) :
  [s(t−1)+(μ−1)(μ−2)]·[s²t(t+1)/μ − 1 − s(t+1) + μ] ≥ μs²(t−1)².
- Pour (2,6,2) : **710 > 200**. L'égalité (triades régulières) est donc impossible.
- PQ(2,t,2) connus : t = 1 et t = 10 seulement. Les représentations linéaires (graphes de cosets) exigent 3^m sommets.

**Analogue C2.** Les triades t-invariantes {x, v, tv} ont [111] = 0 forcé (agent 1), ce qui est cohérent.

**Statut.** Vide.

## 8. Ishida — identité trace = rang (quotient de Brauer) [S]

Identité : tr(t·E) = rang_{F₂}(E[F,F] mod 2), pour E idempotent 2-entier commutant avec t, et F les éléments fixes.

- **Module des sommets** (agent 1) : vide ; il ne redonne que a₁ = 14.
- **Extension (mon calcul exact, `scripts/ishida_modules.py`, `logs/ishida_modules.txt`)** :

| Module | Éléments fixes F | Idempotent 2-entier | Valeurs sur F | Rang = trace |
|---|---|---|---|---|
| droites (231) | 7 droites de x | E_odd = I − Nᵀ(E₁₄/21 + E₋₄/3)N | 62/77, −1/231 | 6 = 0 + tr(t\|ker N) = 6 |
| arêtes (693) | 7 arêtes {eᵢ, −eᵢ} | E′ = BᵀE₃B/17 (BBᵀ = A + 14I) | 6/77, −8/1309 ≡ 0 | 0 = 0 |
| carrés μ (2079) | 21 carrés D | E = Q_sᵀE₋₄Q_s/39 (Q_sQ_sᵀ = 83I + 11A + J) | (16 − 9e)/2457, e pair ⇒ ≡ 0 | 0 = 0 |

**Raison générale (DÉRIVÉ).**
- Côté trace : il est fixé par (tr(t|V_θ)) = (1, 0, 0).
- Côté rang : il ne voit que la configuration fixe (étoile de x, 7 arêtes, 21 carrés D). Sa seule partie variable, le nombre e
  d'arêtes entre deux carrés D, est toujours paire (orbites de t de taille 2).

**Statut.** Vide sur les quatre modules (N14).

## 9. Nombres d'intersection triples [S/R]

**Preuves d'origine.**
- Coolsaet–Jurišić et Vidali : il faut un paramètre de Krein nul pour obtenir des équations supplémentaires. Pour (99,14,1,2), aucun
  ne l'est (q¹₁₁ ≈ 33,24, q²₂₂ ≈ 13,24).
- Makhnev–Guo–Efimov (symétrisation des tableaux, qui tue {22,21,4;1,2,14}) : résumé seul.

**Analogue C2.** Triples t-invariants {x, v, tv} : [111] = 0 forcé, parités respectées.

**Statut.** Vide. HEURISTIQUE : la symétrisation n'apporte que des comptages d'ordre ≤ 4, contenus dans les fréquences d'ordre 7 (N10).
Non vérifié en détail.

## 10. Akiyama (B07)

Identités de Venkov sur des trames : les trames de C2 sont minces. Défavorable (déjà noté).

## 11. Tableau

| Mécanisme | Mouvement abstrait | Ce qui bloque en C2 | Statut |
|---|---|---|---|
| Hall 1960 | réflexions automorphes ⇒ plans affines ⇒ translations | réflexions automorphes en ≥ 2 points | exact, bloqué : lemme (P) |
| Bondarenko–Radchenko 2013 | 1-voisinage = base propre ⇒ la réflexion est globale | rang 14 < 44 (résidu de dim 30) | chiffré ; (P_grille), (P_J), (P_rés) |
| Makhnev 1988 | descente 99 → 33 par parallélisme de grilles | exige n₃ = 0 ; C2 est pauvre en grilles | inapplicable |
| Hamming local | revêtement par complétion de quadrangles | 2187/99 ∉ Z ; diamètre 2 | inapplicable |
| Cameron 1975 | variance des triades | inégalité stricte (710 > 200) | vide |
| Ishida | trace = rang (Brauer) | côté trace fixé par les paramètres | vide (4 modules) |
| Intersections triples | équations de Krein | aucun Krein nul | vide |
| Akiyama | Venkov sur trames | trames minces | défavorable |

## 12. Ce qui change pour la suite

- **Nouvel objet du labo** : la famille (σ_v) et ses défauts de Hall (H1–H5). Le résultat certifié |Σ| ≤ 7 se relit comme « loin de
  Hall en x ».
- **Cibles, par coût croissant** :
  1. J_x : la configuration à 7 points est-elle forcée ? interdite ? C'est une question SAT sur la structure locale en x
     (couplages M_c et D). Il faut une relaxation locale bien choisie : le modèle complet résiste (N11).
  2. R2 = (P_grille), avec un budget long quand la machine est libre.
  3. (P_rés) : SDP du résidu de dimension 30, avec la symétrie t.
- **Forme d'une contradiction** : « Hall en x » ⇒ une régularité des σ_w pour w ~ x ⇒ une borne inférieure sur les grilles ou les
  droites D-fermantes, contre |Σ| ≤ 7 et 2n_sib + n_one ≤ 28.
