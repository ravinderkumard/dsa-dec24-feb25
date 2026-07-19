class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[0]*n for _ in range(m)]
        
        for i in range(n):
            result[m-1][i] = 1
        
        for i in range(m):
            result[i][n-1] = 1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                result[i][j] = result[i][j+1]+result[i+1][j]
        
        print(result)
        return result[0][0]
