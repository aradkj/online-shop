from pytest_bdd import given, when, then, scenarios
from fastapi.testclient import TestClient

from app.main import app


scenarios("../features/product.feature")

client = TestClient(app)


@given("the shop is running")
def shop_is_running():
    response = client.get("/")
    assert response.status_code == 200


@when("I create a product")
def create_product():
    response = client.post(
        "/products",
        json={
            "name": "BDD Gaming Mouse",
            "description": "Gaming Mouse for BDD testing",
            "price": 50,
            "stock": 10
        }
    )

    assert response.status_code == 200

    return response.json()


@then("the product should be available")
def product_should_be_available():
    response = client.get("/products")

    assert response.status_code == 200

    products = response.json()

    assert any(
        product["name"] == "BDD Gaming Mouse"
        for product in products
    )