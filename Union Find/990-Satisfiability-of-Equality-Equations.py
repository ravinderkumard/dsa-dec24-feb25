class UnionFind:
    def __init__(self,n):
        self.parent = {i: i for i in range(n)}
        self.rank = [1]*n
    
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
            return 0
        
        if self.rank[px]>self.rank[py]:
            self.parent[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py]+=self.rank[px]
        return 1
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        uf = UnionFind(26)

        for eq in equations:
            if eq[1]=='=':
                x = ord(eq[0])-ord('a')
                y = ord(eq[3])-ord('a')
                uf.union(x,y)

        for eq in equations:
            if eq[1]=='!':
                x = ord(eq[0])-ord('a')
                y = ord(eq[3])-ord('a')
                if uf.find(x)==uf.find(y):
                    return False
        
        return True