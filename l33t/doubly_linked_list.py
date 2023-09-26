import typing
import functools
from dataclasses import dataclass


@dataclass
class Node:
    val: typing.Any
    next: typing.Any
    prev: typing.Any

    def __repr__(self): 
        return f'({self.val}@{id(self)})'

@dataclass
class LinkedListIterator:
    current: Node

    def __next__(self):
        if self.current == None:
            raise StopIteration
        n = self.current
        self.current = self.current.next
        return n

@dataclass
class LinkedList:
    head: typing.Optional[Node]
    tail: typing.Optional[Node]
    size: int

    def __iter__(self):
        return LinkedListIterator(current = self.head)

    def __repr__(self):
        return '[' + ','.join(str(x.val) for x in self) + ']'

    def __len__(self): 
        return self.size

    def push_back(self, v):
        if self.size == 0:
            self.head = Node(next = None, prev = None, val = v)
            self.tail = self.head
        else:
            n = Node(next = None, prev = self.tail, val = v)
            self.tail.next = n
            self.tail = n
        self.size += 1
        return self
        
    def remove(self, n: Node): 
        n.prev.next = n.next
        n.next.prev = n.prev
        n.next = n.prev = None
        self.size -= 1

    def find(self, val) -> typing.Optional[Node]:
        return next((x for x in self if x.val == val))

    def reverse(self):
        if self.size > 1:
            cur = self.head.next
            prev = self.head
            while cur is not None:
                print(f'at {prev.val},{cur.val}')
                prev.prev = cur
                newcur = cur.next
                cur.next = prev
                prev = cur
                cur = newcur
            self.head, self.tail = self.tail, self.head
            self.head.prev = None
            self.tail.next = None


def empty() -> LinkedList:
    return LinkedList(head = None, tail = None, size = 0)

def create(vals: typing.Sequence) -> LinkedList:
    return functools.reduce(
        lambda acc, v: acc.push_back(v), 
        vals, 
        empty())
