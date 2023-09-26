'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

import typing
import itertools

def product(nums: typing.List[int]) -> typing.List[int]:
    left_to_right = [1] * len(nums) 
    for i in range(1, len(nums)):
        left_to_right[i] = left_to_right[i-1] * nums[i-1]

    right_to_left = [1] * len(nums) 
    for i in reversed(range(0, len(nums) - 1)):
        right_to_left[i] = right_to_left[i+1] * nums[i+1]

    prod = []
    for (l, r) in itertools.zip_longest(left_to_right, right_to_left):
        prod.append(l * r)

    return prod
