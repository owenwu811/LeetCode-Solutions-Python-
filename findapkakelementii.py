
#1901
#medium
#52.5% acceptance rate


#A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

#Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

#You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

#You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.


#my own solution using python3:

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        maxmat = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                maxmat = max(maxmat, mat[i][j])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == maxmat:
                    return [i, j]
