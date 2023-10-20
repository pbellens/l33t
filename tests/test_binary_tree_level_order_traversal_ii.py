from l33t import binary_tree_level_order_traversal_ii as t
from l33t import binary_tree as bt


def test_01():
    tree = bt.create_tree([3,9,20,None,None,15,7])
    assert(tree is not None)
    order = t.bottom_up(tree)

    assert(order == [[15,7],[9,20],[3]])


def test_02():
    tree = bt.create_tree([1])
    assert(tree is not None)
    order = t.bottom_up(tree)

    assert(order == [[1]])


def test_03():
    order = t.bottom_up(None)

    assert(order == [])

