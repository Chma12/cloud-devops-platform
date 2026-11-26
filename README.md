# Cloud & DevOps Platform

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
