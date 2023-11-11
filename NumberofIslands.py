

#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



#Python3 solution:



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(down, right, grid):
            if down < 0 or down >= len(grid) or right < 0 or right >= len(grid[0]) or grid[down][right] == '0': #skipping this block if line 24 equals 1 on the 1st call iteration
                return #out of bounds, so return out of the function
            grid[down][right] = '0' #sinking the 1 into a 0 so we don't double count it - we go here from line 24
            dfs(down + 1, right, grid) #and then we call dfs again to go down one tile and then we boundary check this new tile in line 14 
            dfs(down - 1, right, grid)
            dfs(down, right + 1, grid)
            dfs(down, right - 1, grid)
        count = 0 #we will return this at the end
        for down in range(len(grid)): #right - rows - flipping the ordering of rows vs. columns also works!
            for right in range(len(grid[0])): #down - columns
                if grid[down][right] == '1': #we found a 1, so we found atleast 1 island - if grid[I[j] == 1, then we increment count, and then we call dfs, and we skip the if block and directly call grid[I][j] = '0'? and then we execute dfs(I + 1, j) - so we are boundary checking dfs(I + 1, j) aka the new tile, not the old tile with 1 we already visited
                    count += 1
                    dfs(down, right, grid) #we must do a boundary check before sinking that 1 into a 0!!!!!!
        return count 

#sequence 22 > 21 (this is due to backtracking as we need to check all adjacent cells where it left off)
#sequence 21 > 15 > 16 > 18 > 19 > 15 > 16 > 17 > 19 (we have to start over from the 1st recursive call all over again because we have to explore all possible directions for that one direction!!!! islands can be connected to other islands!)

#sequence 16 > 18 > 19 > 15 (this just means that the direction we are going is fine and is part of the same island, so sink the 1 tile we found to 0 and keep going in the same direction)
#sequence 19 > 15 > 16 > 17 > 20 (this means the tile we visited was either out of bounds or was already visited, so move in another direction to find more 1s to sink IN THE SAME ISLAND)
#sequence 22 > 15 > 16 > 17 > 22 > 25 (this means we've exhausted all directions and are looking for a new island)

#after a DFS call completes, 
#the algorithm returns to the for loop to continue scanning the grid for any other '1's that might represent a different, unvisited island. 
#The DFS call is responsible for an entire island, and the loops are responsible for ensuring every cell in the grid is checked. - THIS IS THE KEY - and, remember that whether rows or columns loop comes first dosen't matter, so we could be returning to j loop or i loop if you wanted to flip the order of loops

#the 1st time this if statement in line 14 is evalvulated, it will never execute the inner block because it came from the if statement where grid[I]jj] was equal to 1 from line 24. It's only after one of the recursive calls below executes that this if block can become true?
                #return
           # grid[i][j] = '0'
            #dfs(i + 1, j, grid) #recursive calls below refers to one of these 4 in lines 17 - 20


#if you wanted to flip the order of loops, your solution would be: 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(down, right, grid):
            if down < 0 or down >= len(grid) or right < 0 or right >= len(grid[0]) or grid[down][right] == '0':
                return
            grid[down][right] = '0'
            dfs(down + 1, right, grid)
            dfs(down - 1, right, grid)
            dfs(down, right + 1, grid)
            dfs(down, right - 1, grid)
        
        count = 0
        for right in range(len(grid[0])): # Iterate over columns first
            for down in range(len(grid)): # Then iterate over rows
                if grid[down][right] == '1': #the dfs function looks for all adjacent 1s aka 1s that comprise of the same island while the loops look for non adjacent 1s that would signal a new island and would increase count
                    count += 1
                    dfs(down, right, grid)
        return count
