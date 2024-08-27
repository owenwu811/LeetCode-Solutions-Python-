
#easy
#60.3% acceptance rate
#485

#Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

#Example 1:

#Input: nums = [1,1,0,1,1,1]
#Output: 3
#Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
#Example 2:

#Input: nums = [1,0,1,1,0,1]
#Output: 2

#my own solution using python3:

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0
        record = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                record += 1
                res = max(res, record)
            elif nums[r] == 0:
                record = 0
            
        return res
