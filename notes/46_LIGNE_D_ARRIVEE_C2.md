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
