'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem 
without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
 

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
 
Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''


import typing
from . import singly_linked_list as sll

def swap(head: typing.Optional[sll.Node]) -> typing.Optional[sll.Node]:
    if head is None:
        return None

    if head.next is None:
        return head

    result = head.next 
    
    h = head
    prev = None
    while h is not None and h.next is not None:
        nexth = h.next.next

        next = h.next
        next.next = h
        h.next = nexth

        if prev is not None:
            prev.next = next

        prev = h
        h = nexth

    return result
