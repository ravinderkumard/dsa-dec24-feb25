class UnionFind:
    def __init__(self,n):
        self.parent = {i: i for i in range(n)}
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        uf = UnionFind(n)
        count = 0
        for u,v in connections:
            uf.union(u,v)

        for i in range(n):
            if uf.parent[i]==i:
                count+=1
        return count-1
        
