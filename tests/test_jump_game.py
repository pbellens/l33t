from l33t import jump_game as t


def test_01():
    assert(t.can_reach([2,3,1,1,4]) == True)

def test_02():
    assert(t.can_reach([3,2,1,0,4]) == False)


