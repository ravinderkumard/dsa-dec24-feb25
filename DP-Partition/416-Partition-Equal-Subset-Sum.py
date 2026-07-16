class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total%2!=0:
            return False
        
        target = total//2
        dp = [[False] * (n+1) for _ in range(target+1)]
        
        for i in range(n+1):
            dp[0][i] = True
        
        for i in range(1,n+1):
            for s in range(1,target+1):
                if nums[i-1]<=s:
                    dp[s][i] = dp[s][i-1] or dp[s-nums[i-1]][i-1]
                else:
                    dp[s][i] = dp[s][i-1]

        return dp[target][n]