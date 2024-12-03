
#1031
#medium

#Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

#The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

#A subarray is a contiguous part of an array.

 

#Example 1:

#Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
#Output: 20
#Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.


#my own solution using python3:

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        first = []
        second = []
        for i in range(len(nums) - firstLen + 1):
            subarr = nums[i: i + firstLen]
            first.append([i, i + firstLen])
        for j in range(len(nums) - secondLen + 1):
            subarr = nums[j: j + secondLen]
            second.append([j, j + secondLen])
        first.sort()
        second.sort()
        res = 0
        for i in range(len(first)):
            for j in range(len(second)):
                if first[i][0] >= second[j][1] or second[j][0] >= first[i][1]:
                    a = first[i]
                    b = second[j]
                    fmin, fmax = a[0], a[-1]
                    smin, smax = b[0], b[-1]
                    ff = sum(nums[fmin:fmax])
                    ss = sum(nums[smin:smax])
                    res = max(res, ff + ss)
        return res
