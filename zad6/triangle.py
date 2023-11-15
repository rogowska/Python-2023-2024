# Oliwia Rogowska #
#    Zadanie 6    #
#     Python      #
#   14.11.2023    #
###################


from points import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        return ("[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), " + str(self.pt2.x) + ", " + str(self.pt2.y)
                + "), " + str(self.pt3.x) + ", " + str(self.pt3.y) + ")]")

    def __repr__(self):
        return ("Triangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y)
                + ", " + str(self.pt3.x) + str(self.pt3.y) + ")")

    def __eq__(self, other):
        list1 = ((self.pt1.x, self.pt1.y), (self.pt2.x, self.pt2.y), (self.pt3.x, self.pt3.y))
        list2 = ((other.pt1.x, other.pt1.y), (other.pt2.x, other.pt2.y), (other.pt3.x, other.pt3.y))
        return sorted(list1) == sorted(list2)

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point(1 / 3 * (self.pt1.x + self.pt2.x + self.pt3.x), 1 / 3 * (self.pt1.y + self.pt2.y + self.pt3.y))

    def area(self):
        return 1 / 2 * abs((self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) - (self.pt2.x - self.pt1.x)
                           * (self.pt3.x - self.pt3.x))

    def move(self, x, y):
        for key, value in self.__dict__.items():
            if isinstance(value, Point):
                value += Point(x, y)
        return self



# Kod testujący moduł.

import unittest


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.myTriangle = Triangle(1, 3, 4, 5, -5, 1)
        self.myTriangle2 = Triangle(0, 0, -6, 9, -5, 8)
        self.myTriangle3 = Triangle(2, 0, 4, 9, -8, -1)
        self.myTriangle4 = Triangle(1, 3, 4, 5, -5, 1)

    def test__eq__(self):
        self.assertTrue(self.myTriangle == self.myTriangle4)
        self.assertFalse(self.myTriangle2 == self.myTriangle3)
        self.assertFalse(self.myTriangle3 == self.myTriangle4)

    def test_move(self):
        self.assertTrue(Triangle.move(self.myTriangle, 3, 3), Triangle(4, 6, 7, 8, -2, 4))
        # self.assertEqual(str(self.myPoint2), "(-2, 5)")
        # self.assertEqual(str(self.myPoint3), "(5, -10)")

if __name__ == '__main__':
    unittest.main()