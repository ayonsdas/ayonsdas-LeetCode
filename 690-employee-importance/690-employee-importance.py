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
        
        key = {}
        for employee in employees:
            key[employee.id] = [employee.importance, employee.subordinates]
        
        def finder(id: int) -> int:
            nonlocal key
            s = [id]
            v = 0
            while s:
                t = s.pop(-1)
                v += key[t][0]
                for l in key[t][1]:
                    s.append(l)
            return v
            
        return finder(id)