"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
            1. Convert this into adjList
            2. Run DFS starting from the employee Id
            3. Keep adding importance.
        """
        emp_list = {}
        for employee in employees:
            emp_list[employee.id] = employee
        
        total = 0
        stack = [id]
        while stack:
            curr_id = stack.pop()
            employee = emp_list[curr_id]

            total+=employee.importance

            for sub_id in employee.subordinates:
                stack.append(sub_id)
        
        return total

