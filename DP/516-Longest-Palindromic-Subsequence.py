class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[None]*n for _ in range(n)]
        def solve(idx1,idx2):
            if idx1>idx2:
                return 0
            if idx2==idx1:
                return 1
            if dp[idx1][idx2] is not None:
                return dp[idx1][idx2]
            answer = 0
            if s[idx1]==s[idx2]:
                answer = 2+solve(idx1+1,idx2-1)
            else:
                answer = max(solve(idx1+1,idx2),solve(idx1,idx2-1))
            dp[idx1][idx2] = answer
            return answer


        return solve(0,len(s)-1)