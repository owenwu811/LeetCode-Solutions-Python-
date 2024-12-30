#1909
#easy

#Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

#The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

 

#Example 1:

#Input: nums = [1,2,10,5,7]
#Output: true
#Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
#[1,2,5,7] is strictly increasing, so return true.


#my own solution using python3:

#my approach: you just keep deleting an element at each iteration and see if it has duplicates or not - may take extra memory

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        clone = nums.copy()
        for i in range(len(nums)):
            del nums[i]
            if nums == sorted(nums) and len(nums) <= len(set(nums)):
                return True
            nums[:] = clone
        return False
