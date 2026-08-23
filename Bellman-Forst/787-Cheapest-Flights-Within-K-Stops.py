from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for frm,to,price in flights:
            graph[frm].append((to,price))

        INF = float("inf")
        cost = [INF]*n
        cost[src] = 0

        queue = [src]

        for _ in range(k+1):
            next_cost = cost.copy()
            next_queue = []

            for city in queue:
                for neighbor,price in graph[city]:
                    new_cost = cost[city]+price

                    if new_cost<next_cost[neighbor]:
                        next_cost[neighbor] = new_cost
                        next_queue.append(neighbor)
            cost= next_cost
            queue = next_queue
        
        return -1 if cost[dst]==INF else cost[dst]
        