# 22 — Revue complète du laboratoire C2 (24/09/2026, soir) : inventaire scoré, corrections, pistes

Demande de l'utilisateur : scorer **toutes** les idées, tentées ou non, et tout revérifier ; lire aussi la branche C1.
Échelles : **P** = potentiel restant pour tuer C2 ou réduire nettement l'analyse de cas (1–5) ; **C** = coût de la prochaine étape
décisive (1 = minutes, 2 = heures, 3 = une journée, 4 = des jours, 5 = des semaines).

## 0. Méthode

- Quatre relecteurs indépendants, en parallèle et en lecture seule. Leurs rapports bruts, avec **une ligne scorée par idée**, sont dans
  `notes/22_annexes/` :
  - A : notes 00–12 et IDEES ;
  - B : notes 13–17 et NEGATIVE_RESULTS ;
  - C : notes 18–21, ponts B01–B07, SYNTHESE, REPRISE ;
  - D : branche C1 (instantané en lecture seule, voir l'annexe D).
- Vérifications faites par moi ce soir (CALCULÉ) :
  - Le constructeur RSF reproduit **à l'octet près** le CNF certifié K2K2P3 (sha256 7ab7737d…, `row_system_full.py`).
  - Encodages des 18 faits du lemme des étoiles, relus terme à terme :
    - (R), (D), (I) et (P) correspondent à λ = 1, μ = 2 ;
    - la négation de compte par sélecteur (≤ k−1 ou ≥ k+1) est correcte ;
    - « Σ exact » ajoute exactement ¬(a∧b) sur les paires non sœurs.
  - Les 11 cubes de l'étoile libre sont **exhaustifs** : tailles d'orbites sous B₆ 3840 + 2304 + 1440 + 720 + 640 + 960 + 160 + 120 +
    180 + 30 + 1 = 10 395 = nombre de couplages parfaits de 12 points.
  - Borne générale, à la main (DÉRIVÉ) : **n₃ ≥ 2079 − 9N**. En effet 9N triplets (sommet, paire de droites) ont c = 4 ; les autres ont
    c ≤ 2, car c = 3 est impossible (Lou–Murin) ; et 6P = 8316 − 2n₃.
  - Parité nouvelle, venue de C1 (L18 : z₂ = S/2, z₁₁ = 4n₃ − 2S), DÉRIVÉ :
    - une copie t-invariante de Z₂ aurait x pour unique sommet de degré 4, et L ~ tL, ce qui est exclu (a₁ = 14) ;
    - donc z₂ est pair et **S ≡ 0 (mod 4)**, puis **z₁₁ ≡ 4·n_one (mod 8)**.
    - Le relecteur D écrivait « z₁₁ ≡ 0 (mod 8) » : c'est faux sauf si n_one est pair.
- Vérifications des relecteurs :
  - les 57 lignes « DRAT VERIFIED » concordent avec les manifestes et les CNF sur disque ;
  - les 29 graphes de degré ≤ 2 sont réénumérés, chaque exclusion rattachée à son certificat ;
  - la preuve humaine d'allsib (note 17) est vérifiée pas à pas : rang δ₀ = 20, rang δ₁ = 85 sur F₂, donc H¹ = 0 ;
  - la complétude de la formulation compacte (note 20 §3) est revérifiée à la main ;
  - les valeurs de Krein et les dénombrements de Burnside de la note 16 sont recalculés.

## 1. Ce qui est réellement établi (la chaîne)

- Étapes, toutes vérifiées :
  1. modèle complet ;
  2. étage Q ;
  3. système χ ;
  4. lemme des étoiles : deg Σ ≤ 2 ; 18 ingrédients DRAT, recollement à la main, revérifié ;
  5. classification des 29 graphes de degré ≤ 2 ;
  6. **10 survivants**, tous avec un bloc libre.
- Réserves :
  - la base de confiance reste l'encodage du modèle complet, identique au k14_none.cnf du dépôt principal ;
  - **aucune preuve DRAT/LRAT n'est archivée** : `cert_run.sh` efface la preuve après vérification. « VERIFIED » est une ligne de
    journal ; revérifier demande de relancer kissat, 20 à 495 s par CNF critique.
- Le lemme de l'étoile libre :
  - sa **forme globale** équivaut au but ;
  - seule sa **forme locale** (RSF(star(c)) UNSAT pour c libre) aurait du contenu, et elle est ouverte (note 20 §0).

## 2. Tableau scoré des grandes lignes (synthèse ; le détail ligne par ligne est dans les annexes)

| ligne | statut réel après revue | P | C | raison |
|---|---|---|---|---|
| G1 (grilles = codes parfaits, k ∈ {4, 14}) | DÉRIVÉ | 3 | – | levier du lemme des étoiles |
| Lemme S1 (paire sœur ⇒ partition, m ∈ {2, 7}) | DÉRIVÉ | 3 | – | idem |
| Lemme des étoiles | DÉRIVÉ, ingrédients DRAT | 3 | 1 | mérite une rédaction de niveau ÉTABLI |
| Allsib impossible, preuve humaine (note 17) | DÉRIVÉ, vérifié | 3 | – | seul mécanisme local → global réussi : **parité** |
| Lemme T (K₃ + K₂) | DÉRIVÉ | 2 | – | vérifié |
| 10 survivants ; C₄, P₄+K₂ exclus (DRAT) | CALCULÉ + DRAT | 3 | 3–4 | P₅, 2P₃ (au moins) et K₃, P₄ (exact) UNKNOWN à 600 s |
| n₃/3 ≡ n_one (mod 2) ; n₃ ≥ 2079 − 9N ; S ≡ 0 (mod 4) ; z₁₁ ≡ 4n_one (mod 8) | DÉRIVÉ | 2 | – | briques pour « q:parite » |
| Parités des 7-rangs (notes 09–10) | DÉRIVÉ ; « aucune obstruction de genre » est HEURISTIQUE | 1 | 4 | ne filtrent rien seules |
| Formulation compacte de l'étoile libre (note 20 §3) | DÉRIVÉ, complète | 4 | 3 | = « holonomie de droite » de C1 ; doit utiliser (i) |
| Cubes RSF, cadical, CP-SAT, MILP, recuit sur l'étoile libre | CALCULÉ, non concluant | 1 | – | UNKNOWN ne vaut rien (calibration) |
| **Parité rendue linéaire** : variables Z, XOR, élimination de Gauss ; propagateur DPLL(T) (19c, 19i, I-33, I-35) | ouvert | **4** | 2–3 | tout ce qui a marché était une parité |
| **Cocycle à défauts** : note 17 étendue par les carrés one/dis (07, I-32, 17b) | ouvert | **4** | 3–4 | seul patron local → global qui a réussi |
| **q:parite** : Burnside mod 2 à l'ordre 7 sous t (N10, L18 de C1) | ouvert | 3 | 3 | une parité de \|Σ\| tuerait la moitié des survivants |
| Scinder (iii) : résoudre ι = Φ∘(−1)∘Φ⁻¹ puis Φ | ouvert | 3 | 2 | deux problèmes bien plus petits |
| Survivants en sémantique exacte, cube-and-conquer (I-34) | ouvert | 3 | 3–4 | réduirait C2 au seul cas Σ = ∅ |
| E7 pour les 6 survivants contenant P₃ (I-18) | ouvert | 3 | 2 | coins forcés par S1 |
| Krein sur les droites scindé par t (L16 de C1) | ouvert | 3 | 3 | positivité à trois points, jamais faite en C2 |
| Programme Δ (12D + note 07) | ouvert | 3 | 3 | bornes certifiées sur n_one, n_dis |
| Règles R0 et L12 de C1 comme préfiltre à x | ouvert | 2 | 1 | gratuit, faible sur A111111 |
| Verrouiller la chaîne (archiver les LRAT, rédiger en ÉTABLI) | ouvert | 2 | 2 | rigueur, citabilité |
| Genres, Brown, discriminants ; moments, SOS, Lasserre ; entrelacement (y compris le modèle à 39 sommets de C1) ; Delsarte local ; Hodge | fermé | 1 | – | ne pas refaire (annexes B et D) |

## 3. Corrections appliquées ce soir

- **Note 19**
  - « d = 0 à 4 » : jamais terminé.
  - Étoiles mixtes : testées sur 6 lignes seulement.
  - survx_K3 et survx_P4 : UNKNOWN, ajoutés au texte.
  - « dès que Σ a 4 arêtes » corrigé : P₅ et 2P₃ sont UNKNOWN.
  - L(Q) : HEURISTIQUE ; 7425 est la dimension d'un noyau.
- **Note 20**
  - Énoncés précis, forme globale et forme locale.
  - Compatibilité BvLS vide.
  - Idée 3 tautologique.
  - Antériorité (I-33, note 19) et portée de la validation.
- **Note 21**
  - J1 est une ERREUR (doublon de G1).
  - J2, J4, J6 et J7 sont des doublons ; J3 a été en partie tenté.
  - Lemme des étoiles : « ingrédients DRAT ».
  - Verdict de la note 09 relabellisé.
- **Notes 09 et 10** : conclusion générale « aucune obstruction de genre » relabellisée HEURISTIQUE.
- **Notes 06, 11, 12, 14, IDEES** : bornes d'avant le lemme des étoiles (|Σ| ≤ 7, n_sib ≤ 7, κ ≥ 28, 28 racines…) annotées avec
  les valeurs actuelles (|Σ| ≤ 4, κ ≥ 34, ≤ 16, ≥ 68, ≤ 25, ≥ 17).
- **Note 13**
  - « coin colinéaire ⇒ dis » : DOUTEUX, le cas one n'est pas exclu.
  - R2 : à reformuler ou retirer.
  - Relèvement vers H(7,3) : SPÉCULATION.
- **Notes 15, 16, NEGATIVE_RESULTS**
  - Portée des leçons « automatiquement cohérent » limitée aux filtres C3, C4, C8.
  - Test de recollement limité à Λ′ ∩ tΛ = ∅.
  - Lasserre : direction douteuse, car aveugle à la parité.
  - N10 : ni intégralité ni parité utilisées.
- **JOURNAL** : ancienne affirmation n₃ ≡ 0 (mod 6) barrée.
- **B01** : allsib désormais exclu.
- **SYNTHESE, REPRISE**
  - Bandeau « état au 24/09 » en tête de REPRISE.
  - « 53 graphes », « 12 restants » et « cible (P) » marqués PÉRIMÉS.

## 4. Diagnostic convergent (les trois relecteurs C2, indépendamment)

- Tout ce qui a réellement tué quelque chose ici est un argument de **parité** : allsib par H¹(M₇; Z₂) = 0 ; le lemme des étoiles
  par (−1)³ ≠ +1.
- Les solveurs CDCL sont exponentiellement mauvais sur la parité (formules de Tseitin). Cela explique que kissat, cadical, CP-SAT et
  les relaxations de moments calent partout. Il faut changer d'outil ou d'encodage, pas ajouter du calcul.
- Obstacle connu (note 19, 19c) : dans les variables (a, b), la parité des signes n'est linéaire qu'à Q fixé. Il faut donc :
  - soit un propagateur de Gauss à Q partiel (I-35) ;
  - soit une preuve à la main du même type que le lemme des étoiles, étendue aux carrés one/dis ;
  - soit des parités globales (Burnside à l'ordre 7).
- **Contrainte de méthode venue de C1.** Ses géométries témoins tordues (20 et 42 sommets) ont chaque σ_x comme automorphisme et
  **tous les blocs libres**. Toute preuve du lemme de l'étoile libre doit donc utiliser la contrainte globale (i), la bijectivité de
  Φ (μ = 2 entre lignes de l'étoile). Les axiomes locaux et la symétrie de réflexion ne suffisent pas.

## 5. Programme proposé, dans l'ordre

1. **q:parite — FAIT le 24/09 au soir (`scripts/order7_burnside.py`) : aucune contradiction, P → 1.**
   - Source : famille affine indépendante des 208 fréquences d'ordre 7 (archive en lecture seule), qui concorde avec Reimbayev corrigé
     de 4 coquilles (audit du dépôt principal). Contrôles : les 208 masques sont canoniques ; Σp = C(99,7) = 14 887 031 544 ; Σq = Σr = 0 ;
     coefficients entiers.
   - En C2 : n₃ ≡ n_one et z = z₁₁/4 ≡ n_one (mod 2), donc f_H ≡ p + (q + r)·n_one.
   - 22 classes admettent une involution compatible avec C2. **4 sont entièrement déterminées par la carte** (types à 2 ou 3 droites par
     x : 3465, 42, 420, 420 copies invariantes) : toutes cohérentes, ce sont des identités.
   - **7 autres réduites à la main** à des identités connues, toutes cohérentes :
     - K₃ + C₄ : 5n_sib + 4n_one + 3n_dis ;
     - « prisme + x » : Σ_c d_c = 2n_sib + n_one ;
     - les deux chaînes de triangles, via les paires de M_c et de τ_c : 42 − Σd_c ;
     - la classe à racines pendantes : 378 + Σd_c ;
     - triangle + 4 isolés : 2499 − 9n_sib − 10n_one − 11n_dis, via les lignes et (I) ;
     - graphe vide : 4382 − 2n_sib − n_one, via #triangles(Γ₁) = 126 + 4n_sib + 2n_one.
   - Les 11 restantes se ramènent à des statistiques de triangles signés, fixées par le spectre ; elles n'ont pas été détaillées.
   - Pourquoi n_sib n'apparaît jamais avec un poids impair : une paire sœur {i, j} est non ordonnée ; un 7-ensemble t-invariant
     (x + 3 orbites) la voit deux fois, par (i, j) et (j, i), ou bien elle se compense avec n_dis via n_sib + n_one + n_dis = 21.
     **Une parité de |Σ| demanderait l'ordre 9** (la grille elle-même), hors de portée des formules connues.
   - Sous-produit (DÉRIVÉ) : S ≡ 0 (mod 4) et z₁₁ ≡ 4n_one (mod 8).
   - Programme initial, conservé pour mémoire : retrouver la 208ᵉ formule et contrôler Σz_i = C(99,7) (fait via la famille
     indépendante), puis calculer la parité des copies t-invariantes. Retrouver la 208ᵉ formule, contrôler la règle de somme Σz_i = C(99, 7) (C1 y a trouvé des erreurs), puis
   calculer pour chaque motif d'ordre 7 la parité des copies t-invariantes (qui contiennent toutes x). But : une contrainte de parité
   sur n_sib = |Σ|, n_one, n_dis. Une parité de |Σ| éliminerait la moitié des 10 survivants.
2. **Parité linéaire** (P4, C2–3). Encodage avec variables de signe Z et XOR de (I) et des orbites « − ». Validation obligatoire :
   K₁,₃ doit devenir instantané. Ensuite les cubes A111111 et A6 avec élimination de Gauss.
3. **Cocycle à défauts** (P4, C3–4), à la main : étendre la note 17 aux carrés one/dis. Le lemme du relecteur A sur les carrés one
   (r_α + r_β ≤ 1) est à vérifier d'abord.
4. En parallèle, quand la machine est libre : survivants en sémantique exacte (I-34) ; archivage des LRAT des certificats critiques.

## 6. Pour la branche C1 (à transmettre si l'utilisateur le souhaite ; rien n'a été écrit dans son dépôt)

**Erreurs et doutes relevés** (annexe D §4) :
- N10:34 : Bruck–Ryser ne dit rien à l'ordre 55, car 55 ≡ 3 (mod 4).
- N60:117 : l'affirmation sur |Aut| contredit leur propre rapport.
- L8 : la justification de la brisure de symétrie est absente de N40.
- L11 : n'est pas rédigé.
- Aucun contrôle positif BvLS, aucun DRAT.
- Étiquettes périmées (twolabel_dom234 et dom2345 sont UNSAT dans leurs données).

**Apports de C2 à C1** :
- **P ≥ 6N** : une grille contient 6 prismes et un prisme est dans au plus une grille. Avec leur L16 : N ≤ 191.
- La chaîne DRAT/Docker de C2 peut leur fournir le contrôle BvLS et des certificats.
- Nos modèles grid_spread.py et grid_offx_phi.py.
- La statistique « appariement D » comme troisième relation candidate entre n₃ et S.
