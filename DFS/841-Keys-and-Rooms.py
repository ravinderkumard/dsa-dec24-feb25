class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            key = stack.pop()
            visited.add(key)
            for next in rooms[key]:
                if next not in visited:
                    stack.append(next)
        
        return len(rooms)==len(visited)