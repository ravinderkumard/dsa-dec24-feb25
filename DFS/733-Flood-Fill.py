from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        orig_color = image[sr][sc]
        if orig_color==color:
            return image

        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque([(sr,sc)])
        image[sr][sc] = color

        while queue:
            curr_x,curr_y= queue.popleft()
            
            for dx,dy in dirs:
                next_x = curr_x+dx
                next_y = curr_y+dy
                if next_x>=0 and next_x<rows and next_y>=0 and next_y<cols and image[next_x][next_y]==orig_color:
                    image[next_x][next_y] = color
                    queue.append((next_x,next_y))
        
        return image
        