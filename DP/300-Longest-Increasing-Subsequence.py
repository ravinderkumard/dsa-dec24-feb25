class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[None]*(n+1) for _ in range(n)]
        def solve(curr,prev):
            if curr == n:
                return 0
            
            if memo[curr][prev+1]is not None:
                return memo[curr][prev+1]

            take = 0
            if prev==-1 or nums[curr]>nums[prev]:
                take = 1+solve(curr+1,curr)
            not_take = solve(curr+1,prev)
            memo[curr][prev+1] = max(take,not_take)
            return max(take,not_take)

        return solve(0,-1)