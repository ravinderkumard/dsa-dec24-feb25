class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        memo = [[None]*cols for _ in range(rows)]
        def getVal(i,j):

            if i==rows or j==cols:
                return float("inf")
            
            if i==rows-1 and j==cols-1:
                return max(1,1-dungeon[i][j])
            
            if memo[i][j] is not None:
                return memo[i][j]

            right_move = getVal(i,j+1)
            down_move = getVal(i+1,j)

            next_health = min(right_move,down_move)

            required_health = next_health-dungeon[i][j]

            memo[i][j] = max(1,required_health)
            return max(1,required_health)
        
        return getVal(0,0)
