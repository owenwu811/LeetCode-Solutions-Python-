
#Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

#The distance between two adjacent cells is 1.

#Ex. mat = [[0,0,0],[0,1,0],[1,1,1]] > [[0,0,0],[0,1,0],[1,2,1]]




#python3 solution:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #we want the matrix at the end that shows, from each cell in the final matrix, how many hops it would take to reach a 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #our deque stores the coordinates of all 0s in the grid
        d = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0: # we are adding all 0 cell coordinates to the deque
                    d.append(([r, c]))
                else: #we see a 1, so we want to find the distance between this cell and the nearest 0 and put that distance as the value for this particular cell in our result
                    mat[r][c] = float('inf')
        while d:
            #these are the new coordinates of every 0, not r and c, so when you update and compare, you use zerox and zeroyy and not r and c - zerox and zeroyy are the starting points aka they are coordinates of a 0 cell, and since we start from every 0 cell coordinate on the deque and move somewhere new, then we are garunteed to land on a 1 cell because anything different from a 0 is a 1 cell, so that's why newonetilex and newonetiley are garunteed to be cooridnates of a 1 cell
            zerox, zeroy = d.popleft()
            for xnew, ynew in directions:
                #we are taking the coordinate of the 0 and exploring adjacent directions from that cell
                newonetilex, newonetiley = zerox + xnew, zeroy + ynew #assuming that this represents coordinates of a tile containing a 1 because the double for loop caught all the 0 tiles in the entire matrix
                #make sure that we are in bounds, so the if condition being true represents we are inbounds and found a smaller distance for that particular cell
                if 0 <=  newonetilex < len(mat) and 0 <= newonetiley  < len(mat[0]) and mat[newonetilex][newonetiley] > mat[zerox][zeroy] + 1:
                    #so again, remember we want each tile to represent the nearest distance from our one to a zero
                    mat[newonetilex][newonetiley] = mat[zerox][zeroy] + 1
                    #The line d.append([onex, oney]) adds newly discovered neighboring cells (which are '1's) to the deque d. 
                    #This ensures that these newly discovered cells are explored in the subsequent iterations, following the BFS strategy. 
                    #Without this line, the algorithm would not explore these neighboring cells immediately. 
                    #Instead, it would only consider the cells that were initially added to d, and it would explore them layer by layer. 
                    #This might not fully utilize the BFS strategy, potentially leading to inefficiency in finding the shortest distances.
                    d.append((newonetilex, newonetiley))
        return mat

#meaning of - mat[newonetilex][newonetiley] > mat[zerox][zeroy] + 1:
#let's say you are on a grid like:
# 000
# 010
# 000 
#and let's say you are on the 1 - well, you know that adjacent cells are INBOUNDS, but then you also know that infinity is bigger than the adjacent cell plus 1 - since your adjacent cells will always be a 0, you know that mat[zerox][zeroy] corresponds to 0, and 0 + 1 = 1, so infinity > 1, so infinity is set to 1 in the next line - mat[newonetilex][newonetiley] = mat[zerox][zeroy] + 1

#if we changed d.popleft() to d.pop(), this would be LIFO instead of FIFO. REMEMBER THAT BFS ALGORITHMS GENERALLY USE FIFO ORDERING ON A STACK WHILE DFS ALGORITHMS GENERALLY USE LIFO ORDERING ON A STACK - BFS WITH FIFO IS GOOD FOR FINDING SHORTEST PATH OR DISTANCES IN A GRAPH OR MATRIX. 


#2/14/24:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #we want the distance of the nearest 0 to the 1 we are on as the value of every tile in the grid
        d = deque()
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0: #all 0 coordinates go inside of our deque
                    d.append([r, c])
                else: #all 1 coordinates are set to infinity
                    mat[r][c] = float('inf')
        while d:
            zerox, zeroy = d.popleft() #FIFO = BFS
            for newx, newy in directions:
                onex, oney = zerox + newx, zeroy + newy
                if 0 <= onex < len(mat) and 0 <= oney < len(mat[0]) and mat[onex][oney] > mat[zerox][zeroy] + 1:
                    #marking as visited since we only start from 1 cells and don't want to keep revisiting the same one cell over and over again
                    mat[onex][oney] = mat[zerox][zeroy] + 1
                    d.append([onex, oney]) #do append it to the rear
        return mat

#another refresher:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #we want to return a Matrix called mat at the end with the tiles in the matrix being the distance to the nearest 0
        if not mat:
            return []
        d = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    d.append([r, c])
                else: #not a 0, so we know this is a 1, so we set this tile to infinity so that nothing will be bigger than infinity later
                    mat[r][c] = float('inf')
        while d:
            for i in range(len(d)):
                zerox, zeroy = d.popleft()
                for newx, newy in directions:
                    onex, oney = zerox + newx, zeroy + newy
                    if 0 <= onex < len(mat) and 0 <= oney < len(mat[0]) and mat[onex][oney] > mat[zerox][zeroy] + 1:
                        mat[onex][oney] = mat[zerox][zeroy] + 1
                        d.append([onex, oney])
        return mat

