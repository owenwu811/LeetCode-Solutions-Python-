#2798
#easy
#87.8% acceptance rate

#There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

#The company requires each employee to work for at least target hours.

#You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.

#Return the integer denoting the number of employees who worked at least target hours.



#my own solution using python3:

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for h in hours:
            if h >= target:
                res += 1
        return res
