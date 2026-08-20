from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_oranges = 0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
        
        time = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue and fresh_oranges!=0:
            time+=1
            size = len(queue)
            for s in range(size):
                cx,cy = queue.popleft()
                
                for dx,dy in dirs:
                    nx = cx+dx
                    ny = cy+dy
                    if 0<=nx<rows and 0<=ny<cols:
                        if grid[nx][ny]==1:
                            fresh_oranges-=1
                            queue.append((nx,ny))
                            grid[nx][ny] =2
        if fresh_oranges!=0:
            return -1
        return time