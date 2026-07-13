class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp = [[None]*(n+1) for _ in range(m+1)]
        def solve(i,j):
            if i==m:
                return 0
            if j==n:
                return 0
            
            if dp[i][j] is not None:
                return dp[i][j]
            
            if word1[i]==word2[j]:
                dp[i][j] = 1+solve(i+1,j+1)
            else:
                dp[i][j] = max(solve(i+1,j),solve(i,j+1))
            return dp[i][j]
        
        lcs = solve(0,0)
        return (m-lcs)+(n-lcs)