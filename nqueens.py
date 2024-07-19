#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

#Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

#Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



#python3 solution:

class Solution:
    def solveNQueens(self, n):
        cols, posd, negd = set(), set(), set()
        board = [["."] * n for row in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r + c) in posd or (r - c) in negd:
                    continue
                cols.add(c)
                posd.add(r + c)
                negd.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                cols.remove(c)
                posd.remove(r + c)
                negd.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


#with explanations:

class Solution:
    def solveNQueens(self, n):
        col = set() #which column out of 0123 we have put a queen into already
        #0123
        #1.
        #2 .
        #3  .
        #notice above 1 - 1, 2 - 2, 3 - 3 are all 0 (this is negative diagnal) - (r - c) = 0 (computation will stay constant)
        #0123
        #1 .
        #2  .
        #3
        #(0 - 2) (row - column)
        #notice above (0 - 2) = -2 and (1 - 3) = -2 because we increase the column and row by one 
        #  0 1 2 3 #negative diagonals from top left to bottom right 
        #0 0 -1 -2
        #1 1 0 -1 -2
        #2 2 1 0 -1
        #3   2 1 0

        #  0 1 2 3 #positive diag from a to d start to end
        #0       d
        #1     c
        #2.  b 
        #3 a
        #notice above we are increasing column by 1 but decreasing the row by 1 (row 3 col 0) to (row 2 col 1), so we can't use (r - c) for positive diagonals because r - c will not be constant - it will be 3 for a and then 1 for b
        #because we increase THE COLUMN BUT DECREASE THE ROW, R + C is going to stay the same (3 + 0) for a is the same as (2 + 1) for b
        posDiag = set() #(r + c) 
        negDiag = set() #(r - c)
        res = []
        #we have an n * n board - putting a dot in every position 
        board = [["."] * n for i in range(n)] #. indicates empty location, so how many rows do we have when multiplied by n
        def backtrack(r): #row 0 through n - n is our base case meaning we completed every single row
            if r == n: #base case meaning we were able to find a valid n queens solution
                copy = ["".join(row) for row in board] #having a copy of board where each row is joined together. take copy and append it to result
                res.append(copy)
                return
            #not reach base case, so go through every single position in the current row we are at and see which positions we are allowed to place a queen in 
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue #not allowed to use this r, c position
                #update sets because weren't using combo before but are now
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q" #setting to queen instead of dot since was not used 
                backtrack(r + 1) #recursive call to go down one (one row down) 
                #we backtrack as soon as we can't place a single queen in the current row!
                col.remove(c) #undoing for backtracking - if the for loop continues for all it's iterations, we go to this line because that means we can't place a queen in this current row, so for example, when r = 2 and c = 3, and we continue, then we come down here because we can't place anything in the 2nd INDEXED aka 3rd row:
                #"Q"	"."	"."	"."
                #"."	"."	"Q"	"."
                #can't place anything in this row, so go to line "col.remove(c) to begin backtracking"
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "." 
                #above 3 lines removes the queen at the 2nd line:
                #"Q"	"."	"."	"."
                #"."	"."	"Q"	"."

                #becomes

                #"Q"	"."	"."	"."
                #"."	"."	"."	"."

                #next, we try 1, 3 by going back to - for c in range(n) - with 1 = r and 3 = c instead of 1, 2 as before that resulted in the dead end of not being able to place any queen in 3rd row!
                #next, if c in col - 3 is not in col set anymore because we removed it when we backtracked the first time
                #we now add 3 to col, 4 to posDiag, and -2 to negDiag
                #next, board[r][c] = "Q" makes:
                
                #"Q"	"."	"."	"."
                #"."	"."	"."	"."

                #turn into:

                #"Q"	"."	"."	"."
                #"."	"."	"."	"Q" 

                #because we are placing a Queen at row 1 column index 3 
                #next, we call backtrack(r + 1) to invoke the 2nd index or 3rd row
                #now, row = 2 and column = 0, so we start at the left hand side of each row!!!

                #because our board looks like:

                #"Q"	"."	"."	"."
                #"."	"."	"."	"Q" 


                #we know that 0 is already in col because it would be attacking from above if we placed a queen at row 2 col 0, so continue
                #now, row = 2, col = 1

                #row = 2 col = 1 seems fine, so we go ahead and add 1 to col set and 3 (2 + 1) to posdiag and 1 to negDiag(2 - 1), and then we go ahead and set board[r][c] to a Queen:

                #now our board looks like:

                #"Q"	"."	"."	"."
                #"."	"."	"."	"Q" 
                #"."	"Q"	"."	"." - note we just placed row 2 col 1 a queen 

                #next, we call backtrack(r + 1), so backtrack(3) to explore the last row and try to place a queen in it because n was 4 and we placed 3 queens so far, so we still need to place one more queen

                #if r == n - 3 == 4 is False, so enter the for c in range(n), so c becomes 0
                #this is our board, so we can't place r = 3 c = 0 a queen because would attack from above (this is hit by the if c in col check where 0 was already in our col set)

                #"Q"	"."	"."	"."
                #"."	"."	"."	"Q" 
                #"."	"Q"	"."	"."
                #row 3 we are currently trying to explore is not shown but would be here 
                
                #now, remember that we are exploring rows from left to right, so continue 
                #r = 3 c = 1 now - again, this is not ok since would attack from above as 1 is already in our col set
                #so continue, and r = 3 c = 2 - not ok because (r - c) aka (3 - 2) is already in negDiag because it would hit a queen toward the left diagnoal looking from
                #next, r = 3 c = 3, which is not ok because loop hits limit because for c in range(4) means 3 is last acceptable and can't continue toward c being 4
                
                #so now, we can't add anything in the 4th 3rd index last row, so we have to backtrack:

                #"Q"	"."	"."	"."
                #"."	"."	"."	"Q" 
                #"."	"Q"	"."	"."
                #can't add a valid queen in this last row

                #so now, we backtrack (col.remove(c)) - start here

        backtrack(0) #row 0 
        return res

        #the goal is to place n frequency of queens on the board 

