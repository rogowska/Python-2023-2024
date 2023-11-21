# Oliwia Rogowska #
#    Zadanie 7    #
#     Python      #
#   21.11.2023    #
###################

import unittest
from points import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        #if the slope of lines joining two pairs of points is the same, points are collinear
        if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
            raise ValueError("Points are collinear")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        return ("[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y)
                + "), (" + str(self.pt3.x) + ", " + str(self.pt3.y) + ")]")

    def __repr__(self):
        return ("Triangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y)
                + ", " + str(self.pt3.x) + ", " + str(self.pt3.y) + ")")

    def __eq__(self, other):
        list1 = ((self.pt1.x, self.pt1.y), (self.pt2.x, self.pt2.y), (self.pt3.x, self.pt3.y))
        list2 = ((other.pt1.x, other.pt1.y), (other.pt2.x, other.pt2.y), (other.pt3.x, other.pt3.y))
        return sorted(list1) == sorted(list2)

    def __ne__(self, other):
        return not self == other

    def center(self):
        sum_point = self.pt1 + self.pt2 + self.pt3
        sum_point.x = round(sum_point.x / 3, 3)
        sum_point.y = round(sum_point.y / 3, 3)
        return sum_point

    def area(self):
        return 1 / 2 * abs(self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y)
                           + self.pt3.x * (self.pt1.y - self.pt2.y))

    # move implemented that it manipulate with object variables
    def move(self, x, y):
        for key, value in self.__dict__.items():
            if isinstance(value, Point):
                setattr(self, key, value + Point(x, y))
        return self

    def make4(self):
        pt12x = (self.pt1.x - self.pt2.x) / 2
        pt12y = (self.pt1.y - self.pt2.y) / 2
        pt23x = (self.pt2.x - self.pt3.x) / 2
        pt23y = (self.pt2.y - self.pt3.y) / 2
        pt31x = (self.pt3.x - self.pt1.x) / 2
        pt31y = (self.pt3.y - self.pt1.y) / 2
        return tuple(Triangle(pt12x, pt12y, pt23x, pt23y, pt31x, pt31y),
                     Triangle(self.pt1.x, self.pt1.y, pt12x, pt12y, pt31x, pt31y),
                     Triangle(self.pt2.x, self.pt2.y, pt23x, pt23y, pt12x, pt12y),
                     Triangle(self.pt3.x, self.pt3.y, pt23x, pt23y, pt31x, pt31y) )



# Kod testujący moduł.

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.myTriangle = Triangle(1, 3, 4, 5, -5, 1)
        self.myTriangle2 = Triangle(0, 0, -6, 9, -5, 8)
        self.myTriangle3 = Triangle(2, 0, 4, 9, -8, -1)
        self.myTriangle4 = Triangle(1, 3, 4, 5, -5, 1)

    def test__str__(self):
        self.assertEqual(str(self.myTriangle), "[(1, 3), (4, 5), (-5, 1)]")
        self.assertEqual(str(self.myTriangle2), "[(0, 0), (-6, 9), (-5, 8)]")
        self.assertEqual(str(self.myTriangle3), "[(2, 0), (4, 9), (-8, -1)]")

    def test__repr__(self):
        self.assertEqual(repr(self.myTriangle), "Triangle(1, 3, 4, 5, -5, 1)")
        self.assertEqual(repr(self.myTriangle2), "Triangle(0, 0, -6, 9, -5, 8)")
        self.assertEqual(repr(self.myTriangle3), "Triangle(2, 0, 4, 9, -8, -1)")

    def test__eq__(self):
        self.assertTrue(self.myTriangle == self.myTriangle4)
        self.assertFalse(self.myTriangle2 == self.myTriangle3)
        self.assertFalse(self.myTriangle3 == self.myTriangle4)

    def test__ne__(self):
        self.assertFalse(self.myTriangle != self.myTriangle4)
        self.assertTrue(self.myTriangle2 != self.myTriangle3)
        self.assertTrue(self.myTriangle3 != self.myTriangle4)

    def test_center(self):
        self.assertEqual(self.myTriangle.center(), Point(0, 3))
        self.assertEqual(self.myTriangle2.center(), Point(-3.667, 5.667))
        self.assertEqual(self.myTriangle3.center(), Point(-0.667, 2.667))

    def test_area(self):
        self.assertEqual(self.myTriangle.area(), 3)
        self.assertEqual(self.myTriangle2.area(), 1.5)
        self.assertEqual(self.myTriangle3.area(), 44)

    def test_move(self):
        self.assertEqual(self.myTriangle.move(3, 3), Triangle(4, 6, 7, 8, -2, 4))
        self.assertEqual(self.myTriangle2.move(-2, 0), Triangle(-2, 0, -8, 9, -7, 8))
        self.assertEqual(self.myTriangle3.move(9, -3), Triangle(11, -3, 13, 6, 1, -4))
        self.assertEqual(self.myTriangle3.move(0, 5), Triangle(11, 2, 13, 11, 1, 1))

    def test_make4(self): pass


if __name__ == '__main__':
    unittest.main()
