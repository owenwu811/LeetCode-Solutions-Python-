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


#1/15/24 refresher:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       #we want the frequency of unique ways to get from every cell to the bottom right, which will include lots of repeated work
       #one because the right and bottom borders will be filled with 1s to build off since we are tilting pascal's triangle from the bottom left in the left direction and building to the top right from the bottom level up
        lowerlevel = [1] * n
        for down in range(m - 1):
            upplevel = [1] * n
            for right in range(n - 2, -1, -1):
                upplevel[right] = upplevel[right + 1] + lowerlevel[right]
            lowerlevel = upplevel
        return lowerlevel[0]


#1/16/24 refresher:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       #we want the number of unique ways from each cell to reach the bottom right corner. we know this anwser will be 1 for the right and bottom edge because you can only go in one direction, and moving 3 cells in the same direction still only counts as one way
        #since there is always one way to get to the bottom right hand cell, we start every cell as [1] instead of [0] to represent the number of ways 
        lowestrow = [1] * n
        #we can move down twice regardless of the value m is
        for down in range(m - 1):
            result = [1] * n
            for right in range(n - 2, -1, -1):
                result[right] = result[right + 1] + lowestrow[right]
            lowestrow = result
        return lowestrow[0]



#again

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       #we can fill the border of the bottom and right cells with 1 way since we know that one direction counts as 1 way: you can only move down OR right, so regardless if you are in the top right or middle right, there is only 1 unique path to get to the bottom right cell
       #if the block is 7 cells wide, we fill the bottom border with 7 1s first since buildoff initially represents the bottom row that we will build upwards from 
        buildoff = [1] * n
        for down in range(m - 1):
            result = [1] * n
            #if n = 7, n starts at 5 and goes to including 0
            for right in range(n - 2, -1, -1):
                result[right] = result[right + 1] + buildoff[right]
            buildoff = result
        return buildoff[0]



#again - 1/17/24

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #we will the right and bottom borders with 1 since it represents 1 direction aka 1 way aka 1 unique path to go from the current cell to the bottom right hand cell
        #buildoff starts to represent the bottom wide row
        buildoff = [1] * n
        #if m = 3 aka 3 rows, then down would move 2 times - 0 and 1
        for down in range(m - 1):
            #result will be the same length as the buildoff row, but result will represent the one row above the bottom most row (buildoff)
            result = [1] * n
            #n = 7, so 6 steps to get from left to right, so 0 through 5
            for right in range(n - 2, -1, -1):
                #pascal's triangle titled
                #right of current cell level plus cell value right below current cell - we are on the 2nd to lowest level row
                result[right] = result[right + 1] + buildoff[right]
            buildoff = result
        return buildoff[0]

#1/18/24 refresher:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #we want the number of unique ways from each cell to the bottom right cell, and note that the right and bottom borders will be filled with 1s first because there is only one way from anywhere on the right border to the bottom right cell (go down) regardless if we move down 1 block or 2 blocks, it still counts as one unique way / path - same goes for the bottom, so we will initially start with an array of 1s filling an array the length of the bottom row and build upwards from right to left 
        buildoff = [1] * n
        #if we have three rows, then we can only move down twice, so down = 0, 1
        for down in range(m - 1):
            #finalresult is one row above the bottom most row and will be build by tilting pascal's triangle towards the left
            finalresult = [1] * n
            for right in range(n - 2, -1, -1):
                finalresult[right] = finalresult[right + 1] + buildoff[right]
            buildoff = finalresult
        return buildoff[0]


#1/24/24 refresher:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #we want the number of unique ways to get from the current cell to the bottom right cell, so we know the bottom and right borders will be filled with 1s because you are only moving in 1 direction
        #we will build up from the bottom row, which is buildoff, so result will be the row above buildoff
        buildoff = [1] * n
        #iterations for rows
        for down in range(m - 1):
            result = [1] * n
            #iterations for columns
            for right in range(n - 2, -1, -1):
                #pascal's triangle tilted to the left
                result[right] = result[right + 1] + buildoff[right]
            buildoff = result
        #buildoff will be the top left corner value, which will be the number of unique ways to go from the top left cell to the bottom right cell 
        return buildoff[0]




#1/29/24 refresher:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #the right and bottom borders will be filled with 1s since they all go in one direction aka one path aka one way to the bottom right cell, and we want the number of unique ways 
        #n represents columns while m represents rows
        buildoff = [1] * n
        for down in range(m - 1):
            #result is above buildoff
            result = [1] * n
            for right in range(n - 2, -1, -1):
                result[right] = result[right + 1] + buildoff[right]
            buildoff = result
        return buildoff[0]


#2/4/24 practice:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #a path is one direction regardless of how far, so we fill the right and bottom borders with 1
        #buildoff array represents the bottom row
        buildoff = [1] * n
        #vertical direction
        for down in range(m - 1):
            #result represents the 2nd to last row
            result = [1] * n
            #horizontal direction
            for right in range(n - 2, -1, -1):
                #pascal's triangle tilted to the left
                result[right] = result[right + 1] + buildoff[right]
            buildoff = result
        #top right corner 
        return buildoff[0]


#2/14/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #unique path means one way from the current cell to the bottom right corner
        buildoff = [1] * n
        for down in range(m - 1):
            above = [1] * n
            for right in range(n - 2, -1, -1):
                above[right] = above[right + 1] + buildoff[right]
            buildoff = above
        return buildoff[0]


#2/22/24: (missed - needs churning!)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        buildoff = [1] * n
        for down in range(m - 1):
            current = [1] * n
            for right in range(n - 2, -1, -1): #5, 4, 3, 2, 1, 0 (inclusive) 
                current[right] = current[right + 1] + buildoff[right]
            buildoff = current
        return buildoff[0]

