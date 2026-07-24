import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        source = k
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        heap = [(0,k)]
        distance = {}
        while heap:
            time,node = heapq.heappop(heap)
            if node in distance:
                continue
            
            distance[node] = time
            for nei, weight in graph[node]:
                if nei not in distance:
                    heapq.heappush(heap, (time + weight, nei))
        if len(distance)!=n:
            return -1
        
        return max(distance.values())
            