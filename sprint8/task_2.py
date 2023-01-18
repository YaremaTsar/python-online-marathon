import unittest

def divide(num_1, num_2):
    if num_2 != 0:
        return float(num_1) / num_2
    raise ZeroDivisionError("ZeroDivisionError")
class DivideTest(unittest.TestCase):
    def test_positive_divide(self):
        expected = 5.0
        actual = divide(10, 2)
        self.assertEqual(actual, expected)
    def test_negative_divide(self):
        expected = -3.33333
        actual = divide(10, -3)
        self.assertAlmostEqual(actual, expected, 5)
    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, divide, 3,0)
