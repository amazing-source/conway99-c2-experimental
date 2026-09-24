# conway99-c2-experimental

Laboratoire expérimental de la branche **C2** du graphe 99 de Conway : un srg(99, 14, 1, 2) muni d'une involution t qui fixe un seul
sommet x.

- **Page de synthèse** (privée) : https://claude.ai/artifact/4sjNU9k9WjvPxnuFzjqu55. Sa source est dans `rapport/c2_lab.html`.
- **Pour reprendre** : `REPRISE.md`, qui contient l'état, les commandes, l'historique des calculs et un message de reprise pour une
  nouvelle session.

## État (24/09/2026)

- **Rien n'est tranché** : ni existence, ni non-existence.
- **ÉTABLI (certifié, 20 preuves DRAT vérifiées)** : le graphe Σ des grilles passant par x est l'un de 53 graphes, donc au plus 7
  grilles passent par x.
- **Mouvement en cours** : t est la réflexion ponctuelle σ_x d'une famille définie en tout sommet. C2 est « de Hall en un seul
  point ».
  - Le lemme manquant est la **propagation (P)** : obtenir une deuxième réflexion automorphe. Il équivaut à la mort de C2.
  - Il est bloqué par un résidu de dimension 30 : le 1-voisinage n'engendre que 14 des 44 dimensions de V₋₄.
  - Voir `notes/14_MECANISMES_PROFONDEUR.md`.

## Démarrage rapide

```
gh repo clone amazing-source/conway99-c2-experimental
cd conway99-c2-experimental
py -3.12 -m venv .venv
.venv\Scripts\pip install -r requirements-lab.txt
```

Ce qui n'est pas versionné se régénère :
- les CNF, via `scripts/make_cnf.py` et `scripts/stage_s_cnf.py`, avec leurs empreintes dans `data/cnf/MANIFEST*.txt` ;
- les images Docker, via `docker/` ;
- les clones externes, dont les adresses et commits sont dans `logs/external_c3_commits.txt`.

## Arborescence

| Chemin | Contenu |
|---|---|
| `REPRISE.md`, `SYNTHESE.md` | point d'entrée ; tous les résultats avec leur statut |
| `JOURNAL.md`, `IDEES.md`, `NEGATIVE_RESULTS.md` | journal chronologique ; idées I-01 à I-30 ; résultats négatifs N01 à N15 |
| `notes/` | preuves et analyses (00 à 14), ponts externes (`external_bridges/`) |
| `scripts/` | modèles SAT et CP-SAT, contrôles (BvLS, Paley), calculs exacts ; `scripts/vendor/` pour les modèles de base |
| `data/` | résultats de certification, tables BvLS, sorties JSON (sans les CNF) |
| `logs/` | journaux de calcul, instantanés de vérification des dépôts en lecture seule |
| `downloads/` | articles et textes extraits (usage de recherche) |
| `docker/` | Dockerfiles reconstruits des images de solveurs |
| `rapport/` | source HTML de la page de synthèse |

## Règles du labo

- `conway99-involution` et `conway99-lab-archive` sont **strictement en lecture seule** : aucun fichier modifié, aucune opération git.
- Aucune mémoire ni note permanente du projet principal n'est modifiée. Aucune autre branche Conway 99 n'est consultée.
- Pas de calcul SAT ou CP-SAT de plusieurs heures.
- Étiquettes de statut : ÉTABLI, DÉRIVÉ, OBSERVÉ, CONJECTURE, HEURISTIQUE, SPÉCULATION, RÉFUTÉ.
- Liberté maximale pour inventer, rigueur maximale pour conclure.
