from interqu import swap_nodes_in_pairs as t
from interqu import singly_linked_list as sll


def test_01():
    l = sll.create([1, 2, 3, 4])
    swapped = t.swap(l.head)
    assert(swapped is not None)
    assert(swapped.value == 2)
    assert(swapped.next is not None)
    assert(swapped.next.value == 1)
    assert(swapped.next.next is not None)
    assert(swapped.next.next.value == 4)
    assert(swapped.next.next.next is not None)
    assert(swapped.next.next.next.value == 3)

def test_02():
    l = sll.create([])
    swapped = t.swap(l.head)
    assert(swapped is None)

def test_03():
    l = sll.create([1])
    swapped = t.swap(l.head)
    assert(swapped is not None)
    assert(swapped.value == 1)
    assert(swapped.next is None)
