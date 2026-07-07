class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        memo = [[None]*(n+1) for _ in range(n)]

        def seq(curr,prev):
            if curr == len(nums):
                return (0,1)
            
            if memo[curr][prev+1] is not None:
                return memo[curr][prev+1]

            takeLen = 0
            takeCount = 0
            if prev==-1 or nums[curr]>nums[prev]:
                nextLen, nextCount = seq(curr+1,curr)
                takeLen = 1+nextLen
                takeCount = nextCount

            skipLen,skipCount = seq(curr+1,prev)

            if takeLen > skipLen:
                ans = (takeLen,takeCount)
            elif skipLen>takeLen:
                ans = (skipLen,skipCount)
            else:
                ans = (takeLen,takeCount+skipCount)
            memo[curr][prev+1] = ans
            return ans

        return seq(0,-1)[1]