
#medium
#52% ac

#A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

#Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

#You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

#You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

#  Input: mat = [[1,4],[3,2]]
#Output: [0,1]
#Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.


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



#a better solution:

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        print(n)
        #note n here is the number of columns
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            cur_max, left = 0, False
            for i in range(m):
                if i > 0 and mat[i-1][mid] >= mat[i][mid]:
                    continue
                if i+1 < m and mat[i+1][mid] >= mat[i][mid]:   
                    continue
                if mid+1 < n and mat[i][mid+1] >= mat[i][mid]:   
                    cur_max, left = mat[i][mid], not mat[i][mid] > cur_max
                    continue
                if mid > 0 and mat[i][mid-1] >= mat[i][mid]:   
                    cur_max, left = mat[i][mid], mat[i][mid] > cur_max
                    continue
                return [i, mid]
            if left:
                r = mid-1
            else:
                l = mid+1
        return []
