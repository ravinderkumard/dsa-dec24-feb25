class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # If sum is not divisible by k false
        total = sum(nums)
        n = len(nums)
        if total%k!=0:
            return False

        target = total//k

        nums.sort(reverse=True)
        if nums[0]>target:
            return False
        memo = {}
        def backtrack(mask,currSum):
            if mask == (1<<n)-1:
                return currSum==0

            if (mask,currSum) in memo:
                return memo[(mask,currSum)]
            prev = -1
            for i in range(n):
                if mask & (1<<i):
                    continue
                if nums[i]==prev:
                    continue
                if currSum+nums[i]>target:
                    continue
                if backtrack(mask|(1<<i),(currSum+nums[i])%target):
                    memo[(mask,currSum)] = True
                    return True
            memo[(mask,currSum)] = False
            return False

        return backtrack(0,0)
