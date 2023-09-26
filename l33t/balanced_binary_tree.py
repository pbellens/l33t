'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Output: true

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Output: false.
'''


import typing
from . import binary_tree as bt

def depth(root: typing.Optional[bt.TreeNode], d: int) -> int:
    if root is None:
        return d
    else: 
        return max(depth(root.left, d+1), depth(root.right, d+1))

def balanced(root: typing.Optional[bt.TreeNode]) -> bool:
    if root:
        return abs(depth(root.left, 0) - depth(root.right, 0)) < 2 \
            and balanced(root.left) and balanced(root.right)
    else: 
        return True
