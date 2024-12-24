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

import java.util.*;

public class DFSTopologicalSort {
    public static List<Integer> topologicalSort(int numNodes, List<int[]> edges) {
        // Step 1: Build the graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < numNodes; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
        }

        // Step 2: Initialize visited and stack
        boolean[] visited = new boolean[numNodes];
        Stack<Integer> stack = new Stack<>();
        boolean[] onPath = new boolean[numNodes]; // For cycle detection

        // Helper function for DFS
        boolean dfs(int node) {
            if (onPath[node]) return false; // Cycle detected
            if (visited[node]) return true;

            visited[node] = true;
            onPath[node] = true;

            for (int neighbor : graph.get(node)) {
                if (!dfs(neighbor)) return false; // Cycle detected
            }

            onPath[node] = false;
            stack.push(node);
            return true;
        }

        // Step 3: Perform DFS for all nodes
        for (int i = 0; i < numNodes; i++) {
            if (!visited[i]) {
                if (!dfs(i)) {
                    throw new IllegalArgumentException("Cycle detected! Graph is not a DAG.");
                }
            }
        }

        // Step 4: Reverse stack to get topological order
        List<Integer> topologicalOrder = new ArrayList<>();
        while (!stack.isEmpty()) {
            topologicalOrder.add(stack.pop());
        }
        return topologicalOrder;
    }

    public static void main(String[] args) {
        List<int[]> edges = Arrays.asList(
                new int[]{5, 0}, new int[]{5, 2}, new int[]{4, 0}, 
                new int[]{4, 1}, new int[]{2, 3}, new int[]{3, 1});
        System.out.println(topologicalSort(6, edges)); // Output: [5, 4, 2, 3, 1, 0]
    }
}



# Kahn's Algorithm (BFS-Based Topological Sort)
This approach uses Breadth First Search (BFS) with an in-degree array to find the topological order.

## Steps:
1.    **Calculate In-Degree:** Use and in-degree array to count incoming edge for each node.
2.    **Queue Initialization:** Add all nodes with in-degree=0 to a queue.
3.    **Process Nodes:**
          *    While the queue is not empty:
              * Remove a node from the queue and add it to the result
              * Reduce the in degree of it neigbhour by 1.
              * If any neigbhour's in-degree  becomes 0, add it ot the queue.
4.    **Cycle Detection**: If the result doesnot include all nodes, the graph contains a cycle.

  ## Time Complexity: 
      O(V+E)
## Space Complexity:
    O(V)


    import java.util.*;

public class BFSTopologicalSort {
    public static List<Integer> topologicalSort(int numNodes, List<int[]> edges) {
        // Step 1: Build the graph and in-degree array
        Map<Integer, List<Integer>> graph = new HashMap<>();
        int[] inDegree = new int[numNodes];
        for (int i = 0; i < numNodes; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            inDegree[edge[1]]++;
        }

        // Step 2: Initialize the queue with nodes having in-degree 0
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numNodes; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        // Step 3: Process nodes in the queue
        List<Integer> topologicalOrder = new ArrayList<>();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            topologicalOrder.add(node);

            for (int neighbor : graph.get(node)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        // Step 4: Check for cycles
        if (topologicalOrder.size() != numNodes) {
            throw new IllegalArgumentException("Cycle detected! Graph is not a DAG.");
        }

        return topologicalOrder;
    }

    public static void main(String[] args) {
        List<int[]> edges = Arrays.asList(
                new int[]{5, 0}, new int[]{5, 2}, new int[]{4, 0}, 
                new int[]{4, 1}, new int[]{2, 3}, new int[]{3, 1});
        System.out.println(topologicalSort(6, edges)); // Output: [5, 4, 2, 3, 1, 0]
    }
}


## Key Points in Both Approaches:
1.    **Graph Represenation:** We used a Map<Integer,List<Integer>> to represent the adjancey List.
2.    **Cycle Detection:** DFS approach use a boolean[] onPath array, BFS approach check if all nodes are processed.
3.    **Edge Cases:** Disconnected Graphs, Graph with cycle.


| Aspect | DFS-Based Topological Sort    | Kahn's Algorithm(BFS Based)    |
| :-----: | :---: | :---: |
| **Traversal Method** | DFS   | BFS   |
| **Cycle Detection** | Recursion stack   | In-degree not reducing to 0 for all nodes   |
| **Result Construction** | Uses a stack(postorder reversal)   | Directly constructs result from queue   |
| **Use case** | Preferred for recursive problems   | Prefered for iterative problems  |



## Problems:
### Beginner Level
    1. Course Schedule (#207)
    2. Course Schedule II(#210)
### Intermediate Level
    1. Alien Dictionary(#269)
    2. Sequence Representation (#444)
### Advance Level
    1. Parallel Courses(#1136)
    2. Minimum Height Trees(#310)
    3. Reconstruct Itinerary(#332)
    4. Course Schedule III(630)


## More Problems
### Intermediate-Level Problems
    1.    Longest Path in Directed Acyclic Graph(Custom Problem)
    2.    Checking validity of an Alien Dictionary(#953)
    3.    Find Eventual Safe States(#802)
### Advanced-Level Problem
    1.    Minimum Tiime to complete All Tasks(#2050)
    2.    Find All Possible Recipes(#2115)
    3.    Number of ways to Reorder Array to Get Same BST(#1569)
    4.    Smallest String with Swaps(#1202)
    5.    Maximum number of Tasks you can Assign(#2071)
### Challenging Problems with Topological Sort
    1.    Number of Connected Components in an Undirected Graph(#323)
    2.    Longest Increasing Path in a Matrix(#329)
    3.    All Tasks Scheduling Order(Premium Problem)
    4.    Find Critical and Pseudo-Critical Edges of MST(#1489)
