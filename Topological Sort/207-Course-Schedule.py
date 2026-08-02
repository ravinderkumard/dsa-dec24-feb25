from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        for course,pre_course in prerequisites:
            graph[course].append(pre_course)

        print(graph)

        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            
            if state[course] == 2:
                return True
            
            state[course] = 1

            for pre_c in graph[course]:
                if dfs(pre_c) == False:
                    return False
            
            state[course] = 2

            return True
        
        for course in range(numCourses):
            if dfs(course)==False:
                return False
        
        return True

        return False


