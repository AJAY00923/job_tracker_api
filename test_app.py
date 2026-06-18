import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers(client):
    response = client.post("/login", data={
        "username": "ajay",
        "password": "secret"
    })
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Job Tracker Api is running!"}

def test_create_application(client, auth_headers):
    response = client.post("/applications",
        json={"company": "Google", "role": "Backend Engineer", "status": "applied"},
        headers=auth_headers
    )
    assert response.status_code == 201
    assert response.json()["message"] == "Application added successfully"

def test_get_applications(client, auth_headers):
    response = client.get("/applications", headers=auth_headers)
    assert response.status_code == 200
    assert "applications" in response.json()