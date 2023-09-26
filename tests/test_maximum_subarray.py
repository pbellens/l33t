from interqu import maximum_subarray as t


def test_01():
    assert(t.max_sub([-2,1,-3,4,-1,2,1,-5,4]) == 6)
        
def test_02():
    assert(t.max_sub([1]) == 1)

def test_03():
    assert(t.max_sub([5,4,-1,7,8]) == 23)
