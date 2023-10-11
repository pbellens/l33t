from l33t import pi


def test_100it():
    a = pi.approximate(100)
    assert(a < 3.5)
    assert(a > 2.5)

def test_1000it():
    a = pi.approximate(1000)
    assert(a < 3.3)
    assert(a > 2.9)

def test_10000it():
    a = pi.approximate(10000)
    assert(a < 3.2)
    assert(a > 3.1)




