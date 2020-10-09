# Challenge Summary

The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array. For simplicity, it is assumed that all vertices are reachable from the starting vertex.

## Challenge Description

Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

## Approach & Efficiency

For time efficency it is O(N)
For space efficency it is O(N)

## Solution
![breadth_first_graph](../../../assets/breadth_first_graph.png)