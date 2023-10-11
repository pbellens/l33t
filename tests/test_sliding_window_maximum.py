from l33t import sliding_window_maximum as t


def test_01():
    assert(t.sliding_window_max([1,3,-1,-3,5,3,6,7], 3) == [3, 3, 5, 5, 6, 7])

def test_02():
    assert(t.sliding_window_max([1], 1) == [1])
