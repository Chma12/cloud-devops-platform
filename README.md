# Cloud & DevOps Platform
![CI](https://github.com/chma12/cloud-devops-platform/actions/workflows/ci.yml/badge.svg)

Projet personnel : une API REST (Task Manager) dont l'intérêt est le cycle
DevOps complet autour : tests, conteneurisation, CI/CD, déploiement AWS,
Infrastructure as Code (Terraform) et monitoring.

## Stack
Python · FastAPI · SQLite · Pytest · Docker · GitHub Actions · AWS · Terraform · Prometheus · Grafana

## Lancer l'application en local
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload

Documentation interactive : http://127.0.0.1:8000/docs

## Endpoints
| Méthode | Endpoint | Fonction |
|---|---|---|
| GET | /health | État de l'API |
| POST | /tasks | Créer une tâche |
| GET | /tasks | Lister les tâches |
| GET | /tasks/{id} | Consulter une tâche |
| PUT | /tasks/{id} | Modifier une tâche |
| DELETE | /tasks/{id} | Supprimer une tâche |

## Tests
    pytest -v

Les tests utilisent une base SQLite en mémoire (fixture dans `tests/conftest.py`),
isolée de la base de développement. Ils couvrent le /health, le CRUD complet
et les cas d'erreur (404 et validation 422).
## Docker
    docker build -t task-manager-api:1.0 .
    docker run -d --name task-manager -p 8000:8000 \
      -v task-data:/data task-manager-api:1.0

- L'application tourne avec un utilisateur non-root.
- La base SQLite est stockée dans un volume Docker (`/data`) pour survivre
  au remplacement du conteneur.
- Le `.dockerignore` exclut secrets, historique Git et bases locales de l'image.

## CI (GitHub Actions)
À chaque push ou pull request vers `main` :
1. installation des dépendances et exécution des tests (pytest) ;
2. construction de l'image Docker (seulement si les tests passent) ;
3. smoke test : le conteneur démarre et répond sur /health.

Le workflow tourne avec des permissions en lecture seule.
