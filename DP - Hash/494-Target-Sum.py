class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def solve(idx,total):
            if idx==n:
                if total == target:
                    return 1
                return 0
            
            addWays = solve(idx+1,total+nums[idx])

            subWays = solve(idx+1,total-nums[idx])

            return addWays+subWays


        
        return solve(0,0)