from interqu import balanced_binary_tree as t
from interqu import binary_tree as bt


def test_01():
    tree = bt.create_tree([3,9,20,None,None,15,7])
    assert(t.balanced(tree) == True)
