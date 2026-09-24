# B05 — Compléments étoilés (star complements) et graphes de compatibilité

**Source.** Azarija–Marc, *There is no (75,32,10,16) strongly regular graph*, LAA 557 (2018), arXiv 1509.05933 (texte local
`downloads/azarija_marc_75_32_10_16.txt`) ; Cvetković–Rowlinson–Simić (théorie des star sets).

**Problème d'origine.** Non-existence de srg(75,32,10,16) (donc de pg(4,7,2), de deux-graphes réguliers à 76 sommets).

**Mécanisme.** Valeur propre r de grande multiplicité f ⇒ complément étoilé H d'ordre n−f (r n'est pas valeur propre de H). Le reste du graphe est
reconstruit par des vecteurs u ∈ {0,1}^{n−f} avec ⟨u,u⟩ = r, ⟨u,v⟩ ∈ {−1,0} (⟨u,v⟩ = u(rI−A_H)^{-1}vᵀ) : le graphe existe ssi le graphe de compatibilité
a une f-clique. On construit une grosse structure induite forcée, on l'étend en complément étoilé (élagage par **entrelacement partitionné**), puis
recherche de clique maximale.

**Objet C2.** Le quotient signé S (49 sommets, valeurs propres 3²⁷, (−4)²²) : un complément étoilé pour 3 a **22 sommets** et peut contenir les 7 sommets
intérieurs (bloc −I₇, sans valeur propre 3). Les vecteurs d'extension ont leurs 7 coordonnées intérieures **imposées** (ligne C_U) ; restent 15
coordonnées dans {0,±1}. Condition : b_Uᵀ(3I−X)^{-1}b_U = 3, b_Uᵀ(3I−X)^{-1}b_V = −S_UV ∈ {0,±1}. Pour −4 : complément de 27 sommets.

**Test rapide.** À faire : sur BvLS (m=11), vérifier la reconstruction à partir d'un complément étoilé contenant les intérieurs ; compter les vecteurs
candidats par orbite.

**Verdict.** Représentation réellement différente (reconstruction spectrale) mais reste une recherche ; intéressant seulement si un complément étoilé
*canonique* (forcé) existe. Idée I-ETOILE (priorité moyenne).
