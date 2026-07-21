class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = {}
        def dfs(r1,c1,r2):
            c2 = r1+c1-r2
            if r1>=rows or c1>=cols or r2>=rows or c2>=cols:
                return -inf
            if grid[r1][c1]==-1 or grid[r2][c2]==-1:
                return -inf
            
            if (r1,c1,r2) in dp:
                return dp[(r1,c1,r2)]

            if r1==rows-1 and c1==cols-1:
                return grid[r1][c1]

            cherries = grid[r1][c1]
            if (r1,c1)!=(r2,c2):
                cherries+=grid[r2][c2]
            
            best = max(dfs(r1+1,c1,r2+1),
                        dfs(r1+1,c1,r2),
                        dfs(r1,c1+1,r2+1),
                        dfs(r1,c1+1,r2))
            dp[(r1,c1,r2)] = best+cherries
            return best+cherries

    
        return max(0,dfs(0,0,0))