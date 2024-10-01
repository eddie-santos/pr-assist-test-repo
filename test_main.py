from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_get_fibonacci_positive():
    response = client.get("/fibonacci/5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_get_fibonacci_zero():
    response = client.get("/fibonacci/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Input must be positive"}

def test_get_fibonacci_negative():
    response = client.get("/fibonacci/-5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Input must be positive"}

def test_get_power():
    response = client.get("/power/2/3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_get_factorial():
    response = client.get("/factorial/5")
    assert response.status_code == 200
    assert response.json() == {"result": 120}

def test_divide():
    response = client.get("/divide/10/2")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_reverse_string():
    response = client.post("/reverse-string", json={"input_string": "hello"})
    assert response.status_code == 200
    assert response.json() == {"reversed": "olleh"}
