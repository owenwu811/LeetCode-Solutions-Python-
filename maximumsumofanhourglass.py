
#You are given an m x n integer matrix grid.

#Return the maximum sum of the elements of an hourglass.

#Note that an hourglass cannot be rotated and must be entirely contained within the matrix.


#Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
#Output: 30
#Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.


#my own solution using python3:

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        tmp = []
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                #print(r, c)
                startingr, startingc = r, c
                tmp.append([startingr, startingc])
        #print(tmp)
        for a, b in tmp:
            print(a + 2, b + 2)
            enda, endb = a + 2, b + 2
            cursum = 0
            carveout = 0
            for i in range(a, enda + 1):
                for j in range(b, endb + 1):
                    if i == a + 1 and j != b + 1:
                        carveout += grid[i][j]
                    cursum += grid[i][j]
            print(cursum)
            print(carveout)
            res = max(res, cursum - carveout)
        return res
