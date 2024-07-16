#Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 4


#python3 solution:

#this solution involves dynamic programming

#(i, j) will be the bottom right corner of the square 

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        sidelength = 0
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n): #sidelength = max(sidelength, dp[r][c]) line comes back here, so column increments meaning ROW STAYS SAME WHILE WE MOVE RIGHT BY ONE CELL
                if matrix[r][c] == "1":
                    #if r == 0 or c == 0 because rectangles do not count as squares!
                    #if r == 0 or c == 0 is FALSE, we go to the else block because we know we can actually form an entire square bigger than 1
                    if r == 0 or c == 0: #reason we do this check is is so that if the statement is not true, then we know we can actually form an entire square with more than one element and can to the to the top to the left to the upper left check with the line dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                        dp[r][c] = 1 #if this is True, we go to sidelength = max(sidelength, dp[r][c]) line and then back to for c in range(n): line
                    else:
                        #we use min() because if even one side (to the left or above or above left) is a 0 instead of a 1, it means the current square cannot be of size 4, so if one out of the 4 squares is a 0, it limits the size of the new square that can be formed at (i, j) because all three squares must contribute equally to form a larger square
                        #we cannot do dp[j-1][i-1] instead of dp[i-1][j-1]
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1 #the reason we do a + 1 at the end is because The +1 accounts for the current cell itself being part of the square.
                    sidelength = max(sidelength, dp[r][c])
        return sidelength * sidelength #the reason we multiply sidelength by itself in the end is because sidelength is the side length of the largest square, and area of a square = sidelength * sidelength


#The reason for the check if i == 0 or j == 0: is to handle the edge cases where the current cell is in the first row or first column. If the cell is in the first row or first column, it cannot form a square larger than 1x1 because there are no cells above or to the left of it. This check ensures that the dp array is correctly initialized for these edge cases.


#for test case:
#matrix = [
#    ['1', '0', '1', '0', '0'],
#    ['1', '0', '1', '1', '1'],
#    ['1', '1', '1', '1', '1'],
#    ['1', '0', '0', '1', '0']
#]

#dp originally becomes the below from the line: dp = [[0] * n for _ in range(m)]:

#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]

#6/1/24 practice:

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        sidelength = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                    sidelength = max(sidelength, dp[r][c])

        return sidelength * sidelength

#6/2/24 review:

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        inputlen = len(matrix)
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        sidelength = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    sidelength = max(sidelength, dp[i][j])
        return sidelength * sidelength

#6/7/24 review (missed):

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        sidelength = 0
        dp = [[0] * cols for i in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1 #1 can't form a square that is bigger than 1 of size because we are on a border
                    else:
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                    sidelength = max(sidelength, dp[r][c])
        return sidelength * sidelength

#6/8/24 review:

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        sidelength = 0
        dp = [[0] * cols for i in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                    sidelength = max(sidelength, dp[r][c])
        return sidelength * sidelength

#6/13/24 review:

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for n in range(rows)]
        sidelength = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                sidelength = max(sidelength, dp[r][c])

        return sidelength * sidelength


#6/18/24 review:

#we go from top left cell to right and then one row down and repeat (from left to right)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for i in range(m)]
        sidelength = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        #we know our current cell is a 0, so we know your entire square can't be of size 4 but only 1 at max, so we get 0 + 1 = 1 as sidelength
                        #we don't include dp[r][c] in the min() because our dp looks like 1 1 meaning we haven't even updated the current cell yet!
                        #                                                                 1 0
                        #with 0 being our current dp[r][c], and since we already checked that matrix[r][c] is indeed "1", then we need to minimum of top, to the left, and top left + 1
                        #so we will get 1 1 
                        #               1 2
                        #and sidelength gets updated to 2 because min(1, 1, 1) + 1 = 2 since we found a valid square length 2 width 2
                        #the reason we use min() and not max() is because current input square is : 0 1
                        #                                                                           0 1 (with bottom left being current matrix[r][c])
                        #and the same area in our dp is 0 1
                        #                               0 0 #(with bottom left being current dp[r][c])

                        #so since our input square has atleast 1 zero in it, the biggest size it could be is 1, so min(1, 0, 0) + 1  = 0 + 1 = 1 (if we use min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1)) ordering
                        #if we used max() instead of min(), even if we see a square with atleast a 0 in it of length 2 by 2, we would still count the sidelength as 2 incorrectly
                        #the inuition behind using min here even though the question asks for max is because is a 2 x 2 square has even 1 zero, the max area it could be is 1 (0 + 1) = 1 aka find the even one zero in the 2 x 2 square using min(1, 1, 0) + 1 = 1
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                    sidelength = max(sidelength, dp[r][c])
        return sidelength * sidelength

#the scenario in which sidelength actually becomes 1 is if we see: 1 1
#                                                                  1 "1" (current matrix[r][c] from input)
#then we know min(1, 1, 1) + 1 = 2 (only in perfect scenario)

#this is because if input is 1 1 
#                            0 1 (then the max area of the SQUARE can only be 1), so min(1, 0, 1) + 1 = 0 + 1 = 1
#if we get 1 1
#          1 "1" matrix[r][c] == "1" then we know that the if matrix[r][c] == "1": check already passed, so we are garunteed a sidelength of 2 now
