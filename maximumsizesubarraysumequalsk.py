

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



#refresher again:

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = dict()
        res = 0
        ss = 0
        for i, n in enumerate(nums):
            ss += n
            if ss == k: #we know that the subarray sum equals k, so everything up to this point is of a valid length, and + 1 for length because we use indicies
                res = max(res, i + 1)
            elif (ss - k) in d: #I'm not entirely sure why we use ss - k vs. k - ss - we cannot use (k - ss) because we track the subarray sum in the dictionary, so when the subarray sum - k equals a previous subarray sum, then we have satisified k from that previous subarray sum's index up to the current subarray sum's index
                res = max(res, i - d[ss - k])
            if ss not in d: #we always track the index that produces the current subarray sum
                d[ss] = i
        return res
