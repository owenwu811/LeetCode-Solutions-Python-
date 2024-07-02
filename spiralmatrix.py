#Given an m x n matrix, return all elements of the matrix in spiral order.

#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]



#Python3 solution:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        rows, cols = len(matrix), len(matrix[0])
        seen = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        r = c = d = 0  # Start from the top-left corner and move right initially
        for _ in range(rows * cols):
            res.append(matrix[r][c])
            seen.add((r, c))
            #if d is 0, then (directions[d][0], directions[d][1]) = (0, 1), meaning movement to the right, so nc is incremented by 1 while nr stays the same
            #if d is 1, (directions[d][0], directions[d][1]) = (1, 0), meaning movement downwards, so nr is incremented by 1 while nc stays the same
            nr, nc = r + directions[d][0], c + directions[d][1]
            # Change direction if next position is out of bounds or has been visited
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in seen:
                #change direction
                #rotating clockwise aka one position to the right
                #When d is 0, (d + 1) % 4 becomes 1, rotating the direction from right to down - we are only moving DOWN because (1, 0) is the 1st element
                #(1, 0) indicates moving down because we are moving one step down (increasing row index) while keeping column index unchanged
                d = (d + 1) % 4  
                nr, nc = r + directions[d][0], c + directions[d][1]
            r, c = nr, nc  # Move to the next position
        return res

#d - current direction of traversal, r - current row index, c - current column index, rows = total # of rows in matrix, cols = totral # of columns in matrix
#the %4 part ensures index stays within range (0, 3) inclusive because there are only 4 directions in total in directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


#The reason (d + 1) % 4 is used is to rotate the direction clockwise. When (d + 1) is calculated, it effectively rotates the direction by one position to the right.

#Here's how it works:

#When d is 0, (d + 1) % 4 becomes 1, rotating the direction from right to down.
#When d is 1, (d + 1) % 4 becomes 2, rotating the direction from down to left.
#When d is 2, (d + 1) % 4 becomes 3, rotating the direction from left to up.
#When d is 3, (d + 1) % 4 becomes 0, rotating the direction from up to right.


#3/16/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        seen = set()
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = c = d = 0 #start at top left corner
        for i in range(rows * cols): #if we have 3 x 3 grid, we have 9 elements in total. if we have 4 x 4 grid, we have 16 elements in total
            res.append(matrix[r][c])
            seen.add((r, c))
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen: #newr, newc in seen, not r, c in seen 
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res


#3/17/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return [] #the input is empty, so there's nothing to return
        res, seen = [], set() #list used to store final output, we can't visit the same element twice
        rows, cols = len(matrix), len(matrix[0]) #length of input
        r = c = d = 0 #start at top left corner
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(rows * cols): # 3 x 3 input, so 9 elements to traverse in total without duplicates because we don't care about visiting duplicates
            seen.add((r, c)) #make sure we don't visit our current cell multiple times - r and c are the current coordinates
            res.append(matrix[r][c]) #tile added to result
            newr, newc = r + directions[d][0], c + directions[d][1] #right, down, left, up
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4 #because we have 4 directions in total 
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res

#again on 3/17/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return [] #base case edge check
        res, seen = [], set()
        rows, cols = len(matrix), len(matrix[0]) #we need this to know how many times we will iterate because we will iterate height times width times, so if 6 by 8 grid, we have 48 iterations
        r = c = d = 0 #current indicies we are at
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #right, down, left, up - y, x, y, x - c, r, c, r
        for i in range(rows * cols): #3 x 3 means 9 total iterations because we don't care about duplicates
            seen.add((r, c)) #add current indicies to mark as visited, which can't be out of bounds or repeated because we start at 0, 0
            res.append(matrix[r][c]) 
            newr, newc = r + directions[d][0], c + directions[d][1] #move right first - directions[0][0], directions[0][1] = 0 + 0, 0 + 1 = 0, 1 = right
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4 #move one index in one of the 4 directions because d represents the current direction we are facing
                newr, newc = r + directions[d][0], c + directions[d][1] #we are facing the right direction, so now we just have to step onto the new tile
            r, c = newr, newc #update the current indicies to reflect the new change before going back to for loop
        return res

