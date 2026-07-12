class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def editDistance(i,j):
            if i == len(word1):
                return len(word2)-j
            
            if j==len(word2):
                return len(word1)-i

            if word1[i]==word2[j]:
                ans = editDistance(i+1,j+1)
            else:
                insert = editDistance(i,j+1)
                delete = editDistance(i+1,j)
                update = editDistance(i+1,j+1)
                ans = 1+min(insert,update,delete)
            
            return ans

        return editDistance(0,0)