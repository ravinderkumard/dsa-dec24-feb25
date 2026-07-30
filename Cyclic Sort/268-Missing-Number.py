class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_len = len(nums)
        sum_actual = (num_len*(num_len+1))//2
        sum_given = sum(nums)
        return sum_actual-sum_given