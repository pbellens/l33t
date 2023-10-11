from l33t import linked_list_cycle as t
from l33t import singly_linked_list as l


def test_01():
    ls = l.create(range(5))
    assert(t.has_cycle(ls) == False)

def test_02():
    ls = l.create([3, 2, 0, -4])
    ls.tail.next = ls.head.next
    assert(t.has_cycle(ls) == True)

def test_03():
    ls = l.create([1, 2])
    ls.tail.next = ls.head
    assert(t.has_cycle(ls) == True)

def test_04():
    ls = l.create([1])
    assert(t.has_cycle(ls) == False)
    
    
    
    
    
    
    
    
