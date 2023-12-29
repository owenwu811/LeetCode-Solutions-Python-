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


#another practice run with important explanation:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #we can only rot an oranhe that is a 1, or, fresh, and if it's adjacent to a rotten orange (2)
        #we know that, at minute 0, there are going to be some rotting oranges, so our task in the first loop will be to find those oranges
        d = deque()
        numberoffresh = 0
        minimumtime = 0
        #find rotten oranges from time 0 that will start the destruction process
        for rows in range(len(grid)):
            for columns in range(len(grid[0])):
                if grid[rows][columns] == 1:
                    numberoffresh += 1
                elif grid[rows][columns] == 2:
                    #append the coordinates of the first rotten orange we found onto the deque list in order 
                    d.append([rows, columns])
                else:
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #we have rotten oranges ready to cause destruction and fresh oranges waiting to be rotten
        while d and numberoffresh > 0:
            #each sublist in d represents the coordinates of a rotting orange that started with the original rotten orange that will rot adjacent oranges for A PARTICULAR MINUTE 
            for index in range(len(d)):
                xoffirstrotten, yoffirstrotten = d.popleft()
                #all adjacent oranges rotting process for a particular minute
                for newdirectionx, newdirectiony in directions:
                    xofdestroynow, yofdestroynow = xoffirstrotten + newdirectionx, yoffirstrotten + newdirectiony
                    if xofdestroynow < 0 or xofdestroynow >= len(grid) or yofdestroynow < 0 or yofdestroynow >= len(grid[0]) or grid[xofdestroynow][yofdestroynow] != 1:
                        continue
                    grid[xofdestroynow][yofdestroynow] = 2
                    d.append([xofdestroynow, yofdestroynow])
                    numberoffresh -= 1
            #IMPORTANT: we need to go through all rotten oranges from time 0 before incrementing minimumtime - time 0 could have more than 1 rotten orange, so just 4 directions of just 1 isn't enough to say tha we're finished rotting all oranges for that particular timeslot
            minimumtime += 1
        return minimumtime if numberoffresh == 0 else -1



#again - refresher 12/29/23

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottingorangesl = deque()
        minminutes = 0
        numberoffresh = 0
        #find all rotten oranges from time 0 
        for rows in range(len(grid)):
            for columns in range(len(grid[0])):
                if grid[rows][columns] == 2:
                    #coordinates of the first rotten orange
                    rottingorangesl.append([rows, columns])
                elif grid[rows][columns] == 1:
                    numberoffresh += 1
                else:
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while rottingorangesl and numberoffresh > 0:
            for i in range(len(rottingorangesl)):
                xoffirstrotting, yoffirstrotting = rottingorangesl.popleft()
                for newx, newy in directions:
                    destroyx, destroyy = xoffirstrotting + newx, yoffirstrotting + newy
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1: 
                        continue
                    grid[destroyx][destroyy] = 2
                    numberoffresh -= 1
                    rottingorangesl.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if numberoffresh == 0 else -1
