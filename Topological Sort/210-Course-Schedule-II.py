class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course,pre in prerequisites:
            graph[pre].append(course)

        state = [0]*numCourses
        ans = []
        def dfs(course):
            if state[course]==1:
                return False
            if state[course]==2:
                return True
            
            state[course] = 1
            
            for pre in graph[course]:
                if dfs(pre)==False:
                    return False
            
            state[course] = 2
            ans.append(course)

            return True
        
        for course in range(numCourses):
            if dfs(course)==False:
                return []
            
        return ans[::-1]