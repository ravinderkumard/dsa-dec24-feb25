class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [0]*n
        result[n-1] = 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    result[j] = 0
                elif j<n-1:
                    result[j]+=result[j+1]
        
        return result[0]
                