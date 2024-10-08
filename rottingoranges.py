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

#1/2/24 refresher solution:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque()
        minminutes = 0
        numberoffresh = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    d.append([row, column])
                elif grid[row][column] == 1:
                    numberoffresh += 1
                else:
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d and numberoffresh > 0:
            for orange in range(len(d)):
                xofrotten, yofrotten = d.popleft()
                for xnew, ynew in directions:
                    xdestroy, ydestroy = xofrotten + xnew, yofrotten + ynew
                    if xdestroy < 0 or xdestroy >= len(grid) or ydestroy < 0 or ydestroy >= len(grid[0]) or grid[xdestroy][ydestroy] != 1:
                        continue
                    grid[xdestroy][ydestroy] = 2
                    numberoffresh -= 1
                    #remember, this is a sublist that will be unpacked, so popleft equals to ONE sublist, and then the xdestroy, ydestroy will be set, in order, to the first and second values of that sublist
                    d.append([xdestroy, ydestroy])
            minminutes += 1
        return minminutes if numberoffresh == 0 else -1


#1/4/24 refresher:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #use a deque to keep track of all rotten oranges at a particular time slot
        d = deque()
        minminutes = 0
        freshcount = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    d.append([row, column])
                elif grid[row][column] == 1:
                    freshcount += 1
                else:
                    continue
        #we want to spread the rot in all 4 directions
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d and freshcount > 0:
            for rottenoranges in range(len(d)):
                xofrotten, yofrotten = d.popleft()
                for xnew, ynew in directions:
                    destroyx, destroyy = xofrotten + xnew, yofrotten + ynew
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    d.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1



