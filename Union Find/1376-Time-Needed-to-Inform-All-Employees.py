class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = [[] for _ in range(n)]
        queue = []
        for i in range(len(manager)):
            if manager[i]!=-1:
                adj_list[manager[i]].append(i)
            
        queue.append((headID,0))
        total_time = 0
        while queue:
            curr_node = queue.pop(0)
            curr_emp = curr_node[0]
            curr_time = curr_node[1]
            total_time=max(curr_time,total_time)
            if len(adj_list[curr_emp])==0:
                continue
            for next_emp in adj_list[curr_emp]:
                next_time = curr_time+informTime[curr_emp]
                queue.append((next_emp,next_time))
        
        return total_time