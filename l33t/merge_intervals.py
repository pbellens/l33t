'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''


import typing

def merge(intervals: typing.List[typing.Tuple[int, int]]) -> typing.List[typing.Tuple[int, int]]:
    if len(intervals) < 2:
        return intervals

    res = []
    cur = intervals[0]
    intervals = sorted(intervals)
    for i in intervals[1:]:
        if cur[1] < i[0]:
            res.append(cur)
            cur = i
        else: 
            cur = (cur[0], i[1])
    res.append(cur)

    return res
