'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''


import typing
from . import binary_tree as bt

def traverse(root: typing.Optional[bt.TreeNode]) -> typing.List[typing.List[int]]:
    res = []

    level = [root]
    while level:
        nextlevel = []
        for l in level:
            if l:
                nextlevel.append(l.left)
                nextlevel.append(l.right)
        ns = [n.val for n in level if n]
        if ns:
            res.append(ns)
        level = nextlevel

    return res

        

        
        

    
   

