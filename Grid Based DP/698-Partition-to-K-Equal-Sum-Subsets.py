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

        buckets = [0]*k

        def backtrack(idx):
            if idx==n:
                return True
            
            for i in range(k):
                if buckets[i]+nums[idx]<=target:
                    buckets[i]+=nums[idx]
                    if backtrack(idx+1):
                        return True
                    
                    buckets[i] -= nums[idx]
                
                if buckets[i]==0:
                    break
            
            return False

        return backtrack(0)