#2/22/24 - again:

#m = 3, n = 7 (test case)

#[1 1 1 1 1 1 1] first
# 0 1 2 3 4 5 6 


#[1 1 1 1 1 (1) 1] above - (1) + (1) = 2, but (1) starts at index 5, so (7 - 2) = 5
# 0 1 2 3 4 5 6 - notice 5, 4, 3, 2, 1, 0 (inclusive)

#[7 6 5 4 3 2 (1)] above, first (first = above)
# 0 1 2 3 4 5 6

#we do go all the way to the end, so we are using (1) + (6) = 7:
#[(1) 1 1 1 1 1 1]
#  0  1 2 3 4 5 6

#[7 (6) 5 4 3 2 1] 
# 0  1 2 3 4 5 6


#[28 21 15 10 6 3 1] above, first (first = above)
# 0  1  2  3  4 5 6

#first[0] = 28

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        first = [1] * n #so if n = 7, then you would have [1] [1] [1] [1] [1] [1] [1] from 0 through 6 inclusive 
        for down in range(m - 1):
            above = [1] * n #this resets every bar level above we build back to [1] [1] [1] [1] [1] [1] [1] from 0 through 6 inclusive, just like first
            for right in range(n - 2, -1, -1): #right starts off at 5 if n = 7
                above[right] = above[right + 1] + first[right] #[7, 6, 5, 4, 3, 2, 1], [28, 21, 15, 10, 6, 3, 1] 
            first = above
        return first[0] #28 


#2/23/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        first = [1] * n
        for down in range(m - 1): #columns
            above = [1] * n
            for right in range(n - 2, -1, -1):
                above[right] = above[right + 1] + first[right]
            first = above
        return first[0]


#2/24/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        first = [1] * n
        for down in range(m - 1): #rows
            above = first #also works 
            for right in range(n - 2, -1, -1): #columns 
                above[right] = above[right + 1] + first[right]
            first = above
        return first[0]

#2/25/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #a path means one direction, so the bottom and right border of our result will be filled with 1s to represent 1 way/direction to reach the bottom right corner from the rightmost or bottommost row
        #we will start by building the bottom up to the top, so we will work from bottom right to top left and return our top right to recompute results in between
        first = [1] * n #n represents the number of columns
        #we can only move down or right from the top left corner 
        for down in range(m - 1): #number of rows
            buildoff = first #every row has the same number of columns - every row has includes a column
            for right in range(n - 2, -1, -1): #using indexes, if n = 7, then it takes 5 hops to reach the left side from the right side if we move left by one place at each iteration
                buildoff[right] = buildoff[right + 1] + first[right] #pascal's triangle titled to the left is the addition of the current level plus one to the right plus down one level
            first = buildoff
        return first[0]

#3/1/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #can move down or right - can come from above or to the left
        #unique paths to go from top left to bottom right
        first = [1] * n #bottom row will be filled with 1s since left is only one unique path
        for down in range(m - 1): #range(2) = 0, 1
            above = [1] * n
            for right in range(n - 2, -1, -1): #5, 4, 3, 2, 1, 0 (all inclusive)
                above[right] = above[right + 1] + first[right]
            first = above
        return first[0]

#3/3/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #we can move down or right meaning coming from left or above
        #we fill the bottom and right borders with 1s because there is one way - down or right
        bottom = [1] * n 
        for down in range(m - 1): #0 1 is m = 3
            above = bottom
            for right in range(n - 2, -1, -1): #543210 inclusive if n = 7 
                above[right] = above[right + 1] + bottom[right]
            bottom = above
        return bottom[0]

#3/5/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #unique ways robot can take to reach bottom right corner starting from top left corner
        #move right or down means coming from top or from the left
        first = [1] * n #one way - to the right
        for down in range(m - 1):
            above = [1] * n 
            for right in range(n - 2, -1, -1):
                above[right] = above[right + 1] + first[right]
            first = above
        return first[0]
 

#3/9/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bottom = [1] * n
        for down in range(m - 1):
            above = [1] * n
            for right in range(n - 2, -1, -1):
                above[right] = above[right + 1] + bottom[right]
            bottom = above
        return bottom[0]

#3/13/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        first = [1] * n
        for down in range(m - 1):
            above = [1] * n
            for right in range(n - 2, -1, -1): #543210 inclusive
                #pascal's triangle tilted left
                above[right] = above[right + 1] + first[right] #first[right] will eventually become first[0]
            first = above
        return first[0]
            

#3/25/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #unique ways to go from top left to bottom right
        first = [1] * n
        for down in range(m - 1):
            buildoff = [1] * n
            for right in range(n - 2, -1, -1):
                buildoff[right] = buildoff[right + 1] + first[right]
            first = buildoff
        return first[0]

#4/7/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        first = [1] * n
        for down in range(m - 1):
            above = [1] * n
            for right in range(n - 2, -1, -1):
                above[right] = above[right + 1] + first[right]
            first = above
        return first[0]


#4/10/24:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        first = [1] * n
        for down in range(m - 1):
            buildoff = [1] * n
            for right in range(n - 2, -1, -1): 
                buildoff[right] = buildoff[right + 1] + first[right]
            first = buildoff
        return first[0]

#5/6/24 refresher:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        buildoff = [1] * n # 1 1 1 1 1 1 1
        for first in range(m - 1): #012
            above = [1] * n # 1 1 1 1 1 1 1
            for second in range(n - 2, -1, -1):
                above[second] = above[second + 1] + buildoff[second]
            buildoff = above
        return buildoff[0]



