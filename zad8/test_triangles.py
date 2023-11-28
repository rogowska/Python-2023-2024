import pytest
from triangles import Triangle


def make4TestMethod(myTriangle, triangleTuple):
    for triangle in myTriangle.make4():
        if triangle not in triangleTuple:
            assert False


@pytest.fixture
def myTriangle():
    return Triangle(1, 3, 4, 5, -5, 1)


@pytest.fixture
def myTriangle2():
    return Triangle(0, 0, -6, 9, -5, 8)


@pytest.fixture
def myTriangle3():
    return Triangle(2, 0, 4, 9, -8, -1)


@pytest.fixture
def myTriangle4():
    return Triangle(1, 3, 4, 5, -5, 1)


def test__str__(myTriangle, myTriangle2, myTriangle3):
    assert str(myTriangle) == "[(1, 3), (4, 5), (-5, 1)]"
    assert str(myTriangle2) == "[(0, 0), (-6, 9), (-5, 8)]"
    assert str(myTriangle3) == "[(2, 0), (4, 9), (-8, -1)]"


def test__repr__(myTriangle, myTriangle2, myTriangle3):
    assert repr(myTriangle) == "Triangle(1, 3, 4, 5, -5, 1)"
    assert repr(myTriangle2) == "Triangle(0, 0, -6, 9, -5, 8)"
    assert repr(myTriangle3) == "Triangle(2, 0, 4, 9, -8, -1)"


def test__eq__(myTriangle, myTriangle2, myTriangle3, myTriangle4):
    assert myTriangle == myTriangle4
    assert not myTriangle2 == myTriangle3
    assert not myTriangle3 == myTriangle4


def test__ne__(myTriangle, myTriangle2, myTriangle3, myTriangle4):
    assert not myTriangle != myTriangle4
    assert myTriangle2 != myTriangle3
    assert myTriangle3 != myTriangle4


def test_center(myTriangle, myTriangle2, myTriangle3):
    assert round(myTriangle.center.x, 3) == 0 and round(myTriangle.center.y, 3) == 3
    assert round(myTriangle2.center.x, 3) == -3.667 and round(myTriangle2.center.y, 3) == 5.667
    assert round(myTriangle3.center.x, 3) == -0.667 and round(myTriangle3.center.y, 3) == 2.667


def test_area(myTriangle, myTriangle2, myTriangle3):
    assert myTriangle.area() == 3
    assert myTriangle2.area() == 1.5
    assert myTriangle3.area() == 44


def test_move(myTriangle, myTriangle2, myTriangle3):
    assert myTriangle.move(3, 3) == Triangle(4, 6, 7, 8, -2, 4)
    assert myTriangle2.move(-2, 0) == Triangle(-2, 0, -8, 9, -7, 8)
    assert myTriangle3.move(9, -3) == Triangle(11, -3, 13, 6, 1, -4)
    assert myTriangle3.move(0, 5) == Triangle(11, 2, 13, 11, 1, 1)


def test_make4(myTriangle, myTriangle2, myTriangle3):
    make4TestMethod(myTriangle, (Triangle(-5, 1, -2, 2, -0.5, 3),
                                 Triangle(-2, 2, -0.5, 3, 2.5, 4),
                                 Triangle(1, 3, -2, 2, 2.5, 4),
                                 Triangle(4, 5, -0.5, 3, 2.5, 4)))

    make4TestMethod(myTriangle2, (Triangle(-5.5, 8.5, -3, 4.5, -2.5, 4),
                                  Triangle(0, 0, -2.5, 4, -3, 4.5),
                                  Triangle(-5, 8, -2.5, 4, -5.5, 8.5),
                                  Triangle(-3, 4.5, -6, 9, -5.5, 8.5)))

    make4TestMethod(myTriangle3, (Triangle(-3, -0.5, 3, 4.5, -2, 4),
                                  Triangle(-8, -1, -3, -0.5, -2, 4),
                                  Triangle(-3, -0.5, 2, 0, 3, 4.5),
                                  Triangle(4, 9, -2, 4, 3, 4.5)))


def test_from_points(): pass


def test_top(): pass


def test_bottom(): pass


def test_left(): pass


def test_right(): pass


def test_width(): pass


def test_height(): pass


def test_topleft(): pass


def test_topright(): pass


def test_bottomleft(): pass


def test_bottomright(): pass


if __name__ == '__main__':
    pytest.main()
