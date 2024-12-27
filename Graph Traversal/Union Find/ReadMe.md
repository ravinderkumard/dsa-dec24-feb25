# UNION FIND
Union Find(Disjoint Set Union) is a data structure used to efficiently manage a collection of disjoint sets and supports the following operations:
1.  **Find**: Determine which set a particular element belong to.
2.  **Union**: Merge two sets into one.

This approach is particualarly  useful for solving graph connectivity problems including:
  * Dectecting Cycle
  * Determining connected components.
  * Solvinng Minimum Spanning Tree(like kruskal's algorithm)

### When to User Union Find
1. The graph is undirected, and you want to:
     * Detect cycles
     * Find Connected components
2. You need to handle dynamic connectivity, such as adding edges over time.
3. You are solving optimization problem like MST(Minimum Spanning Tree).


### Key Operations
1. Find with Path Compression: This operation finds the root of the element and flattens the structure, ensuring future queries are faster.
2. Union by Rank/Size: This ensure that the smaller set is merged under the root of larger set, optimizing the performance.

### Steps for Solving Graph Problem with Union-Find.
1. Initialize Parent and Rank Arrays:
    * parent[i] points to the parent of the node i.
    * rank[i] keeps track of the height or size of the tree to optimize merging.
  
2. Define Find Function(with path compression):
    Ensure every node directly points to the root, reducing the tree height.
3. Define Union Function(with union by Rank):
     Always attach the smaller tree under the larger tree to keep the structure balanced.
4. Iterate through edges:
     For each edge, check if the two nodes belong to the same set.
     If not, merge them
     If they already belong to the same set, a cycle exists.

   ![image](https://github.com/user-attachments/assets/56730927-3d08-4bba-91f4-e9b0d9d18b93)

  Path compression:
  ![image](https://github.com/user-attachments/assets/14056a50-d722-4335-bb3e-f3dfdba9bc9f)

  ![image](https://github.com/user-attachments/assets/48635f69-3681-48fb-8769-7b544d3da42b)

![image](https://github.com/user-attachments/assets/0d069c1a-83bb-4b11-8249-9a923c4b83ec)

