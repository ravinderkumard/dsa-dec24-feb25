class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[None]*(len(word2)+1) for _ in range(len(word1)+1)]
        def editDistance(i,j):
            if i == len(word1):
                return len(word2)-j
            
            if j==len(word2):
                return len(word1)-i

            if dp[i][j] is not None:
                return dp[i][j]

            if word1[i]==word2[j]:
                ans = editDistance(i+1,j+1)
            else:
                insert = editDistance(i,j+1)
                delete = editDistance(i+1,j)
                update = editDistance(i+1,j+1)
                ans = 1+min(insert,update,delete)
            dp[i][j] = ans
            return ans

        return editDistance(0,0)