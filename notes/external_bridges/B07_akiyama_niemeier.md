# B07 — Non-existence de srg(266,45,0,9) par un réseau de Niemeier (Akiyama, arXiv 2609.08319, 8 sept. 2026)

- **Source** : K. Akiyama, *Nonexistence of a Strongly Regular Graph with Parameters (266,45,0,9): A Certificate-Free Lean Proof*.
  Lu via la page HTML d'arXiv (résumé technique, non vérifié ligne à ligne).
- **Mécanisme** : argument de **classe** de réseau, au-delà du genre.
  1. Le second sous-constituant (220 sommets) donne L = 9I + 3J − S − 3H, de valeurs propres 165¹ et 45¹¹ : un réseau entier de rang 12 avec
     centroïde entier (radical calculé modulo 11).
  2. Forme lorentzienne [v,w] = ⟨v,w⟩ − h(v)h(w), puis u_y = g_y − ρ/4 : **repère serré** de 220 vecteurs dans R¹¹ (constante 45).
  3. « D₇ marqué » : t_y = (u_y, s) avec s = (½)⁷, de norme 4 et ⟨t_y,t_z⟩ = L_yz + 1. On complète en un réseau pair unimodulaire de rang 24
     (réseau de Niemeier).
  4. Identité harmonique de Venkov : Σ_r ⟨r,v⟩⟨r,w⟩ = |R|/12·⟨v,w⟩. Avec l'isolation des racines (220 > 180), elle force A₁₁D₇E₆, puis
     une identité de projection impossible 4x + 4y − 2z = 50.
- **Analogue C2** :
  - L₋ (Gram 3I − S, rang 22) : 49 vecteurs (7 intérieurs de norme 4, deux à deux orthogonaux ; 42 extérieurs de norme 3, qui se projettent
    sur −¼·C_o, motifs de racines de D₇). Repère serré de constante 7.
  - Sa partie W₁₅ : 42 vecteurs z_o = 2w_o de norme 10, Gram 12I − 4S_out − G, **réseau pair de rang 15**, repère serré de constante 28.
  - L₊ (Gram S + 4I, rang 27).
  - Le « D₇ marqué » est naturel ici : les blocs sont les coordonnées de Z⁷.
- **Verdict** : HEURISTIQUE défavorable. La méthode exige un repère **épais** (220 vecteurs en dimension 11, soit 20 par dimension), qui
  sert à l'isolation des racines. Les repères de C2 sont **minces** (49 en dimension 22, 42 en dimension 15). Dans le graphe 99 tout entier,
  les sous-espaces petits (V₋₂, V₀ de H) sont explicites (blocs) et ne portent aucune information ; l'inconnu vit dans des espaces
  propres de grande dimension.
  À garder pour un cas où ρ_S serait connu (si ρ_S = 20, L₋ a pour déterminant 49 et admet un complément de rang 2 vers le rang 24).
- **Test possible** : si l'étage S seul a des solutions, calculer ρ_S, le minimum de L₋ et le réseau pair de rang 15 sur ces solutions.
