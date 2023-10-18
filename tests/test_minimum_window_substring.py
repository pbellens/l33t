from l33t import minimum_window_substring as t


def test_01():
    found = t.substring(s = 'ADOBECODEBANC', t = 'ABC')
    assert(found == 'BANC')

def test_02():
    found = t.substring(s = 'A', t = 'A')
    assert(found == 'A')

def test_03():
    found = t.substring(s = 'A', t = 'AA')
    assert(found == '')
