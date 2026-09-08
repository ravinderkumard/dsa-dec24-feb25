class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        INF = float("inf")
        dp = [[0]*(cols+1) for _ in range(rows+1)]

        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i==0:
                    dp[i][j] = grid[i][j]+dp[i][j-1]
                elif j==0:
                    dp[i][j] = grid[i][j]+dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        
        return dp[rows-1][cols-1]

        # memo[rows][cols-1] = 0
        # memo[rows-1][cols] = 0

        # for i in range(rows-1,-1,-1):
        #     for j in range(cols-1,-1,-1):
        #         memo[i][j] = grid[i][j] + min(memo[i][j+1],memo[i+1][j])
        
        # return memo[0][0]



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