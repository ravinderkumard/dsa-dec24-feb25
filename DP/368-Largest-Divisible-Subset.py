class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []
        cache = [[None]*(n+1) for _ in range(n+1)]
        def solve(curr,prev):
            if curr == n:
                return 0
            if cache[curr][prev+1] is not None:
                return cache[curr][prev+1]
            take = 0
            if prev==-1 or nums[curr]%nums[prev]==0:
                take = 1+solve(curr+1,curr)
            not_take = solve(curr+1,prev)
            cache[curr][prev+1] = max(take,not_take)
            return max(take,not_take)
        
        solve(0,-1)
        curr = 0
        prev = -1

        while curr < n:
            take = -1
            if prev == -1 or nums[curr]%nums[prev]==0:
                take = 1+solve(curr+1,curr)
            not_take = solve(curr+1,prev)

            if take>=not_take:
                ans.append(nums[curr])
                prev = curr
            curr+=1
        return ans