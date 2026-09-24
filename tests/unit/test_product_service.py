import pytest

from app.services.product_service import (
    calculate_discount,
    calculate_cart_total
)


def test_calculate_discount():
    result = calculate_discount(100, 20)

    assert result == 80


def test_calculate_cart_total():
    result = calculate_cart_total(50, 3)

    assert result == 150


def test_discount_cannot_be_negative():
    with pytest.raises(ValueError):
        calculate_discount(100, -10)


def test_discount_cannot_be_more_than_100():
    with pytest.raises(ValueError):
        calculate_discount(100, 120)


def test_quantity_must_be_greater_than_zero():
    with pytest.raises(ValueError):
        calculate_cart_total(50, 0)