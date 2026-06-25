1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        result = [0]*(n+1)
4        for i in range(1,n+1):
5            count = 0
6            x = i
7            while x:
8                if result[x]!=0:
9                    count+=result[x]
10                    break
11                x&=x-1
12                count+=1
13            result[i] = count
14        return result