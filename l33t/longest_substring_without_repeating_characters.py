"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def longest_substring(s: str) -> int:
    l = 0
    r = 0
    seen = {}
    res = -1

    while r != len(s):
        print(f'{l}-{r} ({seen.items()})')
        if s[r] in seen.keys():
            if (r-l) > res:
                res = r-l
            skip = seen[s[r]]
            for i in range(l,skip+1):
                seen.pop(s[i])
            l = skip+1
        seen[s[r]] = r
        r += 1

    return res
