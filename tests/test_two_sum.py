from interqu import two_sum


def test_01():
    idxs = two_sum.two_sum(xs = [2, 7, 11, 15], target = 9, limits = (-109, 109))
    i = min(idxs[0], idxs[1])
    j = max(idxs[0], idxs[1])
    assert(i == 0)
    assert(j == 1)

def test_02():
    idxs = two_sum.two_sum(xs = [3, 2, 4], target = 6, limits = (-109, 109))
    i = min(idxs[0], idxs[1])
    j = max(idxs[0], idxs[1])
    assert(i == 1)
    assert(j == 2)

def test_03():
    idxs = two_sum.two_sum(xs = [3, 3], target = 6, limits = (-109, 109))
    i = min(idxs[0], idxs[1])
    j = max(idxs[0], idxs[1])
    assert(i == 0)
    assert(j == 1)



