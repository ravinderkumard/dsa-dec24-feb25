class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        INF = float("inf")
        memo = [[INF]*cols for _ in range(rows)]

        def minPath(i,j):
            if i==rows or j==cols:
                return float("inf")
            
            if i==rows-1 and j==cols-1:
                return grid[i][j]

            if memo[i][j] != INF:
                return memo[i][j]

            memo[i][j] = grid[i][j] + min(minPath(i+1,j),minPath(i,j+1))
            return memo[i][j]
        
        return minPath(0,0)