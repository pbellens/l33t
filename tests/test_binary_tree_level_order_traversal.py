from l33t import binary_tree_level_order_traversal as t
from l33t import binary_tree as bt


def test_01():
    input = bt.create_tree([3,9,20,None,None,15,7])
    traversal = t.traverse(input)
    assert(traversal == [[3],[9,20],[15,7]])

def test_02():
    input = bt.create_tree([1,None, None])
    traversal = t.traverse(input)
    assert(traversal == [[1]])

def test_03():
    input = bt.create_tree([])
    traversal = t.traverse(input)
    assert(traversal == [])




