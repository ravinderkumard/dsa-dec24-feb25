1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        result = [0]*(n+1)
4        for i in range(1,n+1):
5            count = 0
6            x = i
7            while x:
8                x&=x-1
9                count+=1
10            print(i,count)
11            result[i] = count
12        return result