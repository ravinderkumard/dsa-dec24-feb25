1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
3        map = {}
4
5        def dfs(s,wordDict):
6            if s in map:
7                return map[s]
8            res = []
9            n = len(s)
10            for word in wordDict:
11                if not s.startswith(word):
12                    continue
13                end = len(word)
14                if end == n:
15                    res.append(word)
16                else:
17                    subList = dfs(s[end:],wordDict)
18                    for item in subList:
19                        item = word+" "+item
20                        res.append(item)
21            map[s] = res
22            return res
23        return dfs(s,wordDict)