from interqu import symmetric_tree as t
from interqu import binary_tree as bt


def test_01():
    r = bt.create_tree([1,2,2,3,4,4,3])
    bt.print_tree(r)
    assert(t.is_symmetric(r) == True)

def test_02():
    r = bt.create_tree([1,2,2,None,3,None,3])
    bt.print_tree(r)
    assert(t.is_symmetric(r) == False)
