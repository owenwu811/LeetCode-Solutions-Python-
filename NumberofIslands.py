

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

#sequence 22 > 21 (this is due to backtracking as we need to check all adjacent cells where it left off) - This backtracking ensures that every part of an island (group of connected '1's) is visited and marked, and no potential connections are missed. Once an island is fully explored and marked, the algorithm continues to search for other islands in the grid.
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
            grid[down][right] = '0' #the 0 check here is to be sure that either we haven't revisited a cell because the previous cell was already flipped from 1 to 0 or we are not stepping onto water - 0 means it can't be part of the same island in either one of these two scenarios 
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



#time, space, and memory complexities are the same whether we iterate over rows first or columns first 
#Time Complexity
#The time complexity of this algorithm is primarily determined by the number of cells in the grid and the number of times each cell is visited. Let's assume the grid is of size m x n, where m is the number of rows and n is the number of columns.

#Outer Loops: The outer for loops iterate through each cell of the grid once. Therefore, the total number of iterations here is m * n.
#DFS Calls: For each cell that is a '1', a DFS (Depth-First Search) is performed. In the worst case, DFS can visit each cell in the grid once (if the entire grid is filled with '1's). However, each cell is visited only once across all DFS calls because the visited '1' cells are marked as '0', preventing revisits.
#Combining these factors, the worst-case time complexity is O(m * n).

#Space Complexity
#The space complexity of the algorithm is determined by the maximum size of the call stack during the recursive DFS calls.

#Call Stack in DFS: In the worst case, where the grid is filled with '1's, the DFS could potentially go as deep as the total number of cells in the grid before backtracking. However, this is a highly unlikely scenario since it would require a pathological case of a grid where DFS traverses the entire grid in a snake-like pattern. A more realistic worst-case scenario would involve a DFS depth equivalent to the maximum of m and n.
#Therefore, the worst-case space complexity is O(max(m, n)).

#Memory Complexity
#In terms of memory usage, the algorithm modifies the input grid in place and does not use any additional significant memory that scales with the size of the input. Thus, the memory complexity is essentially the same as the space complexity, O(max(m, n)).

#Summary
#Time Complexity: O(m * n)
#Space Complexity: O(max(m, n))
#Memory Complexity: O(max(m, n))


#11/24 refresher:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:  
        def search(rows, columns, grid):
            if rows < 0 or rows >= len(grid) or columns < 0 or columns >= len(grid[0]) or grid[rows][columns] == '0': #if we are on water, then return. If 1, then keep going to the next tile because it's part of the same island. 
                return
            grid[rows][columns] = '0' #set any 1s to 0 so we don't double count - the if block will always be false, and this line will always execute the first time this recursive function is called
            search(rows + 1, columns, grid)
            search(rows - 1, columns, grid)
            search(rows, columns + 1, grid)
            search(rows, columns - 1, grid)
        count = 0
        for rows in range(len(grid)):
            for columns in range(len(grid[0])): #cannot be grid[1] because it would fail test case [["1"]], so grid[0] and grid[-1] work!!!!!!!!!!!!!!!!!
                if grid[rows][columns] == '1':
                    count += 1
                    search(rows, columns, grid)
        return count

#12/17/23 refresher:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        def f(row, column, grid):
            #the grid[row][column] checks if we are on water 
            #len(grid[-1]) works for test case grid = [["1"]]
            if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[-1]) or grid[row][column] == "0":
                return
            grid[row][column] = "0" #will always execute on the 1st turn. this is for making sure we don't double count islands since any 1s in 4 directions are part of the same island, so flip them to 0
            f(row + 1, column, grid)
            f(row - 1, column, grid)
            f(row, column + 1, grid)
            f(row, column - 1, grid)
        res = 0
        for row in range(len(grid)):
            for column in range(len(grid[-1])): #works for test case grid = [["1"]]
                if grid[row][column] == '1':
                    res += 1
                    f(row, column, grid)
        return res



#1/6/24 refresher:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, row, column):
            if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] == "0":
                return
            #we are only given 1s and 0s, so if the grid dosen't contain a string 0 and is in bounds, then it must be a 1 and is part of the same island, so turn that 1 into a 0 so we don't keep calling that 1 tile forever
            grid[row][column] = "0" #avoid infinite recursion
            dfs(grid, row + 1, column)
            dfs(grid, row - 1, column)
            dfs(grid, row, column + 1)
            dfs(grid, row, column - 1)



        res = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    res += 1
                    dfs(grid, row, column)
        return res


#1/14/24 refresher:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            #won't be true in 1st turn bc we already found start of island (a 1 string cell that is in bounds)
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c] = "0" #prevents infinite recursion
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        res = 0
        #vertical
        for r in range(len(grid)):
            #horizontal - wide 
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    res += 1
                    dfs(grid, r, c)
        return res


#1/21/24 refresher:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return
            #prevent infinite recursion while looking for parts of the same island
            grid[r][c] = "0"
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    res += 1
                    dfs(grid, r, c)
        return res


#1/24/24 refresher:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c): 
            #if we are out of bounds or see water, which won't be true the 1st time this conditional is evaluated, we return nothing back to the parent caller
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return
            #set it equal to 0 so we don't double count it and run into infinite recursion
            grid[r][c] = "0"
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(grid, r, c)
        return count

#1/28/24 review:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #grid is a list of list of strings with cell values of either "1" or "0" as string
        #any 1 we see, we know we can count that as 1 island, and since all the 1st adjacent to that 1 also count as the same island, we want to find them so we don't overcount islands, so we do that with this recursive call

        def dfs(grid, r, c):
            #this if block won't be true in the 1st turn that it executes since we already determined that atleast one island exists
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                #if we are out of bounds of the grid or find water, then we return nothing back to the parent function call that caused it
                return
            #we found another 1, so we have to set it to 0 so we don't double count it
            grid[r][c] = "0"
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)



        count = 0
        for r in range(len(grid)):
            #this is the width since we know that all lists of lists are of the same width
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(grid, r, c)
        return count
