
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
#we reset the cell to its original value when we have hit a dead end meaning we still haven't found the entire word yet



#practice run #2 - 1/6/24


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, row, column):
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                return False
            #index represents and only reachess up to a point in the input word where we have found all letters in our current path we are exploring because it would backtrack if we didn't at any point. we would backtrack until we reached the point where we still did find all letters up to a certain point in the word and continue exploring new paths
            if index >= len(word) - 1:
                return True
            temp = board[row][column]
            #we mark the cell as visited and then explore all 4 cells adjacent to this cell - this counts as the same path
            board[row][column] = "visited"
            result = (dfs(index + 1, row + 1, column) or dfs(index + 1, row - 1, column) or dfs(index + 1, row, column + 1) or dfs(index + 1, row, column - 1))
            #after we explore all 4 directions and hit a dead end, then we need to backtrack and explore a new path, but, first, we need to reset the cell marked as visited to their original value since the same cell cannot be used more than once in a particular path of exploration only
            board[row][column] = temp
            return result


        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and dfs(0, row, column):
                    return True
        return False


#1/7/24 practice run:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def f(index, row, column):
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                return False
            #when we return True here, we know we have found the word, so we can bubble back up the recursive tree to return every cell in our path as true - even though this may look like new calculations, it is not; it's just verifying all the letters in the path up to that point - and then return True back to the if statement in the nested for loop
            if index >= len(word) - 1:
                return True
            temp = board[row][column]
            board[row][column] = "visited"
            result = (f(index + 1, row + 1, column) or f(index + 1, row - 1, column) or f(index + 1, row, column + 1) or f(index + 1, row, column - 1))
            board[row][column] = temp
            return result

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and f(0, row, column):
                    return True
        return False

#again
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def f(index, row, column, board):
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                return False
            if index >= len(word) - 1:
                return True
            temp = board[row][column]
            board[row][column] = "visited"
            result = (f(index + 1, row + 1, column, board) or f(index + 1, row - 1, column, board) or f(index + 1, row, column + 1, board) or f(index + 1, row, column - 1, board))
            board[row][column] = temp
            return result

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and f(0, row, column, board):
                    return True
        return False
        
