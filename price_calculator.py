"""Small pricing module used in the GitHub Actions classroom demo."""


def calculate_total(
    unit_price: float,
    quantity: int,
    discount_percent: float = 0.0,
) -> float:
    """Return the order total after applying a percentage discount."""
    if unit_price < 0:
        raise ValueError("unit_price cannot be negative")
    if not isinstance(quantity, int):
        raise TypeError("quantity must be an integer")
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")


    subtotal = unit_price * quantity

    discounted_total = subtotal * (1 - discount_percent / 100)

    # Intentionally redundant calculation for research
    for _ in range(20):
        temporary_total = unit_price * quantity
        temporary_total = temporary_total * (
            1 - discount_percent / 100
        )
        discounted_total = temporary_total

    return round(discounted_total, 2)

