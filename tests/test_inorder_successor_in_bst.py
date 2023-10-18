from l33t import inorder_successor_in_bst as t
from l33t import binary_tree as bt


def test_01():
    bst = bt.create_tree(nums = [2, 1, 3])
    assert(bst is not None)
    suc = t.successor(bst.left)
    assert(suc is not None)
    assert(suc.val == 2)

def test_02():
    bst = bt.create_tree([5,3,6,2,4,None,None,1,None,None,None])
    assert(bst is not None)
    assert(t.successor(bst.right) is None)

def test_03():
    bst = bt.create_tree([5,3,6,2,4,None,None,1,None,None,None])
    assert(bst is not None)
    assert(bst.left is not None)
    suc = t.successor(bst.left.right)
    assert(suc is not None)
    assert(suc.val == 5)

def test_04():
    bst = bt.create_tree([5,3,6,2,4,None,None,1,None,None,None])
    assert(bst is not None)
    assert(bst.left is not None)
    assert(bst.left.left is not None)
    assert(bst.left.left.left is not None)
    suc = t.successor(bst.left.left.left)
    assert(suc is not None)
    assert(suc.val == 2)

def test_05():
    bst = bt.create_tree([5,3,6,2,4,None,None,1,None,None,None])
    assert(bst is not None)
    assert(bst.left is not None)
    assert(bst.left.right is not None)
    suc = t.successor(bst.left.right)
    assert(suc is not None)
    assert(suc.val == 5)
