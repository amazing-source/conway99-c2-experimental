# Exclusion uniforme des enveloppes contenant D8^3

**Statut : preuve adverse et petit controle exact independants acquis.** Le resultat porte sur une enveloppe integrale unimodulaire impaire U de rang24 portant le repere physique42+7, pas sur tous les reseaux unimodulaires. Les reseaux D8^3 construits existent ; c'est leur repere physique qui est impossible.

## 1. Reduction par les classes de la coque de norme3

Le discriminant de R=D8^3 est F2^6. Dans chaque composante les classes s,c ont norme minimale2, v=s+c a norme minimale1, et le produit2b est symplectique avec b(s,s)=b(c,c)=0 et2b(s,c)=1. Le collage H=U/R est un Lagrangien de dimension3.

Les normes1 sont interdites. Une singleton spinorielle ajoute E8 et deux classes vectorielles ajoutent D16 ; ces deux familles sont deja exclues dans une enveloppe portant le repere physique. Il reste a examiner la coque3. Puisque le repere contient des u de norme3 et R est pair, une classe de minimum3 existe. Les seules classes possibles sont vvv ou un v et un spinor dans deux composantes.

Si vvv appartient a H, aucune classe v-spinor n'est orthogonale a elle : les classes de coque3 se reduisent donc a vvv. Toute composante D8 voit exclusivement v dans la coque3.

Sinon fixer a=(v,s,0), apres permutation et echange s/c. Une autre classe3 avec un centre vectoriel deplace est soit non orthogonale a a, soit donne par addition deux classes vectorielles (D16), soit est de la forme(s ou c,v,0). Ce dernier cas remplit un Lagrangien sur les deux premieres composantes. Tout prolongement de dimension3, apres soustraction des deux premiers generateurs, ajoute une singleton sur la troisieme composante, donc une norme1 ou E8. Ces alternatives sont exclues. Toutes les classes3 ont ainsi le meme centre vectoriel. La coque3 complete voit seulement0/v dans cette composante D8.

## 2. Le piege polaire ferme le repere physique

Les42 u engendrent N integralement, par la relation des soeurs D7 deja prouvee. Une composante D8 dont les projections de la coque3 sont0 ou+/-e_i fournit huit directions orthogonales de norme1 ayant produits entiers avec tous les42 u.

Leurs projections sur N appartiennent a N*. Le gap dual8/7 les force nulles. Elles devraient donc toutes appartenir a N_R perpendiculaire, de dimension2 dans U, contradiction. L'argument n'exige ni caracteristiques8 ni indice de sous-reseau de coordonnees ; il s'applique uniformement aux deux valeurs g18/g20 et sans P0.

## 3. Certificat fini independant

verifier_collages_D8_independant.mjs construit les sous-espaces par extension symplectique et les canonise par leurs listes completes de vecteurs. Il n'utilise ni le RREF de l'agent, ni les fichiers de collage du parent. Les135 Lagrangiens se repartissent en30 pairs et105 impairs. Dans les105 impairs, le filtre ordonne rejette37 normes1,24 singleton spinor/E8 et12 doubles vectoriels/D16. Les32 restants sont8 collages dont la coque3 a seulement vvv et24 dont les deux classes v-spinor ont le meme centre vectoriel. Chacun a4096 vecteurs de norme3 et au moins une composante entierement0/v.

Le meme source controle les13 minima de classes3 et toutes leurs paires orthogonales a centres deplaces. Ce dernier controle ne remplace pas le raisonnement de prolongement Lagrangien ; il en verifie les seules alternatives locales.

Les comptes concordent avec les deux autres voies. Aucun classement de tous les reseaux impairs de rang24, aucune borne universelle de rang du Gram de coque, ni aucune fermeture globale g18/g20 n'est invoque.
