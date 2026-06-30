1class Solution:
2    def numDecodings(self, s: str) -> int:
3        memo = {}
4        def backtrack(idx):
5            if idx==len(s):
6                return 1
7            if s[idx] == '0':
8                return 0
9            
10            if idx in memo:
11                return memo[idx]
12            
13            ans = backtrack(idx+1)
14            if idx+1<len(s) and int(s[idx:idx+2])>=10 and int(s[idx:idx+2])<=26:
15                ans+=backtrack(idx+2)
16            memo[idx] = ans
17            return ans
18
19
20        return backtrack(0)