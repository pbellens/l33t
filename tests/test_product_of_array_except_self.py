from interqu import product_of_array_except_self as t

def test_01():
    assert(t.product([1,2,3,4]) == [24,12,8,6])

