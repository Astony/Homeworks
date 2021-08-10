from homework11.task02.discount_strategy import Order

"""We'll use different types of discounts"""


def ten_percent_discount(order: Order) -> float:
    return order.price * 0.10


def fifty_percent_discount(order: Order) -> float:
    return order.price * 0.50


def ten_dollars_discount(order: Order) -> float:
    return 10.0


def test_percentage_discount():
    """Test cases with percentage discounts"""
    order1 = Order(100, ten_percent_discount)
    order2 = Order(100, fifty_percent_discount)
    assert order1.use_discount() == 90.0
    assert order2.use_discount() == 50.0


def test_non_percentage_discount():
    """Test cases with non percentage discounts"""
    order1 = Order(5, ten_dollars_discount)
    assert order1.use_discount() == 0
