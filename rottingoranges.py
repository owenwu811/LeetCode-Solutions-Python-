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


#12/20/23 refresher with explanation python3 - my solution: 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #each deque will represent original rotten oranges from a particular timeslot 
        d = deque()
        minminutes = 0
        numberoffresh = 0
        #find all rotten oranges from:
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    #indicies of each rotten orange we found at time 0
                    d.append([row, column])
                elif grid[row][column] == 1:
                    numberoffresh += 1
                else:
                    continue
        #since we found all rotten oranges from a particular timeslot, we now want to simulate the spread of rotting and correlate the spread to each minute progression
        #remember, we can spread the disease in all 4 directions aka 4 directionally adjacent
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #since each deque represents the coordinates of each rotten orange from a particular timeslot, we want to start the spread, so we have to loop through the deque, a list of lists, and since the values of the list is the x and y of the rotten orange from the original timeslot, we want to add this original x and y value to all 4 x and y values from each sublist in directions
        #remember, this entire block of code below this represents the simulation process of spreading disease at a particular timeslot, which is why we pop from the deque after counting that organge from a particular timeslot and then add to the deque the new destroyed orange since the new destroyed orange can spread to other destroyed oranges at a new timeslot while the original bad orange can only destroy adjacently once in all directions from it's own timeslot
        while d and numberoffresh > 0:
            #since each deque represents each timeslot, the change in time should line up with this
            for index in range(len(d)):
                #we have to get rid of each coordinate from the deque as we can't count the same orange twice from the same timeslot 
                xoforiginal, yoforiginal = d.popleft()
                for xofnew, yofnew in directions:
                    destroyx, destroyy = xoforiginal + xofnew, yoforiginal + yofnew
                    #while stepping onto this new coordinate that we will spread the disease to, this new coordinate must be in the grid and also must be a fresh orange to rot, not an already rotten orange (2) or an empty cell (0)
                    #if this new grid we are stepping onto in one particular sublist direction from the directions sublist + our original coordinate is out of bounds or not a fresh orange, we can continue since this is not recursive but iterative
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    #if this new grid from a particular timeslot and a particular direction is a fresh orange and in the grid, then we can make that fresh orange rotten by turning the 1 in that new grid to a 2
                    grid[destroyx][destroyy] = 2
                    #since this new grid from a particular timeslot and direction's 1 became a 2, we need to reflect that one less fresh orange in our count of fresh oranges to determine if we can even rot all FRESH oranges we have 
                    numberoffresh -= 1
                    #since this new grid from a particular timeslot and direction's 1 became a 2, we now have a new rotten orange, that, from the NEXT TIMESLOT, can spread to other fresh oranges in all 4 directions, so add this slot's coordinates to the deque
                    d.append([destroyx, destroyy])
            minminutes += 1
        #after we have no more rotten oranges to rot or no more fresh oranges, we return minminutes. but if we still have fresh oranges that have not ever been adjacent to a rotting orange after this entire process of spreading at each timeslot and stepping onto new directions in the grid, we return -1 - this is the case where deque is empty meaning no more diseases to spread or rotten oranges to spread but still have fresh oranges
        return minminutes if numberoffresh == 0 else -1


#12/31/23 refresher:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque()
        freshcount = 0
        minminutesres = 0
        #starting from time 0 slot, find all rotting oranges and add them to the deque by adding their indiciy coordinate
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    d.append([row, column])
                #we need to count fresh oranges to make sure we can even rot any fresh oranges. if no fresh oranges exist, then we won't increment minutes, and we will return -1 at the end since freshcount stays 0
                elif grid[row][column] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        #we want to make sure we have rotten oranges from time slot 0 and there are fresh oranges to rot so we won't have to return -1 
        while d and freshcount > 0:
            #since we do have work to do, we loop through out deque, which represents a time period where the rotting spread happens
            for rottenorangeindex in range(len(d)):
                #since we know our deque will have the coordinates / indicies of rotten oranges from a time slot starting from the first time slot, we unpack those indicies into an x and y coordinate
                rottenorangexindex, rottenorangeyindex = d.popleft()
                #now, we have to simulate the spread, so we loop through our directions and spread the rotting in all 4 directions using unpacking as well because our directions array is a list of lists with 2 values in each sublist
                for xnewindex, ynewindex in directions:
                    #make a new x and y variables to represnet the new tile that was rotted in this time frame
                    xdestroyedindex, ydestroyedindex = xnewindex + rottenorangexindex, ynewindex + rottenorangeyindex
                    #boundary check the new tile we are spreading the disease to and make sure this new tile has a fresh orange or 1 because we can only rot fresh oranges into rotten and not empty cells of cells with already rotten oranges - 2s in them
                    if xdestroyedindex < 0 or xdestroyedindex >= len(grid) or ydestroyedindex < 0 or ydestroyedindex >= len(grid[0]) or grid[xdestroyedindex][ydestroyedindex] != 1:
                        continue
                    grid[xdestroyedindex][ydestroyedindex] = 2 #set the fresh ornage to rotten so we don't run into an infinite loop because we will keep searching for 1s in all 4 directions for this particular timeframe
                    #after turning a fresh orange rotten, we have to reflect this change in our total number of fresh oranges and add this new rotting orange that we just turned from 1 to 2 into the next timeslot aka our deque - we never pop off rotting oranges off the deque because rotting oranges never change
                    freshcount -= 1
                    #we are appending a coordinate pair of indicies of the new rotten orange we just turned rotten as a sublist 
                    d.append([xdestroyedindex, ydestroyedindex])
            minminutesres += 1
        return minminutesres if freshcount == 0 else -1
