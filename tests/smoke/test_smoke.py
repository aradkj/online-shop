from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_application_is_running():
    response = client.get("/")

    assert response.status_code == 200


def test_products_endpoint_is_available():
    response = client.get("/products")

    assert response.status_code == 200


def test_can_create_product():
    response = client.post(
        "/products",
        json={
            "name": "Smoke Test Product",
            "description": "Product for smoke testing",
            "price": 10,
            "stock": 5
        }
    )

    assert response.status_code == 200