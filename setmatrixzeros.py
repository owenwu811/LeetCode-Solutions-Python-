
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
                    for i in range(cols): #must be cols here instead of rows here and cols below! 
                        if matrix[r][i] != 0:
                            matrix[r][i] = "*"
                    for i in range(rows): #if we did cols here instead of rows, for test case matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]], we would be out of bounds when i = 3, c = 0 because we have 3 rows in total, so we can't go down to a 4th row aka index 3 row
                        if matrix[i][c] != 0:
                            matrix[i][c] = "*"
        for r in range((len(matrix))):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0


#6/14/24 review (missed):

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for i in range(cols):
                        if matrix[r][i] != 0: #i starts at 0, so [1][0] is the 2nd row's leftmost element
                            matrix[r][i] = "*"
                    for i in range(rows):
                        if matrix[i][c] != 0: #i starts at 0, so [0][1] is the 1st row's 2nd element
                            matrix[i][c] = "*"
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0
        

#practice again:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows): #0
            for c in range(cols): #0
                if matrix[r][c] == 0:
                    #if we find a cell, say matrix[1][1] to contain a 0, we have to set matrix[1][1]'s entire vertical and horizontal DIMENSIONS OF THE INPUT MATRIX AKA ROWS AND COLS to 0, which is why we loop through rows and cols - they are the dimensions of the input list of lists
                    for i in range(cols): #starts at 0
                        #if matrix[1][1] had a 0, we need to set [1][0], [1][1], [1][2] to "*", so the way we set the particular cell's adjacent rows is because [t][0] [t][1] [t][2] - t is always the same value (left square)
                        if matrix[r][i] != 0: #[0][2] = 2 to the right
                            matrix[r][i] = "*"
                    for i in range(rows): #starts at 0
                        #if matrix[1][1] had a 0, we need to set [0][1], [1][1], [2][1] to "*", so the way we set the particular cell's adjacent cols is because [0][c] [1][c] [2][c] - c always stays the same value (right square)
                        if matrix[i][c] != 0: 
                            matrix[i][c] = "*"
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0



#6/15/24 review:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for i in range(cols):
                        if matrix[r][i] != 0:
                            matrix[r][i] = "*"
                    for i in range(rows):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "*"
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0

#6/27/24 review:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0: #matrix[1][1] == 0
                    for i in range(cols): #i = 0
                        #without these conditional checks: the issue is because the original 0 is incorrectly marked as "*", the if matrix[r][c] == 0 never even executes, so we don't see the original 0 as a 0 anymore, so that row and column dosen't even get populated with "*" hence why we get [[0,0,0,0],[0,4,5,2],[0,3,1,5]] instead of [[0,0,0,0],[0,4,5,0],[0,3,1,0]] without the conditional checks for input [[0,1,2,0],[3,4,5,2],[1,3,1,5]] - the nested for loops to populate block never even executes because if matrix[r][c] == 0 is false when it should have been true because only original 0 cells can spread to rows and cols adjacent!!!!!
                        if matrix[r][i] != 0: 
                            matrix[r][i] = "*"
                    for j in range(rows):
                        if matrix[j][c] != 0:
                            matrix[j][c] = "*"
                    
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0

#7/3/24 review:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    for i in range(n):
                        if matrix[r][i] != 0:
                            matrix[r][i] = "*"

                    for i in range(m):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "*"
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0

#8/3/24 refresher (easier to understand solution since couldn't solve today):

row, col = set(), set()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            row.add(i)
            col.add(j)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i in row or j in col:
            matrix[i][j] = 0

#8/16/24 review (from grokking course) - needed hint about the variables overlapping each other:

def set_matrix_zeros(mat):
    
    m, n = len(mat), len(mat[0])
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] != 0:
                continue
            if mat[r][c] == 0:
                for i in range(len(mat)):
                    if mat[i][c] != 0:
                        mat[i][c] = "*"
                for i in range(len(mat[0])):
                    if mat[r][i] != 0:
                        mat[r][i] = "*"
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == "*":
                mat[row][col] = 0

    return mat - set matrix zeros


#solved again on leetcode platform on 8/16/24 minutes later:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] != 0:
                    continue
                if matrix[r][c] == 0:
                    for i in range(rows):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "*"

                    for j in range(cols):
                        if matrix[r][j] != 0:
                            matrix[r][j] = "*"
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0
        return matrix


#8/21/24 review:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        rows, cols = len(matrix), len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    for j in range(cols):
                        if matrix[r][j] != 0:
                            matrix[r][j] = "*"
                    for i in range(rows):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "*"
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0


#my own solution using python3 on 10/24/24:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        print(rows)
        print(cols)
        for i in range(len(matrix)):
            if i in rows:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        print(matrix)
        j = 0
        while j < len(matrix[0]):
            for i in range(len(matrix)):
                print(matrix[i][j])
                if j in cols:
                    matrix[i][j] = 0
            j += 1
        
