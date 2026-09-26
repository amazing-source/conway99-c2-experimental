# A111111 (3,3) : torsion équilibrée de dimension au plus un et g⁻=20 forcé

26 septembre 2026. **Démontré par certificats entiers, vérifiés par un second programme indépendant**, puis conséquence humaine sur la dimension. Le cas A33 à g⁻=20 reste ouvert.

## Résultat concret

Pour l'étoile A111111 (3,3), les 400 directions projectives de torsion se répartissent en 17 classes. Quinze classes sont exclues par nos nouveaux certificats ; une se ferme par une obstruction élémentaire déjà connue. Il reste **une classe de douze directions**.

Toutes ces directions sont non nulles en chacune des douze coordonnées. Cela donne immédiatement **r₀≤1**, où r₀ est la dimension de la torsion équilibrée. Avec la formule de C1 et son plafond g⁻≤20, on obtient

    r₀=1, ρ=0, g⁻=20.

Ainsi **A111111 (3,3) est impossible à g⁻=16 et à g⁻=18**. Son existence à g⁻=20 n'est pas tranchée. Ni l'involution générale ni l'étoile totalement libre générale ne sont exclues.

L'état précédent de C1 laissait 375 directions mixtes dans treize classes : nos certificats en éliminent **363**, et douze demeurent indécises. Il s'agit d'une exclusion sur toutes les données de cette strate, sans tirage aléatoire de boules.

## 1. Cadre exact

Les douze étiquettes sont 0,…,11 ; σ(i)=i xor 1. Ici μ=σ et

    τ=(0 5)(1 2)(3 4)(6 11)(7 8)(9 10).

Les deux composantes du graphe alterné σ/τ sont C₆ et C₆. Les racines lointaines z sont les soixante paires d'étiquettes de blocs différents, groupées en trente paires z/σz. Les ombres e=Φ(z) parcourent exactement une fois les soixante arêtes de K₁₂−μ.

Les contraintes compactes de structures sont :

    #{z : a∈z, b∈Φ(z)} = K₂[a,b],
    #{z : b∈Φ(z), d∈Φ(σz)} = K₃[b,d],

avec

    K₂[a,b]=2−[a=b]−2[b=σa]−[b=τσa],
    K₃[b,d]=2−[d=σb]−[d=τb]−[d=τσb]−[d=στb].

La bijection et ces deux matrices sont nécessaires dans une vraie SRG avec involution. Le problème traité n'impose aucune absence de prismes.

La torsion est ker₇(I+P_σ+P_τ), de dimension quatre. Sur chaque composante, elle s'écrit

    (a,b,−a−b,a,b,−a−b) mod 7.

Une torsion φ est équilibrée si, pour chaque paire z/σz,

    φ(Φ(z))−φ(Φ(σz))+2[φ(z)−φ(σz)] ≡ 0 mod 7.       (1)

φ(e) désigne la somme des deux valeurs de φ sur une paire e.