#1/6/24 refresher solution:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minminutes = 0
        freshcount = 0
        d = deque()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    d.append([row, column])
                elif grid[row][column] == 1:
                    freshcount += 1
                #we don't care about 0s or empty spaces, and we know we are only given 0s and 1s and 2s in our grid
                else:
                    continue
        #simulate the spread in all 4 directions using coordinates as indices 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d and freshcount > 0:
            for i in range(len(d)):
                xrotten, yrotten = d.popleft()
                for xofnew, yofnew in directions:
                    #we have to get the new coordinate we are stepping onto - xdstroy and ydestroy - before we boundary check and make sure the new coordinate is a fresh orange that we can rot 
                    xdestroy, ydestroy = xrotten + xofnew, yrotten + yofnew
                    if xdestroy < 0 or xdestroy >= len(grid) or ydestroy < 0 or ydestroy >= len(grid[0]) or grid[xdestroy][ydestroy] != 1:
                        continue
                    #prevent infinite looping
                    grid[xdestroy][ydestroy] = 2
                    freshcount -= 1
                    d.append([xdestroy, ydestroy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#1/7/24 my refresher solution with explanation:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #deque represents all the initial rotten oranges at the 1st time slot
        d = deque()
        minminutes = 0
        freshcount = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    d.append([row, column])
                elif grid[row][column] == 1:
                    freshcount += 1
                elif grid[row][column] == 0:
                    continue
        #start the spread of rotten oranges in all 4 directions at a certain timeslot 
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while d and freshcount > 0:
            for i in range(len(d)):
                xrottenindex, yrottenindex = d.popleft()
                for xdestroy, ydestroy in directions:
                    xrotcell, yrotcell = xrottenindex + xdestroy, yrottenindex + ydestroy
                    #the new cell that we are trying to rot must be 4 directionally adjacent to a rotten orange, simulated by the directions list of lists above selecting a random direction to step. the new cell that we are trying to rot must also be in the bounds of the grid and must be a fresh cell (1) and not an empty cell (0)
                    if xrotcell < 0 or xrotcell >= len(grid) or yrotcell < 0 or yrotcell >= len(grid[0]) or grid[xrotcell][yrotcell] != 1:
                        continue
                    grid[xrotcell][yrotcell] = 2
                    #we rot by stepping onto a new cell in the grid through unpacking pairs of indicies, and the deque represents a particular time slot
                    d.append([xrotcell, yrotcell])
                    freshcount -= 1
            #each time cell has passed since we iterated through the entire d from time 0, so increment minminutes
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#1/9/24 refresher:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #each time limit is represented with the deque
        d = deque()
        minminutes = 0
        freshcount = 0
        #we can only turn fresh oranges (1) into rotten (2)
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    #the coordinates to identify the cell of the rotten orange from this particular time slot
                    d.append([row, column])
                elif grid[row][column] == 1:
                    freshcount += 1
                elif grid[row][column] == 0:
                    continue
        #simulate the spread in all 4 directions - we will step onto this cell from each fresh orange in our deque at a particular minute
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while d and freshcount > 0:
            for i in range(len(d)):
                #unpacking the coordinates of the rotten oranges from our d from left to right because each sublist only has 2 values
                rottenr, rottenc = d.popleft()
                #unpacking directions aka the cells we want to step onto - the format of directions is the same as the deque - list of lists with 2 values in each sublist describing coordinates or indicies to identify a spot in our cell
                for xsteponto, ysteponto in directions:
                    rotthisx, rotthisy = rottenr + xsteponto, rottenc + ysteponto
                    #now that we have to cell we want to rot because it's adjacent to the rotten orange from that timeslot, we have to boundary check and make sure the new cell is a fresh orange we can rot - if we are out of bounds of the cell dosen't contain a 1 aka fresh orange, then we go in another direction
                    if rotthisx < 0 or rotthisx >= len(grid) or rotthisy < 0 or rotthisy >= len(grid[0]) or grid[rotthisx][rotthisy] != 1:
                        continue
                    grid[rotthisx][rotthisy] = 2
                    freshcount -= 1
                    #the format is the same as d.append[row, column] 
                    d.append([rotthisx, rotthisy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1

#1/13/ 24 refresher:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #number of rotten oranges from time 0
        d = deque()
        minminutes = 0
        numberoffresh = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                #we will use rotten from this time slot to spread the disease later in all 4 directions
                if grid[row][column] == 2:
                    d.append([row, column])
                elif grid[row][column] == 1:
                    numberoffresh += 1
                else:
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d and numberoffresh > 0:
            #for each time slot
            for i in range(len(d)):
                xofrotten, yofrotten = d.popleft()
                for xnew, ynew in directions:
                    xdestroy, ydestroy = xofrotten + xnew, yofrotten + ynew
                    if xdestroy < 0 or xdestroy >= len(grid) or ydestroy < 0 or ydestroy >= len(grid[0]) or grid[xdestroy][ydestroy] != 1:
                        continue
                    grid[xdestroy][ydestroy] = 2
                    numberoffresh -= 1
                    d.append([xdestroy, ydestroy])
            minminutes += 1
        if numberoffresh == 0:
            return minminutes
        else:
            return -1


#1/14/24 practice:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #all rotten oranges at each timeslot will be inside of the deque
        d = deque()
        minminutes = 0
        freshcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                #we found a rotten orange at this timeslot, so append the indicies / coordinates of that orange so we can spread from that cell in the future by unpacking from left to right
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else: # we don't care about empty cells or input values of 0
                    continue
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        #we have fresh oranges to rot and rotten oranges to infect others at this timeslot
        while len(d) > 0 and freshcount > 0:
            for index in range(len(d)):
                xinfected, yinfected = d.popleft()
                for xnew, ynew in directions:
                    #infecting another cell in one of the 4 directions
                    xdestroy, ydestroy = xinfected + xnew, yinfected + ynew
                    #boundary check and make sure we see a 1 on the new cell we are stepping onto 
                    if xdestroy < 0 or xdestroy >= len(grid) or ydestroy < 0 or ydestroy >= len(grid[0]) or grid[xdestroy][ydestroy] != 1:
                        continue
                    #rot the current cell since we are in bounds and initially found a 1 here
                    grid[xdestroy][ydestroy] = 2
                    #reflect the change in freshcount
                    freshcount -= 1
                    #append this new rotten orange so that, in the next minute, this new rotten orange, identified by its coordinates, can rot other oranges
                    d.append([xdestroy, ydestroy])
            #since an entire iteration of the deque represents an entire minute, increment minminutes
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#1/16/24 refresher:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #use a deque to keep track of all rotten oranges at a particular minute as we can pop off the deque and append to it - we will pop off rotten oranges off the deque while also appending the neighboring rotten oranges
        d = deque()
        minminutes = 0
        freshcount = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        #now we have all the fresh oranges from the 1st minute appended onto the deque in form of lists 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while len(d) > 0 and freshcount > 0:
            #unppacking list of length 2 representing x and y coordinates of the bad oranges from that minute
            for i in range(len(d)):
                badx, bady = d.popleft()
                for xdestroy, ydestroy in directions:
                    #the new coordinate we will try to rot that is adjacent and in one of the four directions
                    rotx, roty = badx + xdestroy, bady + ydestroy
                    if rotx < 0 or rotx >= len(grid) or roty < 0 or roty >= len(grid[0]) or grid[rotx][roty] != 1:
                        continue
                    grid[rotx][roty] = 2
                    freshcount -= 1
                    #will spread in the next minute 
                    d.append([rotx, roty])
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#1/18/24 refresher:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #used to keep track of rotten oranges at each timeslot
        d = deque()
        freshcount = 0
        minminutes = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    #indicies / coordinates to identify the cell that the rotten orange is in 
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while len(d) > 0 and freshcount > 0:
            #each minute, we will simulate the rotting process
            for i in range(len(d)):
                #we are unpacking the 1st sublist inside our deque list in order of the coordinates of the rotten orange we found from this minute
                xrotten, yrotten = d.popleft()
                #we want to step onto a new cell - REMEMBER THIS REQUIRES UNPACKING THE LIST OF LISTS IN DIRECTIONS!!!! XNEW BECOMES THE X COORDINATE OF THE PARTICULAR SUBLIST WE ARE ON (INDEX 0) WHILE YNEW BECOMES THE Y COORDINATE OF THE PARTICULAR SUBLIST WE ARE ON (INDEX 1)
                for xnew, ynew in directions:
                    #becomex, becomey is the new cell indicies that we are trying to rot in one of the 4 directions
                    becomex, becomey = xrotten + xnew, yrotten + ynew
                    
                    if becomex < 0 or becomex >= len(grid) or becomey < 0 or becomey >= len(grid[0]) or grid[becomex][becomey] != 1:
                        continue
                    #turning this new fresh orange cell into rotten
                    grid[becomex][becomey] = 2
                    #since this fresh orange became rotten, we have to add it's coordinate indicies to our deque for the next minute so this one can infect others
                    d.append([becomex, becomey])
                    freshcount -= 1
            #since our deque represents each passing minute, after we finish looping through each iteration of our deque, we increment the minutes that have passed
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#another:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #keep track of all rotten oranges from a particular timeslot starting from the 1st minute that elapses
        d = deque()
        minminutes = 0
        freshcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    #coordinates of rotten orange appended in order to unpack later
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #we can only turn freshoranges (1) into rottenoranges (2)
        while len(d) > 0 and freshcount > 0:
            for i in range(len(d)):
                xrotten, yrotten = d.popleft()
                for xstepon, ystepon in directions:
                    xdestroy, ydestroy = xrotten + xstepon, yrotten + ystepon
                    #now, we have to boundary check the new cell we are trying to rot and make sure it's a fresh orange
                    if xdestroy < 0 or xdestroy >= len(grid) or ydestroy < 0 or ydestroy >= len(grid[0]) or grid[xdestroy][ydestroy] != 1:
                        continue
                    grid[xdestroy][ydestroy] = 2
                    freshcount -= 1
                    #coordinates that will spread again later
                    d.append([xdestroy, ydestroy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1

#1/21/24 practice refresher:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #used to store rotten oranges from each particular timeslot
        d = deque()
        #return this at the end
        minminutes = 0
        #if this is still 0 by the end, then it's still possible to return minminutes - so minminutes is the independent variable
        freshcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                #if, in our cell, we are seeing a rotten orange, then add it's indicies/cell coordinates to the deque in order as a list with 2 elements in it
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        #now that we have all of our rotten and fresh oranges from the 1st minute, it's time to spread the rot in all 4 directions to fresh oranges that are 4 directionally adjacent to a rotten orange
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while len(d) > 0 and freshcount > 0:
            for i in range(len(d)):
                #unpacking from our list with 2 elements added earlier
                carrierx, carriery = d.popleft()
                for xchange, ychange in directions:
                    xmutate, ymutate = carrierx + xchange, carriery + ychange
                    if xmutate < 0 or xmutate >= len(grid) or ymutate < 0 or ymutate >= len(grid[0]) or grid[xmutate][ymutate] != 1:
                        continue
                    #if our new cell is in boundaries and is a fresh orange, we can rot it by turning that cell's 1 into a 2
                    grid[xmutate][ymutate] = 2
                    #we have to reflect the change in the independant variable, freshcount
                    freshcount -= 1
                    #this new carrier can be a carrier for other oranges later, so add this new carrier's indicies / cell coordinates to the deque in the form of a list with 2 elements so it can be unpacked later on
                    d.append([xmutate, ymutate])
            #since our deque represents one full minute, increment minminutes by 1
            minminutes += 1
        return minminutes if freshcount == 0 else -1



#1/28/24 review:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        d = deque()
        minminutes = 0
        freshcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while len(d) > 0 and freshcount > 0:
            for i in range(len(d)):
                xrotten, yrotten = d.popleft()
                for xnew, ynew in directions:
                    xdestroy, ydestroy = xrotten + xnew, yrotten + ynew
                    if xdestroy < 0 or xdestroy >= len(grid) or ydestroy < 0 or ydestroy >= len(grid[0]) or grid[xdestroy][ydestroy] != 1:
                        continue
                    grid[xdestroy][ydestroy] = 2
                    freshcount -= 1
                    d.append([xdestroy, ydestroy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#2/1/24 review:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #contains the coordinates as lists for all rotten oranges from time 0 for each minute of time that passes
        d = deque()
        minminutes = 0
        freshcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        #we want to simulate the spread in all 4 directions
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #we can only rot fresh oranges into rotting oranges
        while len(d) > 0 and freshcount > 0:
            #each unit of time has this many iterations beacuse those were all the bad oranges from the previous minute
            for i in range(len(d)):
                rottenx, rotteny = d.popleft()
                for xnew, ynew in directions:
                    destroyx, destroyy = rottenx + xnew, rotteny + ynew
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    d.append([destroyx, destroyy])
                    freshcount -= 1
            minminutes += 1
        return minminutes if freshcount == 0 else -1
        
#2/4/24 refresher:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque()
        minminutes = 0
        freshcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d and freshcount > 0:
            for i in range(len(d)):
                rottenx, rotteny = d.popleft()
                for xnew, ynew in directions:
                    destroyx, destroyy = rottenx + xnew, rotteny + ynew
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    d.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1
            

#2/12/24:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #each cell has either a 0 or 1 or 2
        #stores all rotten oranges from the 1st minute
        d = deque()
        minminutes, freshcount = 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else: #has to be an empty cell or 0
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d and freshcount > 0:
            #iterations from each minute
            for i in range(len(d)):
                #removing from beginning of list and unpacking the [r, c] values you appended 
                rottenx, rotteny = d.popleft()
                for xnew, ynew in directions:
                    destroyx, destroyy = rottenx + xnew, rotteny + ynew
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    d.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1

#this works too:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #each cell has either a 0 or 1 or 2
        #stores all rotten oranges from the 1st minute
        d = deque()
        minminutes, freshcount = 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.appendleft([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else: #has to be an empty cell or 0
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d and freshcount > 0:
            #iterations from each minute
            for i in range(len(d)):
                #removing from beginning of list and unpacking the [r, c] values you appended 
                rottenx, rotteny = d.pop()
                for xnew, ynew in directions:
                    destroyx, destroyy = rottenx + xnew, rotteny + ynew
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    d.appendleft([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1

#so basically as long as we use pop and appendleft or append and popleft(), we're good, so this problem requires 1st in 1st out, not 1st in last out
#Processing oranges based on when they became rotten ensures that you're considering the progression of time correctly. This approach mimics the real-world scenario where the rot spreads gradually from one orange to another.
#LIFO causes some oranges to take longer to rot than others

#2/18/24:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #stores coordinates of all rotten oranges from the minute we are on starting from 0 and will be unpacked later
        d = deque()
        minminutes, freshcount = 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2: #found a rotten orange
                    d.append([r, c])
                elif grid[r][c] == 1: #we don't care about the coordinates of fresh - we just increment freshcount - this is because, if we eliminate all rotten orange coordinates and empty cells, we are left with nothing but cells with fresh
                    freshcount += 1
                else: #empty cell - we don't care about
                    continue
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while d and freshcount > 0: #only can turn fresh oranges into rotten
            for i in range(len(d)):
                rottenx, rotteny = d.popleft() #BFS = FIFO
                for newx, newy in directions:
                    destroyx, destroyy = rottenx + newx, rotteny + newy
                    #we are trying to step onto a cell that is out of bounds of the grid or is not a fresh orange
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    #rot the fresh orange
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    #now becomes a carrier in future iterations
                    d.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1
    

#2/22/24:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minminutes = 0
        freshcount = 0
        #stores all rotten orange coordinates from time 0
        d = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d and freshcount > 0:
            for i in range(len(d)):
                rottenx, rotteny = d.popleft()
                for newx, newy in directions:
                    destroyx, destroyy = rottenx + newx, rotteny + newy
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    d.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#3/1/24:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #stores coordinates of all rotten oranges from each 1 unit of time
        d = deque()
        minminutes = 0
        freshcount = 0 #no cell has a freshorange means when freshcount equals 0 in the end
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1 #we have to track each fresh orange we find
                else: #0 / empty dosen't matter
                    continue
        #simulate each minute spread
        #since we want to spread adjacently in all 4 directions, we can use tuple unpacking breadth first search
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #each minute, any fresh orange adjacent to a rotten orange becomes rotten means we can only rot a 2 to a 1
        while d and freshcount > 0:
            for i in range(len(d)):
                rottenx, rotteny = d.popleft() #append popleft is BFS aka care about distance not direction
                for xnew, ynew in directions: #unpacking in 4 directions means adjacent
                    destroyx, destroyy = rottenx + xnew, rotteny + ynew #this is the new cell we want to rot, so we have to check if it's inbounds of our list of lists and also that it contains a 1, not a 0
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue #if we are out of bounds or aren't seeing a cell with a 1, continue 
                    #we are in bounds and seeing a 1 in all other scenarios, so rot the orange
                    grid[destroyx][destroyy] = 2 #rot the 1 cell by turning it into 2, which also means we now have one less fresh orange and are one step closer to getting that freshcount to 0 as in the beginning
                    #since we now have one more rotten orange that can be a carrier for the future and one less fresh orange, we want to add this new rotten orange to the deque to spread in future minutes
                    d.append([destroyx, destroyy]) # we want the coordinates of the rotten orange in our list of lists, just like the beginning format
            #the for loop only saw the original length of our deque representing the current minute
                    freshcount -= 1
            minminutes += 1
        #we use the deque to say if there are any rotten oranges left at all meaning more sick children in future
        return minminutes if freshcount == 0 else -1



#3/4/24:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque()
        minminutes = 0
        freshcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                elif grid[r][c] == 0:
                    continue
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while d and freshcount > 0:
            for i in range(len(d)):
                rx, ry = d.popleft() #note that d.pop() makes things wrong here! grid = [[2,1,1],[1,1,0],[0,1,1]] would return 3 instead of 4!
                for newx, newy in directions:
                    dx, dy = rx + newx, ry + newy
                    if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or grid[dx][dy] != 1:
                        continue
                    grid[dx][dy] = 2
                    d.append([dx, dy])
                    freshcount -= 1
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#3/13/24:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minminutes, freshcount = 0, 0
        d = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else: #seeing a 0
                    continue
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while d and freshcount > 0:
            for i in range(len(d)):
                rottenx, rotteny = d.popleft()
                for newx, newy in directions:
                    destroyx, destroyy = rottenx + newx, rotteny + newy
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    d.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#3/20/24:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque() 
        freshcount, minminutes = 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue 
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while d and freshcount > 0:
            for i in range(len(d)): #each minute
                rottenx, rotteny = d.popleft()
                for newx, newy in directions:
                    destroyx, destroyy = rottenx + newx, rotteny + newy
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    d.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1

#3/30/24:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque() #rotten oranges from a particular minute
        minminutes, freshcount = 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while d and freshcount > 0:
            for i in range(len(d)):
                rottenx, rotteny = d.popleft()
                for destroyx, destroyy in directions:
                    newx, newy = rottenx + destroyx, rotteny + destroyy
                    if newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[0]) or grid[newx][newy] != 1:
                        continue
                    grid[newx][newy] = 2
                    d.append([newx, newy])
                    freshcount -= 1
            minminutes += 1
        return minminutes if freshcount == 0 else -1

#4/14/24:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minminutes = 0
        freshcount = 0
        d = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while d and freshcount > 0:
            for i in range(len(d)):
                rottenx, rotteny = d.popleft()
                for newx, newy in directions:
                    destroyx, destroyy = rottenx + newx, rotteny + newy
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    d.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#5/4/24 refresher:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque()
        minminutes = 0
        freshcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while d and freshcount > 0:
            for i in range(len(d)):
                rx, ry = d.popleft() #we are doing BFS here
                for nx, ny in directions:
                    destroyx, destroyy = rx + nx, ry + ny
                    if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
                        continue
                    grid[destroyx][destroyy] = 2
                    freshcount -= 1
                    d.append([destroyx, destroyy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#5/24/24 practice:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque() #stores coordinates of all rotten oranges from time 0
        freshcount = 0
        minminutes = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2: 
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while d and freshcount > 0:
            for i in range(len(d)):
                rottenx, rotteny = d.popleft()
                for newx, newy in directions:
                    onex, oney = rottenx + newx, rotteny + newy
                    #we can only turn fresh oranges into rotten
                    if onex < 0 or onex >= len(grid) or oney < 0 or oney >= len(grid[0]) or grid[onex][oney] != 1:
                        continue
                    grid[onex][oney] = 2 #rotting the tile
                    freshcount -= 1
                    d.append([onex, oney])
            minminutes += 1
        return minminutes if freshcount == 0 else -1

#6/20/24 review:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque() 
        freshcount = 0
        minminutes = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    d.append([r, c])
                elif grid[r][c] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while d and freshcount > 0:
            for i in range(len(d)):
                zx, zy = d.popleft()
                for dx, dy in directions:
                    tx, ty = zx + dx, zy + dy
                    if tx < 0 or tx >= len(grid) or ty < 0 or ty >= len(grid[0]) or grid[tx][ty] != 1:
                        continue
                    grid[tx][ty] = 2
                    freshcount -= 1
                    d.append([tx, ty])
            minminutes += 1
        return minminutes if freshcount == 0 else -1


#8/18/24 refresher (solved on 1st try):

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque() #stores coordinates of all rotten oranges
        minminutes = 0
        freshcount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    d.append([i, j])
                elif grid[i][j] == 1:
                    freshcount += 1
                else:
                    continue
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while d and freshcount > 0:
            for i in range(len(d)):
                rx, ry = d.popleft() #perform bfs 
                for nx, ny in directions:
                    dx, dy = rx + nx, ry + ny
                    if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or grid[dx][dy] != 1:
                        continue
                    grid[dx][dy] = 2
                    freshcount -= 1
                    d.append([dx, dy])
            minminutes += 1
        return minminutes if freshcount == 0 else -1

#9/8/24 review from grokking course:

from collections import deque
def min_minutes_to_rot(grid):
    minminutes, freshcount = 0, 0
    d = deque()
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 2:
          d.append([i, j])
        elif grid[i][j] == 1:
          freshcount += 1 
        else:
          continue
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while d and freshcount > 0:
      for i in range(len(d)):
        zx, zy = d.popleft()
        for nx, ny in directions:
          destroyx, destroyy = zx + nx, zy + ny
          if destroyx < 0 or destroyx >= len(grid) or destroyy < 0 or destroyy >= len(grid[0]) or grid[destroyx][destroyy] != 1:
            continue
          grid[destroyx][destroyy] = 2
          freshcount -= 1 
          d.append([destroyx, destroyy])
      minminutes += 1 
    return minminutes if freshcount == 0 else -1
