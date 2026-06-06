from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Job Tracker Api is running!"}

def test_create_application():
    response = client.post("/applications", json={
        "company": "TechCorp",
        "role": "Software Engineer",
        "status": "applied"
    })# POST a new application
    assert response.status_code == 201
    assert response.json() ["message"]== "Application added successfully"

def test_get_applications():
    response = client.get("/applications")# GET all applications
    assert response.status_code == 200
    assert "applications" in response.json()