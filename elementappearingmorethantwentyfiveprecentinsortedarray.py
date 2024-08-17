
#Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

#1287
#Easy
#61.0%acceptancerate

#Example 1:

#Input: arr = [1,2,2,6,6,6,6,7,10]
#Output: 6
#Example 2:

#Input: arr = [1,1]
#Output: 1

#my own solution using python3:


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = dict()
        for n in arr:
            if n not in d:
                d[n] = 0
            d[n] += 1
        for k in d:
            if d[k] > len(arr) / 4:
                return k
