
class UnionFind:
    def __init__(self):
        self.parent = {}
        
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x
        
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)

        if px!=py:
            self.parent[px] = py

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        dsu = UnionFind()

        for r,c in stones:
            dsu.union(r,~c)

        components = set()

        for r,_ in stones:
            components.add(dsu.find(r))

        return len(stones) - len(components)        