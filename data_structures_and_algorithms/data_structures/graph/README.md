# Graphs
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

Here is some common terminology used when working with Graphs:

* Vertex - A vertex, also called a “node”, is a data object that can have zero or more adjacent vertices.
* Edge - An edge is a connection between two nodes.
* Neighbor - The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.
* Degree - The degree of a vertex is the number of edges connected to that vertex.

## Challenge
Implement the graph, which should be represented as an adjacency list, and should include the following methods: add_node(), add_edge(), get_nodes(), get_neighbors(), size()

## Approach & Efficiency
* add_node() time Big O(1), space Big O(1)
* add_edge() time Big O(1), space Big O(1)
* get_nodes() time Big O(1), space Big O(1)
* get_neighbors() time Big O(1), space Big O(1)
* size() time Big O(1), space Big O(1)

## API
class Node():

Class to create Vertex with the given value
Input: Vertex value
class Graph():

class to implement Graph object with the given methods:
add_node():

Adds a new vertex to the graph
Input: the value of that vertex
Output: the added vertex
add_edge():

Adds a new edge between two nodes in the graph with ability to add weight
Input: two vertexes to be connected by the edge
Both nodes should already be in the Graph
get_nodes():

Returns all of the vertexes in the graph as a collection
get_neighbors():

Returns a collection of vertexes connected to the given vertex with the weights of their connections
Input: Takes in a given vertex
size():

Returns the total number of nodes in the graph