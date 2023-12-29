#You are given an m x n grid where each cell can have one of three values:

#0 representing an empty cell,
#1 representing a fresh orange, or
#2 representing a rotten orange.
#Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

#Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
#Output: 4




#my solution python3:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque()
        fresh = 0
        time = 0
        #find all rotten oranges origianlly 
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    d.append([row, column])
                elif grid[row][column] == 1:
                    fresh += 1
                else:
                    continue
        #rot adjacent oranges
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d and fresh > 0:
            for i in range(len(d)):
                #first bad orange - x, y indicies 
                xoffirstrottingorange, yoffirstrottingorange = d.popleft()
                for newdirectionx, newdirectiony in directions:
                    #bad orange x + new direction x
                    #note myrow and mycolumn don't have to be the same as row and column
                    myrow, mycolumn = xoffirstrottingorange + newdirectionx, yoffirstrottingorange + newdirectiony
                    if myrow < 0 or myrow >= len(grid) or mycolumn < 0 or mycolumn >= len(grid[0]) or grid[myrow][mycolumn] != 1:
                        continue
                    grid[myrow][mycolumn] = 2
                    d.append([myrow, mycolumn])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else - 1


#my solution python3 with explanations:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #we can only rot fresh oranges into rotting oranges, not empty cells
        #deque used to keep track of all rotting oranges left that can possibly cause destruction in 4 directions - we will loop through this deque later. deque used to place where oranges can rot and is used to keep track of indicies or coordinates of rotting oranges at time 0
        d = deque()
        mintime = 0
        numberoffresh = 0
        #loop through grid to find all rotten oranges from time 0
        for rows in range(len(grid)):
            for columns in range(len(grid[0])):
                if grid[rows][columns] == 1:
                    numberoffresh += 1
                elif grid[rows][columns] == 2:
                    #append coordinates of rotten orange from time 0
                    d.append([rows, columns])
                else:
                    continue
        #we can rot in all 4 directions
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #means there are oranges to rot and rotting oranges in our deque ready to cause destruction
        while d and numberoffresh > 0:
            for index in range(len(d)):
                #values from the deque represent the x and y coordinates of the rotten oranges we found from time 0
                xfirstrotten, yfirstrotten = d.popleft()
                for xnew, ynew in directions:
                    
                    rotadjacentx, rotadjacenty = xfirstrotten + xnew, yfirstrotten + ynew
                    if rotadjacentx < 0 or rotadjacentx >= len(grid) or rotadjacenty < 0 or rotadjacenty >= len(grid[0]) or grid[rotadjacentx][rotadjacenty] != 1:
                        continue
                    grid[rotadjacentx][rotadjacenty] = 2
                    d.append([rotadjacentx, rotadjacenty])
                    numberoffresh -= 1
            mintime += 1
        return mintime if numberoffresh == 0 else -1
