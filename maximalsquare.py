#Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 4


#python3 solution:

#this solution involves dynamic programming

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        sidelength = 0
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
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
