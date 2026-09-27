# Bilan de l'audit independant 0836

Les preuves et controles de ce dossier concernent le meme repere physique de42 vecteurs u de norme3 et sept vecteurs h de norme4, dans une enveloppe unimodulaire impaire de rang24, avec deux normales de norme7. Le terme racine de reseau designe ici un vecteur de norme2. Aucun registre de types locaux, aucun resultat de foret et aucun fichier ancien n'a ete modifie.

| Resultat acquis | Portee exacte |
| --- | --- |
| Toute enveloppe impaire unimodulaire24 de minimum>=2 a48+r caracteristiques de norme8 | r est le nombre total de racines de norme2 de l'enveloppe ; preuve theta/Poisson et dimension par norme modulaire |
| Moments des caracteristiques8 et de la coque3 | M_chi=(16+r)I-8R et M_coque3=(512+2r)I-24R, R somme des operateurs de TOUTES les racines de l'enveloppe |
| Si l'enveloppe est sans racines, les48 caracteristiques8 donnent24 ombres orthogonales | Le template commun devient necessaire ; code autodual doublement pair[24,12,8], sans unicite de Golay invoquee |
| Les42 u engendrent N integralement | Relation entiere utilisant deux soeurs D7 et les coefficients2 et3 ; aucun transport aux constantes p3 des controles positifs |
| D11 est impossible dans l'enveloppe portant le repere | Un spinor physique fournit de vraies racines D12 ; la direction2b n'est pas supposee dans le reseau |
| Toute enveloppe contenant D8^3 est impossible pour le repere | Classification135 Lagrangiens ; les32 collages restants ont une composante0/v dans toute la coque3, contredisant le petit polaire de dimension2 |
| Tout collage impair D6^4 admissible pour le repere se reduit au cycle4 | Classification135 codes binaires ; les boucles donnent norme1 et les doubles aretes D12 |
| Six blocs spinoriels sur une meme paire opposee D6 sont impossibles | Le cas mixte2+4/4+2 n'est pas ferme par cette preuve |
| Dans le regime4AC+2BD avec h7 entier dans AC, les quatre centres AC sont distincts et se partagent2B+2D | Coupe de repetitions puis orthogonalite ; regime entier non ferme |
| Sept octades de rang binaire<=4 forcent leur octade de multiplicite1 dans leur span | La paire de normales0803 viole cette condition ; aucune exclusion si l'octade est dans le code, ni pour les rangs5..7 |
| Congruences de selection Q42 | Les24 conditions de lignes se reduisent a un mot ; XOR, code et checksum sont controles sur deux temoins fixes non physiques |

## Limites et contre-controles

Le moment candidat M_shadow=4I+R a ete falsifie par le vrai reseau E8 orthogonal U16. La formule correcte est M_shadow=(4+r/4)I-2R. Avec des racines, une coque de caracteristiques8 ne fournit pas automatiquement un repere d'ombres orthogonales.

Les collages D6^4/C4 et D4^6/C6 ont4096 vecteurs de norme3 dont le Gram complet a rang24 modulo2. Ils sont des contre-controles a une borne universelle20 de coque ; ils ne fournissent pas de selection physique42+7. Le minimum du reseau est2, distinct du minimum3 des classes ajoutees.

Le code de rang24 rootless et ses octades sont necessaires sous l'hypothese sans racines. Les congruences Q, checksum, code et budgets ne sont pas presentees comme une contradiction globale. La classification des autres enveloppes et le verrou de la meme selection physique restent ouverts. Aucune cloture g18 ou g20 globale n'est annoncee.

## Verification et provenance

Onze sources Node propres ont ete executes avec sortie exacte. Les series sont tronquees seulement pour les controles de normalisation ; les preuves analytiques de dimension et de Poisson sont dans les notes, et ne sont pas deduites d'une troncature. Les petites enumerations finales ont ete completes :135 codes D6,135 Lagrangiens D8,1716 distributions de six centres,1365 distributions de quatre centres. Aucun solveur, Python local, depot ou Web n'a ete utilise.

Les vrais controles H(2,3) et BvLS du dossier0803 sont conserves et lies en lecture seule. Leurs parametres r=1,d=3 et r=4,d=9, normes u=1 et4, h=2 et5, restent distincts des constantes99. Ils ne sont soumis ni a F7, ni a P0, ni aux regles de purete de norme3.

MANIFEST_AUDIT_INDEPENDANT_0836.json lie les onze notes, onze sources, onze resultats, ce bilan et son constructeur. Chaque resultat porte exact=true et le SHA de son source. Les dependances anciennes et le seul fichier de temoins de selection sont lies separement ; leurs contenus n'ont pas ete modifies.
