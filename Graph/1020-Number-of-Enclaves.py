class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def set_value(i,j):
            if i<0 or i>=rows or j<0 or j>=cols:
                return
            
            if grid[i][j] ==0:
                return

            
            grid[i][j] = 0
            
            set_value(i+1,j)
            set_value(i-1,j)
            set_value(i,j+1)
            set_value(i,j-1)


        for i in range(rows):
            set_value(i,0)
            set_value(i,cols-1)
            
        for i in range(cols):
            set_value(0,i)
            set_value(rows-1,i)
        
        return sum(sum(row) for row in grid)