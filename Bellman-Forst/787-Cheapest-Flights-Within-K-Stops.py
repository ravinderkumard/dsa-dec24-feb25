from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for frm,to,price in flights:
            graph[frm].append((to,price))

        INF = float("inf")
        cost = [INF]*n
        cost[src] = 0

        queue = deque([src])

        stops = 0

        while queue and stops <= k:
            size = len(queue)

            next_cost = cost.copy()

            for _ in range(size):
                city = queue.popleft()
                for neighbor,price in graph[city]:
                    new_cost = cost[city]+price
                    if new_cost < next_cost[neighbor]:
                        next_cost[neighbor] = new_cost
                        queue.append(neighbor)
            
            cost = next_cost
            stops+=1
        
        return -1 if cost[dst]==INF else cost[dst]
