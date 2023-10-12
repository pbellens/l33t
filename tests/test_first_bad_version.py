from l33t import first_bad_version as t


def test_01():
    assert(t.bad([True, True, True, False, True]) == 3)

def test_02():
    assert(t.bad([False]) == 0)
