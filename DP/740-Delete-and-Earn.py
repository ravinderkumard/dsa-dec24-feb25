from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_map = Counter(nums)
        max_number = max(nums)
        def count(num):
            if num <=0:
                return 0
            if num == 1:
                return num_map.get(num,0)
            
            gain = num*num_map.get(num,0)
            not_take = count(num-1)
            take = gain + count(num-2)
            return max(take,not_take)


        return count(max_number)
