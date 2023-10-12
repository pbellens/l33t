'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two 
subtrees of every node never differ by more than 1.

Example 1:
G iven the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5,null], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''

import typing
from . import binary_tree as bt


def make_tree(nums: typing.List[int]) -> typing.Optional[bt.TreeNode]:
    if nums is None or len(nums) == 0:
        return None
    if len(nums) == 1:
        return bt.TreeNode(val = nums[0], left = None, right = None)
    middle = int(len(nums) / 2)
    return bt.TreeNode(val = nums[middle], left = make_tree(nums[:middle]), right = make_tree(nums[middle+1:]))
