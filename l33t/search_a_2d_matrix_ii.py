'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
'''


import typing
import itertools

def search_wavefront(matrix: typing.List[typing.List[int]], target: int) -> bool:
    scope = len(matrix)
    for r in matrix:
        for i in range(scope):
            if r[i] == target:
                return True
            elif r[i] > target:
                if i == 0: 
                    return False
                scope = i
                break
            else:
                continue

    return False

def search_hop(matrix: typing.List[typing.List[int]], target: int) -> bool:
    i = len(matrix) -1
    j = 0

    for _ in range(len(matrix) + len(matrix[0]) - 2):
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j += 1
        else:
            i -= 1

    return False
