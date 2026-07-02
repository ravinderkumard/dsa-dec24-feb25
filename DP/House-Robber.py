1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        memo = {}
4        def backtrack(idx):
5            if idx>=len(nums):
6                return 0
7            
8            if idx in memo:
9                return memo[idx]
10
11            take = nums[idx]+backtrack(idx+2)
12            notTake = backtrack(idx+1)
13            memo[idx] = max(take,notTake)
14            return memo[idx]
15
16        return backtrack(0)