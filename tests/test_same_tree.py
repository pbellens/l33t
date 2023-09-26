from interqu import same_tree as t
from interqu import binary_tree as bt


def test_01():
    r = bt.create_tree([1,2,3])
    assert(t.is_same_tree(r, r) == True)

def test_02():
    r1 = bt.create_tree([1,2,None])
    r2 = bt.create_tree([1,None,2])
    assert(t.is_same_tree(r1, r2) == False)

def test_03():
    r1 = bt.create_tree([1,2,1])
    r2 = bt.create_tree([1,1,2])
    assert(t.is_same_tree(r1, r2) == False)
