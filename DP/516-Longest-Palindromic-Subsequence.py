class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)

        dp = [[0]*(n+1) for _ in range(n+1)]

        for idx1 in range(n-1,-1,-1):
            for idx2 in range(n-1,-1,-1):
                if s[idx1]==rev[idx2]:
                    dp[idx1][idx2] = 1+dp[idx1+1][idx2+1]
                else:
                    dp[idx1][idx2] = max(dp[idx1+1][idx2],dp[idx1][idx2+1])
        
        return dp[0][0]