import pytest
from RBTree import RBTree


def insert_values(tree, list_of_values):
    for value in list_of_values:
        tree.insert(value)
    return tree


@pytest.fixture(scope="function")
def TreeWithRootOnly():
    atree = RBTree(5)
    yield atree
    del atree


@pytest.fixture(scope="function")
def Tree1():
    atree = RBTree(11)
    insert_values(atree, [5, 15, 3, 54, 10, 14, 21, 16])
    yield atree
    del atree


@pytest.fixture(scope="function")
def Tree2():
    atree = RBTree(1)
    insert_values(atree, [59, 2, 3, 32, 7, 14, 40, 80])
    yield atree
    del atree


def test_display(TreeWithRootOnly, Tree1, Tree2):
    assert str(TreeWithRootOnly) == "5"
    assert str(Tree1) == "3 5 10 11 14 15 16 21 54"
    assert str(Tree2) == "1 2 3 7 14 32 40 59 80"


def test_insert(TreeWithRootOnly):
    assert str(TreeWithRootOnly) == "5"
    TreeWithInsertedValues = insert_values(TreeWithRootOnly, [11])
    assert str(TreeWithInsertedValues) == "5 11"
    TreeWithInsertedValues = insert_values(TreeWithInsertedValues, [15, 40])
    assert str(TreeWithInsertedValues) == "5 11 15 40"
    TreeWithInsertedValues = insert_values(TreeWithInsertedValues, [3, 10])
    assert str(TreeWithInsertedValues) == "3 5 10 11 15 40"
    TreeWithInsertedValues.insert(50)
    assert str(TreeWithInsertedValues) == "3 5 10 11 15 40 50"
    with pytest.raises(ValueError) as excinfo:
        TreeWithInsertedValues.insert(3)
    assert "Nie można wstawić duplikatu. Spróbuj z inną wartością węzła." in str(excinfo.value)


def test_search(Tree1, Tree2):
    assert str(Tree1.search(54)) == "54"
    assert str(Tree1.search(100)) == 'None'
    assert str(Tree2.search(7)) == "7"
    assert str(Tree2.search(0)) == 'None'


def test_delete(Tree1, Tree2, TreeWithRootOnly):
    Tree1.delete(54)
    assert str(Tree1) == "3 5 10 11 14 15 16 21"
    Tree1.delete(5)
    assert str(Tree1) == "3 10 11 14 15 16 21"
    Tree2.delete(32)
    assert str(Tree2) == "1 2 3 7 14 40 59 80"
    Tree2.delete(14)
    assert str(Tree2) == "1 2 3 7 40 59 80"
    TreeWithRootOnly.delete(5)
    assert str(TreeWithRootOnly) == ""
    with pytest.raises(ValueError) as excinfo:
        TreeWithRootOnly.delete(50)
    assert "Nie ma węzła do usunięcia." in str(excinfo.value)


def test_minimum(Tree1, Tree2, TreeWithRootOnly):
    assert str(TreeWithRootOnly.minimum()) == '5'
    assert str(Tree1.minimum()) == '3'
    assert str(Tree2.minimum()) == '1'
    node = Tree1.search(21)
    assert str(Tree1.minimum(node)) == '16'
    node = Tree1.search(15)
    assert str(Tree1.minimum(node)) == '14'
    node = Tree2.search(59)
    assert str(Tree1.minimum(node)) == '40'
    node = Tree2.search(32)
    assert str(Tree2.minimum(node)) == "3"


def test_maximum(Tree1, Tree2, TreeWithRootOnly):
    assert str(TreeWithRootOnly.maximum()) == '5'
    assert str(Tree1.maximum()) == '54'
    assert str(Tree2.maximum()) == '80'
    node = Tree1.search(5)
    assert str(Tree1.maximum(node)) == '10'
    node = Tree1.search(21)
    assert str(Tree1.maximum(node)) == '54'
    node = Tree2.search(7)
    assert str(Tree2.maximum(node)) == '14'
    node = Tree2.search(3)
    assert str(Tree2.maximum(node)) == '3'


def test_successor(Tree1, Tree2):
    node = Tree1.search(15)
    assert str(Tree1.successor(node)) == "16"
    node = Tree1.search(5)
    assert str(Tree1.successor(node)) == "10"
    node = Tree1.search(54)
    assert str(Tree1.successor(node)) == 'None'
    node = Tree2.search(32)
    assert str(Tree2.successor(node)) == "40"
    node = Tree2.search(1)
    assert str(Tree2.successor(node)) == "2"
    node = Tree2.search(80)
    assert str(Tree2.successor(node)) == 'None'


def test_predecessor(Tree1, Tree2):
    node = Tree1.search(15)
    assert str(Tree1.predecessor(node)) == "14"
    node = Tree1.search(5)
    assert str(Tree1.predecessor(node)) == "3"
    node = Tree1.search(3)
    assert str(Tree1.predecessor(node)) == 'None'
    node = Tree2.search(32)
    assert str(Tree2.predecessor(node)) == "14"
    node = Tree2.search(80)
    assert str(Tree2.predecessor(node)) == "59"
    node = Tree2.search(1)
    assert str(Tree2.predecessor(node)) == 'None'


if __name__ == '__main__':
    pytest.main()