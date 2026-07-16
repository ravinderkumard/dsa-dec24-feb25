class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total%2!=0:
            return False
        
        target = total//2
        memo = [[None] * (n+1) for _ in range(target+1)]
        def partition(idx,target):
            if target==0:
                return True
            if idx==n:
                return False
            if target<0:
                return False
            if memo[target][idx] is not None:
                return memo[target][idx]

            take = partition(idx+1,target-nums[idx])
            skip = partition(idx+1,target)
            memo[target][idx] = take or skip
            return take or skip

        return partition(0,target)