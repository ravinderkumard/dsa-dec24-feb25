from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_map = Counter(nums)
        max_number = max(nums)
        memo = {}
        def count(num):
            if num <=0:
                return 0
            if num == 1:
                return num_map.get(num,0)
            if num in memo:
                return memo[num]
            gain = num*num_map.get(num,0)
            not_take = count(num-1)
            take = gain + count(num-2)
            memo[num] = max(take,not_take)
            return memo[num]


        return count(max_number)
