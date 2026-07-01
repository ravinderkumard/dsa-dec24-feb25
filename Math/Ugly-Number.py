1class Solution:
2    def isUgly(self, n: int) -> bool:
3        if n<=0: 
4            return False
5        
6        for i in (2,3,5):
7            while n%i==0:
8                n//=i
9        return n==1