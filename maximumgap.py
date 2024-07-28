
#Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

#You must write an algorithm that runs in linear time and uses linear extra space.

#Input: nums = [3,6,9,1]
#Output: 3
#Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.


#my solution in Python3:

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        if len(nums) < 2: return 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                res = max(res, nums[i] - nums[i - 1])
                print(res)
            elif nums[i - 1] > nums[i]:
                res = max(res, nums[i - 1] - nums[i])
                print(res)
        return res
            
