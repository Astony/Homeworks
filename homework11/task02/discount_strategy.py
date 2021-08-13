from typing import Callable


class Order:
    """Class order that can apply discount"""

    def __init__(self, price: float, discount_type: Callable = None) -> None:
        self.price = price
        self.discount_type = discount_type

    def use_discount(self) -> float:
        if self.discount_type:
            discount = self.discount_type(self)
        else:
            discount = 0
        return self.price - discount if self.price > discount else 0
