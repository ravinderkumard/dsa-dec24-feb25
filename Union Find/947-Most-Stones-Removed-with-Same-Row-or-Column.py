
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

        if px==py:
            return
        
        if self.rank[px]<self.rank[py]:
            self.parent[px] = py
        elif self.rank[px]>self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px]+=1
        

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = len(stones)
        cols = len(stones[0])
        dsu = UnionFind(rows)

        for i in range(rows):
            for j in range(i+1,rows):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    dsu.union(i,j)
        
        components = set()
        for i in range(rows):
            components.add(dsu.find(i))
        
        return rows-len(components)
                