#again on 3/17/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return [] #the input is empty
        res, seen = [], set() #we don't want to visit the same cell twice
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #right, down, left, up
        r = c = d = 0 #start from top left cell of matrix
        for i in range(rows * cols): #if our grid is 4 x 4, we have 26 total cells to visit
            #note that we need (()) if we are appending more than one coordinate to our set, which we are since we are appending both r and c
            seen.add((r, c)) #add current row and column coordinates to our set to mark them as visited
            res.append(matrix[r][c]) #add the current cell to our result
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4 #we move one index in whatever direction and we only have 4 directions
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc #updating current row and column index
        return res



#3/18/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res, myset = [], set()
        rows, cols = len(matrix), len(matrix[0]) #dimensions of input needed to know how many iterations we will have because we have row * col number of iterations like 6 times 8 = 48 iterations
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #right, down, left, up
        r = c = d = 0
        for i in range(rows * cols):
            myset.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in myset:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res

#3/19/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res, seen = [], set()
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = c = d = 0
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res

#3/20/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res, seen = [], set()
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = c = d = 0
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res

#3/21/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #we want to start at the top left
        res = [] #result is an array - list in python
        seen = set()
        rows, cols = len(matrix), len(matrix[0]) #dimensions of our input used to multiply to get how many tiles we have to traverse
        r = c = d = 0 #starting at top left
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #right, down, left, up
        for i in range(rows * cols): #total number of iterations we have is the width times height aka total number of tiles we will traverse
            seen.add((r, c)) #r, c = current
            res.append(matrix[r][c]) #appending tile starting from top left
            newr, newc = r + directions[d][0], c + directions[d][1] # we have to change directions more than once, so newr and newc calculation goes inside of the for loop, not outside
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen: #not gonna be out of bounds or already in seen for the 1st turn because we're visiting a new tile for ther 1st time to the right assuming that the width of the grid if more than 1
                #we are out of bounds, so change directions according to depicted in the char, so down then left then up - we start coming from right
                d = (d + 1) % 4 #moving current direction because d is used to calculate newr and newc, the actual new tile
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc #setting current to the pivoted tile
        return res

#3/25/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        seen = set()
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = c = d = 0 #starting from top left
        for i in range(rows * cols): #number of iterations without visiting the same tile twice
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res

#3/29/24:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        rows, cols = len(matrix), len(matrix[0])
        r = c = d = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res

#4/10/24 (missed)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        rows, cols = len(matrix), len(matrix[0])
        seen = set()
        r = c = d = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res

#practice again:

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        rows, cols = len(matrix), len(matrix[0])
        r = c = d = 0 #start from top left
        seen = set() #use set to keep track of indicies to identify duplicates!
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen: #look if NEW COORDINATES WE JUST MOVED TO ARE IN SET
                d = (d + 1) % 4 #point in new direction since out of bounds or duplicate
                newr, newc = r + directions[d][0], c + directions[d][1] #actually move to new cell
            r, c = newr, newc
        return res
            

 
#practice again 4/10 afternoon:

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        rows, cols = len(matrix), len(matrix[0])
        seen = set()
        r = c = d = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res

#4/12/24:

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        r = c = d = 0 #current coordinate starting at top left 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res

#4/20/24 refresher:

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        r = c = d = 0
        seen = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1] #we move because we just added the 1st tile into our list and set already
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res


#4/30/24 refresher:

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        seen = set()
        res = []
        rows, cols = len(matrix), len(matrix[0])
        r = c = d = 0 #start at top left
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res


#5/16/24 refresher:

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        seen = set()
        r = c = d = 0
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(rows * cols):
            seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res
            

#7/2/24 review:

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = c = d = 0
        seen = set()
        for i in range(rows * cols):
            if (r, c) not in seen:
                seen.add((r, c))
            res.append(matrix[r][c])
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= len(matrix) or newc < 0 or newc >= len(matrix[0]) or (newr, newc) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return res
