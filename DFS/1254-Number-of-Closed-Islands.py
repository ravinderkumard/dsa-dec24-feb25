class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def mark_water(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==1:
                return
            
            grid[i][j]=1
            mark_water(i,j+1)
            mark_water(i,j-1)
            mark_water(i+1,j)
            mark_water(i-1,j)

        for i in range(rows):
            if grid[i][0]==0:
                mark_water(i,0)
            if grid[i][cols-1]==0:
                mark_water(i,cols-1)
        
        for j in range(cols):
            if grid[0][j]==0:
                mark_water(0,j)
            if grid[rows-1][j]==0:
                mark_water(rows-1,j)
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    count+=1
                    mark_water(i,j)
        
        return count

        
