import pytest
from data_structures_and_algorithms.data_structures.graph.graph import *
from data_structures_and_algorithms.challenges.get_edge.get_edge import get_edge

@pytest.fixture
def made_graph():
    graph = Graph()

    # add all nodes
    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    cantelope = graph.add_node('cantelope')
    dates = graph.add_node('dates')
    eggplant = graph.add_node('eggplant')
    figs = graph.add_node('figs')

    # add all edges
    graph.add_edge(apple, banana, 1)

    graph.add_edge(banana, apple, 2)
    graph.add_edge(banana, cantelope, 3)
    graph.add_edge(banana, figs, 4)

    graph.add_edge(cantelope, banana, 5)
    graph.add_edge(cantelope, figs, 6)
    graph.add_edge(cantelope, dates, 7)

    graph.add_edge(figs, banana, 8)
    graph.add_edge(figs, cantelope, 9)
    graph.add_edge(figs, dates, 10)
    graph.add_edge(figs, eggplant, 20)

    graph.add_edge(dates, cantelope, 30)
    graph.add_edge(dates, figs, 40)
    graph.add_edge(dates, eggplant, 50)

    graph.add_edge(eggplant, figs, 60)
    graph.add_edge(eggplant, dates, 70)

    return graph

def test_graph_empty():
    graph = Graph()
    lst = ['a','b','c']

    assert get_edge(graph, lst) == 'False : $0'

def test_cities_empty(made_graph):
    graph = made_graph
    lst = []
    assert get_edge(graph, lst) == 'False : $0'

def test_city_not_in_graph(made_graph):
    graph = made_graph
    lst = ['apple', 'banana', 'watermellon']
    assert get_edge(graph, lst) == 'False : $0'

def test_graph_no_edges():
    graph = Graph()
    lst = ['apple', 'banana', 'cantelope']
    # add all nodes
    graph.add_node('apple')
    graph.add_node('banana')
    graph.add_node('cantelope')
    graph.add_node('dates')
    graph.add_node('eggplant')
    graph.add_node('figs')

    assert get_edge(graph, lst) == 'False : $0'

def test_graph_with_correct_edges(made_graph):
    lst = ['apple','banana','cantelope','dates','eggplant','figs']

    assert get_edge(made_graph,lst) == 'True : $121'

def test_one_city(made_graph):
    lst = ['apple']

    assert get_edge(made_graph,lst) == 'False : $0'    