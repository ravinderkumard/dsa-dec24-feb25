class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        

        adj_list = [[] for _ in range(n)]

        if len(connections)<n-1:
            return -1

        for u,v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n
        components = 0

        def dfs(node):
            visited[node] = True
            for next in adj_list[node]:
                if not visited[next]:
                    dfs(next)

        for i in range(n):
            if not visited[i]:
                components+=1
                dfs(i)

        return components-1