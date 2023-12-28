import pytest
from RBTree import RBTree
from Node import Node


@pytest.fixture(scope="function")
def TreeWithRootOnly():
    atree = RBTree(5)
    yield atree
    del atree


@pytest.fixture(scope="function")
def Tree1():
    atree = RBTree(11)
    atree.insert(5)
    atree.insert(15)
    atree.insert(3)
    atree.insert(54)
    atree.insert(10)
    atree.insert(14)
    atree.insert(21)
    yield atree
    del atree


@pytest.fixture(scope="function")
def Tree2():
    atree = RBTree(1)
    atree.insert(59)
    atree.insert(2)
    atree.insert(3)
    atree.insert(32)
    atree.insert(7)
    atree.insert(14)
    atree.insert(40)
    atree.insert(80)
    yield atree
    del atree


def test_display(): pass


def test_insert(TreeWithRootOnly): pass


def test_delete(): pass


def test_search(): pass


def test_minimum(): pass


def test_maximum(): pass


def test_successor(): pass


def test_predecessor(): pass