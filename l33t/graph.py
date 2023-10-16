import typing
from dataclasses import dataclass


@dataclass
class Node:
    value: typing.Any
    neighbors: typing.Set

    def __str__(self):
        nsrep = ','.join(map(lambda n: str(n.value), self.neighbors))
        return f'{self.value}: {nsrep}'

    def __hash__(self):
        return self.value
    
@dataclass
class Graph:
    roots: typing.List[Node]
    nodes: typing.List[Node]

    def __str__(self): 
        return '\n'.join(map(lambda n: str(n), self.nodes))


def create(adjl: typing.List[typing.List[int]], seen: typing.Dict = {}) -> typing.Optional[Graph]:
    for i, ns in enumerate(adjl, 1):
        present = i in seen
        neighbors = set() if not present else seen[i].neighbors
        for n in ns:
            if n in seen:
                neighbors.add(seen[n])
            else:
                neighbor = Node(value = n, neighbors = set())
                seen[n] = neighbor
                neighbors.add(neighbor)
        if not present:
            seen[i] = Node(value = i, neighbors = neighbors)

    return Graph(roots=[], nodes = list(seen.values())) if adjl else None


def print_connected_component(node: Node):
    to_visit = [node]
    seen = set()

    while to_visit:
        n = to_visit.pop()
        if not n.value in seen:
            print(n)
            seen.add(n.value)
            to_visit.extend((n for n in n.neighbors if not n.value in seen))
