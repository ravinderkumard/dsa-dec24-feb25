1class Solution:
2    def tribonacci(self, n: int) -> int:
3        t_0 = 0
4        t_1 = 1
5        t_2 = 1
6        if n<1: return 0
7        if n<2 or n<3: return 1
8        n = n-2
9        while n>0:
10            t_4 = t_0+t_1+t_2
11            print(t_4)
12            t_0 = t_1
13            t_1 = t_2
14            t_2 = t_4
15            n-=1
16        
17        return t_2