class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0]*(len(text2)+1) for _ in range((len(text1)+1))]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    ans = 1+cache[i+1][j+1]
                else:
                    ans = max(cache[i+1][j],cache[i][j+1])
                cache[i][j] = ans
        
        return cache[0][0]