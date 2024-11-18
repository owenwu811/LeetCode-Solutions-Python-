
#1064
#easy

#Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.

 

#Example 1:

#Input: arr = [-10,-5,0,3,7]
#Output: 3
#Explanation: For the given array, arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3, thus the output is 3.



#my own solution using python3:

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        arr.sort()
        res = []
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == mid:
                res.append(mid)
                r = mid - 1
            elif arr[mid] > mid:
                r = mid - 1
            else:
                l = mid + 1
        print(res)
        if not res:
            return -1
        return min(res)
            
