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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        emailGroup = {}
        for i in range(n):
            accountList = accounts[i]
            for j in range(1,len(accountList)):
                email = accountList[j]
                if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    uf.union(i,emailGroup[email])

        components = {}
        for email in emailGroup:
            group = emailGroup[email]
            groupRep = uf.find(group)
            if groupRep not in components:
                components[groupRep] = []
            components[groupRep].append(email)
        
        mergedAccounts = []
        for group in components:
            component = components[group]
            component.sort()
            component.insert(0,accounts[group][0])
            mergedAccounts.append(component)
        
        return mergedAccounts
