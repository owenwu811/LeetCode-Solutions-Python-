
#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

#You must do it in place.

#Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]


#python3 solution:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    for i in range(cols):
                        if matrix[r][i] != 0:
                            matrix[r][i] = "*"
                    for i in range(rows):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "*"
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0

#5/27/24 review:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    for i in range(cols):
                        if matrix[r][i] != 0:
                            matrix[r][i] = "*"
                    for i in range(rows):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "*"
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0
