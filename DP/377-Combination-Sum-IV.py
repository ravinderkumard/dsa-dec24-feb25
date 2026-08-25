class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(total):
            if total==0:
                return 1
            if total<0:
                return 0
            
            if total in memo:
                return memo[total]

            ways = 0
            for num in nums:
                ways+=backtrack(total-num)
            memo[total] = ways
            return ways
        
        return backtrack(target)