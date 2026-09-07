class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        INF = float("inf")
        memo = [[INF]*(cols+1) for _ in range(rows+1)]
        
        memo[rows][cols-1] = 1
        
        memo[rows-1][cols] = 1

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                next_health = min(memo[i+1][j],memo[i][j+1])

                memo[i][j] = max(1,next_health-dungeon[i][j])
        
        return memo[0][0]