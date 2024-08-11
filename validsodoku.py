
#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:

#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.


#python3 solution:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #return boolean if it's valid or not
        res = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".": #cell dosen't contain a digit
                    #(r, board[r][c]) checks row constraint - element must be unique in row r
                    #(board[r][c], c) checks column constraint - element must be unique in column c
                    #(r // 3, c // 3) part determines index of 3x3 sub grid that a cell belongs to in a sodoku board. this is to ensure each digit appears no more than once within each of the 9 total 3x3 sub grids

                    res += [(r, board[r][c]), (board[r][c], c), (r // 3, c // 3, board[r][c])]
        return len(res) == len(set(res)) # the entire tuple has to be duplicated? so (0, 1) vs (0, 2) dosen't count as a duplicate even though it's within the same 3x3 grid!

IMPORTANT:

#so the list [(rowduplicatecheck), (columnduplicatecheck), (3x3duplicatecheck)] basically says if even a single tuple is duplicate, then the entire problem is wrong, so if 3 dosen't appear in the same row but appears in the opposite corner of the 3x3 column, then the (3x3duplicatecheck) will be of one less length in the resulting set, causing the result to be false

#In a standard 9x9 Sudoku board, there are nine 3x3 sub-grids, and they can be indexed as follows:

#Top-left 3x3 sub-grid: (0, 0) 
#Top-middle 3x3 sub-grid: (0, 1) (r moves by how much down, c moves by how much right)
#Top-right 3x3 sub-grid: (0, 2) 
#Middle-left 3x3 sub-grid: (1, 0)
#Center 3x3 sub-grid: (1, 1)
#Middle-right 3x3 sub-grid: (1, 2)
#Bottom-left 3x3 sub-grid: (2, 0)
#Bottom-middle 3x3 sub-grid: (2, 1)
#Bottom-right 3x3 sub-grid: (2, 2)

#5/29/24 review:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    res += [(r, board[r][c]), (board[r][c], c), (r // 3, c // 3, board[r][c])]
        return len(res) == len(set(res))

#5/30/24 review:

class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    res += [(r, board[r][c]), (board[r][c], c), (r // 3, c // 3, board[r][c])]
        return len(res) == len(set(res))
                    
#5/31/24 review:

class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    res += [(r, board[r][c]), (board[r][c], c), (r // 3, c // 3, board[r][c])]
        return len(res) == len(set(res))

#6/8/24 review:

class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    res += [(r, board[r][c]), (board[r][c], c), (r // 3, c // 3, board[r][c])]
        return len(res) == len(set(res))


#6/10/24 refresher (my own solution in python3):

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    res += [(r, board[r][c]), (board[r][c], c), (r // 3, c // 3, board[r][c])]
        return len(res) == len(set(res))

#6/14/24 review:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    res += [(r, board[r][c]), (board[r][c], c), (r // 3, c // 3, board[r][c])]
        return len(res) == len(set(res))

#7/2/24 review:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    res += [(r, board[r][c]), (board[r][c], c), (r // 3, c // 3, board[r][c])]
        return len(res) == len(set(res))

#7/31/24 refresher:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".": #it's important to include this check because we only want to add to result for cells with a digit that are non empty! or else you will only get 344/507 test cases
                    res += [(r, board[r][c]), (board[r][c], c), (board[r][c], r // 3, c // 3)]
        return len(res) == len(set(res))

#8/11/24 review (missed):

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        res = []
        for r in range(9): #we can do rows here too instead of 9
            for c in range(9): #we can do cols here too instead of 9
                if board[r][c] != ".":
                    res += [(r, board[r][c]), (board[r][c], c), (r // 3, c // 3, board[r][c])] #we place the r, board[r][c], not r // 3, board[r][c] because we want to check the row and column constraints first without the 3 x 3 check which is once for both rows and columns
        return len(res) == len(set(res))

