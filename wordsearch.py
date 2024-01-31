
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


#1/11/24 refresher:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, index, row, column):
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            temp = board[row][column] 
            board[row][column] = "visited"
            result = (dfs(board, index + 1, row + 1, column) or dfs(board, index + 1, row - 1, column) or dfs(board, index + 1, row, column + 1) or dfs(board, index + 1, row, column - 1))
            board[row][column] = temp
            return result
 


        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and dfs(board, 0, row, column):
                    return True
        return False
        


#1/12/24 refresher:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, row, column):
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                #we are using booleans for each recursive function call to determine - if we return False, then that path has already failed, so we need to undo the step (path) and try another of the 3 directions left. If we can't find the next letter we need in the remaining 3 directions, then our path isn't valid, so undo the change, and then, in another path, we can reuse the cell because we start a new path
                #reember that return False can't be caused by the 1st call of this dfs function because we already found the 1st letter of the word in our nested for loop - return False can only be caused by one of the 4 direction calls in result
                return False
            if index >= len(word) - 1:
                return True
            #we aren't out of bounds, haven't found the entire word yet, but we have found the current letter we are looking for in our current cell, so save it before marking this cell as visited, and keep looking for the NEXT letter (indicated by index + 1 in the recursive call in result )in a NEW direction (indicated by either row + 1 or - 1 or colum + 1 or -1 in the recursive call in result) - if any of the 4 directional recursive calls in result return True, then we found our letter and can keep going again until we find the entire word
            originalvalue = board[row][column]
            board[row][column] = "visited"
            result = (dfs(index + 1, row + 1, column) or dfs(index + 1, row - 1, column) or dfs(index + 1, row, column + 1) or dfs(index + 1, row, column - 1)
            ) 
            #if none of the directions find our next letter, the entire path is invalid, so restore the original value of any of the cells we marked as visited in our current path, undo the current change and keep undoing until we are still valid and have made some progress beyond the 1st letter
            board[row][column] = originalvalue
            return result



        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and dfs(0, row, column):
                    return True
        #if we started the full dfs from every cell in the grid and couldn't find a 100% valid path given the constraint of not reusing the same cell, return False
        return False


#1/14/24 refresher:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, row, column):
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[index]:
                return False
            elif index == len(word) - 1:
                return True
            original = board[row][column]
            board[row][column] = "visited"
            bol = (dfs(index + 1, row + 1, column) or dfs(index + 1, row - 1, column) or dfs(index + 1, row, column + 1) or dfs(index + 1, row, column - 1))
            board[row][column] = original
            return bol
        

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and dfs(0, row, column):
                    return True
        return False


#1/18/24 refresher:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[-1]) or board[r][c] != word[index]: #not equal to word index means equal to visited that we marked since visited would never be equal to a particular letter that we are looking for
            #we haven't returned False up to the last letter of the word, so if we reach the last index of the word, then we can say we found the entire word
                return False
            elif index >= len(word) - 1:
                return True
            original = board[r][c]
            board[r][c] = "visited"
            result = (dfs(index + 1, r + 1, c) or dfs(index + 1, r - 1, c) or dfs(index + 1, r, c + 1) or dfs(index + 1, r, c - 1))
            #if none of the 4 directions find the path, then return False and backtrack to last viable position that was not yet tried as a path
            board[r][c] = original
            return result
            


        for r in range(len(board)):
            for c in range(len(board[-1])):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        return False


#better notes:

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                return False
                #when False executes here, we return nothing to the call in result, and index, r, c all reset to 0 if we are still looking for the 2nd character, and we proceed to call the next function call a line down in result
            elif index >= len(word) - 1:
                return True
            #when we do find the next letter we are looking for, we start executing from the 1st line recursive call in result, but instead of resetting index, r, c to 0, index, r, c continue from the last value. note that, if we already made progress, and one of the function calls return False, then we start from the last viable point in which we know progress has been made, so index, r, c might reset to 1, 0, 1 if we already found a in "abcb" if the grid is board = [["A","B","C","E"], ["S","F","C","S"],["A","D","E","E"]], and we continue executing the next recursive call in result at the next line if the 1st one lead to False, so everytime we find another progress letter, then that (index, r, c) combination now becomes the last viable point to backtrack too if we return False from any of the 4 function calls
            original = board[r][c]
            board[r][c] = "visited"
            result = (
                dfs(index + 1, r + 1, c) or
                dfs(index + 1, r - 1, c) or
                dfs(index + 1, r, c + 1) or
                dfs(index + 1, r, c - 1)
            )
            board[r][c] = original
            return result
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
solution = Solution()
result = solution.exist(board, word)

#at this point, let's say that we've made progress up to (2, 0, 2), and from (2, 0, 2), we call all 4 recursive functions, and none of them lead to the next character. IN THAT CASE, WE WOULD board[r][c] = original because we already marked c as stepped on in board = [["A","B","CCCCCC","E"],["S","F","C","S"],["A","D","E","E"]], and we would return False, and then we would backtrack from (2, 0, 2) to (2, 0, 0), not (1, 0, 1) because THE ONLY VIABLE PATH FORWARD OUT OF THE 4 RECURSIVE CALLS from (1, 0, 1) that lead to a correct result, WAS (2, 0, 2).
#return result


#1/22/24 refresher:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                #return back to the dfs call that started it and try the next one down in result
                return False
            elif index >= len(word) - 1:
                return True
            original = board[r][c]
            board[r][c] = "visited"
            #if we find the letter in word that we are on in any of the 4 directions, we can mark it as visited and go onto the next word in our input string words
            result = (dfs(index + 1, r + 1, c) or dfs(index + 1, r - 1, c) or dfs(index + 1, r, c + 1) or dfs(index + 1, r, c - 1))
            #if we can't find the letter we are looking for in any of the 4 directions, then we have to start a new path and backtrack
            board[r][c] = original
            #return back to the parent call that started the wrong path and go back to the last viable path
            return result
            
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        return False


#1/24/24 refresher:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                return False
            #we found the word since we didn't return False before this returns True
            elif index >= len(word) - 1:
                return True
            original = board[r][c] 
            #word[index] will never be equal to visited
            board[r][c] = "visited"
            result = (dfs(index + 1, r + 1, c) or dfs(index + 1, r - 1, c) or dfs(index + 1, r, c + 1) or dfs(index + 1, r, c - 1))
            #we backtrack to the last viable path if all 4 directions don't make progress, so since we are starting a new path, we can reuse the cell
            board[r][c] = original
            return result

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        return False


#1/25/24 refresher:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                return False
            #haven't returned False up to the last letter in the word means we found the entire word
            elif index >= len(word) - 1:
                return True
            original = board[r][c]
            #visited will never equal a particular letter of the word, so it's a safe thing to set a cell to in order to represent it as already visited
            board[r][c] = "visited"
            result = (dfs(index + 1, r + 1, c) or dfs(index + 1, r - 1, c) or dfs(index + 1, r, c + 1) or dfs(index + 1, r, c - 1))
            #if we can't find the letter we are looking for in all 4 directions, we backtrack until the last viable point and un unmark the current cell since we aren't using it in a path
            board[r][c] = original
            #return False to the parent recursive call that started it and keep going
            return result



        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        return False


#1/31/24 refresher solution:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                return False
            elif index >= len(word) - 1:
                return True
            original = board[r][c]
            board[r][c] = "visited"
            result = (dfs(index + 1, r + 1, c) or dfs(index + 1, r - 1, c) or dfs(index + 1, r, c + 1) or dfs(index + 1, r, c - 1))
            board[r][c] = original
            return result
 

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        return False
