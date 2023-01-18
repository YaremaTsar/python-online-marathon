import unittest


def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    try:
        if discriminant > 0:
            x1, x2 = (- b + discriminant ** 0.5) / (2 * a), (- b - discriminant ** 0.5) / (2 * a)
            return x1, x2
        elif discriminant < 0:
            return None
        elif discriminant == 0:
            x1 = -b / (2 * a)
            return x1
    except ZeroDivisionError:
        print("error")


class QuadraticEquationTest(unittest.TestCase):
    def test_discriminant_less_zero(self):
        expected = None
        actual = quadratic_equation(4, 1, 2)
        self.assertEqual(actual, expected)
    def test_discriminant_more_zero(self):
        expected = (0.1880892557650571, -0.7595178271936286)
        actual = quadratic_equation(7, 4, -1)
        self.assertAlmostEqual(actual, expected)
    def test_discriminant_more_zero1(self):
        expected = (0.5, -1.0)
        actual = quadratic_equation(2, 1, -1)
        self.assertEqual(actual, expected)
    def test_discriminant_equal_zero(self):
        expected = 2.0
        actual = quadratic_equation(1, -4, 4)
        self.assertEqual(actual, expected)

