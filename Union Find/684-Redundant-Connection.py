class UnionFind:
    def __init__(self,n):
        self.parent = {i: i for i in range(1, n)}
        self.rank = [0]*n
    
    def find(self,x):
        result = x
        while self.parent[result]!=result:
            self.parent[result] = self.parent[self.parent[result]]
            result = self.parent[result]
        return result
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)

        if px==py:
            return False
        
        if self.rank[px]>self.rank[py]:
            self.parent[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py]+=self.rank[px]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n+1)

        for x,y in edges:
            if uf.find(x)==uf.find(y):
                return [x,y]
            else:
                uf.union(x,y)
        
        return []