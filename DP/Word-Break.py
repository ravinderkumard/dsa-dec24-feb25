1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        def backtrack(s:str,wordDict:List[str],idx:int,cache:List[bool]) -> bool:
4            if idx < 0:
5                return True
6            if cache[idx] is not None:
7                return cache[idx]
8
9            for word in wordDict:
10                if idx-len(word)+1<0:
11                    continue
12                
13                if s[idx-len(word)+1:idx+1] == word and backtrack(s,wordDict,idx-len(word),cache):
14                    cache[idx] = True
15                    return True
16            cache[idx] = False
17            return False
18        return backtrack(s,wordDict,len(s)-1,[None]*(len(s)+1))