r'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
'''


import typing
from . import binary_tree as bt

def is_same_tree(t1: typing.Optional[bt.TreeNode], t2: typing.Optional[bt.TreeNode]) -> bool:
    if t1 is None and t2 is None:
        return True
    if t1 is None and t2 is not None:
        return False
    if t1 is not None and t2 is None:
        return False
    return t1.val == t2.val \
        and is_same_tree(t1.left, t2.left) \
        and is_same_tree(t1.right, t2.right)
