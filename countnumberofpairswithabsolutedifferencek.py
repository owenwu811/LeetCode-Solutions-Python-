
#easy
#84.1% acceptance rate

#Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

#The value of |x| is defined as:

#x if x >= 0.
#-x if x < 0.
 

#Example 1:

#Input: nums = [1,2,2,1], k = 1
#Output: 4
#Explanation: The pairs with an absolute difference of 1 are:
#- [1,2,2,1]
#- [1,2,2,1]
#- [1,2,2,1]
#- [1,2,2,1]


#my own solution using python3 after reading a hint:

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    res += 1
        return res
