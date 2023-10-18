'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 
Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

import typing
from collections import defaultdict


def add(idx: int, s: str, found: typing.DefaultDict[str, int], missing: typing.Set[str], target: typing.Set[str]):
    if idx < len(s):
        fresh = s[idx]
        if fresh in target:
            found[fresh] += 1
            if found[fresh] == 1:
                missing.remove(fresh)

def remove(drop: str, found: typing.DefaultDict[str, int], missing: typing.Set[str], target: typing.Set[str]):
    if drop in target:
        found[drop] -= 1
        if found[drop] == 0:
            missing = missing.add(drop)

def substring(s: str, t: str):
    context = set(s)
    target = set(t)

    left = 0
    while not s[left] and left < len(s):
        left += 1
    if len(s) - left < len(t):
        return ''
    right = left + 1

    result = (0, 105)
    missing = set(t)
    found = defaultdict(int)
    add(left, s, found, missing, target)
    if not missing:
        result = (left, right)
    while left < len(s) and right < len(s)+1:
        if missing:
            add(right, s, found, missing, target)
            right += 1
            if not missing and right - left < result[1] - result[0]:
                result = (left, right)
        else:
            drop = s[left]
            left += 1
            remove(drop, found, missing, target)
            if not missing and right - left < result[1] - result[0]:
                result = (left, right)
    if result[1] != 105:
        return s[result[0]:result[1]]
    else: 
        return ''

