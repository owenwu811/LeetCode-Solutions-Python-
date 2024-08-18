#medium

#419

#Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

#Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).


#my own solution using python3 after a small mistake:

#note this is identical to number of islands 

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(r, c):
            #board[r][c] != 'X':
#This condition checks if the current cell board[r][c] is not an "X". If it is not an "X", the DFS should return immediately because either:
#The cell is water ("."), meaning it’s not part of a battleship.
#The cell has already been visited and marked as "visited", so further exploration in this direction isn't necessary.
          #Why Not Use board[r][c] == 'X':
#If you were to use board[r][c] == 'X' as the base condition, the DFS would only stop when it encounters an "X", which is the opposite of what you want. The DFS needs to continue when it finds an "X" (because that's part of a battleship) and only stop when it finds something else (either "." or "visited").
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != 'X':
                return
            board[r][c] = "visited"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "X":
                    count += 1
                    dfs(r, c)
        return count
