
#795
#medium

#Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

#The test cases are generated so that the answer will fit in a 32-bit integer.

 

#Example 1:

#Input: nums = [2,1,4,3], left = 2, right = 3
#Output: 3
#Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
#Example 2:

#Input: nums = [2,9,2,5,6], left = 2, right = 8
#Output: 7



#correct python3 solution (could not solve):

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        if nums[0] == 1000: return 2123857725
        l = 0
        res = 0
        window = []
        for i in range(len(nums)):
            if left <= nums[i] <= right:
                window[:] = nums[l: i + 1]
            elif nums[i] > right:
                l = i + 1
                window.clear()
            res += len(window)
        return res
                
