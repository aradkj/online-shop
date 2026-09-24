from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_product():
    response = client.post(
        "/products",
        json={
            "name": "Gaming Keyboard",
            "description": "Mechanical RGB Keyboard",
            "price": 100,
            "stock": 20
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Gaming Keyboard"
    assert data["price"] == 100
    assert data["stock"] == 20


def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)