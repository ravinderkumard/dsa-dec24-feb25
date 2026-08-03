from typing import List

class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)

        if px==py:
            return False
        
        if self.rank[px]<self.rank[py]:
            self.parent[px] = py
        elif self.rank[px]>self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px]+=1
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dsu = DSU(rows*cols)
        island = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    island+=1

        directions = [(0,1),(1,0)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue
                
                curr = r*cols+c

                for dr,dc in directions:
                    nr,nc = r+dr,c+dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                        neighbor = nr*cols+nc
                        if dsu.union(curr,neighbor):
                            island-=1
        
        return island