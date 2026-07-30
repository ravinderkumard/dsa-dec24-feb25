class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            correct = nums[i]-1
            if 1<=nums[i] and nums[i]<=n and nums[i]!=nums[correct]:
                nums[correct],nums[i] = nums[i],nums[correct]
            else:
                i+=1

        for i in range(0,n):
            if nums[i]!=i+1:
                return i+1
        
        return n+1