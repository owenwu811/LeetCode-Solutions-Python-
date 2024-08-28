

#An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

#Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

#easy
#51.9% acceptance rate
#2133

#my own solution using python3:

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        allrows = []
        for r in range(rows):
            currow = []
            for c in range(cols):
                currow.append(matrix[r][c])
            for k in range(1, len(matrix) + 1):
                if k not in currow:
                    return False
            #print(currow)

        i = 0
        while i < len(matrix):
            curcol = []
            for m in matrix:
                curcol.append(m[i])
            i += 1
            for j in range(1, len(matrix) + 1):
                if j not in curcol:
                    return False
        return True
            #print(curcol)
            #i += 1

