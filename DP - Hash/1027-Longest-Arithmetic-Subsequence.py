class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [dict() for _ in range(n)]

        answer = 2

        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]

                dp[i][diff] = dp[j].get(diff,1)+1

                answer = max(answer,dp[i][diff])
        
        return answer