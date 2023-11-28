# Oliwia Rogowska #
#    Zadanie 8    #
#     Python      #
#   28.11.2023    #
###################

import unittest
from points import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # if the slope of lines joining two pairs of points is the same, points are collinear
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
        pt12x = (self.pt1.x + self.pt2.x) / 2
        pt12y = (self.pt1.y + self.pt2.y) / 2
        pt23x = (self.pt2.x + self.pt3.x) / 2
        pt23y = (self.pt2.y + self.pt3.y) / 2
        pt31x = (self.pt3.x + self.pt1.x) / 2
        pt31y = (self.pt3.y + self.pt1.y) / 2
        return (Triangle(pt12x, pt12y, pt23x, pt23y, pt31x, pt31y),
                Triangle(self.pt1.x, self.pt1.y, pt12x, pt12y, pt31x, pt31y),
                Triangle(self.pt2.x, self.pt2.y, pt23x, pt23y, pt12x, pt12y),
                Triangle(self.pt3.x, self.pt3.y, pt23x, pt23y, pt31x, pt31y))

    @staticmethod
    def from_points(list_of_points):
        Triangle.validation_of_points(list_of_points)
        return Triangle(list_of_points[0].x, list_of_points[0].y, list_of_points[1].x, list_of_points[1].y,
                        list_of_points[2].x, list_of_points[2].y)

    @staticmethod
    def validation_of_points(list_of_points):
        if len(list_of_points) != 3:
            raise ValueError("List should contain 3 points")
        for point in list_of_points:
            if not isinstance(point, Point):
                raise ValueError("All elements should be Point type")
        if ((list_of_points[2].y - list_of_points[1].y) * (list_of_points[1].x - list_of_points[0].x) ==
                (list_of_points[1].y - list_of_points[0].y) * (list_of_points[2].x - list_of_points[1].x)):
            raise ValueError("Points are collinear")

    @property
    def center(self):
        sum_point = self.pt1 + self.pt2 + self.pt3
        sum_point.x = sum_point.x / 3
        sum_point.y = sum_point.y / 3
        return sum_point

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)
