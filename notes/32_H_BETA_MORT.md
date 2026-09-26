# 32 — H-β est impossible : preuve assistée, certificats rationnels exacts (26/09/2026)

Session principale C2. Calcul plafonné, **autorisé explicitement par l'utilisateur** (26/09, « Run capped search », plafond ≈ 3 h).
**Statut : PROUVÉ, sous réserve de relecture.**
- Les contraintes sont toutes démontrées à la main (notes 27, 28, 30, 31, et carnet 19.1).
- Chaque squelette est tué par un certificat de Farkas **rationnel**, revérifié en **arithmétique exacte** (fractions), sans solveur.
- Idée du modèle par colonnes : « structures », S15. Identités (P2) : C1, notes/116.

## 1. Le modèle par colonnes (`scripts/hb_colmodel.py`)
Squelette H-β fixé :
- T = Z₇ ;
- orientation eulérienne des cordes ;
- en chaque bloc, un ordre β du chemin D P_c – {c,A} – {c,B} – P_{c+1}.

On obtient ainsi les 42 orbites (i,j,k) (pivot, bloc libre, troisième bloc) et les 6 orbites libres de chaque bloc.

**Colonne** c = (Z, p, s), où p est la paire de voisins de Z sur le cycle libre en j, et s une solution entière exacte du rang
lointain de Z. Toutes les valeurs val_c(R) = φ_Z(R) sont alors des **constantes** de la colonne :
- val(P_Z) = 0 ;
- F1 : val({i,r}) = 2[r = k] ;
- val({j,r}) = #{Y ∈ p : P_Y = {j,r}} ;
- s satisfait (L) (sommes de bloc égales à 4), avec des valeurs dans {0,1,2}. φ ≤ 2 vaut pour toute paire, car un voisin de chaque
  orbite au plus, sinon Z serait partenaire D.

**Contraintes linéaires** en x_c ∈ [0,1] :
- **une colonne par orbite** ;
- **cycles libres**, laissés **variables** :
  - arêtes symétriques ;
  - aucune arête entre sœurs (19.1) ;
  - coupes de sous-tours de tailles 3, 4 et 5. Elles sont valides car f = 6 : le graphe libre est un seul 6-cycle ;
  - deux sœurs ont au plus un voisin commun (19.1) ;
  - règle typée : p ⊄ {j,k} (note 30 §4) ;
- **(S)** Σ_c val_c(R) x_c = 24 ;
- **(PPE)** Σ_c val_c(R)² x_c = 32 ;
- **(C)** couplage : E[R][R′] = E[R′][R] ;
- **(P2)** Σ_c val_c(R) val_c(R′) x_c + E[R][R′] = 16 − 4[R ∩ R′ ≠ ∅].

Toutes ces identités sont contrôlées sur BvLS (note 31 §1 : 0 violation sur 3 025).

**Certificat.** On résout le PL « min Σ écarts ». En cas d'infaisabilité, on garde les multiplicateurs y des lignes, arrondis en
rationnels. Pour tout point de la boîte (x_c ∈ [0,1], écart de chaque ligne ≤ dans [0, rhs]), yᵀAx reste dans un intervalle [LB, UB]
calculé exactement, colonne par colonne. **Si yᵀb ∉ [LB, UB], aucune configuration n'existe.**

## 2. Contrôles
- Cycles fixés au cycle symétrique 10, qui est F2-faisable, sans (P2) : PL faisable. ✓
- Cycles fixés au cycle 0 : infaisable, certificat vérifié. ✓
- Squelette circulant, cycles libres, **sans (P2)** : PL faisable. Le premier ordre seul ne suffit donc pas, comme mesuré au niveau
  indicatrices (note 31). ✓
- Même squelette **avec (P2)** : infaisable, écart 56,26. Certificat exact : yᵀb = 56,26 > UB ≈ 0.

## 3. Résultat
`scripts/hb_colmodel_all.py` : 552 classes de squelettes à D₇ près, soit 7 680 squelettes (60 orientations × 2⁷). Une ligne JSON par
classe dans `logs/hb_colall_*.jsonl`, avec les multiplicateurs rationnels.

**Toutes les 552 classes sont PL-infaisables, avec certificat vérifié exactement dans le même processus.**
- Écart minimal : 55,41. Les marges sont larges : yᵀb dépasse UB de plus de 55 dans chaque classe.
- Couverture : **7 680 squelettes sur 7 680**.
- Temps : environ 12 250 s de CPU (8 processus, 25 min de temps réel), environ 22 s par classe.
- Certificats compressés dans `logs/hb_certs/hb_colall_*.jsonl.gz` (3 Mo).

Revérification indépendante (`scripts/hb_verify_certs.py`) : elle relit les multiplicateurs stockés, reconstruit le modèle et
vérifie en fractions, sans aucun solveur.

**552 sur 552 vérifiées, 0 échec, 7 680 squelettes couverts** (`logs/hb_verify_all.log`, environ 300 s × 8).

## 4. Conséquence
**Théorème 32.1.** La famille H de M1 est impossible. On a H = H-β (note 30), et H-β n'a aucune configuration.
Dans M1, il ne reste que les familles avec un bloc A de degré 6 : (1,0,n) pour n = 3…6, et (1,1,4), (1,1,5).

**Nature de la preuve.** Les certificats sont denses : toutes les lignes (P2) portent un poids non nul, et ce poids n'est pas
fonction de |R ∩ R′| seul. C'est un argument spectral global de second ordre, adapté à chaque squelette, et non une chasse aux
doubles. Une version entièrement « à la main » reste ouverte.

## 5. Modèle général : orientation fixée, structures D variables (`scripts/gen_colmodel.py`, petits tests)
Colonnes (Z, pivot, troisième bloc, vecteur n, rang lointain). Sont variables : les pivots des paires tordues, les couplages D en chaque
pivot (variables m), les graphes libres (variables e), et les rangs lointains. On résout par **génération de colonnes**, et le
certificat est vérifié exactement **sur toutes les colonnes** (énumérées, arithmétique entière).
- **Orientation H circulante** (T = Z₇ tordu, cordes ancrées en c+2 et c+3), α et β tous permis, **sans aucun des lemmes 28.x ou
  30.1** : sans (P2), faisable ; avec (P2), **PL infaisable**, écart 7,42. Certificat exact : yᵀb = 7,417 > UB = 0,0013.
  C'est une confirmation indépendante, pour cette orientation, de 30.2 et de 32.1 ensemble.
- **Orientation variable** (tout laissé libre) : PL **faisable**. Ancrages variables avec T = C₇ tordu : PL **faisable** aussi. Le
  relâchement mélange les orientations fractionnaires : il faut **fixer l'orientation**.

## 6. Suite
Le même moteur s'applique à toute configuration à carrés « un bloc » : mélanges quelconques et tout-tordu (« structures » l'applique
au tout-tordu, S15). Il demande :
- de rendre variables les structures D elles-mêmes (pivots et partenaires), et pas seulement les cycles libres ;
- d'utiliser des coupes valides pour f > 6 : tailles 3 et 5 seulement, puisque 4 + 4 est possible ;
- de nouveaux calculs, hors du plafond autorisé pour H-β. **Ils ne seront pas lancés sans accord.**
