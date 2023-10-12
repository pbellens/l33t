from l33t import flatten_binary_tree_to_linked_list as t
from l33t import binary_tree as bt


def test_01():
    tree = bt.create_tree([1,2,5,3,4,None,6])

    t.flatten(tree)

    lense = tree

    assert(lense is not None)
    assert(lense.val == 1)
    assert(lense.left is None)
    lense = lense.right

    assert(lense is not None)
    assert(lense.val == 2)
    assert(lense.left is None)
    lense = lense.right

    assert(lense is not None)
    assert(lense.val == 3)
    assert(lense.left is None)
    lense = lense.right

    assert(lense is not None)
    assert(lense.val == 4)
    assert(lense.left is None)
    lense = lense.right

    assert(lense is not None)
    assert(lense.val == 5)
    assert(lense.left is None)
    lense = lense.right

    assert(lense is not None)
    assert(lense.val == 6)
    assert(lense.left is None)
    lense = lense.right

def test_02():
    tree = bt.create_tree([])

    t.flatten(tree)

    assert(tree is None)

def test_03():
    tree = bt.create_tree([1])

    t.flatten(tree)

    lense = tree

    assert(lense is not None)
    assert(lense.val == 1)
    assert(lense.left is None)
    assert(lense.right is None)
