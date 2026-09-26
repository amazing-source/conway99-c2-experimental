# A111111 (3,3) entièrement exclue

**Résultat démontré, vérifié par deux implémentations.** Une involution de srg(99,14,1,2) ne peut avoir cette étoile. P=0 n’est pas utilisé.

Le bloc connu a rang14 modulo7 et discriminant carré, donc une partie non scindée. Sa complétion dans l’espace global hyperbolique impose g⁻≥24−2r₀. Nos certificats antérieurs donnent r₀≤1 ; le genre donne g⁻≤20. Contradiction.

Le cas qui restait ouvert, r₀=1,ρ=0,g⁻=20, est donc fermé. C’est le signe du résidu qui manquait au seul calcul de rang.

[Preuve complète](PREUVE.md) · [Vérificateur indépendant et contrôles](verifier_signe_et_controles.py) · [Second calcul du signe](verifier_signe_sage.py) · [Sorties exactes](sorties_independantes.txt).

Contrôles H(2,3) et BvLS : décomposition de Witt, rangs et discriminants reproduits ; aucune fausse exclusion. La vérification de la bijection entre les quatre torsions locales et les conditions d’ombres est incluse.

Les autres étoiles sans classe fermée, les carrés disjoints et l’involution générale restent ouverts. Normes9/10 sur six et sept blocs : aucune nouvelle fermeture ici. L’automation reste active.
