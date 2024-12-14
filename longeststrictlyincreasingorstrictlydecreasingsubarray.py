

#3105
#easy

#You are given an array of integers nums. Return the length of the longest 
#subarray
# of nums which is either 
#strictly increasing
# or 
#strictly decreasing
#.

 

#Example 1:

#Input: nums = [1,4,3,3,2]

#Output: 2

#Explanation:

#The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

#The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

#Hence, we return 2.



#my own solution using python3:

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                bigger, smaller = sorted(subarr), sorted(subarr)[::-1]
                if subarr == bigger and len(subarr) == len(set(subarr)):
                    res = max(res, len(subarr))
                    print(subarr)
                if subarr == smaller and len(subarr) == len(set(subarr)):
                    print(subarr)
                    res = max(res, len(subarr))
        return res
