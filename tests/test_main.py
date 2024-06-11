from fastapi.testclient import TestClient # type: ignore
from app import app # type: ignore

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_get_sum():
    response = client.get("/sum?a=1&b=2")
    assert response.status_code == 200
    assert response.json() == {"La suma es:": 3}

    response = client.get("/sum?a=-1&b=2")
    assert response.status_code == 200
    assert response.json() == {"La suma es:": 1}
