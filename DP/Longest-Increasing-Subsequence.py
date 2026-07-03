1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        n = len(nums)
4        memo = [[-1]*(n+1) for _ in range(n)]
5        def solve(curr,prev):
6            if curr == n:
7                return 0
8            
9            if memo[curr][prev+1]!=-1:
10                return memo[curr][prev+1]
11
12            take = 0
13            if prev==-1 or nums[curr]>nums[prev]:
14                take = 1+solve(curr+1,curr)
15            not_take = solve(curr+1,prev)
16            memo[curr][prev+1] = max(take,not_take)
17            return max(take,not_take)
18
19        return solve(0,-1)