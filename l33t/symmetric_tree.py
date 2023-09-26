'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
 
Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''


import typing
from . import binary_tree as bt

def symmetric(t1: bt.TreeNode, t2: bt.TreeNode) -> bool:
    if t1 is None and t2 is None:
        return True
    if t1 is None and t2 is not None:
        return False
    if t2 is None and t1 is not None:
        return False
    return t1.val == t2.val\
        and symmetric(t1.left, t2.right)\
        and symmetric(t1.right, t2.left)

def is_symmetric(root: typing.Optional[bt.TreeNode]) -> bool:
    if root is None:
        return True
    return symmetric(root, root)

#def is_also_symmetric(root: typing.Optional[TreeNode]) -> bool:
