import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_new_stories():
    response = client.get("/new-stories")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_top_stories():
    response = client.get("/top-stories")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_best_stories():
    response = client.get("/best-stories")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_invalid_route():
    response = client.get("/invalid-route")
    assert response.status_code == 404