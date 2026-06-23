1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        left = 0
5        right = len(people)-1
6        count = 0
7        while(left<=right):
8            sum = people[left]+people[right]
9            if sum<=limit:
10                left+=1
11
12            right-=1
13            count+=1
14        
15        return count
16            