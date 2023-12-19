# Oliwia Rogowska #
#   Zadanie 11    #
#     Python      #
#   19.12.2023    #
###################

import pytest
from SingleList import SingleList
from Node import Node


def reverse_list_and_to_string(mylist):
    mylist.reverse()
    myStr = ""
    for item in mylist:
        myStr += str(item) + " "
    return myStr


@pytest.fixture(scope="function")
def emptyList():
    alist = SingleList()
    yield alist
    del alist


@pytest.fixture(scope="function")
def myList1():
    alist = SingleList()
    alist.insert_head(Node(11))
    alist.insert_head(Node(22))
    alist.insert_head(Node(33))
    alist.insert_head(Node(50))
    yield alist
    del alist


@pytest.fixture(scope="function")
def myList2():
    alist = SingleList()
    alist.insert_head(Node(63))
    alist.insert_head(Node(22))
    alist.insert_head(Node(30))
    alist.insert_head(Node(50))
    alist.insert_head(Node(63))
    alist.insert_head(Node(8))
    alist.insert_head(Node(3))
    alist.insert_head(Node(44))
    yield alist
    del alist


@pytest.fixture(scope="function")
def myList3():
    alist = SingleList()
    alist.insert_head(Node(6))
    alist.insert_head(Node(2))
    alist.insert_head(Node(0))
    alist.insert_head(Node(8))
    alist.insert_head(Node(3))
    alist.insert_head(Node(4))
    yield alist
    del alist


def test_reverse(myList1, myList2, myList3, emptyList):
    assert reverse_list_and_to_string(myList1) == "11 22 33 50 "
    assert reverse_list_and_to_string(myList2) == "63 22 30 50 63 8 3 44 "
    assert reverse_list_and_to_string(myList3) == "6 2 0 8 3 4 "
    assert reverse_list_and_to_string(emptyList) == ""


def test_find_min(myList1, myList2, myList3, emptyList):
    assert emptyList.find_min() is None
    assert myList1.find_min() == Node(11)
    assert myList2.find_min() == Node(3)
    assert myList3.find_min() == Node(0)


def test_find_max(myList1, myList2, myList3, emptyList):
    assert emptyList.find_max() is None
    assert myList1.find_max() == Node(50)
    assert myList2.find_max() == Node(63)
    assert myList3.find_max() == Node(8)


def test_search(myList1, myList2, myList3, emptyList):
    assert myList1.search(33) == Node(33)
    assert emptyList.search(50) is None
    assert myList1.search(52) is None
    assert myList2.search(63) == Node(63)
    assert myList3.search(2) == Node(2)


if __name__ == '__main__':
    pytest.main()