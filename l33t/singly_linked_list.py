import typing
import functools
from dataclasses import dataclass


@dataclass
class Node:
    next: typing.Any
    value: typing.Any

@dataclass
class List:
    head: typing.Optional[Node]
    tail: typing.Optional[Node]
    length: int

    def push_back(self, value: typing.Any):
        n = Node(next = None, value = value)
        if self.length == 0:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.length += 1
        return self 

    def pop_front(self) -> typing.Optional[Node]:
        if self.length == 0:
            return None
        else:
            head = self.head
            self.head = head.next
            self.length -= 1
            head.next = None
            return head

    def as_list(self) -> typing.List:
        res = []
        head = self.head
        while head is not None:
            res.append(head.value)
            head = head.next
        return res

def empty() -> List:
    return List(head = None, tail = None, length = 0)

def create(xs: typing.Sequence[typing.Any]) -> List:
    return functools.reduce(
        lambda acc, v: acc.push_back(v), 
        xs,
        empty())

