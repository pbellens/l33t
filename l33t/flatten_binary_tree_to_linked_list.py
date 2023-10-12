'''
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to 
the next node in the list and the left child pointer is always null. The "linked list" should 
be in the same order as a pre-order traversal of the binary tree.

For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
 

Constraints:
Do not return anything, modify root in-place instead.
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''

import typing
from . import binary_tree as bt


def flatten_internal(root: typing.Optional[bt.TreeNode], rights: typing.List[bt.TreeNode]) -> None:
    if root is None:
        return
    print(f'root {root.val} rights {len(rights)}|{rights[-1].val if rights else None}')
    left = root.left
    right = root.right
    if left:
        print(f'left {left.val}')
        root.left = None
        root.right = left
    else:
        if rights:
            left = rights.pop()
            root.left = None
            root.right = left
        else:
            return
    if right:
        print(f'right {right.val if right else None}')
        rights.append(right)
    print()
    flatten_internal(root.right, rights)

def flatten(root: typing.Optional[bt.TreeNode]) -> None:
    flatten_internal(root, [])

