from l33t import best_time_to_buy_and_sell_stock as t


def test_01(): 
    assert(t.max_profit([7,1,5,3,6,4]) == 5)

def test_02(): 
    assert(t.max_profit([7,6,4,3,1]) == 0)

