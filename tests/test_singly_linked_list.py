from interqu import singly_linked_list as t


def test_empty():
    l = t.empty()
    assert(l.length == 0)
    assert(l.head is None)
    assert(l.tail is None)

def test_create():
    l = t.create([1, 2, 3])
    assert(l.length == 3)
    assert(l.head is not None and l.head.value == 1)
    assert(l.tail is not None and l.tail.value == 3)
