import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_short_url(reset_db):
    original_url = "https://example.com/"
    response = client.post("/short-url", json={"url": original_url})
    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data["url"]) == 8


def test_redirect(reset_db):
    original_url = "https://example.com/"
    response = client.post("/short-url", json={"url": original_url})
    data = response.json()
    response = client.get("/" + data["url"])
    assert response.url == original_url


def test_redirect_not_found(reset_db):
    response = client.get("/BAD")
    assert response.status_code == 404
