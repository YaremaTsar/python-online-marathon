import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

class Cart:
    def __init__(self, products):
        self.products = products
    def price_with_discount(self, product):
        count = product.count
        price = product.price
        discount = [0.95, 0.90, 0.8, 0.7, 0.5]
        amount = [5, 7, 10, 20]
        if count < 5:
            return count * price
        for index, value in enumerate(amount):
            if count == 20:
                return price * 0.7 * count
            if count > 20:
                return price * 0.5 * count
            if count >= value and count < amount[index + 1]:
                return price * discount[index] * count

    def get_total_price(self):
        return sum([self.price_with_discount(i) for i in self.products])


class CartTest(unittest.TestCase):
    def test_equal(self):
        products = (Product('p1', 10, 4),
                    Product('p2', 100, 5),
                    Product('p3', 200, 6),
                    Product('p4', 300, 7),
                    Product('p5', 400, 9),
                    Product('p6', 500, 10),
                    Product('p7', 1000, 20))
        cart = Cart(products)
        self.assertEqual(cart.get_total_price(), 24785.0)
