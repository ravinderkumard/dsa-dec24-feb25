class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def solve(idx1,idx2):
            if idx1==len(text1):
                return 0
            if idx2==len(text2):
                return 0
            ans = 0
            if text1[idx1]==text2[idx2]:
                ans = 1+solve(idx1+1,idx2+1)
            else:
                ans = max(solve(idx1+1,idx2),solve(idx1,idx2+1))
            return ans

        return solve(0,0)