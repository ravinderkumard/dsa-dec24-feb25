class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)
        dp = [[0]*(word2_len+1) for _ in range(word1_len+1)]

        for j in range(0,word2_len):
            dp[word1_len][j] = word2_len-j

        for i in range(0,word1_len):
            dp[i][word2_len] = word1_len-i

        for i in range(word1_len-1,-1,-1):
            for j in range(word2_len-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    
                    insert = dp[i][j+1]
                    delete = dp[i+1][j]
                    update = dp[i+1][j+1]
                    dp[i][j] = 1+min(insert,update,delete)
        
        return dp[0][0]
