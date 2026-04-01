import pytest
from app.app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200


def test_add(client):
    res = client.get("/add/2/3")
    assert res.json["result"] == 5