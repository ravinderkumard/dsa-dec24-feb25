class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        words = set(wordDict)
        memo = {}
        n = len(s)

        def dfs(start):
            
            if start==n:
                return [""]
            if start in memo:
                return memo[start]

            res = []

            for end in range(start+1,n+1):
                word = s[start:end]
                if word not in words:
                    continue
                
                for sentence in dfs(end):
                    if sentence:
                        res.append(word+" "+sentence)
                    else:
                        res.append(word)
            memo[start] = res
            return res
            
        return dfs(0)