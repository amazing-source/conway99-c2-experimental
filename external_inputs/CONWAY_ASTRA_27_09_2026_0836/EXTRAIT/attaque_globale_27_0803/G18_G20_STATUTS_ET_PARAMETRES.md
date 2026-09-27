# Statuts des coupes uniformes et parametres des controles positifs

Toutes les nouvelles pieces ci-dessous utilisent les memes49 generateurs dans le meme espace N de rang22. Elles ne recollent pas des etoiles independantes. Dans une extension de rang superieur, l'operateur du frame vaut7P_N, jamais7I sur l'extension entiere.

## Familles fermees et branches restantes

| Objet | Resultat acquis | Hypotheses supplementaires / portee |
|---|---|---|
| Borne duale | min(N*)>=8/7 ; toute norme1 d'une extension integrale est orthogonale a N | Borne ancienne, raccord physique audite ; aucune nouveaute revendiquee |
| Indecomposabilite | N et toute surlattice integrale de meme rang22 sont indecomposables | Meme frame D7 ; min>=2 vient de la borne duale |
| E8 | Aucun E8 dans une extension integrale de dimension<=29 | Minuscule + les42 u engendrent N reel ; pas de minimum2 suppose pour l'extension |
| D_n dans rang22 | Aucun D_n pour n>=11 | Trace + facteur unimodulaire + indecomposabilite |
| D_n dans rang<=24 | Aucun D_n pour n>=12 | D12 traite separement les branches spinorielle et non spinorielle ; D11 reste ouvert |
| A_n dans rang22 | Aucun A_n pour n>=20 | Trace rationnelle, produits minuscules |
| A_n dans rang<=24 | Aucun A_n pour n>=22 | Meme trace avec defaut commun au plus2 ; A20/A21 restent ouverts |
| Racines, rang total | Rang<=20 dans Nmax et N | Det(Nmax)=49 et discriminant7 elementaire de dimension2, plus les preuves independantes du plein rang et du corang1 |
| Coefficient lourd d'une norme2 | Si un coefficient double est present : il est unique et interieur ; six racines incidentes et quatre externes ; tous les autres interieurs nuls | Reflexion et parite, sans P0 ; le cas plat reste ouvert |
| Carrier lourd | Les quatre supports externes sont distincts et leur graphe simple a degre maximal3 | P0 seulement pour cette annexe ; les regimes restants ne sont pas fermes |

La borne de rang des racines a ses propres hypotheses de determinant/discriminant, exposees dans [AUDIT_RACINES_CORANG_UN.md](AUDIT_RACINES_CORANG_UN.md). La table ne remplace aucune de ces hypotheses par une consequence implicite du genre.

Sources des nouvelles familles : [E8](G18_G20_E8_MINUSCULE.md), [D>=13 par trace](G18_G20_D13_FRAME.md), [D11/D12 de meme rang](G18_G20_D11_D12_DANS_N.md), [D12 en rang24](G18_G20_D12_COLLAGE.md), [A>=20 par trace](G18_G20_A20_FRAME.md), [regimes lourds](G18_G20_LOURD_REGIMES.md) et [carrier P0](G18_G20_CARRIER_LOURD_P0.md). Chaque source JS joint ne controle que les etapes finies annoncees ; aucune sortie ne pretend reconstruire un SRG.

## Parametres anonymes du cadre signe

Pour les positifs, on garde leurs propres parametres. Dans le cadre signe general, ecrire S=[-I_m,C;C^t,T], avec valeurs propres r et-(r+1). Poser

    H=rI-S, H^2=(2r+1)H,
    ||h_c||^2=r+1, ||u_p||^2=r,
    r h_c + somme_p C_cp u_p=0,
    CC^t=2(m-1)I=r(r+1)I.

La relation entre m et r vaut pour les exemples physiques ici controles, pas pour une matrice arbitraire. Le nombre de colonnes racines est m(m-1), et le rang reel du frame est

    rank(H)=m(1+mr)/(2r+1).

| Controle | Sommets | m | r | Constante du frame | Normes h/u | Rang H |
|---|---:|---:|---:|---:|---|---:|
| H(2,3) | 9 | 2 | 1 | 3 | 2 / 1 | 2 |
| Hypothese SRG99 | 99 | 7 | 3 | 7 | 4 / 3 | 22 |
| BvLS | 243 | 11 | 4 | 9 | 5 / 4 | 55 |

[controles_positifs_cadre_global.mjs](controles_positifs_cadre_global.mjs) reconstruit les deux graphes positifs et controle leurs vrais comptes communs, le polynome de S, le frame et les incidences. Son resultat existant est exact=true :36 paires du petit graphe et29403 paires BvLS. Aucun nouveau calcul positif n'est necessaire pour cette cloture documentaire.

Ces positifs valident la normalisation du cadre. Ils ne satisfont pas les hypotheses norm3/norm4/constante7 des exclusions ci-dessus : H(2,3) possede des normes1, et BvLS a des generateurs racines de norme4. On ne leur impose donc ni min(N*)>=8/7, ni determinant49, ni premier7, ni P0, ni les bornes E8/D/A specifiques au frame SRG99.

## Ce qui n'est pas prouve

Aucune borne g>=21, aucune exclusion uniforme des genres g18/g20, aucun graphe certifie, aucune fermeture des classes de racines plus petites n'est produite. Le contre-modele d'enveloppe Golay de rang22 et determinant49 reste coherent avec les contraintes de genre citees : il ne porte pas de frame physique49 construit. Le verrou restant est donc l'existence simultanee du frame, de ses incidences D7 et des produits entiers des42 colonnes ; il ne suffit pas de repeter les seules contraintes de genre.
