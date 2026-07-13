class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[None]*(m+1) for _ in range(n+1)]
        def distance(i,j):
            if j==m:
                return 1
            if i==n:
                return 0
            if dp[i][j] is not None:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j] = distance(i+1,j+1)+distance(i+1,j)
            else:
                dp[i][j] = distance(i+1,j)
            return dp[i][j]
            
        return distance(0,0)