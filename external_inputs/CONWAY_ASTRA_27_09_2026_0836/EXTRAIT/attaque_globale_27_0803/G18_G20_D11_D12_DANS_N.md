# Aucun D_n de rang au moins11 dans le reseau commun de rang22

## Hypotheses et provenance

M est une surlattice INTEGRALE de meme rang22 contenant le frame physique N. On garde les sept h_c de norme4, les42 u_p de norme3, les incidences D7 et l'operateur commun7I sur cet espace reel22. La borne duale de N donne min(M)>=2. Le meme frame rend M indecomposable ; les preuves independantes sont [INDECOMPOSABILITE_GLOBALE.md](INDECOMPOSABILITE_GLOBALE.md) et [AUDIT_INDECOMPOSABILITE.md](AUDIT_INDECOMPOSABILITE.md).

Chaque u_p a produit0,+1 ou-1 avec les racines de M. Pour un D_n dans un espace E, sa projection est donc0,+/-e_i, ou un demi-vecteur dont toutes les valeurs absolues sont1/2. La derniere norme est n/4. Ces reductions sont detaillees dans [G18_G20_D13_FRAME.md](G18_G20_D13_FRAME.md).

On traite ici D11 et D12. Le cas n>=13 est deja ferme par la trace, puisque les demi-vecteurs auraient norme>3. Aucun determinant49, type W ou P0 n'est necessaire.

## La trace force une projection spinorielle

Sans demi-vecteur parmi les projections des42 u, leur contribution totale est au plus42, celle des sept h au plus28. Mais E est dans le meme espace reel22 : le frame sur E a trace7n. Pour n=11 ou12, 7n est77 ou84, strictement superieur a70.

Il existe donc un generateur u=p+b, avec p dans E un demi-vecteur et b dans E^perp.

## D12

On a p^2=3=u^2, donc b=0. Le reseau P=D12+Z u est integral, de rang12. La classe de u a ordre2 modulo D12, et det(D12)=4 ; ainsi det(P)=4/2^2=1.

Un sous-reseau integral unimodulaire P se detache de M : les projections de chaque vecteur de M appartiennent a P*=P, donc M=P orthogonalement somme Q. Comme P a rang12<22, c'est une decomposition non triviale, contraire a l'indecomposabilite acquise.

## D11

Ici p^2=11/4 et b^2=1/4. Dans le modele D11={z dans Z11 : somme z_i paire}, 4p appartient a D11, tandis que2p n'y appartient pas. Puisque u et4p appartiennent a M, 4b=4u-4p appartient a M et a norme4.

Le reseau de base

    R=D11 orthogonalement somme Z(4b)

a rang12 et determinant4*4=16. Le vecteur u=p+b a ordre exactement4 modulo R : 4u appartient a R, tandis que les multiples1,2,3 ont une composante orthogonale b,2b,3b qui n'est pas un multiple entier de4b.

Ainsi P=R+Z u est integral, d'indice4 sur R, et det(P)=16/4^2=1. Il se detache de M comme dans le cas precedent, donnant encore une decomposition non triviale. Contradiction.

## Conclusion et limite de transport

Il n'existe aucun sous-systeme D_n de rang n>=11 dans M. Cela s'applique a N et a Nmax, puisque le raisonnement ne requiert que l'integralite et le meme espace de rang22 contenant le frame. La preuve des deux petites branches a ete relue independamment par g18_audit_neuf, qui a confirme les ordres2/4, les determinants et le raccord par indecomposabilite.

On ne transporte PAS cette indecomposabilite a un collage de rang24. La preuve specifique [G18_G20_D12_COLLAGE.md](G18_G20_D12_COLLAGE.md) y exclut D12, meme si le collage a des normes1 ; D11 en rang24 reste ouvert par les arguments presents. Aucun genre g18/g20 entier n'est exclu par cette note.
