class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        memo = {}
        def getVal(i,j):
            if i == rows or j==cols:
                return float("inf")
            
            if i==rows-1 and j==cols-1:
                return -dungeon[i][j]+1 if dungeon[i][j]<=0 else 1
            
            if (i,j) in memo:
                return memo[(i,j)]

            if_we_go_right = getVal(i,j+1)
            if_we_go_down = getVal(i+1,j)

            min_health_required = min(if_we_go_right,if_we_go_down) - dungeon[i][j]

            memo[(i,j)] = 1 if min_health_required <=0 else min_health_required
            return memo[(i,j)]

        return getVal(0,0)