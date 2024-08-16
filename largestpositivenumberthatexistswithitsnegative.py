
#Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

#Return the positive integer k. If there is no such integer, return -1.

#Input: nums = [-1,2,-3,3]
#Output: 3
#Explanation: 3 is the only valid k we can find in the array.


#my own solution using python3:

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort() 
        for i in range(len(nums) -1, -1, -1):
            if -nums[i] in nums:
                return nums[i]
        return -1
