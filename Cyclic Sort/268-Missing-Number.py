class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_len = len(nums)
        for i in range(0,num_len):
            num_len = num_len^i^nums[i]
        
        return num_len