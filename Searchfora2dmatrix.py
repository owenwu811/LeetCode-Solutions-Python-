

#You are given an m x n integer matrix matrix with the following two properties:
#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.

#You must write a solution in O(log(m * n)) time complexity.


#mysolution:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if target == matrix[i][j]:
                    return True
        return False
