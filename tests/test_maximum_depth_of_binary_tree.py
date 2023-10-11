from l33t import maximum_depth_of_binary_tree as t
from l33t import binary_tree as bt


def test_01():
    tree = bt.create_tree([3,9,20,None,None,15,7])
    assert(t.max_depth(tree) == 3)

def test_02():
    tree = bt.create_tree([1,None,2])
    assert(t.max_depth(tree) == 2)

def test_03():
    tree = bt.create_tree([])
    assert(t.max_depth(tree) == 0)
