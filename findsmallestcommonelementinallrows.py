

#1198
#medium

#Given an m x n matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

#If there is no common element, return -1.

 

#Example 1:

#Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
#Output: 5
#Example 2:

#Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
#Output: 2



#my own solution using python3:

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        d = dict()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] not in d:
                    d[mat[i][j]] = []
                d[mat[i][j]].append(i)
        print(d)
        res = float('inf')
        for k in d:
            if len(d[k]) == len(mat):
                res = min(res, k)
        if res == float('inf'):
            return -1
        return res
                
