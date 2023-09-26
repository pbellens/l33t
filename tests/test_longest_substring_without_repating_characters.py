from interqu import longest_substring_without_repeating_characters as t

def test_01():
    assert(t.longest_substring('abcabcbb') == 3)
    assert(t.longest_substring('bbbbb') == 1)
    assert(t.longest_substring('pwwkew') == 3)

