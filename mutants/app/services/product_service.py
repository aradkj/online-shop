def calculate_discount(price: float, discount_percent: float) -> float:
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    return price - (price * discount_percent / 100)


def calculate_cart_total(price: float, quantity: int) -> float:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return price * quantity