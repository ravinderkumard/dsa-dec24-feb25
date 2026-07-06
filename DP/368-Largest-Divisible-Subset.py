class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        parent = [-1]*n
        dp = [1]*n
        maxLen = 1
        lastIndex = 0

        for i in range(0,n):
            for j in range(0,i):
                if nums[i]%nums[j]==0:
                    if dp[j]+1>dp[i]:
                        dp[i] = dp[j]+1
                        parent[i] = j
            
            if dp[i]>maxLen:
                maxLen = dp[i]
                lastIndex = i
        
        answer = []
        while lastIndex != -1:
            answer.append(nums[lastIndex])
            lastIndex = parent[lastIndex]
        
        answer.sort(reverse=True)

        return answer

