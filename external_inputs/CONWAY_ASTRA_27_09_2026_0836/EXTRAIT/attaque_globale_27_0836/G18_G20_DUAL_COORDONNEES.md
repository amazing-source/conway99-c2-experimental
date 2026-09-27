# Axes courts duaux : coupe de coque et fermeture D11 en rang24

## Lemme commun de trois directions

Les42 generateurs de norme3 engendrent integralement le reseau physique N ; voir [G18_G20_QUARANTE_DEUX_GENERATEURS.md](G18_G20_QUARANTE_DEUX_GENERATEURS.md). On garde la borne duale acquise min(N*)>=8/7. Si w est un vecteur reel de norme<=1 dont les produits avec ces42 vecteurs sont ENTIERS, alors proj_N(w) appartient a N* et a norme<=1. Cette projection est donc nulle.

Dans une extension de dimension<=24, trois tels w lineairement independants sont impossibles, car ils seraient contenus dans N^perp, de dimension<=2. Cela ne suppose pas que w appartient au reseau ambiant.

La forme globale du piege de coque est immediate : si toute la coque3 d'un reseau ambiant appartient aux coordonnees entieres d'un repere orthonormal, ses axes ont produits entiers avec toute selection des42 u. Les24 axes seraient orthogonaux a N. Cette enveloppe ne peut donc porter le frame physique. D8^3, dont la coque3 est composee de triples unites entieres, est une famille fermee par ce principe, sans les caracteristiques8 ni les normales.

## Une seule composante D4 uniforme en classe suffit

Pour D4, les trois classes minuscules v,s,c de norme1 sont chacune composees de quatre paires d'axes orthonormaux. Elles peuvent se realiser par les axes standards, ou par les lignes d'un Hadamard4 divise par2, avec la parite voulue.

Si les projections des42 u sur UNE composante D4 appartiennent a0 et une seule de ces classes, choisir ses quatre axes. Leurs produits avec tous les u sont entiers. Le lemme les rend orthogonaux a N, impossible en codimension<=2. Les projections de classe0, lorsqu'elles sont considerees, restent aussi entieres apres trialite.

Donc chaque composante D4 d'un collage candidat doit utiliser au moins DEUX classes parmi les42 vecteurs effectivement selectionnes. Un melange dans la coque ambiante complete ne suffit pas : il faut le garder dans la selection physique. Cette coupe ne ferme pas tous les D4^6 ; une enveloppe D4^6 avec plusieurs classes reste possible.

## Nouvelle fermeture D11 dans toute extension integrale de dimension<=24

Soit E l'espace d'un D11 de roots du collage L. Les projections des42 u sont0,+/-e_i ou des spinors de norme11/4 : le lemme minuscule acquis donne cette liste.

Si aucune projection n'est spinorielle, les onze axes e_i ont produits entiers avec les42 u. Ils seraient tous dans N^perp, contradiction. Il existe donc u=p+b, p dans E un spinor, b dans E^perp, avec

    p^2=11/4, b^2=1/4.

On a4p dans D11, donc4b=4u-4p appartient a L. Poser e12=2b comme AXE EUCLIDIEN de norme1 ; il n'est pas suppose appartenir a L. Les onze coordonnees de2p valent+/-1. Pour chaque i, le vecteur2p-e_i a somme entiere paire et appartient a D11. Alors

    2u-(2p-e_i)=e_i+e12

est une root de norme2 de L. Lui soustraire4b=2e12 donne aussi e_i-e12 dans L. Avec les roots D11, ces roots engendrent le D12 standard dans l'espace E plus Rb.

Mais D12 dans un collage de dimension<=24 portant le frame est DEJA exclu par la preuve0803, [G18_G20_D12_COLLAGE.md](../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md). Contradiction. Ainsi aucun D11 ne peut figurer non plus : tous les D_n de rang n>=11 sont fermes dans ces extensions de rang<=24.

Ce raccord a ete relu independamment par g18_audit_neuf. Il ne suppose ni que2b est un vecteur du reseau, ni que L est indecomposable, ni que D11 est contenu dans N. Il n'exclut pas D10 ni toutes les racines mixtes, et ne ferme pas les genres g18/g20.
