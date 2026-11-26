def create_task(client, title="Apprendre Docker", description="Phase 3"):
    return client.post("/tasks", json={"title": title, "description": description})


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_task(client):
    response = create_task(client)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Apprendre Docker"
    assert data["done"] is False


def test_create_task_with_invalid_title_is_rejected(client):
    assert client.post("/tasks", json={"title": ""}).status_code == 422
    assert client.post("/tasks", json={"description": "sans titre"}).status_code == 422


def test_list_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks(client):
    create_task(client, title="Tâche 1")
    create_task(client, title="Tâche 2")
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_task(client):
    task_id = create_task(client).json()["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Apprendre Docker"


def test_update_task(client):
    task_id = create_task(client).json()["id"]
    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Apprendre Docker", "description": "Terminé", "done": True},
    )
    assert response.status_code == 200
    assert response.json()["done"] is True
    assert response.json()["description"] == "Terminé"


def test_delete_task(client):
    task_id = create_task(client).json()["id"]
    assert client.delete(f"/tasks/{task_id}").status_code == 204
    assert client.get(f"/tasks/{task_id}").status_code == 404


def test_unknown_task_returns_404(client):
    assert client.get("/tasks/999").status_code == 404
    assert client.put("/tasks/999", json={"title": "x"}).status_code == 404
    assert client.delete("/tasks/999").status_code == 404