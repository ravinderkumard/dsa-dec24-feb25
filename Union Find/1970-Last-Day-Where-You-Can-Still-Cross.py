class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def canCross(day):
            # 0 = land, 1 = water
            grid = [[0] * col for _ in range(row)]
            queue = []
            for i in range(day):
                grid[cells[i][0]-1][cells[i][1]-1]=1
            
            for i in range(col):
                if grid[0][i]==0:
                    queue.append((0,i))
                    grid[0][i] = -1
            
            while queue:
                curr = queue.pop(0)
                r,c = curr[0],curr[1]
                if r==row-1:
                    return True
                
                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==0:
                        grid[nr][nc]=-1
                        queue.append((nr,nc))
            
            return False

        left, right = 1, row*col
        ans = 0

        while left < right:
            mid = right - (right-left)//2

            if canCross(mid):
                left = mid
            else:
                right = mid - 1

        return left

    