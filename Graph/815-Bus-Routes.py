from collections import defaultdict, deque
from typing import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0

        stops = defaultdict(list)
        len_routes = len(routes)

        for bus,route in enumerate(routes):
            for stop in route:
                stops[stop].append(bus)
        
        queue = deque([(source,0)])
        visited_stops = {source}
        visited_buses = set()

        while queue:
            stop,buses_taken = queue.popleft()
            if stop==target:
                return buses_taken

            for bus in stops[stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)

                for next_stop in routes[bus]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop,buses_taken+1))

        
        return -1

        return -1
