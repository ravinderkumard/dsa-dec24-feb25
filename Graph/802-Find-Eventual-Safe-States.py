class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        1. Identify the terminal node where outgoing edge is 0.
        2. Then check all the node that is reaching these terminal nodes.
        """
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        outdegree = [0] * n

        for i in range(len(graph)):
            outdegree[i] = len(graph[i])
            for v in graph[i]:
                reverse_graph[v].append(i)
        queue = []
        for i in range(len(outdegree)):
            if outdegree[i]==0:
                queue.append(i)

        safe = []

        while queue:
            node = queue.pop()

            safe.append(node)

            for prev_node in reverse_graph[node]:
                outdegree[prev_node]-=1
                if outdegree[prev_node]==0:
                    queue.append(prev_node)
        
        safe.sort()
        return safe

        return []