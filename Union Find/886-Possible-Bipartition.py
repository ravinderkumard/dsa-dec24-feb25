from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        parent = list(range(2*n+1))

        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_x] = root_y

        for a,b in dislikes:

            if find(a)==find(b):
                return False

            union(a,b+n)

            union(b,a+n)

        return True        