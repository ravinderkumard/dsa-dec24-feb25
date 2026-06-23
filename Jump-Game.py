1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        farthest = 0
4        for i in range(len(nums)):
5            if i > farthest:
6                return False
7            farthest = max(farthest,i+nums[i])
8        
9        return True