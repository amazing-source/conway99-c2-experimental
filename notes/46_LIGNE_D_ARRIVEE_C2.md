# 46 — Ligne d'arrivée de C2 (27/09/2026, adoptée par le pilote)

Directive de l'utilisateur, relayée par C1 : **toutes les ressources vont sur C2 (cas involution), jusqu'à le finir.** Pas de
dossier Sol, pas de piste visant le graphe entier.

Objectif : « si le graphe de Conway existe, il est asymétrique », avec « pas d'ordre 3 » (C3).

La ligne d'arrivée ci-dessous est une liste FINIE et UNIFORME d'instances. Proposée par C1 ; relue et amendée par C2.

## 1. Identité de comptage (C1 ; relue par C2)
- **Étiquettes.** Chaque orbite a une étiquette en chacun de ses 2 blocs, soit 84 étiquettes, 12 par bloc.
- **Bouts pivots par orbite.**
  - Frère : 2.
  - « Un bloc » via i : 1 (en i).
  - Dis : 0.
- **Notations.** #piv_c = nombre d'étiquettes pivots en c ; d_c = nombre d'étiquettes non pivots en c dont l'orbite est dis.
- **Comptes.**
  - Σ_c #piv_c = 4|Σ| + (42 − 2|Σ| − 2n_dis) = 42 + 2|Σ| − 2n_dis.
  - Σ_c d_c = 4 n_dis.
- **Donc** Σ_c w_c = 84 + 4|Σ| ≥ 84, avec w_c := 2#piv_c + d_c. **En toute configuration, un bloc a w_c ≥ 12.**

