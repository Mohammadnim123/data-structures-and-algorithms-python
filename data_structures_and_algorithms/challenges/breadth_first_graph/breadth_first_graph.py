from queue import Queue
from data_structures_and_algorithms.data_structures.graph.graph import Graph


def breadth_first(graph, start_node):

        if start_node not in graph._adjacency_list:
                raise Exception('this node not in the graph')

        q = Queue()
        q.enqueue(start_node)
        visited_nodes = {}
        visited_nodes[start_node] = True
        output = []

        while len(q):
            cur = q.dequeue()
            output.append(cur)
            neighbors = graph._adjacency_list[cur]
            for n in neighbors:
                if n[0] not in visited_nodes:
                    q.enqueue(n[0]) 
                visited_nodes[n[0]] = True
        return output

if __name__ == "__main__":
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    
    g.add_edge(a,b,5)
    g.add_edge(b,c,5)
    g.add_edge(b,a,5)
    g.add_edge(c,a,5)

    print(breadth_first(g, a))

