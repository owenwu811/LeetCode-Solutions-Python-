
#885
#medium

#You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

#You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

#Return an array of coordinates representing the positions of the grid in the order you visited them.

#Input: rows = 5, cols = 6, rStart = 1, cStart = 4
#Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


#my own solution using python3:

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        startx, starty = rStart, cStart 
        bigger = max(rows, cols)
        res = []
        res.append([startx, starty])
        allowance, turnsallowed = 1, 1
        right, down = [0, 1], [1, 0]
        left, up = [0, -1], [-1, 0]
        curx, cury = startx, starty
        for i in range(bigger):
            allowance = turnsallowed
            #print(turnsallowed, "t")
            h = allowance
            #print(allowance, "r")
            while allowance > 0:
                curx, cury = curx + right[0], cury + right[1]
                if curx >= 0 and curx < rows and cury >= 0 and cury < cols:
                    print(curx, cury)
                    res.append([curx, cury])
                allowance -= 1
            allowance = h
            #print(allowance, "d")
            while allowance > 0:
                curx, cury = curx + down[0], cury + down[1]
                if curx >= 0 and curx < rows and cury >= 0 and cury < cols:
                    print(curx, cury)
                    res.append([curx, cury])
                allowance -= 1
            allowance = h + 1
            #print(allowance, "l")
            leftallowance = h + 1
            while allowance > 0:
                curx, cury = curx + left[0], cury + left[1]
                if curx >= 0 and curx < rows and cury >= 0 and cury < cols:
                    print(curx, cury)
                    res.append([curx, cury])
                allowance -= 1
            allowance = h + 1
            #print(allowance, "u")
            while allowance > 0:
                curx, cury = curx + up[0], cury + up[1]
                if curx >= 0 and curx < rows and cury >= 0 and cury < cols:
                    print(curx, cury)
                    res.append([curx, cury])
                allowance -= 1
            turnsallowed = leftallowance + 1
        return res

        

        #right
        #down 

        #left, left 
        #up, up

        #right, right, right #problem is right, down is still getting 2 instead of 3
        #down, down, down 

        #left, left, left, left 
        #up, up, up, up

        #right, right, right, right, right
        #down, down, down, down, down 
        
        #left, left, left, left, left, left 
        #up, up, up, up, up, up
