from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dist = [[-1] * cols for _ in range(rows)]

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] ==0:
                    dist[r][c] = 0
                    queue.append((r,c))
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        while queue:
            curr_r,curr_c = queue.popleft()

            for x,y in dirs:
                neigh_r = curr_r + x
                neigh_c = curr_c + y
                if 0<=neigh_r<rows and 0<=neigh_c<cols:
                    if dist[neigh_r][neigh_c]==-1:
                        dist[neigh_r][neigh_c] = dist[curr_r][curr_c]+1
                        queue.append((neigh_r,neigh_c))
        
        return dist
