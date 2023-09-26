from interqu import valid_parenthesis as t

def test_01():
    assert(t.valid_parenthesis('()') == True)
    assert(t.valid_parenthesis('()[]{}') == True)
    assert(t.valid_parenthesis('(]') == False)
