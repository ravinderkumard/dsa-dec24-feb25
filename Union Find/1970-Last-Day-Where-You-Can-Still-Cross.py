class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        
        if self.rank[px]>self.rank[py]:
            px,py = py,px
        self.parent[py] = px

        if self.rank[px] == self.rank[py]:
            self.rank[px]+=1

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        total = row * col
        TOP = total
        BOTTOM = total+1
        dsu = UnionFind(total+2)
        land = [[False]*col for _ in range(row)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def get_id(r,c):
            return r*col+c
        
        for day in range(len(cells)-1,-1,-1):
            r,c = cells[day]
            r-=1
            c-=1
            land[r][c] = True
            curr = get_id(r,c)

            if r==0:
                dsu.union(curr,TOP)
            
            if r==row-1:
                dsu.union(curr,BOTTOM)
            
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc

                if 0<=nr<row and 0<=nc<col and land[nr][nc]:
                    dsu.union(curr,get_id(nr,nc))
            
            if dsu.find(TOP) == dsu.find(BOTTOM):
                return day
        return 0