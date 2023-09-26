'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'
'''

def opens(p: str) -> bool:
    return p == '('  or p == '{' or p == '['

def closes(p: str) -> bool:
    return not opens(p)

def match(p: str) -> str:
    if p == '[':
        return ']'
    elif p == '{':
        return '}'
    elif p == '(':
        return ')'
    else:
        return '*'

def valid_parenthesis(ps: str) -> bool:
    st = []
    for s in ps:
        if opens(s):
            st.append(s)
        elif closes(s):
            if len(st) == 0:
                return False
            o = st.pop()
            if not match(o) == s:
                return False
        else:
            return False

    return len(st) == 0





