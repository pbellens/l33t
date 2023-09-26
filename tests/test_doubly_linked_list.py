from interqu import doubly_linked_list as dll


def test_creation():
    l = dll.empty()
    assert(l.head == None)
    assert(l.tail == None)
    assert(l.size == 0)

def test_push():
    l = dll.empty()
    l.push_back(1)
    l.push_back(2)
    l.push_back(3)
    assert(l.head is not None and l.head.val ==1)
    assert(l.head.next is not None and l.head.next.val == 2)
    assert(l.head.next.next is not None and l.head.next.next.val == 3)
    assert(l.size == 3)

def test_create():
    l = dll.create([1,2,3])
    assert(l.head is not None and l.head.val ==1)
    assert(l.head.next is not None and l.head.next.val == 2)
    assert(l.head.next.next is not None and l.head.next.next.val == 3)
    assert(l.size == 3)

def test_reverse():
    l = dll.create([1,2,3])
    l.reverse()
    assert(l.head is not None and l.head.val == 3)
    assert(l.head.next is not None and l.head.next.val == 2)
    assert(l.head.next.next is not None and l.head.next.next.val == 1)
    assert(l.size == 3)
