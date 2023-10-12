from l33t import convert_sorted_array_to_binary_search_tree as t
from l33t import binary_tree as bt
from l33t import same_tree as st


def test_01():
    tree = t.make_tree([-10,-3,0,5,9])
    exp = bt.create_tree([0, -3, 9, -10, None, 5, None])

    assert(st.is_same_tree(tree, exp))

def test_02():
    tree = t.make_tree([1, 3])
    exp1 = bt.create_tree([1, None, 3])
    exp2 = bt.create_tree([3, 1, None])

    assert(st.is_same_tree(tree, exp1) or st.is_same_tree(tree, exp2))