#7/6/24 refresher:

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posD = set()
        negD = set()
        res = []
        board = [["."] * n for r in range(n)] #if we made ["."] into just ".", we would get error because board[r][c] wouldn't be an identifiable cell!
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return #even without return here, the solution works
            for c in range(n):
                if c in cols or (r + c) in posD or (r - c) in negD:
                    continue
                cols.add(c)
                posD.add(r + c) #if we swapped the order of posD and negD, it would work too
                negD.add(r - c)
                board[r][c] = "Q"
                dfs(r + 1)
                cols.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res

#7/8/24 (missed):

class Solution:
    def solveNQueens(self, n):
        res = []
        cols, posd, negd = set(), set(), set()
        board = [["."] * n for r in range(n)]
        def dfs(r):
            if r == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r + c) in posd or (r - c) in negd:
                    continue
                cols.add(c) #add the queen since another queen isn't already looking at this space in directions
                posd.add(r + c)
                negd.add(r - c)
                board[r][c] = "Q"
                dfs(r + 1)
                cols.remove(c)
                posd.remove(r + c)
                negd.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res

#7/9/24 refresher:

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posd, negd = set(), set(), set()
        board = [["."] * n for r in range(n)]
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                self.res.append(copy)
                return
            for c in range(n):
                if c in cols or (r + c) in posd or (r - c) in negd: #we've already been eyeing this cell
                    continue
                #not eyeing this cell, so place it
                cols.add(c)
                posd.add(r + c)
                negd.add(r - c)
                board[r][c] = "Q" #placing it after placing cells above so we know what cells we eye in the future
                dfs(r + 1)
                cols.remove(c)
                posd.remove(r + c)
                negd.remove(r - c)
                board[r][c] = "." #resetting it since we removed a queen from the most bottom row we last visited
        self.res = []
        dfs(0)
        return self.res


#7/14/24 review:

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posd, negd = set(), set(), set()
        board = [["."] * n for r in range(n)]
        self.res = []
        def dfs(r):
            if r == n:
                copy = ["".join(rows) for rows in board]
                self.res.append(copy)
                return
            for c in range(n):
                if c in cols or (r + c) in posd or (r - c) in negd:
                    continue
                cols.add((c))
                posd.add((r + c))
                negd.add((r - c))
                board[r][c] = "Q"
                dfs(r + 1)
                cols.remove((c))
                posd.remove((r + c))
                negd.remove((r - c))
                board[r][c] = "." #resetting back to an empty space

        
        dfs(0)
        return self.res

#7/19/24 refresher:

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [["."] * n for i in range(n)]
        cols, posd, negd = set(), set(), set()
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                self.res.append(copy)
                return
            for c in range(n):
                if c in cols or (r + c) in posd or (r - c) in negd:
                    continue
                cols.add((c))
                posd.add((r + c))
                negd.add((r - c))
                board[r][c] = "Q"
                dfs(r + 1)
                cols.remove((c))
                posd.remove((r + c))
                negd.remove((r - c))
                board[r][c] = "."
        dfs(0)
        return self.res
