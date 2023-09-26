from interqu import counting_bits as t

def test_01():
    assert(t.count(2) == [0, 1, 1])

def test_02():
    assert(t.count(5) == [0, 1, 1, 2, 1, 2])