#2/15/24:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #we want to start from a 1 and fill that 1 tile with the smallest number of hops it takes to reach an adjacent 0 tile
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #stores the coordinates of all 0 tiles originally so we don't start from them and step onto a different tile starting from a 0 tile
        d = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    d.append([r, c])
                else: # if the tile is a 1, then we set to infinity
                    mat[r][c] = float('inf')
        #we need to now start from 1s and find the nearest 0 and fill the 1 cell with the shortest distance
        while d:
            for i in range(len(d)):
                zerox, zeroy = d.popleft() #BFS = FIFO
                for newx, newy in directions:
                    onex, oney = zerox + newx, zeroy + newy
                    if 0 <= onex < len(mat) and 0 <= oney < len(mat[0]) and mat[onex][oney] > mat[zerox][zeroy] + 1:
                        mat[onex][oney] = mat[zerox][zeroy] + 1
                        d.append([onex, oney])
  
        return mat


#2/16/24:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #we want every cell in the matrix, a list of list of integers that we will return, to be the distance from that cell to the nearest 0
        if not mat:
            return []
        d = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    d.append([r, c])
                else: #1 
                    mat[r][c] = float('inf')
        while d:
            for i in range(len(d)):
                #anything away from a 0 tile will be a 1 tile if the current tile exceeds the value of the previous tile we came from
                zerox, zeroy = d.popleft()
                for newx, newy in directions:
                    onex, oney = zerox + newx, zeroy + newy
                    if 0 <= onex < len(mat) and 0 <= oney < len(mat[0]) and mat[onex][oney] > mat[zerox][zeroy] + 1:
                        #because our zero cell was one adjacent away from our current one cell, we set the 1 cell to the zero cell plus 1 to represent the distance
                        mat[onex][oney] = mat[zerox][zeroy] + 1
                        #bfs is FIFO 
                        d.append([onex, oney])
        return mat


#2/17/24:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #we want each tile to represent the distance to the nearest zero 
        distance = [(0, 1), (0, -1), (1, 0), (-1, 0)] # we use tuple unpacking to traverse the matrix and step onto a new cell
        d = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    d.append([r, c])
                else: #a 1
                    mat[r][c] = float('inf')
        while d:
            for i in range(len(d)):
                zerox, zeroy = d.popleft() #BFS = FIFO
                for newx, newy in distance: #tuple unpacking
                    onex, oney = zerox + newx, zeroy + newy
                                                                             #will be infinity in 1st turn, making comparison valid
                    if 0 <= onex < len(mat) and 0 <= oney < len(mat[0]) and mat[onex][oney] > mat[zerox][zeroy] + 1:
                        #setting actual closest distance to the zero value on the right side since that zero cell is adjacent to our current 1
                        mat[onex][oney] = mat[zerox][zeroy] + 1 
                        d.append([onex, oney])
        return mat

#2/19/24:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #we want the distance in units of 1 to the nearest 0 from each cell to be the final value for that cell in the list of list matrix we will return at the end
        distance = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        d = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    d.append([r, c])
                else: #cell contains a 1, so set to infinity so that our conditional allows us to update that cell since infinity will always be bigger than the value in any zero cell + 1
                    mat[r][c] = float('inf')
        while d:
            for i in range(len(d)):
                zerox, zeroy = d.popleft() #BFS = FIFO
                for newx, newy in distance:
                    onex, oney = zerox + newx, zeroy + newy
                    if 0 <= onex < len(mat) and 0 <= oney < len(mat[0]) and mat[onex][oney] > mat[zerox][zeroy] + 1:
                        #a 0 cell must be adjacent to this 1 cell for the mat[onex][oney] > mat[zerox][zeroy] + 1 conditional to be True
                        mat[onex][oney] = mat[zerox][zeroy] + 1
                        d.append([onex, oney])
        return mat
        

#2/20/24:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        d = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    d.append([r, c])
                else:
                    mat[r][c] = float('inf')
        while d:
            #BFS = FIFO
            for i in range(len(d)):
                zerox, zeroy = d.popleft()
                for newx, newyy in directions:
                    onex, oney = zerox + newx, zeroy + newyy
                    if 0 <= onex < len(mat) and 0 <= oney < len(mat[0]) and mat[onex][oney] > mat[zerox][zeroy] + 1:
                        mat[onex][oney] = mat[zerox][zeroy] + 1
                        d.append([onex, oney])
        return mat


#2/22/24:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #will store all coordinates for 0
        d = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    d.append([r, c])
                else:
                    #we do this so that infinity is always bigger and will set that 1 tile to the nearest 0 value
                    mat[r][c] = float('inf')
        while d:
            for i in range(len(d)):
                #bfs = fifo
                zerox, zeroy = d.popleft()
                for newx, newy in directions:
                    onex, oney = zerox + newx, zeroy + newy
                    if 0 <= onex < len(mat) and 0 <= oney < len(mat[0]) and mat[onex][oney] > mat[zerox][zeroy] + 1:
                        mat[onex][oney] = mat[zerox][zeroy] + 1
                        d.append([onex, oney])
        return mat
