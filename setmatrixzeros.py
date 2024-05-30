
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


#matrix = [[1,1,1],
#          [1,0,1],
#          [1,1,1]]
#rows = 3, cols = 3
#r = 0, c = 0
#matrix[0][0] is equal to 1, not 0, so go back to for c in range(len(matrix[0]))
#r = 0, c = 1
#matrix[0][1] is equal to 1, not 0, so go back to for c in range(len(matrix[0]))
#r = 0, c = 2
#matrix[0][2] is equal to 1, not 0, so go back to for c in range(len(matrix[0]))
#c hits limit since can't go past 2, so go back to for r in range(len(matrix)): 
#r = 1, c = 0
#matrix[1][0] is equal to 1, not 0, so go back to  for c in range(len(matrix[0])):
#r = 1, c = 1
#matrix[1][1] is equal to 0 - TRUE - so continue to for i in range(cols):

#r = 1, i = 0 inside of for i in range(cols):
#matrix[1][0] != 0 is True - so set the cell to a "*":

#[[1,1,1],
#[1,0,1],
#[1,1,1]]

#becomes

#[[1,1,1],
#["*",0,1],
#[1,1,1]]

#r = 1, i = 1 inside of for i in range(cols):
#matrix[1][1] is equal to 0 - false, so go back to for i in range(cols):
#r = 1, i = 2
#matrix[1][2] != 0 is True, so set the cell to a "*":

#[[1,1,1],
#["*",0,1],
#[1,1,1]]

#becomes

#[[1,1,1],
#["*",0,"*"],
#[1,1,1]]

#for i in range(cols): finishes all iterations
#we are now inside for i in range(rows):
#c = 1, i = 0
#matrix[0][1] != 0 is True, so set the cell to a "*":

#[[1,1,1],
#["*",0,"*"],
#[1,1,1]]

#becomes


#[[1,"*",1],
#["*",0,"*"],
#[1,1,1]]

#back to for i in range(rows):
#c = 1, i = 1
#matrix[1][1] != 0 is False, so go back to for i in range(rows):
#c = 1, i = 2
#matrix[2][1] != 0 is True, so set the cell to a "*":

#[[1,"*",1],
#["*",0,"*"],
#[1,1,1]]

#becomes

#[[1,"*",1],
#["*",0,"*"],
#[1,"*",1]]

#for i in range(rows): finishes
#go back to for c in range(len(matrix[0]):
#r = 1, c = 2
#matrix[1][2] == 0 is False because it was "*" in the 2nd row rightmost cell, so go back to for c in range(len(matrix[0])
#c can't go past 2, so go back to for r in range(len(matrix)):
#r = 2, c = 0 (COLUMN MUST RESET EVERYTIME THE ABOVE LOOP VARIABLE INCREMENTS!)
#matrix[2][0] == 0 is False since it was a 1, so go back to for c in range(len(matrix[0])
#r = 2, c = 1
#matrix[2][1] == 0 is False becuase it was a "*", so go back to for c in range(len(matrix[0])
#r = 2, c = 2
#matrix[2][2] == 0 is False because it was a 1, so go back to so go back to for c in range(len(matrix[0]) and then for r in range(len(matrix)) 
#because r = 2 and c = 2, the 1st douple loop finishes

#our grid still looks like:

#[[1,"*",1],
#["*",0,"*"],
#[1,"*",1]]

#now, we go through the entire matrix and change any cell with "*" to a 0




#5/30/24 review:

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
        for r in range((len(matrix))):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0