## 2. Information locale par étiquette non pivot v (C1, Lemme 1 ; relecture formelle demandée à structures)
- **Fait.** v ∈ Φ(z) ∩ Φ(σz) ⟺ {z, σz} est le partenaire D de l'orbite étoile de v.
- **Si cette orbite est « un bloc »** (via bloc(v), puisque v n'est pas pivot) : SEC_v. La sécante centrée en v est sur une paire
  qui CONTIENT bloc(v).
- **Si elle est dis** : SEC-dis_v. La paire ÉVITE bloc(v).

## 3. Instance I(τ), une par classe de type τ
- **Variables et contraintes.**
  - Le système local (i)–(iii) + L1/S1/S2, plus les lemmes généraux de LEMMA_SCOPES (valides avec dis et Σ ≠ ∅).
  - Pour chaque étiquette non pivot v, une variable β_v : β_v = 0 ⟹ SEC_v ; β_v = 1 ⟹ SEC-dis_v.
  - La cardinalité 2#piv(τ) + Σ_v β_v ≥ 12.
- **Cas particuliers.**
  - ≥ 6 pivots : la cardinalité est automatique.
  - Étoiles libres : β ≡ 1.
- **Complétude.** Toute configuration a un bloc c de poids w_c ≥ 12. Son système local, muni du VRAI β, est satisfiable. Donc, si
  **toutes les I(τ) sont UNSAT, il n'y a pas d'involution.** Cela couvre Σ ≠ ∅, les carrés dis, M1, les mélanges, et T = K₇
  simple ou non. Plus d'arbre de familles.

## 4. Mesure du progrès
- **N = 3 308 classes de types** : 1 787 à 0 pivot, 958 à 2, 407 à 4, 106 à 6, 39 à 8, 11 à 12 (compte à confirmer par
  structures).
- **Progrès = X / 3 308.** Une instance compte quand elle est certifiée : encodage sans lex-leader, preuve DRAT, drat-trim
  « s VERIFIED ».
- **Déjà acquis.**
  - Un certificat SANS SEC (voie rung-1, `logs/rung1_proofs.log`) implique I(τ) : moins de contraintes, donc l'UNSAT se transmet.
  - Les 33 certificats AVEC SEC (`logs/decl_proofs.log`) ne prouvent que l'étage n_dis = 0 : c'est le théorème Σ = ∅
    « tout un bloc », extensible à Σ ≠ ∅ si n_dis = 0. Ils sont à refaire sous forme I(τ) ou sans SEC.

## 5. Risque principal
- Les étoiles libres (β ≡ 1, SEC-dis partout) : inconnues à 40 s au portable (glucose) sur 2 types.
- Mesure au PC : ~20 étoiles libres à 1 h, dès que structures a poussé --beta. Elle dira si la ligne d'arrivée se compte en
  jours ou en semaines.

## 6. Raffinement (C1, vérifié par C2) : les étoiles libres deviennent UNE famille globale
- **Lemme (bris d'égalité).** On choisit comme bloc lourd un c qui maximise (w_c, #piv_c) dans l'ordre lexicographique. Si c est
  une étoile libre, la configuration est TOUT-DIS : n_dis = 21, Σ = ∅, et les 7 blocs sont des étoiles libres à d = 12.
- **Preuve.**
  - w_max = d_c ≤ 12, donc tous les w ≤ 12. Or Σw = 84 + 4|Σ| ≥ 84, d'où |Σ| = 0 et w ≡ 12.
  - Un bloc à pivots aurait w = 12 et #piv > 0, et gagnerait le bris d'égalité. Il n'y en a donc aucun. ∎
- **Nouvelle ligne d'arrivée : X / 1 521 + (B).**
  - **(A)** I(τ) pour les 1 521 types À PIVOTS (958 à 2, 407 à 4, 156 à ≥ 6), avec β, SEC/SEC-dis et 2#piv + Σβ ≥ 12.
  - **(B)** La famille globale TOUT-DIS : 7 étoiles libres, SEC-dis partout, et le graphe D est un 2-facteur de KG(7,2). C1 en fait
    son chantier mathématique.
  - Si les étoiles libres tout-SEC-dis sont UNSAT en mono-bloc, (B) tombe aussi par les 1 787 instances locales.

## 7. État du 27/09, fin de matinée
- **(A) = 1 507 types.**
  - L'élimination de Σ est inconditionnelle : les notes 18–19 (RSF/χ = relaxations de l'étage Q, paires non frères libres) ont
    été relues par C2 ; le carnet §7 (Thm D) et §11–13 l'ont été par C1, sans hypothèse « un bloc ».
  - Donc Σ fait partie des 9 motifs, de degré ≤ 2. Les 14 types à ≥ 3 blocs pivots frères sortent : (6,3) 7, (8,3) 2, (8,4) 2,
    (12,3/4/6) 1+1+1. Liste : `logs/finishA_excluded_sigma.json`.
  - Une seconde relecture indépendante est proposée par structures.
- **Organisation des passes sur (A).**
  - Passe 1 : sans preuve, plafond 30 min, ids en ordre aléatoire. Elle sert aussi de calibrage. Journal :
    `logs/finish_A_pass1.log`.
  - Passe 2 : la preuve DRAT (plus drat-trim) n'est rejouée que pour les UNSAT, dans `logs/finish_A.log`. Les preuves atteignaient
    ~3 Go en 24 min : trop gros pour être gardées sur les inconnues.
- **(B) — PL d'orbites réduit par symétrie** (`scripts/sym_alldis.py`) : FAISABLE.
  - G = S₇ ⋉ Z₂²¹, transitif sur les 42 orbites. Réduction exacte : 22 classes de lignes sommées, sur les 6 387 120 colonnes de
    Z₀.
  - Le PL non signé ne tue pas le tout-dis ; il faut les signes et le niveau étiquette (C1).
- **Plan (B) de C1.**
  - Recensement mono-bloc des 1 787 étoiles libres en --beta=all. Échantillon de 20 en cours (`logs/finish_B_freestars.log`).
  - Puis un modèle à deux blocs tout-dis sur les couples survivants.
  - En parallèle : la couche signée du PL et le 7-adique (C1).
- **Outil de symétrie déclarable** (structures, `spec_local.py`, 3dfa451) : spec compilée octet pour octet, invariance vérifiée
  sous les générateurs de Stab, LEX régénéré. Il servira pour les types de (A) restés inconnus sans lex.
