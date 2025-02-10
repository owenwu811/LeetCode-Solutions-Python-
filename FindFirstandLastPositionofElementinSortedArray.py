#34. Find First and Last Position of Element in Sorted Array
#Medium
#18.7K
#449
#Companies
#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexity.

 

#Example 1:

#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
#Example 2:

#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]
#Example 3:

#Input: nums = [], target = 0
#Output: [-1,-1]



#my own solution using python3 on 2/9/25:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        return [bisect_left(nums, target), bisect_right(nums, target) - 1]


#My Solution (Python3):

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == target and nums[r] == target:
                return [l, r]
            elif nums[l] < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]

refresher 10/10/23 - my solution (python3):

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < target:
                l += 1
            elif nums[r] > target:
                r -= 1
            else:
                return [l, r]
        return [-1, -1]

        
