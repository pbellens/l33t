'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

from . import singly_linked_list as sll

def merge(l1: sll.List, l2: sll.List) -> sll.List:
    res = sll.empty()

    c1 = l1.head
    c2 = l2.head
    while c1 is not None or c2 is not None:
        l1cand = c1.value if c1 is not None else 101 
        l2cand = c2.value if c2 is not None else 101 
        if l1cand <= l2cand:
            c1 = c1.next
            res.push_back(l1cand)
        else:
            c2 = c2.next
            res.push_back(l2cand)

    return res;




