
#Given an m x n grid of characters board and a string word, return true if word exists in the grid.

#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#Output: true



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def f(index, row, column):
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                return False
            #we found all letters in the word because index + 1 is in every recursive call
            if index >= len(word) - 1:
                return True
            temp = board[row][column]
            #each cell is marked as visited only in that particular path 
            board[row][column] = "visited"
            #result will be either True or False - if we find a point in which all 4 directions don't find the next letter we want, we backtrack to the previous letter and search in all 4 directions
            result = (f(index + 1, row + 1, column) or f(index + 1, row - 1, column) or f(index + 1, row, column + 1) or f(index + 1, row, column - 1))
            board[row][column] = temp
            return result

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and f(0, row, column):
                    return True
        return False


#the idea is that we backtrack only to the point where we still had the correct letters in the word up to that point, and we reset the variable back to temp for a new exploration because the use once rule only applies to a specific exploration or path - this is the essence of the backtracking mechanism 
#Backtracking is a technique used in recursive algorithms where, upon reaching a dead-end or determining that a certain path is not valid, you backtrack to the previous state to explore alternative paths.
#By resetting the cell to its original value, you undo the changes made during the current exploration path. This ensures that the grid is restored to its state before the exploration began.
