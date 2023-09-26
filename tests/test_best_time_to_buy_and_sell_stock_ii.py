from interqu import best_time_to_buy_and_sell_stock_ii as t


def test_01():
    assert(t.max_profit([7,1,5,3,6,4]) == 7)

def test_02():
    assert(t.max_profit([1,2,3,4,5]) == 4)

def test_03():
    assert(t.max_profit([7,6,4,3,1]) == 0)
