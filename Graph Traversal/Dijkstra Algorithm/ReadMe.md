## Dijkstra's Algorithm
Dijkstra's algorithm is a graph traversal technique used to find the shortest path from single source of node to all other nodes in a graph. It works on graphs with non-negative edge weights and is optimal for such cases.

###Key Characteristics:
 * **Graph Type**: Directed or undirected graphs with non-negative weights.
 * **Time Complexity**: O((V+E).log V) using a priority Queue(min-heap)
 * **Output**: Shortest path from the source to all nodes, or to a specific node if required.
 

## Steps to Solve Dijkstra's Algorithm
	1. Initialization:
		* Assign a distance of infinity to all nodes except the source node, which gets a distance of 0.
		* User priority queue(min-heap) to store nodes based on their current shortest distance.
		
	2. Relaxation Process:
		* Extract the node with the smallest distance from the queue.
		* Update the distance to its neighbour if a shortest path is found via the current node.
	
	3. Terminiation:
		* The algorithm ends when all nodes have been processed, or the shortest distance to the target node is determined.
	
	4. Backtrack for Path Reconstruction(Optional):
		* To find the actual path, maintain a parent map to track how each node was reached.
		

## When to Use Dijkstra's Algorithm
	1. Shortest Path in Weighted Graphs.
		Finding the shortest distance in road networks, delivery systems, or navigation apps.
	2. Resource Optimization Problems:
		Problems where you need to minimize cost, time or distance.
	3. Non-Negative Edge Weights:
		If edge weights are negative, consider Bellman-for or other algorithms.
		


## Example Code

	public int[] dijkstra(int n, int[][] edges, int source) {
        // Adjacency List representation of the graph
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) graph.put(i, new ArrayList<>());
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph.get(u).add(new int[]{v, w});
            graph.get(v).add(new int[]{u, w}); // For undirected graph
        }

        // Min-Heap to get the node with the smallest distance
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[]{source, 0});

        // Distance array
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[source] = 0;

        // Dijkstra's Algorithm
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int node = current[0], distance = current[1];

            if (distance > dist[node]) continue; // Skip outdated entries

            for (int[] neighbor : graph.get(node)) {
                int nextNode = neighbor[0], weight = neighbor[1];
                if (dist[node] + weight < dist[nextNode]) {
                    dist[nextNode] = dist[node] + weight;
                    pq.offer(new int[]{nextNode, dist[nextNode]});
                }
            }
        }

        return dist; // Contains shortest distances from the source to all nodes
    }


## LeetCode Problems to Build Intuition
	1. Network Delay Time (#743)
		Find the time it takes for all nodes to receive a signal from a source node.
		**Key Insight**: Treat it as a shortest path problem using Dijkstra
	2. Path With Minimum Effort (#1631)
		Minimize the maximum effort required to traverse from top-left to bottom-right corner of grid.
		**KeyInsight**: Use Dijkstra to explore paths minimizing the effort(cost).
	3. Cheapest Flight with K Stops (#787)
		Find the cheapest flight route between two cities at most K stops.
		**Key Insight**: Modified Dijkstra using stops as an additional constraint.
	4. Shortest Path in a Grid with Obstacles Elimination (#1293)
		Shortest Path in a grid with obstacles you can eliminate.
		**Key Insight**: Use Dijkstra or BFS with additional state tracking.
	5. Swin in Rising Water (#778)
		Minimize the maximum water level required to reach the bottom-right corner
		**Key Insight**: Use a priority queue to minimize the maximum "cost" on the path.
	6. Minimum Cost to Reach Destination in Time(#1928).
		Minimize the cost to reach a destination within a given time.
		**Key Insight**: Use Dijkstra with additional constraints.
		
		
## How to Build Intuition for Interviews
	1. Understand Problem Requirements:
		Look for terms like "shortest path","minimum cost", or "minimum distance".
		Check if weights as non-negative.
	2. Recognize tht Graph Representation:
		Grid can often be treated as graphs where adjacent cells are connected.
		Explicit edges suggest adjacency list/matrics.
	3. Plan the Approach
		Is the graph unweighted? Use BFS
		Are weights involved? Use Dijkstra
		Do weights include negative values? Consider Bellman-ford or Floyd Warshall.
	4. Simulate on Small Examples:
		Draw a graph and manually simulate Dijkstra's steps to understand updates.
	5. Practice Problems:
		Start with straightforward problem like Network Delay time.
		Gradually move to advance problems with constraints like at most K stops.
		
		
## Key Interview Tips
1.	Explain the Algorithm
	*	Be ready to explain why Dijkstra works and how the priority queue is used.
2.	Time Complexity:
	*	Mention the complexity: O((V+E).log V)
3. 	Edge Case:
	*	Handle disconnected graphs, unreachable nodes, and single-node graphs.
4.	Variants:
	*	Be prepared for modifications, such as limiting stops or adding constraints.
	

## Interview Question Framework
1.	Understand the input/output.
	*	What's the input(graph represenstation)? What's the output(shortest path, distance)?
2.	Graph Representation
	*	Clarify if the graph is given as an adjacency list, matrix, or edge list.
3.	Constraints
	*	Non-negative weights? Specific constraints like "K stops" or "minimize efforts"?
4.	Edge Cases:
	*	Handle scenarios like isolated nodes or graph with no connections.
5.	Code and Explain	
	*	Write clean, modular code with comments
	*	Use helper functions for readability.