class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_val = sum(nums)

        if abs(target)>sum_val:
            return 0
        
        if (target+sum_val) %2!=0:
            return 0
        
        sub_target = (target+sum_val) // 2

        dp = [0]*(sub_target+1)
        dp[0] = 1

        for num in nums:
            for s in range(sub_target,num-1,-1):
                dp[s] += dp[s-num]

        return dp[sub_target]