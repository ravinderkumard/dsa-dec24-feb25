class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        orig_color = grid[row][col]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        borders = []
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c):
            visited.add((r,c))
            is_border = False
            for dr,dc in dirs:
                nr = r+dr
                nc = c+dc
                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    is_border = True
                elif grid[nr][nc]!=orig_color:
                    is_border = True
                elif (nr,nc) not in visited:
                    dfs(nr,nc)
            
            if is_border:
                borders.append((r,c))
        
        dfs(row,col)

        for (r,c) in borders:
            grid[r][c] = color
        return grid
