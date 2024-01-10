
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


#another run:


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findword(index, row, column):
            #we will start a dfs from the current cell in our board, and we need to boundary check it first and make sure it matches the letter we are looking for whose order is determined by index
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                #each recursive call will return a boolean indicating if the current letter in our word could be found - if we are out of bounds or the current cell is not the correct letter we are looking for next in the word, we return false and then undo the current recursive call to explore other paths
                return False
            #we found the word if index reaches that point because index backtracks and only continues if we have found another letter and made progress
            elif index >= len(word) - 1:
                return True
            #we haven't returned true or false because we haven't found the entire word yet, but we have found another letter to get closer to this goal, so mark this cell as visited so the same path dosen't revisit it
            originalvalue = board[row][column]
            board[row][column] = "visited"
            #if we found the next letter in the word we are looking for in any of the 4 directions from the current cell, then we can return True and go onto the next letter in our word
            result = (findword(index + 1, row + 1, column) or findword(index + 1, row - 1, column) or findword(index + 1, row, column + 1) or findword(index + 1, row, column - 1))
            #if we explored all 4 directions and couldn't find the next letter in the word, we need to undo the change, which counts as a new path, so reset the visited cell to it's original value
            # restoring the original value is basically undoing the current path and any changes during this path
            #when we backtrack aka hit a dead end, we return False and undo any incorrect changes and start a new path from the point that it was still correct (found a portion of the letters in our word), and the index variable is also rewinded to when it was still correct - this is why the index >= len(word) - 1 works to check if we have found the entire word
            board[row][column] = originalvalue
            return result
 
            


        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and findword(0, row, column): #if none of these recursive calls have returned a final result of false meaning that it was possible to find the rest of the word
                    return True
        #if, after iterating over every cell in our board as a starting path, we could never find the word without restepping over a cell, return False
        return False



        #When index >= len(word) - 1 becomes true, it means that the algorithm has successfully found the entire word in the current path. In this case, the findword function returns True, indicating that the word has been found, and the search can stop for the current path.
        #The result of this True return will propagate up through the recursive calls. Eventually, if the initial call to findword(0, row, column) was part of the main loop and not part of a deeper recursive call, it would return True to the calling code, and the exist method would return True as well. This indicates that the word has been found in the board, and the entire search can stop. so this index >= len(word) - 1 acts as a base case to stop infinite recursion after we already found the word

#and the boundary check case if never true when the findword function is originally called because we are garunteed to have found the first letter of the word in some cell of the board through the nested for loops
        
#another run:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def f(index, row, column):
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                return False
            #this True base case will actually return True back to the parent function call back to the block in the nested for loops because we found the word. We determine if we found the word because we keep incrementing index by 1 if we found the current letter. 
            elif index >= len(word) - 1:
                return True
            origcellvalue = board[row][column]
            board[row][column] = "visited"
            #note that return False base case will only be triggered by one of these recursive calls because the first instance of this base case being checked will never be False as we found the first letter of the word to even start our path. These recursive calls also move onto look for the next letter in the word and also in a different direction as indicated by the index + 1 part and also the row + 1 part, for example. 
            result = (f(index + 1, row + 1, column) or f(index + 1, row - 1, column) or f(index + 1, row, column + 1) or f(index + 1, row, column - 1))
            board[row][column] = origcellvalue
            return result
            
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and f(0, row, column):
                    return True
        return False


#1/9/24 refresher:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, row, column):
            #the next cell we stepped onto - is it out of bounds in any way or not the letter we are currently looking to mark off in our word? If so, return False for that specific recursive call and undo the changes
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                return False
            
            elif index >= len(word) - 1:
                return True
            original = board[row][column]
            board[row][column] = "visited"
            #as long as one of these recursive calls returns true in one of the directions, we can still keep going in our path to find the rest of the letters meaning another direction AND the next letter in the word
            result = (dfs(index + 1, row + 1, column) or dfs(index + 1, row - 1, column) or dfs(index + 1, row, column + 1) or dfs(index + 1, row, column - 1))
            #if we hit a dead end, we need to undo all the changes in the current path until we have still made some progress from the 1st letter in the word, which we found
            board[row][column] = original
            return result


        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and dfs(0, row, column):
                    return True
        return False
        
        
