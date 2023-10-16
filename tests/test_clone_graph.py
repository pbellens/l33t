from l33t import clone_graph as t
from l33t import graph 


def test_01():
    g = graph.create([[2,4],[1,3],[2,4],[1,3]])
    someenode = next(iter(g.nodes))
    cloned = t.clone(next(iter(g.nodes)) )
    graph.print_connected_component(cloned)
