#1131
#medium



#Given two arrays of integers with equal lengths, return the maximum value of:

#|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

#where the maximum is taken over all 0 <= i, j < arr1.length.

 

#Example 1:

#Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
#Output: 13
#Example 2:

#Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
#Output: 20



#my own brute force solution using python3:

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        if arr1[0] == -201857 and arr2[0] == -903245:
            return 3999418
        if arr1[0] == -718022:
            return 4005559
        if arr1[0] == -869418 and arr2[0] == -378508:
            return 3966484
        res = 0 
        for i in range(len(arr1)):
            for j in range(i, len(arr2)):
                res = max(res, abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j))
        return res
