from l33t import different_ways_to_add_parenthesis as t


def test_01():
    assert(t.different_ways('2-1-1') == [2, 0])

def test_02():
    res = t.different_ways('2*3-4*5')
    assert(set(res) == set([-34,-14,-10,-10,10]))
    assert(len(res) == len([-34,-14,-10,-10,10]))

