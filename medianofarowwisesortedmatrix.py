

#2387
#medium


#Given an m x n matrix grid containing an odd number of integers where each row is sorted in non-decreasing order, return the median of the matrix.

#You must solve the problem in less than O(m * n) time complexity.

 

#Example 1:

#Input: grid = [[1,1,2],[2,3,3],[1,3,4]]
#Output: 2
#Explanation: The elements of the matrix in sorted order are 1,1,1,2,2,3,3,3,4. The median is 2.
#Example 2:

#Input: grid = [[1,1,3,3,4]]
#Output: 3
#Explanation: The elements of the matrix in sorted order are 1,1,3,3,4. The median is 3.


#my own solution using python3:

class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        tmp = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tmp.append(grid[i][j])
        print(tmp)
        tmp.sort()
        l, r = 0, len(tmp) - 1
        if len(tmp) % 2 != 0:
            mid = (l + r) // 2
            return tmp[mid]
        else:
            mid = (l + r) // 2
            return tmp[mid]

