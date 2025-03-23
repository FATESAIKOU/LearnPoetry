from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos", json={"id": 1, "title": "Test Todo", "description": "Test Description", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Test Todo", "description": "Test Description", "completed": False}

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_get_todo():
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_todo():
    response = client.put("/todos/1", json={"id": 1, "title": "Updated Todo", "description": "Updated Description", "completed": True})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Todo"

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

    # Verify deletion
    response = client.get("/todos/1")
    assert response.status_code == 404
