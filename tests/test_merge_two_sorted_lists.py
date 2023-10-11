from l33t import merge_two_sorted_lists as t
from l33t import singly_linked_list as l


def test_01():
    assert(t.merge(l.create([1, 2, 4]), l.create([1, 3, 4])).as_list() == [1, 1, 2, 3, 4, 4])

def test_02():
    assert(t.merge(l.create([]), l.create([])).as_list() == [])

def test_03():
    assert(t.merge(l.create([]), l.create([0])).as_list() == [0])
