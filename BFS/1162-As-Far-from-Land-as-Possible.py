from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        has_water = False
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i,j))
                else:
                    has_water = True
        
        if not queue or has_water == False:
            return -1

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        max_distance = -1
        while queue:
            for _ in range(len(queue)):
                curr_x,curr_y = queue.popleft()

                for dx,dy in dirs:
                    next_x = curr_x+dx
                    next_y = curr_y+dy

                    if 0<=next_x<rows and 0<=next_y<cols:
                        if grid[next_x][next_y]==0:
                            grid[next_x][next_y] = 1    
                            queue.append((next_x,next_y))
            max_distance += 1

        return max_distance

