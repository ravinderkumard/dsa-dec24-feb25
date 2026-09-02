class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sum_val = sum(nums)
        if abs(target) > sum_val:
            return 0
        memo = [[-1]*(2*sum_val+1) for _ in range(n+1)]

        def solve(idx,total):
            if idx==n:
                if total == target:
                    return 1
                return 0
            
            if memo[idx][total+sum_val] != -1:
                return memo[idx][total+sum_val]
            
            addWays = solve(idx+1,total+nums[idx])

            subWays = solve(idx+1,total-nums[idx])
            memo[idx][total+sum_val] = addWays+subWays
            return addWays+subWays

        return solve(0,0)