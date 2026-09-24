# B03 — Paramètres de Krein, schémas de translation, nombres d'intersection triples

**Sources.** Cameron–Goethals–Seidel ; Coolsaet–Jurišić (JCTA 2008, « Using equality in the Krein conditions… ») ; Vidali (symbolic computation,
EJC 25(4) 2018) ; schémas de translation : paramètres de Krein = nombres d'intersection du schéma dual (donc entiers ≥ 0).

**Mécanisme.** Si q^k_ij = 0, combinaison linéaire nulle des nombres d'intersection triples → énumération → contradiction.

**Calcul (`scripts/krein.py`, CALCULÉ).** Pour srg(2m²+1,2m,1,2) :
| m | d = r−s | q¹₁₁ | q²₂₂ |
|---|---|---|---|
| 2 | 3 | 1 | 1 |
| 7 | 7 | 1629/49 | 649/49 |
| 11 | 9 | 81 | 37 |
| 56 | 21 | 90733/49 | …/49 |
| 497 | 63 | …/49 | …/49 |
Aucun q nul (pas de mécanisme CGS). **Dichotomie OBSERVÉE** : les paramètres de Krein sont entiers exactement pour les cas existants
(d ∈ {3, 9}, schémas de translation sur F₃^k) et ont dénominateur 7² pour les trois cas ouverts (7 | d). Rappel (DÉRIVÉ) : les paramètres admissibles
de srg(n,k,1,2) sont exactement d | 63, d ∈ {3,7,9,21,63} ; existants : d ∈ {3,9} ; ouverts : 7 | d.

**Analogue C2.** Nombres d'intersection triples pour les triplets (x, u, σu) : [111] = 0 forcé. Rien de plus sans Krein nul.

**Verdict.** Pas d'obstruction directe. HEURISTIQUE forte : « 7 est le premier de l'obstruction » ; toute obstruction uniforme devrait être 7-adique
(et tomber sur m = 7, 56, 497 mais pas sur m = 2, 11). Motive l'idée I-7ADIQUE.
