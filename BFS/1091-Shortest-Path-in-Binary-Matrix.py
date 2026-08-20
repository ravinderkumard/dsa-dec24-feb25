from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]!=0:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        queue.append((0,0,1))
        grid[0][0] = 1
        dirs = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        while queue:
            curr = queue.popleft()
            if curr[0]==rows-1 and curr[1]==cols-1:
                return curr[2]
            for dx,dy in dirs:
                nx = curr[0]+dx
                ny = curr[1]+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0:
                    queue.append((nx,ny,curr[2]+1))
                    grid[nx][ny] = 1
        
        return -1