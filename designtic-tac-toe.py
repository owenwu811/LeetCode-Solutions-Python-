

#348
#medium

#Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

#A move is guaranteed to be valid and is placed on an empty block.
#Once a winning condition is reached, no more moves are allowed.
#A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
#Implement the TicTacToe class:

#TicTacToe(int n) Initializes the object the size of the board n.
#int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
#0 if there is no winner after the move,
#1 if player 1 is the winner after the move, or
#2 if player 2 is the winner after the move.


#my own solution using python3:

class TicTacToe:
    def __init__(self, n: int):
        self.finishline = n
        self.board = [["x"] * n for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player 
        rows = []
        for b in self.board:
            rows.append(b)
        cols = []
        j = 0
        while j < len(self.board):
            k = 0
            curcol = []
            for k in range(len(self.board)):
                curcol.append(self.board[k][j])
            cols.append(curcol)
            j += 1
        posdiag = []
        startr, startc = 0, 0
        while startr <= len(self.board) - 1 and startc <= len(self.board) - 1:
            posdiag.append(self.board[startr][startc])
            startr += 1
            startc += 1
        negdiag = []
        startr, startc = len(self.board) - 1, 0
        while startr >= 0 and startc <= len(self.board) - 1:
            negdiag.append(self.board[startr][startc])
            startr -= 1
            startc += 1
        for r in rows:
            if "x" not in r and len(set(r)) == 1:
                return player
        for c in cols:
            if "x" not in c and len(set(c)) == 1:
                return player
        if len(set(posdiag)) == 1:
            if posdiag[0] == 1:
                return 1
            elif posdiag[0] == 2:
                return 2
        if len(set(negdiag)) == 1:
            if negdiag[0] == 1:
                return 1
            elif negdiag[0] == 2:
                return 2
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
