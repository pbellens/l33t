from l33t import merge_intervals as t


def test_01():
    assert(t.merge([(1,3),(2,6),(8,10),(15,18)]) == [(1,6), (8,10), (15,18)])

def test_02():
    assert(t.merge([(1,4),(4,5)]) == [(1,5)])

def test_03():
    assert(t.merge([(1,4)]) == [(1,4)])

def test_04():
    assert(t.merge([]) == [])
