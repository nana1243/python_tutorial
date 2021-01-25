from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "_total"):
            self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total : {.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """ 할인액을 구체적인 숫자로 반환한다"""


class FidelityPromo(Promotion):
    """충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용"""

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """20 개 이상의 동일 상품을 구입하면, 10% 할일 적용"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item in order.cart:
                if item.quaantity >= 20:
                    discount += item.total() * 0.1

        return discount


class LargeOrderPromo(Promotion):
    """10 종류 이상의 상품을 구입하면 전체 7% 할인 적용"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


joe = Customer("john Done", 0)
ann = Customer("Ann Smith", 1100)
cart = [
    LineItem("banana", 4, 0.5),
    LineItem("apple", 10, 1.5),
]

t1 = Order(joe, cart, FidelityPromo)
t2 = Order(ann, cart, FidelityPromo)
