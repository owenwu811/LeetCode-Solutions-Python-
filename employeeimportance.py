
#690
#medium

#You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

#You are given an array of employees employees where:

#employees[i].id is the ID of the ith employee.
#employees[i].importance is the importance value of the ith employee.
#employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
#Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.

#Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
#Output: 11
#Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
#They both have an importance value of 3.
#Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.


#my own solution using python3:

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
        #importance of direct + indirect sub 
        d = defaultdict(list)
        newd = defaultdict(list)
        for e in employees:
            #print(e.id, e.importance)
            d[e.id].append(e.importance)
            for a in e.subordinates:
                newd[e.id].append(a)
            
        print(d)
        print(newd)
        print(id)
        queue = deque([id])
        res = 0
        while queue:
            cur = queue.popleft()
            print(cur)
            print(d[cur])
            for h in d[cur]:
                res += h
            for a in newd[cur]:
                print(a)
                queue.append(a)
        return res
            
