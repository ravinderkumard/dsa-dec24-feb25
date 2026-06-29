1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
3        map = {}
4
5        def dfs(s,wordDict):
6            res = []
7            n = len(s)
8            for word in wordDict:
9                if not s.startswith(word):
10                    continue
11                end = len(word)
12                if end == n:
13                    res.append(word)
14                else:
15                    subList = dfs(s[end:],wordDict)
16                    for item in subList:
17                        item = word+" "+item
18                        res.append(item)
19            return res
20        return dfs(s,wordDict)