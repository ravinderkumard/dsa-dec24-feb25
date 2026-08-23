class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        cost = [INF]*n
        cost[src] = 0

        for _ in range(k+1):
            next_cost = cost.copy()

            for frm,to,price in flights:
                if cost[frm]==INF:
                    continue
                
                next_cost[to] = min(next_cost[to],cost[frm]+price)

            cost = next_cost
        
        return -1 if cost[dst] == INF else cost[dst]
    