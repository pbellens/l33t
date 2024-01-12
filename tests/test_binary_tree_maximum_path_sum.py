from l33t import binary_tree_maximum_path_sum as t
from l33t import binary_tree as bt


def test_01():
    tree = bt.create_tree([1, 2, 3])
    assert(tree)
    assert(t.max_sum(tree) == 6)

def test_02():
    tree = bt.create_tree([-10,9,20,None,None,15,7])
    assert(tree)
    assert(t.max_sum(tree) == 42)
