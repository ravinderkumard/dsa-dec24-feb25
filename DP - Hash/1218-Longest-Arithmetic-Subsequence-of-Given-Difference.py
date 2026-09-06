class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        answer = 1

        for x in arr:
            previous = x-difference

            dp[x] = dp.get(previous,0)+1

            answer = max(answer,dp[x])
        
        return answer