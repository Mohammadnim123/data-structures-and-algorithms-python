import pytest
from data_structures_and_algorithms.challenges.depth_first.depth_first import *

def test_import():
    g = NewGraph()
    assert g.add_double_edge

def test_depth_first(made_graph):

    graph = made_graph[0]
    apple = made_graph[1][0]
    
    assert graph.depth_first(apple) == made_graph[1]

def test_no_edges():
    graph = NewGraph()

    # add all nodes
    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    cantelope = graph.add_node('cantelope')
    dates = graph.add_node('dates')
    eggplant = graph.add_node('eggplant')
    figs = graph.add_node('figs')

    assert graph.depth_first(apple) == [apple]

def test_directional_edges():
    graph = NewGraph()

    # add all nodes
    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    cantelope = graph.add_node('cantelope')
    dates = graph.add_node('dates')
    eggplant = graph.add_node('eggplant')
    figs = graph.add_node('figs')

    # add some edges
    graph.add_edge(apple, banana, 1)

    graph.add_edge(banana, figs, 4)

    graph.add_edge(figs, eggplant, 20)

    assert graph.depth_first(apple) == [apple, banana, figs, eggplant]



@pytest.fixture
def made_graph():
    graph = NewGraph()

    # add all nodes
    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    cantelope = graph.add_node('cantelope')
    dates = graph.add_node('dates')
    eggplant = graph.add_node('eggplant')
    figs = graph.add_node('figs')

    # add all edges
    # graph.add_edge(apple, banana, 1)
    # graph.add_edge(banana, apple, 2)
    graph.add_double_edge(apple, banana, 3)

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

    return (graph, [apple,banana,cantelope,figs,dates,eggplant])