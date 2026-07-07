class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        memo = [None] * n

        def dp(i):
            if memo[i] is not None:
                return memo[i]
            
            bestLen = 1
            count = 1

            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    childLen, childCount = dp(j)

                    if childLen+1>bestLen:
                        bestLen = childLen+1
                        count = childCount
                    elif childLen+1==bestLen:
                        count +=childCount
            
            memo[i] = (bestLen,count)
            return memo[i]
        
        maxLen = 0
        totalCount = 0

        for i in range(n):
            length,count = dp(i)
            if length > maxLen:
                maxLen = length
                totalCount = count
            elif length == maxLen:
                totalCount+=count
        
        return totalCount