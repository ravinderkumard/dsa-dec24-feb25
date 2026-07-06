class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        memo = [[None]*(n+1) for _ in range(n+1)]
        def solve(curr,prev):
            if curr == n:
                return 0
            
            if memo[curr][prev+1] is not None:
                return memo[curr][prev+1]

            not_take = solve(curr+1,prev)
            take = -1
            if prev == -1 or nums[curr]%nums[prev]==0:
                take = 1+solve(curr+1,curr)
            memo[curr][prev+1] = max(take,not_take)
            return memo[curr][prev+1]
        
        solve(0,-1)
        ans = []
        curr = 0
        prev = -1

        while curr < n:
            take = -1
            if prev == -1 or nums[curr]%nums[prev] == 0:
                take = 1+solve(curr+1,curr)
            
            skip = solve(curr+1,prev)

            if take >=skip:
                ans.append(nums[curr])
                prev = curr
            curr+=1
        
        return ans