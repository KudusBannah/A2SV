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
        def dfs(id):
            employee = employees_id[id]
            subordinates_sum = 0
            for subordinate_id in employee.subordinates:
                subordinates_sum += dfs(subordinate_id)
            return subordinates_sum + employee.importance
        
        employees_id = defaultdict(int)
        for employee in employees:
            employees_id[employee.id] = employee
        
        return dfs(id)