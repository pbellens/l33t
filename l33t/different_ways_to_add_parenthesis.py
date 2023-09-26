'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
'''


import typing 
import re

def is_operator(t: str) -> bool:
    return t == '+' or t == '-' or t == '*'

def apply_operator(t: str, l: int, r: int) -> int:
    if t == '+':
        return l + r
    elif t == '-': 
        return l - r
    else:
        return l * r
    

def different(expr: typing.List) -> typing.List[int]:
    if len(expr) == 1 and not is_operator(expr[0]):
        return expr
    else:
        res = []
        for i,t in enumerate(expr):
            if is_operator(t): # there will always be an i+1
                left = different(expr[:i])
                right = different(expr[i+1:])
                res.extend([apply_operator(t, l, r) for l in left for r in right])
        return res


def different_ways(expression: str) -> typing.List[int]:
    return different(
        list(
            map(
                lambda t: int(t) if not is_operator(t) else t, 
                re.split(r'([-+*])', expression))))
