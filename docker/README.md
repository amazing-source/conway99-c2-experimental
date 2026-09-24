# Images Docker du labo

Ces Dockerfiles sont **reconstruits** à partir de `docker history --no-trunc` (sorties dans `logs/docker_history_*.txt`). Les images
d'origine sont encore sur le poste du 24/09/2026 (identifiants dans `logs/docker_images.txt`). Les Dockerfiles n'ont pas encore été
reconstruits pour vérification.

Les solveurs sont clonés à HEAD, comme à l'origine. Versions de l'image d'origine : kissat 4.0.4 et cadical 3.0.1.

```
docker build -t satbox         -f docker/Dockerfile.satbox docker
docker build -t satbox-proof   -f docker/Dockerfile.satbox-proof docker
docker build -t satbox-breakid -f docker/Dockerfile.satbox-breakid docker
docker build -t satbox-cnc     -f docker/Dockerfile.satbox-cnc docker
docker build -t c99py          -f docker/Dockerfile.c99py docker
```

| Image | Contenu | Usage |
|---|---|---|
| `satbox-proof` | kissat, cadical, drat-trim | certification DRAT (`scripts/cert_run.sh`) |
| `satbox-breakid` | kissat, cadical, BreakID | nuits C et D |
| `satbox-cnc` | march_cu | cube-and-conquer |
| `c99py` | pysat, numpy, sympy, ortools | scripts Python en conteneur |
