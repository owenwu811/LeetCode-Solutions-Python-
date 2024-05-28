
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
        return len(res) == len(set(res))



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


