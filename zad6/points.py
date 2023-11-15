# Oliwia Rogowska #
#    Zadanie 6    #
#     Python      #
#   14.11.2023    #
###################
import math


# zad 6.2

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "Point" + str(self)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return (self.x, self.y) != (other.x, other.y)

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def __hash__(self):
        return hash((self.x, self.y))


# Kod testujący moduł.

import unittest


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.myPoint = Point(3, 4)
        self.myPoint2 = Point(-2, 5)
        self.myPoint3 = Point(5, -10)
        self.myPoint4 = Point(3, 4)

    def test__str__(self):
        self.assertEqual(str(self.myPoint), "(3, 4)")
        self.assertEqual(str(self.myPoint2), "(-2, 5)")
        self.assertEqual(str(self.myPoint3), "(5, -10)")

    def test__repr__(self):
        self.assertEqual(repr(self.myPoint), "Point(3, 4)")
        self.assertEqual(repr(self.myPoint2), "Point(-2, 5)")
        self.assertEqual(repr(self.myPoint3), "Point(5, -10)")

    def test__eq__(self):
        self.assertTrue(self.myPoint == self.myPoint4)
        self.assertFalse(self.myPoint == self.myPoint2)
        self.assertFalse(self.myPoint3 == self.myPoint4)

    def test__ne__(self):
        self.assertFalse(self.myPoint != self.myPoint4)
        self.assertTrue(self.myPoint != self.myPoint2)
        self.assertTrue(self.myPoint3 != self.myPoint4)

    def test__add__(self):
        self.assertEqual(self.myPoint + self.myPoint2, Point(1, 9))
        self.assertEqual(self.myPoint2 + self.myPoint3, Point(3, -5))
        self.assertEqual(self.myPoint3 + self.myPoint, Point(8, -6))

    def test__sub__(self):
        self.assertEqual(self.myPoint - self.myPoint2, Point(5, -1))
        self.assertEqual(self.myPoint2 - self.myPoint3, Point(-7, 15))
        self.assertEqual(self.myPoint3 - self.myPoint, Point(2, -14))

    def test__mul__(self):
        self.assertEqual(self.myPoint * self.myPoint2, 14)
        self.assertEqual(self.myPoint2 * self.myPoint3, -60)
        self.assertEqual(self.myPoint3 * self.myPoint, -25)

    def test_cross(self):
        self.assertEqual(self.myPoint.cross(self.myPoint2), 23)
        self.assertEqual(self.myPoint2.cross(self.myPoint3), -5)
        self.assertEqual(self.myPoint3.cross(self.myPoint), 50)

    def test_length(self):
        self.assertEqual(self.myPoint.length(), 5)
        self.assertEqual(self.myPoint2.length(), math.sqrt(29))
        self.assertEqual(self.myPoint3.length(), 5*math.sqrt(5))

    def test_hash(self):
        self.assertTrue(hash(self.myPoint) == hash(self.myPoint4))
        self.assertTrue(hash(self.myPoint) != hash(self.myPoint3))
        self.assertTrue(hash(self.myPoint) != hash(self.myPoint2))
        self.assertTrue((hash(Point(5,10)) != hash(Point(10, 5))))


if __name__ == '__main__':
    unittest.main()
