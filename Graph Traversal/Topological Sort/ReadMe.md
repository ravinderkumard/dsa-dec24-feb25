# Tips for Preparation

1. Understand Graph Representation: Familiarize yourself with adjacency lists/matrices.
2. Learn Two Approaches:
    1. DFS-Based Topological Sort (Recursive with stack).
    2. Kahn’s Algorithm (Iterative with in-degree count).
Cycle Detection: Ensure you know how to detect cycles in a directed graph.
Practice Variations: Try problems that require calculating paths, depths, or lexicographical orders.
Optimize for Edge Cases: Test graphs with cycles, single nodes, and disconnected components.


# DFS Based Topological Sort
This approach uses Depth First Search (DFS) to find a valid topological order by exploring nodes deeply before adding them to the result.

## Steps:
1.    ** **Represent the Graph
