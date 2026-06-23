1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        farthest = 0
4        for idx in range(len(nums)):
5            if idx > farthest:
6                return False
7            farthest = max(farthest,idx+nums[idx])
8        
9        return True