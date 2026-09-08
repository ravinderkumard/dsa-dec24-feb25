class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        INF = float("inf")
        memo = [[INF]*(cols+1) for _ in range(rows+1)]

        memo[rows][cols-1] = 0
        memo[rows-1][cols] = 0

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                memo[i][j] = grid[i][j] + min(memo[i][j+1],memo[i+1][j])
        
        return memo[0][0]



        # def minPath(i,j):
        #     if i==rows or j==cols:
        #         return float("inf")
            
        #     if i==rows-1 and j==cols-1:
        #         return grid[i][j]

        #     if memo[i][j] != INF:
        #         return memo[i][j]

        #     memo[i][j] = grid[i][j] + min(minPath(i+1,j),minPath(i,j+1))
        #     return memo[i][j]
        
        # return minPath(0,0)