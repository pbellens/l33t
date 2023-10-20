'''
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

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


def bottom_up(root: typing.Optional[bt.TreeNode]) -> typing.List[typing.List[int]]:
    if not root:
        return []

    levels = [[root]]
    while True:
        fresh = []
        for n in levels[-1]:
            if n.left: 
                fresh.append(n.left)
            if n.right: 
                fresh.append(n.right)
        if not fresh:
            break
        else:
            levels.append(fresh)

    result = []
    while levels:
        l = levels.pop()
        result.append(list(map(lambda n: n.val, l)))

    return result
