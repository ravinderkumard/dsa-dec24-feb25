class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        Create an adj list and try to define the values.
        Then from the list run DFS check how many groups we can create if that belong to more that 2 groups or just 1 group we can return false.
        """

        adj = [[] for _ in range(n+1)]

        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        color = [0]*(n+1)

        def dfs(node):
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = 3-color[node]

                    if not dfs(neighbor):
                        return False
                elif color[neighbor] == color[node]:
                    return False
            
            return True

        for person in range(1,n+1):
            if color[person]==0:
                color[person] = 1
                if not dfs(person):
                    return False
        
        return True