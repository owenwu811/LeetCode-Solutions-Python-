

#325
#medium

#Given an integer array nums and an integer k, return the maximum length of a 
#subarray
# that sums to k. If there is not one, return 0 instead.

 

#Example 1:

#Input: nums = [1,-1,5,-2,3], k = 3
#Output: 4
#Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
#Example 2:

#Input: nums = [-2,-1,2,1], k = 1
#Output: 2
#Explanation: The subarray [-1, 2] sums to 1 and is the longest.



#correct python3 solution (could not solve):

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = dict() 
        ss = 0
        res = 0
        for i, n in enumerate(nums):
            ss += n
            if ss == k:
                res = max(res, i + 1)
            elif (ss - k) in d:
                res = max(res, i - d[ss - k])
            if ss not in d:
                d[ss] = i     
        return res
