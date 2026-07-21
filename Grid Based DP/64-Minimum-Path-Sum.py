class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [0]*(cols)
        dp[0] = grid[0][0]

        for i in range(1,cols):
            dp[i] = grid[0][i]+dp[i-1]
        
        for i in range(1,rows):
            dp[0]+=grid[i][0]
            for j in range(1,cols):
                    dp[j] = grid[i][j]+min(dp[j-1],dp[j])
        
        return dp[cols-1]