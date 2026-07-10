class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)

        nextRow = [0]*(n+1)

        for i in range(m-1,-1,-1):
            currRow = [0]*(n+1)
            for j in range(n-1,-1,-1):
                if text1[i]==text2[j]:
                    ans = 1+nextRow[j+1]
                else:
                    ans = max(nextRow[j],currRow[j+1])
                currRow[j] = ans
            nextRow = currRow
        
        return nextRow[0]