1import heapq
2class Solution:
3    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
4        score = []
5        count,prev = 0,0
6        for station in stations:
7            loc = station[0]
8            capacity = station[1]
9            startFuel-=loc-prev
10            while score and startFuel<0:
11                startFuel+=-heapq.heappop(score)
12                count+=1
13            
14            if startFuel<0:
15                return -1
16            
17            heapq.heappush(score,-capacity)
18            prev = loc
19        
20        startFuel-=target-prev
21        while score and startFuel<0:
22            startFuel+=-heapq.heappop(score)
23            count+=1
24        if startFuel < 0:
25            return -1
26        return count