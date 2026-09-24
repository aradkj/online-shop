from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_complete_product_flow():

    # Create product
    create_response = client.post(
        "/products",
        json={
            "name": "Gaming Headset",
            "description": "Wireless Gaming Headset",
            "price": 150,
            "stock": 5
        }
    )

    assert create_response.status_code == 200

    product = create_response.json()
    product_id = product["id"]

    # Get all products
    products_response = client.get("/products")

    assert products_response.status_code == 200

    products = products_response.json()

    assert len(products) > 0

    # Get created product
    product_response = client.get(
        f"/products/{product_id}"
    )

    assert product_response.status_code == 200

    result = product_response.json()

    # Verify product
    assert result["id"] == product_id
    assert result["name"] == "Gaming Headset"
    assert result["price"] == 150
    assert result["stock"] == 5