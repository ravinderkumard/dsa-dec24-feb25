You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10

https://chatgpt.com/share/6a596cfc-fbb0-83e8-b19d-b42c26a65cb4



class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for gap in range(2,n):
            for left in range(n-gap):
                right = left+gap
                for k in range(left+1,right):
                    dp[left][right] = max(dp[left][right],dp[left][k]+dp[k][right]+nums[left]*nums[k]*nums[right])
        
        return dp[0][n-1]




class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums) # New lenght after adding 1 elment on both side
        dp = [[None]*n for _ in range(n)]
        def solve(left,right):
            if right-left==1:
                return 0
            
            if dp[left][right] is not None:
                return dp[left][right]

            ans = 0
            for k in range(left+1,right):
                coins = solve(left,k)+solve(k,right)+nums[left]*nums[k]*nums[right]
                ans = max(ans,coins)
            dp[left][right] = ans
            return ans

        return solve(0,n-1)
