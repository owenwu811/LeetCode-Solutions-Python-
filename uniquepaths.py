#There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

#Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

#The test cases are generated so that the answer will be less than or equal to 2 * 109.




#python3 solution:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #think about this like pascal's triangle tilted
        row = [1] * n
        #number of iterations for rows 
        for r in range(m - 1):
            #modified row
            newrow = [1] * n
            #number of iterations for columns - (n - 1)
            for column in range(n - 2, -1, -1):
                #pascal's triangle rule - build off of the first array called row
                newrow[column] = newrow[column + 1] + row[column]
            row = newrow
        return row[0]



#1/11/24 refresher:

buildoff = [1] * n
for row in range(m - 1):
    result = [1] * n
    for column in range(n - 2, -1, -1):
        result[column] = result[column + 1] + buildoff[column]
    buildoff = result
return buildoff[0]


#1/12/24 refresher:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        buildoff = [1] * n
        for rows in range(m - 1):
            res = [1] * n
            for column in range(n - 2, -1, -1):
                res[column] = res[column + 1] + buildoff[column]
            buildoff = res
        return buildoff[0]


#1/14/24 refresher:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        buildoff = [1] * n
        #down is an index
        for down in range(m - 1):
            new = [1] * n
            #we are trying to find the cell at [2, 6] in terms of lengths, which is [1, 5] in indexes, and we get this by adding the cell to the right at the current level plus the cell below at the same position - pascale's triangle tilted left
            for right in range(n - 2, -1, -1):
                new[right] = new[right + 1] + buildoff[right]
            buildoff = new
        return buildoff[0]

#1/14/24 refresher with better comments:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #unique paths means frequency of ways from every cell to the bottom right. if we only move down from the top cell to the bottom, it only counts as 1 way even though 2 arrows are required, but it only counts as 1 way / path because we are still going in the same direction - this is why the right and bottom most borders are filled with 1s - because only one direction or path from any cell in the bottom most or right most row to the bottom right cell
        #the bottom array filled with 1s initially
        buildoff = [1] * n
        #columns
        for down in range(m - 1):
            #the array right above the most bottom array 
            result = [1] * n
            #we have 7 cells wide, so since the rightmost cell is already filled with 1s, we don't care about the right most cell of the 2nd level we are trying to build, so 7 cells wide is through 0 1 2 3 4 5 6, but we are only going up through 0 1 2 3 4 5
            for right in range(n - 2, -1, -1):
                #result[5] = result[6] + buildoff[5]
                result[right] = result[right + 1] + buildoff[right]
            buildoff = result
        return buildoff[0]
