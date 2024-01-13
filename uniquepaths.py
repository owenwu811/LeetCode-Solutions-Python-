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
       
