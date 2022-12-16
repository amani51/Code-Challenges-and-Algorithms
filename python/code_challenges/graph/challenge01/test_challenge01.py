# Write your test here
from challenge01 import Graph


def test_breadth_first1():
    graph = Graph()

    a = graph.add_node("A")
    b = graph.add_node("B")
    c = graph.add_node("C")
    d = graph.add_node("D")

    graph.add_edge(a,b)
    graph.add_edge(a,c)
    graph.add_edge(c,b)
    graph.add_edge(d,b)
    graph.add_edge(d,c)

    assert graph.breadth_first(a)==['A', 'B', 'C', 'D']
    assert graph.breadth_first(d)==['D', 'B', 'C', 'A']


def test_breadth_first2():
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h= graph.add_node('H')
    i= graph.add_node('I')
    k= graph.add_node('K')

    graph.add_edge(a,c)
    graph.add_edge(a,e)
    graph.add_edge(a,b)

    graph.add_edge(c,f)
    graph.add_edge(b,d)
    graph.add_edge(e,g)
    graph.add_edge(e,d)
    graph.add_edge(e,f)

    graph.add_edge(f,i)
    graph.add_edge(g,h)
    graph.add_edge(f,h)

    graph.add_edge(i,k)
    graph.add_edge(h,k)


    assert graph.breadth_first(a)==['A', 'C', 'E', 'B', 'F', 'G', 'D', 'I', 'H', 'K']
    assert graph.breadth_first(k)==['K', 'I', 'H', 'F', 'G', 'C', 'E', 'A', 'D', 'B']

