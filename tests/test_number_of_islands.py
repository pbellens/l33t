from l33t import number_of_islands as t


def test_01():
    count = t.count_islands(
        grid = [
            [1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]])
    assert(count == 1)

def test_02():
    count = t.count_islands(
        grid = [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]])
    assert(count == 3)

