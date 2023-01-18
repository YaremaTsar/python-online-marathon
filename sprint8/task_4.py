import unittest
import math

class TriangleNotValidArgumentException(Exception):
    def __str__(self):
        return 'Not valid arguments'


class TriangleNotExistException(Exception):
    def __str__(self):
        return 'Can`t create triangle with this arguments'


class Triangle:
    def check_args(self, coordinates):
        if not isinstance(coordinates, (list, tuple)) or len(coordinates) != 3 or  not all([isinstance(i, (int, float)) for i in coordinates]):
            raise TriangleNotValidArgumentException
        return coordinates

    def __init__(self, coordinates):
        self.coordinates = self.check_args(coordinates)
        self.area = self.get_area()
    def get_area(self):
        a, b, c = self.coordinates
        if a == 0 or b == 0 or c == 0:
            raise TriangleNotExistException
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        if isinstance(area, complex) or area <= 0 or a <= 0 or b <= 0 or c <= 0:
            raise TriangleNotExistException
        return math.floor(area * 100) / 100
class TriangleTest(unittest.TestCase):
    def test_check1(self):
        
