class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0]*(cols) for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(1,cols):
            dp[0][i] = grid[0][i]+dp[0][i-1]
        print(dp)
        for i in range(1,rows):
            dp[i][0] = grid[i][0]+dp[i-1][0]

        for i in range(1,rows):
            for j in range(1,cols):
                    dp[i][j] = grid[i][j]+min(dp[i][j-1],dp[i-1][j])
        
        return dp[rows-1][cols-1]