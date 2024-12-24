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
1.    **Represent the Graph:** Use an adjacency list to represent the directed graph.
2.    **Mark Visited Nodes:** Use a visited array to track visited nodes.
3.    **DFS Traversal**
          *    For each unvisited node, perform a DFS traversal.
          *    Mark the current node as visited.
          *    Recursively visit all its neighbors.
          *    Once all neighbors are processed, add the current node to a stack (postorder traversal).
4.    **Check for Cycle:** Maintain a recursion stack to detect cycles in the graph.
5.    **Build Result:** Once DFS is complete for all nodes, the stack contains the topological order (reverse the stack to get the order).

  ## Time Complexity: O(V+E)
  ## Space Complexity: O(V)
