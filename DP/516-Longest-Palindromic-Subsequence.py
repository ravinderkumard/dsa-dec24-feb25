class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)

        dp = [[-1]*n for _ in range(n)]

        def lcs(idx1,idx2):
            if idx1==n or idx2==n:
                return 0
            
            if dp[idx1][idx2]!=-1:
                return dp[idx1][idx2]
            
            if s[idx1] == rev[idx2]:
                dp[idx1][idx2] = 1+lcs(idx1+1,idx2+1)
            else:
                dp[idx1][idx2] = max(lcs(idx1+1,idx2),lcs(idx1,idx2+1))
            
            return dp[idx1][idx2]
        
        return lcs(0,0)