Sources des réductions : [C1, note 129](https://github.com/amazing-source/conway99-c1/blob/c4b22393b28cd1f400ab291d3152a3be8d85bf3a/notes/129_Q7_SECTEUR_IMPAIR_INVOLUTION.md) et [structures, formulation compacte](https://github.com/amazing-source/conway99-structures-lab/blob/2e13d68e155d9de862e8d7c8fe14441d11a70184/astra/PROBLEMES_OUVERTS_INVOLUTION.md). Dépôts consultés exclusivement en lecture seule.

## 2. Objet utilisé : les ombres appariées et leur centre

La bijection transporte l'involution sur les soixante arêtes. Une paire e/f est soit sécante, avec un centre b=e∩f, soit disjointe.

K₃[b,b]=2 pour chaque b ; une paire sécante contribue deux à cette entrée. Donc les trente paires d'ombres contiennent exactement **douze paires sécantes, une de chaque centre**, et dix-huit paires disjointes. Ce fait était déjà connu ; l'avancement est de le coupler simultanément à l'usage unique de chaque ombre, aux deux matrices de comptes et au relèvement entier de (1).

Pour une direction projective, choisir un représentant entier

    ψ=(a,b,−a−b,a,b,−a−b ; c,d,−c−d,c,d,−c−d).

Alors les trente charges

    q_z=[ψ(e)−ψ(f)+2(ψ(z)−ψ(σz))]/7

sont entières sous (1). L'énergie exacte, déjà obtenue par C1, est

    Σ q_z² = E(ψ) = 3‖ψ‖²/2.                          (2)

Le nouveau test contraint ces charges et leurs centres **avec toutes les ombres et tous les comptes**, et non par leurs seules sommes séparées.

### Vérification indépendante de l'énergie

Soient Y et W les matrices d'incidence des ombres et des racines, et R la permutation z↔σz. On a

    YYᵀ=9I+J−P_σ,    YRYᵀ=K₃,
    WWᵀ=9I+J−P_σ,    WRWᵀ=J−I+9P_σ,
    WYᵀ=K₂.

Le carré total des charges avant division par 49 est donc

    ψᵀ(YYᵀ−K₃)ψ
      +4ψᵀ(WWᵀ−WRWᵀ)ψ
      +4ψᵀK₂ᵀ(I−P_σ)ψ.

Sur le sous-espace périodique indiqué, ψᵀP_σψ=−‖ψ‖²/2 et (I+P_σ+P_τ)ψ=0. La formule se réduit à 49·3‖ψ‖²/2. Le second programme vérifie aussi cette réduction par arithmétique entière, séparément de la génération des certificats. K₂ n'étant pas symétrique, le produit croisé doit être écrit dans cet ordre ; le vérificateur initial avait une transposition erronée, corrigée avant les sorties finales.

## 3. Forme du certificat : une inégalité par choix d'ombres

Pour chaque paire lointaine Z, on énumère tous les choix ordonnés e/f distincts qui :

- respectent les zéros de K₂ ;
- ne dépassent individuellement aucune capacité de K₃ ;
- vérifient la congruence (1).

Tout choix d'une vraie solution figure dans ce domaine. On ne suppose pas que ces conditions individuelles suffisent à construire une solution.

Un certificat contient des coefficients entiers :

- λ_e pour chacune des soixante ombres ;
- γ_ab et δ_bd pour les deux matrices de comptes ;
- α_b pour les douze centres, α_* pour une paire disjointe ;
- β_Z pour les trente paires lointaines ;
- une échelle entière s, valant 100 ou 1000.

Sur chaque choix admissible, le vérificateur contrôle exactement

    s q_Z² ≥ λ_e+λ_f
              + γ·contribution_K₂(Z,e,f)
              + δ·contribution_K₃(e,f)
              + α_centre + β_Z.                       (3)

En sommant sur une solution, les ombres apparaissent chacune une fois, les centres chacun une fois, les dix-huit paires disjointes chacune avec α_*, et les matrices valent exactement K₂ et K₃. Ainsi

    sE ≥ Σλ + γ·K₂ + δ·K₃ + Σ_b α_b +18α_*+Σ_Z β_Z.

Le membre de droite est le nombre B du certificat. Si B>sE, contradiction. **Aucun arrondi ni calcul flottant n'intervient dans la validité.**

Les coefficients ont été trouvés par une recherche de potentiels entiers et un algorithme d'affectation écrit ici. Leur validité ne dépend ni de la convergence de cette recherche ni de son résultat optimal : le second programme relit chaque colonne et contrôle (3).

## 4. Couverture des directions et sorties exactes

Le groupe qui préserve σ et τ a 72 éléments. Le vérificateur le reconstruit par permutations, puis reconstruit les 400 points de l'espace projectif P³(F₇). Il vérifie que les dix-sept orbites sont disjointes et couvrent tous les points.

| Classe | Taille projective | Multiplicateur du représentant | E | Échelle s | B | Verdict |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 6 | 1 | 6 | 100 | 900 | exclue |
| 1 | 6 | 1 | 18 | 100 | 2000 | exclue |
| 2 | 4 | 1 | 42 | 100 | 4249 | exclue |
| 3 | 18 | 1 | 12 | 100 | 1245 | exclue |
| 4 | 36 | 1 | 30 | 100 | 3021 | exclue |
| 5 | 36 | 1 | 24 | 100 | 2401 | exclue |
| 6 | 72 | 2 | 66 | 1000 | 66014 | exclue |
| 7 | 36 | 1 | 84 | 1000 | 84017 | exclue |
| 8 | 36 | 1 | 78 | 1000 | 78060 | exclue |
| 9 | 9 | 1 | 36 | — | — | domaine impossible, preuve humaine |
| 10 | 36 | 1 | 60 | 100 | 6021 | exclue |
| 11 | 18 | 1 | 96 | 100 | 9659 | exclue |
| 12 | 18 | 1 | 90 | 1000 | 90001 | exclue |
| 13 | 9 | 1 | 36 | 1000 | 36014 | exclue |
| 14 | 36 | 1 | 60 | 1000 | 60019 | exclue |
| 15 | 12 | 1 | 84 | 1000 | 84054 | exclue |
| 16 | 12 | 1 | 84 | 10000 | 839623 | **indécise**, cette borne n'exclut rien |

La classe 6 a été certifiée après multiplication par 2 modulo 7 et choix d'un autre représentant entier périodique. Cela conserve exactement la condition d'équilibre projective. La validité de la nouvelle inégalité et de sa nouvelle énergie est vérifiée séparément.

Pour la classe 9, ψ=(1,1,−2,1,1,−2) sur les deux composantes. Les sommes sur les ombres prennent les résidus {2,3,6}, dont les différences valent {0,1,3,4,6}. Pour z={2,5}, la congruence exige la différence 5, impossible. Cette exclusion reproduit celle de C1 ; elle n'est pas présentée comme nouvelle.

Les quinze certificats ont été vérifiés indépendamment, sur tous les choix admissibles. Les fichiers contiennent les coefficients complets, pas seulement ces nombres.

## 5. Conséquence humaine : la dimension équilibrée s'effondre

La classe restante est représentée par

    φ=(1,2,4,1,2,4 ; 3,5,6,3,5,6) mod 7.

Chaque composante utilise, deux fois chacune, les trois résidus quadratiques non nuls ou leurs opposés. Toutes les douze coordonnées sont non nulles. L'action du groupe et la multiplication scalaire préservent cette propriété.

Soit V₀ l'espace linéaire des torsions équilibrées d'une éventuelle solution. D'après les certificats, tout φ∈V₀ non nul a φ(0)≠0. L'application linéaire

    V₀ → F₇, φ ↦ φ(0)

est donc injective. **dim V₀=r₀≤1.** C'est une preuve humaine, sans classification supplémentaire des plans projectifs.

En contrôle distinct, le programme vérifie que les douze directions restantes ne contiennent aucune des huit directions d'une droite projective entière ; leur intersection avec une telle droite est au plus trois.

Pour A33, t=4. La formule démontrée par C1 donne

    g⁻=18+t−2r₀+ρ =22−2r₀+ρ,   ρ≥0.

Avec g⁻≤20 et r₀≤1, nécessairement

    r₀=1, ρ=0, g⁻=20.

C'est le raccord qui manquait entre l'exclusion finie des directions et un résultat uniforme sur le rang.

## 6. Contrôles, limites et prochaine cible

Les vrais graphes H(2,3) et BvLS passent la bijection et les deux matrices compactes, avec leurs propres paramètres. Ils ne sont pas des étoiles A33 : on ne leur applique pas cette exclusion.

La recherche de la classe 16 n'a produit ni certificat d'impossibilité ni solution intégrale de Φ. Une borne 83,9623 pour une énergie imposée de 84 est **insuffisante**, quelle que soit sa proximité. La restriction multiplicative F₇× est une tentative supplémentaire ; elle n'autorise aucune conclusion générale si elle échoue.

Le verrou s'est réduit à une direction équilibrée unique, de type résidus quadratiques opposés, avec g⁻=20 et ρ=0. La prochaine question porte sur la réalisation de ses soixante ombres, ou sur la compatibilité de ces conditions avec le résidu lointain et les autres blocs. Les étoiles totalement libres à t=0 et les autres types ne sont pas fermés par ce résultat.

Fichiers : [certificats_A33.json](certificats_A33.json) ; [verifier_A33_independant.py](verifier_A33_independant.py) ; [chercher_certificat_A33.py](chercher_certificat_A33.py) ; [sorties_A33_independantes.txt](sorties_A33_independantes.txt). Les programmes ont tourné à distance sur SageMathCell. Aucun SAT, CP, PLNE ou solveur externe n'a été utilisé ; aucun calcul lourd local ni dépôt distant modifié.
