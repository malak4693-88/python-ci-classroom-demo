import pytest

from price_calculator import calculate_total


@pytest.mark.parametrize(
    ("unit_price", "quantity", "discount_percent", "expected"),
    [
        (4.50, 2, 0, 9.00),
        (10.00, 3, 20, 24.00),
        (5.99, 0, 0, 0.00),
        (12.00, 1, 100, 0.00),
    ],
)
def test_calculates_expected_total(
    unit_price,
    quantity,
    discount_percent,
    expected,
):
    assert calculate_total(unit_price, quantity, discount_percent) == expected


def test_rounds_result_to_two_decimal_places():
    assert calculate_total(10.00, 1, 33.333) == 6.67


@pytest.mark.parametrize(
    ("unit_price", "quantity", "discount_percent"),
    [
        (-0.01, 1, 0),
        (1.00, -1, 0),
        (1.00, 1, -0.01),
        (1.00, 1, 100.01),
    ],
)
def test_rejects_values_outside_supported_range(
    unit_price,
    quantity,
    discount_percent,
):
    with pytest.raises(ValueError):
        calculate_total(unit_price, quantity, discount_percent)


def test_rejects_non_integer_quantity():
    with pytest.raises(TypeError):
        calculate_total(2.50, 1.5)
