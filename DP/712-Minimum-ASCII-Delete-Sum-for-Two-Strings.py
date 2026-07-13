class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = len(s1),len(s2)
        dp = [[None]*(n+1) for _ in range(m+1)]
        def solve(i,j):
            if i==m:
                return sum(ord(c) for c in s2[j:])

            if j==n:
                return sum(ord(c) for c in s1[i:])

            if dp[i][j] is not None:
                return dp[i][j]

            if s1[i]==s2[j]:
                dp[i][j] = solve(i+1,j+1)
            else:
                dp[i][j] = min(ord(s1[i]) + solve(i+1,j), ord(s2[j])+solve(i,j+1))
            return dp[i][j]
        return solve(0,0)