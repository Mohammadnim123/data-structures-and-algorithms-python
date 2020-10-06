from data_structures_and_algorithms.data_structures.graph.graph import *

def get_edge(graph, cities):

    price = 0
    is_neighbor = False

    if not cities:
        return f'{is_neighbor} : ${price}'

    nodes = graph.get_nodes()
    if not nodes:
        return f'{is_neighbor} : ${price}'
        
    city_nodes = []
    for city in cities:
        for node in nodes:
            if city == node.value:
                city_nodes.append(node)
    if len(cities) != len(city_nodes):
        return f'{is_neighbor} : ${price}'

    neighbors = graph.get_neighbors(city_nodes[0])

    for i in range(1, len(city_nodes)):
        is_neighbor = False
        for neighbor in neighbors:
            if neighbor[0] == city_nodes[i]:
                price += neighbor[1]
                is_neighbor = True
                break
        if not is_neighbor:
            return f'{is_neighbor} : $0'
        neighbors = graph.get_neighbors(city_nodes[i])

    return f'{is_neighbor} : ${price}'



if __name__ == "__main__":
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


    print(get_edge(graph,['apple','banana','cantelope','dates','eggplant','figs']))